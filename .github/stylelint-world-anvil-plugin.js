#!/usr/bin/env node

/**
 * World Anvil CSS Compliance Stylelint Plugin
 * Enforces World Anvil Terms of Service rules during formatting
 * Reference: World Anvil Structure/CSS_Limits_and_Rules.md
 */

const stylelint = require('stylelint');

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

const ruleName = 'world-anvil-compliance/no-prohibited-selectors';
const messages = stylelint.utils.ruleMessages(ruleName, {
  prohibited: (selector) =>
    `Selector "${selector}" is prohibited by World Anvil Terms of Service. You cannot target top-navigation, footer, social buttons, or external UI elements.`,
  nonUserCss: (selector) =>
    `Selector "${selector}" does not appear to be under .user-css. World Anvil only allows styling within .user-css namespace.`,
  hidingElements: (selector) =>
    `Selector "${selector}" appears to hide UI elements. This violates World Anvil ToS - required UI elements must remain visible.`,
  disablingInteraction: (selector) =>
    `Selector "${selector}" appears to disable interaction. This violates World Anvil ToS - interactive elements must remain functional.`,
});

function checkSelector(selector) {
  // Pseudo-elements and pseudo-classes starting with : are allowed
  if (selector.startsWith(':')) {
    return null;
  }

  // Check prohibited selectors
  for (const prohibited of PROHIBITED_SELECTORS) {
    if (selector.includes(prohibited)) {
      return messages.prohibited(selector);
    }
  }

  // Check prohibited patterns
  for (const pattern of PROHIBITED_PATTERNS) {
    if (pattern.test(selector)) {
      return messages.prohibited(selector);
    }
  }

  // Check if selector is under .user-css (required for most styling)
  // Some exceptions: @media, @keyframes, etc.
  if (!selector.includes('.user-css') && !selector.startsWith('@')) {
    // Allow some global selectors that don't need user-css context
    const allowedGlobal = [
      'body',
      'html',
      ':root',
      '::placeholder',
      '::selection',
      '::before',
      '::after',
    ];

    const baseSelector = selector.split(/[>+~\s]/)[0];
    const isAllowed = allowedGlobal.some((g) =>
      baseSelector === g || baseSelector.startsWith(g)
    );

    if (!isAllowed && !selector.includes('.user-css')) {
      // Warn but don't fail - some selectors may be intentional
      return messages.nonUserCss(selector);
    }
  }

  return null;
}

function checkDeclaration(decl) {
  const prop = decl.prop.toLowerCase();
  const value = decl.value.toLowerCase();

  // Check for display: none
  if (
    prop === 'display' &&
    value === 'none' &&
    !decl.parent.selector.includes('.collapse') &&
    !decl.parent.selector.includes('.hidden-comment')
  ) {
    return messages.hidingElements(decl.parent.selector);
  }

  // Check for visibility: hidden
  if (prop === 'visibility' && value === 'hidden') {
    return messages.hidingElements(decl.parent.selector);
  }

  // Check for opacity: 0
  if (prop === 'opacity' && value === '0') {
    return messages.hidingElements(decl.parent.selector);
  }

  // Check for pointer-events: none
  if (prop === 'pointer-events' && value === 'none') {
    return messages.disablingInteraction(decl.parent.selector);
  }

  return null;
}

module.exports = stylelint.createPlugin(ruleName, function (primaryOptions) {
  return function (postcssRoot, postcssResult) {
    const validOptions = stylelint.utils.validateOptions(postcssResult, ruleName, {
      actual: primaryOptions,
      possible: [true, false],
      optional: true,
    });

    if (!validOptions) {
      return;
    }

    postcssRoot.walkRules((rule) => {
      // Check selector compliance
      const selectorError = checkSelector(rule.selector);
      if (selectorError) {
        stylelint.utils.report({
          message: selectorError,
          node: rule,
          result: postcssResult,
          ruleName,
        });
      }

      // Check declarations in this rule
      rule.walkDecls((decl) => {
        const declError = checkDeclaration(decl);
        if (declError) {
          stylelint.utils.report({
            message: declError,
            node: decl,
            result: postcssResult,
            ruleName,
          });
        }
      });
    });
  };
});

module.exports.ruleName = ruleName;
module.exports.messages = messages;
