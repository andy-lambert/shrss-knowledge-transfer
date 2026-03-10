# Adobe Experience Manager as a Cloud Service

## Comprehensive Best Practices Guide (All Roles)

> **Scope.** This guide goes deeper than public documentation, but continuously points back to Experience League and other public resources for canonical definitions and diagrams. It is intended for:
>
> - **Developers & Technical Architects**
> - **AEM / Cloud Admins & DevOps**
> - **Content Authors & Site Owners**
> - **DAM Architects & Librarians**

------

## 1. Foundations: How to Think About AEM as a Cloud Service

### 1.1 Core principles

**Key principles for every role**

- **Always-on**: no planned downtime for upgrades; code and content must tolerate rolling updates and node churn.
  *Ref:* [What is New and What is Different](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different)  
- **Cloud-native & stateless**:
  - Code runs in containers with **ephemeral storage**; do not rely on local file system or single-node state.
  - Persist state in **JCR**, external systems, or event streams – never in in‑memory singletons.
    *Ref:* [Architecture of AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/introduction/architecture)
- **Immutable vs mutable content**:
  - `/apps`, `/libs`, and code artifacts are **immutable**, deployed via Cloud Manager.
  - `/content`, `/conf`, `/var`, `/home`, `/oak:index` and user data are **mutable**, changing at runtime and across environments.
    *Ref:* [Implementing Applications for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/home)

**Best practices**

- **Architect for churn**: assume any given pod can disappear at any time; nothing critical should live only in one node’s memory or local /tmp.
- **Prefer configuration over code** when solving authoring problems (policies, templates, content models, workflows).
- **Align your vocabulary** (environments, programs, pipelines, mutable/immutable) with Experience League and Adobe contracts to avoid ambiguity in runbooks and RFPs.

------

### 1.2 Programs, environments, and topologies

**Concepts**

- **IMS Org → Product → Program → Environment**:
  - IMS Org = customer tenant.
  - Program = logical solution space (e.g. “Global Sites”, “Assets”), contains multiple environments.
  - Environment = specific stack (DEV, STAGE, PROD, RDE, etc.).
    *Ref:* [Managing your environments with Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments)
- Typical **topology per environment**:
  - Author cluster, Publish tier, Dispatcher + Adobe managed CDN.
    *Ref:* [Introduction to the Architecture of AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture)

**Best practices (architect/admin)**

- **Single codebase per program**:
  - Avoid splitting a single site into multiple programs unless there is a clear SLA / legal / region boundary.
- **Environment roles**:
  - `DEV`: integration, developer testing (non‑prod pipeline).
  - `STAGE`: prod‑like, performance & UAT, pre‑prod approvals (prod pipeline gate).
  - `PROD`: production only, no ad‑hoc experimentation.
  - `RDE`: short‑lived “scratch” environment for near‑real‑time dev testing.
    *Ref:* [Rapid Development Environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/rapid-development-environments)
- **Use Preview** (if licensed) for approval flows & SEO checks, not as a generic extra non‑prod.

**Anti-patterns**

- Treating **DEV as a personal sandbox** (random manual changes, no pipeline discipline).
- Using **STAGE for experiments** that are not intended to go to PROD.
- Hard‑coding environment URLs or credentials in code – always inject via OSGi config & environment variables.

------

## 2. Development Best Practices (Backend / Full Stack)

> **Audience:** developers, technical architects, DevOps, senior admins.
> **Reference anchor:** [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)

### 2.1 Project structure and modularization

**Baseline**

- Start from the **AEM Project Archetype** and keep it recognizable:
  - `core` – Java code (Sling Models, servlets, services, schedulers).
  - `ui.apps` – components, dialogs, clientlibs, policies.
  - `ui.content` – minimal baseline content/configs for bootstrapping.
  - `ui.config` – OSGi configs, repo init, ACL seeds.
  - `ui.frontend` – front‑end build (Webpack, TypeScript, etc.).
  - `dispatcher` – Apache/Dispatcher configs.
  - `it.tests` / `ui.tests` – integration & UI tests feeding Cloud Manager gates.
    *Ref:* [AEM Project Structure](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure)

**Best practices**

