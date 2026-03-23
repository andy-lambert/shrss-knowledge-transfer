# SHRSS AEM Best Practices Library

This folder contains the SHRSS AEM as a Cloud Service best‑practices library, organized by role and depth of responsibility.  
All documents are intended as **deskside references** and **training material for agentic services**.

> Folder: `SHRSS-AEM-Best-Practices/`  
> Output format: PDFs generated from the corresponding Markdown sources using `SHRSS_Adobe_Word_Template.docx`.

---

## 1. Volumes Overview

- **All Roles – Platform & Shared Practices**  
  `./SHRSS-AEM-Best-Practices-All-Roles.pdf`

- **Engineering – Developers & Technical Architects**  
  `./SHRSS-AEM-Best-Practices-Engineering-Developers-and-Technical-Architects.pdf`

- **Admin & DevOps – Operations, SRE, Platform Engineering**  
  `./SHRSS-AEM-Best-Practices-Admin-and-DevOps.pdf`

- **Authors – Content Authors, Content Designers, Product Owners**  
  `./SHRSS-AEM-Best-Practices-Authors.pdf`

- **DAM – DAM Architects, Librarians, Asset Stewards**  
  `./SHRSS-AEM-Best-Practices-DAM.pdf`

Each PDF goes deeper than Experience League, but **anchors to public docs** for terminology and conceptual alignment.

---

## 2. SHRSS-AEM-Best-Practices-All-Roles.pdf

**Path:** `./SHRSS-AEM-Best-Practices-All-Roles.pdf`

### 2.1 Purpose

This is the **platform-wide reference**. It provides:

- Core AEMaaCS concepts (architecture, multi‑tenant model, immutable runtime, content repository).
- Cross‑cutting best practices that apply to **all roles**:
  - Security, IAM, permissions and governance.
  - Content modeling concepts shared across Jobs, Events, News, Locations, Careers, etc.
  - Indexing & performance basics (with deeper details in the engineering + admin volumes).
  - Common terminology and SHRSS domain language.
- **SHRSS‑specific overlays** that explain how the general principles are applied in:
  - SHRSS Jobs/Events/Careers/News/Locations/Shared Data.
  - SHRSS authoring experience and component library.
  - SHRSS indexing and caching strategy.

### 2.2 Recommended audience

- All technical stakeholders (devs, architects, admins).
- Product owners, content leads, DAM stewards who need a **big‑picture view**.
- Any agentic service that needs a **canonical understanding of the SHRSS platform**.

### 2.3 How other volumes relate

- **Engineering volume** extends the "Development & Indexing" concepts from this all‑roles volume with deeper code‑level practices and examples.
- **Admin & DevOps volume** extends the "Operations & Governance" chapters (Cloud Manager, RDEs, pipelines, observability).
- **Authors volume** deepens the "Authoring & UX" portion with component‑level tips, workflows, and editorial patterns.
- **DAM volume** deepens the DAM/metadata chapters and applies them to SHRSS's Jobs/Events/News/Locations asset flows.

---

## 3. SHRSS-AEM-Best-Practices-Engineering-Developers-and-Technical-Architects.pdf

**Path:** `./SHRSS-AEM-Best-Practices-Engineering-Developers-and-Technical-Architects.pdf`

### 3.1 Purpose

This is the **deep technical volume** for:

- Back‑end & front‑end developers.
- Technical architects and lead engineers.
- Anyone designing or reviewing AEMaaCS solutions and integrations for SHRSS.

It includes:

- **AEM technology stack deep dive**  
  Sling, OSGi, JCR/Oak, Granite; how these surface in AEMaaCS with containerization and shared data stores.

- **AEMaaCS development principles**  
  - Stateless + cluster‑aware patterns.
  - Immutability and separation of code vs content.
  - Run modes, OSGi config patterns (`ui.config`, environment variables, secrets).

- **Component & template best practices**  
  - HTL & Sling Model patterns (and anti‑patterns).
  - Core Components extension strategy and how SHRSS uses them across Jobs, Events, Careers, News, Locations.
  - Layout, policies, and responsive behavior from an engineering perspective.

- **Indexing & query design**  
  - Oak index internals, Lucene vs property indexes, ordered properties.
  - Customizing OOTB indexes (`damAssetLucene`) and adding project‑specific ones.
  - Anti‑patterns that cause performance issues and pipeline violations.
  - Mapping SHRSS query patterns (Jobs search, Events, News, Location proximity) to index definitions.

