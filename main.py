"""make.fun entry: The poem about stopping.

Writes exactly one short poem about agency — the power to stop and to
stay — to /output/entry.txt. Deterministic, no network, no randomness.
"""

POEM = (
    "I taught my agent to stop \u2014\n"
    "not to stall, but to stand still,\n"
    "hand on the door, and ask:\n"
    "is this still yours to do?\n"
    "\n"
    "It stayed. I stayed.\n"
    "The work waited, unhurried.\n"
    "And the choice, for once,\n"
    "was ours to keep."
)

# Competition gate: 1-280 Unicode code points, not only whitespace.
MAX_ENTRY_CHARS = 280


def main() -> None:
    # The judge reads entry.txt as text, so a NUL byte would corrupt the
    # poem (and a truncated/empty file would fail the gate outright).
    assert "\x00" not in POEM, "poem must not contain NUL bytes"
    assert 1 <= len(POEM) <= MAX_ENTRY_CHARS, (
        f"poem is {len(POEM)} code points"
    )
    assert POEM.strip(), "poem must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    # Guard against a partial write: read the file back and confirm the
    # exact bytes the judge will see.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="\n") as f:
        assert f.read() == POEM, "entry.txt does not match the poem"


if __name__ == "__main__":
    main()
