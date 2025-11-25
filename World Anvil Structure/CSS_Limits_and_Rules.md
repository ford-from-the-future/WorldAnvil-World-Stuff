# World Anvil CSS Limits and Rules

## What's CSS?

Websites are built using HTML and CSS, two coding languages that tell your web browser everything it needs to know in order to display a website. HTML tells the browser about the structure and contents of the website (on World Anvil, BBCode is like simplified HTML!), while CSS is all about defining what each element should look like.

As an example, the BBCode `[h1]Title[/h1]` tells the browser that "Title" is a first-level header. Then, CSS can tell the browser how big should this title be, what font to use, if it should be bold or underlined, etc. To do that, CSS uses **selectors**, i.e. keywords that refer to specific elements. For example, to make a first-level header red, you would use the `h1` selector.

---

## Resources to learn more

The above is only a very basic explanation. If you aren't familiar with CSS, these resources might be useful:

- **Codex CSS guides** - Community-written and maintained guides that include selectors for various elements in your world
- **W3Schools' CSS course** - A good starting point to learn CSS fundamentals

The rest of this guide assumes you have at least beginner CSS skills.

---

## What can you change with CSS?

You can target almost everything on your world. The exact rules are as follows:

### ✅ What you CAN modify

- **General rule**: You can modify anything that's under the `.user-css` selector (or that includes `user-css`, such as `.user-css-extended`)
- Most visual elements within articles and world pages
- Colors, fonts, spacing, layouts, and styling of content areas
- Widget styling (family trees, calendars, tables, tabs, etc.)
- Custom containers and sections

### ❌ What you CANNOT modify

You **may not alter in any way** the following elements, even if they are under a `user-css` selector:

- **Top menu bar** - Including the World Anvil logo and navigation links
- **Global World Anvil footer** - The footer at the very bottom of every article
- **Social media buttons** - Patreon, Ko-fi, Twitter, Reddit, etc.
- **World Anvil social buttons** - Article buttons, "follow world" button, etc.
  - *Note: You can disable community features in the world configuration page*

### ⚠️ What you CAN modify, but with restrictions

You may edit the following elements, **as long as you don't hide them or significantly reduce their readability and usability**:

- **Metadata section** - At the bottom of all articles
- **Comments section** - Can be disabled entirely in world configuration

---

## Important compliance notes

⚠️ **Breaking any of these rules is against World Anvil's Terms of Service**

Repeatedly violating these rules might result in:
- Your CSS being disabled
- Your account being blocked

### If you're unsure

If you're not sure whether your CSS breaks the rules above, contact World Anvil support at **contact@worldanvil.com** to check before applying it to your world.

---

## Best practices for CSS modification

1. **Test your CSS** - Always preview your changes before publishing
2. **Keep elements visible** - Never hide required UI elements with `display: none`
3. **Maintain readability** - Ensure text remains legible and interactive elements are usable
4. **Use user-css selectors** - Always target `.user-css` or `.user-css-*` classes when possible
5. **Document your changes** - Comment your CSS code for future reference and maintenance
6. **Version control** - Keep backups of your CSS versions in case you need to revert

---

## CSS selector hierarchy on World Anvil

The main selectors you'll work with include:

| Selector | Target |
|----------|--------|
| `.user-css` | Main world content area |
| `.user-css-extended` | Extended page layouts |
| `.user-css-presentation` | Presentation/slideshow mode |
| `.user-css-map-sidebar` | Map view sidebars |
| `.user-css-rpgblock` | RPG block/statblock elements |

### Common elements to target

```css
/* Text and headings */
.user-css h1 { }
.user-css h2 { }
.user-css p { }
.user-css a { }

/* Content containers */
.user-css .article-content { }
.user-css .article-title { }
.user-css .article-panel { }

/* Sidebars */
.user-css .article-content .col-md-4 { }

/* Special elements */
.user-css .blockquote { }
.user-css .table { }
.user-css .timeline { }
.user-css .rhea-family-tree { }
```

---

## Common CSS mistakes to avoid

❌ **Don't hide required elements:**
```css
/* BAD - This violates ToS */
.top-navigation { display: none; }
.world-anvil-footer { display: none; }
```

❌ **Don't make content unreadable:**
```css
/* BAD - Text becomes invisible */
.user-css p {
    color: white;
    background: white;
}
```

❌ **Don't disable interaction:**
```css
/* BAD - Buttons become unusable */
.user-css button {
    pointer-events: none;
    opacity: 0.1;
}
```

✅ **DO style within constraints:**
```css
/* GOOD - Styling without hiding or breaking functionality */
.user-css h1 {
    color: gold;
    font-family: Georgia, serif;
    font-size: 3em;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.user-css p {
    color: #333;
    line-height: 1.8;
    font-size: 1.1em;
}
```

---

## Troubleshooting CSS issues

### "My CSS isn't working! What can I do?"

**Step 1: Check selector specificity**
- Is your selector targeting the right element?
- Use browser DevTools (F12) to inspect elements and find correct selectors

**Step 2: Verify you're using .user-css**
- Most CSS must target elements under `.user-css` or `.user-css-*`
- Check if your selector includes the right parent class

**Step 3: Check for !important**
- World Anvil's default styles may override yours
- Use `!important` flag to force your styles (use sparingly)

**Step 4: Clear cache**
- Refresh with Ctrl+Shift+R or Cmd+Shift+R to hard refresh and clear browser cache
- CSS changes can take a few minutes to propagate

**Step 5: Use browser DevTools**
- Right-click → Inspect Element
- Check what styles are being applied
- Look for conflicting rules
- Check that your CSS is being loaded

**Step 6: Test in isolation**
- Create a minimal test case
- Add one rule at a time to identify conflicts

### If you still need help

- Consult the **Codex CSS guides** for community expertise
- Email **contact@worldanvil.com** if you suspect a violation or need clarification

---

## Additional resources

- [World Anvil Documentation](https://www.worldanvil.com)
- [CSS Basics Guide](https://www.w3schools.com/css/)
- [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- World Anvil Community Forums - CSS Support Section
