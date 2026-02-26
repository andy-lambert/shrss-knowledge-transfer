# Scratch Notes

> ## Purpose
>
> Agent note keeper and archiver for this project.  
> Use to log, track, and make actionable the spontaneous thoughts, creative/design ideas, potential new tasks, etc. that come up during the course of an agent's work session.
>
> ## Instructions for Use (REQUIRED)
>
> - ALWAYS prefix the note with a timestamp (date and time in ISO 8601 format; e.g. `2026-01-06T10:46:00Z` and local equivalent)
> - ALWAYS populate the **Category** field from the following options:
>   - Idea
>   - New Task
>   - Other
>   - Reminder
> - ALWAYS populate the **Context** field. Concise bulleted list. What precipitated the note? What step/activity in the current task?
> - ALWAYS populate the **Description** field. Be as detailed as is required to accurately and completely capture the thought
> - ALWAYS populate **Note Status** from the following actions:
>   - Pending Action
>   - Resolved
> - When **Note Status** is **Pending Action**, the **Required Action** field is ALWAYS required.
> - When **Note Status** is **Resolved**, the **Resolution** field is ALWAYS required
>
> ### Template (REQUIRED)
>
> ```md
> - **Timestamp (UTC):** 2026-01-06T10:46:00Z
> - **Timestamp (Local):** 2026-01-06T05:46:00-05:00
> - **Timezone (IANA):** America/New_York
> 
> - **Category:**
> 
> - **Context:**
> 
> - **Description:**:
> 
> - **Note Status:**:
> 
> - **Required Action:**
> 
> - **Resolution:**
> 
> ---
> ```
>
---

## KT Preparation Onboarding (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T12:00:00Z (session)
- **Category:** Reminder
- **Context:** SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md steps 3–4 completed; scratch notes updated so future agents can proceed without re-running full onboarding.
- **Description:**
  - **Implementation architecture (step 3):** Authoritative analysis lives at `/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`. Start with `00_EXEC_SUMMARY.md` then `01_STRUCTURAL_ARCHITECTURE.md`–`05_INDEX_AND_NAVIGATION.md`. Summary: SHRSS AEMaaCS implementation — 3 sites, ~500GB DAM; 313+ structural elements (backend 203, UI 101, Dispatcher/CDN, Testing); 83 cross-layer interactions; 97 quality issues (14 P0); quality grade C+. Critical: Unity backend not implemented (iframe only); 5 pre–Phase 2 blockers (test servlets, hardcoded creds, servlet auth, GraphQL syntax, CDN purge key). Staging details: `staging/backend/`, `staging/ui/`, `staging/dispatcher/`, `staging/testing/`.
  - **Content package (step 4):** Path `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`. FileVault package roots: `/conf`, `/content/cq:tags/shrss`, `/content/dam/shrss/corporate/logos`, `/content/dam/shrss/cf`, `/content/experience-fragments/shrss`, `/content/shrss`. **Templates/policies:** `conf/shrss/settings/wcm/templates/` — page-content, page-news, page-event, page-messi, page-news-search, config-page, microsite-page, blank-page, xf-shrss-variation, news-home-page, page-open; each has structure/initial/policies; policies map components to policy IDs (e.g. `shrss/components/container/policy_*`). **Asset metadata schema:** `conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema/.content.xml` — custom DAM metadata form (Basic tab: Upload Details, Metadata fields dc:title, description, etc.). **Tagging:** Package filter includes `/content/cq:tags/shrss`; assets use tags (e.g. `properties:orientation/square`). **Content sampled:** DAM logos with standard + Smart Crop/AI metadata; Content Fragments under `content/dam/shrss/cf` (venue model: guestRooms, area, shortDescription, meetingRooms, etc.; news CFs by path); GraphQL persistent queries under `conf/shrss/settings/graphql/persistentQueries/`.
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Onboarding completed; agent ready to proceed with additional KT tasks per user direction.

---

