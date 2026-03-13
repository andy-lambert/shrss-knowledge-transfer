## Sessions 1 & 2 — Overview, AEM Application Development

### Overview

#### Cloud services ecosystem (Admin Console → Cloud Manager)

**Recommendations / additions**

- Explicitly connect **identity & access** to environments:
  - IMS org → AEM as a Cloud Service product → product profiles → environments.
  - Cloud Manager roles (Business Owner, Deployment Manager, Developer) vs AEM Users/Admins.
- Call out the **three consoles** and when each is used:
  - Admin Console – users, product profiles.
  - Cloud Manager – environments, pipelines, logs.
  - AEM Developer Console – runtime introspection & logs for a single environment.
- Briefly mention **Edge Delivery Services & Adobe-managed CDN** so they know where AEM Sites fits.

**Content ideas**

- 5–7 minute live walk‑through:
  1. Admin Console: show AEM CS product and AEM Users/AEM Administrators profiles.
  2. Cloud Manager: show the SHRSS program, dev/stage/prod, and pipelines.
  3. From Cloud Manager, jump into DEV Author.

**References**

- AEM as a Cloud Service implementation guide: [Implementing Applications for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/home)
- Team & product profiles (IAM mapping): [AEM as a Cloud Service Team and Product Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/concepts/aem-cs-team-product-profiles)
- Cloud Manager & environment types: [Manage environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments)

#### AEMaaCS architecture (high level)

**Recommendations / additions**

- Separate **“logical”** (author/publish/preview + CDN/Dispatcher) from **“service”** architecture (pods, autoscaling, golden master publish, shared data store).
- Explicitly contrast with 6.5:
  - No direct TarMK admin; content on a **shared cloud repository**, code on immutable images.
  - **Always‑on rolling updates**, no in‑place upgrades.
- Call out multi‑layer caching: **CDN → Dispatcher → Publish** and where invalidation happens.

**Content ideas**

- One **topology slide** based on public diagrams, covering:
  - Browser → CDN → Dispatcher (Apache) → Publish tier → (Author via replication).
  - Where Assets binary store / data store fit.
- Use 2–3 “tenets” as framing: *Always on*, *Always current*, *Always at scale*.

**References**

- Overall architecture: [Introduction to the Architecture of Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture)
- Content delivery path & caching: [Content Delivery Flow](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/overview), [Caching in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/caching)

#### AEMaaCS Cloud Manager paradigms (environments, pipelines, repos)

**Recommendations / additions**

- Clarify **types of environments** and their use:
  - Dev vs Stage vs Prod vs RDE vs Specialized Testing (if applicable).
- Explicitly map **pipelines**:
  - Non‑prod pipelines (code quality, dev deployment).
  - Production pipeline (stage + prod, with code quality, functional tests, UI tests, experience audit).
- Mention **where tests run** (unit, integration, UI) and how that ties to `it.tests` and `ui.tests`.

**Content ideas**

- Pipeline swimlane diagram showing:
  - Git branch → build & unit tests → code quality → image build → deploy to Stage → product tests/custom tests → deploy to Prod.
- Use your SHRSS pipeline as a concrete example (branching, triggers, approvals).

**References**

- CI/CD overview & pipeline steps: [CI/CD Pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/overview/ci-cd-pipelines)
- Production vs non‑production pipelines: [Using Adobe Cloud Manager - CI/CD Production Pipeline](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/cicd-production-pipeline), [Using Adobe Cloud Manager - CI/CD Non-Production Pipeline](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/cicd-non-production-pipeline)
- Tests in pipelines (code, functional, UI): [Cloud Manager Tests Overview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/overview-test-results)

------

### AEM Application Development

#### Development tooling / IDEs; local dev setup

**Recommendations / additions**

- Make AEM **SDK + local Dispatcher** first‑class:
  - Author + Publish locally, plus Dispatcher SDK via Docker.
- Recommended stack:
  - Java 11+, Maven, Node.js LTS, Git, VS Code or IntelliJ, VSCode AEM Sync (if they like).
- Show **remote debugging** with the SDK and basic log usage.

**Content ideas**

- Short demo: start local SDK, build & deploy SHRSS project with `mvn clean install -PautoInstallSinglePackage`, hit local site.
- Highlight typical **dev loop**: edit → unit tests → local deploy → commit → Cloud Manager pipeline.

**References**

- Local dev setup: [Local Development Environment Set up](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview)
- Dev playlists: [AEM development playlists](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/playlists/development)

#### Code structure (Maven / modules / other configs)

**Recommendations / additions**

