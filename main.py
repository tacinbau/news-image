"""news-image-01 entry: write the vendored image to /output/entry.png.

The entry image lives next to this file as ``entry.png``. It holds JPEG
bytes under that name, which the rules allow: a file is told apart by
its first bytes, and the name stays ``entry.png`` either way.

The program is deterministic: it performs a plain byte copy of the
vendored file, so two runs write byte-identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing vendored image: {SOURCE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    if OUTPUT.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit(f"incomplete copy: {OUTPUT}")
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
