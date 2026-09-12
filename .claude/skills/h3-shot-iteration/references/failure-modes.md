# Failure modes

Symptom, cause, fix. Everything here happened at least once.

## Barely any camera motion

| Cause | Fix | Evidence |
|---|---|---|
| 4-step turbo render | 20 steps, turbo LoRA off | Motion almost entirely suppressed at 4 steps regardless of prompt |
| A background reference plate | Drop it, environment in text | Background transform 0.81x with, 0.47x without |
| An impossible subject instruction | Ask for natural motion | *"holds one single pose completely rigid"* cost 80% of the camera travel |
| The legacy first-frame scaffold | `[reference generation]`, never call the plate the first frame | Roughly halves the move |
| `with small amplitude` on a compound move | Remove it | Damping one of two opposing primitives collapses the effect |
| Equipment named in an audio slot | Never name camera, lens, rig or move in audio | *"an array of still cameras fired in sequence"* collapsed motion from 108% to 22% |

## The move happens but it reads as the wrong shot

| Symptom | Cause | Fix |
|---|---|---|
| A dolly in looks like a zoom in | Nothing near the lens | Put two objects at the left and right frame edges for the camera to pass and sweep out |
| A 360 orbit is a small curve | Modifiers omitted | `with large amplitude at fast speed`. Peak travel 72 → 203 px/step |
| A whip pan glides instead of spiking | No destination | Name where it lands. 23 → 218 px/step |
| No motion blur on a fast move | You asked for blur | You cannot. The destination produces the speed and the speed produces the blur |
| An "extreme wide" opening is not wide | You asked for a wide lens | Ask for wide framing. An 8mm rendered pixel-identical to a 50mm |
| A crane rise never gets overhead | Subject is stationary | It is a tracking shot. The subject has to run |
| A handheld reads as a defect | Subject is stationary | Shake has to be earned by motion |

## Framing ran out of room

**Open at whichever end of the range the subject is LARGEST.** Two shots in the same scene from the same
waist-up default: the one that had to end wide passed, the one that had to end tight failed and was called *"not
a super dolly at all"*. Given an explicit extreme-wide opening its subject range went 3.08x → 7.42x.

**Exception:** subject-locked shots (dolly zoom, snorricam) open where they end.

## The subject grows when it should be locked

**Unsolved.** This is the dolly zoom's remaining failure and there is no known lever.

- `at slow speed` was added specifically to tighten the lock. **The lock got worse** (1.57 → 1.88x).
- Stacking absolute invariant clauses is the current best attempt: framed identically in the last frame as the
  first, never drifts from centre, faces the lens squarely, rooted to one spot, does not step or lean.
- The background half of the recipe ports fine. Only the lock fails.
- Lock detail on a failing take: horizontal drift 3.15%, vertical 10.13%, size variation 13.3% — the subject is
  wandering, not just growing.

## One frozen expression for the whole clip

The performance was written as a **state** instead of a **change**. *"Runs hard and open-faced, breath
clouding"* held a single open-mouthed frame for eight seconds.

Write the arc and its timing: *"easing out of hard concentration into open delight"*, *"the change building
through the middle of the shot and settling into a held stillness by the end"*.

❌ **Not the cause, and it was tested:** a soundscape line reading *"breathing stays audible throughout"*. A
shot that kept it and dropped only the **visual** breathing cues came back mouth-closed, as did two others
carrying the same line. The expensive fix was not the necessary one.

On any running shot, **state lips closed and jaw relaxed explicitly.**

## A camera rig is visible in frame

The gear slot named something the camera could see. *"Snorricam body rig"* rendered the rig.

**Describe the effect, not the equipment.** Crane, dolly, gimbal and tripod are safe because they sit behind
the camera. Anything mounted to the subject is not.

## Everything happens in the first 2.5 seconds

H3's own schedule, and **not fixable from the prompt.**

| Asked | Got |
|---|---|
| reveals at ~1.5s and ~3.0s | 1.67s and **2.46s** |
| reveals at **2.0s and 4.0s** | **0.83s** and **2.46s** — the gaps swapped |
| zoom out, no pause, snap back | **3.5s of nothing**, then everything |

The last panel of a triptych opened at 2.46s in both runs from materially different prompts. The model picks a
window, compresses the action into it, and pads the rest. **State the sequence, never the timing.** Cut timing
in an editor. ⚠️ n=3 across 2 shots.

## The environment changes mid-shot

Working as intended, and it is the price of the camera move. No background plate means the scene is re-invented
as it goes — a drum kit became a grand piano in one verified take. `conditioning.md` has the trade.

## The reference image seems to have been ignored

It probably was. ComfyUI's autogrow inputs need flat dot-notation keys (`ref_images.ref_image_0`). The nested
form validates, reports success, and silently discards the reference.

```bash
node scripts/verify_refs.mjs <workflow.json>
```

Four gear comparisons in this project ran with no reference at all, invented four different characters in four
different scenes, and were compared as if only the lens differed. The recorded finding from that tier was false
and had to be retracted.

## A generated reference plate produces nothing usable

Check it is not black. One image checkpoint wrote valid, entirely black PNGs while reporting success — suspected
fp8 numerical overflow under `--fast fp16_accumulation`.

```bash
ffmpeg -v error -i plate.png -vf scale=1:1 -f rawvideo -pix_fmt gray - | od -An -tu1
# 0 = black frame, generation failed
```

## A three-phase shot never completes

Frame count. 96 and 124 cannot hold out-hold-return, or two staggered reveals plus a run-out. **192 frames.**
Lengths must satisfy `% 17 == 5`: 124, 192, 243, 362.
