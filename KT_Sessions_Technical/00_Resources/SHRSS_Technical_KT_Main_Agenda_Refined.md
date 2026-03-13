# Technical Knowledge Transfer Agenda (Refined)

**NOTE:** All topics are contextual to the current SHRSS implementation.

**Document:** Refined from strawman agenda. See *Refinement summary & recommendations* below.

**Exercises:** Suggested in-session and homework exercises are in the supplemental:  
`Technical_KT_Session_Content/00_Resources/SHRSS_Technical_KT_Exercises_Supplemental.md`  
(organized by session/topic/subtopic; includes steps and repo file paths.)

**Authoring KT cross-reference:** Where it adds context, this technical KT will reference the **authoring KT** sessions—especially questions, comments, or conversations involving **Gonzalo Calasich**, **Taranjeet Loh (TJ)**, and **Tim Willis**, who are primary participants in the technical sessions. Consolidated authoring transcripts: `KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md`

---

## Refinement summary & recommendations

The following changes were made to better align the agenda with the **target audience** (SHRSS developers, system administrators, QA, technical managers taking ownership of the platform) and with the **current SHRSS implementation** (per implementation analysis and solution design):

1. **Session mapping to 5 × 2h blocks**  
   Content is organized to match the desired split: Session 1–2 (Intro + App Dev Parts 1–2), Session 3–4 (App Dev Parts 3–6), Session 5 (Change/Release + DevOps Part 1), Session 6 (DevOps Part 2 + Conclusion). This keeps a clear narrative and balances depth vs. time.

2. **Additions**
   - **Security & hardening:** Callout for servlet authentication, secrets management, and removal of test/debug endpoints in production (aligned to implementation analysis P0 findings). Placed in App Dev (backend) and again in DevOps (IAM/permissions).
   - **Idempotency:** Explicit topic under AEMaaCS development considerations (schedulers, listeners, workflows, repo init) so SHRSS understands cloud-safe patterns before maintaining or extending code.
   - **SHRSS external integrations:** Dedicated sub-blocks for **Workday** (jobs sync), **DPLT** (locations/venues), **GraphQL** (persistent queries, headless), and any **third-party frontend** integrations (e.g. OpenTable, Grubhub, Google Maps) so teams know where they live in the repo and how they are configured.
   - **Content Fragments & GraphQL:** CF models, persistent queries, and consumption in components—needed for Careers and for future property migrations.
   - **Testing:** Unit (JUnit), integration (AEM testing client), and UI (Cypress) in one place, with a short note on Cloud Manager pipeline steps and coverage expectations.
   - **RDE and Preview:** Rapid Development Environment and Preview tier mentioned explicitly under Cloud Manager so admins know when to use them.

3. **Order**
   - Overview and Cloud ecosystem first (Admin Console → Cloud Manager) so everyone has the same mental model.
   - Code structure and tooling before deep backend/frontend so developers can follow along in the repo.
   - Backend (run modes, OSGi, integrations) before Dispatcher/CDN so request flow and security (e.g. servlet auth) are clear before discussing cache and filters.
   - Change/Release and DevOps in the last two sessions so the “how we build and deploy” story is consolidated after “what we have.”

4. **Participant exercises**  
   Multiple suggested exercises (in-session and as homework) are listed in the **exercise supplemental** document, organized by session/topic/subtopic. These include the IAM → native AEM group walk-through, repo navigation (e.g. locate a Sling Model for a component), Cloud Manager, and testing. Complete as time permits; the supplemental can also be shared with participants as suggested homework.

5. **Topic scope**  
   All added topics (security, idempotency, integrations, CF/GraphQL, testing) are retained. The next subtask will timebox topics/subtopics; pruning will be done after that exercise as needed.

6. **References**  
   Implementation analysis (`00_EXEC_SUMMARY.md`, `01_STRUCTURAL_ARCHITECTURE.md`, `02_CROSS_LAYER_INTERACTIONS.md`), SDD, and implementation notes are the primary references for SHRSS-specific detail; AEM canonical references in `docs/ai/reference` for best practices.

---

## Presenters

- **Andy Lambert** — Principal Technical Architect, Adobe  
  - AEMaaCS application and cloud service paradigms, DevOps, best practices

- **Vinay S A** — AEM Technical Architect, Adobe  
  - SHRSS implementation details, backend code, configurations, AEM authoring components

- **Deepkamal Narang** — Senior Technical Consultant, Adobe  
  - Frontend code, UX implementation, AEM authoring components

---

## Session 1 & 2 — Introduction/overview, AEM Application Development Parts 1 & 2 (2 hours)

### Overview (Andy)

- Cloud services ecosystem (Admin Console → Cloud Manager)
- AEMaaCS architecture (high level)
- AEMaaCS Cloud Manager paradigms (environments, pipelines, repos)

### AEM Application Development — Part 1

- **Development tooling / IDEs (Andy / Vinay)**  
  - Local dev setup, IDE configuration, connecting to dev/author

- **Code structure (Andy / Vinay)**  
  - Maven/POM configuration and dependency management  
  - Main modules: `core`, `ui.apps`, `ui.frontend`, `ui.content`, `ui.config`, `dispatcher`, `it.tests`, `ui.tests`, `all`, `acl`, `config`  
  - Other configs: CDN rules, maintenance tasks, log forwarding (per implementation notes)

