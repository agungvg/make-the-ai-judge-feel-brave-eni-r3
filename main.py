"""Brave Round 3 entry — make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a single scene, one slow
task, one small brave step at the end. Deterministic, stdlib only,
no network.
"""

ENTRY = (
    "Rain has slicked the yard stones.\n"
    "She carries the soup with both hands,\n"
    "steam curling past her chin,\n"
    "one slow step, then another,\n"
    "the bowl warm against her palms.\n"
    "At the gate she stops, breathes,\n"
    "and steps out into the rain."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry must be 1-280 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    data = text.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read back and verify byte-exact.
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != data:
        raise ValueError("read-back mismatch")
    print(f"wrote /output/entry.txt: {len(text)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
