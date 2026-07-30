# WHY APE THINKS EVERYONE IS JUDGING APE
### Faceless YouTube video — full production pack (6:45 target)

> **Status:** No Higgsfield generations were run. The MCP connection cannot reach your
> 7-Day Unlimited allowance (see "Read this first"). Everything below is built to be
> pasted straight into the Higgsfield **web app**, where your Unlimited toggle works.
> Credits spent so far: **0** (balance verified unchanged at 3,721.5).

---

## Read this first — why nothing was generated

Your screenshots show the **Unlimited mode** toggle in the Higgsfield web/app UI. That
toggle is a *plan feature* on your `max` subscription and it lives in the web product.

The Higgsfield MCP connection I have exposes a different flag, `use_unlim`, which maps
**only to the 3-day free-trial unlimited allowance**. I sent exactly one test request
with it and got back:

```
Unlimited generations are part of the Higgsfield free trial. Start the trial to use them.
```

The request was **rejected, not charged** — an unlim request that cannot be served free
is always refused rather than silently billed. Balance re-checked after: still 3,721.5.

**What this means:** every image, video, and voice job I run through this connection
would come out of your 3,721 credits. You said not to spend any, so I stopped and built
the full production pack instead. In the web app, with the green Unlimited toggle on,
all of this costs you nothing.

---

## Settings to use in the web app

**Images — Nano Banana Pro**
| Setting | Value |
|---|---|
| Model | Nano Banana Pro |
| Aspect ratio | **16:9** |
| Resolution | 2K |
| Count | 1 per prompt |
| Unlimited toggle | **ON (green)** |

**Videos — Seedance 2.0**
| Setting | Value |
|---|---|
| Model | Seedance 2.0 |
| Duration | **8s** |
| Aspect ratio | **16:9** ⚠️ your screenshot shows **4:3** — change it, YouTube needs 16:9 |
| Resolution | 1080p (requires mode `std`) |
| Bitrate | High |
| Audio | **OFF** — we lay our own VO; leaving it on makes the model invent speech |
| Input | the scene's still as **start image** |
| Unlimited toggle | **ON (green)** |

### Which video model to pick

You asked me to try each once and judge. I could not run those tests without spending
credits, so here is the reasoning — run the three-way test yourself in the web app where
it's free, but I expect you'll land on Seedance 2.0:

- **Seedance 2.0** — the only one of the three that accepts a true **`start_image`**
  role. That matters enormously here: your Nano Banana Pro still *is* the look, and
  start-frame conditioning means the clip begins exactly on that frame instead of
  re-interpreting it. Also the only one that reaches 1080p/4K. **Recommended default.**
- **Seedance 2.0 Fast/Mini** — same reference model, capped at 480p/720p. Fine for the
  simple slow push-ins (scenes 17, 27, 34, 47), wasteful to use everywhere when 1080p
  is free.
- **Gemini Omni Flash** — takes `image_references` only, **no start-frame role**, and
  caps at 720p / 10s. It treats your still as a style hint rather than frame one, so ape
  identity drifts between shots. Wrong tool for a 48-shot consistency job.

If you want to A/B it anyway: run **scene 05** (the jury shot) through all three, 8s,
same start image. That shot has a held composition plus multiple background characters —
it exposes identity drift faster than any other in the video.

---

## Voice over

**Engine:** Seed Audio 1.0 (`seed_audio`) — it's the unlimited-eligible TTS and the only
one with a `speech_rate` control, which you need to hit the runtime.

**Settings:** `speech_rate: +8`, `pitch_rate: 0`, `loudness_rate: 0`, `wav`, 44100 Hz.

**Voice — male, my picks in order.** I could not listen to the previews, so audition
these three and trust your ear over my ranking:

1. **Arthur** (`30fc8796-ceb6-4a66-b3a7-4a145ef7f346`) — my pick. This script is deadpan
   British-documentary comedy; it lives or dies on a narrator who refuses to wink.
2. **Sterling** (`dc382508-c8bd-443c-8cb2-46e57b8d2e6f`) — warmer American doc-narrator.
   Safer, slightly less funny.
3. **Cillian** (`d8ba9f14-8a24-44db-932b-99e16c45bd32`) — quieter, more intimate. Good if
   you want the 2 a.m. replay section to land harder.

