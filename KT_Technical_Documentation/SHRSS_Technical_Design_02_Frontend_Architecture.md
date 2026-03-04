# SHRSS Technical Design — Frontend Architecture

**Layer:** UI/Frontend (ui.apps + ui.frontend)  
**Purpose:** Structural architecture of AEM components, clientlibs, and frontend build.

---

## 1. Overview

**Modules:** `ui.apps` (FileVault content package), `ui.frontend` (Webpack build)  
**Target:** AEMaaCS  
**Source:** `ui.apps/`, `ui.frontend/` at repository root

The frontend layer contains AEM authoring components (HTL), client library definitions, and frontend assets (TypeScript/JavaScript, Sass/SCSS) built by Webpack and deployed into ui.apps as clientlibs.

### Scope (Codebase Counts)

- **AEM components:** 95 custom authoring components under `ui.apps/.../apps/shrss/components/` (each with a `.content.xml` defining `cq:Component`; includes structure/page, structure/open-page, structure/blank-page, form/*, video/embeddable/*, accordion, container, jobsearch, jobfilters, cfcard, cfcardlist, etc.).
- **Content Fragment models:** 6 models in `ui.content/.../conf/shrss/settings/dam/cfm/models/` — events, news, promotion, locations, venue, jobs (no separate FAQ model in this path).
- **Clientlibs:** Categories such as `shrss.base`, `shrss.site`, `shrss.components`, and brand-specific (e.g. `shrss.hrhh`, `shrss.hrcasino`, `shrss.hrhcasino`).

---

## 2. Module: ui.apps

**Path:** `ui.apps/`  
**Type:** FileVault content package  
**Purpose:** AEM authoring components, HTL templates, clientlib definitions, content structure.

### Key Paths

- **Custom components:** `ui.apps/src/main/content/jcr_root/apps/shrss/components/`
- **Clientlibs:** `ui.apps/src/main/content/jcr_root/apps/shrss/clientlibs/`
- **i18n:** `ui.apps/src/main/content/jcr_root/apps/shrss/i18n/`
- **Settings (OOTB extensions):** `ui.apps/src/main/content/jcr_root/apps/settings/` (merge mode in filter)

### Build and Vault Filter

- **FileVault Package Maven Plugin** packages JCR content; **HTL Maven Plugin** validates HTL at build time.
- **Filter (vault/filter.xml):** Defines included paths and modes (replace vs merge). `/apps/settings` is typically merge to preserve OOTB configurations.

---

## 3. Module: ui.frontend

**Path:** `ui.frontend/`  
**Type:** Webpack-based frontend build  
**Purpose:** Compile TypeScript/JavaScript and Sass/SCSS into clientlibs consumed by ui.apps.

### Build Output

- Compiled assets are copied to `ui.apps/src/main/content/jcr_root/apps/shrss/clientlibs/` (or equivalent per project layout).
- **clientlib.config.js** defines how Webpack output maps to clientlib categories and embed structure.

### Conventions

- **Languages:** TypeScript/JavaScript (ES6+), Sass/SCSS.
- **Multi-brand:** Separate entry points and/or brand-specific Sass variables; shared component library with brand overrides.
- **Optimization:** Code splitting, tree shaking, asset optimization (images, fonts).

---

## 4. Component Categories (Summary)

| Category | Examples |
|----------|----------|
| **Content** | hero, text, title, image, video, teaser, RTE |
| **Container** | container, panelcontainer, tabs, accordion, carousel |
| **Navigation** | header, footer, breadcrumb, mainnavigation, languagenavigation |
| **Form** | form, formcontainer, button, text, options, hidden |
| **Experience Fragment** | experiencefragment, xfpage |
| **Search / Filter** | search, jobsearch, newssearch, promotionsearch, destinationsearch |
| **Integration** | crowncta (Unity iframe), googlemap, bookingwidget, cafedeliverywidget |
| **List / Display** | list, imagelist, cfcardlist, locationList, categorylisting |

### Component Patterns

- **Core Component extension:** Many components use `sling:resourceSuperType` to extend Core Components (e.g. hero extends teaser, breadcrumb extends Core Breadcrumb).
- **Custom components:** Full custom implementations with Sling Model + HTL; dialogs under `_cq_dialog/`, design under `_cq_design_dialog/`.
- **CommonFields:** Shared dialog tabs (styling, analytics, SEO) inherited by content components.

---

## 5. Notable Components (Examples)

- **Hero:** Full-width hero; image/video; parallax; extends Core Teaser. Model: HeroModel.
- **Container:** Responsive grid; background/padding options; GLightbox, parallax. Model: ContainerModel.
- **Header:** Site header; main navigation; responsive; Unity login orchestration (iframe). Model: HeaderModel.
- **jobsearch / jobfilters:** Careers job search and filters; backend servlet + frontend JS for filtering/sorting; updated for accessibility and sort options.
- **cfcard / cfcardlist:** Content Fragment card display; GraphQL/CF-backed; CFCardUtils in core.
- **promotionsearch:** Promotion search and filtering; CF-backed.
- **Accordion:** Collapsible sections; Core Accordion extension; transparent variation style added.
- **Crown CTA:** Unity login/registration iframe modal (frontend iframe integration).
- **Google Map:** Embedded Google Maps; API key configuration.

---

## 6. Content Fragment Models

**Location (example):** `ui.content/.../conf/shrss/settings/dam/cfm/models/` (or equivalent in content package).

**Models (6):** events, news, promotion, locations, venue, jobs (in `ui.content/.../conf/shrss/settings/dam/cfm/models/`).

**Usage:** Rendered via cfcard, cfcardlist, and dedicated CF components; exposed via GraphQL for headless consumption.

---

## 7. Recent Frontend Additions (Post–Analysis)

Examples of changes after the baseline analysis:

- **Careers:** jobsearch, jobfilters components (HTL + frontend TS/SCSS); sort options, accessibility, scroll behavior; header/favicon logic for Careers site; Careers favicons and apple-touch-icons in `ui.frontend` (e.g. `site/master/resources/careers/`).
- **Accordion:** Transparent variation style.
- **CFCard / cfcard:** Component and CFCardUtils (core) updates.
- **Header:** Reverb-specific styles, logo/favicon handling, dropdown/button styles.
- **clientlib.config.js:** Updates for clientlib mapping.
- **Stories:** jobSearch, accordion, cards (Storybook-style stories in ui.frontend).

---

## 8. Dependency Direction

- **HTL** uses Sling Models (data-sly-use) and includes other components (data-sly-resource).
- **Clientlibs** are requested by component categories; frontend build produces the assets that satisfy those categories.
- **No direct** frontend-to-OSGi-service binding; data flows via models or servlets.

---

*For runtime behavior and component interactions, see `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md`. For integrations (Unity, OpenTable, etc.), see `SHRSS_Technical_Design_03_Integrations.md`.*
