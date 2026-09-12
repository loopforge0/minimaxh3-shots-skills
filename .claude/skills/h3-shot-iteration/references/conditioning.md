# Reference conditioning

The single biggest finding in this project, and the one most likely to be costing you a camera move right now.

## A reference plate pins framing, and a camera move needs framing free

Controlled A/B. Identical prompt, identical seed, identical settings — **only the plates differed.**

| Config | Background transform | Identity | Scenery drift |
|---|---|---|---|
| **identity plate only** ← the default | **0.47x** ✅ full move | ✅ held | 0.08 |
| identity + background plates | 0.81x ⚠️ roughly halved | ✅ held | 0.02 ✅ locked |
| no plates, all text | 0.46x ✅ full move | ❌ invented | 0.15 |

Scenery drift: 0 means the scene persists through the shot, higher means the model re-invents it as it goes.

**It is the ENVIRONMENT plate that costs you motion. A character plate costs nothing.** A whip pan ran two
character plates and produced the fastest move in the entire set.

## So the trade is explicit

A background plate buys about a **4x reduction in scenery drift** and costs about **half the camera move**.
That is the whole transaction. Adding one is a deliberate decision *against* the shot, so make it knowingly.

What you are accepting without one: the environment *content* drifts. In one verified dolly zoom a drum kit
became a grand piano by the end of the shot. The camera move was correct throughout.

If a locked environment matters more than the move — a product shot, a matched cut, anything that has to
intercut — take the background plate and accept the halved motion.

## The scaffold wording matters as much as the plate count

An earlier scaffold anchored the plate as a first frame:

```text
<Picture 1> is the first frame of [Shot 1], establishing both <Subject 1> and the environment: …
summary:
[keyframe completion] The target video continues from <Picture 1> …
[Shot 1] … begins in the position and framing established by <Picture 1> …
```

**That form pins the opening composition and roughly halves the move.** It was only ever validated in runs
where the reference image was being silently dropped, so it had never actually been tested with a plate
attached.

Three rules follow:

1. **`[reference generation]`, not `[keyframe completion]`.** The plate is an identity reference, not a frame
   the video continues from.
2. **Never call the plate "the first frame"**, and never say the shot *"begins in the position and framing
   established by"* it.
3. **Keep the environment out of the plate.** Describe it in text.

⚠️ **One dissent on the record, and it is unresolved.** The best dolly zoom in the whole project was generated
on that banned legacy scaffold, and the project's test runner now *throws* on it — so the guard currently
blocks the best-performing recipe there is. The rule above is right on the controlled A/B and the exception is
real. If you are chasing a subject lock and nothing else works, that is a thing worth trying.

## `ref_image_size`

**`max`.** On `match` the plate renders as frame 0 and the subject is missing for roughly the first 16 frames.

## Reference video

**No.** Tested twice, with the connection verified the second time.

| | subject lock | frame-margin energy | reading |
|---|---|---|---|
| the clip used **as** the reference | 1.16x, background 0.52x | — | a strong dolly zoom |
| the generation referencing it | 1.15x | **11.27** ← lowest of the set | locked, but moved least |
| a composed version, no reference video | 1.88x | 19.99 | moved most, lock failed |

A locked subject in a shot where little happens is not evidence of transferred motion. The reference clip's own
strong background recession was not reproduced, and the background shifted *laterally* rather than warping in
depth. An earlier test with a different reference clip was cleaner: the output stayed static at 1.01x while the
reference itself measured 0.34x. **No motion transfer.**

⚠️ Not a clean negative either — the lock did improve, and the decisive background measurement was unavailable
in that scene. It was later judged a pass by eye, which reopens the question. **Treat reference video as
unproven rather than useless**, and do not spend an iteration on it expecting a camera move.

## Multiple characters

Free. Two plates for a whip pan, three for a rack focus, no measurable cost to camera motion in either.

Wire them in order and remember `<Picture N>` is **positional** — the number comes from the wiring order in the
node, not from anything written in the prompt.
