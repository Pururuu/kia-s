#!/usr/bin/env python3
"""Composite bold headers onto the generated diagrams -> finished picture cards
(1280x720), matching the reference explainer style: golden bg, black bold
header at top, hand-drawn labeled diagram below."""
import os, csv
from PIL import Image, ImageDraw, ImageFont

FONT = "fonts/LuckiestGuy.ttf"
W, H = 1280, 720
BLACK = (30, 26, 20)
SRC = "picture_cards/diagrams"
OUT = "picture_cards"

# diagram file -> (header text, suggested audio timestamp in the narration)
CARDS = [
    ("atoms.png",      "ATOMS ARE REAL",       "2:18"),
    ("light_both.png", "LIGHT IS BOTH",        "2:34"),
    ("gravity.png",    "MASS BENDS SPACE",     "2:44"),
    ("emc2.png",       "MASS BECOMES ENERGY",  "3:04"),
    ("eclipse.png",    "STARLIGHT BENDS",      "3:45"),
    ("lightbeam.png",  "RIDE A BEAM OF LIGHT", "1:38"),
]


def fit_font(draw, text, maxw, start=86, lo=44):
    s = start
    while s >= lo:
        f = ImageFont.truetype(FONT, s)
        if draw.textlength(text, font=f) <= maxw:
            return f
        s -= 4
    return ImageFont.truetype(FONT, lo)


manifest = []
for i, (fname, header, ts) in enumerate(CARDS, 1):
    im = Image.open(os.path.join(SRC, fname)).convert("RGB").resize((W, H))
    d = ImageDraw.Draw(im)
    font = fit_font(d, header, W - 140)
    tw = d.textlength(header, font=font)
    asc, desc = font.getmetrics()
    y = 40
    # subtle soft shadow for legibility, then black text
    d.text(((W - tw) / 2 + 3, y + 3), header, font=font, fill=(180, 140, 55))
    d.text(((W - tw) / 2, y), header, font=font, fill=BLACK)
    out = f"picture_{i:02d}_{fname}"
    im.save(os.path.join(OUT, out))
    manifest.append([out, ts, header])

with open(os.path.join(OUT, "picture_cards_manifest.csv"), "w", newline="") as f:
    wtr = csv.writer(f)
    wtr.writerow(["file", "suggested_audio_time", "header"])
    wtr.writerows(manifest)
print("composited", len(CARDS), "picture cards")
for m in manifest:
    print(m)
