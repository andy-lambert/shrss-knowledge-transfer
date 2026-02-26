# Session Notes — Jobs — 2026-02-10

**Session:** Jobs  
**Date:** February 10, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260210_130301-Meeting Recording  
**Duration:** 1h 53m 23s  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context and agenda

- Lucas Nelson opened with logistics and confirmed that a **gap analysis phase** will follow the KT sessions (final week of the seven-week schedule) to capture gaps and noted functionality for the backlog.
- Daniela Tea led the session focused on **job-related components** and the **Jobs content fragment** (Workday-driven). Careers site is in QA and intended to go live next month.
- Questions are to be captured on the session-specific Confluence page; Adobe will answer in Confluence or allocate time at the start of future sessions.

---

## What was covered

1. **Jobs content fragment (CF)**  
   - Location: Assets → SHRSS → content fragments → jobs. Folder structure: country → state → location/property → job CFs. All job data synced from Workday; authors do not create job posts. Empty folders remain when jobs are removed in Workday. Stage is connected to Workday QA API (smaller subset); production will have full set.
   - Fields: Job ID, Job Unique ID (both from Workday; **Job ID** currently displayed to user—noted as wrong; ticket exists), Image (author-only; not overwritten by sync), Hot job toggle, LD JSON (author-only). Remaining fields (job title, job portal URL, category, type, address, job property, etc.) are Workday-sourced and overwritten on sync.
   - Author can create a manual job via Create → Content Fragment → Jobs; no dropdowns for category—must match exact value (e.g. casino sales). Workday jobs publish automatically on sync; manual jobs can use schedule.
   - **Override vs sync:** Only Workday fields are overwritten. Image, Is Hot Job, and LD JSON are author-only and persist.

2. **Job Search component**  
   - Maps CF fields to results (job ID, image, title, job portal URL, updated date, category, job type, address, job property). Sort options: most recent (default), job title, location; hot jobs always on top. Filters: categories, properties, job types, locations (from CF country/state/city). Configuration: labels, results per page, etc. Mobile: “Refine your search” opens filters; apply filters button.
   - **Open items:** Deep links (filters in URL for shareable links); Tealium data layer / unique IDs per card for analytics; sync on-demand and production sync frequency/duration; error message when sync fails (vs “no jobs found”); logo image specs.

3. **Job Listings component**  
   - Two modes: All jobs vs Hot jobs. Root path: single folder selection (e.g. Florida or Orlando)—**one only**, not multiple properties. Layout: 1–4 columns; max job cards. Apply Now button text configurable; link from CF. Default image for cards without CF image. **Gaps:** No multi-property selection; no centering when fewer than column count (e.g. 1 or 2 cards); hot jobs with no results shows title but blank (no message/hide).

4. **Job Filters component**  
   - Homepage careers filter: search page path configurable (author must set); labels for job categories, properties, job types, locations. Request: default search page so authors don’t have to set every time.

5. **Job Category Cards**  
   - Categories and counts from CFs; link to job search page. Sort: by number of jobs or alphabetical. **Gap:** Cannot pick/choose which categories to show (e.g. only casino sales and housekeeping).

6. **Job Image configuration (ACS AEM Commons → Content Packagers → image config)**  
   - Job Images: list of job property name + image. Match by CF “job property” value. New jobs from Workday get image when property matches. Pre-existing jobs (before config) do not auto-inherit. **Concern:** 500+ locations; list in config is incomplete; manual mapping; if Workday changes property name, new config entry needed. Source of full location list to be confirmed (Lucas/Vinay; Scott/IT).

7. **Hot jobs page / Hiring events**  
   - Hot jobs page uses same Job Listings component (hot jobs); one toggle in CF drives both homepage and hot jobs page. Filtering on hot jobs page is a known gap (JIRA). Hiring events use a **different content fragment** (Events session).

8. **Shared content / queries**  
   - Get in the Game–style cards (casinos, cafes, etc.): currently per-page; Experience Fragment approach would allow single update. **Additional need:** Logic to exclude current page (e.g. on Casinos page, don’t show Casinos card). To be revisited (shared data / experience fragments).

---

## Questions, comments, and answers (captured)

*See the “SHRSS Adobe KT Session Follow-Up Tracker” workbook, **Jobs** sheet, for the full list of questions/comments, who asked, answers when provided, and status. Summary below.*

