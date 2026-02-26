#!/usr/bin/env python3
"""Remove image refs and normalize line continuations in pandoc markdown transcript."""
import re
import sys
from pathlib import Path

def strip_images(path_in: Path, path_out: Path) -> None:
    text = path_in.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    out = []
    for line in lines:
        # Skip lines that are only image refs (optional **\ at end)
        if re.match(r'^!\[\]\(media/image\d+\.png\)\{[^}]+\}\s*\*\\?$', line.strip()):
            continue
        # Skip standalone image-only lines (any variant)
        if re.match(r'^!\[\]\(media/', line.strip()):
            continue
        # Strip trailing backslash (pandoc line continuation)
        line = line.rstrip()
        if line.endswith("\\"):
            line = line[:-1].rstrip()
        # Restore leading ** for speaker lines (was on removed image line)
        if line and not line.startswith("**") and re.match(r'^[\w\s\(\)\-]+(?:\(SHRSS\))?\*\* \d+:\d+', line):
            line = "**" + line
        out.append(line)
    path_out.write_text("\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    for name in ["10_SHRSS_Adobe_KT_Session_Transcript_Locations_Day_2_2_24_2026.md",
                 "12_SHRSS_Adobe_KT_Session_Transcript_Media_2_25_2026.md"]:
        base = Path(__file__).resolve().parent
        strip_images(base / name, base / name)
