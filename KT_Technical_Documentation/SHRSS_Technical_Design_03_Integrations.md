# SHRSS Technical Design — Integrations

**Purpose:** Overview of external and internal integration points used by the SHRSS implementation.

---

## 1. External System Integrations

### 1.1 Unity API (Frontend Iframe)

- **Purpose:** Member login, registration, rewards.
- **Pattern:** Frontend iframe modal (Crown CTA component); header orchestrates Unity login flow.
- **Backend:** Unity-related backend services exist in the codebase (e.g. UnityProductService, UnityCheckoutService, UnityOrderService) but are not in use; only the frontend iframe integration is active.
- **Components:** crowncta, header (Unity orchestration).

### 1.2 Workday / Jobs (Careers)

- **Purpose:** Job data for Careers site (sync or feed into Content Fragments).
- **Location:** Backend services and/or schedulers; Jobs Content Fragment config (e.g. JobsContentFragmentConfigService); joblistings, jobsearch, jobfilters components.
- **Configuration:** OSGi config or environment variables for endpoints and credentials (recommended: use Cloud Manager secrets).

### 1.3 DPLT (Locations / Venues)

- **Purpose:** Location and venue data for properties.
- **Location:** Backend services and models; components that consume location/venue data; persistent queries (e.g. locationListing, searchVenuLocations, franchiseLocations).
- **Data flow:** DPLT → backend service → Sling Model or API → component.

### 1.4 GraphQL (Content Fragments)

- **Purpose:** Headless consumption of Content Fragment data (jobs, events, news, locations, promotions).
- **Pattern:** Persistent queries stored under `conf/shrss/settings/graphql/persistentQueries/`; backend services or models invoke GraphQL client; components consume via models or servlets.
- **Endpoint (example):** `/content/cq:graphql/shrss/endpoint.json`
- **Usage:** CF card list, job listings, event calendar, news search, promotion search, etc.

### 1.5 OpenTable API

- **Purpose:** Restaurant reservation availability and booking.
- **Pattern:** Backend OpenTableService; frontend component (e.g. Dining Reservation); API key should be configured via Cloud Manager secrets.
- **Flow:** Component → model → OpenTableService → OpenTable REST API → response to frontend.

### 1.6 Grubhub API

- **Purpose:** Online food ordering (menu data, order submission).
- **Pattern:** Backend GrubhubService; Cafe Delivery Widget component; API key via configuration.
- **Flow:** Component → model → GrubhubService → Grubhub API; order submission via separate request.

### 1.7 Google Maps API

- **Purpose:** Embedded location maps.
- **Pattern:** Google Map component; API key in component or OSGi configuration.
- **Location:** `ui.apps/.../components/content/googlemap`; GoogleMapModel.

### 1.8 Adobe Dynamic Media

- **Purpose:** Image transformations and video delivery.
- **Pattern:** AEMaaCS native integration; Core Components and custom image/video components can use Dynamic Media.

### 1.9 Other / Planned

- **TransPerfect:** Translation services (not yet implemented).
- **Adobe Target:** Personalization (pilot planned).

---

## 2. Internal AEM Dependencies

### 2.1 AEM Core Components

- Many custom components extend Core Components via `sling:resourceSuperType`.
- Upgrades managed via Maven dependency (e.g. core components, CIF version).

### 2.2 Adobe Commerce Integration Framework (CIF)

- Included in ui.apps dependencies (e.g. core-cif-components-apps).
- Commerce-specific usage should be confirmed against the current project scope.

### 2.3 AEM Headless (GraphQL)

- Content Fragment models exposed via GraphQL; persistent queries used for headless and server-side consumption.
- See §1.4 above.

---

## 3. Configuration and Credentials

- **API keys and secrets:** Should be stored in Cloud Manager (environment variables or secrets), not in repository code.
- **OSGi config:** Endpoints, timeouts, and feature flags can be in `ui.config` (runmode-specific) where appropriate.
- **Component-level config:** Some integrations (e.g. Google Maps) may expose API key or endpoint in dialog; prefer centralized config where possible.

---

*For runtime flows of specific integrations, see `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md`. For backend service and servlet locations, see `SHRSS_Technical_Design_01_Backend_Architecture.md`.*
