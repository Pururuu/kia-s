# Handoff: "Food For Thought" — Einstein Video Asset Production

**Created:** 2026-07-22
**Branch:** `claude/einstein-video-production-85kmiv` (repo `pururuu/kia-s`)
**Session type:** Ongoing per-line asset production for a faceless YouTube video

---

## Summary

Building assets for a chibi-storybook YouTube video, **"What It Was Like To Be Albert Einstein"** (channel: *Food For Thought*). An 8-minute base video was assembled early on (`video_assets/einstein_8min.mp4`), but the bulk of the work since is producing **individual per-line assets** (title/reveal cards + illustrated scenes) that the **user edits together in their own video editor** — I am NOT re-rendering the full video each time. Work continues line-by-line from the narration script. Working tree is clean; everything is committed and pushed.

---

## How the video is actually being built

The user reads their narration script line by line and asks for either:
1. **Black text cards** (title/interstitial) — plain or word-by-word "reveal"
2. **Illustrated scenes** — chibi storybook images, usually 2–3 **continuous** images per beat
3. **Picture black cards** — reveal text on top + an illustration below, all on pure black

They drop these onto their editing timeline themselves. Deliver each asset via `SendUserFile`, commit, and push.

---

## CRITICAL CONVENTIONS (follow exactly — the user has corrected these repeatedly)

