# Snorricam

**Status:** verified. One of the two best results in the library.
**Effect:** the camera is rigidly attached to the subject's body. Their face holds dead centre at constant
size while the entire world lurches and swings behind them.
**Primitives:** none, directly. This is a **described result**, not a composition — and that is why it works.
**Reference:** *Requiem for a Dream*; Aronofsky and Gaspar Noé.

## Shot line

> {SUBJECT} {WALK_VERB} while the camera, fixed rigidly to {PRONOUN}, holds {FACE} locked dead-centre at
> exactly the same size and position throughout; the whole background lurches, sways and swings behind
> {PRONOUN} {STRIDE}.

## Never name the rig

The first version named a *"Snorricam body rig"* in the gear line and **H3 rendered the rig in frame**. Real
problem, immediate fix: delete the gear reference and describe the *effect*. The shot line above names no
equipment at all.

This is the general rule. **Never name a rig a camera could see.** `../references/gear.md`.

## What a correct snorricam measures

| | value | reading |
|---|---|---|
| subject scale | **0.99x** | locked — the defining requirement |
| shake | 3.94 / 2.70 px vs 0.11 locked | the world lurches |
| pan | **absolute 43%, net 1%** | swings out and returns |

⭐ That **absolute-43% / net-1%** split is the signature. An ordinary pan drifts one way and stays; a
snorricam swings and returns while the face never moves.

## Framing

Open where it ends. The subject's scale never changes, so there is no range to open into. This is the
exception to the wide-opening rule. `../references/framing.md`.

A tight head-and-shoulders crop works and does **not** cost the background parallax, which was the worry —
background objects still cross frame-left to frame-right. Ask for the crop explicitly; a 14mm will not
produce it.

## ⚠️ The trap: do not create background motion by moving the subject

This shot generated the library's most instructive retraction.

A version that added a curve to the walk plus a red barn, a fence and an oak looked dramatically better and
was judged **worse**. So was a tighter-cropped follow-up. The plain straight walk across an empty meadow won.

| | staging | x drift | y drift | verdict |
|---|---|---|---|---|
| **plain** | straight walk, empty meadow | **0.67%** | **0.78%** | ✅ **best** |
| + staging | turn + barn, fence, oak | 0.88% | 1.63% | worse |
| + tight crop | turn + barn, tight crop | 1.72% | 1.37% | worse |

**The turn bought background drama and spent the lock, and the lock IS the shot.** On a subject-locked shot,
move the camera or stage objects the *camera* passes. Never add subject movement to reveal the world.

⭐ And no metric in the project could see this: every axis measured the camera or the subject's *scale*, and
none measured whether the face holds its *position*. The person judging was working on an axis the
instrumentation did not have.

## Gotchas

- The subject must **walk**, not swivel. An early template said *"standing completely still"* on every shot,
  which contradicted this one outright and is almost certainly why the first attempt swivelled in place.
- *"Never once looking at the camera"* is worth stating. A subject who acknowledges a body-mounted lens breaks
  the illusion that it is not there.

## Machine-readable

```json
{
  "id": "D-01",
  "slug": "snorricam",
  "name": "snorricam shot",
  "status": "verified",
  "motion": "walk",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "{SUBJECT} {WALK_VERB} while the camera, fixed rigidly to {PRONOUN}, holds {FACE} locked dead-centre at exactly the same size and position throughout; the whole background lurches, sways and swings behind {PRONOUN} {STRIDE}.",
  "extra_slots": {},
  "performance_note": "Keep it minimal and forward-facing. e.g. \"walks with hard, fixed determination, eyes locked forward, jaw tight, never once looking at the camera\". Do NOT add turns or direction changes.",
  "gear_warning": "Do not name a body rig in the gear slot. H3 will render it.",
  "subject_warning": "The subject has to be travelling under its own power, because the camera is attached to it. A static object cannot carry this shot; a vehicle or a machine in motion can."
}
```

## Prompt as it ran

`prompts/D-01_snorricam.txt`
