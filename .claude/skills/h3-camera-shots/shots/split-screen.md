# Multi-Panel Split Screen

**Status:** verified on layout, **uncontrollable on timing**
**Effect:** three vertical panels side by side show the same action from three different angles, revealed one
at a time, unopened panels solid black.
**Primitives:** none. There is no layout primitive and no timed-event primitive in H3's vocabulary.
**Reference:** *The Thomas Crown Affair* (1968), *Requiem for a Dream*.

## Shot line

This shot's "shot line" is most of the prompt, because the layout has to be described panel by panel.

> The frame is divided into three equal vertical panels side by side, separated by thin black gutters. The
> left panel holds {SUBJECT}, {ACTION}. Every panel is locked off and completely static; nothing pans, zooms
> or moves at any point. The three panels open one after another. The left panel plays from the very first
> frame, showing {PANEL_1_ANGLE}, while the centre and right panels are solid black. The centre panel comes on
> next, showing the same moment from {PANEL_2_ANGLE}. The right panel comes on last, showing {PANEL_3_ANGLE}.
> For the rest of the shot all three panels play together in perfect sync, the same continuous {ACTION_SHORT}
> at the same instant from three different angles.

## What worked, first attempt

| panel | angle | measured onset |
|---|---|---|
| left | her left side, in profile, typing | **0.00s** |
| centre | from the front, over the back of the monitor, screen glow on her face | **1.67s** |
| right | from behind, her back and the monitor | **2.46s** |

Unopened panels measured **0.0 mean luminance** — genuinely black, not dim. Typing stayed in sync across all
three once open.

⭐ Neither a layout nor a timed event has any primitive behind it, and H3 produced both. Expectation going in
was that the layout might land and the timing certainly would not.

## ⚠️ The timing is not yours

A second run asked for 2.0s and 4.0s instead of 1.5s and 3.0s:

| | left | centre | right | gaps |
|---|---|---|---|---|
| asked (v2) | 0s | **2.00s** | **4.00s** | 2.00 / 2.00 |
| v1 got | 0.00s | 1.67s | **2.46s** | 1.67 / 0.79 |
| v2 got | 0.00s | **0.83s** | **2.46s** | 0.83 / 1.62 |

It **swapped** the gaps, and the centre panel moved *earlier* despite being asked for later. **The right panel
opened at 2.46s in both runs**, from two materially different prompts.

**Read: H3 has its own reveal schedule — everything is on screen inside the first ~2.5s of an 8s clip — and
the prompt shifts only how the earlier gap is divided, not when it finishes.**

So: **you can ask H3 to stagger a reveal; you cannot choose when.** State the order, not the times. If exact
timing matters, cut the panels in an editor. ⚠️ n=2.

## It needs 192 frames

Two staggered reveals plus a shared run-out cannot fit in 5 seconds. `../references/settings.md`.

## Gotchas

- **Say "solid black", and say it about each unopened panel.** That is what produced genuine 0.0 luminance
  rather than a dim or crossfaded panel.
- **Lock every panel off explicitly.** *"Nothing pans, zooms or moves at any point"* — otherwise one panel will
  find a camera move of its own.
- The three angles must be angles on the **same action at the same instant**, stated as such, or you get three
  unrelated clips.
- Give the subject one continuous action that reads from every angle. Typing works; anything with large
  travel does not fit three narrow panels.

## Machine-readable

```json
{
  "id": "D-04",
  "slug": "split-screen",
  "name": "three-panel split screen",
  "status": "verified-layout-only",
  "summary_action": "{ACTION_SHORT}",
  "length": 192,
  "framing": "custom, described in the shot line",
  "framing_summary": "a frame divided into three equal vertical panels",
  "shot_intro": "custom",
  "subject_action": "described per panel",
  "shot_line": "The frame is divided into three equal vertical panels side by side, separated by thin black gutters. The left panel holds {SUBJECT}, {ACTION}. Every panel is locked off and completely static; nothing pans, zooms or moves at any point. The three panels open one after another. The left panel plays from the very first frame, showing {PANEL_1_ANGLE}, while the centre and right panels are solid black. The centre panel stays solid black and then comes on, showing the same moment from {PANEL_2_ANGLE}. The right panel stays solid black longer than the centre one and comes on last, showing {PANEL_3_ANGLE}. For the remainder of the shot all three panels play together in perfect sync, the same continuous {ACTION_SHORT} at the same instant from three different angles.",
  "extra_slots": {
    "ACTION": "the one continuous action, with its setting, e.g. \"seated at a cluttered desk typing on a keyboard, a bright monitor in front of her\"",
    "ACTION_SHORT": "the action in two words, e.g. \"typing\"",
    "PANEL_1_ANGLE": "e.g. \"her from her left side in profile as she types\"",
    "PANEL_2_ANGLE": "e.g. \"the front, framed over the back of the monitor with the screen glow on her face\"",
    "PANEL_3_ANGLE": "e.g. \"her from behind in full, her back and the bright monitor in view\""
  },
  "timing_warning": "Do not state absolute times. They are not honoured. State the order only."
}
```

## Prompt as it ran

`prompts/D-04_multi-panel-split-screen.txt` — note it *does* state absolute times (2s and 4s), and those are
exactly the instructions that were not honoured. Kept as-is because that is what ran.
