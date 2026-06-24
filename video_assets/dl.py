#!/usr/bin/env python3
"""Download generated media. Reads a map file (uuid -> filename) and scans
stdin for CDN raw URLs (which embed the job uuid). Skips files already present.
Downloads in parallel via a curl config file."""
import sys, os, re, subprocess, tempfile

OUT = sys.argv[1] if len(sys.argv) > 1 else "images"
MAPFILE = sys.argv[2] if len(sys.argv) > 2 else "id_map.txt"

idmap = {}
with open(MAPFILE) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        uid, fname = line.split()
        idmap[uid] = fname

os.makedirs(OUT, exist_ok=True)
blob = sys.stdin.read()
url_re = re.compile(r"https://d8j0ntlcm91z4\.cloudfront\.net/[^\"'\s]+")
uuid_re = re.compile(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})")
seen = set()
cfg = []
for url in url_re.findall(blob):
    if "_min" in url:
        continue
    m = uuid_re.search(url)
    if not m:
        continue
    uid = m.group(1)
    fname = idmap.get(uid)
    if not fname or uid in seen:
        continue
    seen.add(uid)
    out = os.path.join(OUT, fname)
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        continue
    cfg.append(f'url = "{url}"\noutput = "{out}"')

if cfg:
    with tempfile.NamedTemporaryFile("w", suffix=".curl", delete=False) as tf:
        tf.write("\n".join(cfg))
        cfgpath = tf.name
    subprocess.run(["curl", "-s", "--parallel", "--parallel-max", "16",
                    "-K", cfgpath], check=False)
    os.unlink(cfgpath)
print(f"attempted {len(cfg)} downloads to {OUT}/")
