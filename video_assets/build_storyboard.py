#!/usr/bin/env python3
"""Generate the narration text + the ordered storyboard (image prompts) for
the 'What It Was Like To Be Albert Einstein' 8-minute slideshow.

Style bible: flat chibi storybook illustration (Baldwin IV inspired), warm
beige/brown palette, clean outlines, cozy educational vibe, 16:9.
"""
import json

STYLE = (
    "Flat 2D storybook children's-book illustration, cute chibi proportions, "
    "round pale faces with tiny black dot eyes, thick clean bold outlines, "
    "soft flat cel shading, warm cozy beige and brown color palette, gentle "
    "golden lighting, simple readable composition, 16:9. Albert Einstein is a "
    "chibi character with thick curly brown hair, small brown mustache and a "
    "brown wool suit. NOT painterly, NOT oil painting, NOT 3D render, NOT "
    "photorealistic, no caption text overlays."
)

# Framing variants appended to add cinematic variety across shots of one beat.
FRAMING = [
    "Wide establishing shot.",
    "Medium shot, centered.",
    "Extreme close-up detail.",
    "Low angle, slightly dramatic.",
    "Over-the-shoulder framing.",
    "Soft slow zoom composition.",
]

# Each beat: (narration_line, base_visual_prompt, num_shots)
# narration_line == "" means it shares/continues the previous narration moment.
BEATS = [
    # ---------- PART 1: POV intro 0:00-0:42 (from handoff file) ----------
    ("Imagine knowing the universe is wrong.",
     "Chibi Albert Einstein standing alone in a dim classroom at night in front of a huge chalkboard covered in faint physics equations, single warm lamp", 1),
    ("Not slightly wrong.",
     "Extreme close-up of a dark chalkboard covered in handwritten white chalk physics equations, drifting chalk dust", 1),
    ("Completely wrong.",
     "A tall stack of thick worn physics textbooks on a wooden desk lit by warm window light", 1),
    ("Every scientist believes it.",
     "A crowded old lecture hall full of chibi bearded scientists in dark suits all nodding in agreement", 1),
    ("Every professor teaches it.",
     "A stern chibi professor with glasses pointing a stick at a blackboard, lecturing", 1),
    ("And somehow...",
     "Tiny lonely chibi Einstein standing small and isolated facing a large crowd of identical chibi scientists", 1),
    ("I'm the only one who can see it.",
     "Tight close-up of young chibi Einstein's thoughtful determined face lit by a single lamp in darkness", 1),
    ("But right now...",
     "Young chibi Einstein sitting alone at a small wooden school desk in an empty classroom", 1),
    ("Nobody thinks I'm special.",
     "Chibi young Einstein slumped sadly alone at his desk, rows of empty desks around him", 1),
    ("My teachers certainly don't.",
     "A tall stern chibi teacher looming over a tiny nervous chibi Einstein at a desk", 1),
    ("They want answers.",
     "A chibi teacher holding out a test paper demandingly toward the viewer", 1),
    ("I only have questions.",
     "Chibi Einstein at a desk with glowing question marks floating above his curly head", 1),
    ("Questions are dangerous here.",
     "Chibi Einstein nervously raising one hand in class while other chibi students stare", 1),
    ("They make adults uncomfortable.",
     "An annoyed frowning chibi teacher glaring down at little chibi Einstein", 1),
    ("Why does light move the way it does?",
     "Chibi Einstein sketching glowing yellow light rays and a sunbeam in a notebook", 1),
    ("What is time?",
     "Close-up of an antique brass pocket watch held in small chibi hands, warm glow", 1),
    ("What is gravity?",
     "A single red apple falling from a leafy tree branch against a beige sky, chibi storybook", 1),
    ("And why does reality behave the way it does?",
     "Chibi Einstein from behind gazing out a tall window at a deep starry night sky", 1),
    ("Then one day...",
     "A warm glowing doorway opening, the gentle silhouette of a chibi father stepping into a child's cozy room", 1),
    ("My father shows me a compass.",
     "A chibi father kneeling down handing a shiny brass compass to a wide-eyed little chibi Einstein, warm light", 1),

    # ---------- PART 2: continuation script 0:42 onward ----------
    ("The needle moved. But nothing touched it.",
     "Extreme close-up of a brass compass in a child's hands, the red needle pointing, soft glow", 2),
    ("No strings. No hands. No visible force.",
     "Little chibi Einstein staring in wonder at the glowing compass needle in his palms", 2),
    ("That moment haunted him.",
     "Chibi Einstein lying awake in bed at night, the glowing compass on the nightstand", 2),
    ("If invisible forces existed, what else was hiding beneath reality?",
     "Dreamy chibi Einstein surrounded by faint glowing magnetic field lines and floating question marks", 2),
    ("That question would consume the rest of his life.",
     "Small chibi Einstein looking up at an enormous swirl of stars and galaxies in a warm night sky", 3),
    ("Fast forward. Einstein isn't a famous scientist.",
     "Exterior of a quaint old Swiss patent office building, cobblestone street, warm afternoon", 2),
    ("He's not even a university professor. He's a clerk.",
     "Chibi adult Einstein in a plain clerk's suit standing at a tall office counter with stamps and papers", 2),
    ("Every day. The same desk. The same papers.",
     "Chibi Einstein at a cluttered desk buried under towering stacks of paperwork and ink stamps", 3),
    ("But inside his mind, something extraordinary was happening.",
     "Chibi Einstein daydreaming at his patent-office desk, eyes soft, faint glowing ideas swirling above him", 3),
    ("He began running thought experiments.",
     "Chibi Einstein imagining himself riding on a glowing beam of light through a starry sky", 2),
    ("Imagine riding a beam of light. What would you see?",
     "A vintage steam train moving through warm countryside, chibi Einstein leaning out a window watching a light beam", 3),
    ("Nobody knew. Because nobody had ever asked.",
     "Stylized visualization of a bright golden light beam streaking across a dark cosmos, chibi storybook", 2),
    ("Then he asked another question. What if time isn't fixed?",
     "Several old clock towers at different angles, hands at different times, warm dusk sky, chibi", 3),
    ("What if it changes?",
     "Surreal soft-melting pocket watches draped over a desk, cozy storybook version of melting clocks", 2),
    ("At the time, this sounded ridiculous. Time was time.",
     "Chibi scientists laughing and waving dismissively at a small earnest chibi Einstein", 2),
    ("In 1905, everything changed.",
     "Chibi Einstein writing intensely by candlelight late at night, papers scattered everywhere", 3),
    ("Einstein published four papers. Not one. Four.",
     "Four glowing old scientific journal papers fanned out on a wooden desk, warm light", 3),
    ("Each capable of making someone famous. Together they transformed physics forever.",
     "A montage of small glowing science icons - atoms, light, energy - swirling around chibi Einstein", 3),
    ("He showed that space and time were connected. Not separate. One fabric.",
     "A glowing grid of spacetime stretching through stars, chibi Einstein gesturing at it", 3),
    ("Mass bends space. And that bending is what we call gravity.",
     "A planet sitting on a stretched glowing grid, warping it into a funnel, stars around, chibi style", 3),
    ("Imagine discovering that reality itself works differently than everyone believes.",
     "Iconic chibi Einstein portrait with wild curly hair, warm beige background, gentle confident smile", 2),
    ("Many didn't believe him. Some mocked him.",
     "A group of stern chibi scientists arguing and pointing fingers across a debate table", 2),
    ("Others ignored him entirely.",
     "Chibi Einstein sitting alone at a table while other chibi scientists turn their backs", 2),
    ("Because every revolutionary idea begins the same way. Alone.",
     "A single small chibi Einstein under a spotlight in a vast dark empty hall", 3),
    ("Then came 1919. A solar eclipse.",
     "A dramatic solar eclipse, golden corona around a black sun, warm storybook sky", 3),
    ("Scientists tested Einstein's prediction. And it worked.",
     "Chibi scientists with a big telescope on a tropical hill observing the eclipse, excited", 3),
    ("Overnight, he became the most famous scientist on Earth.",
     "Old newspapers spinning with headlines and a chibi Einstein portrait, sepia tones", 3),
    ("The world fell in love with the genius. But few noticed the cost.",
     "A big cheering chibi crowd surrounding and reaching toward chibi Einstein", 3),
    ("Fame followed him everywhere. Every speech. Every photograph.",
     "Chibi Einstein on a stage blinded by old flash cameras and a sea of reporters", 3),
    ("Yet despite being surrounded by people, he often seemed alone.",
     "Chibi Einstein sitting quietly alone on a chair while a blurry crowd passes around him", 3),
    ("Because genius solves many problems. Loneliness isn't always one of them.",
     "A single chibi Einstein in a large empty room by a window, long soft shadows", 3),
    ("Then came darker times. Nazism was rising. Europe was changing.",
     "An ominous darkening European city skyline at dusk, long shadows, cold grey-brown tones, chibi", 3),
    ("As a Jewish scientist, Einstein became a target.",
     "Small chibi Einstein looking worried as a huge dark shadow of marching boots looms behind him, no symbols", 2),
    ("He left Germany. Never to return.",
     "Chibi Einstein with a suitcase standing at the railing of a steam ship leaving a European harbor at dusk", 3),
    ("America became his new home.",
     "Chibi Einstein arriving at the warm ivy-covered buildings of Princeton University, autumn trees", 3),
    ("But another dilemma awaited him.",
     "Older chibi Einstein with grey wild hair looking thoughtful in a cozy study", 2),
    ("One that would trouble him for the rest of his life.",
     "Older chibi Einstein gazing out a window with a heavy worried expression", 2),
    ("His discoveries helped pave the road toward nuclear weapons.",
     "A distant ominous glowing mushroom cloud on the horizon seen across a quiet field, muted storybook", 3),
    ("Einstein never built the bomb. Yet many associated his name with it.",
     "Older chibi Einstein looking down sadly, a faint reflection of a mushroom cloud in his glasses", 3),
    ("He spent years advocating for peace.",
     "Older chibi Einstein speaking earnestly at a podium with a small dove and peace imagery", 3),
    ("Trying to prevent humanity from destroying itself.",
     "Older chibi Einstein holding a small glowing globe protectively in his hands", 2),
    ("Imagine understanding the universe better than almost anyone alive.",
     "A warm view of planet Earth glowing softly against a starry cosmos, storybook", 3),
    ("And still worrying about whether humanity would survive.",
     "Tiny older chibi Einstein silhouette gazing up at the glowing Earth and stars", 2),
    ("As he grew older, he became obsessed with one final dream.",
     "Older chibi Einstein walking alone down a quiet tree-lined Princeton path in autumn", 3),
    ("A theory that explained everything. Every force. Every law.",
     "A chalkboard filled with glowing interconnected equations forming a beautiful unified pattern", 3),
    ("For decades he searched. And failed.",
     "Older chibi Einstein staring exhausted at a vast chalkboard covered edge to edge with equations", 3),
    ("The universe had given him many answers. But not this one.",
     "Older chibi Einstein sitting head-in-hand, deep in thought, a single equation glowing faintly", 2),
    ("Perhaps that's the strange thing about knowledge. The more you learn, the bigger the mystery becomes.",
     "Chibi Einstein small beneath an immense breathtaking starry night sky, awe", 3),
    ("Einstein showed us that time can bend. Space can curve. Reality can surprise us.",
     "A dreamy galaxy spiral glowing in warm gold and deep blue, storybook cosmos", 3),
    ("But his greatest lesson wasn't physics.",
     "Gentle iconic chibi Einstein portrait, warm beige background, kind eyes", 2),
    ("It was curiosity.",
     "A small chibi child looking up wide-eyed at a sky full of stars", 3),
    ("The willingness to ask questions nobody else asks.",
     "A chibi child peering through a brass telescope on a hill at night, glowing stars", 3),
    ("To doubt assumptions. To challenge certainty. To wonder.",
     "A dreamy swirling cosmos of planets, comets and stars in warm storybook colors", 3),
    ("Because the discovery that changed the world began with a simple thought.",
     "Composite of chibi Einstein's face merging softly into a starry cosmos, warm tones", 3),
    ("A child staring at a compass. Wondering why the needle moved.",
     "Close-up of the brass compass again in small child's hands, glowing softly, full circle", 3),
    ("And maybe that's what made Einstein different. Not intelligence. Not equations. Not fame.",
     "Slow gentle zoom on a warm iconic chibi Einstein portrait, soft smile", 3),
    ("Just an unwillingness to stop asking why.",
     "Chibi Einstein looking up at a vast field of glowing stars, hopeful", 3),
    ("The universe is still filled with mysteries. Questions nobody can answer. Ideas waiting to be discovered.",
     "A sweeping panorama of a glowing cosmos, nebulae and countless stars, warm storybook", 4),
    ("And somewhere, the next person who changes the world might simply be a curious child.",
     "A small chibi child silhouette standing on a hill looking up at the enormous starry sky", 3),
    ("Looking at something ordinary. And refusing to look away.",
     "Chibi child holding a small ordinary object, staring at it with intense wonder, warm glow", 3),
    ("Albert Einstein spent his life trying to understand reality.",
     "Chibi Einstein silhouette against a soft glowing sunset-and-stars horizon", 3),
    ("The remarkable thing is, he showed us that reality is far stranger than anyone imagined.",
     "A gentle fade of chibi Einstein dissolving into a sky full of warm glowing stars", 3),
    ("And perhaps that's still true today.",
     "Cozy end card: a warm starry storybook sky with a softly glowing lightbulb, space for a channel logo, 'Food For Thought' mood", 3),
]


