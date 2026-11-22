"""Write one short relaxing text to /output/entry.txt.

The entry (v2) is a quiet house after the rain: the rain has stopped,
the gutters keep dripping, one drop at a time, as if the house is still
counting something it has already forgotten. A moth bumps the porch
light, soft as a fingertip on glass, and nobody shoos it away. Nothing
here needs you.

Contract: the program writes exactly TEXT to <out_dir>/entry.txt in
UTF-8, creating the directory if needed. TEXT is 248 Unicode code
points, inside the 1-280 gate, and not only whitespace. The program is
deterministic (same bytes on every run), uses only the standard
library, and makes no network calls. The output directory defaults
to /output and can be overridden with MAKEFUN_OUTPUT_DIR.
"""

import os

TEXT = (
    "The rain has stopped. "
    "The gutters keep dripping, one drop at a time, as if the house is still counting something it has already forgotten. "
    "A moth bumps the porch light, soft as a fingertip on glass, and nobody shoos it away. "
    "Nothing here needs you."
)

MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the entry gate: 1-280 code points, not only whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry text out of range: %d characters" % len(text))
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")


def output_dir() -> str:
    """The directory for entry.txt: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(text: str, out_dir: str) -> str:
    """Write text to <out_dir>/entry.txt in UTF-8; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    validate(TEXT)
    write_entry(TEXT, output_dir())


if __name__ == "__main__":
    main()
