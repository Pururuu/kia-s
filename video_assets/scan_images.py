#!/usr/bin/env python3
import subprocess, os
bad = []
for i in range(1, 191):
    f = f"images/img_{i:03d}.png"
    if not os.path.exists(f):
        bad.append(i); continue
    try:
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f,
                            "-frames:v", "1", "-f", "null", "-"],
                           capture_output=True, timeout=6)
        if r.returncode != 0:
            bad.append(i)
    except subprocess.TimeoutExpired:
        bad.append(i)
print("BAD:", bad)