def build():
    style = STYLE
    storyboard = []
    narration_lines = []
    idx = 0
    for beat_i, (line, visual, shots) in enumerate(BEATS):
        if line:
            narration_lines.append(line)
        for s in range(shots):
            framing = FRAMING[(beat_i + s) % len(FRAMING)]
            prompt = f"{visual}. {framing} {style}"
            idx += 1
            storyboard.append({
                "n": idx,
                "beat": beat_i + 1,
                "narration": line,
                "prompt": prompt,
                "file": f"img_{idx:03d}.png",
            })
    return storyboard, narration_lines


if __name__ == "__main__":
    sb, lines = build()
    with open("storyboard.json", "w") as f:
        json.dump(sb, f, indent=2)
    with open("narration_full.txt", "w") as f:
        f.write("\n".join(lines))

    # Per-beat manifest: each narrated beat with its images, for per-beat TTS
    # and precise pacing/sync in assembly. Each beat is generated with a single
    # image call using count=N to produce N framed variations of the scene.
    beats = []
    for beat_i, (line, visual, shots) in enumerate(BEATS):
        imgs = [s["file"] for s in sb if s["beat"] == beat_i + 1]
        gen_prompt = f"{visual}. {STYLE}"
        beats.append({
            "beat": beat_i + 1,
            "narration": line,
            "audio": f"beat_{beat_i + 1:03d}.mp3",
            "gen_prompt": gen_prompt,
            "count": len(imgs),
            "images": imgs,
        })
    with open("beats.json", "w") as f:
        json.dump(beats, f, indent=2)

    full = " ".join(lines)
    print(f"Total images: {len(sb)}")
    print(f"Total beats: {len(beats)}")
    print(f"Full narration chars: {len(full)}, words: {len(full.split())}")
