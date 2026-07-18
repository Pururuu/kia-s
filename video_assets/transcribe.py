#!/usr/bin/env python3
import json, sys
from faster_whisper import WhisperModel

AUDIO = "/root/.claude/uploads/375a4db4-b02f-51ad-9bce-26ba1797cd58/72568e0e-einstein_audio.MP3"

model = WhisperModel("small.en", device="cpu", compute_type="int8")
segments, info = model.transcribe(AUDIO, vad_filter=True)
out = []
for s in segments:
    out.append({"start": round(s.start, 2), "end": round(s.end, 2),
                "text": s.text.strip()})
    print(f"[{s.start:7.2f}-{s.end:7.2f}] {s.text.strip()}", flush=True)
json.dump(out, open("transcript.json", "w"), indent=2)
print(f"\n{len(out)} segments, audio duration {info.duration:.1f}s")
