#!/usr/bin/env python3
"""Build a MiniMax H3 Ref2VA prompt for a named camera shot from your own scene.

The shot supplies the camera clause, the framing requirement and the subject action.
You supply the subject, the environment, the performance and the audio.

    python scripts/build_prompt.py --list
    python scripts/build_prompt.py snorricam --slots
    python scripts/build_prompt.py snorricam --scene my-scene.json
    python scripts/build_prompt.py dolly-zoom --scene my-scene.json -o out/dolly.txt

Set "SUBJECT_KIND" in your scene file to person (default), animal, bird or object. It selects the
vocabulary for framing, the anti-frozen clause and the pronouns. Only person was ever tested.

Standard library only. No dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / ".claude" / "skills" / "h3-camera-shots"
SHOTS_DIR = SKILL / "shots"
SCAFFOLD_MD = SKILL / "references" / "scaffold.md"

# Slots the scaffold fills in for you unless your scene file overrides them.
DEFAULTS = {
    "SUBJECT": "<Subject 1>",
    "PLATE": "<Picture 1>",
    "SUBJECT_2": "<Subject 2>",
    "SUBJECT_3": "<Subject 3>",
    "SUBJECT_4": "<Subject 4>",
    "ENVIRONMENT_PREP": "in",
    "MUSIC": "N/A",
    # Direction. Only these defaults were tested - see references/direction.md.
    "PAN_DIRECTION": "right",
    "ROLL_DIRECTION": "counterclockwise",
}

# A subject is not necessarily a person. These vocabularies keep the shot lines sane for an
# animal, a bird or an inanimate object.
#
# ⚠️ EVERY shot in this library was developed and judged on human subjects. The non-person
# vocabularies are reasoned from the same rules, not measured. See references/subjects.md.
KINDS = {
    "person": {
        "PRONOUN": "her", "PRONOUN_SUBJ": "she", "POSSESSIVE": "her",
        "IDENTITY_LOCK": "{POSSESSIVE_CAP} exact facial structure, features and proportions stay "
                         "identical to {PLATE} in every frame.",
        "RETAINED": "face, identity and clothing",
        "LIFE": "breathing softly, hair and clothing stirring in the air, blinking and shifting "
                "{POSSESSIVE} weight a little as people naturally do",
        "STATIONARY_VERB": "standing in place",
        "WALK_VERB": "walks steadily forward",
        "WALK_PARTICIPLE": "walking steadily forward",
        "RUN_VERB": "running steadily",
        "MOVE_DETAIL": "hair flying and clothing snapping with the movement",
        "SUMMARY_STATIONARY": "standing still",
        "SUMMARY_WALK": "walking steadily forward",
        "SUMMARY_RUN": "running",
        "MEDIUM_FRAMING": "A waist-up medium close-up",
        "TIGHT_FRAMING": "A tight close-up",
        "WIDE_FRAMING": "A wide shot",
        "WIDE_FRAMING_EXTREME": "An extreme wide shot",
        "FACE": "{POSSESSIVE} face",
        "DETAIL": "{POSSESSIVE} right eye, the iris and pupil filling the view",
        "SMALL_NOUN": "figure",
        "STRIDE": "with every stride",
        "ORBIT_ACKNOWLEDGE": "{PRONOUN_SUBJ_CAP} turns {POSSESSIVE} head slightly to keep the "
                             "camera in view.",
        "FACE_CAMERA": "{PRONOUN_SUBJ_CAP} faces the camera squarely for the whole shot and never "
                       "turns away from it.",
        "ROOTED": "{PRONOUN_SUBJ_CAP} stands rooted to one spot and does not step, lean or shift "
                  "{POSSESSIVE} weight.",
        "FAR_ACTION": "stand talking together",
    },
    "animal": {
        "PRONOUN": "it", "PRONOUN_SUBJ": "it", "POSSESSIVE": "its",
        "IDENTITY_LOCK": "{POSSESSIVE_CAP} exact markings, coat, build and proportions stay "
                         "identical to {PLATE} in every frame.",
        "RETAINED": "face, markings and coat",
        "LIFE": "breathing, fur and ears moving in the air, blinking and shifting {POSSESSIVE} "
                "weight a little as animals naturally do",
        "STATIONARY_VERB": "standing",
        "WALK_VERB": "walks steadily forward",
        "WALK_PARTICIPLE": "walking steadily forward",
        "RUN_VERB": "running steadily",
        "MOVE_DETAIL": "fur and ears moving with the stride",
        "SUMMARY_STATIONARY": "standing still",
        "SUMMARY_WALK": "walking steadily forward",
        "SUMMARY_RUN": "running",
        "MEDIUM_FRAMING": "A medium close-up on {POSSESSIVE} head and shoulders",
        "TIGHT_FRAMING": "A tight close-up on {POSSESSIVE} face",
        "WIDE_FRAMING": "A wide shot",
        "WIDE_FRAMING_EXTREME": "An extreme wide shot",
        "FACE": "{POSSESSIVE} face",
        "DETAIL": "{POSSESSIVE} right eye, the iris and pupil filling the view",
        "SMALL_NOUN": "figure",
        "STRIDE": "with every stride",
        "ORBIT_ACKNOWLEDGE": "{PRONOUN_SUBJ_CAP} turns {POSSESSIVE} head slightly to keep the "
                             "camera in view.",
        "FACE_CAMERA": "{PRONOUN_SUBJ_CAP} stays turned toward the camera for the whole shot.",
        "ROOTED": "{PRONOUN_SUBJ_CAP} stays rooted to one spot and does not step or lean.",
        "FAR_ACTION": "stand together",
    },
    "bird": {
        "PRONOUN": "it", "PRONOUN_SUBJ": "it", "POSSESSIVE": "its",
        "IDENTITY_LOCK": "{POSSESSIVE_CAP} exact plumage, markings and proportions stay identical "
                         "to {PLATE} in every frame.",
        "RETAINED": "head, plumage and markings",
        "LIFE": "breathing, feathers stirring in the air, blinking and making the small quick head "
                "movements birds naturally make",
        "STATIONARY_VERB": "perched",
        "WALK_VERB": "hops steadily forward",
        "WALK_PARTICIPLE": "hopping steadily forward",
        "RUN_VERB": "flying steadily",
        "MOVE_DETAIL": "wings beating and feathers moving in the air",
        "SUMMARY_STATIONARY": "perched still",
        "SUMMARY_WALK": "hopping forward",
        "SUMMARY_RUN": "flying",
        "MEDIUM_FRAMING": "A medium close-up on {POSSESSIVE} head and body",
        "TIGHT_FRAMING": "A tight close-up on {POSSESSIVE} head",
        "WIDE_FRAMING": "A wide shot",
        "WIDE_FRAMING_EXTREME": "An extreme wide shot",
        "FACE": "{POSSESSIVE} head",
        "DETAIL": "{POSSESSIVE} eye, the iris filling the view",
        "SMALL_NOUN": "shape",
        "STRIDE": "with every wingbeat",
        "ORBIT_ACKNOWLEDGE": "{PRONOUN_SUBJ_CAP} turns {POSSESSIVE} head to keep the camera in view.",
        "FACE_CAMERA": "{PRONOUN_SUBJ_CAP} stays turned toward the camera for the whole shot.",
        "ROOTED": "{PRONOUN_SUBJ_CAP} stays on the same perch and does not shift position.",
        "FAR_ACTION": "sit together",
    },
    "object": {
        "PRONOUN": "it", "PRONOUN_SUBJ": "it", "POSSESSIVE": "its",
        "IDENTITY_LOCK": "{POSSESSIVE_CAP} exact shape, proportions, materials, wear and markings "
                         "stay identical to {PLATE} in every frame.",
        # An object genuinely does not move, so the anti-frozen clause moves to the world around it.
        "RETAINED": "shape, materials and markings",
        "LIFE": "completely still and inanimate, with {AMBIENT} moving around {PRONOUN}",
        "STATIONARY_VERB": "resting",
        "WALK_VERB": "travels steadily forward",
        "WALK_PARTICIPLE": "travelling steadily forward",
        "RUN_VERB": "moving quickly",
        "MOVE_DETAIL": "the world streaming past it",
        "SUMMARY_STATIONARY": "sitting still",
        "SUMMARY_WALK": "travelling forward",
        "SUMMARY_RUN": "moving quickly",
        "MEDIUM_FRAMING": "A medium close-up",
        "TIGHT_FRAMING": "A tight close-up",
        "WIDE_FRAMING": "A wide shot",
        "WIDE_FRAMING_EXTREME": "An extreme wide shot",
        "FACE": "{PRONOUN}",
        "DETAIL": None,  # no eye to land on; the user must supply one
        "SMALL_NOUN": "shape",
        "STRIDE": "constantly",
        "ORBIT_ACKNOWLEDGE": "Nothing about {PRONOUN} changes as the camera travels.",
        "FACE_CAMERA": "{POSSESSIVE_CAP} orientation to the camera never changes.",
        "ROOTED": "{PRONOUN_SUBJ_CAP} does not move at all.",
        "FAR_ACTION": "sit together",
    },
}

# How each shot's motion resolves into the two action slots.
MOTION = {
    "stationary": ("{STATIONARY_VERB} {PLACE}, {LIFE}", "{SUMMARY_STATIONARY}"),
    "walk":       ("{WALK_PARTICIPLE} {PLACE}, {MOVE_DETAIL}", "{SUMMARY_WALK}"),
    "run":        ("{RUN_VERB} {PLACE}, {MOVE_DETAIL}", "{SUMMARY_RUN}"),
}

# Slots that must come from the scene file. No sensible default exists for any of them.
REQUIRED_FROM_SCENE = [
    "SUBJECT_DEFINITION",
    "ENVIRONMENT",
    "ENVIRONMENT_ELEMENTS",
    "PLACE",
    "LIGHTING",
    "PALETTE",
    "GEAR",
    "PERFORMANCE",
    "SOUNDSCAPE",
]

SLOT_RE = re.compile(r"\{([A-Z0-9_]+)\}")


def fenced_block(path: Path, lang: str) -> str:
    """Return the first ```<lang> fenced block in a markdown file."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^```" + lang + r"\s*\n(.*?)\n```", text, re.S | re.M)
    if not m:
        sys.exit(f"error: no ```{lang} block found in {path}")
    return m.group(1)


