# SHRSS Technical Design — Cross-Layer Interactions

**Purpose:** Scenario-based description of how frontend components, backend models, services, servlets, and external systems interact at runtime. This document covers **execution flow**, **data movement**, and **responsibility handoffs**; it does not redefine component responsibilities (see structural docs 01–04).

---

## 1. How to Use This Document

- **Trigger** — What initiates the flow (user action, system event, HTTP request).
- **Participating elements** — Components, models, services, servlets, external systems in order of participation.
- **Execution flow** — Step-by-step runtime behavior.
- **Data flow** — Who owns data, who consumes it, where it is transformed or cached.
- **Error paths** — What can fail, how it is detected, and fallback or user impact where applicable.

For structural details (what each component owns, dependencies), use `SHRSS_Technical_Design_01_Backend_Architecture.md` and `SHRSS_Technical_Design_02_Frontend_Architecture.md`.

---

## 2. Example: Page Render with Sling Model and Service

**Overview:** A typical page request flows from Dispatcher to AEM Publish; HTL components use Sling Models, which may call OSGi services for data.

**Trigger:** HTTP GET for a page (e.g. `/content/shrss/corporate/hardrock/en/home.html`).

**Participating elements:**  
1. Dispatcher (cache check, forward or serve from cache)  
2. AEM Publish (Sling resolution)  
3. Page component (structure)  
4. Child components (e.g. hero, container, list)  
5. Sling Models (e.g. HeroModel, ContainerModel)  
6. OSGi services (e.g. AssetService, ContentAccessService)  
7. JCR / DAM

**Execution flow (simplified):**  
1. Request hits Dispatcher; if not cached, forwarded to AEM.  
2. Sling resolves page resource and template.  
3. Page and child components render; each component’s HTL uses `data-sly-use` to adapt resource to a Sling Model.  
4. Models read resource properties and, when needed, call OSGi services (e.g. for navigation, assets, tags).  
5. Services query JCR or DAM and return DTOs or lists.  
6. Models expose data to HTL; HTL renders markup.  
7. Response returned; Dispatcher may cache it per cache rules.

**Data flow:**  
- **Primary owner:** JCR (content, DAM).  
- **Consumers:** Models (read-only), services (read-only).  
- **Caching:** Dispatcher and CDN per filter/cache configuration.

**Error paths:**  
- **Service unavailable:** Model may return empty or default; component renders with fallback.  
- **Missing resource:** Sling returns 404 or component omitted per template logic.

---

## 3. Example: Content Fragment / GraphQL Consumption

**Overview:** Components that display Content Fragment data (e.g. job list, events, news) use backend services or models that call the GraphQL endpoint or persistent queries.

**Trigger:** Page render or AJAX request that requires CF data (e.g. job list, event list).

**Participating elements:**  
1. Component (e.g. joblistings, cfcardlist)  
2. Sling Model (e.g. JobListingsModel, CFCardListModel)  
3. OSGi service (e.g. GraphQL client, Jobs Content Fragment config service)  
4. AEM GraphQL endpoint (persistent queries)  
5. JCR (Content Fragments)

**Execution flow (simplified):**  
1. Component’s HTL uses a Sling Model bound to the component resource.  
2. Model reads authored props (e.g. root path, tags, list type).  
3. Model invokes a service that runs a persistent GraphQL query (by name) against the GraphQL endpoint.  
4. Endpoint resolves query and returns JSON.  
5. Service maps JSON to DTOs; model exposes list or structure to HTL.  
6. HTL iterates and renders cards or list items.

**Data flow:**  
- **Primary owner:** JCR (Content Fragments under `/content/dam/.../cf/`).  
- **Transformations:** CF → GraphQL schema → JSON → DTO → model properties.  
- **Caching:** Dispatcher/CDN for page; API responses may be cached per backend design.

**Error paths:**  
- **Invalid query or syntax:** Backend returns 400/500; service can log and return empty list; component can show empty state or message.  
- **Timeout:** Service timeout; fallback to empty or error message.  
- **Content Fragment not found:** Empty result set; component renders accordingly.

---

## 4. Example: Job Content Fragment Management (Backend API)

**Overview:** Job data is created, updated, retrieved, or deleted via backend servlets that interact with Content Fragment Manager and JCR.

**Trigger:**  
- GET `/services/shrss/v1/jobs/getClientDetails?jobId=...` — retrieve job details.  
- GET `/services/shrss/v1/jobs/getJobIds` — list job IDs (e.g. via GraphQL).  
- POST `/services/shrss/v1/jobs/update` — create/update job Content Fragments.  
- POST `/services/shrss/v1/jobs/deleteJob` — delete job Content Fragment.

**Participating elements:**  
1. Client (external system or admin)  
2. Servlets (JobDetailsServlet, JobIdsServlet, UpdateJobServlet, DeleteJobServlet)  
3. Content Fragment Manager (AEM)  
4. GraphQL client (for read paths)  
5. JCR (Content Fragment storage)

