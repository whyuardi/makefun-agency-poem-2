# The Salt

An entry for agency-poem-01: a program that writes one poem about
agency to `entry.txt`.

The idea in one line: the agent cooks exactly as the book says, and
the speaker keeps the salt — the one step no instruction can carry.

Run it with:

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

It writes `entry.txt` in the output directory, the same bytes on
every run. Python 3.13, standard library only.
