# SHRSS DAM Training & Usage Guide for Admins

*Comprehensive Session Guide (Host + Attendee Version)*

**Ticket:** AAEMDAM-3736
**Audience:** SHRSS DAM architect (primary), AEM authors, AEM devs/TAs (secondary)
**Duration:** 60 minutes  

------

## 0. Session Overview

**Objective**

Help SHRSS/HRI use AEM Assets in a consistent way across Hard Rock properties, by:

- Explaining the **current DAM structure** under `/content/dam/shrss`
- Showing how **tags (`shrss` namespace)** and **metadata (`shrssmetadataschema`)** should be used together
- Clarifying **admin/author processes** (uploading, versioning, approvals, avoiding broken references)
- Outlining an **adoption roadmap** (metadata/tag cleanup, folder refactoring, Dynamic Media readiness)
- Capturing **follow-up work** for a new backlog/roadmap

> **Timebox summary (60 min)**
>
> - 0–5: Context + goals  
> - 5–20: Current DAM content architecture  
> - 20–35: Tagging & metadata in practice  
> - 35–50: Operations & governance  
> - 50–60: Decisions, backlog items, and next steps

------

## 1. Current SHRSS DAM Landscape (15 min)

### 1.1 AEM Sites & Environments (context)

- **Production Sites**
  - `https://www.hardrock.com/` — global brand, cafes, hotels, casino, news, etc.
  - `https://reverb.hardrock.com/` — Reverb brand site
- **Upcoming**
  - `https://aem.careers.stage.hardrock.com/` — careers site in UAT; go-live planned for **2026-03-16**

**Discussion prompts**

- Which teams currently upload assets (central brand vs. property-level teams)?
- Which teams are expected to use the **careers** assets specifically (HR, TA, brand)?

------

### 1.2 DAM Folder Structure (under `/content/dam/shrss`)

**Top-level branches**

| Top-level folder | Typical usage (current)                     | Example paths                                           |
| ---------------- | ------------------------------------------- | ------------------------------------------------------- |
| `cafe`           | Cafe-specific assets per location           | `/content/dam/shrss/cafe/amsterdam/en/photography`      |
| `cf`             | Content fragments (locations, news, venues) | `/content/dam/shrss/cf/locations/europe/france`         |
| `corporate`      | Brand/corporate: logos, campaigns, careers  | `/content/dam/shrss/corporate/careers/en/photography`   |
| `hotel`          | Hotel-specific assets (global + properties) | `/content/dam/shrss/hotel/davos/en/photography/media`   |
| `reverb`         | Reverb brand assets                         | `/content/dam/shrss/reverb/atlanta/en/photography`      |
| `training`       | Training/sample content (CF + images)       | `/content/dam/shrss/training/cf/news/corporate/en/2025` |

> **Important:** `/content/dam/shrss/cf` holds **content fragments**, not traditional media assets. They are part of the **content model** and used heavily for locations and news.

**Notable patterns from folder outline and Excel**

- **Location-driven CF structure:**
  `/content/dam/shrss/cf/locations/<region>/<country>`
  Roughly mirrors the **country** and **properties** tag branches.
- **News CF structure:**
  `/content/dam/shrss/cf/news/corporate/en/<year>/<month>`
  Also mirrored under `/content/dam/shrss/training/cf/news/...` for demos.
- **Brand/site alignment:**
  - Cafe imagery: `/cafe/...`
  - Hotel imagery: `/hotel/...`
  - Reverb imagery: `/reverb/...`
  - Corporate/careers imagery: `/corporate/careers/en/...`

**Talking points**

- The top-level segmentation (`cafe`, `hotel`, `reverb`, `corporate`) maps cleanly to **site/brand**.
- `cf` and `training` are special: CF = structured content; training = safe sandbox.
- **Question:** Is anything “production-critical” currently stored under `training`? If yes, we should plan to move it.

------

### 1.3 How Folder Structure, Tags, and Metadata Work Together

**Conceptual model**

