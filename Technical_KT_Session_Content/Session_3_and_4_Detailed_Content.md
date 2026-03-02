# Session 3 & 4 — AEM Application Development Parts 3 & 4

**Duration:** 2 hours  
**Presenters:** Andy Lambert, Vinay S A, Deepkamal Narang  
**Agenda reference:** `SHRSS_Technical_KT_Main_Agenda.md`  
**Exercises:** `SHRSS_Technical_KT_Exercises_Supplemental.md` (Session 3 & 4)

---

## AEM Application Development — Part 2 (continued) — 117 min

### Backend (Andy → Vinay) — 38 min

#### Run modes, environment variables and secrets — 5 min

- **Run modes:** AEMaaCS uses run modes (e.g. `author`, `publish`, `dev`, `stage`, `prod`) to select OSGi configs. In repo: `ui.config/.../config.author/`, `config.publish/`, etc. Each environment gets the right config at deploy time; no runtime change.
- **Environment variables and secrets:** Set in **Cloud Manager** per environment (not in repo). Use for API URLs, API keys, feature flags. **Never** commit secrets; use Cloud Manager “Secrets” for sensitive values. Implementation analysis P0: hardcoded credentials in GraphQLUtils (remove and use config/secrets).

**SHRSS-specific:** Reference `01_STRUCTURAL_ARCHITECTURE.md` §1.2.3 Configuration Pattern; `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md` ISSUE-BACKEND-012 (GraphQLUtils).

---

#### Repo initialization — 5 min

- **Repo init:** Scripts that run when the repository is first created or when a runmode is first applied. Used for creating base structure, service users, ACLs, default content. In AEMaaCS, repo init runs during deployment; must be **idempotent** (safe to run multiple times). Pattern: check if node/config exists before creating.
- **Where in SHRSS:** Repo init scripts typically in `core` or a dedicated package; OSGi config points to the script. Reference AGENTS.md idempotency appendix: conditional writes, no blind `addNode` without existence checks.

**SHRSS-specific:** Implementation notes and structural docs; align with acl module and any bootstrap content in `ui.content`.

---

#### OSGi component implementations (servlets, Sling models, services, listeners, schedulers) — 12 min

- **Services:** Interface + impl in `core`; registered as OSGi services. Other services and Sling Models inject via `@Reference` or `@OSGiService`. Used for business logic, integrations, data access. SHRSS: 17 service impls, 94.1% test coverage (exec summary).
- **Servlets:** Sling servlets for HTTP endpoints (JSON APIs, form handlers). Register with `@SlingServletResourceTypes` or path. **Security:** Author-only or sensitive servlets must require authentication; implementation analysis: 4 servlets (DeleteJob, JobsCFUpdate, InvalidateCache, UserDashboard) missing auth — P0.
- **Sling Models:** Covered in Session 1&2; backend exposes them in `core`.
- **Listeners:** JCR/OSGi event listeners; must be idempotent and thread-safe (AEMaaCS can scale horizontally). One listener in SHRSS; test exists but idempotency not validated (Phase 3 finding).
- **Schedulers:** Cron or periodic jobs; must be idempotent (may run on multiple nodes). SHRSS: 2 schedulers; same quality note. **Workflows:** One workflow step; must be idempotent (workflow may retry).

**SHRSS-specific:** `01_STRUCTURAL_ARCHITECTURE.md` §1.1 package distribution (servlets 22, schedulers 3, listeners 2, workflows 1). `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md` for P0/P1 servlet and idempotency issues.

---

#### OSGi configurations (`ui.config`) — 5 min

- **Location:** `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/`. Format: `.cfg.json`. Runmode-specific folders: `config.author`, `config.publish`, etc. PID matches the component (e.g. `com.shrss.core.services.impl.MyServiceImpl.cfg.json`).
- **Immutable in cloud:** Deployed with code; no Felix Console edit. Change config = change repo and redeploy. Use environment variables (Cloud Manager) for env-specific values when possible.

**Repo path:** `ui.config/.../osgiconfig/`. Exercise 2.1 touches JobsContentFragmentConfigService and its config.

---

#### Security & hardening — 8 min

