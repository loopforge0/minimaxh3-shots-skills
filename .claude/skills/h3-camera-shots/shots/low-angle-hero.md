# Low-Angle Hero Shot

**Status:** verified on two renders (two seeds, two scenes), with a caveat. Part 2.
**Effect:** the camera sits near the ground looking up and creeps in until the subject towers over the frame.
**Primitives:** `Push In` + `at slow speed`, from a low camera tilted up.
**Reference:** all over superhero films; *The Avengers*, *The Dark Knight*.

⚠️ **The shipped take is gentler than the name suggests.** An earlier version went properly low but started
too far back. Asking for a closer start (the waist-up framing below) made the angle much milder, so what
shipped reads more as a push in from slightly below than a dramatic low angle. There is a trade between how
close it opens and how low it looks, and this recipe has not found the point that gets both.

## Shot line

> The camera stays low near the ground and tilted up at {PRONOUN} the whole time, and pushes in at slow speed
> until {PRONOUN_SUBJ} towers over the frame, {FACE} high in the shot, looking down past the lens.

## Framing

> A low-angle medium close-up from the waist up, the lens just above the ground and tilted up, looks up at
> {SUBJECT} against the sky

## Gotchas

- If you want a stronger angle, open wider (a medium shot rather than waist-up) and accept the subject
  starting smaller. That is the earlier version's trade, not a tested fix.

## Machine-readable

```json
{
  "id": "P2-15",
  "slug": "low-angle-hero",
  "name": "low-angle hero shot",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A low-angle medium close-up from the waist up, the lens just above the ground and tilted up, looks up at {SUBJECT} against the sky",
  "framing_summary": "a low-angle medium close-up from the waist up, looking up",
  "shot_intro": "comma",
  "shot_line": "The camera stays low near the ground and tilted up at {PRONOUN} the whole time, and pushes in at slow speed until {PRONOUN_SUBJ} towers over the frame, {FACE} high in the shot, looking down past the lens.",
  "extra_slots": {},
  "framing_note": "The waist-up opening gives a gentle angle. A wider opening went lower but started too far back."
}
```

## Prompt as it ran

`prompts/P2-15_low-angle-hero.txt`