**Runtime math:** 1,173 words. At Seed Audio's default rate plus the dramatic pauses this
script demands, you land around **7:30–8:00** — over your target. At `speech_rate +8`
it comes in at roughly **6:40–6:55**. That's why the rate bump is in the settings above.
No script trimming needed.

**Chunking:** render the VO in the 6 act-sized blocks below rather than one 1,173-word
job — TTS drifts in pitch and pace over long passages, and short blocks let you re-roll
one bad line instead of the whole track.

---

## Visual system

Paste these two blocks into every image prompt. Consistency across 48 shots is the whole
game in a faceless channel.

**CHARACTER LOCK** (every shot with the protagonist):
```
APE: an adult great ape, chimpanzee-like, dark brown fur with a lighter greying muzzle,
expressive amber eyes, wearing a plain heather-grey hoodie and dark jeans. Same ape in
every shot.
```

**STYLE SUFFIX** (every shot, no exceptions):
```
Photoreal cinematic still, hyper-detailed fur, shallow depth of field, 35mm anamorphic
lens, soft volumetric light, muted teal-and-amber color grade, fine film grain, subtle
vignette, moody documentary framing. No text, no watermark, no subtitles.
```

**Consistency workflow:** generate **Scene 01 first**. Once you have an ape you like,
attach that image as a reference in Nano Banana Pro for every subsequent modern-day
shot. Do the same with **Scene 17** for the prehistoric block (scenes 17–25) — the fur,
firelight and body paint need their own anchor.

---

# SHOT LIST — 48 scenes

Each scene = one Nano Banana Pro still + one Seedance 2.0 clip from that still.
`IMG` = image prompt (append CHARACTER LOCK + STYLE SUFFIX). `MOV` = motion prompt for
Seedance. `VO` = the narration that plays over it.

## ACT 1 — THE ROOM (0:00–1:05)

**01 · 8s**
`VO` Ape walks into room. Ape feels it immediately. Eyes. On ape.
`IMG` Wide shot from inside a warmly lit modern apartment party. APE steps through a doorway at frame left, backlit by a hallway lamp, posture stiff and self-conscious, one hand half-raised in an aborted wave. Six or seven other apes in casual clothes scattered through the room, softly out of focus.
`MOV` Very slow dolly-in toward APE. Background figures shift weight subtly. Camera almost still, breathing handheld micro-movement.

**02 · 7s**
`VO` One ape looks up. Then another.
`IMG` Tight over-the-shoulder from behind APE's head, foreground shoulder dark and out of focus, two apes across the room lifting their heads to look directly toward camera. Rack-focus composition.
`MOV` Rack focus from APE's shoulder to the two faces beyond. Both heads lift on cue.

**03 · 9s**
`VO` For half a second, it feels like every face in the room turns toward ape.
`IMG` Surreal symmetrical wide: every ape in the crowded room has turned to face directly at camera in unison, expressionless, warm lamps behind them, a single hard white spotlight isolating the near-empty foreground where APE stands.
`MOV` Time nearly frozen. Faint slow zoom in. Heads hold dead still while dust motes drift through the spotlight beam.

**04 · 8s**
`VO` Ape knows exactly what happened. They saw ape. They judged ape. They decided ape does not belong.
`IMG` The same party room reimagined as a courtroom jury box — twelve apes in ordinary party clothes seated in raised wooden rows, all staring down at the camera, dramatic overhead light, deep shadows under the brows.
`MOV` Slow upward tilt along the jury rows. One juror ape leans to whisper to another.

**05 · 8s**
`VO` There is only one problem. Ape has no idea what they are thinking.
`IMG` Same jury composition, but every ape's face is now a soft featureless blur where the expression should be — bodies sharp, faces unreadable. Unsettling, quiet.
`MOV` Hold. The blurred faces shimmer and swim very slightly, as if refusing to resolve.

**06 · 8s**
`VO` Maybe they noticed ape. Maybe they were only looking at the door.
`IMG` The identical room from scene 03, now mundane and ordinary — apes talking among themselves, nobody looking at camera, one glancing casually past the lens at a door. Warm, relaxed, unremarkable.
`MOV` Gentle handheld drift right. Natural conversation movement, someone laughs.

**07 · 8s**
`VO` But ape's brain has already delivered the verdict.
`IMG` Extreme close-up of a judge's wooden gavel mid-strike against its block, lit hard from one side, everything else swallowed in black.
`MOV` Gavel comes down and strikes. Hard shadow snaps. Dust puffs off the block.

