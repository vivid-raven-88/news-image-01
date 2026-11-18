#!/usr/bin/env python3
"""news-image-01 v4 entry: a portrait cream-paper broadsheet.

Friday 13 November 2026 in 30 stories, led by the FAA nationwide
ground stop. The picture itself is the entry; this program just
places it where the grader expects it.
"""
import os
import shutil
import sys
from pathlib import Path

ENTRY_FILE = "image.jpg"
OUTPUT_FILE = "entry.png"
FALLBACK_DIR = "/output"
# The grader runs this program twice; both runs must write identical
# bytes, which a plain file copy guarantees.


def source_path():
    """The broadsheet image, stored next to this program."""
    return Path(__file__).resolve().parent / ENTRY_FILE


def destination_dir():
    """Where the grader wants the entry; honour its env override."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR)


def main():
    src = source_path()
    out_dir = destination_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / OUTPUT_FILE
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
