# SHRSS Technical Design — Backend Architecture

**Layer:** Backend (core bundle + OSGi configuration)  
**Purpose:** Structural architecture of the Java backend: what exists, what each part owns, and dependency boundaries.

---

## 1. Core Bundle Overview

**Module:** `core` (OSGi bundle — `com.shrss.core`)  
**Build:** Maven  
**Target:** AEMaaCS  
**Source:** `core/` at repository root

The core bundle contains backend business logic, data access, integrations, and Sling Models used by HTL components. It uses OSGi Declarative Services and follows interface-plus-implementation separation for services.

### Package Distribution

*Counts below reflect the current codebase (post–Unity cleanup).*

| Package | Count | Primary role |
|---------|-------|--------------|
| models | 155 | Sling Models for HTL component data (interfaces + impl in `models/` and `models/impl/`) |
| services | 8 | OSGi service implementations (in `services/impl/`; business logic, integrations, config) |
| servlets | 20 | HTTP endpoints and JSON APIs (servlets package: 18 servlet classes + 2 support classes, e.g. JSONComponent) |
| utils | 6 | Utility classes and helpers (CFCardUtils, SHRSSUtils, TagUtils, LinkUtils, GraphQLUtils, CFCardListUtils) |
| filters | 3 | Sling filters (LoggingFilter, CFFilter; CustomRequestWrapper is support) |
| bean | 4 | DTOs and data transfer objects (CFCardResults, Jobs, PageData, ReservationData) |
| schedulers | 2 | Background jobs (LocationExportScheduler, LocationsDataExportJobConsumer) |
| commerce | 2 | Commerce/marquee model (MarqueeModel, MarqueeModelImpl in `commerce/models/`; Unity code removed or in cleanup) |
| listeners | 1 | Event listener (ActivateServiceEventHandler) |
| config | 1 | Configuration (GoogleMapConfig) |
| constants | 1 | Application constants (SHRSSConstants) |
| caconfig | 1 | Context-Aware Configuration (TealiumConfig) |
| workflows | 1 | AEM Workflow process step (EventIdCreationProcess) |

**OSGi configurations:** Multiple configs in the **ui.config** module, correlated by runmode and service PID.

---

## 2. Architectural Patterns

### 2.1 Service Pattern

- **Interface:** `core/src/main/java/com/shrss/core/services/<ServiceName>.java`
- **Implementation:** `core/src/main/java/com/shrss/core/services/impl/<ServiceName>Impl.java`
- **OSGi config:** `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/config[.runmode]/<ServicePID>.cfg.json`

Example: `TagsPathMappingConfigService` (interface), `TagsPathMappingConfigServiceImpl` (impl), with a matching `.cfg.json` in ui.config.

### 2.2 Sling Model Pattern

- Models adapt `Resource` or `SlingHttpServletRequest` to Java objects for HTL.
- Common injectors: `@ValueMapValue`, `@ChildResource`, `@OSGiService`, `@Self`, `@SlingObject`.
- Models are read-only for content; business logic is delegated to services.

### 2.3 Configuration Pattern (AEMaaCS)

- OSGi configurations are **immutable** and **source-code based** (in ui.config).
- Deployed via Cloud Manager; no runtime changes via Felix Console.
- Runmode folders: `config`, `config.author`, `config.publish`, `config.dev`, `config.stage`, `config.prod`.
- Preferred format: `.cfg.json`.

---

## 3. Package-Level Summary

### 3.1 models

- **Purpose:** Expose content and data to HTL (component models, exporters, injectors).
- **Constraints:** Stateless; no JCR writes; delegate business logic to services; use `@PostConstruct` for initialization.

### 3.2 services

- **Purpose:** Business logic, integrations, data access, configuration.
- **Count:** 8 OSGi service implementation classes in `core/src/main/java/com/shrss/core/services/impl/` (e.g. JobsContentFragmentConfigServiceImpl, NewsSearchConfigImpl, PageJSONServletServiceImpl, SitemapServiceImpl, TagsPathMappingConfigServiceImpl, ThirdPartyURLConfigurationServiceImpl). The `services` package also contained a `unityapi` subpackage (Unity API POJOs and related classes); that Unity API code was never fully implemented and is being removed as part of cleanup.
- **Domains (examples):** Content Fragment config (jobs, news search), sitemap generation, page JSON, third-party URL configuration, tags path mapping.
- **Constraints:** Idempotent where applicable for cloud; close ResourceResolvers; use service users where appropriate.