def load_shots() -> dict[str, dict]:
    """Every shot's machine-readable block, keyed by slug."""
    shots = {}
    for md in sorted(SHOTS_DIR.glob("*.md")):
        if md.name == "INDEX.md":
            continue
        text = md.read_text(encoding="utf-8")
        m = re.search(r"^```json\s*\n(.*?)\n```", text, re.S | re.M)
        if not m:
            continue  # shots with no recipe, e.g. bullet-time
        try:
            shot = json.loads(m.group(1))
        except json.JSONDecodeError as exc:
            sys.exit(f"error: malformed json block in {md.name}: {exc}")
        shot["_file"] = md.name
        shots[shot["slug"]] = shot
    return shots


def resolve(template: str, values: dict[str, str], passes: int = 6) -> str:
    """Substitute {SLOTS}, repeatedly, because slot values contain slots of their own."""
    out = template
    for _ in range(passes):
        before = out
        out = SLOT_RE.sub(lambda m: values.get(m.group(1), m.group(0)), out)
        if out == before:
            break
    return out


def slots_in(*templates: str) -> set[str]:
    found: set[str] = set()
    for t in templates:
        found |= set(SLOT_RE.findall(t))
    return found


def cmd_list(shots: dict[str, dict]) -> None:
    width = max(len(s) for s in shots)
    print("shots (see .claude/skills/h3-camera-shots/shots/INDEX.md for what each one looks like)\n")
    for slug, shot in sorted(shots.items()):
        print(f"  {slug:<{width}}  {shot['length']:>3}f  {shot['status']:<22} {shot['name']}")
    print("\nbullet-time has no recipe on purpose. Read shots/bullet-time.md for why.")


