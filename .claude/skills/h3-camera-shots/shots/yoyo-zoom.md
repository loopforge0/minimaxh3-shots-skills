# Yo-Yo Zoom

**Status:** verified in shape, imperfect in proportion. **The hardest shot in the library.**
**Effect:** from a tight close-up the view tears away into the far distance, holds, then snaps back to the
identical close-up.
**Primitives:** `Zoom Out` accelerating, a hold, then `Zoom In with large amplitude at fast speed`
⚠️ **No canonical film shot.** A preset label with no reference film behind it; judge it against described
behaviour.

## Shot line

> The camera begins in a tight close-up on {FACE}, then zooms out, starting slowly and accelerating harder
> and harder as it goes until the whole view smears into motion blur and {SUBJECT} has fallen away into
> the far distance, a tiny {SMALL_NOUN} {PLACE}. The camera holds there for about a second, then zooms
> back in with large amplitude at fast speed, snapping across the entire distance in a single instant to
> land tight on {FACE} again exactly as it began.

## It needs 192 frames

Three phases do not fit in 96 or 124. At 192 frames (8s) they completed for the first time. This is the
clearest case in the library of **frame count being load-bearing**. `../references/settings.md`.

Face height every 10 frames on the verified take:

```
163 203 114  63  34  26 26 26 26 26 26 26 26 26 26  31  68 135 224 205
      out, accelerating       held ~4.2s                 back
```

Range **11.3x**, and the return (~1.25s) is faster than the departure (~1.7s), which is the asymmetry the
shot is named for.

## What is still wrong, and the failed fix

Against a spec of *"~80-100x distant, hold ~1s, snap back in ~500ms"*: distance reached ~8x not 80x, the
hold ate **4.2s of the 8s**, and the return was 1.25s.

Removing the hold from the wording made it worse:

```
verified  163 203 114  63  34  26 ...  31  68 135 224 205     range 11.3x
          |<- out ->|      |<-- HOLD 4.2s -->|  |<- back ->|

revised   118 211 216 217 212 206 ...  60 159 218 156          range  7.9x
          |<----- STATIC 3.5s, nothing -----> |<-hold->|<-back->|
```

The hold shortened from 4.2s to 2.5s and bought **3.5 seconds of dead opening** where the subject just sits
there at full size, and cost range. **The dead time moved; it did not go away.**

⭐ That is the same behaviour as the split-screen shot: **H3 packs the described action into a window of its
choosing and pads the rest.** In neither case did the prompt control *where* in the clip the action sat.
`../references/performance.md`.

## Gotchas

- **Do not try to fix the hold by deleting it from the prompt.** Attack the dead opening instead, or cut the
  clip in an editor.
- The acceleration has to be stated as acceleration (*"starting slowly and accelerating harder and harder"*),
  not as `at fast speed` — a flat fast zoom out has no yo-yo in it.
- Describe the return as a single instant across the entire distance. Anything softer reads as a second
  ordinary zoom.

## Machine-readable

```json
{
  "id": "C-08",
  "slug": "yoyo-zoom",
  "name": "yo-yo zoom",
  "status": "verified-partial",
  "motion": "stationary",
  "length": 192,
  "framing": "{TIGHT_FRAMING} fills the frame with {FACE}",
  "framing_summary": "a tight close-up",
  "shot_intro": "sentence",
  "shot_line": "The camera begins in a tight close-up on {FACE}, then zooms out, starting slowly and accelerating harder and harder as it goes until the whole view smears into motion blur and {SUBJECT} has fallen away into the far distance, a tiny {SMALL_NOUN} {PLACE}. The camera holds there for about a second, then zooms back in with large amplitude at fast speed, snapping across the entire distance in a single instant to land tight on {FACE} again exactly as it began.",
  "extra_slots": {}
}
```

## Prompt as it ran

`prompts/C-08_yoyo-zoom.txt`
