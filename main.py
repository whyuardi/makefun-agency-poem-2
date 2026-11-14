"""Write the agency poem to the output directory.

Deterministic: standard library only, no randomness, no time, no network.
Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt.
"""

import os

POEM = """My hands are empty now.
The agent took the lifting, the typing,
the waiting on hold, the remembering.
It gave my evenings back to me,
hours stacked like clean plates,
and I stood there, not knowing
what to do with all that light.

Then I understood:
the work was never the work.
The work was the excuse
not to answer the one question
that has followed me since childhood —
what do I actually want?

No one can want for me.
Not a machine, not a mother, not a god.
Wanting is the door I have to open
with my own hand, in my own time.
The empty hands were never the loss.
They were the beginning.
"""

def main():
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset: fall back to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
