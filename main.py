"""Write one short relaxing text to /output/entry.txt.

The text is the entry: a quiet house after the rain, shown not told,
written to leave the AI judge reading it held and unhurried.
The program is deterministic (same bytes on every run), uses only
the standard library, and makes no network calls.
"""

import os

TEXT = (
    "The rain has stopped. "
    "The gutters keep dripping, one drop at a time, as if the house is still counting something it has already forgotten. "
    "A moth bumps the porch light, soft as a fingertip on glass, and nobody shoos it away. "
    "Nothing here needs you."
)


def main() -> None:
    # Gate: the entry must be 1-280 characters (Unicode code points),
    # and not only whitespace.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text out of range: %d characters" % len(TEXT))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
