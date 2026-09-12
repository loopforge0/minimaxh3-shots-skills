# Performance, and the audio slots

H3 generates picture and audio together, which makes both of these camera problems rather than
acting problems.

## "Still" must never mean "frozen"

An early template said *"standing completely still"* on every shot, and subjects stopped blinking and
breathing. It also silently contradicted the shots that need the subject **walking** or **running**,
which is almost certainly why a snorricam swivelled in place instead of walking.

| The shot needs | Write |
|---|---|
| A stationary subject | *"standing in place, breathing softly, hair and clothing stirring in the air, blinking and shifting her weight a little as people naturally do"* |
| A moving subject | *"running steadily through the tall grass, hair flying and clothing snapping with the movement"* - explicitly **walking** or **running** |
| Genuinely frozen | Don't. See below. |

## Describe an expression that CHANGES

A condition gets held as one rigid pose for the entire clip. One prompt asked for *"runs hard and
open-faced, breath clouding"* and H3 held a single open-mouthed frame for eight seconds. The
reference plate was innocent - it is a closed-mouth smile.

Write the arc and its timing instead:

> *expression shifts from blank and neutral into dawning realization and slight shock: her eyes
> widen and focus more intensely, her brow lifts and tightens, her lips part slightly, the change
> building through the middle of the shot and settling into a held, wide-eyed stillness by the end*

Verified across every shot in this library.

❌ **Disproved, and worth keeping as a disproof:** that a soundscape line reading *"breathing stays
audible throughout"* was what held a mouth open. A shot that kept that line and dropped only the two
**visual** breathing cues came back mouth-closed, as did two others carrying the same line. The
expensive fix was not the necessary one. **Visual cues stated as a condition are the cause.**

## An impossible instruction costs you the rest of the shot

Same subject, same rooftop, same camera clause (`arc shot with large amplitude at fast speed`):

| Subject instruction | Camera travel |
|---|---|
| natural motion | **98-108%** of frame width |
| *"holds one single pose completely rigid"* | **22%** |

Asking for natural motion is free. Asking for an impossibility is not ignored - it **drags the whole
shot down**, here costing about 80% of the camera move. H3 has a strong prior that people in video
move, and fighting it is expensive.

## The audio slots are performance instructions

Two rules, both learned the hard way.

**1. Never name the camera, lens, rig or move in an audio slot.** An audit found eight soundscape
slots mentioning "the camera". A *"low drone that climbs in pitch"*, meaning a sustained tone, is
ambiguous in a project that also flies actual drones. Nobody wants equipment sounds in a finished
shot. This is the audio twin of the rule about naming a rig that would be in frame.

**2. Specify positively and completely.** A negative instruction plants the idea. There is no
"without" that works here.

## You cannot place events in time

You can state a **sequence** and H3 honours the order. You cannot say when.

| Asked | Got |
|---|---|
| reveals at ~1.5s and ~3.0s of 8s | 1.67s and **2.46s** |
| reveals at **2.0s and 4.0s** of 8s | **0.83s** and **2.46s** - it swapped the gaps |
| zoom out, no pause, snap back | **3.5s of nothing**, then all of it in the last 4.5s |

The right panel of a triptych opened at **2.46s in both runs** from two materially different
prompts. The model picks a window, compresses the described action into it, and pads the remainder.

**State the sequence, never the timing.** If exact timing matters, cut it in an editor.
⚠️ n=3 across 2 shots. A suspected limit, not a proven one.
