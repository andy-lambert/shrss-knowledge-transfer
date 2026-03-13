# Recommendations: Enhance Technical KT Agenda and Content

**Purpose:** Ideas to augment the existing technical KT session agenda, detailed content, and exercise supplemental so the sessions are as useful as possible for SHRSS technical stakeholders (developers, system administrators, QA, technical managers) taking ownership of the platform.

**Status:** Recommendations only; integrate as the team sees fit. Timeboxed agenda may need minor adjustments if new items are adopted.

---

## 1. JCR / Exported Content Structure Walk-Through (Your idea — placement and scope)

**Idea:** Walk through the structure of site content exported from the JCR so stakeholders can “read” a content package and relate it to pages, components, and code.

**Suggested placement:** **Session 1 & 2**, immediately after **Code structure** and before or as a short bridge into **AEM authoring components**. Rationale: once they know the repo modules, showing where *content* lives (exported JCR) and how it maps to *templates* and *component resource types* sets up the authoring-components section (hrccard, Sling Models, dialogs). Alternative: a dedicated 10–15 min block in **Session 3 & 4** right before or after **Content Fragments & GraphQL**, to tie page content structure to CF-backed components (e.g. joblistings, promotionsearch).

**Recommended scope and flow:**

1. **Content package and path**  
   - Stage content (Careers):  
     `Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/shrss/corporate/careers`  
   - Production content:  
     `Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/shrss`  
   - Explain: FileVault export = JCR as XML (`.content.xml` per node). One folder per page/asset; children = child pages or component nodes under `jcr:content`.

2. **Site hierarchy (Careers example)**  
   - **Root page** `careers`: `jcr:primaryType="cq:Page"`, `jcr:content` with `cq:template="/conf/shrss/settings/wcm/templates/page-content"`, `sling:resourceType="shrss/components/structure/page"`.  
   - **Language root** `en`: `cq:isLanguageRoot="true"`, `sling:sitemapRoot="true"`, template `page-home`; list child pages (home, jobs, hot-jobs, kt-careers, locations, benefits, etc.).  
   - **Concrete page** (e.g. `en/kt-careers` or `en/home`): same pattern — `jcr:content` holds template, page-level props (e.g. `mainClientLib`, `subClientLib`, `hfragmentVariationPath`), and the **component tree** under `root` → `maincontainer` → `container` → … (hero, breadcrumb, joblistings, promotionsearch, etc.).

3. **Component tree → code**  
   - For one page (e.g. `en/kt-careers/.content.xml`): point out `root` (container) → nested containers → `joblistings` with `sling:resourceType="shrss/components/joblistings"` and authored props (`rootFolder="/content/dam/shrss/cf/jobs"`, `jobsType="hotJobs"`, `maxJobCards="8"`).  
   - Same for `promotionsearch`: `cfBasePath`, `displayType`, etc.  
   - Message: “This node is the resource your Sling Model and HTL render; these properties are what the dialog wrote. When you debug, you’re often looking at this resource and its path.”

4. **Templates and policies**  
   - `cq:template` points to `/conf/shrss/settings/wcm/templates/...` (page-content, page-home, page-open, etc.). Templates define allowed components and structure; policies (in conf) map to policy IDs in the package. Reference: onboarding scratch notes — `conf/shrss/settings/wcm/templates/` and policies.

5. **Optional one-liner**  
   - “Author creates the page in UI; export gives you this XML. When you need to script content, migrate, or debug why a component doesn’t get the right props, you’ll look at this structure.”

**Deliverable suggestion:** Add a short subsection to **Session_1_and_2_Detailed_Content.md** (and optionally Session_3_and_4 for CF-heavy pages) and, if time allows, one slide or a 5–10 min live walk-through of `careers` → `en` → `en/kt-careers` (or `en/home`) in an editor. Add an exercise to the supplemental: “Open Careers `en/kt-careers/.content.xml`, find the joblistings node, and in the repo locate the component and Sling Model that use `rootFolder`.”

---

## 2. One-Page “Where do I find…?” Quick Reference

**Idea:** A single-page cheat sheet for “where do I find X?” (code, config, content, logs, pipelines).

