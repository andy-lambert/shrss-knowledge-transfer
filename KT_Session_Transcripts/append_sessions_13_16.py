#!/usr/bin/env python3
"""Append sessions 13-16 transcript markdown to consolidated file."""
from pathlib import Path

DIR = Path(__file__).resolve().parent
CONSOLIDATED = DIR / "SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md"

# (filename, session_title, session_date)
SESSIONS = [
    ("13_SHRSS_Adobe_KT_Session_Transcript_Page_Templates_2_26_2026.md", "Page Templates", "2026-02-26"),
    ("14_SHRSS_Adobe_KT_Session_Transcript_Nav_and_Data_Displays_3_2_2026.md", "Nav and Data Displays", "2026-03-02"),
    ("15_SHRSS_Adobe_KT_Session_Transcript_LOB_Specific_Components_3_3_2026.md", "LOB Specific Components", "2026-03-03"),
    ("16_SHRSS_Adobe_KT_Session_Transcript_Additional_Components_3_4_2026.md", "Additional Components", "2026-03-04"),
]


def main():
    consolidated = CONSOLIDATED.read_text(encoding="utf-8", errors="replace").rstrip()
    sections = []
    for filename, title, date in SESSIONS:
        path = DIR / filename
        if not path.exists():
            print(f"Skip (not found): {filename}")
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        # First 5 lines: meeting title, blank, date, blank, duration
        header_lines = lines[:5]
        body_lines = lines[5:]
        body = "\n".join(body_lines).strip()
        section = f"""## Session: {title} — {date}

{header_lines[0]}

{header_lines[2]}

{header_lines[4]}

{body}
"""
        sections.append(section)
    out = consolidated + "\n\n" + "\n\n".join(sections) + "\n"
    CONSOLIDATED.write_text(out, encoding="utf-8")
    print("Appended sessions 13–16 to consolidated.")


if __name__ == "__main__":
    main()