## Session Handoff & Next Session (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T12:00:00Z
- **Category:** Reminder
- **Context:** User reported that the **Tagging, Taxonomy & Metadata Governance** KT session was delivered successfully; asset metadata/tag examples and CF Card List page examples were well received and complimented. Next session to prep: **DAM Training and Usage Guide for Admins**.
- **Description:**
  - **Accomplished this session:** Tagging/Taxonomy KT content (session guide, proposed content, content–tag mapping, Asset Metadata Fields doc, CF_Card_List_Page_Examples_KT_Reference.md) was used to host the session; delivery went really well.
  - **Next:** Prepare for **DAM Training and Usage Guide for Admins** using:
    - **Agenda:** `DAM/AAEMDAM-3736_DAM_Training_and_Usage_Guide_for_Admins_Agenda.pdf`
    - **Jira:** `DAM/AAEMDAM-3736_DAM_Training_and_Usage_Guide_for_Admins_Agenda_JIRA.docx` (ticket AAEMDAM-3736)
  - **Jira summary (from DOCX):** Parent AEM Enablement; Status To Do; Priority Show Stopper; Assignee Jenny Yang. **Audience:** Librarian, Content Admins, Product Owner have DAM access; **Content Authors do not.** Goal: enablement so Admins can manage assets, maintain governance, support property teams without misuse or disorganization. **Learning goals:** DAM structure (based on spreadsheet), upload/version/manage assets, where to store assets (hierarchy), how metadata and folders work, Dynamic Media in publishing, avoid breaking references, how asset updates flow to live pages. Training required before DAM becomes part of daily operations. Affects R1.0/R7.0; Fix versions R2.0–R7.1.
- **Note Status:** Resolved
- **Resolution:** Scratch notes updated; next agent can use agenda + Jira + this handoff to continue DAM Training for Admins prep.

---

## DAM Training and Usage Guide for Admins — Content & Approach Notes (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T12:00:00Z
- **Category:** Idea
- **Context:** Prep for next KT session per agenda PDF and Jira AAEMDAM-3736. Audience: Admins (Librarian, Content Admins, Product Owner); not Content Authors.
- **Description:**

  **Objective (from agenda):** Understand how to properly use the DAM so admins can manage assets, maintain governance, and support property teams without risking misuse or disorganization.

  **Thoughts by agenda section:**

  1. **DAM Content Architecture**
     - **Content:** How the DAM is structured; how and where to store assets in the correct hierarchy; best practices; architecture realignment roadmap (shrss → shrss-primary).
     - **Approach:** Ground “structure” in the actual content package and implementation: `/content/dam` (e.g. `content/dam/shrss/corporate/logos`, `content/dam/shrss/cf`). Jira says structure is “based on spreadsheet”—**confirm/locate that spreadsheet** (folder hierarchy, naming, placement rules) and use it as the single source of truth for “where to store.” Clarify **shrss → shrss-primary**: is this a rename, a migration, or a new root? Not clearly present in implementation analysis final docs; get client/roadmap input so the realignment slide is accurate and non-speculative.
     - **Deliverable idea:** One-page “DAM folder map” or hierarchy diagram + short best-practices list (naming, no orphan assets, use of folders vs. tags).

  2. **Assets Metadata**
     - **Content:** Metadata schemas; folder metadata schemas; metadata profiles; best practices.
     - **Approach:** Reuse and point to existing KT artifacts: **Tagging session** and **Asset_Metadata_Fields_Tag_Selection.md** (and Asset Metadata Fields doc) already document `shrssmetadataschema`, tag roots, and fields. This section can focus on: (a) where schemas live (`/conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`), (b) folder-level metadata schemas if used in this implementation, (c) metadata profiles (e.g. processing/renditions) if applicable. Keep “best practices” concrete (e.g. required fields, tag consistency) and aligned with governance from the Tagging session.
     - **Deliverable idea:** Short “Metadata for Admins” cheat sheet: schema overview + link to Tagging/metadata docs; folder metadata and profiles if present.

  3. **DAM Operations**
     - **Content:** How to upload, version, and manage assets; how to avoid breaking references; how asset updates flow to live pages; best practices.
     - **Approach:** This is highly procedural and UI/UX. Cover: upload flows, versioning (AEM versioning behavior), when updates propagate (references, Sites usage, publish). “Avoid breaking references” is critical: document or demonstrate what breaks references (move/rename/delete), and safe patterns (replace binary, use versioning). Implementation analysis mentions AssetService and JCR at `/content/dam`; no need to go deep technically for Admins—focus on authoring behavior and outcomes. If there are workflows or scheduling in use, describe them from an admin perspective.
     - **Deliverable idea:** Step-by-step “Safe asset update” and “Do not do” one-pagers; optional short demo script (replace vs. delete, version before major change).

  4. **Dynamic Media**
     - **Content:** Current state; integration roadmap.
     - **Approach:** Keep factual: what is enabled today (e.g. Smart Crop, renditions) vs. not (e.g. DM Scene7/Hybrid). Implementation analysis and content package show Smart Crop/AI-style metadata on assets—that’s “current state” evidence. Roadmap is client/PM territory; document only what is confirmed (e.g. “Integration roadmap to be shared by product/project”) so the session doesn’t over-promise.
     - **Deliverable idea:** One slide/section “Dynamic Media today” (what works now) + “Planned” (roadmap TBD or high-level only).

  **Cross-cutting:** All content must stay **analysis/documentation only** (no code or config changes). Align any “best practice” or “how it works” claims to implementation analysis and content package evidence, and to AEM canonical refs where useful (see AGENTS.md and docs/ai/reference).