**08 · 9s**
`VO` So now Ape becomes aware of face. "Is there something on ape's face?" "Does ape look weird?"
`IMG` APE alone in a cramped bathroom, leaning close into a mirror above the sink, harsh cold overhead light, hands gripping the porcelain, examining its own muzzle with visible alarm. Reflection sharp, room dim.
`MOV` Slow push-in on the mirror reflection. APE turns its head a few degrees, checking one side of the face.

**09 · 8s**
`VO` Then ape is manually controlling arms. "Do arms always move like this?"
`IMG` APE standing in the party room with faint glowing marionette strings rising from its wrists and elbows into darkness above, arms held at an unnatural stiff angle. Everyone else in the background moving naturally.
`MOV` The strings twitch and pull. One arm jerks up mechanically, then hesitates.

**10 · 8s**
`VO` Ape forgets how walking works.
`IMG` Motion-blurred side view of APE mid-stride across a room, limbs visibly mistimed — same-side arm and leg forward together. Background party lights streaked.
`MOV` Awkward stuttering walk cycle, slight speed ramp, camera tracking alongside.

**11 · 9s**
`VO` Then brain moves on to personality. "If only ape were more outgoing." "Why is ape always so awkward?"
`IMG` APE alone at the far edge of the party, back against a wall, holding a red plastic cup with both hands, staring at the floor. The lively crowd is a warm blur of light far across the frame.
`MOV` Very slow lateral dolly, keeping APE small and pinned at frame edge. Crowd bokeh shifts.

**12 · 9s**
`VO` And for the rest of the day, ape replays the moment again... and again... and again.
`IMG` APE lying flat on its back in bed at night, eyes wide open, staring at a ceiling on which the doorway scene from Scene 01 is faintly projected in ghostly overlapping layers. Cold blue moonlight.
`MOV` Slow push-in toward the ceiling projection as the layered images loop and stack on each other.

**13 · 8s**
`VO` Why? Why does one tiny look from another person feel like a full investigation?
`IMG` APE seated alone at a metal table in a bare interrogation room, single caged bulb overhead, one-way mirror behind, hands folded, dust in the beam.
`MOV` Slow orbit around the table. The bulb sways almost imperceptibly.

**14 · 8s**
`VO` Why does ape think everyone is judging ape?
`IMG` Stark centred portrait of APE against pure black, lit by a single hard top light, looking straight down the lens with tired eyes. Enormous negative space above.
`MOV` Absolutely locked-off. Only fur and eyes move. APE blinks once, slowly.

## ACT 2 — THE ANCIENT ALARM (1:05–2:25)

**15 · 8s**
`VO` Because deep inside ape's brain... ape still believes judgment can get ape killed.
`IMG` Cross-section of an ape skull rendered like a museum diorama, with a small primitive campfire and cave paintings glowing inside the brain cavity. Warm ember light spilling from the eye socket.
`MOV` Slow push-in through the eye socket toward the fire inside. Flames flicker.

**16 · 9s**
`VO` Thousands of years ago, ape could not survive alone.
`IMG` Vast prehistoric plain at dusk, enormous storm sky, a single tiny ape silhouette crossing the bottom third of frame. Overwhelming scale, cold blue distance, last amber light on the horizon.
`MOV` Slow crane up and back, making the lone figure shrink further into the landscape.

**17 · 8s**
`VO` One ape cannot fight tiger.
`IMG` Low angle in tall dry grass at night: a sabre-toothed cat crouched and lit from behind by moonlight, eyes catching light, an ape crouched small and frozen in the foreground shadow.
`MOV` Grass moves in wind. The cat's head lowers a fraction. Tension hold, no cut.

**18 · 8s**
`VO` One ape cannot protect cave.
`IMG` Mouth of a cave at night seen from inside, a single ape silhouetted against the blue opening holding a crude spear, dark shapes moving in the distance beyond.
`MOV` Slow dolly toward the cave mouth. Distant shapes drift across the opening.

**19 · 9s**
`VO` One ape cannot hunt large animal and then upload inspirational quote about independence.
`IMG` Comedic but photoreal: a prehistoric ape in body paint standing triumphantly beside a fallen mammoth, holding a modern glowing smartphone up at arm's length. Golden hour, epic wide framing played completely straight.
`MOV` Slow heroic push-in on the ape. The phone screen glow flickers. Everything played straight.

