#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea
to /output/entry.txt.

The pitch: funerals for dead houseplants. It sounds like a joke,
but plant parents really do grieve, and grief services are a real
market - the absurd premise turns out to pencil out. The sentence
does the judge's whole job in one line: it names the odd thing sold
(the funeral), who pays (guilt-ridden plant owners), and the price
($89), so the reader goes from laughing to nodding.
"""

import os

SENTENCE = (
    "We stage elaborate funerals for dead houseplants, and guilt-ridden "
    "owners pay $89 for a eulogy, a tiny coffin, and a certificate of closure."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    assert text.count(".") == 1, "must be exactly one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
