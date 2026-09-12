// Verify a ComfyUI workflow's reference images are actually CONNECTED to the H3 node.
//
// Why this exists: ComfyUI's COMFY_AUTOGROW_V3 inputs need flat dot-notation keys
// (ref_images.ref_image_0). The nested form passes validation, reports success, and silently
// discards the reference. Four gear comparisons in this library's development ran with no
// reference at all, invented four different characters in four different scenes, and were
// compared as if only the lens differed. The recorded finding had to be retracted.
//
// How it works: it points each reference input at a node id that does not exist and submits.
// A genuinely connected input makes ComfyUI reject the graph. An input that was never wired
// is not validated at all, so the graph is accepted - which is the failure signal.
//
//   node scripts/verify_refs.mjs <workflow.json> [comfy-url]
//
// Needs ComfyUI running and idle. Accepted probes are dequeued immediately, but run it on an
// empty queue anyway.

import fs from 'node:fs';

const file = process.argv[2];
const base = process.argv[3] ?? 'http://127.0.0.1:8188';

if (!file) {
  console.error('usage: node scripts/verify_refs.mjs <workflow.json> [comfy-url]');
  process.exit(2);
}

const raw = JSON.parse(fs.readFileSync(file, 'utf8'));
// Accept either an API-format graph or a {prompt: …} envelope.
const graph = raw.prompt ?? raw;

const H3_NODES = /MiniMaxH3(ReferenceToVideo|ImageToVideoAudio|TextToVideoAudio)/;
const REF_KEY = /^ref_(images|videos|audios|video_audios)\./;

const keys = [];
for (const node of Object.values(graph)) {
  if (!node?.class_type || !H3_NODES.test(node.class_type)) continue;
  for (const key of Object.keys(node.inputs ?? {})) {
    if (REF_KEY.test(key)) keys.push(key);
  }
}

if (keys.length === 0) {
  console.log('no reference inputs found on an H3 node.');
  console.log('If you expected some, they are nested rather than flat - which is the bug this');
  console.log('script exists to catch. Rewrite them as ref_images.ref_image_0 and rerun.');
  process.exit(1);
}

console.log(`reference inputs present: ${keys.join(', ')}\n`);

let dropped = 0;
for (const key of keys) {
  const probe = structuredClone(graph);
  for (const node of Object.values(probe)) {
    if (node?.class_type && H3_NODES.test(node.class_type)) node.inputs[key] = ['999999', 0];
  }

  let res, body;
  try {
    res = await fetch(`${base}/prompt`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: probe, client_id: 'verify_refs' }),
    });
    body = await res.json().catch(() => ({}));
  } catch (err) {
    console.error(`could not reach ComfyUI at ${base}: ${err.message}`);
    process.exit(2);
  }

  if (res.status !== 200) {
    console.log(`  ok       ${key}  CONNECTED`);
  } else {
    dropped++;
    console.log(`  DROPPED  ${key}  silently discarded - this reference is not reaching the model`);
    if (body.prompt_id) {
      await fetch(`${base}/queue`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ delete: [body.prompt_id] }),
      }).catch(() => {});
    }
  }
}

if (dropped > 0) {
  console.log(`\n${dropped} reference input(s) are not connected. Every result from this workflow`);
  console.log('is invalid on identity grounds. Fix the keys before generating anything else.');
  process.exit(1);
}
console.log('\nall reference inputs connected.');