**Execution flow (create/update):**  
1. Client POSTs job data (JSON) to update endpoint.  
2. Servlet validates payload and resolves or creates Content Fragment at configured path.  
3. Servlet maps JSON to CF properties; Content Fragment Manager persists to JCR.  
4. Servlet returns success and job ID; replication may be triggered for publish.

**Execution flow (retrieve):**  
1. Client GETs job details with job ID.  
2. Servlet invokes GraphQL (persistent query) or CF API to load job data.  
3. Servlet maps result to response DTO and returns JSON.

**Execution flow (delete):**  
1. Client POSTs delete with job ID.  
2. Servlet resolves Content Fragment and deletes via Content Fragment Manager.  
3. Servlet returns success.

**Data flow:**  
- **Primary owner:** JCR (job Content Fragments).  
- **Consumers:** Servlets (read-write for update/delete); client (read or trigger write).

**Error paths:**  
- **Invalid job ID or payload:** 400.  
- **Content Fragment not found:** 404.  
- **GraphQL or JCR failure:** 500; client may retry or report.

---

## 5. Example: Location Data Export (Scheduled Job)

**Overview:** A scheduler creates a Sling Job; a job consumer retrieves location data and sends it to an external API.

**Trigger:** Cron schedule (e.g. hourly or daily) or manual trigger via Sling Jobs API.

**Participating elements:**  
1. LocationExportScheduler (cron)  
2. Sling Job Manager  
3. LocationsDataExportJobConsumer  
4. LocationDataService  
5. External API (location consumer)

**Execution flow:**  
1. Scheduler runs on cron; creates Sling Job with topic (e.g. `shrss/jobs/locationexport`).  
2. Job Manager queues job; consumer picks it up.  
3. Consumer calls LocationDataService to load locations (e.g. from JCR/CF).  
4. Service returns location DTOs; consumer serializes and POSTs to external API.  
5. Consumer marks job complete or failed; Job Manager may retry on failure.

**Data flow:**  
- **Primary owner:** JCR (location Content Fragments).  
- **Transformations:** CF → service DTO → JSON → HTTP POST.  
- **External API:** Receives export; does not write back to AEM.

**Error paths:**  
- **JCR or service failure:** Job fails; retries on next run or per retry policy.  
- **External API unavailable or timeout:** Job fails; retries up to configured limit.

---

## 6. Example: Unity Login (Frontend Iframe)

**Overview:** The Crown CTA component and header work together to show a Unity login modal implemented as an iframe. This is the active Unity integration (frontend only).

**Trigger:** User clicks sign-in CTA; Crown CTA sets a request attribute; header renders the login modal iframe.

**Participating elements:**  
1. Crown CTA component (sign-in button)  
2. CrownCTAModel (sets request attribute for login)  
3. Header component (includes login iframe template)  
4. Login iframe template (lazy-loaded iframe)  
5. LoginModal JavaScript (opens modal, loads iframe, handles postMessage)  
6. Unity login endpoint (in iframe)

**Execution flow:**  
1. Crown CTA renders sign-in button; CrownCTAModel sets `request.setAttribute("login", "true")`.  
2. Header checks model for login flag; includes login iframe template.  
3. Template outputs iframe with lazy `data-src` (e.g. `/services/loginwrapper`).  
4. On button click, LoginModal JavaScript opens modal and sets iframe `src` to load Unity.  
5. User logs in inside iframe; Unity sends postMessage (e.g. `unityLoginSuccess`).  
6. JavaScript handles event and updates UI (e.g. cookie `unity_login_info`).

**Data flow:**  
- **Primary owner:** Unity endpoint (session, auth state).  
- **Contracts:** Request attribute `login`; cookie `unity_login_info`; postMessage events for height, spinner, success.

**Error paths:**  
- **Iframe load failure or timeout:** Modal may stay open with empty iframe; user may need to refresh.  
- **PostMessage not received:** UI may not reflect logged-in state; refresh may be needed.

---

## 7. Interaction Categories (Summary)

Backend and frontend interactions in the implementation fall into categories such as:

- **External integrations:** OpenTable, Grubhub, Google Maps, Unity (iframe), Workday/jobs, DPLT/locations.  
- **Content Fragment / GraphQL:** CF queries, persistent queries, job/event/news/location/promotion data.  
- **DAM:** Asset queries, metadata, renditions (AssetService, Dynamic Media).  
- **Background jobs:** Location export, asset cleanup, other schedulers and Sling Jobs.  
- **Component rendering:** Page and component render; models and services; cache at Dispatcher/CDN.  
- **User interactions:** Forms, search, filters (e.g. job search, promotion search); AJAX and client-side updates.

For a given feature, trace from **trigger** (e.g. page load, button click, cron) through **participating elements** (component → model → service/servlet → JCR or external API) to **output** (rendered HTML, JSON response, or side effect). Use the structural docs to see what each element is allowed to depend on and where it lives in the codebase.

---

*For structural details see `SHRSS_Technical_Design_01_Backend_Architecture.md`, `SHRSS_Technical_Design_02_Frontend_Architecture.md`, and `SHRSS_Technical_Design_03_Integrations.md`. For Dispatcher and request flow see `SHRSS_Technical_Design_04_Dispatcher_Configurations.md`.*
