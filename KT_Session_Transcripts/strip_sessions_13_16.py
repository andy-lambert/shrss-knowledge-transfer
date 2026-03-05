#!/usr/bin/env python3
"""Remove image refs and normalize line continuations in pandoc markdown transcripts (sessions 13-16)."""
import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
FILES = [
    "13_SHRSS_Adobe_KT_Session_Transcript_Page_Templates_2_26_2026.md",
    "14_SHRSS_Adobe_KT_Session_Transcript_Nav_and_Data_Displays_3_2_2026.md",
    "15_SHRSS_Adobe_KT_Session_Transcript_LOB_Specific_Components_3_3_2026.md",
    "16_SHRSS_Adobe_KT_Session_Transcript_Additional_Components_3_4_2026.md",
]

# Image line: optional leading spaces, ![](media/...){...}, optional **, optional \ at end
IMAGE_LINE = re.compile(r"^\s*!\[\]\(media/[^)]+\)\{[^}]+\}\s*\*?\\?\s*$")


def strip_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    out = []
    for line in lines:
        stripped = line.strip()
        if IMAGE_LINE.match(stripped):
            continue
        # Skip standalone image-only lines (no {attrs})
        if re.match(r"^\s*!\[\]\(media/", stripped):
            continue
        # Strip trailing backslash (pandoc line continuation)
        line = line.rstrip()
        if line.endswith("\\"):
            line = line[:-1].rstrip()
        # Add leading ** for speaker lines (match "Name** 0:00" or "Name** started")
        if line and not line.startswith("**") and re.match(
            r"^[A-Za-z][^*]*\*\* (?:started|\d+:\d+)", line
        ):
            line = "**" + line
        out.append(line)
    path.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    for name in FILES:
        p = DIR / name
        if p.exists():
            strip_file(p)
            print(f"Stripped: {name}")
        else:
            print(f"Skip (not found): {name}")
