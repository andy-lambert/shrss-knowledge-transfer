#!/usr/bin/env python3
"""
Generate markdown documentation from consolidated metadata schema .content.xml
with configuration details at each level.
"""
import xml.etree.ElementTree as ET
from pathlib import Path

SCHEMA_FILE = Path(__file__).resolve().parent / ".content.xml"
OUT_FILE = Path(__file__).resolve().parent / "shrss_metadata_schema_structure.md"

# Attributes to show as config (skip internal/verbose)
CONFIG_ATTRS = (
    "jcr:primaryType", "jcr:title", "sling:resourceType", "fieldLabel", "name",
    "readOnly", "emptyText", "granite:id", "metaType", "listOrder",
    "max", "min", "typeHint", "requiredCascading", "visibilityCascading",
    "cq-msm-lockable", "choicesCascading", "ordered", "size",
    "granite:rel", "tabid", "text", "value",
)


def local_name(tag):
    return tag.split("}", 1)[1] if tag and "}" in tag else (tag or "")


def attr_local_name(k):
    return k.split("}")[-1] if k and "}" in k else k


def format_attrib(attrib):
    if not attrib:
        return ""
    want_local = {a.split(":")[-1] if ":" in a else a for a in CONFIG_ATTRS}
    parts = []
    for k, v in sorted(attrib.items(), key=lambda x: x[0]):
        local = attr_local_name(k)
        if v is None or not str(v).strip():
            continue
        if local in CONFIG_ATTRS or (":" in local and local.split(":")[-1] in want_local) or local in want_local:
            parts.append(f"**{local}:** `{v}`")
    return " · ".join(parts) if parts else ""


def emit_md(elem, depth, lines, max_depth=10):
    name = local_name(elem.tag)
    if not name or name == "root":
        name = "shrssmetadataschema"
    config = format_attrib(elem.attrib)
    if depth < 6:
        indent = "#" * (depth + 1)
        if config:
            lines.append(f"{indent} {name}")
            lines.append("")
            lines.append(config)
            lines.append("")
        else:
            lines.append(f"{indent} {name}")
            lines.append("")
    else:
        bullet = "  " * (depth - 6) + "-"
        if config:
            lines.append(f"{bullet} **{name}** — {config}")
        else:
            lines.append(f"{bullet} **{name}**")
        lines.append("")
    if depth >= max_depth:
        children = list(elem)
        if children:
            lines.append(f"  {'  ' * (depth - 6)}*({len(children)} child nodes)*")
            lines.append("")
        return
    for child in elem:
        emit_md(child, depth + 1, lines, max_depth)


def main():
    tree = ET.parse(SCHEMA_FILE)
    root = tree.getroot()
    lines = [
        "# SHRSS metadata schema structure",
        "",
        "Configuration details at each level. Source: consolidated `.content.xml` in this directory.",
        "",
        "JCR path: `/conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`",
        "",
        "---",
        "",
    ]
    # Root attributes
    root_config = format_attrib(root.attrib)
    if root_config:
        lines.append("## Root (jcr:root)")
        lines.append("")
        lines.append(root_config)
        lines.append("")
    for child in root:
        emit_md(child, 1, lines, max_depth=10)
    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_FILE}")


if __name__ == "__main__":
    main()
