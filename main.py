# Entrypoint for the news-image-20261119 entry (v3 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page summing up Thursday 19 November 2026 in 42 stories — 15
# illustrated panels, a world map and 27 briefs. The page source is
# index.html; the per-story verification record is STORIES.md. This
# program copies entry.png into $MAKEFUN_OUTPUT_DIR (default /output)
# and prints a one-line dossier describing the page.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261119"
DATE = "2026-11-19"
STORIES = 42
ILLUSTRATED = 15
CONTINENTS = 6


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "schema": "makefun/dossier/v1",
        "competition": COMPETITION,
        "date": DATE,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "continents": CONTINENTS,
        "image": "entry.png",
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier))


if __name__ == "__main__":
    main()
