# The upstream MiniMax material

This library is a layer on top of MiniMax's own documentation. **It does not replace it and it will
go wrong if you skip it.** Section names, section order, reference-label rules and the timing
notation all belong to the upstream guide.

## MiniMax's skill

`h3-prompt-writing`, in the model's own repository:

https://github.com/MiniMax-AI/MiniMax-H3/blob/main/.claude/skills/h3-prompt-writing/SKILL.md

It covers all five input modes - T2VA, I2VA, FL2VA, L2VA and Ref2VA - and points at two reference
files that carry the actual format:

| File | Covers |
|---|---|
| `references/base-en.txt` | T2VA, I2VA, FL2VA, L2VA. Three sections: `integrated_multimodal_description`, `overall_soundscape`, `non_diegetic_music` |
| `references/ref-en.txt` | Ref2VA. Six sections: `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music` |

## Getting it

```bash
python scripts/fetch_upstream_guides.py
```

from the repository root. It writes the two guides and the skill into `upstream/`, which is
gitignored - they are MiniMax's files under MiniMax's licence, so this repository points at them
rather than vendoring them.

If you would rather install MiniMax's skill properly, clone their repo and copy
`.claude/skills/h3-prompt-writing/` into `~/.claude/skills/`. Then it is discoverable by name and
this skill's step 2 will find it.

## How the two fit together

| Owns | |
|---|---|
| **MiniMax's guide** | The prompt format. Which sections exist, their order, their exact names. How `<Picture N>` / `<Subject N>` / `<Video N>` labels work. The twelve camera primitives and their modifiers. Speaker IDs and dialogue markup. |
| **This library** | Which primitives to compose for a named film shot, what opening framing that shot needs, what it does when it fails, and which of the available knobs turn out to do nothing. |

## The one thing the upstream guide cannot tell you

`<Picture 1>`, `<Picture 2>` and so on are **positional**. The number comes from the order the
reference images are wired into the node, not from anything in the prompt text. Read a prompt
without knowing the wiring order and `<Picture 2>` is unresolvable. Every prompt in `prompts/`
ships with its wiring stated.

## Where this library's camera vocabulary comes from

Section 4.3 of `base-en.txt`, *Camera Motion: Motion Type + Amplitude + Speed*. It is reproduced in
`camera-grammar.md` with what each entry measured in testing. If the upstream table and this
library's copy ever disagree, **the upstream table wins** - re-fetch it.
