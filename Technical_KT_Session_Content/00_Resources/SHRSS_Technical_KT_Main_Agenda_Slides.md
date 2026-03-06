### Slide 1 – Session Title & Objectives

**Title:**
AEM & AEM as a Cloud Service – Technical Architecture & Development Overview

**Slide content (bullets):**

- Context: Customer ownership of AEM as a Cloud Service (AEMaaCS)
- Goals for this KT series
  - Understand AEM foundations (JCR, Sling, OSGi, Granite)
  - Understand AEMaaCS architecture & Cloud Manager
  - Understand project structure, pipelines, and operations
- Today’s focus
  - Architecture overview
  - Development model
  - Ops & troubleshooting guardrails

**Speaker notes (optional):**
“This series is about handing you the keys to your AEMaaCS platform. Today we’ll align on how AEM works under the hood, what changes in Cloud Service, and how the development and operations model fits together. Later sessions will drill into components, integrations, and day‑to‑day workflows.”

**Visual guidance (Gemini prompt):**  

> Create a clean, minimal title slide background in Adobe brand style: abstract geometric shapes in light greys and a subtle red accent, with an architectural / cloud computing theme but no text. 16:9 aspect, high contrast but not busy.

------

### Slide 2 – AEM in the Adobe Experience Cloud

**Title:**
Where AEM Fits in the Adobe Experience Cloud

**Slide content:**

- AEM as part of **Experience Cloud**
  - AEM Sites, Assets, Forms, Edge Delivery Services
- AEM as a Cloud Service (AEMaaCS)
  - Always on, always current, cloud‑native
- Integrations (high level)
  - Analytics / Customer Journey Analytics, Target, Journey Optimizer, Workfront, etc.

**Speaker notes:**
“Quickly placing AEM in the broader Adobe stack: it’s our content and experience management foundation. As a Cloud Service, it’s continuously updated and designed to integrate with the rest of Experience Cloud and with your enterprise systems.”

**Visual guidance:**  

> Generate a simplified Experience Cloud landscape diagram: a central “AEM” box connected to “Sites”, “Assets”, “Forms”, and “Edge Delivery Services”, with surrounding icons for “Analytics”, “Target”, “Journey Optimizer”, “Workfront”, etc. Use flat icon style, Adobe-like color palette (red, dark grey, white), 16:9.

**Reference:**  

- [Adobe Experience Manager as a Cloud Service videos and tutorials](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/overview)

------

### Slide 3 – Cloud Services Ecosystem & Consoles

**Title:**
Cloud Services Ecosystem: Admin Console, Cloud Manager, Developer Console

**Slide content:**

- **Admin Console**
  - IMS org, products, product profiles (AEM Users / AEM Admins)
- **Cloud Manager**
  - Programs, environments, pipelines, logs & monitoring
- **Developer Console**
  - Per‑environment, read‑only runtime introspection
  - Bundles, OSGi configs, Sling models, logs, status

**Speaker notes:**
“Think of three main consoles: Admin Console for identity and product profiles, Cloud Manager for environments and pipelines, and Developer Console for runtime introspection. We’ll keep referring back to these as we move through Dev, Ops, and troubleshooting topics.”

**Visual guidance:**  

> Create a 3-column infographic with icons labeled “Admin Console”, “Cloud Manager”, and “Developer Console”. Show arrows: Admin Console → Cloud Manager → AEM Environments, and a side arrow from Cloud Manager to Developer Console. Use a clean, thin-line style.

**References:**  

- [AEM as a Cloud Service Team and Product Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/concepts/aem-cs-team-product-profiles)  
- [Using Adobe Cloud Manager - Environments](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/environments)  
- [Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)

------

### Slide 4 – AEMaaCS Logical Architecture

**Title:**
AEMaaCS Logical Architecture: Author, Publish, Dispatcher, CDN

**Slide content:**

- **Author**: internal content authoring, workflows, approvals
- **Publish**: public‑facing experiences, APIs (Sites, headless)
- **Preview**: internal review of “near‑live” content
- **Dispatcher + CDN**
  - Apache + Dispatcher cache in front of Publish
  - Adobe‑managed CDN at the edge

**Speaker notes:**
“Logically, Cloud Service still looks familiar: Author for internal users, Publish serving the outside world, Dispatcher and CDN providing caching and protection in front. Preview is a special tier for validating what’s about to go live.”

**Visual guidance:**  

