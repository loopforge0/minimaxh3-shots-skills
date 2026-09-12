#!/usr/bin/env python3
"""Fetch MiniMax's own H3 prompt-writing skill and its two reference guides into upstream/.

Those files are MiniMax's, under MiniMax's licence, so this repository points at them rather than
vendoring copies. upstream/ is gitignored.

    python scripts/fetch_upstream_guides.py

Standard library only.
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEST = REPO / "upstream"

RAW = "https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/"

FILES = {
    ".claude/skills/h3-prompt-writing/SKILL.md":
        "MiniMax's prompt-writing skill. Owns the prompt format for all five modes.",
    ".claude/skills/h3-prompt-writing/references/base-en.txt":
        "T2VA / I2VA / FL2VA / L2VA. Section 4.3 is the camera-motion vocabulary.",
    ".claude/skills/h3-prompt-writing/references/ref-en.txt":
        "Ref2VA, the six-section format this library's shots all use.",
}


def fetch(rel: str) -> bytes | None:
    url = RAW + rel
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return resp.read()
    except urllib.error.HTTPError as exc:
        print(f"  skip  {rel}  (HTTP {exc.code})")
    except urllib.error.URLError as exc:
        print(f"  fail  {rel}  ({exc.reason})")
    return None


def main() -> None:
    print(f"fetching into {DEST}\n")
    got = 0
    for rel, note in FILES.items():
        data = fetch(rel)
        if data is None:
            continue
        out = DEST / Path(rel).name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"  ok    {out.name:<16} {len(data):>7,} bytes   {note}")
        got += 1

    if not got:
        sys.exit("\nnothing fetched. Check the network, or clone "
                 "https://github.com/MiniMax-AI/MiniMax-H3 and copy "
                 ".claude/skills/h3-prompt-writing/ by hand.")

    readme = DEST / "README.md"
    readme.write_text(
        "# upstream\n\n"
        "MiniMax's files, fetched by `scripts/fetch_upstream_guides.py`. Not part of this "
        "repository and not covered by its licence. Gitignored.\n\n"
        "Source: https://github.com/MiniMax-AI/MiniMax-H3\n\n"
        "`base-en.txt` section 4.3 is the camera-motion vocabulary this library composes from. If it "
        "ever disagrees with `.claude/skills/h3-camera-shots/references/camera-grammar.md`, "
        "**the upstream file wins** and the library copy is stale.\n",
        encoding="utf-8", newline="\n")

    print(f"\n{got} file(s). To install MiniMax's skill properly, copy the h3-prompt-writing "
          "directory into ~/.claude/skills/ so it is discoverable by name.")


if __name__ == "__main__":
    main()
