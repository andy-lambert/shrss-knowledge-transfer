# SHRSS DAM Architect Ops Runbook

*Role: SHRSS DAM Architect / AEM TA*
*Goal: Keep `/content/dam/shrss` healthy, searchable, and ready for future enhancements (metadata, DM).*

------

## 1. Scope & Responsibilities

**You own:**

- DAM folder structure under `/content/dam/shrss`
- `shrss` tag namespace design and governance
- `shrssmetadataschema` (and future extensions)
- DAM authoring guardrails and best practices
- Coordination with Sites teams and developers on how DAM is used in components/CFs

------

## 2. Current State Snapshot

### 2.1 Folder Structure

- **Root:** `/content/dam/shrss`
- **Top-level branches:**
  - `cafe` — cafe property assets
  - `cf` — content fragments (locations, news, venues)
  - `corporate` — corporate brand, campaigns, careers
  - `hotel` — hotel assets (global + properties)
  - `reverb` — Reverb brand
  - `training` — training/sample content (CF + images)
- **Volume:** 230+ folders (per latest Excel export).

**Key patterns**

- CF locations follow region → country structure that aligns with `shrss/country` and `shrss/properties`.
- CF news uses `/cf/news/corporate/en/<year>/<month>`.
- Training mirrors part of CF/news for demo purposes.

------

### 2.2 Tags (`shrss` namespace)

- Rich taxonomy with branches for:
  - `lob`, `properties`, `country`, `category`, `news-categories`, `event-categories`, `venues-and-branded-experiences`, `brands`, `regions`, `products`, etc.
- Known issues:
  - Typos (`guadalaraja`, `northernindiana`).
  - Duplicates/overlaps (e.g., `northernindiana` vs `northern-indiana`, `wroclaw` also under `country`).
  - Encoded names (`_x0032_4k-boutique`, `lobby-bar-gmt_x002b_1`).
  - Trailing hyphen tags (`unplugged-`, `velvet-sessions-`).

------

### 2.3 Metadata Schema

- Active schema: `/conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`
- Current focus: **technical metadata** plus a few content fields (Location, Pdf Title).
- No dedicated fields yet for rights, campaign, owner, or internal/external.

------

## 3. Day-to-Day / Weekly Tasks

### 3.1 Intake and Triage

- **Intake channels:**
  - Tag requests (new property/venue/category)
  - Folder requests (new brand/property)
  - Issues (can’t find assets, broken images after moves, etc.)
- **Triage questions:**
  - Is there an **existing tag/folder** that already covers this use case?
  - Is this a **short-lived campaign** or a long-term classification?

### 3.2 Folder Hygiene

- Verify new folders under `/content/dam/shrss` follow the pattern:
  - `<brand>/<property>/<language>/<type>`
  - Example: `cafe/amsterdam/en/photography`
- Push back on:
  - New top-levels that don’t map to a brand/site.
  - Deep nesting that doesn’t add meaning.

------

## 4. Monthly & Quarterly Tasks

### 4.1 Tag Governance

- **Monthly:**
  - Review newly created tags under `shrss`.
  - Identify typos, duplicates, and overlapping tags.
  - Mark candidates for **merge/deprecation**.
- **Quarterly:**
  - Run a **tag usage report** (author-driven, via queries or exports).
  - Identify tags that are never used or used incorrectly.
  - Update your **Tag Cleanup Checklist** (Jira issues if applicable).

### 4.2 Metadata Schema Review

- Check if any teams are:
  - Maintaining critical information in spreadsheets (rights, campaign names).
  - Struggling to filter assets by usage rights or owner.
- From these inputs, propose:
  - New fields (rights, owner, campaign).
  - Mapping to `shrss` tags where appropriate.

------

## 5. Folder Strategy & Refactoring

### 5.1 Golden Rules

- One **root** DAM for brand: `/content/dam/shrss`.
- One **canonical folder** per combination of:
  - Brand/site (cafe, hotel, reverb, corporate)
  - Property (amsterdam, davos, atlanta)
  - Language (en)
  - Content type (logos, photography, etc.)

### 5.2 Common Pain Areas to Watch

- **Production assets in `/training`**
  - Action: Identify and move to correct brand folders.
- **Content Fragments mixed with raw assets**
  - Keep `/cf` strictly for CFs.
  - Keep images/video in the brand folders.

### 5.3 Refactor Playbook (Safe Changes)

When refactoring folders:

1. **Inventory** candidate folders and assets.
2. Use **Reference Search** to find where assets are used (pages, CFs).
3. For high-risk assets:
   - Consider leaving current path and organizing via **tags** and **collections** instead.
4. When moving assets:
   - Move in small batches.
   - Re-publish and spot-check pages.
   - Communicate to site owners.

------

## 6. Tagging Strategy & Patterns

### 6.1 Recommended Minimum Tag Set

For brand imagery:

- `shrss/lob/<lob>` (cafe/hotel/casino/…)
- `shrss/properties/<property>` when property-specific
- `shrss/country/<country>`
- `shrss/category/<category>` (logo, lifestyle, rooms, suites, awards, etc.)
- `shrss/news-categories` / `shrss/event-categories` for news/event assets

### 6.2 Tag Cleanup Backlog

Maintain a living backlog for:

- Typos to correct (rename + remap).
- Duplicates to merge (with migration plan).
- Tags to deprecate (keep for legacy references, hide from UI).

------

## 7. Metadata Roadmap

### 7.1 Short-Term

- Confirm where `shrssmetadataschema` is applied (default vs. folder-specific).
- Document current fields in a one-pager for authors.
- Identify **top 2–3 business fields** to add:
  - E.g., `Usage rights`, `Content owner`, `Primary brand`.

### 7.2 Medium-Term

- Align schema fields with `shrss` tags:
  - Avoid duplicating concepts in both a tag and a free-text field.
- Consider **folder-specific schemas** if needed:
  - Careers imagery vs. general marketing imagery.

------

## 8. Dynamic Media Readiness

Even before DM is enabled in production, you can:

- Identify candidate **image types**:
  - Hero images, banners, carousel items.
- Encourage consistent:
  - Aspect ratio naming (e.g., `hero-16x9`, `banner-4x1`).
  - Folders for DM-ready imagery (e.g., `/corporate/careers/en/photography/hero`).

When DM is adopted, you’ll already have:

- Clear source folders.
- Good tags to drive **smart crop profiles or variations**.

------

## 9. Communication & Enablement

- Maintain:
  - **Author Tagging & Metadata Quick Guide** (for authors).
  - **Author Do/Don’t Guide** (simple rules).
- Run:
  - Short refreshers when tag/schema changes go live.
- Keep:
  - A simple Confluence page with:
    - Canonical folder diagram.
    - Canonical tag combinations for common scenarios.

*End of DAM Architect Ops Runbook.*