**Content (examples):**  
- Repo modules and what each contains (core, ui.apps, ui.frontend, ui.content, ui.config, dispatcher, it.tests, ui.tests, config).  
- Key paths: components, clientlibs, OSGi configs, persistent queries, Dispatcher, Jobs/GraphQL services.  
- Cloud: Admin Console (IAM), Cloud Manager (program, envs, pipelines, logs).  
- Content packages: PROD vs STAGE paths; Careers under `content/shrss/corporate/careers`.  
- Implementation analysis: where the final docs live and how to use 00_EXEC_SUMMARY, 01_STRUCTURAL, 04_QUALITY.

**Placement:** Create as `Technical_KT_Session_Content/00_Resources/SHRSS_Technical_KT_Quick_Reference.md` (or similar). Hand out at start of Session 1 or after Session 2; refer to it in every session.

---

## 3. Troubleshooting Decision Tree / Runbook Skeleton

**Idea:** A short, practical “when something goes wrong” guide: pipeline failed, page 500, content not updating, cache stale, “where do I look?”.

**Suggested content:**  
- Pipeline failed → Build vs Quality vs Security vs Deploy vs Custom Test; where logs are; “run same Maven locally” for build.  
- 500 on a page → AEM logs, Developer Console; component/resource type and Sling Model; common causes (NPE, missing config, resolver leak).  
- Content not updating on publish → Replication/distribution queue; Dispatcher invalidation; browser cache.  
- One table: symptom → likely layer → next step (with pointers to agenda sessions and implementation analysis issues where relevant, e.g. servlet auth, Dispatcher filter).

**Placement:** New doc under `Technical_KT_Session_Content/` (e.g. `SHRSS_Technical_KT_Troubleshooting_Runbook.md`). Referenced in Session 5 (troubleshooting) and Session 6 (Conclusion). Can be expanded over time into a living runbook.

---

## 4. Security & P0 Remediation Tracker (Lightweight)

**Idea:** A single table or short doc that lists the 14 P0 items from implementation analysis (and optionally top P1) with “what to do” and “where in code/config” so technical owners can prioritize and track.

**Content:**  
- Rows: Issue ID (e.g. ISSUE-BACKEND-019), short title (e.g. “Servlet auth – DeleteJob, JobsCFUpdate, InvalidateCache, UserDashboard”), location (servlet name, Dispatcher filter), recommended action, reference (04_IMPLEMENTATION_QUALITY_ASSESSMENT.md, Optimized SDD Appendix C).  
- Same for hardcoded creds, test servlets, CDN purge key, GraphQL syntax, Dispatcher P0, testing P0s.

**Placement:** New file in `Technical_KT_Session_Content/` (e.g. `SHRSS_Technical_KT_P0_Remediation_Tracker.md`). Session 3 & 4 (Security & hardening) and Session 6 (SHRSS-prioritized topics) can point to it; managers can use it for backlog alignment.

---

## 5. Glossary and Acronyms

**Idea:** One-page glossary: AEMaaCS, Author/Publish, Dispatcher, CDN, BYOCDN, Sling, JCR, resource type, Sling Model, clientlib, OSGi, run mode, RDE, pipeline, IAM, etc. SHRSS-specific: DPLT, Workday, Careers, mainClientLib/subClientLib, page-content vs page-open vs page-home.

**Placement:** `Technical_KT_Session_Content/00_Resources/SHRSS_Technical_KT_Glossary.md`. Link from main agenda and from Session 1 overview so new-to-AEM participants can use it during and after the sessions.

---

## 6. “Day in the Life” Flows (Optional Narrative)

**Idea:** Short, scenario-based narratives: “Developer adds a new component,” “Author publishes a Careers page,” “Pipeline runs and deploys to Stage,” “Support gets a 500 — what do they do?”. Not a replacement for the agenda, but a bridge for technical managers and support: “this is how it all fits together.”

**Placement:** Optional add-on doc or a few slides; could live under `Technical_KT_Session_Content/` or `00_Resources/`. Reference in Session 1 (overview) or Session 6 (Conclusion).

---

## 7. Pre-Session Read-Ahead / Homework List

**Idea:** Curated list of “read or skim before Day 1” and “before each session” so participants come prepared and time is used for discussion and exercises.

