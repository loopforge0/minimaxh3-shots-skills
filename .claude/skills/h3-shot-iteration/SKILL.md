---
name: h3-shot-iteration
description: Diagnose and fix a MiniMax H3 generation whose camera move came out wrong - no motion, a subject that drifts when it should be locked, a wrong-looking zoom, a frozen expression, a rig rendered in frame, a reference image that appears to have been ignored, or a black reference plate. Use when judging whether a generated shot reads as the intended shot, and when deciding what to change for the next attempt.
compatibility: Reads local files only. No API calls, no proprietary runtime.
---

# H3 shot iteration

A generation came back and it is not the shot you asked for. This skill is the diagnosis order.

Its companion `h3-camera-shots` owns writing the prompt in the first place.

## Check the rig before you rewrite the prompt

Roughly a third of the failures in this library's development were not prompt failures. Work down this list
first, because every one of them produces a plausible-looking wrong result with no error.

1. **Steps.** 20. A 4-step turbo render suppresses camera motion almost entirely, no matter what the prompt
   says. Turbo LoRA off.
2. **Frame count.** 124 minimum. Below that you are outside H3's trained range (124-362). Anything with three
   phases needs 192.
3. **Did the reference image actually attach?** ComfyUI's autogrow inputs silently discard a nested
   `ref_images` key — validates, reports success, drops the reference. Four gear comparisons in this project ran
   with **no reference at all**, invented four different characters in four different scenes, and were compared
   as if only the lens differed. `scripts/verify_refs.mjs` catches it.
4. **Is the reference plate black?** One image checkpoint wrote valid, entirely black PNGs and reported
   success. `ffmpeg -v error -i plate.png -vf scale=1:1 -f rawvideo -pix_fmt gray - | od -An -tu1`, and zero
   means a failed generation.
5. **Is there a background plate?** It halves the camera move. `references/conditioning.md`.
6. **`ref_image_size`.** `max`. On `match` the plate renders as frame 0 and the subject is missing for about
   16 frames.

Full table in `../h3-camera-shots/references/settings.md`.

## Then diagnose the shot

`references/failure-modes.md` is the lookup table: symptom, cause, fix, and what it measured. The common ones:

| Symptom | Most likely cause |
|---|---|
| Barely any camera motion | 4 steps, or a background plate, or an impossible subject instruction |
| The move is there but reads as the wrong shot | `Zoom` where you needed `Push`, or no foreground for the travel to register against |
| Ran out of room, ended too tight or too wide | Opening framing — open at the end of the range where the subject is largest |
| Subject grows when it should be locked | Unsolved on the dolly zoom. Stack invariant clauses; do not add `at slow speed`, it made it worse |
| One frozen expression for the whole clip | The performance was written as a state, not as a change |
| A camera rig visible in frame | The gear slot named a rig the camera could see |
| Everything happens in the first 2.5 seconds | H3's own schedule. Not fixable from the prompt |
| The environment changes mid-shot | No background plate. That is the trade you made for the camera move |

## Judging: a person decides, metrics are evidence

**This is the most useful thing in this repository and it is the least technical.**

Over one day of this project, three separate measurements confidently mis-described a shot. Over the project as
a whole, **four of its most confident written conclusions were overturned by watching the clips**, including one
that had been recorded as the headline finding.

| Recorded conclusion | What watching it showed |
|---|---|
| A prompt was "confounded" for naming a prime lens on a zoom shot, and measured 3.15x against 8.97x | That version was the keeper. Lenses do almost nothing, so the confound was never real |
| "The dolly zoom does not port" — three failed attempts | It ports. The failure was in the metric |
| A scaffold was banned for halving the camera move, and the test runner **throws** on it | The best dolly zoom in the project used it |
| "No clear motion transfer from a reference video" | Judged a pass, which reopens the question |

Every correction came from watching, not measuring. **Run metrics privately as a sanity check and never let one
outrank your eyes.** `references/judging.md` has the specific ways each axis lies, and which axis to pick per
shot.

## When a measurement returns nothing

Not neutral. **Weak evidence against the shot.** A background a feature tracker cannot follow is probably a
background that is not doing anything legible. Two dolly zooms were judged on half the evidence because their
scene had too little texture; re-shoot the test in a scene with trackable structure rather than trusting a blank.

## Iterating without going backwards

- **One variable per attempt**, and keep the seed. Three shots in this project changed precision *and* length
  at once and stopped being attributable to either.
- **Write down what each attempt disproved.** Two theories in this library were expensive and wrong, and both
  are recorded as disproofs so nobody re-runs them.
- **Do not fix a problem by deleting it from the prompt.** Removing a yo-yo zoom's hold shortened the hold and
  bought 3.5 seconds of dead opening instead. The dead time moved; it did not go away.
- **Do not make a move bigger to make it more visible.** Amplitude is not the lever, staging is — but on a
  subject-locked shot, never create background motion by moving the subject. That trade cost the lock, and on
  those shots the lock is the shot.

## What is in here

| Path | What it is |
|---|---|
| `references/failure-modes.md` | Symptom to cause to fix, with what each one measured |
| `references/conditioning.md` | The reference-plate A/B, in full |
| `references/judging.md` | How each measurement axis lies, and which to use per shot |

## Path convention

Paths written as `prompts/…`, `scripts/…` or `.claude/skills/…` are relative to the **repository root**. Paths beginning `./` or `../` are relative to the file they appear in.
