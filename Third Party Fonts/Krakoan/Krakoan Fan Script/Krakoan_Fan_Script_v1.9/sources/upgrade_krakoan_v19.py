#!/usr/bin/env python3
"""Build Krakoan Fan Script v1.9 with circular numeral tallies."""

from __future__ import annotations

import math
import shutil
from pathlib import Path

from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "work_v16" / "Krakoan_Fan_Script_v1.5"
OUTPUT_DIR = ROOT / "build_v19" / "Krakoan_Fan_Script_v1.9"
SOURCE_FONT = SOURCE_DIR / "KrakoanFanScript-Regular.ttf"
OUTPUT_FONT = OUTPUT_DIR / "KrakoanFanScript-Regular.ttf"
OUTPUT_WOFF = OUTPUT_DIR / "KrakoanFanScript-Regular.woff"

# Numerical-cell geometry. Version 1.8 expands the enclosure and gives its
# frame the same heavy modular presence as the alphabetic glyphs.
NUM_ADVANCE = 720
OUTER_LEFT = 20
OUTER_RIGHT = 620
OUTER_BOTTOM = -100
OUTER_TOP = 850
OUTLINE = 80
FUSED_STEP = (OUTER_RIGHT - OUTER_LEFT) - OUTLINE

TALLY_DIAMETER = 138
TALLY_X = (145, 350)
TALLY_Y = (0, 153, 306, 459, 612)  # bottom to top

DIGIT_NAMES = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)


def rect(pen: TTGlyphPen, x0: int, y0: int, x1: int, y1: int, clockwise: bool = True) -> None:
    """Add a rectangular contour with an explicit winding direction."""
    if clockwise:
        points = ((x0, y0), (x0, y1), (x1, y1), (x1, y0))
    else:
        points = ((x0, y0), (x1, y0), (x1, y1), (x0, y1))
    pen.moveTo(points[0])
    for point in points[1:]:
        pen.lineTo(point)
    pen.closePath()


def circle(pen: TTGlyphPen, x0: int, y0: int, x1: int, y1: int, clockwise: bool = True) -> None:
    """Add a smooth circular contour using eight quadratic segments."""
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    radius = min(x1 - x0, y1 - y0) / 2
    direction = -1 if clockwise else 1
    segment = direction * math.pi / 4
    control_radius = radius / math.cos(segment / 2)

    pen.moveTo((round(cx + radius), round(cy)))
    for index in range(1, 9):
        start_angle = (index - 1) * segment
        end_angle = index * segment
        middle_angle = (start_angle + end_angle) / 2
        control = (
            round(cx + control_radius * math.cos(middle_angle)),
            round(cy + control_radius * math.sin(middle_angle)),
        )
        endpoint = (
            round(cx + radius * math.cos(end_angle)),
            round(cy + radius * math.sin(end_angle)),
        )
        pen.qCurveTo(control, endpoint)
    pen.closePath()


def draw_cell_frame(pen: TTGlyphPen, index: int) -> None:
    left = OUTER_LEFT + index * FUSED_STEP
    right = OUTER_RIGHT + index * FUSED_STEP
    rect(pen, left, OUTER_BOTTOM, right, OUTER_TOP, clockwise=True)
    rect(
        pen,
        left + OUTLINE,
        OUTER_BOTTOM + OUTLINE,
        right - OUTLINE,
        OUTER_TOP - OUTLINE,
        clockwise=False,
    )


def tally_origin(stream_position: int) -> tuple[int, int]:
    """Return a 1-indexed position on the bottom-up serpentine path."""
    zero_based = stream_position - 1
    cell_index, local = divmod(zero_based, 10)
    row, step_in_row = divmod(local, 2)
    # Bottom row runs left-to-right. Each succeeding row reverses direction,
    # forming one continuous snake through the ten positions.
    column = step_in_row if row % 2 == 0 else 1 - step_in_row
    return (
        TALLY_X[column] + cell_index * FUSED_STEP,
        TALLY_Y[row],
    )


def numerical_glyph(
    *,
    whole: int,
    fraction: int | None = None,
) -> tuple[object, int]:
    """Construct an integer cell or a packed/fused decimal enclosure."""
    if not 0 <= whole <= 10:
        raise ValueError(whole)
    if fraction is not None and not 0 <= fraction <= 10:
        raise ValueError(fraction)

    if fraction is None:
        cell_count = 1
        filled_positions = list(range(1, whole + 1))
    elif fraction == 0:
        # A fused empty cell makes x.0 distinct from x0.
        cell_count = 2
        filled_positions = list(range(1, whole + 1))
    else:
        decimal_position = whole + 1
        last_filled_position = decimal_position + fraction
        cell_count = max(1, math.ceil(last_filled_position / 10))
        filled_positions = list(range(1, whole + 1))
        filled_positions.extend(range(decimal_position + 1, last_filled_position + 1))

    pen = TTGlyphPen(None)
    for cell_index in range(cell_count):
        draw_cell_frame(pen, cell_index)
    for position in filled_positions:
        x, y = tally_origin(position)
        circle(
            pen,
            x,
            y,
            x + TALLY_DIAMETER,
            y + TALLY_DIAMETER,
            clockwise=True,
        )

    right = OUTER_RIGHT + (cell_count - 1) * FUSED_STEP
    advance = right + (NUM_ADVANCE - OUTER_RIGHT)
    return pen.glyph(), advance


