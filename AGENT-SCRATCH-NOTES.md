# Scratch Notes

> Agent note keeper and archiver for this project.  
> Use to log, track, and make actionable the spontaneous thoughts, creative/design ideas, potential new tasks, etc. that come up during the course of an agent's work session.

---

## KT Preparation Onboarding (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T (session)
- **Category:** Reminder
- **Context:** SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md steps 3–4 completed; scratch notes updated so future agents can proceed without re-running full onboarding.
- **Description:**
  - **Implementation architecture (step 3):** Authoritative analysis lives at `/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`. Start with `00_EXEC_SUMMARY.md` then `01_STRUCTURAL_ARCHITECTURE.md`–`05_INDEX_AND_NAVIGATION.md`. Summary: SHRSS AEMaaCS implementation — 3 sites, ~500GB DAM; 313+ structural elements (backend 203, UI 101, Dispatcher/CDN, Testing); 83 cross-layer interactions; 97 quality issues (14 P0); quality grade C+. Critical: Unity backend not implemented (iframe only); 5 pre–Phase 2 blockers (test servlets, hardcoded creds, servlet auth, GraphQL syntax, CDN purge key). Staging details: `staging/backend/`, `staging/ui/`, `staging/dispatcher/`, `staging/testing/`.
  - **Content package (step 4):** Path `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`. FileVault package roots: `/conf`, `/content/cq:tags/shrss`, `/content/dam/shrss/corporate/logos`, `/content/dam/shrss/cf`, `/content/experience-fragments/shrss`, `/content/shrss`. **Templates/policies:** `conf/shrss/settings/wcm/templates/` — page-content, page-news, page-event, page-messi, page-news-search, config-page, microsite-page, blank-page, xf-shrss-variation, news-home-page, page-open; each has structure/initial/policies; policies map components to policy IDs (e.g. `shrss/components/container/policy_*`). **Asset metadata schema:** `conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema/.content.xml` — custom DAM metadata form (Basic tab: Upload Details, Metadata fields dc:title, description, etc.). **Tagging:** Package filter includes `/content/cq:tags/shrss`; assets use tags (e.g. `properties:orientation/square`). **Content sampled:** DAM logos with standard + Smart Crop/AI metadata; Content Fragments under `content/dam/shrss/cf` (venue model: guestRooms, area, shortDescription, meetingRooms, etc.; news CFs by path); GraphQL persistent queries under `conf/shrss/settings/graphql/persistentQueries/`.
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Onboarding completed; agent ready to proceed with additional KT tasks per user direction.

---

## Instructions for Use (REQUIRED)

- ALWAYS prefix the note with a timestamp (date and time in ISO 8601 format; e.g. `2026-01-06T10:46:00Z` and local equivalent)
- ALWAYS populate the **Category** field from the following options:
  - Idea
  - New Task
  - Other
  - Reminder
- ALWAYS populate the **Context** field. Concise bulleted list. What precipitated the note? What step/activity in the current task?
- ALWAYS populate the **Description** field. Be as detailed as is required to accurately and completely capture the thought
- ALWAYS populate **Note Status** from the following actions:
  - Pending Action
  - Resolved
- When **Note Status** is **Pending Action**, the **Required Action** field is ALWAYS required.
- When **Note Status** is **Resolved**, the **Resolution** field is ALWAYS required

### Template (REQUIRED)

```md
- **Timestamp (UTC):** 2026-01-06T10:46:00Z
- **Timestamp (Local):** 2026-01-06T05:46:00-05:00
- **Timezone (IANA):** America/New_York

- **Category:**

- **Context:**

- **Description:**:

- **Note Status:**:

- **Required Action:**

- **Resolution:**

---
```

---
