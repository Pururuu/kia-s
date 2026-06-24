#!/usr/bin/env python3
"""Assemble the 8-minute Einstein slideshow.

- Per narration line: one audio clip + its images (from audio_lines.json).
- Narration track = lead-in silence + (audio + pause) per line, sized so the
  whole thing lands on TARGET seconds.
- Each image gets a gentle Ken Burns move and is held for its share of the
  line's window. Images concatenated into the video track.
- A very soft ambient pad sits under everything so the reflective pauses are
  not dead air.
"""
import json, os, subprocess, math

TARGET = 480.0     # 8:00
LEAD_IN = 1.5
TAIL = 2.5
W, H = 1280, 720
FPS = 30
IMG = "images"
AUD = "audio"
WORK = "clips"
os.makedirs(WORK, exist_ok=True)

lines = json.load(open("audio_lines.json"))


def dur(path):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
    try:
        return float(out)
    except ValueError:
        return 0.0


# 1) audio durations
adur = []
for l in lines:
    d = dur(os.path.join(AUD, l["audio"]))
    adur.append(d)
S = sum(adur)
N = len(lines)
pause = (TARGET - LEAD_IN - TAIL - S) / (N - 1)
print(f"speech total={S:.1f}s lines={N} pause={pause:.2f}s")
if pause < 0.4:
    pause = 0.4  # floor; will overrun slightly, trimmed later

# 2) build narration audio: lead-in silence then audio+pause per line
parts = []
parts.append(f"aevalsrc=0:d={LEAD_IN}[s0]")
seg = ["[s0]"]
ai = []
for i, l in enumerate(lines):
    ai.append(f"-i {os.path.join(AUD, l['audio'])}")
# Build with concat filter: silence, a1, sil, a2, sil ... aN, sil(tail)
# Construct input list
inputs = []
for l in lines:
    inputs += ["-i", os.path.join(AUD, l["audio"])]

fc = []
# silence generators
fc.append(f"aevalsrc=0:d={LEAD_IN}:s=44100[lead]")
sil_label = []
for i in range(N):
    p = TAIL if i == N - 1 else pause
    fc.append(f"aevalsrc=0:d={p:.3f}:s=44100[sil{i}]")
# resample each audio input to 44100 stereo->mono consistent
amap = []
for i in range(N):
    fc.append(f"[{i}:a]aformat=sample_rates=44100:channel_layouts=mono[a{i}]")
# concat order: lead, a0, sil0, a1, sil1, ... aN-1, silN-1
order = "[lead]"
for i in range(N):
    order += f"[a{i}][sil{i}]"
fc.append(f"{order}concat=n={2*N+1}:v=0:a=1[narr]")
filtergraph = ";".join(fc)

cmd = ["ffmpeg", "-y"] + inputs + ["-filter_complex", filtergraph,
       "-map", "[narr]", "narration.wav"]
if not (os.path.exists("narration.wav") and os.path.getsize("narration.wav") > 1_000_000):
    print("building narration track...")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists("narration.wav"):
        print(r.stderr[-3000:])
        raise SystemExit("narration build failed")
NARR = dur("narration.wav")
print(f"narration.wav = {NARR:.1f}s")

# 3) per-image clip durations
imgdurs = []  # (imgpath, seconds)
for i, l in enumerate(lines):
    p = TAIL if i == N - 1 else pause
    window = adur[i] + p
    extra = LEAD_IN if i == 0 else 0.0
    window += extra
    imgs = l["images"]
    k = len(imgs)
    per = window / k
    for j, im in enumerate(imgs):
        imgdurs.append((os.path.join(IMG, im), per))

total_v = sum(d for _, d in imgdurs)
print(f"video total={total_v:.1f}s over {len(imgdurs)} images")

# 4) render each image as a Ken Burns clip
listf = open("concat_list.txt", "w")
for idx, (im, d) in enumerate(imgdurs):
    outc = os.path.join(WORK, f"c{idx:03d}.mp4")
    frames = max(2, int(round(d * FPS)))
    # alternate zoom in / zoom out
    if idx % 2 == 0:
        z = "min(zoom+0.0006,1.10)"
    else:
        z = "if(eq(on,1),1.10,max(zoom-0.0006,1.0))"
    vf = (f"scale=1920:-1,zoompan=z='{z}':d={frames}:"
          f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
          f"format=yuv420p")
    if not (os.path.exists(outc) and os.path.getsize(outc) > 1000):
        try:
            subprocess.run(["ffmpeg", "-y", "-loop", "1", "-i", im, "-t", f"{d:.3f}",
                            "-vf", vf, "-c:v", "libx264", "-preset", "veryfast",
                            "-crf", "23", "-an", outc],
                           capture_output=True, text=True, timeout=45)
        except subprocess.TimeoutExpired:
            print(f"  clip {idx} timed out, skipping")
    if idx % 20 == 0:
        print(f"  clips progress: {idx}/{len(imgdurs)}")
    listf.write(f"file '{os.path.abspath(outc)}'\n")
listf.close()
print("clips rendered")

# 5) concat video clips
subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i",
                "concat_list.txt", "-c", "copy", "video_silent.mp4"],
               capture_output=True, text=True)
print(f"video_silent.mp4 = {dur('video_silent.mp4'):.1f}s")

# 6) ambient pad bed (soft, low volume), length = NARR
bed_fc = (
    "sine=frequency=110:duration=%0.1f[b0];"
    "sine=frequency=146.83:duration=%0.1f[b1];"
    "sine=frequency=220:duration=%0.1f[b2];"
    "[b0][b1][b2]amix=inputs=3,tremolo=f=0.12:d=0.4,"
    "aecho=0.8:0.88:800:0.3,lowpass=f=700,volume=0.05[bed]" % (NARR, NARR, NARR)
)
subprocess.run(["ffmpeg", "-y", "-filter_complex", bed_fc, "-map", "[bed]",
                "bed.wav"], capture_output=True, text=True)

# 7) mix narration + bed, mux with video, trim to TARGET
subprocess.run([
    "ffmpeg", "-y", "-i", "video_silent.mp4", "-i", "narration.wav",
    "-i", "bed.wav",
    "-filter_complex",
    "[1:a]volume=1.0[n];[2:a]volume=1.0[m];[n][m]amix=inputs=2:duration=longest[a]",
    "-map", "0:v", "-map", "[a]",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-shortest", "-t", f"{TARGET}",
    "einstein_8min.mp4"], capture_output=True, text=True)
print(f"DONE einstein_8min.mp4 = {dur('einstein_8min.mp4'):.1f}s")