def cmd_slots(shot: dict, scaffold: str, kind: str) -> None:
    vocab = {k: v for k, v in KINDS[kind].items() if v is not None}
    action = shot.get("subject_action") or MOTION.get(shot.get("motion"), ("", ""))[0]
    needed = slots_in(scaffold, shot["shot_line"], shot["framing"], action,
                      *[v for v in vocab.values()])
    derived = {"SHOT_LINE", "FRAMING", "FRAMING_LOWER", "SUBJECT_ACTION", "SUMMARY_ACTION",
               "SHOT_NAME", "POSSESSIVE_CAP", "PRONOUN_SUBJ_CAP"}
    from_you = sorted(needed - derived - set(DEFAULTS) - set(vocab))

    print(f"{shot['slug']}  ({shot['name']}, {shot['length']} frames, {shot['status']})")
    print(f"subject kind: {kind}\n")
    print("your scene file must provide:")
    for slot in from_you:
        hint = shot.get("extra_slots", {}).get(slot, "")
        print(f"  {slot:<24} {hint}")

    print(f"\nfrom the '{kind}' vocabulary (override any of these in your scene file):")
    for k, v in sorted(vocab.items()):
        print(f"  {k:<24} {v}")
    print("\nother defaults:")
    for k, v in DEFAULTS.items():
        print(f"  {k:<24} {v}")
    print(f"  {'FRAMING':<24} {shot['framing']}")
    print(f"  {'SUBJECT_ACTION':<24} {action}")

    missing_vocab = sorted(k for k, v in KINDS[kind].items() if v is None and k in needed)
    for slot in missing_vocab:
        print(f"\n!! the '{kind}' vocabulary has no default for {slot}. You must supply it.")
    for key in ("framing_note", "performance_note", "gear_warning", "timing_warning",
                "scene_warning", "subject_warning"):
        if key in shot:
            print(f"\n!! {key}: {shot[key]}")