### 3.3 servlets

- **Purpose:** HTTP endpoints for AJAX, JSON APIs, form submissions.
- **Patterns:** Path-based or resource-type-based registration; selector-based routing (e.g. `.json`).
- **Constraints:** Thread-safe (no mutable instance state); set appropriate cache headers; handle errors and return consistent JSON where applicable.

### 3.4 filters

- **Purpose:** Request/response interception (logging, security headers, validation, CORS).
- **Constraints:** Performant; fail gracefully; use appropriate filter scope and ranking.

### 3.5 listeners

- **Purpose:** Event-driven logic (JCR, OSGi, workflow, replication).
- **Constraints:** Idempotent where events may repeat; close ResourceResolvers; avoid blocking JCR operations.

### 3.6 schedulers

- **Purpose:** Background jobs (e.g. location export, asset cleanup) via cron or Sling Jobs.
- **Constraints:** Idempotent for concurrent execution in cloud; use Sling Jobs for long-running work; close ResourceResolvers.

### 3.7 workflows

- **Purpose:** AEM Workflow process steps. One implementation: **EventIdCreationProcess** (event ID creation).
- **Constraints:** Idempotent; use workflow sessions; handle partial failures and log progress.

### 3.8 bean, utils, config, constants, caconfig, commerce

- **bean:** DTOs (e.g. CFCardResults, GraphQLResponse, LocationData).
- **utils:** Stateless helpers (e.g. DateUtils, PathUtils, JsonUtils); no OSGi dependencies.
- **config / constants / caconfig:** GoogleMapConfig (config), SHRSSConstants (constants), TealiumConfig (caconfig).
- **commerce:** MarqueeModel and MarqueeModelImpl in `commerce/models/` (marquee component). Unity-related code was never fully implemented and is being removed as part of cleanup.

---

## 4. OSGi Configuration (ui.config)

- **Location:** `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/`
- **Organization:** By runmode (`config`, `config.author`, `config.publish`, `config.dev`, `config.stage`, `config.prod`).
- **Important configs (examples):**
  - Service user mappings: `org.apache.sling.serviceusermapping.impl.ServiceUserMapperImpl.amended~shrss.cfg.json`
  - Repository initializers (author/publish): `org.apache.sling.jcr.repoinit.RepositoryInitializer~shrss.cfg.json`
  - CORS: `com.adobe.granite.cors.impl.CORSPolicyImpl.cfg.json`
  - Externalizer: `com.day.cq.commons.impl.ExternalizerImpl.cfg.json`
- **Patterns:** PID-based configs; factory configs use `~<name>`; amended configs use `.amended~<name>`.

---

## 5. Integration Tests

- **Module:** `it.tests`
- **Framework:** AEM Testing Clients.
- **Execution:** Cloud Manager pipeline (Custom Functional Testing step).
- **Location:** `it.tests/` at repository root.

---

## 6. Recent Codebase Additions (Post–Analysis)

The following are examples of backend changes after the baseline analysis; the codebase may have further updates.

- **CFCardUtils** — Utility used in conjunction with CFCard/cfcard component and Content Fragment card behavior.
- **TestServlet** — Exists in core; usage and lifecycle should be aligned with environment and deployment policy.
- **Removed:** Some test classes (e.g. VimeoImplTest, CoreComponentTestContext) and committed `core/bin` output; build and test run from source.

When extending or refactoring the backend, correlate new or changed classes with the appropriate package (models, services, servlets, etc.) and with ui.config if new OSGi config is required.

---

## 7. Dependency Direction

- **Allowed:** HTL → Sling Models → OSGi services → JCR / external APIs; models and servlets may use utilities.
- **Avoid:** Services depending on Sling Models; models depending on servlets; utilities depending on OSGi services.

---

*For runtime behavior and request flows, see `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md`. For external systems, see `SHRSS_Technical_Design_03_Integrations.md`.*