- Anchor on **AEM Project Archetype** and the **“all package”** concept.
- Call out key modules and their responsibilities:
  - `core` – Java/Sling Models/OSGi services.
  - `ui.apps` – components, dialogs, clientlibs, policies.
  - `ui.frontend` – Webpack build, compiled into clientlibs.
  - `ui.content` – minimal baseline content/config; stress “don’t ship author content.”
  - `ui.config` – OSGi configs & repo init.
  - `dispatcher` – Apache/Dispatcher config for cloud.
  - `it.tests` / `ui.tests` – integration & UI tests wired into Cloud Manager.
- Explicitly relate **SHRSS repo layout** back to this structure so they can orient themselves.

**Content ideas**

- Show the SHRSS repo tree side‑by‑side with the standard WKND archetype tree; point out any **project‑specific additions** (ACL module, CDN config module, maintenance jobs, log forwarding).
- Add a simple **“what changes where?”** table: “new servlet → `core`”, “new component → `ui.apps` + `ui.frontend`”.

**References**

- Project structure & archetype:
  - [AEM Project Structure](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure)
  - [AEM Project Archetype (overview)](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/overview)
  - [What is the AEM as a Cloud Service Project Structure?](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/basics/project-structure)

#### AEM authoring components (Core Components, dialogs, clientlibs, Sling Models, best practices)

**Recommendations / additions**

- Make **Core Components** the baseline pattern and show how SHRSS extends them.
- For dialogs:
  - Show **policy vs edit dialog**, and how configuration lives under `/conf`.
- For clientlibs:
  - Emphasize **categories, dependencies, allowProxy**, and separation of **site‑level** vs **component‑level** libraries.
- For Sling Models:
  - Show **annotation style**, request vs resource adaptables, and use for JSON export (`ComponentExporter`).

**Content ideas**

- Demo: open a SHRSS page, inspect a custom component:
  - Component resource type → HTL script → Sling Model in `core` → dialog structure → clientlib category.
- Include a **small anti‑pattern slide**: logic in HTL, heavy use of JCR APIs directly, writing to `/content` from components, etc.

**References**

- Components & Core Components:
  - [Components Overview (developer)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/components-templates/overview)
  - [Core Components Introduction](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction)
- Clientlibs: [Using Client-Side Libraries on AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/clientlibs)
- Component & Sling Model basics: [Component Development in Adobe Experience Manager Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/components/component-development)

------

## Sessions 3 & 4 — AEM Application Development (continued)

### Backend

**Recommendations / additions**

- **Run modes / environment variables & secrets**
  - Show how environment variables map into `OSGi` configs via `ui.config` and/or `AIO` secrets for external services.
- **Repo init**
  - Include examples of repo init scripts in `ui.config` for users/groups/paths; stress avoiding manual changes in `/apps`.
- **OSGi components (servlets, Sling Models, services, schedulers)**
  - Show one **end‑to‑end example** in SHRSS – e.g. a scheduler that reads a config and writes to a log.
  - Call out **idempotency and cluster‑safety** for schedulers and listeners (tie to later AEMaaCS considerations).
- **Testing**
  - Clarify the three levels:
    - Unit tests for `core` classes.
    - Integration tests (`it.tests`) using AEM Testing Clients.
    - Cloud Manager **custom functional tests** running after stage deployment.

**Content ideas**

- Live view of an SHRSS OSGi config (via `/system/console/configMgr`) and where it’s defined in `ui.config`.
- Show a **JUnit test** and an **integration test** for the same feature, and where they run in the pipeline.

**References**

- Development guidelines (cluster awareness, no local FS state): [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)
- Integration & functional tests:
  - [Java Functional Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/java-functional-testing)
  - [Functional Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/functional-testing)

### Frontend

**Recommendations / additions**

- Place **ui.frontend** front and center:
  - Webpack, NPM scripts, TypeScript/SASS (if used), and how build output is copied into clientlibs.
- Make it clear how **authoring & theming** work:
  - Style System, design policies, how your SHRSS design tokens map into CSS.
- Testing:
  - Clarify **what Cypress tests cover**, where they live (`ui.tests`), and how they’re wired into the **Custom UI Testing** pipeline step. [UI Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/ui-testing)

**Content ideas**

- Show the `ui.frontend` folder in SHRSS:
  - NPM scripts → Webpack config → generated `clientlib-site` in `ui.apps`.
- Demo a **small front‑end change** (CSS tweak) deployed locally via Webpack dev server (if you use that pattern).

**References**

- ui.frontend & clientlibs workflow: [Client libraries and front-end workflow](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/project-archetype/client-side-libraries)
- Front-end with archetype: [Front-End Development with the AEM Project Archetype](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/front-end)
- UI tests in Cloud Manager: [UI Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/ui-testing)

### External integrations

**Recommendations / additions**