> Create a simple left-to-right topology diagram: “Authors” → “Author Service” → “Replication” → “Publish Tier” → “Dispatcher (Apache)” → “Adobe-managed CDN” → “End Users”. Use labeled boxes and arrows. Minimal, technical whiteboard style.

**References:**  

- [Introduction to the Architecture of Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture)  
- [Content Delivery Flow](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/overview)

------

### Slide 5 – AEMaaCS Service Architecture & Scaling

**Title:**
Service Architecture: Pods, Scaling, Immutable Images

**Slide content:**

- AEMaaCS runs on **Kubernetes** pods
  - Author and Publish clusters, autoscaled
- **Immutable images** for code & configs
  - Built by Cloud Manager pipelines
- Shared **content repository**
  - Publish “golden master” + distribution queues
- Tenets: *Always on*, *Always current*, *Always at scale*

**Speaker notes:**
“Underneath, AEMaaCS is containerized. Your application code and configuration are baked into immutable images. Cloud Manager builds and deploys these images, and the platform scales pods up and down without you having to manage servers.”

**Visual guidance:**  

> Generate a diagram of a Kubernetes-based architecture: two grouped clusters labeled “Author pods” and “Publish pods” inside a “Kubernetes” boundary, with a shared “Content Repository / Data Store” below them and a “Cloud Manager CI/CD” box feeding new images into both clusters. Use a technical, blueprint style.

**Reference:**  

- [Architecture of AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/introduction/architecture)

------

### Slide 6 – From On-Prem/AMS to AEMaaCS

**Title:**
Key Differences: AEM 6.x vs AEM as a Cloud Service

**Slide content:**

- No direct TarMK / MongoMK admin; **Adobe manages platform**
- **Rolling updates**, no in‑place upgrades
- Clear split: **code/config (immutable)** vs **content (mutable)**
- Access to **logs & runtime** via Cloud Manager / Developer Console
- Guardrails: limited filesystem access, whitelisted OSGi options

**Speaker notes:**
“For teams used to AEM 6.5 or AMS, the big change is mindset: you no longer manage the platform. You focus on clean, stateless code and content structures; Cloud Manager and Adobe handle scaling and versioning.”

**Visual guidance:**  

> Create a before/after comparison diagram: left side “AEM 6.x / AMS” (servers, manual upgrades), right side “AEMaaCS” (pods, Cloud Manager, rolling updates). Use a split-screen style with concise icons.

**Reference:**  

- [What is Different and What is New – AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different)

------

### Slide 7 – Cloud Manager: Programs, Environments, Pipelines

**Title:**
Cloud Manager: Programs, Environments, Pipelines

**Slide content:**

- **Program**
  - Logical container for environments, repos, pipelines
- **Environments**
  - Dev, Stage, Prod, RDE, Specialized Testing, Preview
- **Pipelines**
  - Production pipelines (Stage → Prod)
  - Non‑production pipelines (Dev, code quality)

**Speaker notes:**
“Each customer program encapsulates an AEM deployment: environments, code repo, and pipelines. Production pipelines drive Stage and Prod, while non‑prod pipelines and RDE support rapid development and validation.”

**Visual guidance:**  

> Generate a diagram with a “Program” box containing three environment boxes (Dev, Stage, Prod) plus a “RDE” box, and arrows from a “Git Repository” through “Non‑Prod Pipeline” to Dev and “Prod Pipeline” through Stage to Prod.

**References:**  

- [Introduction to CI/CD Pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/cicd-pipelines/introduction-ci-cd-pipelines)  
- [Create Environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/create-environments)

------

### Slide 8 – CI/CD Pipeline Flow

**Title:**
CI/CD Pipeline Flow in Cloud Manager

**Slide content:**

- Trigger
  - Manual, on Git change, or scheduled
- Build & test
  - Maven build, unit tests, code quality scan
- Stage deployment
  - Security & performance tests, optional functional/UI tests
- Production deployment
  - Managed approval gates, rolling updates, cache invalidation

**Speaker notes:**
“This slide explains how code travels from Git to production: build and tests, then deployment to Stage with automated checks, then gated promotion into Prod. A key point is that the same build artifacts are reused, guaranteeing what passed in Stage is what lands in Prod.”

**Visual guidance:**  

> Create a horizontal pipeline diagram with labeled stages: “Trigger” → “Build & Unit Tests” → “Code Quality Scan” → “Deploy to Stage” → “Functional/UI Tests” → “Deploy to Prod”. Use distinct colors per stage and a clear flow arrow.

