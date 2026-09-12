# The prompt scaffold

Ref2VA, one character reference image. Six sections, exact field names, exact order - this is
MiniMax's documented format and H3 parses it noticeably better than plain prose. Confirm the field
names against `ref-en.txt` (see `upstream.md`); they are reproduced here for convenience, not as the
authority.

Fill the `{...}` slots. Drop the chosen shot's **shot line** into `{SHOT_LINE}`.

```text
subject_definitions:
{SUBJECT} is {SUBJECT_DEFINITION}. {IDENTITY_LOCK}

summary:
[reference generation] The target video shows {SUBJECT} {SUMMARY_ACTION} {ENVIRONMENT_PREP} {ENVIRONMENT}, in {FRAMING_LOWER}, as the camera performs a {SHOT_NAME}.

retention_analysis:
{SUBJECT} (appears in [Shot 1]): fully_preserved - {POSSESSIVE} {RETAINED} are held identical to {PLATE} in every frame with zero drift.

detailed_description:
The target video is live-action and cinematic, shot on {GEAR}, {LIGHTING}, {PALETTE}.
[Shot 1] {FRAMING} frames {SUBJECT} {SUBJECT_ACTION}, with {ENVIRONMENT_ELEMENTS} behind {PRONOUN}. {SHOT_LINE} As the shot plays out, {SUBJECT}'s {PERFORMANCE}.

overall_soundscape: {SOUNDSCAPE}

non_diegetic_music: {MUSIC}
```

`scripts/build_prompt.py` reads **this exact block** and fills it, so editing the scaffold here changes what the
generator emits. `{SUBJECT}` defaults to `<Subject 1>` and `{PLATE}` to `<Picture 1>`. `{FRAMING}`,
`{SUBJECT_ACTION}`, `{SHOT_NAME}` and `{SHOT_LINE}` come from the shot file, and any of them can be overridden in
your scene file.

## Slots

**You supply these.** `build_prompt.py <shot> --slots` prints the list for any given shot.

| Slot | Guidance |
|---|---|
| `{SUBJECT_DEFINITION}` | Concrete and itemised - hair, skin, every garment, accessories. Always written as *"the … in `<Picture 1>`: …"* so the plate binds to the **subject**, not to the frame. |
| `{ENVIRONMENT}` | The location as a short noun phrase, e.g. *a snow-covered arctic coastline*. Used in the summary line. |
| `{ENVIRONMENT_PREP}` | The preposition in front of it - `in` (default) or `on`. *on a coastline*, *in a forest*. |
| `{PLACE}` | Where the subject physically is, with its preposition: *on the snowy rocky shore*, *in the tall grass*. Goes inside the subject action. |
| `{ENVIRONMENT_ELEMENTS}` | Everything visible behind the subject, itemised, **in text only, never as a second plate**. These become the things the camera move is measured against, so name several. |
| `{LIGHTING}` / `{PALETTE}` | Style line. Cosmetic but cheap. |
| `{GEAR}` | Cosmetic - see `gear.md`. Keep it plausible and keep it out of frame. **Never name a rig a camera could see.** |
| `{PERFORMANCE}` | An expression that **changes** over the shot, with its timing. Written to follow *"`<Subject 1>`'s …"*. A state gets held as one frozen pose - see `performance.md`. |
| `{SOUNDSCAPE}` / `{MUSIC}` | H3 writes audio and picture together, so these change the image. Never name the camera, lens, rig or move in either. `{MUSIC}` defaults to `N/A`. |
| `{PRONOUN}` / `{PRONOUN_SUBJ}` / `{POSSESSIVE}` | Come from the subject kind. Override to match your subject. |

**The shot supplies these**, and any of them can be overridden in your scene file.

