"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (<=280 chars) recalling a childhood memory to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Pure standard library.
"""

import os
from pathlib import Path

# The sentence is 164 characters, one line: the screen door, barefoot
# fireflies at dusk, and the mother's call from the porch — concrete
# sensory detail with the ache left in the last clause.
SENTENCE = (
    "Every June I still hear the screen door slam behind me as I ran "
    "barefoot into the dusk to catch fireflies, my mother's voice already "
    "calling me home from the porch."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 280, "sentence must be 1-280 characters"
    assert SENTENCE.strip() == SENTENCE, "no leading/trailing whitespace"
    assert "\n" not in SENTENCE, "must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