**References:**  

- [CI/CD Pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/overview/ci-cd-pipelines)  
- [Using Adobe Cloud Manager – CI/CD Production Pipeline](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/cicd-production-pipeline)

------

### Slide 9 – Local Development Environment

**Title:**
Local Development for AEMaaCS

**Slide content:**

- Local **AEM SDK** (Author + Publish)
- Local **Dispatcher Tools** (Apache + Dispatcher via Docker)
- Required tools
  - Java 11+, Maven, Node.js, Git, IDE (IntelliJ/VS Code)
- Dev loop
  - Code → unit tests → local deploy → Git push → pipeline

**Speaker notes:**
“Even though we deploy through Cloud Manager, most work should be done locally on the SDK with a local Dispatcher. That’s the fastest way to validate changes before they ever hit a shared environment.”

**Visual guidance:**  

> Generate a diagram with three boxes: “AEM Project (code)” → “Local AEM Runtime (Author/Publish)” → “Local Dispatcher Runtime”, with a laptop icon beside them and a circular arrow showing the inner dev loop.

**References:**  

- [Local Development Environment for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview)  
- [Set up local development environment](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/basics/local-development-environment)

------

### Slide 10 – AEM Project Structure Overview

**Title:**
AEM Project Structure (Maven Multi‑Module)

**Slide content:**

- **all** – container package; embeds other packages
- **core** – Java code, Sling Models, OSGi services
- **ui.apps** – components, dialogs, clientlibs, policies
- **ui.content** – baseline content/config (no author content)
- **ui.config** – OSGi configs, repo init
- **dispatcher** – Apache & Dispatcher config
- **it.tests / ui.tests** – integration & UI tests

**Speaker notes:**
“The archetype sets up a best‑practice project structure. The `all` package is the single artifact Cloud Manager deploys; it pulls in your Java bundle, components, configs, and dispatcher config. Understanding what belongs in each module is key to maintainable code.”

**Visual guidance:**  

> Create a vertical tree diagram showing the Maven modules under a top-level “AEM Project” node, with brief labels beside each module name (all, core, ui.apps, ui.content, ui.config, dispatcher, it.tests, ui.tests).

**References:**  

- [AEM project structure](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/basics/project-structure)  
- [AEM Project Archetype overview](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/overview)

------

### Slide 11 – Mutable vs Immutable Content

**Title:**
Immutable Code, Mutable Content

**Slide content:**

- **Immutable (deployed via `all`)**
  - `/apps`, OSGi configs, dispatcher configs
- **Mutable (runtime‑writable)**
  - `/content`, `/conf`, `/var`, `/home`, `/oak:index`, etc.
- Implication:
  - No runtime writes to immutable areas
  - Use repo init / packages for structural changes

**Speaker notes:**
“A core Cloud Service concept is the split between immutable code/config and mutable content. Your application must never write to immutable areas at runtime. Structural changes are made via code and deployed; content changes are authoring activities or content packages.”

**Visual guidance:**  

> Create a two-column “Immutable vs Mutable” comparison graphic with icons and example paths for each side. Use a lock icon on the immutable side and a pencil/edit icon on the mutable side.

**Reference:**  

- [Repository Modernizer (mutable vs immutable)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/refactoring-tools/repo-modernizer-cam)

------

### Slide 12 – Components & Core Components

**Title:**
AEM Components & Core Components

**Slide content:**

- Components = mapping of **resource type → HTL → Sling Model**
- **Core Components**
  - Prebuilt, versioned, extensible
  - Proxy pattern for customization
- Project pattern
  - Prefer Core Components + styling
  - Custom components only when required

**Speaker notes:**
“For authors and implementers, components are the building blocks. Technically, each component is a resource type with HTL templates and often a Sling Model. Core Components should be the default choice; custom components are reserved for true business uniqueness.”

**Visual guidance:**  

> Generate a layered diagram showing “Content Resource (resourceType)” → “Component (HTL)” → “Sling Model (Java)” → “Rendered HTML/JSON”. Include a callout showing “Core Component” with a small ‘proxy’ icon.

**References:**  

- [Components and templates overview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/components-templates/overview)  
- [Core Components introduction](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction)

------

### Slide 13 – Dialogs, Policies, and Style System

**Title:**
Authoring Experience: Dialogs, Policies, Style System

**Slide content:**