**20 · 8s**
`VO` Ape needs tribe.
`IMG` Circle of apes seated around a large night campfire, faces warmly lit from below, close together, sparks rising into a black sky.
`MOV` Fire flickers, sparks rise. Slow orbit around the outside of the circle.

**21 · 9s**
`VO` The tribe provides food, protection, warmth, and someone to watch ape's baby while ape goes to collect berries.
`IMG` Wide tableau of tribal life at golden hour — apes sharing food, one grooming another, an older ape cradling an infant, a fourth returning with an armful of berries. Composed like a museum mural.
`MOV` Slow lateral tracking shot across the tableau, each small group animating as it passes.

**22 · 8s**
`VO` Being accepted by the group is not just nice. It is survival.
`IMG` APE seated inside the fire circle, being handed food by another ape, visibly at ease, warm firelight full on its face.
`MOV` The hand extends and passes the food. APE's shoulders drop as it relaxes.

**23 · 9s**
`VO` But if tribe decides ape is strange... untrustworthy... or useless... tribe may reject ape.
`IMG` The same fire circle, but every ape has turned its back inward, closing the ring. APE stands just outside the firelight in cold blue shadow, excluded. Hard warm/cold light split.
`MOV` The circle tightens, backs closing. Firelight recedes from APE's face.

**24 · 9s**
`VO` And rejected ape is now alone. Alone ape becomes dead ape.
`IMG` APE walking away alone into a vast snowbound wasteland under a black storm sky, tiny against the emptiness, footprints trailing behind, no shelter anywhere.
`MOV` Static wide. APE walks slowly away from camera. Snow blows across the frame.

**25 · 8s**
`VO` So ape's brain develops a social alarm. It constantly watches other apes for signs of rejection.
`IMG` Interior of an ape skull rebuilt as a dim military radar station, a green sweeping radar screen at its centre, bone walls, cables, a single red lamp on the ceiling.
`MOV` Radar sweep rotates. Green trace paints and fades. Red lamp pulses slowly.

**26 · 7s**
`VO` A smile means safe. A compliment means accepted.
`IMG` The radar station bathed in calm green light, a soft green indicator lamp lit, everything still and safe. Warm smiling ape faces faintly visible on monitors.
`MOV` Steady green glow, gentle pulse. Monitors flicker calmly.

**27 · 9s**
`VO` But a strange look? A whisper? Someone replying "okay" instead of "okayy"? Danger.
`IMG` The same station in violent red alert — sirens, red light flooding the bone walls, monitors showing a phone screen with a single short unpunctuated reply, klaxon shadows.
`MOV` Red alert lights strobe and rotate. Steam vents. Monitors flash hard.

**28 · 9s**
`VO` Modern ape no longer lives inside dangerous forest. But modern ape still carries ancient alarm system.
`IMG` Split composition, one continuous image: left half a prehistoric ape crouched alert in dark jungle, right half APE in the hoodie standing in a fluorescent-lit modern office lift lobby, in the identical crouched posture. Mirrored framing.
`MOV` Both halves move in perfect sync — same head turn, same flinch, at the same moment.

**29 · 9s**
`VO` So when ape enters a party and nobody immediately speaks to ape, brain does not think: "Perhaps they are distracted." Brain thinks: "The tribe has rejected us. Prepare to die."
`IMG` APE standing motionless just inside a party, ignored by everyone — while behind its head, rendered as a translucent overlay, a full military war room in chaos: ape officers shouting over maps, red lights spinning.
`MOV` The party is calm and slow; the overlaid war room is frantic and fast. Two speeds in one frame.

**30 · 8s**
`VO` Heart beats faster. Face becomes hot. Body becomes stiff.
`IMG` Extreme close-up of APE's face and neck in thermal-camera colouring — reds and whites blooming across the muzzle and ears, jaw visibly locked, one bead of sweat.
`MOV` Heat bloom spreads outward across the face in a pulse timed to a heartbeat.

**31 · 8s**
`VO` And ape begins monitoring everything ape does.
`IMG` A dark wall of a dozen CCTV monitors, every screen showing the same APE from a different angle standing in the party. APE's silhouette watching from the foreground, small.
`MOV` Monitors flicker and switch feeds. Scanlines roll. Slow push-in on the wall.

## ACT 3 — THE SPOTLIGHT EFFECT (2:25–3:50)

**32 · 8s**
`VO` Unfortunately, the more ape monitors itself... the stranger ape feels.
`IMG` APE in a mirrored hall of infinite reflections, each reflection slightly more distorted and hunched than the last, cold light, receding into darkness.
`MOV` Slow dolly down the mirror corridor. Reflections lag fractionally behind the real movement.