def blank_period_glyph() -> object:
    return TTGlyphPen(None).glyph()


def set_version(font: TTFont, version: str) -> None:
    font["head"].fontRevision = float(version)
    replacements = {
        3: f"Krakoan Fan Script {version}00",
        5: f"Version {version}00",
    }
    for record in font["name"].names:
        if record.nameID not in replacements:
            continue
        encoding = record.getEncoding()
        record.string = replacements[record.nameID].encode(encoding)


def add_numerals(font: TTFont) -> None:
    glyph_order = list(font.getGlyphOrder())
    glyf = font["glyf"]
    hmtx = font["hmtx"]

    additions: list[tuple[str, object, int]] = []
    for value, glyph_name in enumerate(DIGIT_NAMES):
        glyph, advance = numerical_glyph(whole=value)
        additions.append((glyph_name, glyph, advance))

    ten_glyph, ten_advance = numerical_glyph(whole=10)
    additions.append(("ten", ten_glyph, ten_advance))
    additions.append(("period", blank_period_glyph(), 0))

    decimal_names: dict[tuple[int, int], str] = {}
    for whole in range(11):
        for fraction in range(11):
            name = f"num{whole}dec{fraction}"
            glyph, advance = numerical_glyph(whole=whole, fraction=fraction)
            additions.append((name, glyph, advance))
            decimal_names[(whole, fraction)] = name

    for name, glyph, advance in additions:
        if name not in glyph_order:
            glyph_order.append(name)
        glyf[name] = glyph
        hmtx.metrics[name] = (advance, 0)

    font.setGlyphOrder(glyph_order)

    # Add standard digit/period mappings and stable PUA access for the ten cell
    # and decimal composites.
    for cmap_table in font["cmap"].tables:
        if not cmap_table.isUnicode():
            continue
        cmap_table.cmap[0x002E] = "period"
        for value, glyph_name in enumerate(DIGIT_NAMES):
            cmap_table.cmap[0x0030 + value] = glyph_name
        cmap_table.cmap[0xE200] = "ten"
        pua = 0xE300
        for whole in range(11):
            for fraction in range(11):
                cmap_table.cmap[pua] = decimal_names[(whole, fraction)]
                pua += 1


def feature_source() -> str:
    lines = [
        "languagesystem DFLT dflt;",
        "languagesystem latn dflt;",
        "",
        "lookup COMPOUND_LETTERS {",
        "  sub C H by CH;",
        "  sub S T by ST;",
        "  sub T H by TH;",
        "} COMPOUND_LETTERS;",
        "",
        "lookup TEN_CELL {",
        "  sub one zero by ten;",
        "} TEN_CELL;",
        "",
        "lookup DECIMAL_CELLS {",
    ]

    number_tokens = list(DIGIT_NAMES) + ["ten"]
    for whole, left in enumerate(number_tokens):
        for fraction, right in enumerate(number_tokens):
            lines.append(f"  sub {left} period {right} by num{whole}dec{fraction};")
    lines.extend(
        [
            "} DECIMAL_CELLS;",
            "",
            "lookup ECHO_CUTS {",
        ]
    )
    for name in [chr(code) for code in range(ord("A"), ord("Z") + 1)] + ["CH", "ST", "TH"]:
        lines.append(f"  sub {name} {name} by {name}.echo;")
    lines.extend(
        [
            "} ECHO_CUTS;",
            "",
            "feature liga {",
            "  lookup COMPOUND_LETTERS;",
            "  lookup TEN_CELL;",
            "  lookup DECIMAL_CELLS;",
            "  lookup ECHO_CUTS;",
            "} liga;",
            "",
        ]
    )
    return "\n".join(lines)


def build_font() -> None:
    font = TTFont(SOURCE_FONT)
    add_numerals(font)
    addOpenTypeFeaturesFromString(font, feature_source())
    set_version(font, "1.9")

    # Allow the larger numerical cells to define the global bounds.
    font.recalcBBoxes = True
    font.recalcTimestamp = False
    font.save(OUTPUT_FONT)

    web_font = TTFont(OUTPUT_FONT)
    web_font.flavor = "woff"
    web_font.save(OUTPUT_WOFF)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size, layout_engine=ImageFont.Layout.RAQM)


