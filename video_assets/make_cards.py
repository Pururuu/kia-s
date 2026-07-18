#!/usr/bin/env python3
"""Render every sentence of the transcribed narration as a title card:
1280x720, black background, Patrick Hand SC, warm cream text, centered."""
import json, os, re, csv
from PIL import Image, ImageDraw, ImageFont

FONT = "fonts/PatrickHandSC.ttf"
W, H = 1280, 720
CREAM = (245, 237, 220)
OUT = "titlecards/full_set"
os.makedirs(OUT, exist_ok=True)

segs = json.load(open("transcript.json"))

# Build a word stream with an approximate timestamp per word so each
# sentence can carry the time where it starts in the audio.
words = []
for s in segs:
    ws = s["text"].split()
    if not ws:
        continue
    span = (s["end"] - s["start"]) / len(ws)
    for i, w in enumerate(ws):
        words.append((s["start"] + i * span, w))

# Split into sentences on ., ?, ! keeping the delimiter.
sentences = []
cur = []
start_t = None
for t, w in words:
    if start_t is None:
        start_t = t
    cur.append(w)
    if re.search(r"[.?!]$", w):
        sentences.append((start_t, " ".join(cur)))
        cur, start_t = [], None
if cur:
    sentences.append((start_t, " ".join(cur)))

# Merge tiny fragments (1-2 words like "Four." "Alone.") into a card of
# their own is actually desirable for this style — keep them standalone.

def wrap(draw, text, font, maxw):
    lines, line = [], ""
    for w in text.split():
        test = (line + " " + w).strip()
        if draw.textlength(test, font=font) <= maxw:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines

manifest = []
for n, (t0, text) in enumerate(sentences, 1):
    # Strip trailing periods/commas for the on-screen text (keep ? and !)
    disp = re.sub(r"[.,]+$", "", text.strip()).upper()
    img = Image.new("RGB", (W, H), "black")
    d = ImageDraw.Draw(img)
    size = 96
    while size >= 44:
        font = ImageFont.truetype(FONT, size)
        lines = wrap(d, disp, font, W - 160)
        lh = int(size * 1.18)
        if len(lines) <= 4 and len(lines) * lh <= H - 200:
            break
        size -= 6
    total_h = len(lines) * lh
    y = (H - total_h) // 2
    for ln in lines:
        lw = d.textlength(ln, font=font)
        d.text(((W - lw) / 2, y), ln, font=font, fill=CREAM)
        y += lh
    fname = f"card_{n:03d}.png"
    img.save(os.path.join(OUT, fname))
    mm, ss = divmod(int(t0), 60)
    manifest.append([fname, f"{mm}:{ss:02d}", text])

with open(os.path.join(OUT, "cards_manifest.csv"), "w", newline="") as f:
    wtr = csv.writer(f)
    wtr.writerow(["file", "audio_time", "text"])
    wtr.writerows(manifest)

print(f"rendered {len(sentences)} cards to {OUT}/")
for row in manifest[:8]:
    print(row)