- For each integration (TransPerfect, Workday, DPLT, Unity, OpenTable/Grubhub/Maps):
  - Show **where configuration lives** (OSGi config vs conf/global vs environment variables).
  - Call out **authentication patterns** (OAuth server‑to‑server, API keys, technical account).
  - Discuss **failure modes** and how to detect them in logs.
- Tie into **AEM APIs / OpenAPI / Developer Console** for any inbound integrations (if relevant).

**Content ideas**

- Pick **one integration** (Workday jobs or TransPerfect) and walk through:
  - Trigger → servlet/workflow → external API → repository write → front‑end component.
- Show log snippets from a **happy path** and a **failure** to illustrate troubleshooting.

**References**

- Access tokens & technical accounts: [Generating Access Tokens for Server-Side APIs](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis)
- Product profiles & API permissions: [API Credentials and Product Profile management](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/how-to/credentials-and-product-profile-management)

### Content Fragments & GraphQL

**Recommendations / additions**

- Emphasize **content modeling**:
  - Show SHRSS CF Models (jobs, events, locations, venues) and how they map to actual use cases.
- Show **persisted queries** and why they matter:
  - Cacheable GET requests through CDN/Dispatcher vs ad‑hoc POST queries.
- Clarify **where queries are executed** from your code:
  - Server‑side via Sling Models / HTTP clients vs front‑end SPA (if applicable).

**Content ideas**

- In author:
  - Open a CF Model, then a Content Fragment instance for something real in SHRSS (e.g. “Job posting”).
  - Open **GraphiQL** and run a persisted query that returns those fragments. [Persisted GraphQL queries](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/persisted-queries)
- Show how that persisted query is wired into a **component** in the SHRSS codebase.

**References**

- CF & GraphQL basics:
  - [AEM GraphQL API for use with Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/content-fragments)
  - [Content Fragments - Setup](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/setup)
  - [Persisted GraphQL queries](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/persisted-queries)
- Headless journeys:
  - [Getting Started with AEM Headless as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/journeys/developer/getting-started)
  - [Path to Your First Experience Using AEM Headless](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/journeys/developer/path-to-first-experience)

------

## Sessions 5 & 6 — AEM App Dev (continued), Change & Release Management

### Dispatcher / CDN

**Recommendations / additions**

- Emphasize that **Dispatcher is part of the codebase** and validated by Cloud Manager.
- Show:
  - Folder structure under `dispatcher/src/conf.d` and `conf.dispatcher.d`.
  - **Filters** (security), **cache rules**, and **vhosts** for SHRSS domains.
- Connect **Dispatcher caching headers** to the **CDN behavior** (Cache-Control / Surrogate-Control etc.).

**Content ideas**

- Show an SHRSS `filters.any` with:
  - Rules for blocking `/system/console`, `/bin/*` except whitelisted.
  - Example rules for blocking unauthenticated servlet access.
- Demo `dispatcher validator` locally and how an invalid config fails the pipeline.

**References**

