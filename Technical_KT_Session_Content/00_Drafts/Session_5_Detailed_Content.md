# Session 5 — AEM Application Development Parts 5 & 6, Change and Release Management, DevOps Part 1

**Duration:** 2 hours  
**Presenters:** Andy Lambert, Vinay S A  
**Agenda reference:** `SHRSS_Technical_KT_Main_Agenda.md`  
**Exercises:** `SHRSS_Technical_KT_Exercises_Supplemental.md` (Session 5)

---

## AEM Application Development — Part 3 (continued) — 65 min

### Dispatcher / CDN (Andy → Vinay) — 28 min

#### Cloud-optimized Apache and Dispatcher configs — 10 min

- **Location:** `dispatcher/` module in repo. Uses **immutable** files validated by the Dispatcher SDK (AEMaaCS). No runtime edit; changes go through Git and pipeline.
- **Structure:** Apache (e.g. `httpd.conf`, includes) and Dispatcher module (`.vhost`, `dispatcher.any`, `filter.any`, `cache.any`, etc.). Cloud-optimized = no filesystem cache paths that conflict with scaling; use allowed document root and cache directories per Adobe docs.
- **SHRSS-specific:** Implementation analysis Phase 3: 50+ config files; 14 configuration issues (2 P0, 10 P1, 2 P2). Reference `01_STRUCTURAL_ARCHITECTURE.md` §3 (Dispatcher Layer) and staging `staging/dispatcher/STRUCTURAL_DISPATCHER_CDN.md` for inventory.

**Repo path:** `dispatcher/`.

---

#### Caching and security (filter rules, blocking unauthenticated servlet access) — 10 min

- **Caching:** Dispatcher caches eligible responses (e.g. GET, no auth, cacheable content). Invalidation via replication agent or API (flush). Cache rules in `filter.any` / `cache.any`; allow/deny for paths.
- **Security:** **Filter rules** must block unauthenticated access to sensitive servlets on publish. Implementation analysis P0: **DeleteJobServlet** and **JobsCFUpdateServlet** are allowed through Dispatcher without auth (ISSUE-DISPATCHER-008, 009). Add filter rules to deny these paths on publish (or ensure they are author-only). Author-only servlets should not be exposed on publish at all.
- **Best practice:** Deny by default for `/apps/` or specific servlet paths that require auth; allow only public APIs and page/content paths as needed.

**Reference:** `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md` Phase 3 Dispatcher issues; `05_INDEX_AND_NAVIGATION.md` for ISSUE-DISPATCHER-008, 009.

---

#### CDN configuration (BYOCDN rules in `config` module) — 5 min

- **BYOCDN:** SHRSS uses Bring Your Own CDN (Cloudflare → Fastly → Dispatcher per exec summary). CDN rules (e.g. cache TTL, purge behavior) may live in `config` module or in Cloud Manager / CDN provider config. Request flow: Browser → Cloudflare → Fastly → Dispatcher → AEM Publish.
- **Repo:** Implementation notes list `config` for CDN rules and maintenance tasks. Point to `config/` and any CDN-related files; clarify with team where Fastly/Cloudflare rules are managed (repo vs provider UI).

**Repo path:** `config/` (per implementation notes).

---

#### Reference to implementation analysis Dispatcher/CDN findings — 3 min

- **Summary:** 14 Dispatcher/CDN issues (2 P0 servlet auth, 10 P1 e.g. filter mismatches, TestServlet in production). Remediation roadmap in `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md`. Use staging docs and index for full list and file references.

---

### General AEM troubleshooting / debugging (Andy / Vinay) — 15 min

#### Cache issues (distribution queues, logs via distribution console) — 5 min

- **Replication / distribution:** Content published from author to publish; replication agents (or distribution) push content and invalidate Dispatcher cache. If content doesn’t update on publish: check replication queue (author), distribution console, and Dispatcher flush. Logs: AEM logs and Cloud Manager for author/publish.
- **Dispatcher cache:** Stale pages if invalidation failed or path not invalidated. Check `filter.any`/`cache.any` for path rules; trigger manual flush if needed (per Adobe docs).

---

#### Unhandled exceptions / 500s (AEM logs) — 5 min

- **Logs:** Developer Console (AEM) or Cloud Manager → Logs. Look for stack traces, CQ/AEM and application errors. Common: missing config, NPE in model/servlet, resource resolver not closed, timeout to external service.
- **SHRSS:** Implementation quality doc notes NPE risks in a few models; resource resolver leaks. Use logs to correlate with component or request path.

**Reference:** Experience League — AEM logging and Developer Console.

---

#### Developer Console (Experience League reference) — 5 min

- **Developer Console:** Available in AEMaaCS (author and publish). Provides status, logs, and diagnostics. Point to Experience League for “AEM as a Cloud Service – Developer Console” (or equivalent). Use for thread dumps, bundle status, and log streaming.

**Reference:** `docs/ai/reference/AEM_CANONICAL_REFERENCES.md` and `AdobeDocs-global-mapping.csv` for exact URLs.

---

### Development considerations for AEMaaCS (Andy) — 22 min

#### Idempotency — 12 min

