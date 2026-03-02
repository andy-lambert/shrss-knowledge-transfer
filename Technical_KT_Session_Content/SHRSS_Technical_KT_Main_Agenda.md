# Technical Knowledge Transfer Agenda

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
