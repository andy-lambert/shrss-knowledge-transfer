## Sessions 1 & 2 — Overview, AEM Application Development

### Overview (Andy)

- Cloud services ecosystem (Admin Console → Cloud Manager)
- AEMaaCS architecture (high level)
- AEMaaCS Cloud Manager paradigms (environments, pipelines, repos)

### AEM Application Development

- **Development tooling / IDEs (Andy / Vinay)**
  - Local dev setup, IDE configuration
- **Code structure (Andy / Vinay)**
  - Maven/POM configuration and dependency management
  - Main modules: core, ui.apps, ui.frontend, ui.content, ui.config, dispatcher, it.tests, ui.tests, all, acl, config
  - Other configs: CDN rules, maintenance tasks, log forwarding
- **AEM authoring components (Vinay / Deepkamal)**
  - Core Components and extending (e.g. hrccard)
  - Dialogs
  - Clientlibs (definition, categories, file/folder structure)
  - Sling Models (Use-API, extending, debugging)
  - Best practices (structure, clientlib categories)

## Sessions 3 & 4 — AEM Application Development (continued)

### AEM Application Development

- **Backend (Andy → Vinay)**
  - Run modes, environment variables and secrets
  - Repo initialization
  - OSGi component implementations (servlets, Sling models, services, listeners, schedulers — as implemented in SHRSS)
  - OSGi configurations (ui.config)
  - Testing
    - Unit tests — JUnit, coverage in core (models, services, servlets, etc.)
    - Integration tests — AEM testing client, it.tests module, Cloud Manager custom functional testing step
  - Debugging/troubleshooting
  - Best practices
- **Frontend (Deepkamal)**
  - Client libraries (clientlibs)
  - Webpack, NPM, build and deploy into ui.apps
  - Testing
    - Cypress, ui.tests module, Cloud Manager custom UI testing step
  - Debugging/troubleshooting
  - Best practices
- **External integrations (Vinay)**
  - TransPerfect (language translation)
  - Workday (jobs sync) — where it lives, how it’s invoked, configuration
  - DPLT (locations/venues) — data flow and usage in components
  - Unity login (iFrame)
  - Other third-party (e.g. OpenTable, Grubhub, Google Maps) as applicable
  - Where to find integration code and configs in the repo
- **Content Fragments & GraphQL (Vinay / Andy)**
  - CF models in SHRSS (e.g. jobs, events, locations, venues)
  - Persistent queries and consumption in components
  - Relevance for Careers and future migrations

## Sessions 5 & 6 — AEM Application Development (continued), Change and Release Management

### AEM Application Development (continued)

- **Dispatcher / CDN (Andy → Vinay)**
  - Cloud-optimized Apache and Dispatcher configs
  - Caching and security (filter rules, blocking unauthenticated servlet access where required)
  - CDN configuration (BYOCDN rules in config module if applicable)
  - Reference to implementation analysis Dispatcher/CDN findings where relevant
- **General AEM troubleshooting / debugging (Andy / Vinay)**
  - Cache issues (distribution queues, logs via distribution console)
  - Unhandled exceptions / 500s (AEM logs)
  - Developer Console (Experience League reference)
- **Development considerations for AEMaaCS (Andy)**
  - Idempotency — why it matters (horizontal scaling, restarts, retries); patterns for schedulers, listeners, workflows
  - Distributed, Mongo-based repository
  - Best practices

### Change and Release Management (Andy)

- Source control management
- Aligning code changes to Jira
- Git branching strategy
- Cutting a release and production deployment

## Sessions 7 & 8 — DevOps

### DevOps (Andy)

- **User / group / permission management (Admin Console IAM → native AEM groups)**
  - Walk-through (participant exercise):
    1. Create IAM group in Admin Console (https://adminconsole.adobe.com/)
    2. Add IAM user with DEV author profile to IAM group
    3. User logs into DEV author
    4. Add IAM group to native AEM group in AEM
    5. View user and IAM group memberships in console
  - How this maps to SHRSS roles and environments
- **Cloud Manager**
  - Environments
    - Dev, QA, Integration, Stage, Prod
    - Rapid Development Environments (RDE)
    - Preview tier
  - Run modes, environment variables and secrets
  - Repositories
  - Build pipelines (build, quality, security, deployment)
    - Where tests run in the pipeline and how to run locally
  - Environment whitelists
  - Content restore and bulk content copy
  - Logs and monitoring (Cloud Manager, AEM logs)
  - Troubleshooting failed pipelines and deployments

## Sessions 9 & 10 — Q&A / SHRSS Topics

- SHRSS-prioritized topics (code deep dives, integrations, configurations, DevOps, etc.)
- Open Q&A
