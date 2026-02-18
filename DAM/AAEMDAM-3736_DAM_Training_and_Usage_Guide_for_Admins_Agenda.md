# DAM Training & Usage Guide for Admins

**Ticket:** AAEMDAM-3736 — Enablement | DAM Training & Usage Guide for Admins

---

## Objective

Understand how to properly use the DAM so admins can manage assets, maintain governance, and support property teams without risking misuse or disorganization.

---

## Review and discuss

- DAM content architecture
- Assets metadata
- Admin/authoring processes (versioning, scheduling, workflows, etc.)
- Dynamic Media

---

## 1. DAM Content Architecture

### Current state: How the DAM is structured

- How and where to store assets in the correct hierarchy

### Optimal state: Discuss optimal structure, adoption strategy/roadmap

1. Possible approach for handling legacy/migrated assets while: also adopting new structure, optimizing for Dynamic Media
   1. Create `migrated-assets` folder:
      1. A-Z subfolders
         1. Move assets by name
      2. 0-9 subfolders
         1. Move assets by number
      3. Create nested folders as needed for < 1000 max per folder requirement (A-01, A-02).
         1. MAYBE nested subfolders based on asset type here
   
   2. Export Excel report of all assets in `<parent folder> -> photography`
      - In report spreadsheet, map assets to new home under `migrated-assets`
   
   3. Use ["Renovator"](https://adobe-consulting-services.github.io/acs-aem-commons/features/mcp-tools/renovator/index.html) tool or equivalent to move migrated assets in bulk to `migrated-assets`. Tool will locate and update all corrresponding asset references in pages, etc. https://adobe-consulting-services.github.io/acs-aem-commons/features/mcp-tools/renovator/index.html
   
      > [!CAUTION]
      >
      > Before executing on a large number of assets, or in production, execute on a small, targeted set of assets in a lower environment and perform regression testing.
      >
      > 1. Example: Subset of assets referenced in a specific set of test pages, experience fragments, and content fragments
   
   4. Define new, optimized folder structure
      1. Already done via `shrss-primary` structure?
   
   5. Require all new assets to be placed in new structure

- Considerations for Dynamic Media

- Best practices

> [!TIP]
>
> When defining DAM structure, adhere to the maxim that asset folder names are for structure and governance, not search. Search for assets by metadata and tags.

---

## 2. Assets Metadata

- Metadata schemas
- Folder metadata schemas
- Metadata profiles
- Best practices

---

## 3. DAM Operations

- How to upload, version, and manage assets
- How to avoid breaking references
- How asset updates flow to live pages
- Best practices

---

## 4. Dynamic Media

- Current state
  - Provisioned
  - Configured in lower environments
  - Not configured in production
  - Sites pages and experience fragments do not currently use Dynamic Media components

- Integration/Adoption roadmap

---

*Working agenda draft for KT session. Source: AAEMDAM-3736_DAM_Training_and_Usage_Guide_for_Admins_Agenda.pdf*