- **Edit dialogs** – author‑visible fields on components
- **Design dialogs / policies**
  - Stored in `/conf`, define allowed components & variations
- **Style System**
  - Change look & feel without creating new components
- Best practice: keep dialogs simple, consistent, accessible

**Speaker notes:**
“Policies and the Style System let you give authors flexibility without exploding the number of components. Dialogs should focus on business fields; policies and styles control layout and presentation.”

**Visual guidance:**  

> Create a conceptual diagram: a “Component” box with arrows to “Edit Dialog” (for authors), “Design Policy (in /conf)” (for admins), and “Style Variants” (for designers). Use simple UI-like icons.

**Reference:**  

- [Getting Started with AEM Sites – Project Archetype (templates & policies)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/project-archetype/project-setup)

------

### Slide 14 – Clientlibs & Front-End Build

**Title:**
Client Libraries & Front‑End Workflow

**Slide content:**

- **Clientlibs (client‑side libraries)**
  - Categories, dependencies, `allowProxy`
- **ui.frontend**
  - Webpack/Node build → emits CSS/JS into clientlibs
- Separation of concerns
  - Component‑level vs site‑level libraries
- Best practices
  - Avoid global selectors; use BEM, minimize blocking JS

**Speaker notes:**
“AEM’s clientlibs system manages how CSS and JS are delivered. The `ui.frontend` module can give front‑end devs a modern workflow that outputs into clientlibs consumed by components and templates.”

**Visual guidance:**  

> Generate a pipeline diagram: “ui.frontend (Webpack, Node)” → “Compiled CSS/JS” → “Clientlibs in ui.apps” → “HTML Pages”. Use icons for code, gears, and browser.

**Reference:**  

- [Using Client-Side Libraries on AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/clientlibs)

------

### Slide 15 – Sling Models & Backend Patterns

**Title:**
Sling Models & Backend Development

**Slide content:**

- Sling Models
  - `@Model(adaptables = Resource/Request)`
  - Encapsulate component logic & data access
- OSGi services
  - Shared logic, external integrations, schedulers
- Patterns
  - Prefer Sling Models + services over script logic
  - Keep models focused and testable

**Speaker notes:**
“Sling Models are the primary pattern for binding content to components, and OSGi services hold any shared business logic or integration code. Avoid placing complex logic directly in HTL or JSPs; instead route through models and services.”

**Visual guidance:**  

> Create a class diagram-style visual showing a Sling Model annotated with `@Model` consuming an OSGi service, with arrows from a JCR resource to the model and from the model to rendered HTML/JSON.

**References:**  

- [Component Development in Adobe Experience Manager Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/components/component-development)

------

### Slide 16 – Backend: OSGi Services, Servlets, Schedulers

**Title:**
Backend Building Blocks: Services, Servlets, Schedulers

**Slide content:**

- **OSGi components** (services)
  - Reusable business logic; configured via OSGi configs
- **Servlets**
  - HTTP endpoints (JSON/HTML), always behind auth/Dispatcher filters
- **Schedulers & listeners**
  - Time‑based jobs, event‑driven processing
- Cloud constraints
  - Stateless, idempotent; cluster‑safe design

**Speaker notes:**
“The usual backend primitives still exist in Cloud Service: services, servlets, and schedulers. The difference is how you design them: they must be cluster‑aware and stateless, assuming multiple pods may run your code concurrently.”

**Visual guidance:**  

> Generate a block diagram showing “OSGi Service” in the center, with arrows to “Servlet (HTTP)”, “Scheduler”, and “Event Listener”, and a cloud-shaped boundary labeled “AEMaaCS cluster”.

**Reference:**  

- [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)

------

### Slide 17 – Configuration: Run Modes & Repo Init

**Title:**
Configuration: OSGi, Run Modes, Repo Init

**Slide content:**

- OSGi configs in code
  - Stored in `ui.config` / repo, deployed via pipeline
- Environment‑specific behavior
  - Environment variables, run‑mode aware configs
- Repo init
  - Define service users, groups, paths, ACLs in code
- No in‑place config editing in Prod

**Speaker notes:**
“Configs are code. OSGi configs are managed via files in your repo, not edited directly in production. Repo init is your friend for defining service users, groups, and permissions in a repeatable, versioned way.”

**Visual guidance:**  

> Create a diagram showing configuration files in Git → Cloud Manager pipeline → AEM Author/Publish (with icons for OSGi config and repo init scripts). Emphasize the “config as code” concept.