- **Why it matters:** AEMaaCS is horizontally scaled; bundle restarts, deployment retries, and concurrent execution mean code may run **multiple times** or **out of order**. **Idempotent** code produces the same final state no matter how many times it runs.
- **Patterns:**
  - **Repo init:** Check `if (!resource.getResourceResolver().getResource(path).exists())` before creating; conditional writes.
  - **Schedulers:** Check “already processed” markers; skip or update safely; no blind appends or increments.
  - **Listeners:** Same: avoid duplicate side effects; use flags or atomic checks.
  - **Workflows:** Process step must be safe to retry; mark work items so they are not processed twice.
- **Anti-patterns:** Blind `node.addNode("child")`; assuming “first run only”; accumulative counters without guards. AGENTS.md idempotency appendix: safe initialization, conditional writes, safe activation, schedulers that tolerate concurrency.
- **SHRSS:** Implementation analysis: schedulers, listener, workflow have tests but idempotency not validated (P0 test quality). Code must be fixed and tests added.

**Reference:** AGENTS.md Appendix (Idempotency); `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md` (reliability, test quality).

---

#### Distributed, Mongo-based repository — 5 min

- **AEMaaCS:** Content is stored in a distributed, Mongo-backed repository. Implications: eventual consistency in some scenarios; no local filesystem; session affinity and clustering handled by Adobe. For developers: avoid assumptions about “single node” or “immediate visibility” across all nodes; use proper JCR APIs and avoid long-held locks.

---

#### Best practices — 5 min

- **Recap:** Idempotency; close ResourceResolvers; no hardcoded secrets; auth on sensitive servlets; no test servlets in production; thread-safe code (no SimpleDateFormat as instance field, no mutable servlet instance state). Reference quality assessment and AGENTS.md.

---

## Change and Release Management (Andy) — 25 min

### Source control management — 5 min

- **Git:** Single repo per program (SHRSS). All application code and OSGi configs in repo; `develop` branch per task. Use branches for features and fixes; follow team branching strategy (e.g. feature branches, release branches).

---

### Aligning code changes to Jira — 5 min

- **Practice:** One Jira ticket per logical change; reference ticket in commit message or branch name. Enables traceability and aligns with Cloud Manager pipeline (e.g. deployment gates, release notes). SHRSS has substantial Jira history (implementation analysis used 1,743 tickets).

---

### Git branching strategy — 8 min

- **Typical:** Long-lived `develop`; short-lived feature branches (e.g. `feature/JIRA-123-description`); release branch (e.g. `release/1.2`) for stabilization; merge to main/master for production. Production deployments from main or from release branch per team policy. Document SHRSS actual strategy (per task or team).

---

### Cutting a release and production deployment — 7 min

- **Release:** Tag or merge to production branch; run **production pipeline** in Cloud Manager. Pipeline: build → quality → security → deploy to production. Optional: approval step. No direct deploy to prod outside Cloud Manager.
- **Rollback:** Per Cloud Manager capabilities (e.g. redeploy previous build). Content changes may require separate rollback (restore, content copy) as documented in Cloud Manager.

**Reference:** Experience League — Cloud Manager pipelines and release management.

---

## DevOps — Part 1 (Andy) — 28 min

### User / group / permission management (Admin Console IAM → native AEM groups) — 15 min

- **Flow:** IAM users and groups are managed in **Admin Console**. Users get product profile (e.g. AEM Author – DEV). In AEM, **native groups** (e.g. `content-authors`) can have **IAM groups** as members. When a user logs in, they are mapped to AEM groups via their IAM group membership; permissions in AEM are then based on those groups (ACLs).
- **Walk-through (participant exercise):**  
  1. Create IAM group in Admin Console (https://adminconsole.adobe.com/).  
  2. Add IAM user (with DEV author profile) to IAM group.  
  3. User logs into DEV author.  
  4. In AEM: Tools → Security → Groups; add IAM group to native AEM group.  
  5. Verify user and IAM group in Tools → Security → Users.  
- **SHRSS roles and environments:** Map to actual SHRSS roles (e.g. author, developer, admin) and which environments (Dev, Stage, Prod) each role can access. Reference `acl` module for base groups/ACLs (Netcentric).

**Exercise cross-reference:** Exercise 3.1 — IAM group to native AEM group (in-session).

---

### Cloud Manager — 13 min

- **Environments:** Dev, Stage, Prod (author + publish each). Optional: **RDE** (Rapid Development Environment), **Preview** tier. Explain purpose of each (dev vs stage vs prod; RDE for quick validation).
- **Repositories:** Git repo URL; branch for pipeline (e.g. `develop` for non-prod, main for prod).
- **Build pipelines:** Full stack (build, quality, security, deploy; custom functional and UI test steps). Front-end pipeline if used. Trigger on commit or manual.
- **Environment variables and secrets:** Per environment; used for API keys, feature flags, endpoints. Secrets for sensitive values.
- **Environment whitelists:** IP allowlists for access to author/publish if configured.
- **Content restore and bulk content copy:** Cloud Manager capabilities for restoring content or copying between environments; reference Adobe docs for current features.

**Exercise cross-reference:** Exercise 3.2 — View environments and pipeline in Cloud Manager (in-session or homework).

---

*End of Session 5 detailed content. Adjust timings in this document and in the main agenda as needed during delivery.*