def kind_of(scene: dict) -> str:
    kind = scene.get("SUBJECT_KIND", scene.get("subject_kind", "person"))
    if kind not in KINDS:
        sys.exit(f"error: SUBJECT_KIND '{kind}' is not one of: {', '.join(KINDS)}")
    return kind


def build(shot: dict, scene: dict, scaffold: str) -> str:
    kind = kind_of(scene)
    values = dict(DEFAULTS)
    values.update({k: v for k, v in KINDS[kind].items() if v is not None})

    values["SHOT_NAME"] = shot["name"]
    values["FRAMING"] = shot["framing"]
    values["SHOT_LINE"] = shot["shot_line"]

    motion = shot.get("motion")
    if motion in MOTION:
        action, summary = MOTION[motion]
        values["SUBJECT_ACTION"], values["SUMMARY_ACTION"] = action, summary
    # A shot may state its own instead (a split screen describes its action per panel).
    if "subject_action" in shot:
        values["SUBJECT_ACTION"] = shot["subject_action"]
    if "summary_action" in shot:
        values["SUMMARY_ACTION"] = shot["summary_action"]

    values.update({k: v for k, v in scene.items()
                   if not k.startswith("_") and k not in ("SUBJECT_KIND", "subject_kind")})

    poss = values.get("POSSESSIVE", "their")
    values["POSSESSIVE_CAP"] = poss[:1].upper() + poss[1:]
    subj = values.get("PRONOUN_SUBJ", "they")
    values["PRONOUN_SUBJ_CAP"] = subj[:1].upper() + subj[1:]

    # The summary wants a short noun phrase. Most shots' framing is already one; the shots whose
    # framing is a full clause carry a separate framing_summary.
    summary_framing = resolve(shot.get("framing_summary", values["FRAMING"]), values)
    values["FRAMING_LOWER"] = summary_framing[:1].lower() + summary_framing[1:]

    # How the framing clause joins the subject action. Framing that is a bare noun phrase ("A
    # waist-up medium close-up") takes "frames"; framing that is already a full clause cannot, and
    # the prompts that shipped joined those with a comma or started a new sentence instead.
    tail = ", {SUBJECT_ACTION}, with {ENVIRONMENT_ELEMENTS} behind {PRONOUN}."
    intros = {
        "frames":   "[Shot 1] {FRAMING} frames {SUBJECT}" + tail,
        "comma":    "[Shot 1] {FRAMING}" + tail,
        "sentence": "[Shot 1] {FRAMING}. {SUBJECT} is {SUBJECT_ACTION}, with "
                    "{ENVIRONMENT_ELEMENTS} behind {PRONOUN}.",
        # A shot whose layout IS the description owns its whole [Shot 1] line.
        "custom":   "[Shot 1]",
    }
    intro = shot.get("shot_intro", "frames")
    if intro not in intros:
        sys.exit(f"error: {shot['slug']} has shot_intro '{intro}', expected one of: "
                 f"{', '.join(intros)}")

    template = re.sub(
        r"^\[Shot 1\].*$",
        (intros[intro] + " {SHOT_LINE} As the shot plays out, {SUBJECT}'s {PERFORMANCE}.")
        .replace("\\", "\\\\"),
        scaffold,
        count=1,
        flags=re.M,
    )

    prompt = resolve(template, values)

    # Extra subjects get their own definition and retention lines, but only as many as this
    # shot actually uses - a scene file may carry spares for other shots.
    extra_defs, extra_retentions = [], []
    for n in range(2, shot.get("subjects", 1) + 1):
        definition = values.get(f"SUBJECT_{n}_DEFINITION")
        if not definition:
            sys.exit(f"error: {shot['slug']} uses {shot['subjects']} subjects; "
                     f"your scene file is missing SUBJECT_{n}_DEFINITION")
        label = values.get(f"SUBJECT_{n}", f"<Subject {n}>")
        plate = values.get(f"PLATE_{n}", f"<Picture {n}>")
        poss_n = values.get(f"POSSESSIVE_{n}", poss)
        definition = definition.rstrip()
        if not definition.endswith("."):
            definition += "."
        extra_defs.append(f"{label} is {definition}")
        retained = values.get(f"RETAINED_{n}", values["RETAINED"])
        extra_retentions.append(
            f"{label} (appears in [Shot 1]): fully_preserved - {poss_n} {retained} are held "
            f"identical to {plate} in every frame with zero drift."
        )
    if extra_defs:
        lines = prompt.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("summary:"):
                lines[i - 1 : i - 1] = extra_defs
                break
        prompt = "\n".join(lines)
        prompt = prompt.replace(
            "\n\ndetailed_description:", "\n" + "\n".join(extra_retentions) + "\n\ndetailed_description:"
        )

    leftover = sorted(set(SLOT_RE.findall(prompt)))
    if leftover:
        print("error: unfilled slots, add them to your scene file:", file=sys.stderr)
        for slot in leftover:
            hint = shot.get("extra_slots", {}).get(slot, "")
            if not hint and KINDS[kind].get(slot, "") is None:
                hint = f"the '{kind}' vocabulary has no default for this, you must supply it"
            print(f"  {slot:<24} {hint}", file=sys.stderr)
        if "subject_warning" in shot:
            print(f"\n  {shot['subject_warning']}", file=sys.stderr)
        print(f"\n  python {Path(sys.argv[0]).name} {shot['slug']} --slots", file=sys.stderr)
        sys.exit(1)

    return prompt.rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("shot", nargs="?", help="shot slug, e.g. snorricam")
    ap.add_argument("--list", action="store_true", help="list available shots")
    ap.add_argument("--slots", action="store_true", help="show the slots this shot needs")
    ap.add_argument("--scene", type=Path, help="your scene json")
    ap.add_argument("-o", "--out", type=Path, help="write here instead of stdout")
    args = ap.parse_args()

    shots = load_shots()
    if args.list or not args.shot:
        cmd_list(shots)
        return

    if args.shot not in shots:
        near = [s for s in shots if args.shot in s]
        sys.exit(f"error: no shot '{args.shot}'."
                 + (f" Did you mean: {', '.join(near)}?" if near else " Try --list."))
    shot = shots[args.shot]
    scaffold = fenced_block(SCAFFOLD_MD, "text")

    if args.slots:
        scene = json.loads(args.scene.read_text(encoding="utf-8")) if args.scene else {}
        cmd_slots(shot, scaffold, kind_of(scene))
        return

    if not args.scene:
        sys.exit("error: --scene is required. Copy scripts/scene.example.json and edit it, "
                 f"or run: build_prompt.py {args.shot} --slots")
    scene = json.loads(args.scene.read_text(encoding="utf-8"))

    prompt = build(shot, scene, scaffold)

    for key, label in (("framing_note", "FRAMING"), ("gear_warning", "GEAR"),
                       ("timing_warning", "TIMING"), ("scene_warning", "SCENE"),
                       ("performance_note", "PERFORMANCE"), ("subject_warning", "SUBJECT")):
        if key in shot:
            print(f"!! {label}: {shot[key]}", file=sys.stderr)
    print(f"-- {shot['slug']} ({kind_of(scene)}): render at {shot['length']} frames, 20 steps, "
          f"turbo LoRA off, one identity plate, ref_image_size max", file=sys.stderr)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(prompt, encoding="utf-8", newline="\n")
        print(f"-- written to {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(prompt)


if __name__ == "__main__":
    main()
