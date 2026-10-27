# POV Shot

**Status:** verified. Part 2.
**Effect:** the shot is the eyes of an unseen viewer. The camera moves the way their head does, and the
only part of them that ever appears is a hand. What happens in front of them is your action, not the move.
**Primitives:** `POV`, one of MiniMax's twelve.
**Reference:** the opening of *Halloween*, and *Hardcore Henry*, shot entirely this way.

## Shot line

> A first-person POV shot {PLACE}, with {ENVIRONMENT_ELEMENTS} around: the camera is the eyes of an unseen
> viewer and moves exactly as the viewer's head does, swaying gently with each step when the viewer walks,
> and {SUBJECT} is seen through the viewer's eyes. Only the viewer's own hand ever appears, reaching in from
> the bottom of the frame when the viewer touches or takes something. {VIEWER_ACTION}

## The move is only the camera

The shot line sets up the first-person camera and nothing else. The walk-up, the called name, the reach and
the handshake all go in `{VIEWER_ACTION}`. Earlier versions wrote a whole scene into the move; it worked once
the scene moved out into the action.

**Say where the character is at the start.** With the scene only in the action, and nothing saying she was in
view at the opening, H3 opened on the empty road and found her halfway through. Where the subject is on the
first frame belongs in your action.

## How it got here

| Take | What came back | What changed |
|---|---|---|
| 1 | A follow shot from behind her, not a POV | The character was the viewer, and the standard retention line holds her face "identical to `<Picture 1>` in every frame", which asks for her face to be on screen |
| 2 | A true first-person view, but two hands held out in front, which read as a zombie game | From here on the character is the person the viewer *sees*, not the viewer |
| 3 to 5 | A walk-up, a tap on the shoulder, a handshake | The lessons below |
| 6 | The camera move alone, with the walk-up and the called name as the action | Shipped |

## Gotchas

- **A passive task comes out as standing still.** "Reading a menu" or "unlocking a car" gave a subject who
  barely moved. Give them something busy, like the shipped prompt's spanner under a car bonnet.
- **The hand needs beats.** Write them as "first... then... only then", with the hand leaving the frame
  between them.
- **A tap lands in the air** unless the camera comes within arm's reach first.
- **192 frames.** A walk-up, a called name, a turn and a handshake do not fit in 124.
- The shipped prompt rewrote the retention line by hand: her hair and clothes held from behind at first,
  her face from the moment she turns. `build_prompt.py` writes the standard line, so edit it if your subject
  starts with their back to the viewer.
- The called name is a dialogue line in the shipped prompt (`<d>[English] Mei?</d>`, spoken by the unseen
  viewer). See `prompts/P2-01_pov.txt`.

## Machine-readable

```json
{
  "id": "P2-01",
  "slug": "pov",
  "name": "POV shot",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 192,
  "framing": "A first-person POV shot {PLACE}",
  "framing_summary": "a first-person POV shot",
  "summary_action": "seen through the eyes of an unseen viewer",
  "shot_intro": "custom",
  "shot_line": "A first-person POV shot {PLACE}, with {ENVIRONMENT_ELEMENTS} around: the camera is the eyes of an unseen viewer and moves exactly as the viewer's head does, swaying gently with each step when the viewer walks, and {SUBJECT} is seen through the viewer's eyes. Only the viewer's own hand ever appears, reaching in from the bottom of the frame when the viewer touches or takes something. {VIEWER_ACTION}",
  "extra_slots": {
    "VIEWER_ACTION": "what happens in front of the viewer, starting with where the subject is on the first frame, e.g. \"The viewer takes a few slow steps toward <Subject 1>, who stands just ahead with her back to the camera, busy at a task. The viewer calls her name; she turns, smiles and holds out her hand, and one hand reaches in from the bottom right of the frame to shake it.\""
  },
  "performance_note": "Give the subject something busy to be doing at the start. A passive task comes out as standing still."
}
```

## Prompt as it ran

`prompts/P2-01_pov.txt`
