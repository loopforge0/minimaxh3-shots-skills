# Crash Zoom Out

**Status:** verified, **with `scripts/snap.py` run after the render**. Part 2.
**Effect:** a held close-up on the face, then one violent zoom out to a wide shot, then a hold on the wide
shot. The mirror of `crash-zoom-in.md`.
**Primitives:** `Zoom Out`, described as a near-instant lens change on a locked-off camera.

## Shot line

> The camera is locked off on a tripod and holds the tight close-up completely still for the first two
> seconds; only the zoom lens changes and the camera body never moves. Between one frame and the next the lens
> crash zooms out to a wide shot with {SUBJECT} small and complete in frame {PLACE}: the whole change takes only
> two or three frames, as abrupt as a cut, with a streak of zoom blur on those few frames only, and nothing
> shifts against anything else, the background simply shrinks flat together with {PRONOUN}. After it lands the
> wide framing is locked and does not change.

## Framing

Open **tight**, on the face. This is the shot that inverts the framing rule: it ends wide, so it has to
start at the end of the range where the subject is largest (`../references/framing.md`).

## H3 will not snap. Ramp it afterwards

H3 picks its own pace for a zoom, whatever the prompt asks for. Two wordings, same subject and seed:

| Wording | Zoom as H3 rendered it | After `snap.py` |
|---|---|---|
| "a Zoom Out with large amplitude at fast speed ... in about 200 milliseconds" | 2.2 s, with parallax; it read like a dolly | 4 frames |
| "between one frame and the next ... two or three frames, as abrupt as a cut ... nothing shifts against anything else" (the shot line above) | 1.75 s | 3 frames |

The second wording is kept because it leaves less to cut. Neither gets anywhere near a snap
on its own, so the fix is in the edit, not the prompt:

```bash
python scripts/snap.py crash-zoom-out_raw.mp4 crash-zoom-out.mp4
```

On the shipped render (1344x768, 124 frames at 24 fps) it reports:

```
zoom found at frames 71-112 (2.96-4.67 s, 41 frames), sped up 13.7x to 3 frames
```

The clip goes from 124 frames to 86, about 3.6 s. `snap.py` speeds the audio over the same stretch by the same
factor, so sound stays in sync. Its docstring lists what it cannot handle.

## Gotchas

- ⚠️ **At 1344x768 the zoom starts late.** On the shipped render the zoom runs from about 3.0 s to 4.7 s of a
  5.2 s clip, so after the ramp the wide framing only holds for about half a second. The test notes suggest
  asking for a one-second opening hold and an explicit two-second closing hold to move it earlier. That
  variant was written but is not what shipped, and no result for it is recorded.
- The first wording came back with parallax and read as a dolly out. The shot line above describes a flat
  magnification instead: only the lens changes, and nothing shifts against anything else.
- The reaction lands with the zoom: calm through the close-up, eyes flicking wide as it snaps out.
- Keep the render as H3 made it (`_raw.mp4`) and write the ramped clip to a new file.

## Machine-readable

```json
{
  "id": "P2-07",
  "slug": "crash-zoom-out",
  "name": "crash zoom out",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "{TIGHT_FRAMING} fills the frame with {SUBJECT}'s face",
  "framing_summary": "a tight close-up",
  "shot_intro": "sentence",
  "shot_line": "The camera is locked off on a tripod and holds the tight close-up completely still for the first two seconds; only the zoom lens changes and the camera body never moves. Between one frame and the next the lens crash zooms out to a wide shot with {SUBJECT} small and complete in frame {PLACE}: the whole change takes only two or three frames, as abrupt as a cut, with a streak of zoom blur on those few frames only, and nothing shifts against anything else, the background simply shrinks flat together with {PRONOUN}. After it lands the wide framing is locked and does not change.",
  "extra_slots": {},
  "timing_warning": "H3 took 1.7 to 2.2 s over this zoom in the renders here, whatever the prompt said. Run scripts/snap.py on the render to ramp it to 3 frames."
}
```

## Prompt as it ran

`prompts/P2-07_crash-zoom-out.txt`
