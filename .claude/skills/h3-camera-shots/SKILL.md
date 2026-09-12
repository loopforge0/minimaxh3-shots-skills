---
name: h3-camera-shots
description: Write MiniMax H3 prompts for a named camera shot - dolly zoom, crash zoom, whip pan, snorricam, 360 orbit, crane rise, aerial pullback, handheld, yo-yo zoom, dutch angle, eyes-in, rack focus, split screen, super dolly in. Use when a request names a camera move, a film shot or a director's shot, when a generated shot has the wrong camera motion, or when composing the camera clause of a Ref2VA / T2VA prompt. Pairs with MiniMax's own h3-prompt-writing skill, which owns the prompt format.
compatibility: Reads local files only. No API calls, no proprietary runtime. Works in any agent that can read a directory.
---

# H3 camera shots

H3 has **twelve documented camera primitives and no named compound shots**. There is no "Dolly
Zoom" button. Every named film shot has to be built out of the twelve, in a sentence, inside a
prompt whose format MiniMax defines.

This skill owns the **camera clause**. It does not own the prompt format.

## Before anything else: load the upstream format

MiniMax's own guide is the authority on section names, order and reference labels. Getting the
camera clause right inside a malformed prompt gets you nothing.

1. Read `references/upstream.md`. It says where the guide lives and how to fetch it.
2. If `h3-prompt-writing` (MiniMax's skill) is installed, invoke it and follow its structure.
3. Only then come back here for the camera clause.

Everything below assumes **Ref2VA** with one character reference image, which is the mode all of
these shots were developed and verified in. `references/scaffold.md` is the filled-in six-section
skeleton.

⚠️ **Two things were tested on one setting only, and both are now parameterised.** Every shot was
developed on **human** subjects, so an animal, a bird or an inanimate object uses a vocabulary that is
reasoned rather than measured (`references/subjects.md`). And each shot writes **one direction** -
the one that was rendered - so a left whip pan or a clockwise roll is a documented primitive with no
render behind it here (`references/direction.md`). Neither is a reason not to use them. Both are a
reason to judge the first generation.

## Workflow

1. **Find the shot.** `shots/INDEX.md` lists every shot, what a viewer actually sees, and which
   primitives it composes. Read that shot's file.
2. **Build the prompt** from `references/scaffold.md`, dropping the shot's *shot line* into the
   `{SHOT_LINE}` slot and substituting its placeholders.
3. **Set the opening framing the shot asks for.** This is the single most common reason a shot
   comes back wrong, and each shot file states its requirement. `references/framing.md` has the
   rule.
4. **Check the four rules below.**
5. **Use the settings in `references/settings.md`.** Some of them are load-bearing; a 4-step turbo
   render suppresses camera motion almost entirely, regardless of how good the prompt is.
6. **Judge it, then iterate.** That is the `h3-shot-iteration` skill.

## The four rules

**1. Camera motion is TYPE + AMPLITUDE + SPEED.** From the documented twelve, written as an action
in the sentence rather than labels bolted on the end. State amplitude and speed when the shot's
identity depends on being large or fast; omit them for a medium, normal move. `with large amplitude
at fast speed` took a 360 orbit from a small curve to a genuine circle. Vocabulary and the measured
effect of each modifier are in `references/camera-grammar.md`.

**2. Open at whichever end of the range the subject is LARGEST.** A shot that must *end* tight has
to *open* wide, or it has nowhere to travel. A shot that must end wide opens tight. Shots where the
subject stays locked (dolly zoom, snorricam) open where they end, because their scale never
changes. A super dolly in inherited a waist-up opening once and read as a plain zoom.

**3. State the observable result, not a stylistic label** - but get the verbs right first. "so that
her size and position in frame stay exactly constant throughout" beats "static framing". The
primitive verbs outrank the result clause though: one prompt described wide behaviour in its result
clause while its verbs asked for telephoto, and the verbs won.

**4. Never ask for something the model cannot do.** An impossible instruction is not ignored, it
drags the whole shot down. Asking a subject to hold "one single pose completely rigid" cost about
80% of the camera move in an otherwise identical prompt. Details in `references/performance.md`.

## Things that are not levers

Read these before spending an iteration on them.

| | |
|---|---|
| **Lenses and camera bodies** | Cosmetic. Swapping Cooke S4 50mm / Petzval 8mm / Zeiss 75mm produced nothing a viewer calls a difference. Gear only matters when it names something that would be **in the scene**. `references/gear.md` |
| **Event timing** | You can state a sequence. You cannot place events in time. Two prompts asking for reveals at 3.0s and 4.0s both delivered 2.46s. Cut timing in an editor. |
| **`with small amplitude`** | Nearly inert on a single primitive - 1.47x against a 1.53x control. It is not a brake. |
| **Reference video** | Transferred no camera motion in two tests. An identity image does the identity work. |
| **Asking an object to hold still** | For a *person*, "completely still" costs you the shot. For an inanimate subject the life clause moves to the world around it instead - `references/subjects.md`. |
| **A background reference plate** | Halves the camera move. It buys a locked environment; spend it knowingly. `../h3-shot-iteration/references/conditioning.md` |

## What is in here

| Path | What it is |
|---|---|
| `shots/INDEX.md` | All fourteen shots, one line each |
| `shots/*.md` | One recipe per shot: effect, primitives, shot line, framing, gotchas |
| `references/scaffold.md` | The six-section Ref2VA prompt skeleton with slot notes |
| `references/camera-grammar.md` | The twelve primitives, modifiers, and what each measured |
| `references/framing.md` | Opening framing, and the one shot that contradicts the rule |
| `references/performance.md` | Expression, "still" vs "frozen", and the audio slots |
| `references/gear.md` | Why the gear line is cosmetic, and the one case where it is not |
| `references/subjects.md` | **Subjects that are not people** - animal, bird and object vocabularies |
| `references/direction.md` | Which directions are slots, and which half of each pair was actually tested |
| `references/settings.md` | Generation settings that change whether the move happens at all |
| `references/upstream.md` | MiniMax's guide and skill, and how to fetch them |
| `../../../prompts/` | The exact prompts behind every verified shot, byte for byte |

## Provenance

Every rule here came out of roughly 80 generations on one subject set, developed at 864x480 on an
RTX 3060 and re-run at 1344x768 on a rented RTX 5090. Sample sizes are stated where they are small.
Several findings in this library replaced an earlier finding that turned out to be wrong; where that
happened, the retraction is written down rather than deleted, because the failure is usually more
useful than the rule.

## Path convention

Paths written as `prompts/…`, `scripts/…` or `.claude/skills/…` are relative to the **repository root**. Paths beginning `./` or `../` are relative to the file they appear in.
