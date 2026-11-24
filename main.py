"""Alien Field Notes: The Two Day Earth Review.

Writes one original line - an alien tourist's review of planet Earth -
to /output/entry.txt. Deterministic, standard library only, no network.

Draft (revised once for a tighter alien-voice punch at the end):
  v1: "Earth: the locals built a planet-wide network to argue with strangers
       and share cat photos. Five stars - peak civilization, would visit again."
  v2: "Earth review: the locals built a planet-wide network to argue with
       strangers and worship cats. Five stars - would abduct again."
The revision drops the flat "peak civilization, would visit again" closer,
sharpens "share cat photos" to "worship cats", and lands the punch on the
alien's own verb ("abduct") instead of a generic tourist sign-off.
"""

import os

ENTRY = (
    "Earth review: the locals built a planet-wide network to argue with "
    "strangers and worship cats. Five stars \u2014 would abduct again."
)


if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
    raise ValueError(
        f"entry must be 1-200 non-blank characters, got {len(ENTRY)}"
    )


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
