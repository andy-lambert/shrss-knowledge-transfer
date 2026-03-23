# AEMaaCS DAM Architect & Librarian Best Practices

*DAM Architects, Librarians, Asset Stewards – SHRSS Volume*

------

## 1. Role & Responsibilities

As DAM architect/librarian for SHRSS you:

- Own the **structure, governance, and metadata** of Assets and Content Fragments.
- Ensure the repository scales and remains **searchable, consistent, and legally compliant**.
- Partner with authors and engineering to support reliable **Jobs/Events/News/Locations** experiences.

Use the **Consolidated All‑Roles Volume** for shared platform concepts.

------

## 2. Information Architecture (IA) for Assets & CFs

### 2.1 Folder Design Principles

- Design for:
  - **Findability** (how humans search).
  - **Scalability** (tens/hundreds of thousands of assets).
  - **Permission boundaries** (who should access what).
- Keep **CFs and media separate**:
  - CFs under structured trees (e.g., `Content Fragments` by domain).
  - Media (images, videos, docs) under `Media` or domain‑specific subfolders.

**References**

- [Assets as a Cloud Service documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/home)

### 2.2 SHRSS Overlay – Folder IA

- Typical structure:
  - `Assets > Files > SHRSS > Content Fragments > Jobs/Events/News/Locations/...`
  - `Assets > Files > SHRSS > Media > ...`
- For Jobs:
  - Use region/country/property folders so recruiters and authors can quickly find relevant jobs.
- For Events:
  - Group by brand or property, depending on how events are used.
- For News:
  - Group by brand/property or central editorial; keep cross‑brand content in shared locations.

------

## 3. Content Fragments as Structured Data

### 3.1 CF Model Governance

- Keep CF model changes **versioned and documented**:
  - Changing field names or types affects queries, index rules, and front‑end.
- Avoid frequent field model changes once live:
  - Add new optional fields instead of repurposing existing ones.

**References**

- [Content Fragment Models](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-fragments/content-fragments-models)

### 3.2 SHRSS Overlay – CF Domains

- **Jobs CF model**
  - Fields split into:
    - Workday/system fields (IDs, URLs, location).
    - Author-only fields (image, hot flag, overrides).
  - DAM governance:
    - Document which fields are overwritten by sync vs controlled by authors.
- **Events CF model**
  - Emphasis on:
    - Date/time, status, location reference.
    - Promotional media fields.
- **News CF model**
  - Metadata fields (publish date, category, hero image) drive lists and cards.
- **Location CF model**
  - Mirrors DPLT structure; do not modify core fields without alignment with integration owners.

------

## 4. Metadata & Taxonomy

### 4.1 Metadata Schemas

- Use **metadata schemas** for:
  - Asset types (images, videos, docs).
  - Domain-specific needs (e.g., Job imagery, Event hero images).
- Enforce:
  - Required fields (license, rights, expiry).
  - Controlled vocabularies via dropdowns tied to tag trees.

**References**

- [Managing Metadata for Assets](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/metadata)

### 4.2 Tags & Taxonomy

- Design tag hierarchies around:
  - **Business concepts**: brand, property, department, event type.
  - **Cross-domain reuse**: tags that unify Jobs/Events/News/Locations.

### 4.3 SHRSS Overlay – Tags

- Ensure there is a **single source of truth** for:
  - Job categories and departments → align with Workday.
  - Properties and locations → align with DPLT.
  - News categories and event types → align with marketing taxonomy.
- Anti-pattern:
  - Ad‑hoc tags like `“new-event-2025”` created only for one use; prefer using start/end dates, status, or existing categories.

------

## 5. Lifecycle & Governance

### 5.1 Asset Lifecycle

- Define policies for:
  - **Retention**: how long to keep assets and CFs.
  - **Archival**: where to move expired materials.
  - **Deletion**: when to safely delete unused assets.

### 5.2 SHRSS Overlay – Jobs/Events/News Lifecycle

- Jobs:
  - Workday may expire jobs; ensure CFs are either archived or clearly marked as expired.
  - Don’t manually delete active jobs; coordinate with Workday owners.
- Events:
  - Past events:
    - Archive CFs or tag as “past” based on business rules.
- News:
  - For compliance or brand tracking, keep historical news CFs and pages but ensure old news is clearly dated.

------

## 6. Supporting Performance & Indexing

### 6.1 Repository Hygiene

- Avoid:
  - Huge “flat” folders (e.g., thousands of CFs under a single node).
  - Excessive nesting (folders 12+ levels deep).
- Design folder hierarchies that:
  - Keep **node counts per folder moderate**.
  - Map to query constraints (e.g., Jobs per region/country/property).

### 6.2 SHRSS Overlay – Index-Friendly Design

- For Jobs:
  - Regions/country/property folders support:
    - Path constraints for region‑specific queries.
    - Better index density and smaller result sets.
- For Events & News:
  - Consider grouping by **year** or **month** to avoid unbounded lists in a single folder.

------

## 7. Collaboration with Authors & Engineering

- Provide **DAM usage guides**:
  - Where to upload images.
  - Required metadata before publishing.
- Work with engineering to:
  - Ensure new search/list components have supporting metadata and tags.
- Work with authors to:
  - Clean up legacy content when IA or taxonomies change.

------

## 8. DAM SHRSS Overlay Summary

For SHRSS DAM roles:

- Treat CFs as **structured data** with strong governance over models.
- Align tags and metadata with **Workday and DPLT** taxonomies.
- Support performance by designing folder structures and lifecycles that keep the repository clean and index‑friendly.

Use alongside:

- The **Consolidated All‑Roles Volume**.
- The **Author Volume** (to ensure authoring patterns align with IA).
- The **Indexing & Performance Volume** (for how DAM choices influence query/index behavior).