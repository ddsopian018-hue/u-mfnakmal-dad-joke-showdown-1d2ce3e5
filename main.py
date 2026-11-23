"""Dad Joke Showdown entry.

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

Pure stdlib, no network, fully deterministic: the same joke every run.
"""

import os

JOKE = "Why did the chatbot come to dinner? It heard Dad was serving dad-a."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