def render_krakoan(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, size: int, fill: str = "#050505") -> None:
    draw.text(xy, text, font=font(str(OUTPUT_FONT), size), fill=fill, features=["liga"])


def update_main_specimen() -> None:
    image = Image.open(SOURCE_DIR / "KrakoanFanScript-Specimen.png").convert("RGB")
    draw = ImageDraw.Draw(image)
    background = image.getpixel((5, 5))
    sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    draw.rectangle((75, 136, 1650, 185), fill=background)
    draw.text(
        (88, 140),
        "A–Z · compound letters · paired cartouches · Echo-Cut doubles · tally numerals",
        font=font(sans, 29),
        fill="#4f4f4f",
    )
    footer_top = image.height - 115
    draw.rectangle((70, footer_top, image.width - 70, image.height - 20), fill=background)
    draw.text(
        (87, footer_top + 23),
        "Unofficial fan-made typeface · experimental v1.9",
        font=font(sans, 28),
        fill="#8a8a8a",
    )
    image.save(OUTPUT_DIR / "KrakoanFanScript-Specimen.png")


def numerals_specimen() -> None:
    width, height = 1800, 1580
    background = "#f6f3ed"
    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)
    sans_regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    sans_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    bold = lambda size: font(sans_bold, size)
    regular = lambda size: font(sans_regular, size)

    draw.text((88, 60), "KRAKOAN NUMERICAL CELLS", font=bold(64), fill="#080808")
    draw.text(
        (90, 137),
        "0–10 · circular serpentine tallies · heavy fused-border decimals",
        font=regular(30),
        fill="#555555",
    )

    labels = [str(value) for value in range(11)]
    card_w, card_h, gap = 250, 335, 28
    start_x, row_y = 88, 220
    for index, label in enumerate(labels):
        row, column = divmod(index, 6)
        x = start_x + column * (card_w + gap)
        y = row_y + row * (card_h + 30)
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=14, fill="#ffffff", outline="#d8d1c6", width=2)
        draw.text((x + 20, y + 15), label, font=bold(28), fill="#5b5b5b")
        sample = label
        sample_font = font(str(OUTPUT_FONT), 140)
        bbox = draw.textbbox((0, 0), sample, font=sample_font, features=["liga"])
        sw = bbox[2] - bbox[0]
        sh = bbox[3] - bbox[1]
        draw.text(
            (x + (card_w - sw) / 2, y + 95 + (150 - sh) / 2 - bbox[1]),
            sample,
            font=sample_font,
            fill="#050505",
            features=["liga"],
        )

    examples_top = 975
    draw.text((88, examples_top), "DECIMAL AND COMPOUND EXAMPLES", font=bold(30), fill="#555555")
    examples = [
        ("710", "7 followed by a full ten-circle cell"),
        ("70", "seven followed by an empty zero cell"),
        ("4.5", "decimal interval contained in one cell"),
        ("6.9", "six, a blank interval, then nine across a fused border"),
        ("7.23", "normal spacing begins the next fractional unit"),
        ("74.20", "packed decimal followed by a significant zero"),
    ]
    box_w, box_h = 520, 220
    for index, (sample, explanation) in enumerate(examples):
        row, column = divmod(index, 3)
        x = 88 + column * 560
        y = examples_top + 65 + row * 250
        draw.rounded_rectangle((x, y, x + box_w, y + box_h), radius=12, fill="#ffffff", outline="#d8d1c6", width=2)
        draw.text((x + 20, y + 14), sample, font=bold(26), fill="#a43716")
        draw.text((x + 20, y + 55), explanation, font=regular(18), fill="#555555")
        sample_font = font(str(OUTPUT_FONT), 72)
        bbox = draw.textbbox((0, 0), sample, font=sample_font, features=["liga"])
        sh = bbox[3] - bbox[1]
        draw.text(
            (x + 20, y + 115 + (80 - sh) / 2 - bbox[1]),
            sample,
            font=sample_font,
            fill="#050505",
            features=["liga"],
        )

    image.save(OUTPUT_DIR / "KrakoanFanScript-Numerals.png")


def prepare_output() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    shutil.copy2(SOURCE_DIR / "KrakoanFanScript-EchoCuts.png", OUTPUT_DIR)
    shutil.copy2(SOURCE_DIR / "krakoan-fan-script.css", OUTPUT_DIR)
    shutil.copy2(ROOT / "README_v19.md", OUTPUT_DIR / "README.md")
    sources = OUTPUT_DIR / "sources"
    sources.mkdir()
    shutil.copy2(Path(__file__), sources / "upgrade_krakoan_v19.py")


def main() -> None:
    prepare_output()
    build_font()
    update_main_specimen()
    numerals_specimen()
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()
