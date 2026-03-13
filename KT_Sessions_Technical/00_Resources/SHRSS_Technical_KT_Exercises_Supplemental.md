# Technical KT — Exercises Supplemental

**Purpose:** In-session exercises and suggested homework for SHRSS technical KT. Organized by session and topic/subtopic. Use during sessions as time permits and share with participants as suggested homework.

**Repo:** All paths are relative to the SHRSS AEM source code repository root (e.g. `shrss-aem-projects`).  
**Reference:** Implementation notes — `Technical_KT_Session_Content/00_Resources/SHRSS_AEM_Implementation_Notes.md`

---

## Session 1 & 2 — Introduction/overview, AEM Application Development Parts 1 & 2

### Overview — Cloud Manager / Admin Console

**Exercise 1.1 — Log into Admin Console and Cloud Manager (homework)**  
- **Goal:** Confirm access and see where IAM and programs/environments live.  
- **Steps:**  
  1. Open [Adobe Admin Console](https://adminconsole.adobe.com/) and log in.  
  2. Navigate to your organization and locate **Products** (e.g. Adobe Experience Manager).  
  3. Note where **Users** and **User groups** (IAM) are managed.  
  4. Open [Cloud Manager](https://experiencecloud.adobe.com/) (or the URL provided for your program).  
  5. Select the SHRSS program and note **Environments** (Dev, Stage, Prod, etc.).  
- **No repo paths.**

---

### Code structure

**Exercise 1.2 — Clone repo and open in IDE (homework or in-session)**  
- **Goal:** Have the SHRSS codebase locally and open in your IDE.  
- **Steps:**  
  1. Clone the SHRSS AEM Git repository (branch `develop` per task).  
  2. Open the root folder in your IDE (e.g. IntelliJ, VS Code).  
  3. Confirm you see these modules at repo root: `core`, `ui.apps`, `ui.frontend`, `ui.content`, `ui.config`, `dispatcher`, `it.tests`, `ui.tests`, `all`, `acl`, `config`.  
  4. Open the root `pom.xml` and note the module list.  
- **Repo paths:**  
  - `pom.xml` (root)  
  - `core/`, `ui.apps/`, `ui.frontend/`, `ui.content/`, `ui.config/`, `dispatcher/`, `it.tests/`, `ui.tests/`, `all/`, `acl/`, `config/`

---

### AEM authoring components — Sling Model

**Exercise 1.3 — Locate the Sling Model for a component (hrccard)**  
- **Goal:** Trace from a component resource type to its Java Sling Model in the repo.  
- **Steps:**  
  1. In the repo, open the **hrccard** component definition (resource type).  
  2. Note the `sling:resourceSuperType` and that this component is a custom extension.  
  3. Search the **core** module for the resource type string `shrss/components/hrccard` to find the Sling Model class.  
  4. Open the Sling Model class and note the `@Model` adaptables and the resource type constant.  
  5. Optionally: open the component’s HTL and see how the model is used (e.g. `data-sly-use.model`).  
- **Repo paths:**  
  - Component: `ui.apps/src/main/content/jcr_root/apps/shrss/components/hrccard/.content.xml`  
  - HTL: `ui.apps/src/main/content/jcr_root/apps/shrss/components/hrccard/hrccard.html`  
  - Sling Model: `core/src/main/java/com/shrss/core/models/impl/CardImpl.java`  
  - Model interface (if used): `core/src/main/java/com/shrss/core/models/Card.java` (or similar; check package `com.shrss.core.models`)

---

**Exercise 1.4 — Trace a clientlib from a component (homework)**  
- **Goal:** See how a component references a client library and where that clientlib is built.  
- **Steps:**  
  1. Open a component under `ui.apps/.../apps/shrss/components/` that uses a clientlib (e.g. check `.content.xml` or HTL for `data-sly-use.clientlib` or categories).  
  2. Find the clientlib definition under `ui.apps/.../apps/shrss/clientlibs/` (or embedded in the component).  
  3. In `ui.frontend`, search for the same category or path to see where the JS/SCSS is built and copied into `ui.apps`.  
- **Repo paths:**  
  - Components: `ui.apps/src/main/content/jcr_root/apps/shrss/components/`  
  - Clientlibs: `ui.apps/src/main/content/jcr_root/apps/shrss/clientlibs/`  
  - Frontend source: `ui.frontend/src/` (Webpack builds into clientlibs)

---

## Session 3 & 4 — AEM Application Development Parts 3 & 4

### Backend — OSGi and integrations

**Exercise 2.1 — Find the jobs (Content Fragment) integration in the backend**  
- **Goal:** Locate where jobs/content-fragment configuration is implemented in the core bundle.  
- **Steps:**  
  1. In `core`, search for “Jobs” or “ContentFragment” in service or model names.  
  2. Open `JobsContentFragmentConfigService` (interface) and `JobsContentFragmentConfigServiceImpl` (implementation).  
  3. Note how configuration is read (e.g. OSGi config, resource) and how it is used by models or servlets.  
- **Repo paths:**  
  - `core/src/main/java/com/shrss/core/services/JobsContentFragmentConfigService.java`  
  - `core/src/main/java/com/shrss/core/services/impl/JobsContentFragmentConfigServiceImpl.java`  
  - Related models: `core/src/main/java/com/shrss/core/models/impl/JobListingsImpl.java`, `JobDetailsImpl.java`, etc.

---

### External integrations — GraphQL

**Exercise 2.2 — Locate a GraphQL persistent query**  
- **Goal:** See where persistent queries are defined and how they are named.  
- **Steps:**  
  1. In the repo, search for “persistentQueries” or “graphql”.  
  2. Open the folder that contains persistent query definitions (e.g. under `conf/shrss/settings/graphql/`).  
  3. List the query names (e.g. `getAllJobIds`, `searchLocations`, `getAllEventsDetails`).  
  4. In `core`, search for one of these names to see where the query is invoked (e.g. in a service or model).  
- **Repo paths:**  
  - Persistent queries (in content package): `ui.content/src/main/content/jcr_root/conf/shrss/settings/graphql/persistentQueries/`  
  - Example names: `getAllJobIds`, `searchLocations`, `getAllEventsDetails`, `getAllPromotionsList`, `newsSearchPaginated`, `locationListing`, `searchVenuLocations`, `franchiseLocations`, etc.  
  - Backend usage: search `core/src/main/java` for the query name or “GraphQL” / “persistentQueries”

---

### Frontend

**Exercise 2.3 — Run the frontend build locally (homework)**  
- **Goal:** Run the Webpack build and see output in `ui.apps`.  
- **Steps:**  
  1. From repo root, go to `ui.frontend`.  
  2. Run `npm install` (if not already done).  
  3. Run the build command (e.g. `npm run build` or per project README).  
  4. Confirm that built assets appear under `ui.apps/.../clientlibs/` (or the path documented in implementation notes).  
- **Repo paths:**  
  - `ui.frontend/`  
  - `ui.frontend/package.json`  
  - Build output: typically `ui.apps/src/main/content/jcr_root/apps/shrss/clientlibs/`

---

## Session 5 — Change/Release, DevOps Part 1

### User/group/permission management (IAM → native AEM)

**Exercise 3.1 — IAM group to native AEM group (in-session walk-through)**  
- **Goal:** Create an IAM group in Admin Console, add a user, map the IAM group to a native AEM group in DEV author, and verify.  
- **Steps:**  
  1. In [Admin Console](https://adminconsole.adobe.com/), go to **Users** → **User groups** (or your org’s IAM group section).  
  2. Create a new user group (e.g. “SHRSS DEV Authors – KT Exercise”).  
  3. Add an IAM user to this group (use a user that has or will have the Adobe Experience Manager product profile for **Author – DEV** or equivalent).  
  4. Log into the **DEV author** AEM instance (URL from Cloud Manager or your admin).  
  5. In AEM, go to **Tools** → **Security** → **Groups** (or User Management).  
  6. Open or create a native AEM group (e.g. for authors).  
  7. Add the **IAM group** (by the same name as in Admin Console) to this native AEM group.  
  8. In **Tools** → **Security** → **Users**, find the user and confirm they show membership in the IAM group and the native AEM group.  
- **No repo paths.**  
- **Note:** This is the primary hands-on exercise for the technical KT; a participant can share their screen and perform the steps while the group watches.

---

### Cloud Manager

**Exercise 3.2 — View environments and pipeline in Cloud Manager (in-session or homework)**  
- **Goal:** See where environments, repos, and pipelines are configured.  
- **Steps:**  
  1. Log into Cloud Manager and select the SHRSS program.  
  2. Open **Environments** and note Dev, Stage, Prod (and RDE/Preview if available).  
  3. Open **Pipelines** and select a non-production and/or production pipeline.  
  4. Note the pipeline steps (build, quality, security, deployment, custom testing).  
  5. Optionally: open **Environment variables** (or **Secrets**) for one environment and see how variables are named (do not expose values).  
- **No repo paths.**

---

## Session 6 — DevOps Part 2, Testing, Conclusion

### Testing

**Exercise 4.1 — Run unit tests locally**  
- **Goal:** Run backend unit tests from the `core` module.  
- **Steps:**  
  1. From repo root, run Maven with the test phase for the `core` module, e.g.  
     `mvn clean test -pl core`  
     (or as documented in the project README).  
  2. Note which tests run (e.g. JUnit for models, services).  
  3. Open one test class (e.g. `CardImplTest`) and relate it to the production class (`CardImpl`).  
- **Repo paths:**  
  - `core/pom.xml`  
  - Tests: `core/src/test/java/com/shrss/core/`  
  - Example: `core/src/test/java/com/shrss/core/models/impl/CardImplTest.java`

---

**Exercise 4.2 — Locate integration and UI test entry points (homework)**  
- **Goal:** Know where integration and UI tests live and how they are run.  
- **Steps:**  
  1. Open the `it.tests` module and find the test runner or test class that runs against AEM.  
  2. Open the `ui.tests` module and find the Cypress configuration and a sample spec.  
  3. Read the project README or `pom.xml` for how to run these (often require a running AEM instance and Cloud Manager runs them in the pipeline).  
- **Repo paths:**  
  - `it.tests/`  
  - `ui.tests/`  
  - `it.tests/pom.xml`, `ui.tests/cypress.config.js` (or equivalent)

---

### Conclusion / Q&A

**Exercise 4.3 — Open pipeline logs in Cloud Manager (homework)**  
- **Goal:** Know where to look when a pipeline fails.  
- **Steps:**  
  1. In Cloud Manager, open a pipeline run (e.g. the latest or a failed one).  
  2. Open the **Build** step and skim the log.  
  3. If available, open **Quality** or **Custom Functional Testing** / **Custom UI Testing** and see where test results appear.  
- **No repo paths.**

---

## Quick reference — Repo paths (SHRSS)

| Area | Path (relative to repo root) |
|------|------------------------------|
| Root POM | `pom.xml` |
| Core (Java) | `core/src/main/java/com/shrss/core/` |
| Core tests | `core/src/test/java/com/shrss/core/` |
| Components | `ui.apps/src/main/content/jcr_root/apps/shrss/components/` |
| hrccard component | `ui.apps/src/main/content/jcr_root/apps/shrss/components/hrccard/` |
| Card Sling Model | `core/src/main/java/com/shrss/core/models/impl/CardImpl.java` |
| Clientlibs | `ui.apps/src/main/content/jcr_root/apps/shrss/clientlibs/` |
| Frontend source | `ui.frontend/src/` |
| OSGi configs | `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/` |
| Jobs CF config service | `core/src/main/java/com/shrss/core/services/impl/JobsContentFragmentConfigServiceImpl.java` |
| Persistent queries | `ui.content/src/main/content/jcr_root/conf/shrss/settings/graphql/persistentQueries/` |
| Dispatcher | `dispatcher/` |
| Integration tests | `it.tests/` |
| UI tests | `ui.tests/` |

---

*End of exercise supplemental. Use with the refined agenda: `SHRSS_Technical_KT_Main_Agenda_Refined.md`*