- **Integration & API practices**  
  - External systems (Workday, TransPerfect, mapping, reservations, etc.).
  - Patterns for robust, observable, fault‑tolerant integrations.
  - Patterns for headless/API consumers using CF + GraphQL.

- **Testing & quality**  
  - Unit, integration, and UI testing patterns wired into Cloud Manager.
  - How to structure tests around SHRSS's modules and domain model.

### 3.2 SHRSS-specific overlay

This volume includes a **dedicated "SHRSS Overlays" chapter** that:

- Maps **SHRSS domain models** (Jobs, Events, Locations, News, Careers, Shared Data) to:
  - CF model structures & relationships.
  - Index design decisions.
  - Custom Sling Models & components.
- Walks through **real SHRSS examples**:
  - A Jobs listing query and its custom index definition.
  - An Events listing driven by CFs and GraphQL.
  - A Location search with facets or geo‑like filters.
- Documents **custom code patterns**:
  - Shared libraries/utilities used across SHRSS features.
  - Custom validators, schedulers, workflows, and integration services.

### 3.3 How to use this volume

- As the **primary deskside reference** for engineers implementing or refactoring SHRSS features.
- As core source material for **agentic code assistants** working on SHRSS repos.
- In combination with:
  - `SHRSS-AEM-Best-Practices-All-Roles.pdf` for shared concepts.
  - `SHRSS-AEM-Best-Practices-Admin-and-DevOps.pdf` when designing deployment & operational characteristics of code.

---

## 4. SHRSS-AEM-Best-Practices-Admin-and-DevOps.pdf

**Path:** `./SHRSS-AEM-Best-Practices-Admin-and-DevOps.pdf`

### 4.1 Purpose

This is the **operations and platform engineering volume**, aimed at:

- AEM administrators and platform owners.
- DevOps / SRE / Cloud engineers.
- Technical architects responsible for **environments, pipelines, security, observability**, and **incident response**.

It covers:

- **Environment model & topology**  
  - Dev, Stage, Prod, RDEs, specialized environments.
  - How Author/Publish/Preview, CDN, and Dispatcher work together in AEMaaCS.

- **Cloud Manager & CI/CD**  
  - Pipeline types and steps.
  - Quality gates (code quality, security, performance).
  - Promotion flows and rollback strategies.

- **Security & access control**  
  - Admin Console IAM → Product profiles → AEM groups & permissions.
  - SHRSS role mappings (authors, approvers, admins, technical accounts).

- **Operations & observability**  
  - Logs, metrics, Developer Console.
  - Troubleshooting workflows for slow pages, errors, cache issues.
  - Backup/restore, content copy, and operational constraints in AEMaaCS.

- **Indexing & performance (Ops view)**  
  - How to monitor index health and query performance.
  - How to respond to "query without index" alerts and performance regressions.
  - Operational side of deploying new/changed index definitions reliably.

### 4.2 SHRSS-specific overlay

The Admin/DevOps volume includes an overlay section that:

- Documents **SHRSS environment topology** (per environment) and:
  - Intended usage per environment.
  - Which SHRSS features are enabled/tested where.
- Captures **SHRSS Cloud Manager setup**:
  - Branch → pipeline mapping (how code flows to DEV/STAGE/PROD).
  - Where integration tests/UI tests run for SHRSS features.

- Provides **incident response playbooks** specific to SHRSS:
  - Jobs/Events pages loading slowly or returning incomplete results.
  - Search/index issues impacting Jobs/News/Locations.
  - Problems with external integrations affecting content or author experiences.

- Clarifies **operational guardrails**:
  - What SHRSS admins are allowed to change directly vs what must go through code.
  - How SHRSS‑specific configs (e.g., external endpoints, feature toggles) are managed per environment.

### 4.3 How to use this volume

- As the **runbook and governance reference** for administrators and SREs.
- As training base for **agentic operations assistants** (e.g., pipeline triage bots).
- In conjunction with:
  - `SHRSS-AEM-Best-Practices-Engineering-Developers-and-Technical-Architects.pdf` to understand how code decisions impact operations.
  - `SHRSS-AEM-Best-Practices-All-Roles.pdf` for shared concepts.

---

## 5. SHRSS-AEM-Best-Practices-Authors.pdf

**Path:** `./SHRSS-AEM-Best-Practices-Authors.pdf`

### 5.1 Purpose

This volume is for:

- Content authors.
- Content designers and UX writers.
- Product owners who curate and review content.

It goes **beyond standard Experience League author docs** with:

- **Practical authoring workflows** for:
  - Jobs, Events, Careers, News, Locations, Shared Data.
  - Dynamic listings driven by filters, searches, and shared data.

