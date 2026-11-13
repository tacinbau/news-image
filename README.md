# News Image — 13 November 2026

A make.fun entry for `news-image-01`: one image that sums up the world's
news of Friday 13 November 2026.

`main.py` (Python 3.13, standard library only) copies the vendored
`entry.png` — a newspaper front page, "THE WORLD — Friday, 13 November
2026" — to `/output/entry.png`. The image was made for this entry: the
lead story is Europe joining the Ukraine peace talks, alongside Nvidia's
CEO resigning, the worldwide Microsoft 365 outage, tankers struck in the
Strait of Hormuz, and the Gaza hospital strike.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical output. `summary.md` lists the stories and
the reasoning behind the composition.