**References:**  

- [Logging for AEM as a Cloud Service (config in code pattern)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/logging)  
- [What is Different and What is New – OSGi configuration](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different)

------

### Slide 18 – Testing Pyramid for AEM

**Title:**
Testing in AEM: Unit, Integration, UI

**Slide content:**

- **Unit tests**
  - Java logic in `core` module
- **Integration tests (`it.tests`)**
  - Exercise AEM APIs against an instance
- **Functional / UI tests (`ui.tests`)**
  - Selenium/Cypress‑style, run in pipeline
- Pipeline integration
  - Code quality gate + functional & UI testing on Stage

**Speaker notes:**
“Cloud Manager encourages a layered testing strategy: unit tests in the build, integration tests for AEM‑specific behavior, and optional functional/UI tests wired into the pipeline. This significantly reduces surprises in Stage and Production.”

**Visual guidance:**  

> Generate a testing pyramid graphic with three layers labeled “UI / Functional Tests”, “Integration Tests”, and “Unit Tests”, with an arrow from the pyramid to a “Cloud Manager Pipeline” icon.

**References:**  

- [Java Functional Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/java-functional-testing)  
- [UI Testing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/functional-testing/ui-testing)

------

### Slide 19 – Front-End Build & UI Testing

**Title:**
Front-End Build & UI Testing

**Slide content:**

- `ui.frontend` responsibilities
  - Modern front‑end toolchain (Webpack, npm)
- Output
  - Compiled CSS/JS integrated as clientlibs
- UI test suite (e.g. Cypress)
  - Runs in `ui.tests` module; executed in pipeline
- Best practice
  - Keep UI tests focused on critical paths & regressions

**Speaker notes:**
“Front‑end and tests are first‑class citizens: the archetype gives you a front‑end module and a place for UI tests. These can be integrated into Cloud Manager to gate deployments on end‑to‑end behavior.”

**Visual guidance:**  

> Create a flowchart: “Front-end Code” → “Webpack Build (ui.frontend)” → “Clientlibs” → “Browser”, with a separate branch “UI Tests (Cypress)” feeding into “Cloud Manager CI/CD Pipeline”.

**Reference:**  

- [Front-End Development with the AEM Project Archetype](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/front-end)

------

### Slide 20 – External Integrations Pattern

**Title:**
External Integrations: Common Pattern

**Slide content:**

- Service user + OSGi service for integration
- Config via OSGi/environment variables
- HTTP client
  - Use Adobe HTTP client / best practices
- Error handling & resiliency
  - Timeouts, retries, circuit breakers where needed
- Observability
  - Logging & metrics for each integration

**Speaker notes:**
“Most integrations follow the same template: a dedicated OSGi service with its own config and service user, using a robust HTTP client and careful error handling. Treat each external dependency as potentially slow or unreliable.”

**Visual guidance:**  

> Generate a sequence diagram-style illustration showing “AEM Component/Sling Model” → “Integration Service (OSGi)” → “External API (e.g., HR, translation)”, with error/timeout icons on the external side and logging icons inside AEM.

**Reference:**  

- [Generating access tokens for server-side APIs](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis)

------

### Slide 21 – Headless Content: Content Fragments & Models

**Title:**
Content Modeling with Content Fragments

**Slide content:**

- **Content Fragment Models**
  - Define structured content types (e.g. Job, Event, Location)
- **Content Fragments**
  - Instances of models, reusable across channels
- Stored in `/content/dam` with model in `/conf`
- Decouples content from page structure

**Speaker notes:**
“Content Fragments let you model business entities as structured content: jobs, events, locations, etc. Authors work with these fragments, and code can render them on web pages or expose them to other channels via APIs.”

**Visual guidance:**  

> Create a diagram with a “Content Fragment Model: Job” box (fields: title, description, location, date) and multiple “Job CF” instances beneath it, each feeding both a “Website” and a “Mobile/App” endpoint.

**Reference:**  

- [Content Fragments – Setup](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/setup)

------

### Slide 22 – GraphQL & Persisted Queries

**Title:**
GraphQL API & Persisted Queries

**Slide content:**

- AEM GraphQL API (read‑only)
  - Fetches Content Fragments as JSON
- **Persisted queries**
  - Predefined, cached GET endpoints
  - Secure & CDN‑friendly
- Usage patterns
  - Server‑side consumption in components
  - Direct consumption by external apps