- **Job ID vs Job Unique ID:** Wrong ID displayed; ticket with dev team.
- **Image override:** Replaces image in both job listings and job search horizontal cards. Request: hot jobs use property image, listings use logo; different treatment for same job in different contexts—gap.
- **Sync override:** Only Workday fields overwritten; image, hot job, LD JSON safe.
- **Logo image dimensions:** Not yet specified; used existing Sage/DAM assets.
- **Immediate hide job:** No current way to hide a single job without Workday; Daniela to check if turning off “is API data” could freeze sync (follow-up).
- **Select locations / new property:** From CF (country, state, city); new Workday property auto-creates structure; author does not add.
- **Image reference if asset moved:** Should update; if deleted, breaks. To confirm.
- **Sort/sequence:** Configurable (most recent, job title, location); hot jobs always top.
- **Tealium / unique IDs per card:** To confirm with tech team.
- **Sync on-demand and production frequency/duration:** To check.
- **Deep links:** Filters not in URL; need shareable deep links (friendly, not opaque params). To discuss with tech team.
- **Error message when sync fails:** Separate from “no jobs found”; gap for gap analysis.
- **Template for careers pages:** Open page template.
- **Conditional filters:** Yes; selecting one filter updates options in others.
- **Multiple properties in Job Listings:** Only one root path; cannot select Coco + Classic + Hollywood together; workaround = multiple components; no sort across. Gap.
- **Center fewer cards:** Not available; gap.
- **Hot jobs with no results:** Section shows title, no cards, no message; request hide or message—gap.
- **Job Filters search page:** Request default to single careers search page.
- **Job Category Cards:** Cannot choose which categories to show—gap.
- **Job image config:** Job property = value from CF; must match exactly. Full location list and ownership of mapping to be confirmed (Vinay; IT).
- **Workday property name change:** Requires new config entry with new name + image.
- **Hot jobs page filtering:** Not in component; JIRA gap.
- **Hiring events:** Different CF; Events session. Card consistency (width/height vs hot jobs) noted as gap.
- **Shared cards / exclusion logic:** Experience Fragment gives reuse; excluding “current” page (e.g. Casinos) needs logic—gap.
- **Reschedule/take down jobs:** Workday is source; AEM-side option to take down/reschedule to be confirmed with tech team.
- **Job filter labels (four labels):** Joseph could not find in config; Daniela to confirm (possibly in markup).
- **Image specs and who fixes before go-live:** No spec sheet yet; Daniela to discuss with Vinay.
- **Pagination / max jobs per page:** No Adobe performance testing; SHRSS to follow up with TJ/Mohsin.

---

## Product Director (SHRSS) — own questions and points of clarification

*Captured in persona as primary notetaker and advocate for authors, content owners, and DAM; amalgamating concerns similar to Mayte Eme and Lisa Cardia; emphasis on authoring, governance, and gap analysis.*

1. **Governance — job image configuration:** Who owns the ongoing maintenance of the job property–to–image mapping (Adobe, IT, or SHRSS content)? What process do we have for adding new properties or changing Workday property names so the mapping stays in sync and authors are not left with broken or missing images?
2. **Authoring — consistency across job-related components:** We now have multiple job components (search, listings, filters, category cards) with different behaviors (e.g. one root path vs multiple, default image in listings but not in search). Can we get a short authoring checklist or decision tree (e.g. “when to use which component,” “what authors can safely edit vs what sync overwrites”) so our team can work confidently without relying on memory?
3. **Tagging / metadata:** For jobs, the only author-controlled “tagging” we heard today is the Hot Job toggle and the image. Are there other metadata or tags authors can set on job CFs that affect display or filtering, and who governs allowed values (e.g. categories) when they come from Workday vs author-created jobs?
4. **Gap analysis — priorities for careers go-live:** Given go-live next month, which of today’s gaps are in scope for remediation before launch (e.g. job ID fix, deep links, hot jobs empty state, image specs) and which are explicitly deferred to post–gap analysis? We need a clear list so we can set author and stakeholder expectations.
5. **Permissions/roles:** Who in AEM can access the Job Image configuration (ACS AEM Commons → Content Packagers)? Is it admin-only or can we assign a “careers content owner” or DAM role to maintain the property–image list without full admin access?

---

## Final thoughts and follow-ups

- Session was dense and aligned with careers timeline pressure. Many questions intentionally parked for “tomorrow” (next session) or gap analysis.
- **Action for Adobe:** Follow-ups promised on job ID ticket, hide job / “is API data,” image reference on move, Tealium/unique IDs, sync on-demand and frequency, deep links, filter labels (Joseph), image specs and Vinay, and full location list (Vinay / IT).
- **Action for SHRSS:** Add questions to Confluence; Scott/IT to pursue full location list; performance/pagination with TJ/Mohsin; track consistency between hot jobs and hiring events cards for gap analysis.
- **Recurring theme:** Need for a single source of truth (Workday) while supporting author overrides (image, hot job) and edge cases (immediate hide, reschedule) without breaking sync. Governance of config (image mapping, categories) and clarity on roles will be important for long-term ownership.

---

*End of session notes. All Q&A rows are recorded in the **Jobs** sheet of `SHRSS_Adobe_KT_Session_Follow_Up_Tracker.xlsx`.*