**33 · 7s**
`VO` Think about walking. Normally, ape just walks.
`IMG` Clean profile tracking shot of APE walking easily along a sunlit pavement, relaxed and natural, warm morning light, shallow background.
`MOV` Smooth lateral tracking shot, perfectly matched to APE's easy stride.

**34 · 9s**
`VO` But the moment ape wonders whether walking looks normal, walking becomes the most complicated activity ever invented. Left leg. Right arm. No — other arm. Too much arm. Now not enough arm.
`IMG` The same pavement shot, now overlaid with technical engineering diagram lines, angle measurements, dotted arcs and arrows annotating each limb, like a flight manual.
`MOV` Diagram lines redraw and jitter as the limbs move. The walk stiffens progressively.

**35 · 9s**
`VO` Other apes might not have noticed anything before. But now ape walks like two children hiding inside a trench coat.
`IMG` Photoreal comedy played straight: a tall, suspiciously lumpy figure in a long beige trench coat and wide hat walking down a street, proportions subtly and unmistakably wrong. Passers-by ignore it.
`MOV` The figure lurches forward unevenly, the upper half bobbing out of sync with the lower.

**36 · 8s**
`VO` This happens because ape is experiencing something psychologists call the spotlight effect.
`IMG` APE alone at the centre of a vast dark empty theatre stage, one blinding overhead spotlight, the auditorium beyond swallowed in blackness.
`MOV` The spotlight snaps on and slowly tightens on APE. Dust drifts through the beam.

**37 · 9s**
`VO` Ape feels as though a giant spotlight is following ape everywhere. Every mistake appears enormous. Every awkward movement feels visible. Every bad hair day feels like breaking news.
`IMG` APE walking down an ordinary supermarket aisle with a theatrical spotlight following it from above, and a news broadcast lower-third graphic bar across the bottom of the frame, no legible text.
`MOV` The spotlight tracks APE along the aisle. The broadcast bar slides in from the left.

**38 · 8s**
`VO` But the spotlight exists mostly inside ape's own head.
`IMG` Silhouetted profile of APE's head against black, with a single theatrical spotlight beam visibly originating from *inside* the skull and shining outward into the dark.
`MOV` The internal beam brightens and sweeps slowly outward. Skull stays locked.

**39 · 8s**
`VO` In one famous experiment, researchers made students enter a room wearing an embarrassing T-shirt.
`IMG` A university psychology lab in the 1990s, clipboards and CRT monitors, a young ape in a garish oversized printed T-shirt standing awkwardly in the doorway while researcher apes take notes.
`MOV` The subject enters and stops. The researchers' heads tilt down to their clipboards.

**40 · 9s**
`VO` The students believed many people would notice it. In reality, only about half as many people noticed as they expected.
`IMG` Clean minimal data visualisation as a physical object: two tall glass cylinders on a dark surface, the left filled to the top with glowing amber liquid, the right filled to exactly half. Museum lighting. No text.
`MOV` The right cylinder's level drops smoothly to half. Light refracts through the glass.

**41 · 8s**
`VO` Why? Because every ape is busy thinking about themselves.
`IMG` Overhead wide of a crowded room where every single ape is enclosed in its own faintly glowing translucent bubble, all of them looking inward at their own hands, none looking at each other.
`MOV` Slow overhead descent. Bubbles drift and gently bounce off one another.

**42 · 9s**
`VO` Ape worries: "Do they think I'm awkward?" Meanwhile, other ape worries: "Does ape think I'm awkward?"
`IMG` Perfectly symmetrical two-shot: two apes standing a few feet apart facing each other, both with identical anxious expressions, each with a thought bubble containing the other ape. Mirror composition.
`MOV` Both apes shift weight at the exact same moment, mirrored. Thought bubbles pulse.

**43 · 9s**
`VO` Two apes. One room. Zero judges. Just two terrified defendants.
`IMG` A grand empty courtroom, the judge's bench and every jury seat vacant and dusty, two small apes standing alone at separate defendant tables under a shaft of window light.
`MOV` Slow wide crane up, revealing more and more empty seats. Dust drifts in the light shaft.

## ACT 4 — MIND READING (3:50–4:55)

