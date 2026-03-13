#!/usr/bin/env python3
"""
Task 6: Create markdown outline and Excel of SHRSS DAM structure from the
scrubbed folder-structure package (Task 3 output).
"""
from pathlib import Path
import openpyxl
from openpyxl.styles import Font

BASE = Path(
    "/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/"
    "dam-shrss-folder-structure-1.0/jcr_root/content/dam/shrss"
)
OUT_DIR = Path("/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM")


def get_folder_paths():
    """List all folder paths (exclude _jcr_content and folderThumbnail.dir)."""
    paths = []
    for d in BASE.rglob("*"):
        if not d.is_dir():
            continue
        rel = d.relative_to(BASE)
        parts = rel.parts
        if "_jcr_content" in parts or "folderThumbnail.dir" in parts:
            continue
        if parts == (".",):
            paths.append("/content/dam/shrss")
            continue
        path_str = "/content/dam/shrss/" + "/".join(parts)
        paths.append(path_str)
    return sorted(set(paths))


def path_to_tree(paths):
    """Convert sorted JCR paths to a tree of (name, [children]). Root name = 'shrss'."""
    root = ("shrss", [])
    for p in paths:
        if p == "/content/dam/shrss":
            continue
        parts = p.replace("/content/dam/shrss/", "").strip("/").split("/")
        node = root
        for i, part in enumerate(parts):
            parent_children = node[1]
            prefix = parts[:i]
            existing = [c for c in parent_children if c[0] == part]
            if existing:
                node = existing[0]
            else:
                child = (part, [])
                parent_children.append(child)
                node = child
    return root


def outline_md(node, depth, lines):
    name = node[0]
    indent = "  " * depth
    lines.append(f"{indent}- {name}")
    for child in sorted(node[1], key=lambda c: c[0]):
        outline_md(child, depth + 1, lines)


def main():
    paths = get_folder_paths()
    tree = path_to_tree(paths)
    # Markdown
    md_lines = [
        "# SHRSS DAM structure (outline)",
        "",
        "Current folder hierarchy under `/content/dam/shrss` from the scrubbed content package (Task 3). No assets—structure only.",
        "",
        "**Source:** `Content/dam-shrss-folder-structure-1.0`",
        "",
        "---",
        "",
    ]
    outline_md(tree, 0, md_lines)
    md_path = OUT_DIR / "SHRSS_DAM_Structure_Outline.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote {md_path}")

    # Excel: flat list with JCR Path, Folder Name, Depth, Parent Path
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Asset Folders"
    headers = ["JCR Path", "Folder Name", "Depth", "Parent Path"]
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        ws.cell(1, c).font = Font(bold=True)
    for p in paths:
        if p == "/content/dam/shrss":
            name = "shrss"
            depth = 0
            parent = "/content/dam"
        else:
            name = p.rstrip("/").split("/")[-1]
            depth = p.count("/") - 2  # /content/dam/shrss -> 0; +1 per level
            parent = "/".join(p.rstrip("/").split("/")[:-1]) or "/content/dam"
        ws.append([p, name, depth, parent])
    xlsx_path = OUT_DIR / "SHRSS_DAM_Structure.xlsx"
    wb.save(xlsx_path)
    print(f"Wrote {xlsx_path} ({len(paths)} rows)")


if __name__ == "__main__":
    main()
