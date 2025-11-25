#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/**
 * World Anvil CSS Compliance Checker
 * Validates CSS files against World Anvil Terms of Service
 * Reference: World Anvil Structure/CSS_Limits_and_Rules.md
 */

const PROHIBITED_SELECTORS = [
  'top-navigation',
  'world-anvil-footer',
  'global-footer',
  '.wa-footer',
  '.patreon',
  '.kofi',
  '.twitter',
  '.reddit',
  '.follow-world',
  '.article-button',
];

const PROHIBITED_PATTERNS = [
  /\.top.*navigation/i,
  /\.global.*footer/i,
  /\.world-anvil-footer/i,
  /social.*button/i,
  /patreon|kofi|twitter|reddit/i,
];

const VIOLATIONS = {
  nonUserCss: [],
  hiddenElements: [],
  disabledInteraction: [],
  prohibitedSelectors: [],
  warnings: [],
};

let totalIssues = 0;

/**
 * Get changed CSS files from git
 */
function getChangedFiles() {
  try {
    let files = [];
    
    // Check if this is a pull request
    if (process.env.GITHUB_EVENT_NAME === 'pull_request') {
      const baseRef = process.env.GITHUB_BASE_REF || 'main';
      const headRef = process.env.GITHUB_HEAD_REF || 'HEAD';
      const output = execSync(`git diff --name-only ${baseRef}...${headRef}`, { encoding: 'utf8' });
      files = output.trim().split('\n').filter(f => f.endsWith('.css'));
    } else {
      // For push events, check the commit
      const output = execSync('git diff-tree --no-commit-id --name-only -r HEAD', { encoding: 'utf8' });
      files = output.trim().split('\n').filter(f => f.endsWith('.css'));
    }
    
    return files.filter(f => f && fs.existsSync(f));
  } catch (error) {
    console.error('Error getting changed files:', error.message);
    return [];
  }
}

/**
 * Check if selector is likely under .user-css
 */
function hasUserCssContext(selector) {
  return /\.user-css/i.test(selector) || selector.startsWith(':');
}

/**
 * Check for hidden elements
 */
function checkForHiddenElements(rule, filePath, lineNum) {
  const displayNone = rule.includes('display') && rule.includes('none');
  const visibility = rule.includes('visibility') && rule.includes('hidden');
  const opacity = /opacity\s*:\s*0[^.]/.test(rule);
  
  // Allow display: none for internal elements (tabs, collapse, etc.)
  const isInternalElement = /\.(well|collapse|collapsing|card|spoiler-content|hidden-comment)/.test(rule);
  
  if ((displayNone || visibility || opacity) && !isInternalElement) {
    VIOLATIONS.hiddenElements.push({
      file: filePath,
      line: lineNum,
      rule: rule.substring(0, 100),
      reason: 'Element appears to be hidden - may violate ToS if hiding required UI'
    });
    totalIssues++;
  }
}

/**
 * Check for disabled interactions
 */
function checkForDisabledInteraction(rule, filePath, lineNum) {
  const pointerEvents = /pointer-events\s*:\s*none/i.test(rule);
  const userSelect = /user-select\s*:\s*none/i.test(rule);
  const disabled = /cursor\s*:\s*not-allowed/.test(rule);
  
  if (pointerEvents || userSelect) {
    VIOLATIONS.disabledInteraction.push({
      file: filePath,
      line: lineNum,
      rule: rule.substring(0, 100),
      reason: 'Property appears to disable user interaction'
    });
    totalIssues++;
  }
}

/**
 * Check for prohibited selectors
 */
function checkForProhibitedSelectors(selector, filePath, lineNum) {
  for (const prohibited of PROHIBITED_PATTERNS) {
    if (prohibited.test(selector)) {
      VIOLATIONS.prohibitedSelectors.push({
        file: filePath,
        line: lineNum,
        selector: selector,
        reason: 'Targeting prohibited World Anvil UI element'
      });
      totalIssues++;
      break;
    }
  }
}

/**
 * Parse and check CSS file
 */
function checkCSSFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  
  let inRule = false;
  let currentSelector = '';
  let currentRule = '';
  let ruleStartLine = 0;
  
  lines.forEach((line, idx) => {
    const lineNum = idx + 1;
    const trimmed = line.trim();
    
    // Skip comments
    if (trimmed.startsWith('/*') || trimmed.startsWith('*') || trimmed.startsWith('//')) {
      return;
    }
    
    // Opening brace - start of rule
    if (trimmed.includes('{')) {
      inRule = true;
      ruleStartLine = lineNum;
      currentSelector = trimmed.substring(0, trimmed.indexOf('{')).trim();
      
      // Check selector compliance
      if (!hasUserCssContext(currentSelector)) {
        VIOLATIONS.nonUserCss.push({
          file: filePath,
          line: lineNum,
          selector: currentSelector,
          reason: 'Selector does not include .user-css context'
        });
        totalIssues++;
      }
      
      checkForProhibitedSelectors(currentSelector, filePath, lineNum);
      return;
    }
    
    // Closing brace - end of rule
    if (trimmed.includes('}')) {
      inRule = false;
      
      // Check the complete rule
      checkForHiddenElements(currentRule, filePath, ruleStartLine);
      checkForDisabledInteraction(currentRule, filePath, ruleStartLine);
      
      currentRule = '';
      currentSelector = '';
      return;
    }
    
    // Inside rule - accumulate properties
    if (inRule) {
      currentRule += ' ' + trimmed;
    }
  });
}

/**
 * Print report
 */
function printReport() {
  console.log('\n═══════════════════════════════════════════════════════════');
  console.log('  WORLD ANVIL CSS COMPLIANCE CHECK');
  console.log('═══════════════════════════════════════════════════════════\n');
  
  if (totalIssues === 0) {
    console.log('✅ All CSS files pass compliance checks!\n');
    return true;
  }
  
  if (VIOLATIONS.prohibitedSelectors.length > 0) {
    console.log('❌ PROHIBITED SELECTORS DETECTED:');
    VIOLATIONS.prohibitedSelectors.forEach(v => {
      console.log(`   📄 ${v.file}:${v.line}`);
      console.log(`      Selector: ${v.selector}`);
      console.log(`      Reason: ${v.reason}\n`);
    });
  }
  
  if (VIOLATIONS.nonUserCss.length > 0) {
    console.log('⚠️  NON .user-css SELECTORS:');
    VIOLATIONS.nonUserCss.forEach(v => {
      console.log(`   📄 ${v.file}:${v.line}`);
      console.log(`      Selector: ${v.selector}`);
      console.log(`      Reason: ${v.reason}\n`);
    });
  }
  
  if (VIOLATIONS.hiddenElements.length > 0) {
    console.log('⚠️  POTENTIALLY HIDDEN ELEMENTS:');
    VIOLATIONS.hiddenElements.forEach(v => {
      console.log(`   📄 ${v.file}:${v.line}`);
      console.log(`      Rule: ${v.rule}...`);
      console.log(`      Reason: ${v.reason}\n`);
    });
  }
  
  if (VIOLATIONS.disabledInteraction.length > 0) {
    console.log('⚠️  POTENTIALLY DISABLED INTERACTIONS:');
    VIOLATIONS.disabledInteraction.forEach(v => {
      console.log(`   📄 ${v.file}:${v.line}`);
      console.log(`      Rule: ${v.rule}...`);
      console.log(`      Reason: ${v.reason}\n`);
    });
  }
  
  console.log('═══════════════════════════════════════════════════════════');
  console.log(`Total Issues Found: ${totalIssues}`);
  console.log('═══════════════════════════════════════════════════════════\n');
  
  console.log('📖 For guidance, see: World Anvil Structure/CSS_Limits_and_Rules.md');
  console.log('📧 Questions? Contact: contact@worldanvil.com\n');
  
  return false;
}

/**
 * Main execution
 */
function main() {
  console.log('\n🔍 Starting CSS Compliance Check...\n');
  
  const files = getChangedFiles();
  
  if (files.length === 0) {
    console.log('ℹ️  No CSS files changed in this commit.\n');
    return true;
  }
  
  console.log(`Found ${files.length} CSS file(s) to check:\n`);
  files.forEach(f => console.log(`  • ${f}`));
  console.log();
  
  files.forEach(file => {
    console.log(`Checking: ${file}`);
    checkCSSFile(file);
  });
  
  const passed = printReport();
  
  if (!passed) {
    process.exit(1);
  }
}

main();