- **One “all” package**:
  - Single top‑level `all` module assembling deployable artifacts; Cloud Manager should deploy only that.
- **Separate concerns**:
  - Keep integration clients (e.g. “WorkdayClient”, “MapsClient”) in dedicated packages under `core`, not scattered through components.
- **Repo init for structure & ACLs**:
  - Use `repoinit` in `ui.config` to create system users, service users, groups, paths, and base ACLs. Do not create these manually in PROD.
- **Configuration-first approach**:
  - For any feature that might change per environment (endpoints, credentials, feature toggles): model it as an OSGi config and/or context-aware configuration.

**Anti-patterns**

- Multiple “all” packages or multiple disjoint AEM subprojects.
- Shipping **large volumes of author content** in `ui.content` (brittle and dangerous to deploy).
- Mixing **code and configuration** in the same module without clear separation.

------

### 2.2 OSGi configuration, run modes, repo init

**OSGi config strategy**

- **Single source of truth** in git:
  - Use `ui.config` with `/apps/<project>/osgiconfig` hierarchy.
- Prefer **factory configs** for multi‑instance services (e.g. multiple endpoints).
- Use **metatype annotations** (`@ObjectClassDefinition`) on config interfaces to give authors meaningful names and descriptions in Web Console for local SDK.

*Ref:* [Deploying to AEM as a Cloud Service – Run Modes](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/overview#runmodes)

**Run modes**

- In AEMaaCS, run modes are largely standardized; you typically differentiate via:
  - Configuration resource hierarchies (`/conf`).
  - Environment variables used by configs.
- For secrets (API keys, passwords):
  - Inject from environment variables or external secret stores; never hard‑code in OSGi configs committed to git.

**Repo init best practices**

- Use `repoinit` for:
  - Creating service users (`project-service`), groups, and path structure.
  - Granting minimal ACLs to service users at the narrowest possible paths.
- Keep **repo init idempotent**:
  - Scripts must be safe to run repeatedly (e.g. using `create path (ignore if exists)` semantics).
- Group repo init scripts by concern: `security.repoinit`, `structure.repoinit`, etc.

*Ref:* [Repository modernization](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/repository-modernization)

------

### 2.3 Sling Models, services, servlets, schedulers

**Sling Models**

- Default to **`@Model(adaptables = Resource.class)`** unless you truly need request‑specific context.
- Keep models **thin and composable**:
  - One responsibility per model; avoid multi‑page mega‑models with dozens of injected fields.
- Use **constructor or field injection**; avoid heavy logic in getters.
- For JSON/SPA use cases:
  - Implement `ComponentExporter` and expose only what the front‑end actually needs.

*Ref:* [Component Development in Adobe Experience Manager Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/components/component-development)

**Services & servlets**

- Create **named services** (interfaces + implementations) for business logic; Sling Models and servlets should delegate to them.
- Register servlets primarily by **resource type + selector + extension** (not arbitrary paths) to keep URL design consistent.
  *Ref:* [Servlets and Scripts (Sling)](https://sling.apache.org/documentation/the-sling-engine/servlets.html)

**Schedulers / event listeners**

- In AEMaaCS, **cluster awareness** is mandatory:
  - Use Sling Jobs / Async Jobs or other distributed mechanisms instead of naive local cron‑style schedulers.
  - Ensure idempotency: rerunning a job should be safe.
- Limit scope:
  - Avoid scanning entire repository trees per execution; use indexes or event streams to narrow the work.

*Ref:* [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)

------

### 2.4 Integration patterns and external systems

**General rules**

- Treat AEM as a **consumer/producer of APIs**, not the system of record for external domains (HR, commerce, reservations).
- Use a **dedicated integration layer** in code:
  - HTTP clients with clear interfaces.
  - DTOs for mapping to/from external payloads.

**Authentication**

- Prefer **OAuth server‑to‑server** or technical accounts over basic auth.
  *Ref:* [Generating Access Tokens for Server-Side APIs](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis)
- Store credentials in:
  - IMS technical account / Adobe Developer Console where possible.
  - Environment variables + encrypted secrets in external stores when not.

**Resilience & timeouts**

- Set **sane timeouts** (connect & read) on all HTTP calls.
- Use **circuit breaker / retry** patterns for transient failures; never block authoring or page rendering on slow external systems if you can serve cached content.
- Log **correlation IDs** so external system teams can match logs.

------

### 2.5 Testing strategy: unit, integration, functional, UI

**Unit tests (local, fast)**

- High coverage on `core` module – service logic, Sling Models, utilities.
- Mock AEM APIs where possible; avoid hitting actual repository in unit tests.

**Integration tests (`it.tests`)**

- Use AEM Testing Clients and run against local SDK or Cloud Manager non‑prod pipeline.
- Cover:
  - Basic endpoint contract tests.
  - Critical workflows (e.g. content approvals, key integrations).

*Ref:* [Java Functional Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/java-functional-testing)

**UI tests (`ui.tests`)**

- Implement end‑to‑end smoke tests with Cypress or Selenium:
  - Authoring smoke flows (log in, create page, edit component, publish).
  - Critical user journeys (landing → product → conversion).
    *Ref:* [UI Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/ui-testing)

**Best practices**

- Treat **Cloud Manager gates** as non‑negotiable:
  - Fix failing unit / code quality issues before retrying pipelines.
- Keep **test suites small & meaningful**:
  - Fast feedback in non‑prod pipelines.
  - Heavier coverage only in the main production pipeline or dedicated performance suites.

------

## 3. Front-End & Component Development

### 3.1 Core Components and component strategy

**Principles**

- **Default to Core Components** wherever possible:
  - Extend via policies, styles, and light overlaying, rather than building everything from scratch.
    *Ref:* [Core Components Introduction](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction)
- Maintain a **design system**:
  - Map design tokens (spacing, colors, typography) into CSS variables and policies.
  - Document which Core Components are allowed where, and which variations are supported.

**Best practices**

- Implement **site-level policies** in `/conf/<site>`; do not hard‑code allowed components in templates.
- Encourage **composition over inheritance**:
  - Use nested components / experience fragments instead of building monolithic “god” components.

------

### 3.2 Dialogs, policies, content structure

- Separate **content vs configuration**:
  - Content dialog: what authors edit instance‑by‑instance.
  - Design dialog / policy: per‑template or per‑site defaults and options.
- Provide **reasonable defaults**:
  - Authors should be productive with minimal configuration; avoid overwhelming dialogs.
- Validate inputs:
  - Use field constraints (`required`, `pattern`, min/max) where appropriate.

*Ref:* [Components and Editable Templates](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/components/component-development)

------

### 3.3 Clientlibs and front-end pipeline

**Clientlibs**

- Use **categories** logically:
  - `project.site`, `project.components`, `project.editor` etc.
- Always use **`allowProxy=true`** and reference via `/etc.clientlibs/...` to leverage Dispatcher / CDN caching.
- Keep JS/CSS modular and associated with components where possible.

*Ref:* [Using Client-Side Libraries on AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/clientlibs)

**Front-end build**

- Treat `ui.frontend` as the **source of truth**:
  - Webpack builds → `ui.apps` clientlibs.
- Avoid in‑browser transpilation; ship **compiled, minified bundles**.
- For SPA/headless scenarios:
  - Decide whether the app is hosted in AEM or externally; document ownership and deploy flows.

------

## 4. Content Modeling & Sites Authoring

> **Audience:** information architects, authors, product owners, architects.

### 4.1 Information architecture and page hierarchy

**Principles**

- Structure URLs to reflect **content, not technology**:
  - `/careers/jobs/1234` not `/content/site/us/en/careers/jobs/job-1234.html`.
- Keep a **shallow, meaningful hierarchy**:
  - Avoid 7+ nested levels; use facets and search rather than deep trees.
- Use **language roots** (`/en`, `/fr`, etc.) and align with MSM structures where needed.

*Ref:* [Sites Readiness for Data Protection and Data Privacy](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/compliance/sites-readiness)

------

### 4.2 Templates, page types, and governance

- Design a minimal set of **page templates**:
  - Home, Landing, Article/Detail, Listing, Utility.
- Govern templates:
  - Authors should choose from curated options; avoid template sprawl.
- Use **launches & workflows** for major changes and campaigns.

*Ref:* [Editable Templates and Page Templates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/templates/page-templates-editable)

------

### 4.3 Headless content: Content Fragments & GraphQL

**Modeling**

- Model **business entities** as Content Fragment Models:
  - Jobs, Events, Locations, Offers, etc.
- Keep models **normalized**:
  - Use references between fragments instead of repeating data.

**Delivery**

- Use **persisted queries**:
  - Stable, cacheable GET URLs for GraphQL requests.
- Implement **versioning strategy**:
  - Keep compatibility when changing CF models; version queries where needed.

*Ref:*  

- [AEM GraphQL API for Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/content-fragments)  
- [Persisted GraphQL Queries](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/persisted-queries)

------

## 5. Assets / DAM Best Practices

> **Audience:** DAM architects, librarians, authors, admins.

### 5.1 Folder structure and metadata

**Foldering**

- Organize by **business meaning**, not teams:
  - `/assets/products`, `/assets/brand`, `/assets/campaigns` instead of `/assets/marketing`, `/assets/it`.
- Use **collections** and saved searches for cross‑cutting needs (by team, region, campaign).

**Metadata**

- Define a **metadata schema**:
  - Use required fields for rights, expiration, usage restrictions.
  - Use controlled vocabularies (lists, tags) for key fields.
- Enforce **minimum metadata on upload** for production libraries.

*Ref:* [Assets as a Cloud Service Guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/home)

------

### 5.2 Asset ingestion and processing

- Use **ingestion profiles** and bulk upload patterns for large libraries.
- Configure **processing profiles** (renditions, transcodes) by asset type; avoid generating unnecessary heavy renditions.
- Use **Asset Compute / Dynamic Media** where real‑time transformations or advanced delivery are needed.
  *Ref:* [Asset Compute Service](https://experienceleague.adobe.com/en/docs/asset-compute/using/introduction)

------

### 5.3 Rights, expiration, and governance

- Make **expiration dates mandatory** for assets with time‑limited rights.
- Train authors to **respect “expired” and “do not use” flags**; wire into workflows where appropriate.
- Implement **role-based DAM permissions**:
  - Librarians with full curation rights.
  - Authors with restricted upload/delete capabilities.

------

## 6. Search, Indexing & Query Performance

> **Audience:** devs, architects, admins.
> *See also your indexing KT chapter for deeper examples.*

### 6.1 Using and extending OOTB indexes

- Know your **OOTB indexes** (e.g. `damAssetLucene`, `cqPageLucene`, `lucene`).
- For most needs:
  - **Extend index rules** instead of creating entirely new indexes.
- Avoid modifying OOTB definitions destructively:
  - Prefer adding properties and rules; document changes for future upgrades.

*Ref:*  

- [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [Query and Indexing Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)

------

### 6.2 Custom index design

**Guidelines**

- Start from the **query**, not from the data:
  - Identify exact where/contains/sort conditions used in production.
- Use **Lucene property indexes** for:
  - Property equality, like `status = 'PUBLISHED'`.
  - Path‑restricted queries with `evaluatePathRestrictions=true`.
    *Ref:* [Lucene Index](https://jackrabbit.apache.org/oak/docs/query/lucene.html)
- Keep indexes **small and precise**:
  - Only index paths under `/content` or relevant subtrees.
  - Only include properties that are actually filtered/sorted on.

**Anti-patterns**

- Full‑repository, catch‑all indexes that index “everything everywhere”.
- Unbounded “contains(., '…')” queries without path or node type restriction.

------

### 6.3 Troubleshooting queries

Tools and techniques:

- Use **Explain Query / Query Analyzer** in the AEM Query Tools to:
  - See which index plan is chosen.
  - Identify when traversal is used.
    *Ref:* [Troubleshooting Slow Queries](https://experienceleague.adobe.com/en/docs/experience-manager-65-lts/content/implementing/developing/bestpractices/troubleshooting-slow-queries) (still relevant conceptually)
- Use the **Performance/Operations Console** (local SDK) and **Developer Console** (cloud) to:
  - Inspect slow queries.
  - Capture stack traces for heavy requests.
    *Ref:* [Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)

**Best practices**

- Treat “**Query without index detected**” alerts as **actionable work**, not noise.
  *Ref:* [Adobe Experience Manager: Handle "Query Without Index Detected" Alert](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27862)
- Add **performance tests** for major search use cases and guard them with thresholds.

------

## 7. Dispatcher, CDN & Content Delivery

> **Audience:** architects, admins, DevOps, senior developers.

### 7.1 Dispatcher configuration structure

**Project layout**

- Use the Cloud Service‑supported structure:
  - `dispatcher/src/conf.d` – vhosts, rewrites, headers.
  - `dispatcher/src/conf.dispatcher.d` – farm, cache, filters, etc.
    *Ref:* [Dispatcher in the Cloud](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/disp-overview)

**Best practices**

- Maintain **separate vhosts** per domain / environment when needed; share common include files.
- Keep **filter rules explicit**:
  - Block by default, allow only required paths and methods.

------

### 7.2 Caching strategy (Dispatcher + CDN)

**Principles**

- Cache as **far to the edge as possible**:
  - Use Adobe managed CDN + Dispatcher in tandem.
    *Ref:* [CDN in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn)
- Make responses **cacheable by default** when safe:
  - Set `Cache-Control` / `Surrogate-Control` headers appropriately.

**Invalidation**

- Use **flush agents / content invalidation** via replication:
  - Single source of truth is AEM’s publish invalidation events.
- Avoid **brute-force cache clears** for entire sites; target paths or patterns.

*Ref:* [Caching in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/caching)

------

### 7.3 Security filtering

- Block:
  - `/system/console`, `/crx/*`, `/libs/*`, `/apps/*`, internal tooling.
- Restrict authenticated paths:
  - Ensure login flows happen on Author, or via secure publish flows if truly needed.
- Add **bot and abuse protection** where appropriate (rate limiting, WAF).

------

## 8. Operations, DevOps & Cloud Manager

### 8.1 Pipelines & branching

**Branching model**

- Common model:
  - `main` → Production pipeline.
  - `develop` → Dev non‑prod pipeline.
  - Feature branches → PRs into `develop`.
- Configure:
  - **Non‑prod pipeline**: fast feedback (DEV deployment, code quality, unit tests).
  - **Prod pipeline**: stage deploy, tests, approvals, prod deploy.
    *Ref:* [CI/CD Pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/overview/ci-cd-pipelines)

**Best practices**

- Treat pipeline failures as **code or config issues**, not infrastructure problems by default.
- Keep **Cloud Manager variables** clearly documented (secrets, endpoints, flags).

------

### 8.2 Environments, RDE, and content operations

- Use **RDE** for:
  - Rapid iteration and joint debugging with Adobe; avoid using PROD for experiments.
- Use **content copy / back-up/restore** features for:
  - Seeding lower environments.
  - Validated restores – understand scope and RPO/RTO.
    *Ref:* [Backup and Restore in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/backup)

------

### 8.3 Logging, monitoring, and troubleshooting

**Logging**

- Standardize log formats and include:
  - Correlation IDs.
  - Key domain identifiers (user, tenant, entity ID) where safe.
- Pull logs via:
  - Cloud Manager log download.
  - Developer Console (streaming).
    *Ref:* [Accessing and Managing Logs](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-logs)

**Monitoring**

- Use Cloud Manager and any integrated APMs for:
  - Error rates, response times.
  - Pipeline durations and test failures.

**Troubleshooting flow**

1. Reproduce on **SDK or RDE** if possible.
2. Inspect logs & Developer Console status.
3. Check Dispatcher/CDN configuration if behavior differs between environments.
4. Escalate with clear evidence (queries, correlation IDs, pipeline runs).

------

## 9. Security, Identity & Compliance

### 9.1 Identity and access control (IAM)

- Manage users and groups via **Admin Console**:
  - Product profiles (`AEM Users`, `AEM Administrators`).
  - Map IMS groups to AEM groups.
    *Ref:* [AEM as a Cloud Service Team and Product Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/concepts/aem-cs-team-product-profiles)
- In AEM:
  - Use AEM groups as **permission containers**, not as identity stores.
  - Avoid assigning ACLs to individual users; assign to groups.

*Ref:* [IMS Support for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/ims-support)

------

### 9.2 Secure coding and configuration

- Avoid:
  - Hard‑coded secrets, URLs, or credentials.
  - Direct HTTP calls without TLS.
- Validate and sanitize all:
  - User input used in queries or external calls.
- Configure:
  - CSP, X‑Frame‑Options, and other headers at Dispatcher where appropriate.

*Ref:* [Security Overview for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/cloud-service-security-overview)

------

### 9.3 Compliance & privacy

- Follow guidance for:
  - Data privacy and retention.
  - Data residency.
  - Web accessibility.
    *Ref:* [Compliance in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/compliance/home)

------

## 10. Governance & Ways of Working

### 10.1 Roles & responsibilities (high-level)

- **Technical Architect**:
  - Owns architecture, integration patterns, non‑functional requirements.
- **Developers**:
  - Implement features, tests, and follow coding standards.
- **AEM Admin / DevOps**:
  - Cloud Manager, pipelines, environments, monitoring, incident response.
- **Authors**:
  - Content creation & governance, workflows.
- **DAM Librarians**:
  - Asset schemas, metadata, lifecycle, rights management.

(You can align this with your AEM Governance Workshop outputs.)

------

### 10.2 Change & release management

- Every change must go through:
  - Code review.
  - Pipeline with automated tests.
- Document:
  - Release notes per deployment (features, fixes, risks).
- Use **feature toggles** where needed:
  - Avoid “big bang” releases; enable capabilities gradually.

------

### 10.3 Documentation & knowledge

- Maintain a **living runbook**:
  - How to deploy, rollback, debug.
  - Key dashboards and logs.
- Maintain **architecture diagrams** that mirror Experience League terminology, so external references remain clear.

------

## 11. Role-Specific Checklists

### 11.1 Developer / Architect checklist

-  Project structure matches AEM Archetype; single `all` package.
-  No direct writes to `/apps` or `/libs` at runtime.
-  No local filesystem reliance in code.
-  All integrations use configurable endpoints & credentials.
-  Indexes exist and are appropriate for all heavy queries.
-  Unit/integration/UI tests cover core flows and pass in Cloud Manager.

### 11.2 AEM Admin / DevOps checklist

-  Cloud Manager pipelines configured with clear branch mapping.
-  Environments documented with roles and data refresh strategy.
-  Log access and rotation procedures are known by on‑call engineers.
-  Backup/restore and content copy flows tested.
-  RDE usage pattern defined and communicated.

### 11.3 Author checklist

-  Understand templates & components available for your site.
-  Use approved page types and workflows for publication.
-  Tag and structure content for search and reuse.
-  Use launches, not ad‑hoc copies, for large campaigns.

### 11.4 DAM architect / librarian checklist

-  Folder structure and metadata schema documented and socialized.
-  Mandatory fields enforced for critical libraries.
-  Expiration and rights managed for assets with limited licenses.
-  Saved searches / collections created for high‑value use cases.

------

## 12. References (Core Public Docs to Pair with This Guide)

Core AEMaaCS implementation and architecture:

- [Implementing Applications for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/home)  
- [What is New and What is Different](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different)  
- [Architecture of AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/introduction/architecture)

Development guidelines and local dev:

- [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)  
- [Local Development Environment Set up](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview)

Cloud Manager and DevOps:

- [Manage environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments)  
- [CI/CD Pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/overview/ci-cd-pipelines)

Content delivery and Dispatcher/CDN:

- [Dispatcher in the Cloud](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/disp-overview)  
- [CDN in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn)  
- [Caching in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/caching)

Search & indexing:

- [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [Query and Indexing Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)  
- [Lucene Index](https://jackrabbit.apache.org/oak/docs/query/lucene.html)

Headless & GraphQL:

- [AEM GraphQL API for Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/content-fragments)  
- [Persisted GraphQL Queries](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/persisted-queries)

Assets:

- [Assets as a Cloud Service Guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/home)  
- [Asset Compute Service](https://experienceleague.adobe.com/en/docs/asset-compute/using/introduction)

Security & compliance:

- [Security Overview for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/cloud-service-security-overview)  
- [Compliance in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/compliance/home)

Debugging:

- [Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)  
- [How to fetch log files for AEM as a cloud service](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-22172)

You can keep extending this guide by embedding project‑specific examples (code snippets, diagrams) under each section while leaving the public references intact for external readers.

------