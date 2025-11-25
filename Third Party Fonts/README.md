# Third Party Fonts

A curated collection of open-source and licensed fonts optimized for World Anvil project styling and typography. This folder contains font files, CSS integration guides, and helper scripts for easy implementation.

## Overview

These fonts are sourced from various third-party creators and are included to support the customization and styling of World Anvil projects, particularly **The Seven Seals Legendarium**. Each font includes documentation on licensing, usage rights, and integration methods.

## Quick Start

### For World Anvil Integration
1. Navigate to the font you want to use
2. Look for CSS invoke files (typically named `*WA Invoke.css` or similar)
3. Copy the CSS into your World Anvil project's custom CSS section
4. Apply the font family name to your desired elements
5. Test in World Anvil's preview before publishing

### World Anvil CSS Files Available
The following fonts include pre-configured CSS for World Anvil integration:
- BluuNext Bold Italics WA Invoke.css
- Boecklins WA Invoke.css
- Davison Art Nouveau Regular WA Invoke.css
- Floral Caps Nouveau WA Invoke.css
- Hyperscript WA Invoke.css
- JetBrains Regular WA Invoke.css
- Jugendstil Ornamente WA Invoke.css
- Jacquard 24 CSS (World Anvil)
- Jersey 25 CSS (World Anvil)

## Font Categories

### Display & Decorative Fonts
- **Adinkra Alphabet** - Symbolic/cultural alphabet font with FontForge customization scripts
- **Boecklins Universe** - Stylized decorative font with elegant curves
- **Davison Art Nouveau** - Art Nouveau aesthetic for headers and accents
- **Dumbledor** - Fantasy-inspired display font
- **Final Fantasy** - Game-inspired typography
- **Floral Caps Nouveau** - Ornamental caps for decorative headers
- **Jugendstil Ornamente** - Ornamental decorative elements and flourishes

### Display & Heading Fonts
- **BluuNext** - Modern sans-serif with bold and italic variants
- **Jacquard 24** - Contemporary display font
- **Jersey 25** - Modern display typography
- **Outward Font** - Bold display/heading font

### Serif & Body Text Fonts
- **Gutenberg Bible Font** - Classical serif with historical aesthetic
- **Isabella Font** - Elegant serif option
- **Optimus Princeps** - Classical Roman typography
- **The Middle Ages Font** - Medieval-themed serif

### Specialty & Monospace Fonts
- **HyperScript** - Modern decorative/technical font
- **JetBrains** - Professional monospace font for code/technical content
- **Patriot** - Specialty font for unique applications

### Other Fonts
- **Lithops** - Specialty typography resource
- **Barber** - Display font option

## Complete Font List

| Font Name | Category | WA CSS | Status |
|-----------|----------|--------|--------|
| Adinkra Alphabet | Symbolic/Decorative | ✓ | With scripts |
| Barber | Display | — | Base files |
| BluuNext | Display/Heading | ✓ | Bold Italics |
| Boecklins Universe | Decorative | ✓ | Serif style |
| Davison Art Nouveau | Decorative | ✓ | With example |
| Dumbledor | Display | — | Base files |
| Final Fantasy | Display | — | Tag set |
| Floral Caps Nouveau | Decorative | ✓ | Caps only |
| Gutenberg Bible | Serif | — | Base files |
| HyperScript | Specialty | ✓ | Technical |
| Isabella | Serif | ✓ | Elegant |
| Jacquard 24 | Display | ✓ | Modern |
| Jersey 25 | Display | ✓ | Contemporary |
| JetBrains | Monospace | ✓ | Professional |
| Jugendstil Ornamente | Decorative | ✓ | With preview |
| Lithops | Specialty | — | Base files |
| Optimus Princeps | Serif | — | Classical |
| Outward Font | Display | — | Base files |
| Patriot | Specialty | — | Base files |
| The Middle Ages | Serif | — | Medieval |

## License & Attribution

**Important:** Unless otherwise stated, these fonts are **NOT** owned by Khali A. Crawford.

Each font folder contains:
- **LICENSE** or **LICENSE.md** - Specific license terms for that font
- **README** or **README.md** - Usage instructions and attribution requirements

### Your Responsibilities
When using these fonts in your projects:
1. **Review the individual license** in each font's folder
2. **Provide proper attribution** as specified by the font creator
3. **Comply with usage restrictions** (commercial/non-commercial limitations)
4. **Respect the license type** (OFL, MIT, CC0, proprietary, etc.)

### Creative Commons License Note
If you use fonts from this repository in World Anvil projects distributed under CC BY-NC-SA 4.0, ensure the fonts' licenses are compatible with non-commercial sharing and attribution requirements.

## Helper Scripts & Customization

Some font folders include build and customization scripts:

### Adinkra Alphabet
- `add_macrons.pe` - FontForge script for adding macron marks
- `add_macrons_paths.pe` - Alternative macro script variant
- Refer to the folder's README for detailed usage instructions

## Adding New Fonts

To add new fonts to this collection:

1. Create a new folder with the font name
2. Add the font files (.ttf, .otf, etc.)
3. Include the font's LICENSE file
4. Create a README.md with:
   - Font description and usage
   - Attribution and creator information
   - License terms
   - Any special notes for World Anvil integration
5. If creating WA CSS, name it following the pattern: `[FontName] WA Invoke.css`
6. Update this README with the new font entry

## Related Resources

For more information on World Anvil styling:
- See `CSS Styling for World Anvil Projects/` for complete styling frameworks
- Check `PreFab CSS WA Elements/` for reusable component templates
- Review `COPILOT.md` for overall repository structure and usage

---

*Last Updated: November 2025*
*Created & Maintained by Khali A. Crawford*
*Licensed under CC BY-NC-SA 4.0 International*