**Suggested items:**  
- Before Day 1: Task doc (target audience, presenters, 5×2h structure); main agenda (high-level); optional: 00_EXEC_SUMMARY (first 2 pages).  
- Before Session 3 & 4: Exercise 1.2 (clone repo), 1.3 (hrccard), 1.4 (clientlib); implementation notes (module list).  
- Before Session 5: Exercise 2.1, 2.2 (jobs, GraphQL); Dispatcher section of implementation analysis or index.  
- Before Session 6: Exercise 3.1, 3.2 (IAM, Cloud Manager); testing section of exec summary.

**Placement:** New file `SHRSS_Technical_KT_Read_Ahead.md` in `Technical_KT_Session_Content/`; send with calendar invite or Session 1 deck.

---

## 8. One End-to-End Integration Deep-Dive (Optional)

**Idea:** Pick one integration (e.g. Jobs: Workday → backend → CF → persistent query → joblistings component → page) and walk it from “trigger” to “rendered page” in 15–20 min. Helps developers and QA see the full chain.

**Placement:** Session 3 & 4, either as part of External integrations + Content Fragments & GraphQL or as a single “Jobs end-to-end” block. Could be optional (time-permitting) or replace a portion of the current integrations breakdown.

---

## 9. Link Agenda and Session Docs to Implementation Analysis

**Idea:** In the main agenda and each session detailed-content file, add explicit “Reference” lines that point to specific sections of the implementation analysis (e.g. “Security: 04_IMPLEMENTATION_QUALITY_ASSESSMENT.md §Critical Findings”; “Dispatcher: 01_STRUCTURAL_ARCHITECTURE.md §3”). Some of this exists already; make it consistent so presenters and participants can jump to the right doc.

**Placement:** Edits to `SHRSS_Technical_KT_Main_Agenda.md` and `Session_*_Detailed_Content.md`; no new file.

---

## 10. Optional “Content Package 101” (If JCR Walk-Through Expands)

**Idea:** If the JCR/content structure walk-through is well received, consider a short “Content package 101”: what’s in the PROD vs STAGE package (pages, XFs, CFs, conf, tags), how filter roots work, and how to relate a content package to what authors see in author. Complements the Careers page-structure walk-through.

**Placement:** Same session as the JCR walk-through (Session 1 & 2 or 3 & 4), or a 5 min recap at the start of Session 3 & 4.

---

## Summary Table

| # | Recommendation | New asset? | Suggested session(s) | Effort |
|---|----------------|------------|----------------------|--------|
| 1 | JCR / exported content structure walk-through (Careers) | Add to session content + optional exercise | 1&2 (after Code structure) or 3&4 (with CF) | Medium |
| 2 | One-page “Where do I find…?” quick reference | New: Quick_Reference.md | All (handout Session 1) | Low |
| 3 | Troubleshooting decision tree / runbook skeleton | New: Troubleshooting_Runbook.md | 5, 6 | Medium |
| 4 | P0 remediation tracker | New: P0_Remediation_Tracker.md | 3&4, 6 | Low |
| 5 | Glossary and acronyms | New: Glossary.md | 1, all | Low |
| 6 | “Day in the life” flows (optional) | New optional doc/slides | 1 or 6 | Medium |
| 7 | Pre-session read-ahead / homework list | New: Read_Ahead.md | Pre-session | Low |
| 8 | One end-to-end integration deep-dive (e.g. Jobs) | Optional block in session content | 3&4 | Medium |
| 9 | Explicit links from agenda/session docs to impl analysis | Edits to existing docs | All | Low |
| 10 | Optional “Content package 101” | Optional add to session content | 1&2 or 3&4 | Low |

---

**Paths used in this document**

- Careers (stage) content:  
  `Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/shrss/corporate/careers`
- Production content:  
  `Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/shrss`
- Implementation analysis:  
  `Implementation_Analysis_Project/Documentation/Implementation-Analysis/final/`
- Session content:  
  `Technical_KT_Session_Content/Session_*_Detailed_Content.md`
- Exercise supplemental:  
  `Technical_KT_Session_Content/SHRSS_Technical_KT_Exercises_Supplemental.md`