- **Servlet authentication:** Servlets that modify data or expose sensitive operations must require authentication (e.g. Sling auth, resource-based auth). Implementation analysis: **DeleteJobServlet**, **JobsCFUpdateServlet**, **InvalidateCacheServlet**, **UserDashboardServlet** — add auth (P0). Public read-only APIs (e.g. GetJobDetails, EventCalendarData) may stay public but consider rate limiting (P2).
- **Test/debug endpoints:** Remove or protect test servlets in production (ISSUE-BACKEND-020 — 4 test servlets; P0). Disable Groovy Console in production (ISSUE-BACKEND-057; P1).
- **Secrets management:** No hardcoded credentials (ISSUE-BACKEND-012 — GraphQLUtils; P0). Use OSGi config with Cloud Manager secrets or env vars.
- **CDN purge key:** Do not pass purge key in URL query (ISSUE-BACKEND-021); use header or secure config.

**Reference:** `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md`; Optimized SDD Appendix C for servlet auth patterns (author vs publish, member vs public).

---

#### Debugging/troubleshooting and best practices — 3 min

- **Debugging:** Logs via AEM Developer Console or Cloud Manager logs; breakpoints in local/RDE. For servlets: check path/resource type registration and auth.
- **Best practices:** Thin models, logic in services; idempotent listeners/schedulers/workflows; close ResourceResolvers; no instance mutable state in servlets (thread safety). Reference AGENTS.md idempotency appendix.

---

### Frontend (Deep) — 22 min

#### Client libraries (clientlibs) — 5 min

- Recap: Clientlibs defined in `ui.apps`, source in `ui.frontend`. Categories and embed; components request categories. Multi-brand: SHRSS may use different clientlib sets per brand (context-aware or separate categories).

**Repo paths:** `ui.apps/.../clientlibs/`; `ui.frontend/src/`.

---

#### Webpack, NPM, build and deploy into `ui.apps` — 8 min

- **Stack:** Node/npm, Webpack. TypeScript/JS and Sass/SCSS. Build produces JS/CSS that are copied into `ui.apps` clientlib folders (e.g. under `apps/shrss/clientlibs/`). Maven build often invokes `npm run build` in `ui.frontend` and then packages `ui.apps`.
- **Deploy:** Cloud Manager runs full Maven build; frontend build runs as part of it. No separate “frontend pipeline” unless the project has a front-end-only pipeline. Local: run `npm run build` in `ui.frontend` and confirm output in `ui.apps`.

**SHRSS-specific:** Implementation notes — `ui.frontend` uses Node, npm, webpack. Exercise 2.3 — Run frontend build locally (homework).

---

#### Debugging/troubleshooting and best practices — 9 min

- **Debugging:** Browser dev tools; source maps if enabled. Check that the right clientlib category is included and that the built bundle is the one loaded (cache). For author vs publish, different clientlibs may be loaded (e.g. author-only categories).
- **Best practices:** Consistent naming; minimal global scope; avoid blocking main thread; use AEM responsive grid and clientlib categories per breakpoint if applicable. Reference Experience League for client library and frontend best practices.

---

### External integrations (Vinay) — 35 min

#### Workday (jobs sync) — 10 min

- **Purpose:** Jobs data synced from Workday for Careers. Backend services and/or schedulers pull or receive job data and update Content Fragments or other content.
- **Where it lives:** In `core`: search for Workday, jobs sync, or related service names. Configuration (endpoints, credentials) in OSGi config or env vars (no hardcoding). Implementation analysis and cross-layer docs reference jobs and Content Fragments.
- **How invoked:** Likely a scheduler or external callback; document the actual flow from implementation (e.g. `02_CROSS_LAYER_INTERACTIONS.md` or backend staging docs). Emphasize: config-driven, secure (secrets in Cloud Manager).

**Repo paths:** `core/.../services/` (e.g. JobsContentFragmentConfigServiceImpl); related models/servlets (JobListingsImpl, JobDetailsImpl, DeleteJobServlet, JobsCFUpdateServlet). Exercise 2.1 — Find jobs CF integration.

---

#### DPLT (locations/venues) — 8 min