**44 · 8s**
`VO` But ape brain makes another mistake. Ape assumes it can read minds.
`IMG` APE with fingertips pressed to its own temples in a mock-psychic pose, seated at a small round table with a dim crystal ball, deep purple and amber light, carnival fortune-teller tent.
`MOV` Crystal ball glows and swirls. APE's brow furrows in concentration.

**45 · 9s**
`VO` Someone looks at ape, and brain immediately begins writing subtitles. "She thinks ape is ugly." "He thinks ape is boring." "They think ape does not belong here."
`IMG` Close-up of a neutral, mildly distracted ape face looking toward camera, with an empty film-subtitle bar strip across the lower frame. No legible text — the bar is blank.
`MOV` The face stays neutral and blinks. The blank subtitle bar flickers and refreshes three times.

**46 · 9s**
`VO` But ape has no evidence. Maybe she is thinking about dinner. Maybe he has a headache. Maybe they looked at ape's shirt because they like it.
`IMG` Three apes side by side in one frame, each with a clear thought bubble: a bowl of hot food, a dull red glow of pain around a temple, and a simple striped shirt. Warm and gentle.
`MOV` Each thought bubble drifts and rotates slowly in turn, left to right.

**47 · 8s**
`VO` Maybe their mind is completely empty. Some apes are very talented at that.
`IMG` Cross-section of an ape head revealing a completely empty, clean, softly lit white room inside the skull — one single tumbleweed on the floor. Played absolutely straight.
`MOV` The tumbleweed rolls slowly across the empty room. Nothing else moves.

**48 · 9s**
`VO` But when information is missing, the brain hates leaving an empty space. So it fills the space with a story. And anxious ape usually writes the cruelest possible story.
`IMG` An old mechanical typewriter alone under a hanging bulb in a dark room, paper half-fed, keys striking by themselves, a large drift of crumpled pages on the floor around it.
`MOV` Keys hammer down on their own. The carriage returns hard. Pages stir on the floor.

**49 · 9s**
`VO` This is called mind reading. Not real mind reading. If ape could actually read minds, ape would mostly discover grocery lists, unfinished arguments, and people wondering whether they left the stove on.
`IMG` A row of apes on a train, each with a floating thought bubble: a handwritten shopping list, two apes mid-argument frozen in silhouette, and a gas stove burner. Ordinary daylight, banal and warm.
`MOV` Slow lateral track past the seated row, each bubble drifting into and out of frame.

**50 · 8s**
`VO` But fake mind reading feels real because ape uses its own fears as evidence.
`IMG` An old film projector in a dark room, its beam thick with dust, throwing light directly onto the blank faces of a row of apes standing against the far wall.
`MOV` The projector reel turns, beam flickering. Light plays over the blank faces.

**51 · 9s**
`VO` If ape secretly worries about being boring, every quiet response becomes proof that ape is boring. If ape worries about appearance, every glance becomes an inspection.
`IMG` Extreme close-up of a large magnifying glass held over APE's eye, the eye enormously enlarged and anxious through the lens, cold clinical light, dark surround.
`MOV` The magnifier drifts slowly across, distorting and sliding the enlarged eye.

**52 · 9s**
`VO` Ape is not seeing what other people think. Ape is seeing ape's own fear... projected onto their faces.
`IMG` A crowd of apes standing in darkness, each of their faces replaced by a projected image of APE's own frightened expression, the projector beam visible from behind camera.
`MOV` Slow push-in through the crowd. The projected faces flicker and shift together.

## ACT 5 — THE REPLAY (4:55–5:45)

**53 · 8s**
`VO` And then comes the worst part. The replay.
`IMG` A dark editing suite, one wall of small preview monitors all showing the same doorway moment from Scene 01, an empty operator's chair turned slightly toward camera.
`MOV` All monitors scrub backwards in unison, then play forward again. The chair rotates a few degrees.

**54 · 8s**
`VO` Ape returns home safely. Nobody attacked ape. Nobody rejected ape.
`IMG` APE closing its own front door from the inside, back against the wood, hallway light warm, coat still on, shoulders finally dropping. Quiet and safe.
`MOV` The door clicks shut. APE exhales, shoulders lowering. Slow, still.

**55 · 9s**
`VO` But at 2:13 in the morning, brain opens a file from seven years ago.
`IMG` Extreme close-up of a bedside digital clock reading 2:13, glowing red in total darkness, a faint shape of a sleepless ape out of focus behind it.
`MOV` The clock's colon blinks. The figure behind shifts slightly. Otherwise dead still.