**Speaker notes:**
“GraphQL is the primary API for Content Fragments. Persisted queries are the recommended pattern: they are versioned, cacheable, and easier to secure than ad‑hoc GraphQL POSTs.”

**Visual guidance:**  

> Generate an API diagram: “GraphQL Persisted Query” endpoint at AEM Publish, serving JSON to both “AEM Component” and “External App”. Indicate CDN and Dispatcher in front with cache icons.

**References:**  

- [AEM GraphQL API for use with Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/content-fragments)  
- [Persisted GraphQL queries](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql-api/persisted-queries)

------

### Slide 23 – Dispatcher & CDN Overview

**Title:**
Dispatcher & CDN: Multi-Layer Caching

**Slide content:**

- Adobe‑managed **CDN** at the edge
- **Dispatcher** (Apache module)
  - Cache of rendered pages & assets
  - Security layer (filters, URL handling)
- Publish tier behind Dispatcher
- Cache invalidation
  - HTTP headers + cache flush on publish/activation

**Speaker notes:**
“Dispatcher plus CDN give you multiple layers of caching and protection. A key part of operating AEMaaCS is understanding what’s cached where and how invalidation works when content changes or new code is deployed.”

**Visual guidance:**  

> Use the diagram from Experience League’s content delivery docs as inspiration.
> Or generate: Browser → CDN → Dispatcher → AEM Publish, with cache icons on CDN and Dispatcher, and labels for ‘Cache hit’ and ‘Origin request’.

**References:**  

- [Content Delivery Flow](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/overview)  
- [AEM as a Cloud Service caching](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/overview)

------

### Slide 24 – Dispatcher Configuration in the Project

**Title:**
Dispatcher Configuration as Code

**Slide content:**

- `dispatcher` module in repo
  - `conf.d`, `conf.dispatcher.d`, vhosts, filters, cache rules
- Validated via **Dispatcher Tools SDK**
  - Local Docker image + validator
- Cloud Manager
  - Fails pipeline if config invalid
- Best practices
  - Start from archetype defaults
  - Restrictive filters; explicit whitelisting

**Speaker notes:**
“Dispatcher config is versioned and validated just like application code. Cloud Manager will not deploy a broken Dispatcher configuration. You should use the SDK and validator locally before pushing changes.”

**Visual guidance:**  

> Generate an illustration of the dispatcher folder structure in a code-editor style, with `filters.any`, `vhosts`, and `cache` configs highlighted, plus a “Validator” badge.

**References:**  

- [Configuring Dispatcher when moving to AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/dispatcher)  
- [Dispatcher Configurations in Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/en/docs/events/tech-sessions/2025/dispatcher-configurations)  
- [Cloud 5 – AEM Dispatcher Validator](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/expert-resources/cloud-5/cloud5-aem-dispatcher-validator)

------

### Slide 25 – Indexing & Query Best Practices (Optional / Add-On)

**Title:**
Indexing & Query Best Practices (AEMaaCS)

**Slide content:**

- Oak indices for performance
  - Customize OOTB indices (e.g. `damAssetLucene`) carefully
- Custom index definitions
  - Only to support frequent, stable queries
- Anti‑patterns
  - Unbounded queries, `LIKE '%text%'`, path=“/”
- Tools
  - Query Debugger, Explain Query, slow query logs

**Speaker notes:**
“Search performance is index performance. Only customize or create indices when you have a clear, frequent query to support. Use the built‑in tools (Query Debugger, Explain) to validate that queries hit the right index and avoid full repository scans.”

**Visual guidance:**  

> Generate a conceptual diagram: “Content Repository” with multiple index nodes (e.g., `damAssetLucene`, `customPageIndex`), and arrows from “Queries” to the matching index. Add a warning icon next to “Query without index”.

**References:**  