- **Note Status:** Pending Action
- **Required Action:** When building session materials: (1) Locate/confirm DAM structure spreadsheet and shrss-primary roadmap; (2) Reuse Tagging/metadata docs for Assets Metadata section; (3) Add DAM Operations procedural/cheat-sheet content; (4) Confirm Dynamic Media current state and roadmap ownership with client/PM.
- **Resolution:** (N/A)

---

## Task 3 — Scrub asset nodes from DAM content package (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T14:00:00Z
- **Category:** New Task
- **Context:** DAM KT session prep; user requested concise DAM structure reference + content package that creates prod folder structure with no assets. Task 3 in SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md.
- **Description:**
  - **Steps 1–2 completed:** Analyzed working folder `Content/dam-shrss-folder-structure-1.0/jcr_root/content/dam/shrss`; found all directories whose immediate `.content.xml` has `jcr:primaryType="dam:Asset"`. Created Excel inventory at **`DAM/AAEMDAM-3736_Asset_Nodes_To_Remove_Inventory.xlsx`** with columns **Path (JCR)** and **Type (jcr:primaryType)**. **Total asset node directories: 4,670** (all type `dam:Asset`). User approved; removal executed.
  - **Scrub completed:** Removed all 4,670 asset directories from the package filesystem. Verification: zero `dam:Asset` nodes remain under `jcr_root/content/dam/shrss`; **275** `.content.xml` files remain (folder nodes and `folderThumbnail.dir` nodes only). Package now contains only the empty folder hierarchy plus folder metadata. **Note:** `folderThumbnail.dir` nodes may still reference deleted asset paths in `dam:folderThumbnailPaths`; AEM may show no thumbnail or regenerate on use—no change made to those nodes per task spec.
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Task 3 scrub complete. Package at `Content/dam-shrss-folder-structure-1.0` is ready for repackaging (zip) and install to create empty DAM folder structure. No META-INF/filter changes were required for this content-only scrub.

---