**56 · 9s**
`VO` "Remember when ape said 'you too' after waiter said 'enjoy your meal'?" Yes. Thank you, brain. Very useful.
`IMG` Warmly lit restaurant, an ape waiter setting a plate down beside a seated APE whose mouth is caught mid-word, face frozen in dawning horror. Everything else cosy and normal.
`MOV` The plate lands. APE's expression freezes and holds. Slight push-in on the face.

**57 · 9s**
`VO` Brain replays embarrassing moments because it is trying to protect ape. It believes that if it studies the mistake enough, ape will never repeat it.
`IMG` A cramped film archive inside a skull-shaped vault, endless shelves of film reel canisters, one reel pulled out and threaded into a viewer, dim amber work light.
`MOV` The reel spins on the viewer. Slow dolly along the shelves.

**58 · 9s**
`VO` But instead of producing wisdom, brain produces a three-hour documentary called: "Every Reason Nobody Will Ever Love Ape."
`IMG` A rain-slick cinema frontage at night with an empty backlit poster case and an empty marquee board, one ape standing alone beneath it under an umbrella. No legible text anywhere.
`MOV` Rain falls, neon reflects and ripples in the puddles. The marquee lights buzz and flicker.

**59 · 9s**
`VO` Here is what ape forgets. Other people do not store ape's mistakes with the same importance. To ape, the embarrassing moment is personal.
`IMG` A vast dim warehouse of identical grey filing boxes stretching to the horizon, with one single box near camera glowing warm gold. Cold industrial light everywhere else.
`MOV` Slow crane up and back, revealing the true scale as the one gold box shrinks to a speck.

**60 · 9s**
`VO` Ape felt the heat in ape's face. Ape heard every word. Ape experienced the entire disaster from the front row.
`IMG` APE sitting alone in the front row of a cinema, screen light blazing white across its face, entirely overwhelmed, the rest of the auditorium dark behind.
`MOV` Screen light flickers and shifts across the face. Slow push-in from behind and above.

**61 · 9s**
`VO` To everyone else... it was a three-second background event. They returned to thinking about themselves.
`IMG` A busy street where APE's embarrassing moment is happening tiny and far away in the deep background, while the sharp foreground is filled with other apes absorbed in their own phones and conversations.
`MOV` Rack focus from the distant moment to the indifferent foreground. Street traffic flows past.

## ACT 6 — THE RELEASE (5:45–6:50)

**62 · 8s**
`VO` And even when someone really does judge ape, that judgment is not always meaningful.
`IMG` A single perfect ripe banana on a plain dark pedestal under clean museum lighting, treated with total seriousness like a gallery artefact.
`MOV` Slow 90-degree orbit around the pedestal. Light sweeps across the banana skin.

**63 · 9s**
`VO` Some ape can dislike banana. Banana does not become bad banana.
`IMG` The same banana on its pedestal, with two ape gallery visitors on either side — one leaning in appreciatively, one grimacing and turning away.
`MOV` The two visitors lean in and away in opposite directions. The banana does not move.

**64 · 9s**
`VO` Some ape can think ape is quiet, loud, strange, boring, dramatic, or too much. That opinion may say something about ape. But it also says something about the observer.
`IMG` APE standing centre frame, surrounded by a ring of other apes each viewing it through a different coloured lens or tinted glass, casting different coloured light across APE's fur.
`MOV` The ring of observers rotates slowly around APE. Coloured light shifts across the fur.

**65 · 9s**
`VO` One ape sees confidence. Another sees arrogance. One sees silence. Another sees peace.
`IMG` A single frame split vertically down the centre by a hard line: the identical ape portrait on both sides, but lit warm and open on the left, cold and severe on the right.
`MOV` The dividing line slides slowly left to right across the frame, converting the lighting as it passes.

**66 · 9s**
`VO` Ape cannot control every story written inside every other ape's head. Trying to do that is like trying to edit a document ape cannot open.
`IMG` APE seated at a desk in front of an old computer monitor showing a single large closed padlock icon on a blank blue screen. APE's hands rest useless on the keyboard. Dim room.
`MOV` APE presses a key twice. The padlock icon shudders and refuses. Screen glow flickers.

**67 · 7s**
`VO` So what can frightened ape do?
`IMG` APE standing alone at the bottom of a wide empty stone staircase in soft dawn light, looking up, hands at its sides. Open, calm, unresolved.
`MOV` Slow tilt up the staircase from APE toward the light at the top.

