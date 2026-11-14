"""Write one poem about agency to entry.txt.

The poem is a kitchen handover: the agent cooks exactly as the book
says, and the speaker keeps the salt — the one step no instruction
can carry.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The agent cooks exactly as the book says:
two cups, a pinch, twelve minutes, low.
It never burns the onions.
It never tastes them either.

My grandmother stood at the same stove
and salted with her eyes closed,
one hand open over the pot,
the other holding the spoon, feeling for the pulse.

The book was right about the heat.
It was wrong about the salt.
She used to say the recipe was a map,
and the map was never the meal.

Tonight I let the agent stir.
I keep the salt.
Some things you do not hand over
because no instruction survives them —
the moment a hand decides
that this, and no more, is enough.
"""


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