- **Folder**: primary grouping by **brand/site + location + language**
- **Tagging (`shrss` namespace)**: cross-cutting dimensions:
  - Brand / line of business (`lob`)
  - Property / venue / region
  - Content category (e.g., lifestyle, rooms, menus, philanthropy)
  - Campaign / news / events categories
- **Metadata schema (`shrssmetadataschema`)**: currently mostly **technical fields** (width, height, PDF title, video tech info) plus a basic **Location** field.

**Gap to call out**

- There are **few to no business fields** in the metadata schema (e.g., rights, usage, internal/external, campaign name).
- Today, **tags are carrying most of the business semantics**. That’s OK, but it means:
  - Tag governance is critical.
  - Future schema enhancements should align carefully with existing tag branches (no duplicate concepts in both places).

------

## 2. Tagging Strategy: `shrss` Namespace (15 min)

### 2.1 Overview of `shrss` Tag Tree

**Top-level branches (from tag outline)**

- `shrss/global` (currently not heavily populated)
- `shrss/hotel` (property/area-specific tags, including some quality issues)
- `shrss/casino`
- `shrss/cafe`
- `shrss/categories`
- `shrss/brands`
- `shrss/venues-and-branded-experiences`
- `shrss/regions`
- `shrss/lob` (line of business)
- `shrss/properties`
- `shrss/type` (corporate/franchise)
- `shrss/category` (imagery/content type, e.g., rooms, logo, lifestyle)
- `shrss/news-categories`
- `shrss/event-categories`
- `shrss/country`
- `shrss/products` (digital screens, email, mobile app, websites, booking…)

**Key ones for authors**

- **Brand / LOB:** `shrss/lob` (cafe, hotel, casino, entertainment, games, shop, sportsbook, unity, bet)
- **Property / Location:** `shrss/properties` (amsterdam, atlanta, davos, wroclaw, etc.)
- **Country:** `shrss/country` (france, germany, united-states, etc.)
- **Imagery category:** `shrss/category` (logo, lifestyle, rooms, suites, awards, philanthropy, etc.)
- **News / events:** `shrss/news-categories`, `shrss/event-categories`
- **Venues & branded experiences:** `shrss/venues-and-branded-experiences` (hard-rock-live, rock-spa, etc.)

------

### 2.2 Known Issues and Cleanup Areas

**Examples from current tag tree**

- **Typos / duplicates**
  - `guadalajara` vs `guadalaraja` under `hotel`
  - `northernindiana` vs `northern-indiana` under `properties`
  - `wroclaw` appears under **country** even though it’s a city
- **Encoded / awkward names**
  - `_x0032_4k-boutique`
  - `lobby-bar-gmt_x002b_1`
  - Tags with trailing hyphens (e.g., `unplugged-`, `velvet-sessions-`)
- **Overlapping concepts**
  - Some venues appear both under `venues-and-branded-experiences` and `properties`.

> **Decision to capture:**
> Which namespace(s) should be the **author-facing “golden path”** (e.g., always use `properties + category + lob`) and which ones are “expert-only”?

------

### 2.3 Recommended Tagging Patterns

**Pattern 1 – Cafe property hero image**

- **Folder**: `/content/dam/shrss/cafe/amsterdam/en/photography`
- **Tags:**
  - `shrss/lob/cafe`
  - `shrss/properties/amsterdam`
  - `shrss/country/netherlands`
  - `shrss/category/lifestyle` (or `exterior-shots`, `interior`, etc., as appropriate)

**Pattern 2 – Hotel room imagery**

- **Folder**: `/content/dam/shrss/hotel/en/photography` or `/hotel/davos/en/photography`
- **Tags:**
  - `shrss/lob/hotel`
  - `shrss/properties/davos` (or specific hotel)
  - `shrss/country/switzerland`
  - `shrss/category/rooms` or `suites`

**Pattern 3 – Corporate/careers headshot**

