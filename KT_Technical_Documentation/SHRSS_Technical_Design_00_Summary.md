# SHRSS Technical Design — Summary

**SHRSS AEM Sites & Assets**  
**Document:** Summary and navigation  
**Purpose:** High-level overview of the implementation for technical stakeholders taking ownership of the platform.

---

## Platform Overview

The SHRSS implementation is a custom, enterprise-scale web content and digital asset management (DAM) platform built on **Adobe Experience Manager as a Cloud Service (AEMaaCS)**.

- **Sites:** Two Hard Rock web properties are live, one is planned for go-live on March 23, 2026 (Careers); additional site migrations are planned.
- **DAM:** Approximately 500 GB of digital assets are managed in AEM Assets.
- **Live sites:**
  - Hard Rock corporate: https://www.hardrock.com
  - Reverb: https://reverb.hardrock.com
- **In UAT, planned go-live March 23, 2026:**
  - Careers (Stage, customer QA/UAT): https://aem.careers.stage.hardrock.com/

---

## Key Modules and Layers

| Layer / Module | Purpose |
|-----------------|---------|
| **core** | OSGi bundle: Sling Models, OSGi services, servlets, filters, listeners, schedulers, workflows, utilities. Backend business logic and component data. |
| **ui.apps** | FileVault package: AEM authoring components (HTL), clientlib definitions, templates structure. |
| **ui.frontend** | Webpack build: TypeScript/JavaScript, Sass/SCSS compiled into clientlibs and deployed into ui.apps. |
| **ui.content** | FileVault package: Default content, site structure, and **conf** (templates, policies, Content Fragment models, GraphQL persistent queries, metadata schemas). |
| **ui.config** | FileVault package: OSGi configurations (runmode-specific). Immutable in AEMaaCS. |
| **dispatcher** | Apache and AEM Dispatcher configuration (caching, security, routing). Cloud-optimized. |
| **config** | CDN rules and maintenance task configurations. |
| **it.tests** | Integration tests (AEM Testing Clients). Run in Cloud Manager pipeline. |
| **ui.tests** | UI tests (Cypress). Run in Cloud Manager pipeline. |
| **all** | Aggregates other packages for deployment. |
| **acl** | Base user groups and ACLs (Netcentric Access Control Tool). |

---

## Structural Scope (Codebase Counts)

- **Backend (core):** 155 Sling Model classes, 8 OSGi service implementations, 20 servlet-package classes (18 HTTP servlets), 3 filters, 2 schedulers, 1 listener, 1 workflow, 6 utils, 4 bean DTOs, 2 commerce model classes (Marquee); OSGi configs in **ui.config**. (Unity API code is being removed.)
- **UI/Frontend:** 95 custom AEM authoring components, 6 Content Fragment models, clientlibs, page templates, content policies, asset metadata configurations.
- **Dispatcher:** Apache virtual hosts, rewrites, and Dispatcher farm/filter/cache configuration.
- **Request flow (high level):** Browser → CDN (e.g. Cloudflare → Fastly) → Dispatcher → AEM Publish.

---

## Where to Go Next

| If you need… | Read… |
|--------------|--------|
| Backend structure (packages, services, models, servlets, OSGi) | `SHRSS_Technical_Design_01_Backend_Architecture.md` |
| Frontend structure (components, clientlibs, Webpack, conventions) | `SHRSS_Technical_Design_02_Frontend_Architecture.md` |
| External integrations (Workday, DPLT, GraphQL, third-party) | `SHRSS_Technical_Design_03_Integrations.md` |
| Dispatcher and Apache (cache, filters, CDN) | `SHRSS_Technical_Design_04_Dispatcher_Configurations.md` |
| Runtime behavior (request flows, data movement, interactions) | `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md` |

---

## AEMaaCS Conventions (Brief)

- **Configuration:** OSGi configs live in **ui.config** and are immutable at runtime. Environment-specific values use Cloud Manager environment variables or secrets.
- **Scaling:** Services, schedulers, and listeners should be designed for horizontal scaling (e.g. idempotent where applicable).
- **Deployment:** Via Cloud Manager pipelines (build, quality, deploy). No direct runtime edits to `/apps` or `/libs`.

---

*For detailed structural and behavioral documentation, use the documents listed above.*