## Task 4 — CF Card List usage inventory (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T15:00:00Z
- **Category:** New Task
- **Context:** Task 4 in SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md; deliverable artifact for customer (no KT session language).
- **Description:**
  - **Completed:** Full mapping of CF Card List component to page usage. **Scope:** PROD = `/content/shrss/corporate` (excl. careers) + `/content/shrss/reverb`; STAGE = `/content/shrss/corporate/careers` only. Experience fragments scanned; **no EFs** in either package contain `shrss/components/cfcardlist`. **Deliverables** in `Tagging_and_Taxonomy/`: (1) **CF_Card_List_Usage_Inventory.md** — inventory by site (Corporate Hard Rock, Reverb, Careers) with tables: Type, Path, Site/Context, Instance, CF Card List Config, Notes; (2) **CF_Card_List_Usage_Inventory.xlsx** — same columns. **8 rows** (one per component instance): blog (1), home (1), corporate (1), cf-card-list-page (2), event-list-reverb (1), knowledge-transfer (1), kt-other (1). Detection by `sling:resourceType="shrss/components/cfcardlist"` in page `.content.xml`; config extracted from element attributes. Script used: `Content/task4_cfcardlist_inventory.py` (reusable for regen).
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Task 4 complete; customer-facing inventory ready.

---

## Task 5 — Consolidate and rename tagging structure package files (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T16:00:00Z
- **Category:** New Task
- **Context:** Task 5 in SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md.
- **Description:**
  - **Completed:** Created a single `.content.xml` representing the entire SHRSS tagging structure. **Source:** `DAM/00_Drafts_and_Resources/tag_working_directory/_cq_tags/shrss`. **Target:** `DAM/00_Drafts_and_Resources/tag_working_directory/shrss_tag_structure_definition_files/.content.xml`. Root file copied to target, then each placeholder element (e.g. `<brands/>`, `<country/>`) recursively expanded with the inner content (children of `<jcr:root>`) from the matching subdirectory’s `.content.xml`. Empty nodes (e.g. `global`) left unchanged. Script: `tag_working_directory/consolidate_tag_structure.py` (reusable for regen).
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Task 5 complete; one consolidated tag structure definition file in target directory.

---

## Task 6 — SHRSS DAM structure markdown and Excel (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T17:00:00Z
- **Category:** New Task
- **Context:** Task 6 in SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md; use scrubbed package from Task 3.
- **Description:**
  - **Completed:** Created markdown document and Excel spreadsheet of current SHRSS DAM architecture. **Source:** `Content/dam-shrss-folder-structure-1.0` (Task 3 scrubbed package). **Deliverables in** `DAM/`: (1) **SHRSS_DAM_Structure_Outline.md** — folder structure in outline form with summary table of top-level branches (cafe, cf, corporate, hotel, reverb, training) and full hierarchy; (2) **SHRSS_DAM_Structure.xlsx** — sheet "Asset Folders" with columns JCR Path, Folder Name, Depth, Parent Path (237 rows). Script: `DAM/build_dam_structure_docs.py`.
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Task 6 complete.

---

## Session close — handoff for next session (2026-02-18)

- **Timestamp (UTC):** 2026-02-18T12:00:00Z
- **Category:** Reminder
- **Context:** User closing out this session; requested last notes before starting a new one.
- **Description:**
  - **This session accomplished:** (1) **Task 3** — Scrubbed 4,670 asset nodes from `Content/dam-shrss-folder-structure-1.0`; inventory in `DAM/AAEMDAM-3736_Asset_Nodes_To_Remove_Inventory.xlsx`. (2) **DAM agenda** — Converted `AAEMDAM-3736_DAM_Training_and_Usage_Guide_for_Admins_Agenda.pdf` to markdown in `DAM/`. (3) **Task 4** — Full CF Card List usage inventory: `Tagging_and_Taxonomy/CF_Card_List_Usage_Inventory.md` and `.xlsx` (8 instances; PROD corporate/reverb, STAGE careers). (4) **Task 5** — Consolidated SHRSS tag structure into single `.content.xml` and outline in `DAM/00_Drafts_and_Resources/tag_working_directory/shrss_tag_structure_definition_files/`. (5) **Metadata schema** — Consolidated `shrssmetadataschema` and child nodes into `DAM/00_Drafts_and_Resources/metadata_schema/.content.xml` and `shrss_metadata_schema_structure.md` (with config details). (6) **Task 6** — SHRSS DAM structure in outline form and Excel: `DAM/SHRSS_DAM_Structure_Outline.md`, `DAM/SHRSS_DAM_Structure.xlsx`. (7) **FluffyJaws PDFs** — Markdown versions of all 5 PDFs in `DAM/00_Drafts_and_Resources/00_FluffyJaws_Final/` (conversion is best-effort; PDFs are slide decks so extracted content is fragmentary).
  - **For next session:** DAM Training and Usage Guide for Admins (AAEMDAM-3736) prep is the next KT focus. Agenda and approach notes are in this scratch file (see "DAM Training and Usage Guide for Admins — Content & Approach Notes"). Key artifacts to reuse: DAM structure outline/Excel, metadata schema docs, Tagging/metadata docs, scrubbed folder-structure package. **Pending:** Confirm DAM structure spreadsheet and shrss-primary roadmap with client; decide whether to remove folder thumbnail nodes from scrubbed package after deploy test.
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Session handoff captured; next agent can continue from AGENTS.md, this file, and SHRSS_Knowledge_Transfer_Preparation_Agent_Tasks.md.

