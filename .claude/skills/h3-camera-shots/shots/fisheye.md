# Fisheye Close-Up

**Status:** verified on two renders, with a caveat. Part 2.
**Effect:** a very wide lens a hand's width from the face, pushing in as the subject leans into it. The middle
of the face swells and straight lines bend at the edges.
**Primitives:** `Push In`, plus a described warp. There is no lens primitive.
**Reference:** *The Favourite* uses it throughout.

⚠️ **This is not a true fisheye.** Neither render shows a strong circular bulge or a curved black rim. Both
read by eye as a wide, close push-in with the lens almost on the face, and that was the call to keep it.

## Shot line

> The camera pushes in toward {PRONOUN} as {PRONOUN_SUBJ} leans into the lens, and the warp grows stronger the
> closer it gets: {POSSESSIVE} nose and the middle of {FACE} balloon toward the viewer while {POSSESSIVE} ears
> and the setting behind {PRONOUN} shrink away and curve around the rim of the frame, and every straight line
> in the background bends into an arc.

## Describe the picture, not the lens

| Take | Wording | What came back |
|---|---|---|
| 1 | Named the lens: "ultra-wide fisheye lens", "barrel distortion" | A plain push-in to a close-up with only slight wide-angle warp |
| 2 | Described what the picture looks like (the framing and shot line here) | A push-in to an extreme close-up with ordinary wide-angle perspective. No bulge, no curved rim, but closer to the look |

Take 1 fits Part 1's finding that lens names do almost nothing (`../references/gear.md`). The recipe keeps
take 2's wording. The shipped clip is take 2 on seed 11.

## Gotchas

- **Give the lean an arc.** For example *"leans into the lens with a slow, mischievous grin that breaks into a
  laugh"*. The lean is what carries the push.
- The framing is a whole clause describing the warp, so it joins the action with a comma.

## Machine-readable

```json
{
  "id": "P2-04",
  "slug": "fisheye",
  "name": "fisheye close-up",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A warped, bulging close-up with the camera almost touching {SUBJECT}'s face: the whole picture is curved like the inside of a glass ball, the middle swelling toward the viewer and the edges bending round into a dark rounded border",
  "framing_summary": "a warped, bulging fisheye close-up",
  "shot_intro": "comma",
  "shot_line": "The camera pushes in toward {PRONOUN} as {PRONOUN_SUBJ} leans into the lens, and the warp grows stronger the closer it gets: {POSSESSIVE} nose and the middle of {FACE} balloon toward the viewer while {POSSESSIVE} ears and the setting behind {PRONOUN} shrink away and curve around the rim of the frame, and every straight line in the background bends into an arc.",
  "extra_slots": {},
  "performance_note": "Give the lean an arc, e.g. \"leans into the lens with a slow, mischievous grin that breaks into a laugh\"."
}
```

## Prompt as it ran

`prompts/P2-04_fisheye.txt`