- Dispatcher & CDN configuration:
  - [Caching in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/caching)
  - [Dispatcher Configurations in Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/en/docs/events/tech-sessions/2025/dispatcher-configurations)
  - [Dispatcher Overview](https://experienceleague.adobe.com/en/docs/experience-manager-dispatcher/using/dispatcher)

### General AEM troubleshooting / debugging

**Recommendations / additions**

- Show a simple **troubleshooting workflow**:
  - Error → locate relevant logs (Cloud Manager vs Developer Console vs AEM log files) → identify root cause → fix → RDE or dev deployment.
- Include:
  - Distribution console for cache invalidation issues.
  - Developer Console **status dumps** (Sling Models, OSGi, health checks).
  - Local SDK as a reproduction environment.

**Content ideas**

- Walk through a **500 error** example:
  - Show log snippet in Cloud Manager / Developer Console.
  - Find relevant Java class or Dispatcher rule.
  - Show the fix and re‑deploy to RDE or dev.

**References**

- Troubleshooting & debugging:
  - [Troubleshooting AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/troubleshooting)
  - [Debugging AEM as a Cloud Service with the Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)
  - [How to fetch log files for AEM as a cloud service](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-22172)

### Development considerations for AEMaaCS

**Recommendations / additions**

- Make this a **Cloud‑specific “guardrails”** section:
  - Code must be **cluster‑aware** and **stateless**.
  - Do **not** write to local filesystem or immutable areas at runtime (`/apps`, `/libs`); use repository or external storage.
  - Idempotency patterns for schedulers/listeners/workflows.
  - Understand **mutable vs immutable** content and the role of the `all` package.

**Content ideas**

- Show a couple of **bad patterns** and their Cloud‑friendly refactors:
  - Writing to `/var` from code vs using a service and proper ACLs.
  - Storing long‑lived state in memory vs writing to JCR / external system.
- Make a **checklist slide** they can use in PR reviews.

**References**

- Cloud development guidelines: [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)
- Migration & repository structure: [Repository modernization](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/repository-modernization)

### Change and Release Management

**Recommendations / additions**

- Show how **Git branching strategy** maps to Cloud Manager pipelines (e.g. `main` → prod pipeline, `develop` → dev deploy, feature branches → code quality pipeline).
- Emphasize:
  - **Pull request discipline** (including unit/integration tests).
  - Using **non‑prod pipelines** and **RDE** for early feedback.
- Tie Jira:
  - Commit message or branch naming conventions (`feature/SHRSS-1234`); maybe automations if they exist.

**Content ideas**

- Draw a **branch & pipeline diagram**:
  - Feature → PR to `develop` → Non‑prod pipeline to DEV → merge to `main` → prod pipeline.
- Show an example **Cloud Manager build result** and how issues are surfaced back to dev.

**References**

- CI/CD & code quality:
  - [Use the CI/CD Pipeline in Adobe Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/cloud-manager/use-the-cicd-pipeline-in-cloud-manager-for-aem)
  - [Continuous Integration and Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/devops/continuous-integration)

------

## Sessions 7 & 8 — DevOps

### User / group / permission management (Admin Console IAM → AEM groups)

**Recommendations / additions**

- Explicitly cover:
  - **Product profiles** (AEM Users vs AEM Administrators) and how they map to AEM groups.
  - Why you **do not** manage identities directly in AEM; AEM groups are for permissions, Admin Console is for membership.
- In the exercise, show:
  - How the IMS user appears in AEM (`/useradmin`).
  - How adding an IMS group to an AEM group grants repo ACLs.

**Content ideas**

- Turn your step‑through into a **live lab**:
  - Have a participant create an IAM group, add themselves, log into DEV, and verify group membership in AEM.
- Show SHRSS **role mapping**: which AEM groups correspond to which SHRSS roles (Author, Approver, Admin, etc.).

**References**

- Product profiles & user access:
  - [Assigning AEM Product Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem)
  - [Configuring access to AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/accessing/overview)

### Cloud Manager (environments, RDE, run modes, repos, pipelines, whitelists, restore, logs)

**Recommendations / additions**

- Environments:
  - Clear table of **Dev / Stage / Prod / RDE / Preview**, what’s running where, and how SHRSS uses each.
- RDE:
  - Show how devs use `aio aem:rde` to push **near‑final code** for fast validation, then promote via pipelines. [Rapid Development Environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/rapid-development-environments)
- Pipelines:
  - Show exactly **where unit tests, integration tests, and UI tests** run.
- Logs & monitoring:
  - Show how to get logs from Cloud Manager vs Developer Console.
- Restore / content copy:
  - Briefly cover **code rollback** vs **content restore** vs **bulk content copy** between envs.

**Content ideas**

- Live Cloud Manager tour:
  - Environments card → Pipelines → start a non‑prod pipeline and show gates.
  - Logs download for an environment; open `aemerror` for a specific time range.
- If licensed, demo a simple **RDE push** of a change and show its appearance on an RDE URL.

**References**

- RDE: [Rapid Development Environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/rapid-development-environments)
- Environments & management:
  - [Manage environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments)
  - [Create Environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/create-environments)

------

## Sessions 9 & 10 — Q&A / SHRSS Topics

For these, the agenda is intentionally open. A few **structured prompts** you could pre‑seed (and be ready with backups):

- **Code deep dives**
  - Pick 1–2 representative components or services (e.g. a GraphQL‑driven listing, a key integration) and walk from **request → Sling → code → repository**.
- **Integrations**
  - Bring sequence diagrams for TransPerfect or Workday so Q&A can be diagram‑driven rather than code‑only.
- **DevOps**
  - Prepare a path for “show us how you’d debug X in production” and walk through logs, Developer Console, and RDE use.
- **Headless & future work**
  - Be ready to revisit the **CF/GraphQL** content with an eye towards **future SHRSS use cases** (new channels, apps, or external consumers).

You can also keep a short **“parking lot”** slide of topics that come up earlier (e.g. search/indexing, performance, security headers) and address them here if time allows; many have good public references you can send them home with.

------

### Summary checklist

If you want a quick action list before you present:

-  Add 1–2 **architecture diagrams** (logical + content delivery).
-  Prepare a **repo structure slide** mapping SHRSS modules to Archetype modules.
-  Select 1–2 **showcase components** to walk through end‑to‑end (HTL + Sling Model + CF/GraphQL if applicable).
-  Capture **one integration** (Workday or TransPerfect) as a simple sequence diagram.
-  Build a **pipeline & testing** slide that aligns with Cloud Manager docs.
-  Plan a short **IAM → AEM group** exercise + a quick **RDE or dev deploy** demo.