- **Purpose:** Location/venue data from DPLT; used in components (e.g. location listing, venue pages). Data flow: DPLT → backend service → Sling Model or API → component.
- **Where:** Services in `core`; models that consume location data. Config for endpoint/API in `ui.config` or env.
- **Usage:** Components may call a model that uses a DPLT service; or a servlet may expose JSON for headless. Reference cross-layer interactions for “locations” or “venues.”

**Repo paths:** `core/.../services/`, `core/.../models/`; persistent queries such as `locationListing`, `searchVenuLocations`, `franchiseLocations` (exercise supplemental).

---

#### GraphQL — 10 min

- **Persistent queries:** Stored under `conf/shrss/settings/graphql/persistentQueries/` (in `ui.content` or content package). Names: e.g. `getAllJobIds`, `searchLocations`, `getAllEventsDetails`, `getAllPromotionsList`, `newsSearchPaginated`, etc. Queries are invoked from backend (GraphQL client) with query name; no inline query string in production.
- **Headless consumption:** Components or headless clients request data via GraphQL endpoint; backend services call persistent queries. SHRSS uses this for jobs, events, locations, promotions, news.
- **Security/quality:** Implementation analysis: GraphQL syntax error in one query (ISSUE-BACKEND-018 — missing parenthesis; P0). GraphQLUtils hardcoded credentials (ISSUE-BACKEND-012; P0). Fix and use config/secrets.

**Repo paths:** `ui.content/.../conf/shrss/settings/graphql/persistentQueries/`; `core` search for “GraphQL” or query names. Exercise 2.2 — Locate a persistent query.

---

#### Other third-party and where to find integration code — 7 min

- **OpenTable, Grubhub, Google Maps:** Referenced in implementation analysis (external integrations). Likely in `core` (services or models) and possibly frontend (maps UI). Document where each lives: which service, which component, which config.
- **Where to find:** `core/.../services/`, `core/.../models/`; `02_CROSS_LAYER_INTERACTIONS.md` and staging backend/UI interaction docs. Unity API: SDD specified OAuth backend; only iframe exists (critical deviation in exec summary); do not present as fully implemented.

**SHRSS-specific:** `00_EXEC_SUMMARY.md` — External Integrations; Unity placeholder; 10 external integrations in cross-layer. List actual integration points and config locations per repo.

---

### Content Fragments & GraphQL (Vinay / Andy) — 22 min

#### CF models in SHRSS — 8 min

- **Content Fragment models** define the structure of CFs (e.g. jobs, events, locations, venues). Stored in repo (e.g. `conf/.../settings/dam/cfm/models/`) or in content package. SHRSS has 6 CF models (structural architecture).
- **Examples:** Jobs (Careers), events, locations, venues. Models have fields (text, number, fragment reference, etc.). Authoring creates CF instances under `/content/dam/...` (e.g. `/content/dam/shrss/cf` per implementation notes).

**Reference:** Content package paths in task doc; `01_STRUCTURAL_ARCHITECTURE.md` UI section; authoring KT (Gonzalo, TJ, Tim) for author-side CF usage.

---

#### Persistent queries and consumption in components — 8 min

- **Persistent queries:** GraphQL queries registered by name; backend calls them (e.g. via GraphQLUtils or a dedicated service). Components get data via Sling Models that call the service, or via a servlet that returns JSON. Flow: Component → Model/Servlet → GraphQL client → persistent query → AEM GraphQL API.
- **Consumption:** HTL uses model getters that return data from the service; or frontend fetches JSON from a servlet that uses GraphQL. Emphasize: use persistent queries (predefined, cached) not ad-hoc queries; fix syntax and credential issues (P0).

**Repo paths:** Persistent queries in `ui.content/.../persistentQueries/`; consumption in `core` (models, services, servlets). Exercise 2.1 and 2.2.

---

#### Relevance for Careers and future migrations — 6 min

- **Careers:** Jobs and related content use CFs and GraphQL; Careers site is in stage (task doc). Future migrations (11 sites) may reuse CF/GraphQL patterns for headless or hybrid pages.
- **Takeaway:** Understanding CF models, persistent queries, and backend consumption is critical for maintaining and extending Careers and future properties.

**Reference:** Task doc (Careers stage content); `00_EXEC_SUMMARY.md` (three sites live, 11 planned).

---

*End of Session 3 & 4 detailed content. Adjust timings in this document and in the main agenda as needed during delivery.*
