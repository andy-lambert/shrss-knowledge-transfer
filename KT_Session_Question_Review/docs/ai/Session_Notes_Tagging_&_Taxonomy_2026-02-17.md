# Session Notes — Tagging & Taxonomy — 2026-02-17

**Session:** Tagging & Taxonomy  
**Date:** February 17, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer - DAM Sessions-20260217_130312  
**Duration:** 1h 2m 28s  
**Primary presenter:** Andy Lambert (Adobe)

---

## Session context

- Objective: Understand how tagging, metadata, and taxonomy are implemented and how they drive dynamic content, search filters, and cross-site behavior. DAM-focused session with Chris Lewis planned for next day (metadata schemas, best practices).
- Tags console: Tools → Tagging. Namespace SHRSS under `/content/cq:tags/SHRSS`. Top-level: regions, brands, hotels, categories, category, news categories, events categories, lines of business, property, etc. Featured news example: content fragment card list uses tag “featured news” to pull content for blog.
- Don: Multiple “categories” (categories, category, news categories, events categories) and property/locations structure—why not consolidated? Andy: different purposes; naming could be clearer; consolidation = assess functional implications (hard-coded paths vs config), then green-light; move tool updates references.

---

## What was covered

1. **Taxonomy** — SHRSS namespace; mix of categories/category/news/events; property vs hotel/casino/cafe under locations. Consolidation desired; Andy to assess code/config impact and report.
2. **Generic lists (ACS AEM Commons)** — Path-to-tag mapping (e.g. Atlantic City property → tag set); governs which tags can be used in a section. Don: how to use? Add to Confluence Q&A. Social media types also in generic lists. Not for corporate/careers today; for upcoming sites.
3. **Tags and content fragments** — Categories field in CF = tag IDs (filtering). CQ tags on assets/pages. Export of pages/experience fragments/content fragments showing tag usage (reference doc). Content fragment model: category field can be tag-driven or enumeration; locations example = not all tag-driven; need to confirm which are which.
4. **Asset metadata and tags** — Document: which asset metadata fields are driven by tags (CQ tags, brand, venues and branded experiences, LOB, event categories). Don: event categories on asset ≠ event categories for CF—confusing; needs cleanup.
5. **Permissions** — Granular permissions on tag tree (Permissions console, group, path under cq:tags). Read/create/update/delete; replicate (publish). Deny vs allow. Lock down so not everyone adds/deletes tags.
6. **Best practices** — Single vocabulary; avoid synonyms; avoid over-tagging; document permissions; generic lists = admin/super author only, not average author.
7. **Export metadata to Excel** — Folder → Export metadata; name; include subfolders; do not select “all properties”; use type-ahead for fields (e.g. SHRSS-prefixed). Edit in Excel, re-upload from anywhere in DAM to bulk update. Don: pre-populated set for export? Andy: pain; keep text file, copy/paste.

---

## Questions, comments, and answers (captured)

*See **Tagging_Taxonomy_Metadata_Gov** sheet in tracker.*

- Why multiple category directories? Consolidation and naming cleanup—Andy to assess implications, then SHRSS can change.
- Restructure tags—break anything? Assess first; prefer no hard-coded paths; env vars/config where possible; then green-light.
- Move tool: updates references.
- Generic lists: what are they for, how to use? Add to Confluence; Andy/Vinay to answer.
- Content fragment model category: tag-driven vs enumeration? Depends on use case; some in model are not tag-driven (e.g. locations). Gap/enhancement to align.
- Asset “categories” vs content fragment categories: different (event categories on asset vs events CF); needs cleanup—action item.
- Permissions on tags: granular by path; use groups.
- Export metadata: pre-populated field set? Not OOTB; use text file of property names.

---

## Product Director — own questions

1. **Governance:** Who owns the SHRSS tag vocabulary and the decision to consolidate categories/category/news/events? What is the process to add a new tag namespace or top-level folder?
2. **Authoring:** When an author picks “category” in a content fragment or asset, where do they see tag-driven vs fixed list? Can we have a one-pager: “Tag-driven fields vs dropdowns” by model/asset type?
3. **Tagging:** Process for bulk retagging (e.g. after consolidation)—export, edit, re-upload? Any impact on published content or references?
4. **Gap analysis:** Which tag/taxonomy changes are safe for SHRSS to do now vs require code/config (Andy’s assessment)?
5. **Permissions:** Which group(s) should have create/update/delete on SHRSS tags vs read-only for authors?

---

*End of session notes. All Q&A rows in **Tagging_Taxonomy_Metadata_Gov** sheet.*
