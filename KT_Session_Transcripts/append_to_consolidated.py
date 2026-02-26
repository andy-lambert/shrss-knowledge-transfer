#!/usr/bin/env python3
"""Append Locations Day 2 and Media transcripts to consolidated markdown."""
from pathlib import Path

DIR = Path(__file__).resolve().parent
CONSOLIDATED = DIR / "SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md"
LOC_DAY2 = DIR / "10_SHRSS_Adobe_KT_Session_Transcript_Locations_Day_2_2_24_2026.md"
MEDIA = DIR / "12_SHRSS_Adobe_KT_Session_Transcript_Media_2_25_2026.md"

def main():
    consolidated = CONSOLIDATED.read_text(encoding="utf-8", errors="replace").rstrip()
    loc2_lines = LOC_DAY2.read_text(encoding="utf-8", errors="replace").splitlines()
    media_lines = MEDIA.read_text(encoding="utf-8", errors="replace").splitlines()

    # Locations Day 2: header is first 6 lines; body from line 7 (index 6)
    loc2_body = "\n".join(loc2_lines[6:]).strip()
    section_loc2 = f"""## Session: Locations, Day 2 — 2026-02-24

**SHRSS Adobe Knowledge Transfer-20260224_130151-Meeting Recording**

February 24, 2026, 1:00PM

1h 50m 12s

{loc2_body}
"""

    # Media: same
    media_body = "\n".join(media_lines[6:]).strip()
    section_media = f"""## Session: Media — 2026-02-25

**SHRSS Adobe Knowledge Transfer-20260225_130204-Meeting Recording**

February 25, 2026, 1:00PM

1h 34m 37s

{media_body}
"""

    out = consolidated + "\n\n" + section_loc2 + "\n\n" + section_media + "\n"
    CONSOLIDATED.write_text(out, encoding="utf-8")
    print("Appended Locations Day 2 and Media to consolidated.")

if __name__ == "__main__":
    main()