- [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [Query and indexing best practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)

------

### Slide 26 – Troubleshooting: Local SDK & IDE

**Title:**
Troubleshooting in IDE & Local SDK

**Slide content:**

- Reproduce issues **locally** when possible
- Use IDE (IntelliJ/Eclipse)
  - Debugging, breakpoints, unit tests
- Local logs
  - `error.log`, custom loggers
- Fast feedback
  - Validate fixes before pushing to shared environments

**Speaker notes:**
“Your first line of defense is always your local SDK and IDE. Reproduce the problem locally, attach a debugger, and iterate quickly. Only after you have a solid hypothesis should you move to RDE or Dev in the cloud.”

**Visual guidance:**  

> Generate an illustration of a developer workstation with IntelliJ open, showing a Java file with a breakpoint, and a terminal tailing an AEM `error.log`, with an arrow labeled “Local AEM SDK”.

**Reference:**  

- [Other tools for debugging AEM SDK](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/other-tools)

------

### Slide 27 – Troubleshooting: Developer Console & Logs

**Title:**
Troubleshooting with Developer Console & Logs

**Slide content:**

- **Developer Console**
  - Bundles, OSGi configs (read‑only), Sling models, health checks
- **Logs in Cloud Manager**
  - Download or stream per environment & tier
- Pattern for issues
  - Reproduce in Dev → inspect logs → narrow scope → fix → redeploy

**Speaker notes:**
“In AEMaaCS, Developer Console and logs are your windows into the running application. Dev Console shows how your bundles and models are seen by the runtime; logs give the behavior. Together they replace the old Web Console/CRX‑DE style of debugging.”

**Visual guidance:**  

> Generate a dashboard-like mockup showing a browser window labeled “Developer Console” with tabs for “Bundles”, “Configurations”, “Logs”, and a separate panel showing a log file with highlighted error lines.

**References:**  

- [Debugging AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/overview)  
- [Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)  
- [Logging for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/logging)

------

### Slide 28 – Development Guardrails in AEMaaCS

**Title:**
Development Considerations for AEMaaCS

**Slide content:**

- No local filesystem persistence
  - Use JCR, external storage, or AEP
- Cluster‑safe logic
  - Avoid node‑local state; idempotent schedulers
- Performance
  - Cache aggressively, avoid unindexed queries
- Operations
  - Feature toggles in config, not ad‑hoc runtime changes

**Speaker notes:**
“Cloud Service pushes you towards clean, stateless, horizontally scalable code. The main pitfalls are relying on local filesystem or node‑local state, and shipping code that depends on runtime tweaks. Treat configs as code and design everything to tolerate scale and restarts.”

**Visual guidance:**  

> Create a “Do / Don’t” checklist graphic with green ticks for “Stateless”, “Cluster-safe”, “Config-as-code” and red crosses for “Write to local FS”, “Node-local caches”, “Manual runtime edits”.

**Reference:**  

- [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)

------

### Slide 29 – Change & Release Management

**Title:**
Change & Release Management in AEMaaCS

**Slide content:**

- Branching model
  - Feature branches → `develop` → `main`
- Pipelines
  - Non‑prod pipeline: Dev deployments, quality gates
  - Prod pipeline: Stage + Prod deployments
- Governance
  - PRs, code reviews, testing gates, approvals

**Speaker notes:**
“Your branching strategy and pipeline configuration together form your release process. Typical patterns: feature branches merge into `develop` for Dev deployments; `main` feeds the production pipeline. Cloud Manager’s quality gates and approvals enforce governance.”

**Visual guidance:**  

> Generate a Git branching diagram: multiple feature branches merging into `develop`, then into `main`, with arrows from `develop` to “Dev Pipeline” and from `main` to “Prod Pipeline (Stage+Prod)”.

**References:**  

- [Use the CI/CD Pipeline in Adobe Cloud Manager](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/cloud-manager/use-the-cicd-pipeline-in-cloud-manager-for-aem)  
- [Configure pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/devops/configure-pipelines)

------

### Slide 30 – Identity & Access: IAM to AEM

**Title:**
Identity & Access: Admin Console → AEM Groups

**Slide content:**

- IMS users & groups in **Admin Console**
  - Assigned to AEM product profiles (Users/Admins)
- Mapping to AEM groups
  - Product profile ↔ AEM group mapping
- Pattern
  - Manage membership in Admin Console
  - Use AEM groups for permissions & roles

**Speaker notes:**
“AEMaaCS relies on Adobe IMS for identity. You manage who is an author, admin, or developer in Admin Console; AEM groups then define what those roles can do inside the repository and UI.”

**Visual guidance:**  

> Generate a mapping diagram: “IMS User Groups (Admin Console)” → “Product Profiles (AEM Users/Admins)” → “AEM Groups (Authors, Approvers, Admins)” → “Permissions on /content and /conf”.

**References:**  

- [Assigning AEM Product Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem)  
- [Configuring access to AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/accessing/overview)

------

### Slide 31 – AEM Permissions & Authoring Roles

**Title:**
AEM Permissions & Authoring Roles

**Slide content:**

- AEM groups represent roles
  - Authors, Approvers, Admins, Integrators
- Permissions via ACLs
  - Read/Write/Replicate at `/content`, `/conf`, `/dam`
- Best practices
  - Least privilege; role‑based groups; avoid direct user ACLs

**Speaker notes:**
“Once IMS users are inside AEM, groups and ACLs determine what they can see and do. It’s important to assign permissions to groups representing stable roles, rather than directly to individuals.”

**Visual guidance:**  

> Create a simple matrix: rows as “Roles” (Author, Approver, Admin) and columns as “Areas” (/content, /conf, /dam, /useradmin), checkmarks representing access levels.

**Reference:**  

- [Projects & roles as an authoring reference](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/projects/overview)

------

### Slide 32 – Cloud Manager Environment Types

**Title:**
Cloud Manager Environment Types

**Slide content:**

- **Production & Stage**
  - Tied to Production pipeline
- **Development**
  - Non‑prod pipelines, integration, QA
- **RDE**
  - Rapid Development Environment for fast deploy/test
- **Specialized Testing**
  - Load/stress, advanced validation

**Speaker notes:**
“Not all environments are equal. Prod and Stage are tightly governed; Dev and RDE are where most development and testing activities happen. Specialized Testing environments are for edge cases like performance and load tests under near‑prod conditions.”

**Visual guidance:**  

> Generate a grid of environment cards: Dev, Stage, Prod, RDE, Specialized Testing, each with a short label and small icon (lab flask for RDE, shield for Prod, etc.).

**Reference:**  

- [AEM Champion Tips and Tricks – Cloud Manager Environment Types](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/expert-resources/aem-champions/environment-types)

------

### Slide 33 – Rapid Development Environments (RDE)

**Title:**
Rapid Development Environments (RDE)

**Slide content:**

- Purpose
  - Fast cloud‑side validation after local SDK
- Deployment
  - `aio aem:rde` push of near‑final code
- Best practice
  - Use RDE for integration and acceptance checks
  - Promote through pipelines once validated

**Speaker notes:**
“RDEs give you a near‑production runtime with minimal friction. They are not a replacement for pipelines but a complement: you validate quickly here, then rely on pipelines for full checks and promotion.”

**Visual guidance:**  

> Create a mini-flow: “Local SDK” → “RDE (fast deploy)” → “Dev/Stage via pipelines” → “Prod”, with the RDE box highlighted as a fast feedback loop.

**Reference:**  

- [How to set up Rapid Development Environment](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/how-to-setup)

------

### Slide 34 – Monitoring & Operations

**Title:**
Monitoring & Operations in Cloud Manager

**Slide content:**

- Environment dashboards
  - Health metrics, error rates, resource usage
- Logs access
  - Download or stream per environment/tier
- Alerts & notifications
  - Performance test results, pipeline failures, errors
- Role of Dev & Ops teams
  - Shared responsibility for observability

**Speaker notes:**
“Cloud Manager gives you environment‑level dashboards and log access, but your teams own interpreting the signals. Build a habit of checking dashboards and logs regularly, not just when things break.”

**Visual guidance:**  

> Generate a dashboard mockup with charts for response time, error rate, CPU/memory, and a log panel, labeled “Cloud Manager Reports”.

**Reference:**  

- [Understand Adobe Cloud Manager (monitoring & reports)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/cloud-manager/understand-cloud-manager-for-aem)

------

### Slide 35 – Q&A and Further Resources

**Title:**
Q&A and Further Resources

**Slide content:**

- Open Q&A
  - Architecture
  - Development patterns
  - DevOps workflows
- Recommended resources
  - AEMaaCS overview & architecture
  - Local development & debugging
  - Cloud Manager CI/CD playlists
- Next steps
  - Deep‑dives: components, indexing, integrations, dispatcher

**Speaker notes:**
“Use this slide as a parking lot for topics that came up earlier and to connect people with self‑serve resources. We can also discuss which areas you want to prioritize for deeper dives in follow‑up sessions.”

**Visual guidance:**  

> Create a simple closing slide visual: a question mark icon next to an abstract cloud/architecture icon, with clean white background and subtle Adobe red accents.

**References (for this slide):**

- [AEM as a Cloud Service videos and tutorials](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/overview)  
- [AEM development playlists](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/playlists/development)  
- [Debugging AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/overview)