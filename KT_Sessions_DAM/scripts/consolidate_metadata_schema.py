#!/usr/bin/env python3
"""
Consolidate SHRSS metadata schema: merge root .content.xml with all child node
directories into a single .content.xml. Uses same pattern as tag structure:
for each element, merge inner content from matching dir's .content.xml;
also include children from subdirectories that have .content.xml (so we get
image/items, image/jpeg, etc.).
"""
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCE = Path(
    "/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/"
    "shrss-tags-content-confs-PROD-1.0/jcr_root/conf/global/settings/dam/"
    "adminui-extension/metadataschema/shrssmetadataschema"
)
TARGET = Path(
    "/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM/"
    "00_Drafts_and_Resources/metadata_schema"
)


def local_name(tag):
    if tag and "}" in tag:
        return tag.split("}", 1)[1]
    return tag or ""


def expand(source_dir: Path, elem: ET.Element) -> ET.Element:
    name = local_name(elem.tag)
    if not name:
        return elem
    subdir = source_dir / name
    content_file = subdir / ".content.xml"
    # Get children from XML if file exists
    xml_children = []
    if content_file.exists():
        try:
            child_tree = ET.parse(content_file)
            child_root = child_tree.getroot()
            xml_children = list(child_root)
        except Exception:
            pass
    # Get children from subdirectories (may have dirs not listed in XML)
    dir_children = []
    if subdir.is_dir():
        for d in sorted(subdir.iterdir()):
            if d.is_dir() and (d / ".content.xml").exists():
                dir_children.append(d.name)
    # Merge: all names from XML first (preserve order), then dir-only
    seen = {local_name(c.tag) for c in xml_children}
    for dname in dir_children:
        if dname not in seen:
            seen.add(dname)
            # Create placeholder element (no namespace for simplicity)
            placeholder = ET.Element(dname)
            xml_children.append(placeholder)
    if not xml_children:
        return elem
    new_elem = ET.Element(elem.tag, attrib=elem.attrib)
    for child in xml_children:
        expanded = expand(subdir, child)
        new_elem.append(expanded)
    return new_elem


def main():
    root_file = SOURCE / ".content.xml"
    if not root_file.exists():
        raise SystemExit(f"Source root not found: {root_file}")
    tree = ET.parse(root_file)
    root = tree.getroot()
    # Only expand top-level folder placeholders that have a directory
    for i, child in enumerate(list(root)):
        name = local_name(child.tag)
        if name in ("image", "application", "video", "dm_video") and (SOURCE / name / ".content.xml").exists():
            expanded = expand(SOURCE, child)
            root.remove(child)
            root.insert(i, expanded)
    TARGET.mkdir(parents=True, exist_ok=True)
    out_file = TARGET / ".content.xml"
    ET.register_namespace("jcr", "http://www.jcp.org/jcr/1.0")
    ET.register_namespace("nt", "http://www.jcp.org/jcr/nt/1.0")
    ET.register_namespace("granite", "http://www.adobe.com/jcr/granite/1.0")
    ET.register_namespace("sling", "http://sling.apache.org/jcr/sling/1.0")
    ET.register_namespace("cq", "http://www.day.com/jcr/cq/1.0")
    tree.write(
        out_file,
        encoding="UTF-8",
        method="xml",
        xml_declaration=True,
        default_namespace=None,
    )
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