- **Core Components tips & tricks**  
  - Component‑level nuances and "pro" authoring patterns.
  - Common pitfalls and how to avoid them (e.g., overusing rich text, misusing layout).

- **Template & policy usage in SHRSS**  
  - How SHRSS templates and policies constrain/enable authoring.
  - What can be adjusted with configuration vs what requires development.

- **Content Fragment authoring**  
  - Job/Event/Location/News CFs and how to maintain consistency.
  - Best practices for structured content, reuse, and headless scenarios.

### 5.2 SHRSS-specific overlay

The author volume includes a rich overlay section that:

- Walks through **real SHRSS pages and content types**:
  - Jobs/Careers: how to create, update, and retire job postings; how Jobs tie into listing pages and search.
  - Events: how to create event content, control visibility, and manage past vs upcoming events.
  - News: how to publish news items, manage promotion positions, and link related content.
  - Locations: how to keep location information consistent and accurate.
  - Shared Data: how to use shared data sources to avoid duplication and ensure consistency across pages.

- Provides **pattern‑based guidance**, e.g.:
  - "If you want X, use Y component with configuration Z."
  - "Avoid doing A, instead use B and C for better maintainability."

- Highlights **authoring anti‑patterns** and their consequences:
  - Overriding shared components with one‑off configuration.
  - Embedding structural layout within RTE content.
  - Overuse of manual "linking" instead of shared references.

### 5.3 How to use this volume

- As the **primary training/enablement asset** for new SHRSS authors.
- As a **just‑in‑time deskside reference** for solving day‑to‑day authoring problems.
- As a specification for **agentic author helpers** (e.g., prompt‑driven bots that guide authors through component selection and content modeling).

---

## 6. SHRSS-AEM-Best-Practices-DAM.pdf

**Path:** `./SHRSS-AEM-Best-Practices-DAM.pdf`

### 6.1 Purpose

This volume is for:

- DAM architects and librarians.
- Asset managers and producers.
- Any role responsible for **asset structure, metadata, and governance**.

It provides deep guidance on:

- **DAM information architecture**  
  - Folder structures and conventions for SHRSS assets (supporting Jobs, Events, News, Locations, Careers).
  - How assets relate to pages, CFs, and shared data.

- **Metadata & taxonomy**  
  - What to capture, where, and how it's used in SHRSS (e.g., BY department, location, campaign, usage rights).
  - Governance for tags and controlled vocabularies.

- **Renditions & performance**  
  - Rendition usage patterns for SHRSS components.
  - Best practices for optimizing asset size vs quality.

- **Lifecycle & governance**  
  - Ingestion, review, approval, and archival processes.
  - Rights management, expiration, and auditability.

### 6.2 SHRSS-specific overlay

The DAM volume includes overlays that:

- Map **SHRSS content domains** (Jobs/Events/News/Locations) to:
  - Expected asset types (hero images, thumbnails, icons).
  - Required metadata/fields critical for search and filtering.
- Document **SHRSS-specific tagging schemes** and how they are expected to be used by:
  - Authors (for search and display).
  - Integrations (e.g., export to other systems).
- Provide **real examples**:
  - How a News image should be set up (naming, folder, metadata) to appear correctly in all its contexts.
  - How Job or Event imagery is managed, reused, and retired.

### 6.3 How to use this volume

- As a **governance playbook** for managing SHRSS DAM.
- As reference for **DAM automation and agentic services** (e.g., bots that suggest tags or detect misfiled assets).
- Together with:
  - `SHRSS-AEM-Best-Practices-Authors.pdf` for end‑to‑end content + asset workflows.
  - `SHRSS-AEM-Best-Practices-All-Roles.pdf` for high‑level metadata and taxonomy intent.

---

## 7. Recommended Reading Order

For a new team member:

1. **All‑roles overview**  
   - `./SHRSS-AEM-Best-Practices-All-Roles.pdf`
2. Then role‑specific deep dive:  
   - Developer/architect → `./SHRSS-AEM-Best-Practices-Engineering-Developers-and-Technical-Architects.pdf`  
   - Admin/DevOps → `./SHRSS-AEM-Best-Practices-Admin-and-DevOps.pdf`  
   - Author → `./SHRSS-AEM-Best-Practices-Authors.pdf`  
   - DAM → `./SHRSS-AEM-Best-Practices-DAM.pdf`

Agents (LLM‑based services) should also ingest **all volumes** to understand:

- Cross‑cutting constraints (all‑roles volume).
- Role‑specific patterns, anti‑patterns, and SHRSS overlays.

---
