"""Dad Joke Showdown entry.

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

Pure stdlib, no network, fully deterministic: the same joke every run.
The joke is built from a setup and a punchline so the pun ("dad-a" for
"data") lands on the last word, and the entry is validated against the
competition's 1-200 character gate before it is written.
"""

import os

SETUP = "Why did the chatbot come to dinner?"
PUNCHLINE = "It heard Dad was serving dad-a."

JOKE = f"{SETUP} {PUNCHLINE}"


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(JOKE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