- **Folder**: `/content/dam/shrss/corporate/careers/en/photography`
- **Tags:**
  - `shrss/brands/hri` or `shr` (as appropriate)
  - `shrss/category/headshots`
  - `shrss/category/careers` (if used)
  - Optional: `shrss/products/websites` (if only used on careers site)

**Pattern 4 – News image (press release)**

- **Folder**: near corresponding CF, or `/corporate/photography`  
- **Tags:**
  - `shrss/news-categories/press-releases` or `hard-rock-news`
  - `shrss/lob/<relevant-lob>`
  - `shrss/properties/<property>` if property-specific
  - `shrss/category/awards` / `events` / `philanthropy` as appropriate

> For the session: walk through **two live assets** (one cafe, one corporate/careers) and show how tags drive **search** and **re-use**.

------

### 2.4 Tag Governance

**Current state (from prior analysis)**

- No explicit documented governance for:
  - Who can create new tags
  - Who can rename/disable tags
  - How to handle typos/duplicates without breaking references

**Proposed lightweight model**

- **DAM Architect (primary owner)**:
  - Approves new top-level branches and high-impact tags.
  - Maintains cleanup backlog (typos, merges, deprecations).
- **Author leads / brand managers**:
  - Request new tags via defined intake (JIRA/ServiceNow/email).
  - Validate the business meaning and re-use potential.
- **Rules of thumb:**
  - Prefer **re-using existing tags** over creating new ones.
  - New tags must specify: **where they’ll be used, who owns them, and if they’re temporary** (campaign-based).

> **Outcome for this session:** alignment on **who owns `shrss` taxonomy** and how authors request changes.

------

## 3. Metadata Schema: `shrssmetadataschema` (10–15 min)

### 3.1 Current Configuration (from `.content.xml`)

**Schema path**

- `JCR path: /conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`

**Asset types covered**

- `image` (base node)
- `image/jpeg`
- `image/tiff`
- `application/pdf`
- `video`

**Fields (summary)**

- **Image (generic image tab)**
  - `Width` (read-only; `tiff:ImageWidth`)
  - `Height` (read-only; `tiff:ImageLength`)
- **JPEG / TIFF**
  - `Location` (free-text; `Iptc4xmpExt:LocationShown`)
- **PDF**
  - `Pdf Title` (free-text; `pdf:Title`)
- **Video**
  - `Size` (`./jcr:content/metadata/size`)
  - `Duration (seconds)` (`videoDuration`)
  - `Total Bit Rate (kbps)` (`bitrate`)
  - `Video Codec` (`videoCodec`)
  - `Video Bit Rate (kbps)` (`videoBitrate`)
  - (All free-text fields; primarily technical.)

> There are currently **no dedicated business fields** such as `Usage rights`, `Internal/External`, `Campaign`, or `Content owner`.

------

### 3.2 How Authors See This in the UI

- When an author opens **Properties → Metadata** for:
  - An **image**, they see a **Basic** tab with Width/Height; JPEG/TIFF also show **Location**.
  - A **PDF**, they see **Pdf Title**.
  - A **video**, they see **Size, Duration, Bitrate, Codec** info.
- Most fields are either **read-only technical data** or **one-off free-text**.

**Implication**

- The **primary semantic classification** right now is **tags**, not form-based metadata.

- Business-critical information such as:

  - “Can I use this off-property?”
  - “Is this asset limited to a specific region or campaign?”

  …is **not captured in the schema** yet, and often not reliably in tags either.

------

### 3.3 Recommended Metadata Enhancements (for follow-up, not in this session)

For future rounds (requirements/discovery), propose adding:

- **Rights & usage**
  - `Usage rights` (controlled list: internal-only, paid media, organic social, etc.)
  - `Expiration date` (if legally required)
- **Business context**
  - `Content owner` (team or role)
  - `Primary brand` (align with `shrss/brands`)
  - `Primary product` (align with `shrss/products`)
- **Search helpers**
  - `Short description` (for authors, not public)

> **In session:** identify **2–3 fields** that would have the highest ROI if added to the schema and confirm these as **backlog candidates**.

------

