#!/usr/bin/env python3
"""
Task 5: Consolidate all SHRSS tag structure .content.xml files under the source
directory into a single .content.xml in the target directory.
Recursively expands each placeholder element with the content from the
matching subdirectory's .content.xml (inner content between jcr:root tags).
"""
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCE = Path("/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM/00_Drafts_and_Resources/tag_working_directory/_cq_tags/shrss")
TARGET = Path("/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM/00_Drafts_and_Resources/tag_working_directory/shrss_tag_structure_definition_files")

NS = {"jcr": "http://www.jcp.org/jcr/1.0", "cq": "http://www.day.com/jcr/cq/1.0", "sling": "http://sling.apache.org/jcr/sling/1.0"}

def local_name(tag):
    if tag and "}" in tag:
        return tag.split("}", 1)[1]
    return tag or ""

def expand(source_dir: Path, elem: ET.Element) -> ET.Element:
    """Recursively expand elem with content from source_dir/<tagname>/.content.xml."""
    tag = elem.tag
    name = local_name(tag)
    content_file = source_dir / name / ".content.xml"
    if not content_file.exists():
        return elem
    try:
        child_tree = ET.parse(content_file)
        child_root = child_tree.getroot()
        inner = list(child_root)  # direct children of jcr:root
    except Exception:
        return elem
    if not inner:
        return elem
    # Create new element with same tag (and copy attributes if any)
    new_elem = ET.Element(tag, attrib=elem.attrib)
    subdir = source_dir / name
    for child in inner:
        expanded = expand(subdir, child)
        new_elem.append(expanded)
    return new_elem

def main():
    root_file = SOURCE / ".content.xml"
    if not root_file.exists():
        raise SystemExit(f"Source root not found: {root_file}")
    tree = ET.parse(root_file)
    root = tree.getroot()
    # Expand each direct child of jcr:root
    for i, child in enumerate(list(root)):
        expanded = expand(SOURCE, child)
        root.remove(child)
        root.insert(i, expanded)
    # Ensure target directory exists
    TARGET.mkdir(parents=True, exist_ok=True)
    out_file = TARGET / ".content.xml"
    # Register namespaces so output uses jcr:, cq:, sling: prefixes
    ET.register_namespace("jcr", NS["jcr"])
    ET.register_namespace("cq", NS["cq"])
    ET.register_namespace("sling", NS["sling"])
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
