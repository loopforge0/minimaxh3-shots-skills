# Super Dolly In

**Status:** verified, after one failure that established the framing rule
**Effect:** the camera charges the whole length of a space toward the subject. Foreground objects sweep
out past the edges of frame as it passes them.
**Primitives:** `Push In` + `with large amplitude` + `at fast speed`
⚠️ **No canonical film shot.** This is a preset label borrowed from Higgsfield, so judge it against
described behaviour rather than against a reference film.

## Shot line

> The camera pushes in with large amplitude at fast speed, charging the entire length of {THE_SPACE}
> toward {PRONOUN}: {NEAR_OBJECTS} sweep outward past the edges of frame and out of shot as the camera
> passes them, {FURTHER_OBJECTS} rush by on both sides and {GROUND} streams underneath, and the move ends
> in a tight close-up with {FACE} filling the frame.

## Framing, and the shot that proved the rule

It must **end** tight, so it must **open** extreme wide.

| | opening | subject range | outcome |
|---|---|---|---|
| first attempt | waist-up medium close-up (inherited default) | 3.08x | ❌ *"not a super dolly at all"* |
| **verified** | **extreme wide, subject a speck at the far end** | **7.42x** | ✅ |

Write the opening explicitly. A wide **lens** will not do this. `../references/framing.md`.

## Foreground is not decoration, it is the shot

**Without near objects this is a crash zoom.** Distant geometry barely changes scale when a camera
translates, so a dolly in past nothing but a far treeline is indistinguishable from a zoom in, and what
you get is the zoom.

The verified version puts **two near trunks at the left and right edges of frame** and has the camera
pass them and sweep them out of shot. That parallax is the only thing separating this shot from
`crash-zoom-in.md`.

## Gotchas

- ⚠️ This shot's background motion has **never been measured** — one metric reported it unmeasurable
  and another returned 9.11x for the same clip. The verdict rests on the stills. Judge by eye.
- Both near objects need to exit frame. If they only slide inward the camera has not travelled far
  enough; push the opening wider rather than raising the amplitude.

## Machine-readable

```json
{
  "id": "C-03",
  "slug": "super-dolly-in",
  "name": "super dolly in",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "framing": "{WIDE_FRAMING_EXTREME} looks straight down {THE_SPACE}, {NEAR_OBJECTS} rising close at the left and right edges of frame, and places {SUBJECT} small and distant at the far end of it",
  "framing_summary": "an extreme wide shot",
  "shot_intro": "comma",
  "shot_line": "The camera pushes in with large amplitude at fast speed, charging the entire length of {THE_SPACE} toward {PRONOUN}: {NEAR_OBJECTS} sweep outward past the edges of frame and out of shot as the camera passes them, {FURTHER_OBJECTS} rush by on both sides and {GROUND} streams underneath, and the move ends in a tight close-up with {FACE} filling the frame.",
  "extra_slots": {
    "THE_SPACE": "the receding space the camera charges down, e.g. \"a forest track\", \"a warehouse aisle\", \"a hotel corridor\"",
    "NEAR_OBJECTS": "two objects close to the lens at the left and right edges that the camera will pass and sweep out of frame, e.g. \"the trunks of two near pines\"",
    "FURTHER_OBJECTS": "what rushes by mid-distance, e.g. \"further trunks\"",
    "GROUND": "what streams underneath, e.g. \"the snow\", \"wet asphalt\""
  }
}
```

## Prompt as it ran

`prompts/C-03_super-dolly-in.txt`