---

## KT Session Participation Task — Historical Context & Future Rounds (2026-02-17)

- **Timestamp (UTC):** 2026-02-17T18:00:00Z
- **Timestamp (Local):** 2026-02-17T13:00:00-05:00
- **Category:** Reminder
- **Context:** User requested documentation of the “Participate in KT sessions as SHRSS stakeholder” task for historical tracking and for future agents executing the same task in subsequent session rounds (additional sessions coming up).
- **Description:**

  ### Task summary (what was done)

  - **Source:** `Task_Participate_in_KT_Sessions_as_SHRSS_Stakeholder.md` (repo root).
  - **Persona:** SHRSS Product Director / senior author; blend of Mayte Eme and Lisa Cardia; focus on authoring components, tagging, governance, gap analysis. Must capture every question, answer, and SHRSS comment; add 3–5 “Product Director” persona questions per session.
  - **For each session:** (1) One **session notes** markdown file in `KT_Session_Question_Analysis/`; (2) Rows added to the corresponding sheet in the Excel follow-up tracker.
  - **Completed sessions (first round):** Jobs (2026-02-10), Events (2026-02-11), Careers (2026-02-12), Tagging & Taxonomy (2026-02-17), DAM (2026-02-18), Shared Data (2026-02-19), News (2026-02-20), Locations (2026-02-23). All have session notes MD + tracker rows.
  - **Workbook column order (current):** Reordered per user request to: **Status** | **Date Asked** | **Answered On** | **Answered By** | **Asked By** | **Question/Comment** | **Answer** | **Notes**. Script: `KT_Session_Question_Analysis/reorder_tracker_columns.py`. All add-row scripts use this order when appending (via reorder constant).

  ### Paths and artifacts

  | Item | Path |
  |------|------|
  | Transcript (consolidated) | `KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md` |
  | Output directory | `KT_Session_Question_Analysis/` |
  | Workbook | `KT_Session_Question_Analysis/SHRSS_Adobe_KT_Session_Follow_Up_Tracker.xlsx` |
  | Session notes naming | `Session_Notes_<Topic>_<YYYY-MM-DD>.md` (e.g. `Session_Notes_Jobs_2026-02-10.md`) |
  | Column reorder script | `KT_Session_Question_Analysis/reorder_tracker_columns.py` |
  | Add-row scripts | `add_jobs_tracker_rows.py`, `add_events_tracker_rows.py`, `add_careers_tracker_rows.py`, `add_remaining_tracker_rows.py` (Tagging, DAM, Shared_Data, News, Locations) |

  ### Sheet name ↔ session mapping (extend for new sessions)

  | Session (transcript heading / topic) | Sheet name |
  |-------------------------------------|------------|
  | Session: Jobs — 2026-02-10 | Jobs |
  | Session: Events — 2026-02-11 | Events |
  | Session: Careers — 2026-02-12 | Careers |
  | Session: Tagging & Taxonomy — 2026-02-17 | Tagging_Taxonomy_Metadata_Gov |
  | Session: DAM — 2026-02-18 | DAM_Training_Usage_Admin |
  | Session: Shared Data — 2026-02-19 | Shared_Data |
  | Session: News — 2026-02-20 | News |
  | Session: Locations — 2026-02-23 | Locations |
  | *(Locations continue / new)* | Locations *(or new sheet if split)* |
  | *Media* | *TBD — add sheet when transcript available* |
  | *Navigation and Data Displays* | *TBD* |
  | *Page Templates* | *TBD* |

  ### Workflow for each new session (steps for future agents)

  1. **Transcript:** Locate the session block in `SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md` (session date and title at top of block).
  2. **Session notes MD:** Create `Session_Notes_<Topic>_<date>.md`. Capture: summary, key points, every Q&A (who asked, who answered, answer text), SHRSS comments, follow-ups. Add 3–5 **Product Director** questions (governance, authoring, tagging, gap analysis, permissions) even if not in transcript.
  3. **Tracker rows:** Add one row per question/comment. Columns (in order): Status, Date Asked, Answered On, Answered By, Asked By, Question/Comment, Answer, Notes. Use session date for Date Asked / Answered On; “Product Director” for persona questions. Status: **Pending** | **Answered** | **Deferred** (use Deferred when item is explicitly deferred to gap/later phase). Capture answers from **any** participant (SHRSS or Adobe).
  4. **Excel:** Either (a) add a new sheet to the workbook if it’s a new session type and append rows (openpyxl), or (b) append rows to existing sheet (e.g. Locations continue → Locations). Reuse pattern from `add_remaining_tracker_rows.py`: tuple order in script = (Question/Comment, Date Asked, Asked By, Answer, Answered On, Answered By, Status, Notes); reorder with `NEW_COL_ORDER = (7, 2, 5, 6, 3, 1, 4, 8)` when writing so workbook columns stay Status, Date Asked, Answered On, Answered By, Asked By, Question/Comment, Answer, Notes.
  5. **Optional:** After first new session in a round, pause for user review of notes + tracker sample before proceeding through remaining new sessions.

  ### Getting the most out of sessions (exercises & analysis)

  - **Pre-session:** Skim implementation analysis (e.g. `Implementation_Analysis_Project/.../final`) and any session-specific prep (e.g. DAM structure, Tagging docs) so Product Director questions are grounded in real gaps and governance needs.
  - **During “attendance”:** Note timestamps or speaker cues for follow-ups (e.g. “Daniela to get back”) and tag them as Pending; note any “we’ll add to gap list” or “defer to platform expansion” as Deferred.
  - **Post-session:** Cross-check session notes against tracker rows so no Q is dropped; add Product Director questions that tie to authoring, tagging, governance, or gap prioritization even if not asked live.
  - **Analysis reports:** If producing summaries (e.g. “Topics for gap analysis,” “Open Pending by session”), derive from the tracker workbook and session notes; keep one source of truth (workbook) for follow-up status.

  ### Recommendations for future agents (subsequent rounds)

  - **Do not** copy/paste prior-session questions from earlier runs; adopt the persona and treat each transcript as live attendance (per task).
  - **Do** reuse conventions: same column order, same Status values, same session-notes filename pattern, same Product Director question style (governance, authoring, tagging, gap, permissions).
  - **New sheets:** If a new session type gets its own sheet, add the sheet to the workbook (same 8 columns), then append rows; update this scratch-note table and any mapping in the task doc if the user maintains it.
  - **Locations continue:** If “Locations (continue from today)” is the same topic, append to the existing **Locations** sheet with the new session date where applicable; no new sheet unless user asks.
  - **Scripts:** Prefer one add-row script per session (or one script per “batch” of new sessions) and keep the `NEW_COL_ORDER` reorder so new rows match the current workbook layout. Running `reorder_tracker_columns.py` again will not harm existing data (idempotent reorder).

  ### Upcoming sessions (as of 2026-02-17)

  | Session | Notes |
  |---------|--------|
  | **Locations** | Continue from today — append to existing Locations sheet/session notes or new MD as appropriate |
  | **Media** | New; add sheet when transcript/session date available; same workflow |
  | **Navigation and Data Displays** | New; add sheet when transcript/session date available |
  | **Page Templates** | New; add sheet when transcript/session date available |

  When transcripts for Media, Navigation and Data Displays, and Page Templates are available: create session notes MD, add or reuse workbook sheet, append tracker rows in the column order above, add Product Director questions, then update this table with sheet names and dates.

- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Documented for historical tracking and for future agents executing the task for Locations (continue), Media, Navigation and Data Displays, and Page Templates. Re-read this section and `Task_Participate_in_KT_Sessions_as_SHRSS_Stakeholder.md` at start of each new round.

---

## Tasks since last scratch update (2026-02-26)

- **Timestamp (UTC):** 2026-02-26T16:00:00Z
- **Timestamp (Local):** 2026-02-26T11:00:00-05:00
- **Category:** Reminder
- **Context:** User requested scratch notes update before starting “Analyze Customer KT Questions” task; capture work completed since last update (Subtask 1, participant list).
- **Description:**
  - **Subtask 1 (Participate in KT sessions — new transcripts):** (1) Created markdown from Word transcripts for **Locations, Day 2** (2026-02-24) and **Media** (2026-02-25), excluding images (`strip_images_from_md.py`). (2) Appended both to `KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md` with section headings. (3) Created new workbook sheets **Locations_Day_2** and **Media** in `SHRSS_Adobe_KT_Session_Follow_Up_Tracker.xlsx`; added session notes MD and tracker rows for both. (4) Updated `Task_Participate_in_KT_Sessions_as_SHRSS_Stakeholder.md` session/sheet table. Scripts: `append_to_consolidated.py`, `add_locations_day2_and_media_tracker_rows.py`.
  - **Column reorder (earlier):** Workbook columns reordered to Status, Date Asked, Answered On, Answered By, Asked By, Question/Comment, Answer, Notes. All add-row scripts use `NEW_COL_ORDER` when appending.
  - **Participant list:** User requested distinct participants from consolidated transcript. Delivered alphabetical list of 18 distinct participants (Adobe + SHRSS); noted “Speaker 1” (unidentified, DAM session only).
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Scratch notes updated; next task is Analyze Customer KT Questions (flag likely AI-generated questions in `SHRSS_KT_Session_Questions.xlsx`).