| Slot | |
|---|---|
| `{SHOT_LINE}` | The camera clause. The only part that genuinely changes between shots. |
| `{FRAMING}` | **Load-bearing.** Each shot states what opening framing it needs. See `framing.md`. |
| `{SUMMARY_ACTION}` | The short action for the summary line - *standing still*, *running*, *walking steadily forward*. |
| `{SUBJECT_ACTION}` | The full action for the shot sentence. Never *"standing completely still"*. |
| `{SHOT_NAME}` | Plain name, e.g. `dolly zoom`. Cosmetic - the shot line does the work. |
| `{IDENTITY_LOCK}` | *Her exact facial structure, features and proportions stay identical to `<Picture 1>` in every frame.* Defaulted from your possessive pronoun. |
| `{SUBJECT}` / `{PLATE}` | `<Subject 1>` and `<Picture 1>` unless you change them. |

### How the framing joins the action

`{FRAMING}` is sometimes a bare noun phrase and sometimes a whole clause, and the two cannot be glued on the
same way. Each shot declares `shot_intro`:

| `shot_intro` | `[Shot 1]` becomes | Used by |
|---|---|---|
| `frames` *(default)* | `{FRAMING} frames {SUBJECT} {SUBJECT_ACTION}, with …` | most shots |
| `comma` | `{FRAMING}, {SUBJECT_ACTION}, with …` | super dolly in, crash zoom in |
| `sentence` | `{FRAMING}. {SUBJECT} is {SUBJECT_ACTION}, with …` | yo-yo zoom, rack focus |
| `custom` | `{SHOT_LINE}` alone — the shot owns its whole description | split screen |

These match how the prompts that actually shipped were written. Get it wrong and you get *"…at the far end of
it frames `<Subject 1>` standing…"*.

Some shots add their own slots, and `--slots` prints those with a one-line hint each: a super dolly in needs
`{THE_SPACE}`, `{NEAR_OBJECTS}`, `{FURTHER_OBJECTS}` and `{GROUND}`; a split screen needs its three panel
angles.

## Three rules about the reference plate

These came out of a controlled A/B on the conditioning, and getting them wrong costs about half the
camera move.

1. **`[reference generation]`, not `[keyframe completion]`.** The plate is an identity reference, not
   a frame the video continues from.
2. **Never call the plate "the first frame"**, and never say the shot *"begins in the position and
   framing established by"* it. That wording pins the opening composition, and a camera move needs
   composition free.
3. **Keep the environment out of the plate.** Describe it in text. One character plate. A
   *background* plate is what actually kills the move.

Attach exactly one reference image, with `ref_image_size: max`. Full measurements in
`../../h3-shot-iteration/references/conditioning.md`.

⚠️ **The trade you are making.** With no background plate the environment *content* drifts across
the shot - in one verified render a drum kit became a grand piano by the end. The camera move is
correct; the scene is being re-invented as it goes. If a locked environment matters more than the
move, add the background plate and accept roughly half the motion.

## Task types

Per MiniMax's guide, pick by the reference's actual role. Combine with ` + ` when several apply.

| Tag | When |
|---|---|
| `[reference generation]` | The reference guides character, style or motion without being a concrete frame. **Default for every shot in this library.** |
| `[keyframe completion]` | An image is a first / last / keyframe anchor. ⚠️ Suppresses camera motion. Deliberately static shots only. |
| `[video editing]` / `[video continuation]` | An existing video is edited or continued |
| `[audio reuse]` / `[audio reference]` | Audio copied, versus only its qualities referenced |

## Worked example

Every prompt in `prompts/` is a filled-in instance of this scaffold with its settings and wiring
stated. `prompts/K-06n_dolly-zoom-k06.txt` is the shipping configuration: one character plate,
environment in text, `max`.

## More than one subject

`whip-pan` uses two character plates and `rack-focus` uses three. Extra **character** plates cost
nothing - a two-plate whip pan produced the fastest move in the set. Add `<Subject 2>` to
`subject_definitions` and to `retention_analysis` in the same shape, and keep the wiring order
straight, because `<Picture N>` is positional.
