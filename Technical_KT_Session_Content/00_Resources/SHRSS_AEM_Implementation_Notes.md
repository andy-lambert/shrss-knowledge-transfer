# SHRSS AEM Implementation Notes

## Source Code: Key Application Modules & Folders

---

##### core
---
**Description:** OSGi bundle. Contains the Java code for backend services, models, and business logic. Uses OSGi for dependency injection, Sling models for exposing content to Sling scripts and JUnit for unit testing.

---

##### dispatcher
---
**Description:** Contains the cloud-optimized Apache and AEM Dispatcher configurations, including caching and security settings. Uses immutable files that are validated by the Dispatcher SDK.

---

##### ui.apps
---
**Description:** FileVault content package. Contains the application code, including AEM  authoring/page components, templates, and client libraries (clientlib definitions). Uses HTL as the scripting engine.

---

##### ui.apps.structure
---
**Description:** FileVault content package. Empty module that defines the structure of the repository content.

---

##### ui.config
---
**Description:** FileVault content package. Contains OSGi configurations for the application.

---

##### ui.content
---
**Description:** FileVault content package. Contains the default mutable content for the application, such as the initial site structure and bas pages and sample/base assets. 

---

##### ui.frontend
---
**Description:** Frontend module built with Webpack. Compiles TypeScript/JavaScript and Sass/SCSS. During the build it is copied to the `ui.apps` module as client libraries (clientlibs). Uses Node.js, npm, and webpack.

---

##### it.tests
---
**Description:** Integration tests module. Uses the AEM Testing clients to run tests against running AEM instances. Executed by Cloud Manager during the *Custom Functional Testing* step of a full stack pipeline.

---

##### ui.tests
---
**Description:** UI tests module. Uses Cypress to run end-to-end tests against running AEM instances. Executed by Cloud Manager during the *Custom UI Testing* step of a full stack pipeline.

---

##### all
---
**Description:** FileVault content package. Includes all other FileVault packages for easy deployment.

---

##### acl
---
**Description:** Defines base user groups and ACLs. Based on *Netcentric - Access Control Tool for Adobe Experience Manager*, version 3.0.10 (https://github.com/Netcentric/accesscontroltool/tree/3.0.10)

---

##### config
---
**Description:** CDN rules and maintenance task configurations