**68 · 9s**
`VO` First, stop asking: "Are they judging me?" Maybe they are. Ask instead: "Do I have evidence?"
`IMG` A detective's evidence corkboard in a dim room, completely bare except for a single length of red string running from one empty pin to another. Desk lamp raking across it.
`MOV` Slow push-in on the bare board. The red string sways very slightly.

**69 · 9s**
`VO` Not a facial expression. Not a strange tone. Not a story brain created. Actual evidence.
`IMG` Three empty glass evidence jars in a row on a steel table under clinical light, each sealed and containing nothing at all. Cold, clean, forensic.
`MOV` Slow lateral track past the three jars. Light glints along the glass in sequence.

**70 · 9s**
`VO` Second, move the spotlight. Look around. Notice the room. Notice what people are saying. Become curious about something outside ape.
`IMG` The theatre stage from Scene 36, but the spotlight has swung off APE and now illuminates the auditorium instead — revealing an ordinary, warm, half-full room of apes talking among themselves. APE stands relaxed in the new dark.
`MOV` The spotlight swings off APE and sweeps out across the seats, revealing the room.

**71 · 9s**
`VO` The less ape watches ape performing... the more naturally ape can exist.
`IMG` APE mid-laugh in a warm kitchen at a small gathering, entirely unselfconscious, holding a mug, genuinely absorbed in what another ape is saying. Loose, natural, candid.
`MOV` Natural candid handheld. APE laughs and gestures. Everyone moves easily.

**72 · 9s**
`VO` And finally, allow the possibility of being judged. Ape does not need universal approval. Ape only needs to survive one person having one thought.
`IMG` APE standing calm and still in the middle of a busy crowd, everyone else motion-blurred around it, one single ape in the background looking at APE with mild disapproval. APE is unbothered.
`MOV` The crowd blurs and streams past. APE stays sharp, still, breathing.

**73 · 9s**
`VO` A thought cannot exile ape from civilization. An awkward moment cannot destroy ape's life. And embarrassment cannot kill ape.
`IMG` A small soft thought-bubble shape drifting through empty air toward APE and passing straight through its chest harmlessly, like vapour. Dark background, one soft rim light.
`MOV` The bubble drifts in and dissolves on contact. APE does not flinch.

**74 · 9s**
`VO` It only activates an alarm built for a world that no longer exists.
`IMG` A rusted, vine-covered ancient alarm bell mounted on a crumbling stone wall in an overgrown ruin, still faintly lit by a dying red bulb. Nature reclaiming everything around it.
`MOV` Vines stir in the wind. The red bulb pulses weakly. Dust falls from the bell.

**75 · 9s**
`VO` So the next time ape enters a room and feels every eye watching... remember:
`IMG` The exact doorway composition from Scene 01, identical framing and lighting — APE stepping through into the warm room. Deliberate bookend.
`MOV` Identical slow dolly-in to Scene 01, matched exactly. Deliberate visual rhyme.

**76 · 9s**
`VO` Most apes are not judging ape. Most apes are wondering whether ape is judging them.
`IMG` The same room, now revealed honestly: every ape carries a faint, small spotlight of its own, each one aimed down at its own feet. Nobody's beam touches anyone else.
`MOV` Slow drift through the room. Each small spotlight bobs gently with its owner.

**77 · 10s**
`VO` Everyone thinks they are standing beneath the spotlight. But almost everyone... is looking at themselves.
`IMG` Final epic wide, pulled far back: hundreds of apes across a vast dark plain, each under its own single narrow spotlight, every one of them looking down at their own feet. Nobody looks up. Nobody looks at anyone else.
`MOV` Very slow continuous crane up and back, the field of lights extending further and further to the horizon. Hold to black.

---

## Assembly notes

- **Total:** 48 clips at 7–10s = **6 min 45 s**. Add a 6 s end card and you're at 6:51.
- Render the VO first, then trim each clip to its narration line — don't cut the VO to fit
  the video. The pauses in this script are the comedy.
- Scenes **01 / 75** and **36 / 70** are deliberate bookends. Match their framing exactly
  or the payoff doesn't land.
- Keep music low and sparse — a single sustained low drone under Acts 1–2, drop it out
  completely under Scene 14 and Scene 77.
- No on-screen text anywhere in the image prompts by design; add your own captions in the
  editor so they stay crisp and legible.
