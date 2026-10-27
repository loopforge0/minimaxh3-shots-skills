# Cut-Away Montage

**Status:** verified. Part 2. An edit, not a camera move: seven timed cuts inside one generation.
**Effect:** a close-up of the face, four very fast inserts of the hands getting ready, each a fraction of a
second, then a snap back to the face, ready.
**Primitives:** none. Timed `[Shot N]` cuts, which MiniMax's guide documents.
**Reference:** the prep montage in *Requiem for a Dream* and *Hot Fuzz*.

## Shot line

The shot owns its whole description, `[Shot 1]` to `[Shot 7]`:

> A tight close-up frames {FACE} {PLACE}, with {ENVIRONMENT_ELEMENTS} soft behind {PRONOUN}; {POSSESSIVE} eyes
> narrow with focus as {PRONOUN_SUBJ} decides. [Shot 2] At 00:01.300, the shot cuts to an extreme close-up
> insert, close on the action as {PRONOUN_SUBJ} reaches to {INSERT_1}. [Shot 3] At 00:01.700, ... {INSERT_2}.
> [Shot 4] At 00:02.100, ... {INSERT_3}. [Shot 5] At 00:02.500, ... {INSERT_4}. [Shot 6] At 00:02.900, the
> shot cuts to an extreme close-up on {POSSESSIVE} face, now {WHERE_IT_ENDS}, as {POSSESSIVE} gaze snaps up,
> sharp and ready. [Shot 7] At 00:03.300, the shot cuts to a tight close-up of {FACE}, still
> {WHERE_IT_ENDS}, now still and ready, and {PRONOUN_SUBJ} looks up into the lens with a small, sure smile.

The full template is in the JSON below.

## Writing the inserts

Each insert is under half a second, and **H3 reuses whatever was in the insert before** unless told otherwise.

- **Name the object and where on it the hands work.** "Push the cable's plug into the socket on the guitar's
  body", not "plug in the guitar". In one take the cable jack went into the guitar strap from the previous
  insert, and a tuning peg became a knob on the amp from the previous insert.
- **Say one hand or both.** An earlier template wrote "her hands" before every insert, and a seatbelt and a
  gear stick were both done two-handed. The template now leaves the hands out ("as she reaches to ...") and
  each insert says which.
- **Say where an insert happens when the object does not.** A seatbelt and a gear stick imply a car;
  sunglasses do not. "Slide on dark sunglasses ... sitting in the driver's seat."
- **Short and plain beats long and exact.** The shipped seatbelt insert was edited by hand down to "as she
  pulls the seatbelt and clicks it into place", from a long version naming the metal tongue, the buckle and
  the hand. The long one was the weakest insert.

## Where the montage ends

This took three rounds:

1. The closing close-ups said "cuts back to the tight close-up", which points at `[Shot 1]`, so H3 put her
   back out on the highway.
2. Saying "in the same place as the last insert" was not enough: the last insert, a gear stick in extreme
   close-up, shows almost nothing of the car, and the closing close-ups came out on a neutral background.
3. `{WHERE_IT_ENDS}` names the place and what is around, in both closing shots, **and anything the inserts put
   on**. Without that, she put sunglasses on in an insert and ended without them. With it, every beat landed:
   keys one-handed, seatbelt once, sunglasses on in the car, gear stick, then both closing close-ups in the
   driver's seat with the sunglasses on.

## Timing

The cut times are written as timestamps. The test notes record the seven cuts landing on time in the first
take. Part 1 found that H3 picks its own clock for events
inside a continuous shot (`../references/performance.md`), so check the cut points on your own render rather
than relying on the timestamps.

## Gotchas

- The retention line covers all seven shots and says **the hands in the inserts are the subject's own**.
  `build_prompt.py` writes that line for you.
- The audio cuts to the same rhythm: a click, snap, whoosh or thud on every insert, then a beat of quiet.

## Machine-readable

```json
{
  "id": "P2-05",
  "slug": "cutaway-montage",
  "name": "cut-away montage",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A tight close-up",
  "framing_summary": "a tight close-up",
  "summary_action": "getting ready in a rapid, rhythmic cut-away montage of quick inserts",
  "shot_intro": "custom",
  "retention_line": "{SUBJECT} (appears in [Shot 1] to [Shot 7]): fully_preserved - {POSSESSIVE} {RETAINED} are held identical to {PLATE} in every shot, and the hands in the inserts are {POSSESSIVE} own.",
  "shot_line": "A tight close-up frames {FACE} {PLACE}, with {ENVIRONMENT_ELEMENTS} soft behind {PRONOUN}; {POSSESSIVE} eyes narrow with focus as {PRONOUN_SUBJ} decides. [Shot 2] At 00:01.300, the shot cuts to an extreme close-up insert, close on the action as {PRONOUN_SUBJ} reaches to {INSERT_1}. [Shot 3] At 00:01.700, the shot cuts to an extreme close-up insert, close on the action as {PRONOUN_SUBJ} reaches to {INSERT_2}. [Shot 4] At 00:02.100, the shot cuts to an extreme close-up insert, close on the action as {PRONOUN_SUBJ} reaches to {INSERT_3}. [Shot 5] At 00:02.500, the shot cuts to an extreme close-up insert, close on the action as {PRONOUN_SUBJ} reaches to {INSERT_4}. [Shot 6] At 00:02.900, the shot cuts to an extreme close-up on {POSSESSIVE} face, now {WHERE_IT_ENDS}, as {POSSESSIVE} gaze snaps up, sharp and ready. [Shot 7] At 00:03.300, the shot cuts to a tight close-up of {FACE}, still {WHERE_IT_ENDS}, now still and ready, and {PRONOUN_SUBJ} looks up into the lens with a small, sure smile.",
  "soundscape": "{SOUNDSCAPE}, cut into a tight rhythm: a sharp click, snap, whoosh or thud on every insert, then a beat of quiet",
  "extra_slots": {
    "INSERT_1": "the first insert: the object, where on it the hand works, and which hand, e.g. \"snatch a set of car keys off a dusty bonnet with the right hand\"",
    "INSERT_2": "the second insert",
    "INSERT_3": "the third insert; say where it happens if the object does not, e.g. \"slide on a pair of dark sunglasses with both hands, sitting in the driver's seat\"",
    "INSERT_4": "the fourth insert",
    "WHERE_IT_ENDS": "where the montage ends up, with what is around, and anything the inserts put on, e.g. \"in the driver's seat of the car, with the steering wheel, dashboard and windscreen all around, the dark sunglasses on\""
  },
  "performance_note": "The face beats are written into the shot line. Keep PERFORMANCE short, or leave it about the first close-up."
}
```

## Prompt as it ran

`prompts/P2-05_cutaway-montage.txt`. The seatbelt insert in it is the hand-edited short version, so it does
not follow the template word for word.
