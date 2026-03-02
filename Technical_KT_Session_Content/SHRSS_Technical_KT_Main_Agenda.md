# Technical Knowledge Transfer Agenda

## Session 1 & 2 — Introduction/overview, AEM Application Development Parts 1 & 2 (2 hours)

### Overview (Andy) — 25 min

- Cloud services ecosystem (Admin Console → Cloud Manager) — 8 min
- AEMaaCS architecture (high level) — 7 min
- AEMaaCS Cloud Manager paradigms (environments, pipelines, repos) — 10 min

### AEM Application Development — Part 1 — 95 min

- **Development tooling / IDEs (Andy / Vinay)** — 12 min  
  - Local dev setup, IDE configuration, connecting to dev/author

- **Code structure (Andy / Vinay)** — 25 min  
  - Maven/POM configuration and dependency management  
  - Main modules: `core`, `ui.apps`, `ui.frontend`, `ui.content`, `ui.config`, `dispatcher`, `it.tests`, `ui.tests`, `all`, `acl`, `config`  
  - Other configs: CDN rules, maintenance tasks, log forwarding (per implementation notes)

- **AEM authoring components (Andy → Vinay)** — 58 min  
  - Core Components and extending (e.g. hrccard) — 10 min  
  - Dialogs — 8 min  
  - Clientlibs (definition, categories, file/folder structure) — 12 min  
  - Sling Models (Use-API, extending, debugging) — 15 min  
  - Best practices (structure, clientlib categories) — 8 min  
  - *Exercise:* See supplemental — “Locate the Sling Model for a component (hrccard)” — 5 min  

---

## Session 3 & 4 — AEM Application Development Parts 3 & 4 (2 hours)

### AEM Application Development — Part 2 (continued) — 117 min

- **Backend (Andy → Vinay)** — 38 min  
  - Run modes, environment variables and secrets — 5 min  
  - Repo initialization — 5 min  
  - OSGi component implementations (servlets, Sling models, services, listeners, schedulers — as implemented in SHRSS) — 12 min  
  - OSGi configurations (`ui.config`) — 5 min  
  - **Security & hardening:** Servlet authentication, avoiding test/debug endpoints in production, secrets management (aligned to implementation analysis findings) — 8 min  
  - Debugging/troubleshooting — 2 min  
  - Best practices — 1 min  

- **Frontend (Deep)** — 22 min  
  - Client libraries (clientlibs) — 5 min  
  - Webpack, NPM, build and deploy into `ui.apps` — 8 min  
  - Debugging/troubleshooting — 5 min  
  - Best practices — 4 min  

- **External integrations (Vinay)** — 35 min  
  - **Workday** (jobs sync) — where it lives, how it’s invoked, configuration — 10 min  
  - **DPLT** (locations/venues) — data flow and usage in components — 8 min  
  - **GraphQL** — persistent queries, headless consumption, SHRSS usage — 10 min  
  - Other third-party (e.g. OpenTable, Grubhub, Google Maps) as applicable — 4 min  
  - Where to find integration code and configs in the repo — 3 min  

- **Content Fragments & GraphQL (Vinay / Andy)** — 22 min  
  - CF models in SHRSS (e.g. jobs, events, locations, venues) — 8 min  
  - Persistent queries and consumption in components — 8 min  
  - Relevance for Careers and future migrations — 6 min  

---

## Session 5 — AEM Application Development Parts 5 & 6, Change and Release Management, DevOps Part 1 (2 hours)

### AEM Application Development — Part 3 (continued) — 65 min

- **Dispatcher / CDN (Andy → Vinay)** — 28 min  
  - Cloud-optimized Apache and Dispatcher configs — 10 min  
  - Caching and security (filter rules, blocking unauthenticated servlet access where required) — 10 min  
  - CDN configuration (BYOCDN rules in `config` module if applicable) — 5 min  
  - Reference to implementation analysis Dispatcher/CDN findings where relevant — 3 min  

- **General AEM troubleshooting / debugging (Andy / Vinay)** — 15 min  
  - Cache issues (distribution queues, logs via distribution console) — 5 min  
  - Unhandled exceptions / 500s (AEM logs) — 5 min  
  - Developer Console (Experience League reference) — 5 min  

- **Development considerations for AEMaaCS (Andy)** — 22 min  
  - **Idempotency** — why it matters (horizontal scaling, restarts, retries); patterns for schedulers, listeners, workflows, repo init — 12 min  
  - Distributed, Mongo-based repository — 5 min  
  - Best practices — 5 min  

### Change and Release Management (Andy) — 25 min

- Source control management — 5 min
- Aligning code changes to Jira — 5 min
- Git branching strategy — 8 min
- Cutting a release and production deployment — 7 min

### DevOps — Part 1 (Andy) — 28 min

- **User / group / permission management (Admin Console IAM → native AEM groups)** — 15 min  
  - Walk-through (participant exercise):  
    1. Create IAM group in Admin Console (https://adminconsole.adobe.com/)  
    2. Add IAM user with DEV author profile to IAM group  
    3. User logs into DEV author  
    4. Add IAM group to native AEM group in AEM  
    5. View user and IAM group memberships in console  
  - How this maps to SHRSS roles and environments  

- **Cloud Manager** — 13 min  
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

### DevOps — Part 2 (Andy) — 32 min

- Pipelines deep dive (build, quality, security, deployment) — 14 min
- Logs and monitoring (Cloud Manager, AEM logs) — 10 min
- Troubleshooting failed pipelines and deployments — 8 min

### Testing (Andy / Vinay) — 38 min

- **Unit tests** — JUnit, coverage in `core` (models, services, servlets, etc.) — 12 min
- **Integration tests** — AEM testing client, `it.tests` module, Cloud Manager custom functional testing step — 10 min
- **UI tests** — Cypress, `ui.tests` module, Cloud Manager custom UI testing step — 10 min
- Where tests run in the pipeline and how to run locally — 6 min

### Conclusion / Q&A / Customer topics — 48 min

- Open Q&A — 20 min
- SHRSS-prioritized topics (e.g. specific integrations, security remediation, or migration prep) — 18 min
- Next steps and follow-up — 10 min
