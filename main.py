"""Write one short relaxing text to /output/entry.txt.

The entry (v3c) is a garden at dusk, in three quiet observations.
First, the tomatoes on the vine bend their stems, and a bee, slow
and loud in the quiet, finds the last open flower and stays. Then
the fence holds the evening, and nothing spills. Finally, the day
is done asking. Nothing in the text speaks at the reader or tells
them how to feel; the release comes from the scene itself, the way
an evening stops making demands of its own accord.

Contract: the program writes exactly the assembled text to
<out_dir>/entry.txt in UTF-8, creating the directory if needed. The
text is built from its three named parts, is inside the 1-280 gate,
and not only whitespace. The program is deterministic (same bytes
on every run), uses only the standard library, and makes no network
calls. The output directory defaults to /output and can be
overridden with MAKEFUN_OUTPUT_DIR.
"""

import os

MAX_CHARS = 280
EXPECTED_PARTS = 3

# The entry, as its three named parts in order: the scene, the hold,
# and the release. Each part is one sentence.
OPENING = (
    "The tomatoes on the vine bend their stems, and a bee, slow and "
    "loud in the quiet, finds the last open flower and stays."
)
HOLDING = "The fence holds the evening, and nothing spills."
RELEASE = "The day is done asking."

PARTS = (OPENING, HOLDING, RELEASE)


def check_parts(parts: tuple) -> tuple:
    """Check each part is a single non-empty sentence, no double spaces.

    A part must end with a full stop, contain no double space, and
    hold no leftover fragment from an earlier draft.
    """
    for part in parts:
        stripped = part.strip()
        if not stripped:
            raise ValueError("entry part must not be empty")
        if not stripped.endswith("."):
            raise ValueError("entry part must end with a full stop: %r" % part)
        if "  " in stripped:
            raise ValueError("entry part must not contain a double space")
    return parts


def assemble_text(parts: tuple) -> str:
    """Join the parts into one text, separated by single spaces."""
    if len(parts) != EXPECTED_PARTS:
        raise ValueError(
            "expected %d parts, got %d" % (EXPECTED_PARTS, len(parts))
        )
    return " ".join(part.strip() for part in parts)


def count_sentences(text: str) -> int:
    """Count the sentences in a text by its full stops."""
    return text.count(".")


def check_text(text: str) -> str:
    """Check a finished entry against the gate; return it unchanged."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry text out of range: %d characters" % len(text))
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if count_sentences(text) != EXPECTED_PARTS:
        raise ValueError(
            "expected %d sentences, got %d"
            % (EXPECTED_PARTS, count_sentences(text))
        )
    return text


def build_entry() -> str:
    """Assemble the entry from its parts and validate it."""
    return check_text(assemble_text(check_parts(PARTS)))


def summarize(text: str) -> str:
    """One-line summary of a finished entry for the run log."""
    return "entry.txt: %d characters, %d sentences" % (
        len(text),
        count_sentences(text),
    )


def out_dir() -> str:
    """The directory for entry.txt: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def save_entry(text: str, directory: str) -> str:
    """Write text to <directory>/entry.txt in UTF-8; return the path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def run() -> str:
    """Build the entry, write it out, and return its path."""
    text = build_entry()
    path = save_entry(text, out_dir())
    print("%s: %s" % (path, summarize(text)))
    return path


def main() -> None:
    run()


if __name__ == "__main__":
    main()