---

## Task: Analyze Customer KT Questions — AI-generated flagging (2026-02-26)

- **Timestamp (UTC):** 2026-02-26T16:30:00Z
- **Category:** New Task
- **Context:** Task from `Task_Analyze_Customer_Knowledge_Transfer_Questions_Cursor_20260226.docx`; 543 questions in `SHRSS_KT_Session_Questions.xlsx` sheet `All_SHRSS_KT_Questions` to be analyzed for likely AI-generation.
- **Description:**
  - **Done:** Script `analyze_ai_generated_questions.py` loads the consolidated transcript by session, scores each question using task criteria (formal/AI phrasing, technical AEM terms, reworded transcript snippet, length, conversational cues), and writes **AI-Generated** (TRUE/FALSE), **Confidence** (1–100%), and **Reasoning** to the workbook.
  - **Result:** 542 rows updated. ~232 TRUE (likely AI-generated), ~310 FALSE. Distribution by session varies (e.g. News 4 questions → 1 TRUE; Tagging 36 → 29 TRUE). Reasoning field summarizes which signals applied (e.g. “technical/AEM terms”, “formal/AI phrasing”, “question appears to rephrase a transcript snippet”, “conversational phrasing (human-like)”).
- **Note Status:** Resolved
- **Required Action:** (N/A)
- **Resolution:** Workbook saved. Analysis is heuristic-based; user can tune thresholds/patterns in the script and re-run to refresh.

---