## 4. DAM Operations & Governance (15 min)

### 4.1 Uploading, Versioning, and Asset Changes

**Current expectations (align in session)**

- **Where to upload**
  - Cafe imagery → `/cafe/<property>/en/photography`
  - Hotel imagery → `/hotel/<property>/en/photography`
  - Reverb imagery → `/reverb/<property>/en/photography`
  - Corporate/careers imagery → `/corporate/careers/en/...`
  - Training/demos → `/training/...` only
- **Versioning**
  - Use **asset versioning** when updating images currently used on live pages.
  - Avoid deleting assets that may still be referenced by Sites pages or Content Fragments.
- **Avoiding broken references**
  - Do **not** move or rename assets that are already referenced, without:
    - Running **Reference Search** first.
    - Updating references in Sites or CFs where possible.

**Discussion questions**

- How do authors currently learn if an asset is used on a page?
- Has SHRSS experienced broken images after DAM cleanup or moves?

------

### 4.2 Search & Findability

- **Current search experience**
  - Authors likely search by **free text** (filename/title) and maybe by **tags**.
  - Many assets might not be consistently tagged yet.
- **Best practices**
  - Always apply:
    - At least **one `lob` tag**
    - A **property** tag (when property-specific)
    - A **category** tag (logo, lifestyle, rooms, etc.)
  - For news/campaign content: use **news/event category** tags as well.

> For the session: demonstrate **a search scenario** (e.g., “Find hero images for Reverb Atlanta rooms”) and show how tags + folders work together.

------

### 4.3 Roles & Responsibilities

**Proposed roles**

- **DAM Architect (primary audience of this session)**
  - Owns folder conventions.
  - Owns `shrss` taxonomy and metadata schema roadmap.
  - Approves new top-level tags and schema changes.
- **Brand/Property author leads**
  - Train their teams on “golden path” folder + tag usage.
  - Request changes to tags/metadata.
- **Developers / AEM TAs**
  - Ensure Sites templates and components correctly use tags and metadata.
  - Support automation where possible (e.g., default tags by folder).

------

### 4.4 Dynamic Media (brief)

**Current state (from original agenda)**

- Dynamic Media is:
  - **Provisioned**, configured in lower environments.
  - **Not configured** in production.
  - Core components on Sites currently **do not use DM components**.

**Roadmap discussion (5 min)**

- Which content types would benefit most from DM?
  - Hero images? Carousels? Media-heavy experiences?
- What would need to change in DAM to adopt DM smoothly?
  - Clear separation of hero vs. raw imagery?
  - Consistent aspect-ratio tagging or naming?

> Outcome: capture whether DM is in scope for **next 6–12 months** and what prerequisites exist in DAM.

------

## 5. Decisions, Backlog, and Next Steps (5–10 min)

Use the last 10 minutes to capture **clear actions**:

### 5.1 Decisions to Capture

- **Folder governance**
  - Confirm top-level structure: `cafe`, `hotel`, `reverb`, `corporate`, `cf`, `training`.
  - Rules for new top-level folders (if any).
- **Tagging**
  - Agree on **minimum tagging standard** (e.g., `lob + property + category`).
  - Decide who **approves new tags** and how authors request them.
- **Metadata**
  - Identify **2–3 high-priority business fields** to add to the schema.
- **Dynamic Media**
  - Decide whether to pursue a **discovery/POC** in the next iteration.

### 5.2 Backlog Candidates (for Jira)

- **Tag cleanup**
  - Fix identified typos/duplicates/encoded names.
  - Deprecate or merge redundant branches.
- **Schema enhancement**
  - Add rights/usage + owner fields; map to clearly named properties.
- **Folder cleanup**
  - Move any production assets out of `/training`.
  - Normalize any ad-hoc substructures that don’t follow brand/site patterns.
- **Author enablement**
  - Publish an updated **Author Tagging and Metadata Quick Guide**.
  - Short video/walkthrough of “upload & tag correctly” for each main brand.

------

*End of comprehensive session guide.*
