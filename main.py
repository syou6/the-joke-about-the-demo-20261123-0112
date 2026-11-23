"""Entry writer for the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents
to the output file. Deterministic, standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "My demo worked perfectly in rehearsal: my agent was presenting "
    "a screenshot it had hallucinated of the app working."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
