# Rooftop Swing

**Status:** verified on two scenes, same seed. Part 2. An effect: the subject's stunt is most of the shot.
**Effect:** the subject leaps off a rooftop and swings on a line in one huge arc across the gap to the next
building, the camera following through the air behind them; they land, stand and turn round to the lens.
**Primitives:** `Tracking Shot` + `with large amplitude` + `at fast speed`.
**Reference:** the web-swing from a well-known superhero film. The prompt does not name the character, and
does not need to.

## Shot line

The shot owns its whole `[Shot 1]` line:

> A wide shot frames {SUBJECT} crouched on the edge of a high rooftop {PLACE}, with {ENVIRONMENT_ELEMENTS} far
> below and around {PRONOUN}, gripping a thin silver line that runs up to the top of a taller building across
> the street. {PRONOUN_SUBJ_CAP} leaps off the edge and swings down on the line in one huge arc across the gap
> between the buildings, the street rushing past far below {PRONOUN}, {POSSESSIVE} hair and clothes streaming
> with the speed. The camera performs a tracking shot behind and slightly to one side of {PRONOUN} through the
> air with large amplitude at fast speed, following the whole swing, so through the swing {PRONOUN_SUBJ} faces
> away from the camera toward the next building, {POSSESSIVE} back to the lens. At the bottom of the arc
> {PRONOUN_SUBJ} sweeps up toward the next building, lets go at the top of the swing, sails through the air and
> lands crouched on its rooftop ledge, still facing away from the camera. Then {PRONOUN_SUBJ} stands up and
> turns around on the spot, stepping and pivoting {POSSESSIVE} whole body through a half turn so that
> {PRONOUN_SUBJ} ends facing the camera, and looks back across the gap with a breathless grin.

## Say which way the subject faces, at every stage

The swing worked on the first take. The landing did not: after landing, her **back became her front** instead
of her turning round. The prompt never said which way she faced, and its ending asked for her face.

The fix states the facing at each stage (back to the lens through the swing, still facing away on landing)
and makes the turn an action she performs: she stands, steps and pivots through a half turn. With that wording
she turned round properly in both scenes it was rendered in.

## Gotchas

- **Needs a city of tall buildings** as the location.
- The shot brings its own music, a driving orchestral theme with pounding drums. A `MUSIC` in your scene file
  replaces it.
- The audio adds wind, the creak of the line and the thud of the landing to your soundscape.

## Machine-readable

```json
{
  "id": "P2-09",
  "slug": "rooftop-swing",
  "name": "rooftop swing",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A wide shot",
  "framing_summary": "a wide shot",
  "summary_action": "leaping from a rooftop and swinging on a line in a huge arc across the gap between two tall buildings",
  "shot_intro": "custom",
  "shot_line": "A wide shot frames {SUBJECT} crouched on the edge of a high rooftop {PLACE}, with {ENVIRONMENT_ELEMENTS} far below and around {PRONOUN}, gripping a thin silver line that runs up to the top of a taller building across the street. {PRONOUN_SUBJ_CAP} leaps off the edge and swings down on the line in one huge arc across the gap between the buildings, the street rushing past far below {PRONOUN}, {POSSESSIVE} hair and clothes streaming with the speed. The camera performs a tracking shot behind and slightly to one side of {PRONOUN} through the air with large amplitude at fast speed, following the whole swing, so through the swing {PRONOUN_SUBJ} faces away from the camera toward the next building, {POSSESSIVE} back to the lens. At the bottom of the arc {PRONOUN_SUBJ} sweeps up toward the next building, lets go at the top of the swing, sails through the air and lands crouched on its rooftop ledge, still facing away from the camera. Then {PRONOUN_SUBJ} stands up and turns around on the spot, stepping and pivoting {POSSESSIVE} whole body through a half turn so that {PRONOUN_SUBJ} ends facing the camera, and looks back across the gap with a breathless grin.",
  "soundscape": "{SOUNDSCAPE}, then wind roaring past as {PRONOUN_SUBJ} swings, the creak of the taut line, and a solid thud as {PRONOUN_SUBJ} lands",
  "music": "A driving, heroic orchestral theme with pounding drums",
  "extra_slots": {},
  "scene_warning": "Needs a city of tall buildings as the location."
}
```

## Prompt as it ran

`prompts/P2-09_rooftop-swing.txt`
