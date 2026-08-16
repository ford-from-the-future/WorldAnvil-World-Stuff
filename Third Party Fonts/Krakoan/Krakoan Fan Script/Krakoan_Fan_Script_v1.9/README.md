# Krakoan Fan Script v1.9

An unofficial traced display font based on the supplied Krakoan alphabet chart and the experimental orthographic rules developed for this fan script.

## Included files

- `KrakoanFanScript-Regular.ttf` — installable TrueType font
- `KrakoanFanScript-Regular.woff` — webfont
- `KrakoanFanScript-Specimen.png` — complete base character sheet
- `KrakoanFanScript-EchoCuts.png` — normal-versus-doubled comparison sheet
- `KrakoanFanScript-Numerals.png` — numerical-cell and decimal specimen
- `krakoan-fan-script.css` — webfont declaration
- `sources/upgrade_krakoan_v19.py` — reproducible v1.9 build source

## Character support

- A–Z and a–z, with identical uppercase and lowercase forms
- Automatic CH, ST, and TH compound-letter ligatures
- Opening `[` and closing `]` cartouche marks
- Automatic Echo-Cut contractions for doubled A–Z, CH, ST, and TH
- Heavy-framed numerical cells for ASCII `0` through `9`
- Automatic single-cell `10`
- Automatic packed and fused decimal constructions

## Circular serpentine numerals

Each numerical cell is a large block-like rectangular enclosure containing ten possible circular tally positions arranged as two columns of five rows. The heavy frame uses a stroke weight comparable to the principal bars and modules of the Krakoan alphabet, while the circular tallies echo the script's frequent circular terminals and counters.

The circles follow one continuous bottom-up serpentine path:

1. The bottom row is filled left-to-right.
2. The next row is filled right-to-left.
3. Direction reverses again on every successive row.
4. The top row is therefore filled left-to-right.

An empty cell represents `0`. One through nine filled circles represent `1` through `9`, and a fully filled cell represents `10`. Typing `10` automatically forms the complete ten-circle cell.

Adjacent ordinary numerical cells retain approximately the same spacing as Krakoan letters. They do not touch. Only an overflowing decimal tally creates a fused construction in which the two enlarged frames share one heavy vertical wall.

Type decimals normally with an ASCII period:

- `4.5` fits inside one numerical cell.
- `6.9` places six filled circles before the decimal interval, leaves the seventh position empty, fills the final three positions of the first cell, and continues the remaining six fractional positions through a fused second cell.
- `7.23` forms a packed `7.2` cell followed by a normally spaced `3` cell.
- `74.20` forms `7`, packed `4.2`, and an empty `0` cell.

The period glyph is intentionally invisible when it does not participate in a supported decimal ligature. Applications must keep the standard `liga` feature enabled for automatic `10`, compound letters, Echo Cuts, and decimal construction.

The direct Private Use mapping for the ten-circle cell is U+E200. Decimal composites occupy U+E300 through U+E378 in row-major order for whole values `0–10` and fractional values `0–10`.

## Dense Echo Cuts

Echo-Cut doubled letters use four through six shallow triangular notches along logical right-hand edges. Compact modules receive four bites, medium bodies five, and tall bodies six. Letters with repeated aligned modules distribute two bites per module. The reduced notch depth keeps the ordinary letter silhouette dominant.

`SUMMERS` therefore displays as six character cells, with `MM` replaced by one serrated M. `CHCH`, `STST`, and `THTH` likewise collapse after compound-letter substitution.

Direct Echo-Cut Private Use mappings run from U+E100 through U+E11C in this order: A–Z, CH, ST, TH.

## Notice

This is an unofficial fan-made typeface. Krakoan, Marvel, and related characters and marks belong to their respective owners. No affiliation or endorsement is claimed. Use it only where you have the necessary rights and permissions.