- **AEM authoring components (Andy → Vinay)**  
  - Core Components and extending (e.g. hrccard)  
  - Dialogs  
  - Clientlibs (definition, categories, file/folder structure)  
  - Sling Models (Use-API, extending, debugging)  
  - Best practices (structure, clientlib categories)  
  - *Exercise:* See supplemental — “Locate the Sling Model for a component (hrccard)”

---

## Session 3 & 4 — AEM Application Development Parts 3 & 4 (2 hours)

### AEM Application Development — Part 2 (continued)

- **Backend (Andy → Vinay)**  
  - Run modes, environment variables and secrets  
  - Repo initialization  
  - OSGi component implementations (servlets, Sling models, services, listeners, schedulers — as implemented in SHRSS)  
  - OSGi configurations (`ui.config`)  
  - **Security & hardening:** Servlet authentication, avoiding test/debug endpoints in production, secrets management (aligned to implementation analysis findings)  
  - Debugging/troubleshooting  
  - Best practices  

- **Frontend (Deep)**  
  - Client libraries (clientlibs)  
  - Webpack, NPM, build and deploy into `ui.apps`  
  - Debugging/troubleshooting  
  - Best practices  

- **External integrations (Vinay)**  
  - **Workday** (jobs sync) — where it lives, how it’s invoked, configuration  
  - **DPLT** (locations/venues) — data flow and usage in components  
  - **GraphQL** — persistent queries, headless consumption, SHRSS usage  
  - Other third-party (e.g. OpenTable, Grubhub, Google Maps) as applicable  
  - Where to find integration code and configs in the repo  

- **Content Fragments & GraphQL (Vinay / Andy)**  
  - CF models in SHRSS (e.g. jobs, events, locations, venues)  
  - Persistent queries and consumption in components  
  - Relevance for Careers and future migrations  

---

## Session 5 — AEM Application Development Parts 5 & 6, Change and Release Management, DevOps Part 1 (2 hours)

### AEM Application Development — Part 3 (continued)

- **Dispatcher / CDN (Andy → Vinay)**  
  - Cloud-optimized Apache and Dispatcher configs  
  - Caching and security (filter rules, blocking unauthenticated servlet access where required)  
  - CDN configuration (BYOCDN rules in `config` module if applicable)  
  - Reference to implementation analysis Dispatcher/CDN findings where relevant  

- **General AEM troubleshooting / debugging (Andy / Vinay)**  
  - Cache issues (distribution queues, logs via distribution console)  
  - Unhandled exceptions / 500s (AEM logs)  
  - Developer Console (Experience League reference)  

- **Development considerations for AEMaaCS (Andy)**  
  - **Idempotency** — why it matters (horizontal scaling, restarts, retries); patterns for schedulers, listeners, workflows, repo init  
  - Distributed, Mongo-based repository  
  - Best practices  

### Change and Release Management (Andy)

- Source control management  
- Aligning code changes to Jira  
- Git branching strategy  
- Cutting a release and production deployment  

### DevOps — Part 1 (Andy)

- **User / group / permission management (Admin Console IAM → native AEM groups)**  
  - Walk-through (participant exercise):  
    1. Create IAM group in Admin Console (https://adminconsole.adobe.com/)  
    2. Add IAM user with DEV author profile to IAM group  
    3. User logs into DEV author  
    4. Add IAM group to native AEM group in AEM  
    5. View user and IAM group memberships in console  
- How this maps to SHRSS roles and environments  

- **Cloud Manager**  
  - Environments: Dev, QA, Integration, Stage, Prod  
  - Rapid Development Environments (RDE)  
  - Preview tier  
  - Run modes, environment variables and secrets  
  - Repositories  
  - Build pipelines  
  - Environment whitelists  
  - Content restore and bulk content copy  

---

## Session 6 — DevOps Part 2, Conclusion / Q&A / Customer topics (2 hours)

### DevOps — Part 2 (Andy)

- Pipelines deep dive (build, quality, security, deployment)  
- Logs and monitoring (Cloud Manager, AEM logs)  
- Troubleshooting failed pipelines and deployments  

### Testing (Andy / Vinay)

- **Unit tests** — JUnit, coverage in `core` (models, services, servlets, etc.)  
- **Integration tests** — AEM testing client, `it.tests` module, Cloud Manager custom functional testing step  
- **UI tests** — Cypress, `ui.tests` module, Cloud Manager custom UI testing step  
- Where tests run in the pipeline and how to run locally  

### Conclusion / Q&A / Customer topics

- Open Q&A  
- SHRSS-prioritized topics (e.g. specific integrations, security remediation, or migration prep)  
- Next steps and follow-up  

---

## References (for presenters and materials)

- Implementation analysis: `Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`  
  - `00_EXEC_SUMMARY.md`, `01_STRUCTURAL_ARCHITECTURE.md`, `02_CROSS_LAYER_INTERACTIONS.md`, `03_SOLUTION_DESIGN_TRUE_UP.md`, `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md`, `05_INDEX_AND_NAVIGATION.md`
- Solution design: `Technical_KT_Session_Content/00_Resources/SHRSS_Optimized_SDD.md`
- Implementation notes: `Technical_KT_Session_Content/00_Resources/SHRSS_AEM_Implementation_Notes.md`
- AEM canonical references: `docs/ai/reference/AEM_CANONICAL_REFERENCES.md`, `docs/ai/reference/AdobeDocs-global-mapping.csv`
- Source code (reference only; no changes): per AGENTS.md, repo path as specified in task document
