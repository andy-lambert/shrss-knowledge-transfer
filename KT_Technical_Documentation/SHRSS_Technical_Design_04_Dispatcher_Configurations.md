# SHRSS Technical Design — Dispatcher Configurations

**Layer:** Web tier (Apache + AEM Dispatcher)  
**Purpose:** Structural overview of Dispatcher and Apache configuration for caching, security, and routing.

---

## 1. Overview

**Module:** `dispatcher/` at repository root  
**Target:** AEMaaCS (cloud-optimized Dispatcher)  
**Constraint:** Configuration is immutable and validated by the Dispatcher SDK; changes are made in the repository and deployed via Cloud Manager.

---

## 2. Apache Configuration (conf.d/)

- **dispatcher_vhost.conf:** Base Apache configuration — Dispatcher module loading, health probes (`/system/probes/*`), environment-specific proxy (e.g. test-site, CRXDE in dev), commerce GraphQL proxy, Dynamic Media bypass, and customer vhost includes.
- **Virtual hosts:** Pattern-based; multiple files in `available_vhosts/` (e.g. brand-specific such as hardrock).
- **Rewrites / redirects:** Multiple files in `rewrites/` for legacy redirects and vanity URLs.
- **Variables:** Environment-specific (e.g. `${FORWARDED_HOST_SETTING}`, commerce endpoints).

---

## 3. Dispatcher Module (conf.dispatcher.d/)

- **dispatcher.any:** Farm definitions and include chain.
- **Farms:** Multiple farms (e.g. default, hardrock_publish) with:
  - **Filters (filters.any):** Allow/deny rules for paths such as `/content/*`, `/bin/shrss/*.json`, `/services/*`, `/content/shrss/unity/*`. Filter rules determine what reaches AEM and what is blocked or cached.
  - **Cache (cache/):** rules.any (cache rules), default TTLs; optional marketing_query_parameters.any; farm-specific rules (e.g. hardrock_rules.any).
  - **Renders:** default_renders.any (AEM publish instance).
  - **Client headers:** Headers passed through to AEM.

**Design considerations:** Filter rules should align with backend servlet paths so that authenticated or sensitive endpoints are not cached or are denied for unauthenticated access where required. Cache rules control which responses are cached and for how long.

---

## 4. CDN Architecture (BYOCDN)

- **Request flow:** Browser → **Cloudflare** (customer edge) → **Adobe Fastly** (pass-through; Surrogate-Control headers) → **Dispatcher** → AEM Publish.
- **Configuration:** CDN-related config (e.g. edge auth, test headers for dev/stage) may live in `config/` (e.g. `cdn.yaml`, `cdn-prod.yaml`, `cdn-stage.yaml`) or in Cloud Manager.
- **Invalidation:** Content activation from AEM author triggers replication to publish; Dispatcher invalidation and CDN purge follow. Invalidation and purge behavior should use a secure mechanism (e.g. secure header or server-side config rather than query parameters) where applicable.

---

## 5. Key File Relationships

- **Parent/includes:** Apache main config includes vhosts, rewrites, and variables; Dispatcher farm includes filter, cache, render, and client header files.
- **Runmodes/environments:** Different vhosts and variables support dev, stage, and production behavior.

---

## 6. Operational Notes

- **Validation:** Dispatcher SDK validates configuration during build; invalid configs fail the pipeline.
- **Deployment:** No runtime edit of Dispatcher files; all changes via Git and Cloud Manager.
- **Troubleshooting:** Cache behavior can be verified via response headers and invalidation logs; filter rules can be reviewed to confirm which paths hit AEM vs. are blocked or served from cache.

---

*For backend servlet paths and authentication context, see `SHRSS_Technical_Design_01_Backend_Architecture.md` and `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md`. For CDN and config module, see repository `config/` and Cloud Manager documentation.*
