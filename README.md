# agency-poem-01

A Python 3.13 program (standard library only) that writes one short poem
about agency — the power to choose and to act — to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes the poem to `out/entry.txt`. Without `MAKEFUN_OUTPUT_DIR`
it writes to `/output/entry.txt`. The program is deterministic: every run
writes the same bytes.
