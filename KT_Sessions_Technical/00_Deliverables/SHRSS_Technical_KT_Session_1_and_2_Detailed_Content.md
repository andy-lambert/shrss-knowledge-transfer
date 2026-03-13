# Session 1 & 2 — Introduction/Overview, AEM Application Development Parts 1 & 2

**Duration:** 2 hours  
**Presenters:** Andy Lambert, Vinay S A  
**Agenda reference:** `SHRSS_Technical_KT_Main_Agenda.md`  
**Exercises:** `SHRSS_Technical_KT_Exercises_Supplemental.md` (Session 1 & 2)

---

## Overview (Andy) — 25 min

### Cloud services ecosystem (Admin Console → Cloud Manager) — 8 min

**What to cover:**
- **Adobe Admin Console** (https://adminconsole.adobe.com/) is the central place for identity and product entitlements. SHRSS stakeholders will use it to manage **Users** and **User groups** (IAM). These IAM groups map into AEM as native groups for author/publish access.
- **Cloud Manager** (accessed via Experience Cloud or program-specific URL) is where the SHRSS **program** lives: environments (Dev, Stage, Prod), **repositories**, **pipelines**, and **environment variables/secrets**. No code runs in Admin Console; code and deployment are entirely in Cloud Manager.
- Flow: Admin Console (who has access) → Cloud Manager (what gets built and deployed, and to which environment). IAM users with the right product profile can log into AEM author/publish; Cloud Manager pipelines deploy the code and content that run on those environments.

**SHRSS-specific:** Three sites (e.g. Hard Rock, Reverb) and ~500GB DAM; 11 more migrations planned. All run in one program; environments are shared (Dev, Stage, Prod). Reference implementation analysis `00_EXEC_SUMMARY.md` for scale.

**Exercise cross-reference:** Exercise 1.1 — Log into Admin Console and Cloud Manager (homework).

---

### AEMaaCS architecture (high level) — 7 min

**What to cover:**
- AEM as a Cloud Service is **managed**: Adobe owns the AEM runtime, updates, and scaling. Customers own **application code** (repos), **content** (author), and **configuration** (OSGi configs in repo, not Felix Console).
- High-level tiers: **Author** (content creation, workflows); **Publish** (scaled, read-only, serves live traffic); **Dispatcher** (cache layer in front of publish); **CDN** (SHRSS uses BYOCDN: Cloudflare → Fastly → Dispatcher). Request flow: Browser → CDN → Dispatcher → AEM Publish.
- **No classic “instance” access:** No SSH, no direct filesystem. Everything is via Cloud Manager (pipelines, env vars), Admin Console (IAM), and AEM Web Console / Developer Console for debugging (logs, status).

**SHRSS-specific:** Implementation is standard AEMaaCS; multi-brand (HRHH, HRCasino, HRHCasino) via Context-Aware Configuration. Reference `01_STRUCTURAL_ARCHITECTURE.md` for layer breakdown (backend 203 elements, UI 101 elements).

---

### AEMaaCS Cloud Manager paradigms (environments, pipelines, repos) — 10 min

**What to cover:**
- **Environments:** Dev (author + publish), Stage (author + publish), Prod (author + publish). Optional: **RDE** (Rapid Development Environment) and **Preview** tier for validation before production.
- **Repositories:** One Git repo per program (SHRSS: single repo, `develop` branch per task). Code and OSGi configs live in repo; content can be in repo (e.g. `ui.content` for immutable content) or authored in author.
- **Pipelines:** **Full stack** (build → quality → security → deploy to non-prod or prod; can include custom functional and UI test steps). **Front-end** (frontend-only build/deploy). Build runs in Cloud Manager; no local deploy to cloud (except RDE with `aio` CLI if used).
- **Run modes and secrets:** Environment-specific config via run modes (`config.author`, `config.publish`, `config.dev`, etc.). Secrets and non-secret env vars configured in Cloud Manager per environment; no hardcoded credentials in repo (implementation analysis flagged hardcoded creds as P0).

**SHRSS-specific:** Implementation notes and task doc reference `config` module for CDN rules and maintenance tasks; `ui.config` for OSGi. Reference `00_EXEC_SUMMARY.md` for P0/P1 findings (e.g. servlet auth, test servlets in production) so audience knows what they are inheriting.

---

## AEM Application Development — Part 1 — 95 min

### Development tooling / IDEs (Andy / Vinay) — 12 min

**What to cover:**
- **Local dev setup:** Need Java (version per project POM), Maven, Node/npm (for `ui.frontend`). Clone repo; build with `mvn clean install` (or skip tests for speed). Run AEM locally only if using **RDE** or **SDK**-style local author (task emphasizes Cloud Manager; confirm with team if they use local AEM or only RDE).
- **IDE configuration:** IntelliJ or VS Code common. Import as Maven project; ensure `core`, `ui.apps`, `ui.frontend`, etc. are recognized. For Java, point to the JDK version required by the project.
- **Connecting to dev/author:** If using a remote dev author (e.g. Cloud Manager Dev environment), use **User Sync** or IAM so your user exists in AEM; log in via the author URL from Cloud Manager. No “admin” password in cloud; access is IAM-driven.

**SHRSS-specific:** Repo path per task: Customer-Git or `/Users/lambert/Documents/Projects/SHRSS/Code/shrss-aem-projects`; branch `develop`. Implementation notes: `core` (Java), `ui.apps` (HTL, components), `ui.frontend` (Webpack).

**Exercise cross-reference:** Exercise 1.2 — Clone repo and open in IDE (homework or in-session).

---

### Code structure (Andy / Vinay) — 25 min

**What to cover:**

- **Maven/POM and dependency management:** POM (Project Object Model) - Root `pom.xml` defines modules and parent POM (AEM archetype or project parent). Each module has its own `pom.xml`; `core` depends on AEM/Sling APIs; `ui.apps` packages content; `all` aggregates for deployment. Build order matters: typically `core` → `ui.apps` (which may depend on `ui.frontend` build output) → `all`.

- **Main modules (per implementation notes):**
  - **core** — OSGi bundle; Java (Sling Models, services, servlets, schedulers, listeners, workflows). Business logic and component models.
  - **ui.apps** — FileVault package; AEM components (HTL, dialogs), clientlib definitions, templates structure. No Java; references `core` for models.
  - **ui.frontend** — Webpack; TypeScript/JS, Sass/SCSS. Build output is copied into `ui.apps` as clientlibs.
  - **ui.content** — FileVault; default/mutable content (site structure, base pages, sample content). Also **persistent queries** under `conf/shrss/settings/graphql/persistentQueries/` (per exercise supplemental).
  - **ui.config** — OSGi configurations (`.cfg.json`); runmode-specific configs (e.g. `config.author`, `config.publish`). Immutable in AEMaaCS; no runtime edit in Felix.
  - **dispatcher** — Apache + Dispatcher configs; cloud-optimized, validated by Dispatcher SDK.
  - **it.tests** — Integration tests (AEM testing client); run in Cloud Manager custom functional testing step.
  - **ui.tests** — Cypress UI tests; run in Cloud Manager custom UI testing step.
  - **all** — Aggregates other packages for one deployment unit.
  - **acl** — Base groups and ACLs (Netcentric Access Control Tool).
  - **config** — CDN rules, maintenance task configurations (per implementation notes).

- **Other configs:** Log forwarding, CDN, maintenance tasks live in `config` or as documented in implementation notes. Point to repo and implementation analysis for exact paths.

**SHRSS-specific:** Implementation analysis: 313+ structural elements (backend 203, UI 101); 95 custom components, 6 CF models. Reference `01_STRUCTURAL_ARCHITECTURE.md` and `SHRSS_AEM_Implementation_Notes.md`.

**Exercise cross-reference:** Exercise 1.2 (clone, open, confirm modules).

---

### AEM authoring components (Andy → Vinay) — 58 min

#### Core Components and extending (e.g. hrccard) — 10 min

- **Core Components:** Adobe’s standard, accessible, editable components (e.g. Title, Text, Image, List). Best practice: extend rather than build from scratch. SHRSS uses this pattern (e.g. ~40% of components extend Core Components per exec summary).
- **hrccard:** Custom component that extends a Core Component or base; resource type `shrss/components/hrccard`. Lives in `ui.apps/.../apps/shrss/components/hrccard/` (`.content.xml` for metadata, `hrccard.html` for HTL). Sling Model in `core`: `CardImpl.java` (adaptable Resource, exposes data to HTL).
- **Extending:** `sling:resourceSuperType` points to Core Component or parent; override only what’s needed (HTL, dialog, or model).

**Repo paths:** `ui.apps/.../shrss/components/hrccard/`; `core/.../models/impl/CardImpl.java`.

---

#### Dialogs — 8 min

- **Dialog:** Author UI for component properties. Typically `_cq_dialog/.content.xml` (Granite/Coral) or classic dialog. Defines fields (text, pathfield, etc.) and maps to `cq:Component` properties.
- **Where:** Under component folder in `ui.apps` (e.g. `hrccard/_cq_dialog/`). Content authors fill these; values stored on the component resource; Sling Model reads via `@ValueMapValue` or similar.

**SHRSS-specific:** Components under `ui.apps/.../apps/shrss/components/`; dialogs follow standard AEM patterns. Reference authoring KT (Gonzalo, TJ, Tim) if dialog design was covered there.

---

#### Clientlibs (definition, categories, file/folder structure) — 12 min

- **Definition:** Client libraries bundle CSS/JS for the page. Categories allow inclusion (e.g. `wknd.base`). In AEM, components request categories via `data-sly-use.clientlib` or template-level `cq:clientlibrary` or page property.
- **Structure in SHRSS:** Clientlib **definitions** (`.content.xml` with `categories`, `allowProxy`) in `ui.apps/.../apps/shrss/clientlibs/`. **Source** JS/SCSS in `ui.frontend`; Webpack builds and embeds or copies into `ui.apps` clientlib folders. So: author sees one clientlib; developer edits in `ui.frontend`, builds, and deploys.
- **Categories:** Use consistent naming (e.g. `shrss.components`, `shrss.base`) to avoid duplicate includes and control load order. Best practice: one category per logical bundle; dependencies via `embed`.

**Repo paths:** `ui.apps/.../shrss/clientlibs/`; `ui.frontend/src/`.

**Exercise cross-reference:** Exercise 1.4 — Trace a clientlib from a component (homework).

---

#### Sling Models (Use-API, extending, debugging) — 15 min

- **Use-API:** In HTL, `data-sly-use.model="com.shrss.core.models.impl.CardImpl"` (or resource-type-based adaptation). Model adapts the current resource (or request) and exposes getters for the template.
- **Extending:** Sling Models are Java classes with `@Model(adaptables = Resource.class, ...)`. Use `@ValueMapValue`, `@ChildResource`, `@OSGiService`, `@Self`, `@SlingObject`. Interface + impl optional; in SHRSS many models in `core/.../models/impl/`. Resource type is often used to pick the model (via `@Model` resourceType or adapter map).
- **Debugging:** Logging in model; breakpoints in IDE when running tests or in local AEM. Check that the correct model is bound (resource type, adaptables). Implementation analysis: 65 model impls, 93.8% test coverage (good); some NPE/missing validation noted in `01_STRUCTURAL_ARCHITECTURE.md`.

**SHRSS-specific:** `CardImpl` for hrccard; pattern: `core/.../models/impl/<Name>Impl.java`. Reference `01_STRUCTURAL_ARCHITECTURE.md` §1.2.2 Sling Model pattern and §1.3.1 models package.

**Exercise cross-reference:** Exercise 1.3 — Locate the Sling Model for hrccard (in-session, ~5 min).

---

#### Best practices (structure, clientlib categories) — 8 min

- **Structure:** Keep components in `ui.apps`; Java in `core`. One component = one (or few) Sling Model(s). Delegate business logic to OSGi services; keep models thin (data shape for HTL).
- **Clientlibs:** Minimal categories; avoid duplicate includes; use `embed` for dependencies. Frontend build should be reproducible (same npm/node version as CI).
- **Dialogs:** Only expose what authors need; use appropriate widget types (pathfield for paths, etc.). Reference AEM canonical docs (Experience League) for component and clientlib best practices; see `docs/ai/reference/AEM_CANONICAL_REFERENCES.md` and `AdobeDocs-global-mapping.csv` per AGENTS.md.

---

#### Exercise: Locate the Sling Model for a component (hrccard) — 5 min

- Follow **Exercise 1.3** in the exercise supplemental: from `shrss/components/hrccard` → resource type → search `core` for resource type or `CardImpl` → open model and HTL, show `data-sly-use` and getters.
- **Repo paths:** `ui.apps/.../shrss/components/hrccard/`; `core/.../models/impl/CardImpl.java`; `hrccard.html`.

---

*End of Session 1 & 2 detailed content. Adjust timings in this document and in the main agenda as needed during delivery.*