### Black text cards & reveal cards → ALWAYS LOCAL, NEVER Higgsfield (zero credits)
- Font: `video_assets/fonts/PatrickHandSC.ttf` (the user's chosen style)
- Black background `#000`, cream text `(245,237,220)`, **ALL CAPS**, centered
- **Drop trailing periods and commas**; KEEP `?` and `!`
- **Reveal cards:** render N frames (one per word); each word is locked to its position in the **full wrapped layout** so words appear in place with no reshuffle. Output `reveal_<key>_<k>of<n>.png`.
- Resolution: newer cards are **1920×1080** (older ones were 1280×720; upgrade on request).
- Rendering is inline Python (PIL). See any recent reveal commit for the exact snippet, or `make_cards.py` for the full-set generator.

### Illustrated scenes → Higgsfield, be credit-mindful
- Model: `nano_banana_pro`, `resolution: "2k"` → **2K costs the SAME 2 credits as 1K** but gives true 1080p. Always generate 2K, then downscale: `ffmpeg -i in -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080" out`.
- **Style ref (Einstein):** media_id `2bc66840-8f17-48a0-b71e-d4089e830ff1` (chibi Einstein at chalkboard). Pass in `medias:[{role:"image", value:...}]`. Style = warm beige/brown flat 2D storybook, chibi, thick clean outlines, soft cel shading. Suffix prompts with "NOT painterly, NOT 3D, NOT photorealistic."
- **Continuity:** generate the FIRST image to lock the setting, then make the next images by passing the **prior job_id as a `medias` reference** with "Keep the EXACT same … unchanged, change ONLY …". You can pass two refs (scene + Einstein ref) for edits that add Einstein.
- Poll results with **`job_display`** (reliable for fresh jobs). `job_status` is **DENIED**. `show_generations` has indexing lag — avoid for just-created jobs. Download from `results.rawUrl` via `curl` (CDN host `d8j0ntlcm91z4.cloudfront.net`).
- **Reusing an existing image is free** — just re-`curl` its CDN URL; no regeneration.

### Picture black cards (reveal text + illustration, continuous)
- Illustration MUST be generated on a **PURE BLACK background** so it blends into the card. **Verify corners are `(0,0,0)`** after download (`im.getpixel((5,5))`). If a generation comes back with white/other corners, it's unusable — regenerate.
- Composite locally: text pinned to the very top, image scaled to fill below.

### Higgsfield server name changes across reconnects
Currently `mcp__d530bb2f-70df-4fee-87ed-e7882387a265__*`. Load tools each session via `ToolSearch` `select:...generate_image,...job_display`. The `higgsfield`-prefixed variant also appears sometimes — same account/CDN.

### Voice (for any narration work): **Arthur** — `30fc8796-ceb6-4a66-b3a7-4a145ef7f346` (ElevenLabs).

---

## Files / assets produced (all under `video_assets/`)

| Dir | Contents |
|---|---|
| `einstein_8min.mp4` | Original 8-min base render (720p). NOT updated with the new cards/scenes. |
| `images/` (190) + `clips/` (gitignored) | Original storyboard frames + Ken Burns clips for the base video |
| `audio/` (42) | Narration line clips (Arthur voice) |
| `titlecards/reveal_cards/` (13 sets) | you-are-albert-einstein, and-one-day, and-somehow, to-everyone-else, almost-forgettable, most-people-ignore-that-feeling, that-makes-you-look-like-a-problem, you-cant, in-1905-everything-changes, what-if-time-isnt-fixed, what-if-it-changes, or-so-they-think, or-would-something-else-break-first |
| `titlecards/extra_cards/` (7) | plain black cards |
| `titlecards/full_set/` (130) | full narration transcribed → one card per sentence |
| `extra_scenes/` (6) | dared-to-ask, another-question (+continuation), time1/2/3 (1080p) |
| `four_papers/` (3) | one → four → four-glowing-with-icons (1080p) |
| `classroom_scenes/` (4) | young Einstein classroom (matched to user's uploaded ref `5c0df432-...`) |
| `atom_sequence/` (3) | they-are-real / invisible / but-real (1080p) — see Known Issue |
| `picture_black_cards/` | "the first proves that atoms aren't just ideas" reveal + single-atom illustration (1080p, 8 frames) |
| `light_scenes/` (3) | wave-particle beat: argue → Einstein → both (1080p) — see Known Issue |
| `thumbnails/` (6) | 3 thumbnail options (+1080p jpgs) |
| `youtube_package.md` | title A/B, description, chapters, tags, upload settings |

**Reusable illustration CDN URLs** (base `https://d8j0ntlcm91z4.cloudfront.net/user_3FLBNTANMX4H5ikBiI5Di5JIiiK/`):
- Gold atom (used for "atoms aren't just ideas"): `hf_20260721_061719_71a55d9b-040c-4e04-af5a-8db88b3b4400.png`
- Blue Bohr atom (current atom_sequence): `hf_20260722_030102_c92b44ec-b31f-4d97-9469-4dd0677dd914.png`

**Scripts:** `build_storyboard.py`, `build_video.py` (full assembly), `dl.py`, `make_cards.py`, `scan_images.py`, `transcribe.py`. Narration source of truth: `video_assets/transcript.json` (from the uploaded `einstein_audio.MP3`, first-person POV).

---

## Known Issues / Open Items

- **`atom_sequence/` atom** — user called the blue Bohr atom "so ugly." A violet retry (`c611daa1…`) came back with a **white background** (unusable). Still needs a nicer atom generated on **true black** for the "They are real / Invisible / But real" sequence. Reuse the fade treatment (blend toward black at ~0.12 for "invisible").
- **`light_scenes/light_1`** keeps small **WAVE!/PARTICLE!** speech bubbles (in-scene dialogue). User was told; may want them removed → regenerate #1 clean.
- The base `einstein_8min.mp4` predates all the per-line cards/scenes. If the user ever wants a re-assembled v2, that's a larger task (not currently requested).

---

## Current State

- **Working / done:** all listed assets delivered + pushed; tree clean.
- **Not a bug, by design:** final edit happens in the user's external editor, not here.
- **Credits:** paid Higgsfield plan. Was ~200 credits mid-session; each 2K image = 2 credits. Verify with the `balance` tool before big batches. Prefer reusing/recoloring existing assets locally when possible.

---

## Next Steps

### Immediate (start here)
1. **Continue the script line-by-line.** Ask the user for (or wait for) the next narration line and whether they want a card or a scene.
2. For a **card:** render locally in Patrick Hand SC (rules above). For a **scene:** generate 2K via Higgsfield, downscale to 1080p, keep continuity by editing from the previous image.
3. **Always:** `SendUserFile` the result(s), then `git add` + commit + `git push -u origin claude/einstein-video-production-85kmiv`.

### If asked to fix outstanding items
- Regenerate a prettier atom on pure black for `atom_sequence/` (verify corners `(0,0,0)`), rebuild the 3 fade cards.
- Regenerate `light_1` without speech bubbles.

---

## Commands to run

```bash
cd /home/user/kia-s
git rev-parse --abbrev-ref HEAD          # confirm branch
git status --short                        # should be clean
ls video_assets/                          # see all asset dirs
# downscale any 2K Higgsfield PNG to 1080p:
ffmpeg -v error -y -i IN.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080" OUT.png
```

Commit footer to use:
```
Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01JiZbjvkosaiFxrRTxUd6Rb
```

---

## Session Notes

- The user is design-sensitive and credit-conscious; when they push back, reuse existing assets (recolor/fade locally) before generating. Do NOT copy other channels' signature formats (e.g., a mustard-yellow circular-diagram card = the "Whatly" look — was flagged as plagiarism and removed).
- Push to the designated branch only. GitHub MCP tools are scoped to `pururuu/kia-s`.

_Generated as a checkpoint; use as initial context for the next session._
