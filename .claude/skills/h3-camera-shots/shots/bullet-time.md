# Bullet Time — DROPPED, and why

**Status:** dropped. Kept in the library because the failure is more useful than the shot would have been.
**Reference:** *The Matrix* lobby scene.

## It is not a camera shot

Time-slice photography is **an array of still cameras fired in sequence**. There is no camera move to imitate,
and no subject behaviour a video model can produce, because the defining feature is that the subject is frozen
while the viewpoint travels. Verdict on the record: *"not a specific camera shot but a very specific action
scene."*

If you want the look, the orbit is the shot that exists — `orbit-360.md` — and the frozen subject is the part
you cannot have.

## What the attempt cost, measured

Same subject, same rooftop, same camera clause (`arc shot with large amplitude at fast speed`) as the verified
360 orbit. **Only the subject instruction differed.**

| subject instruction | camera travel |
|---|---|
| natural motion (the orbit) | **98-108%** of frame width |
| *"holds one single pose completely rigid"* (bullet time) | **22%** |

**An impossible instruction is not ignored. It drags the whole shot down with it**, here costing roughly 80% of
the camera move.

The style line made it worse by describing *"an array of still cameras fired in sequence"*, which tells a video
model the camera does not travel at all.

## The two rules this shot paid for

1. **Never ask for something the model cannot do.** H3 has a strong prior that people in video move. Asking for
   frozen does not get you frozen; it gets you a worse version of everything else in the shot.
   `../references/performance.md`.
2. **Never describe the apparatus.** Naming still cameras cost the camera motion the same way naming a body rig
   rendered the rig. `../references/gear.md`.

## If you want to try anyway

Cut it. Generate the orbit with natural motion, then freeze a frame in an editor and ramp around it. The
camera move is the part H3 is good at; the time freeze is the part an NLE is good at.
