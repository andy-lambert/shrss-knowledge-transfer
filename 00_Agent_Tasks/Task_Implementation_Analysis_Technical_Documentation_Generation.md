# SHRSS Implementation Analysis and Technical Documentation

## Why This Task Exists (Read First)

This task exists to generate technical documentation for the SHRSS technical stakeholders that will be taking ownership of the platform, including new development and operations.

The primary output is comphrehensive technical documentation of the implementation **architecture and interactions**.

---

## Your Task

Execute deep analysis on, and thoroughly document, all facets of the end-to-end application implementation.

The documentation **MUST** include: **structural** architecture and **cross-layer interaction** architecture. Detailed requirements for each of these **focus areas** is provided below.

- I have organized the task into two phases:  *Phase 1 - Deep Analysis* and *Phase 2 - Document Findings*. Specific instructions for each phase are described lower in this file.
- Generate all documentation in markdown, optimized for humans.

---

## Phase 1 - Deep Analysis

Execute a deep analysis of the following project artifacts at the necessary level of granularity to meet all documentation requirements in *Phase 2 - Document Findings*:

- **Current implementation codebase** - *Informs actual implementation reality*: 
  - Code in currently checked out branch (`develop`) of the repo at: `/Users/lambert/Documents/Projects/SHRSS/Code/shrss-aem-projects`

⚠️ **IMPORTANT NOTE:** Given the scope of this effort, execute several rounds of pre-analysis and data gathering/organizaton before commencing with the deeper cross analysis.

---

## Phase 2 - Document Findings

### Focus Areas

#### 1. Structural Architecture

> “What exists and what it owns”

A canonical inventory of the application’s components across all layers, defining **what exists**, **what each element owns**, and **what it is allowed to depend on**, without describing runtime behavior or execution flow.

> The Structural Architecture **does not** describe:
>
> - Request or execution flow
> - Call sequences
> - Data movement across layers
> - Runtime behavior
>
> Those concerns belong exclusively to **Cross-Layer Interaction Architecture**.

> If you can delete a component without explaining how anything breaks at runtime, it belongs in Structural Architecture.
>  If you must explain what calls it or when it runs, it belongs in Cross-Layer Interaction Architecture.

**Each entry MUST provide:**

- Responsibilities
- Inputs / outputs
- Lifecycle
- Dependency boundaries
- Constraints

##### Dependency Direction Rule (Non-Negotiable)

Structural Architecture entries MUST declare allowed and prohibited dependencies.
Unlisted dependencies are assumed prohibited.

**Structural Architecture — Entry Template (Agent Ready)**

```text
### Structural Element: <Name>
Type: <AEM Component (HTL/Client) | OSGi Component () | Clientlib | Frontend Module | Dispatcher Config | other>  
**Layer**: <Frontend (ui.apps, ui.frontend) | Conf (ui.content /conf) | Backend>  
**Source of Truth**: <code/config path(s) + key file(s)>

---

#### Purpose
<One paragraph: what it exists to do. No implementation details, no speculation.>

---

#### Responsibilities
- <Responsibility 1>
- <Responsibility 2>
- <Responsibility 3>

---

#### Public Surface Area
> What other parts of the system can “touch.”

- **Entry points**:
  - <HTTP endpoint | Sling resource type | JS entry module | event topic | workflow process label | scheduler name | other>
- **Inputs**:
  - <request params, authored props, selectors, headers, config keys, runtime context, other>
- **Outputs**:
  - <rendered markup, JSON schema, side effects, persisted nodes, emitted events, other>

---

#### Runtime Context
- **Invocation style**: <synchronous | async | event-driven | scheduled>
- **Lifecycle**: <request-scoped | singleton | OSGi DS | per-component render | build-time | other>

---

#### Dependencies
> Declare boundaries explicitly.

- **Direct dependencies (allowed)**:
  - <Element -> depends on -> Element> (with reason)
- **External dependencies**:
  - <external system/API> (auth, timeouts, retries if known)
- **Prohibited dependencies**:
  - <what it must NOT call/use> (and why)

---

#### Configuration & Variability
- **OSGi / runmode config**: <config path / key settings>
- **Content/config dependencies**: <ui.content /conf policies, templates, content fragments, tags>
- **Feature flags / toggles**: <if any>

---

#### Data
- **Reads**:
  - <JCR paths/properties, external data, caches, other>
- **Writes/Side effects**:
  - <JCR writes, replication, logs, outbound calls, other>
- **Data contracts**:
  - <schemas, property names, expected shapes, other>

---

#### Known Risks / Ambiguities
- **Risk**: <summary> — <impact> — <evidence>
- **Ambiguity**: <what is unclear> → record as Decision Candidate if unresolved

---

#### Related Cross-Layer Interactions
- ⟦Interaction: <Scenario Name>⟧
- ⟦Interaction: <Scenario Name>⟧

---

#### References
- `SOLUTION_DESIGN.md` ⟦SDD §x.x⟧
- `DECISIONS.md` ⟦DR-xxxx⟧
- **Code**: `<path>` (and key classes/files)
```

##### Key Application Modules & Folders

*See the description and specific documentation guidelines under each module/folder below. The guidelines inform the type of content to include along with minimum requirements; however, be opinionated about what else would be useful for future agents that will be working on this project. Recommend additional sections/details/diagrams that could be instrumental in providing context, coding standards, and guardrails to future agents. Always pause, present recommendations, and get approval before implementing. Follow the STOP protocol rule (`@stop-protocol`)*

---

##### core
---
**Description:** OSGi bundle. Contains the Java code for backend services, models, and business logic. Uses OSGi for dependency injection, Sling models for exposing content to Sling scripts and JUnit for unit testing.

**Guidelines:**

- Include an analysis of the settings and configurations in the module's POM `(core/pom.xml)`, including a description of what functionality the specific configured plugins do, and the constraints/guardrails they provide. DO NOT list all module dependencies in the POM.
- Include both the `core/bin` and `core/src` folders in the analysis and documentation
- Describe all packages and their OSGi components and other classes (bean, caconfig, commerce, config, constants, filters, listeners, models, schedulers, services, servlets, utils, workflows)
  - Reference corresponding OSGi configuration files in the `ui.config` module as applicable.
  - Describe corresponding unit tests in `core/src/test`. Highlight where a class/method is missing test coverage that should be added. Mark as *TODO* for future reference.
- Include sections for naming conventions and coding conventions/standards.

---

##### dispatcher
---
**Description:** Contains the cloud-optimized Apache and AEM Dispatcher configurations, including caching and security settings. Uses immutable files that are validated by the Dispatcher SDK.

**Guidelines:**

- Include purpose of main files, both Apache configs and dispatcher module configs
- Include major confguration settings and impications
- Include outline and diagram to convey relationships of files (parent files, includes, aliases)

---

##### ui.apps
---
**Description:** FileVault content package. Contains the application code, including AEM  authoring/page components, templates, and client libraries (clientlib definitions). Uses HTL as the scripting engine.

**Guidelines:**

- Include:
  - Custom AEM components (`ui.apps/src/main/content/jcr_root/apps/shrss`)
  - OOTB AEM component and clientlibs extensions (`ui.apps/src/main/content/jcr_root/apps/settings`)

- Include an analysis of the settings and configurations in the module's POM `(ui.apps/pom.xml)`, including a description of what functionality the specific configured plugins do, and the constraints/guardrails they provide. DO NOT list all module dependencies in the POM.
- Include an analysis of the module's Vault filter settings including the constraints and implications of each filter's mode, and include/exclude elements (`ui.apps/src/main/content/META-INF/vault/filter.xml`)

---

##### ui.apps.structure
---
**Description:** FileVault content package. Empty module that defines the structure of the repository content.

**Guidelines:**

- Include an analysis of the settings and configurations in the module's POM `(ui.apps.structure/pom.xml)`, including a description of what functionality the specific configured plugins do, and the constraints/guardrails they provide. DO NOT list all module dependencies in the POM.

---

##### ui.config
---
**Description:** FileVault content package. Contains OSGi configurations for the application.

**Guidelines:**

- Organize the configuration documentation by the files' parent folders , which correspond to AEM run modes. (*Example: `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/config.author`*)
- Document the purpose, construction, and properties set in each configuration file
- Include correlation of each configuration file to its corresponding OSGi component
- Include detailed analysis of **service user mapping** and **repository initializer** configurations:
  - Service user mappings
    - `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/config/org.apache.sling.serviceusermapping.impl.ServiceUserMapperImpl.amended~shrss.cfg.json`
  - Repository Initializers
    - Author
      - `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/config.author/org.apache.sling.jcr.repoinit.RepositoryInitializer~shrss.cfg.json`
    - Publish
      - `ui.config/src/main/content/jcr_root/apps/shrss/osgiconfig/config.publish/org.apache.sling.jcr.repoinit.RepositoryInitializer~shrss.cfg.json`

---

##### ui.content
---
**Description:** FileVault content package. Contains the default mutable content for the application, such as the initial site structure and bas pages and sample/base assets. 

In addition, the `conf` folder contains page templates and template policies, content fragment model configurations, DAM asset metadata schemas, workflow model configurations, etc.

**Guidelines:**

- Include details for:
  - *Default content* in the following folders under `ui.content/src/main/content/jcr_root/content`: _cq_graphql, dam (assets), experience-fragments, shrss (site pages)
  - *Configurations and settings* in the following folders under `ui.content/src/main/content/jcr_root`: conf, etc, var
- Include an analysis of the settings and configurations in the module's POM `(ui.content/pom.xml)`, including a description of what functionality the specific configured plugins do, and the constraints/guardrails they provide. DO NOT list all module dependencies in the POM.
- Include an analysis of the module's Vault filter settings including the constraints and implications of each filter's mode, and include/exclude elements (`ui.content/src/main/content/META-INF/vault/filter.xml`)

---

##### ui.frontend
---
**Description:** Frontend module built with Webpack. Compiles TypeScript/JavaScript and Sass/SCSS. During the build it is copied to the `ui.apps` module as client libraries (clientlibs). Uses Node.js, npm, and webpack.

**Guidelines:**

- Include details of NPM package definition: `ui.frontend/package.json`
- Webpack components and configurations: `ui.frontend/src/main/webpack`
- JavaScript/TypeScript/CSS:
  - Frameworks and architectural/design patterns/paradigms
  - Coding conventions
  - Naming conventions

- Linter configurations/validation settings
- Clientlib configurations

---

##### it.tests
---
**Description:** Integration tests module. Uses the AEM Testing clients to run tests against running AEM instances. Executed by Cloud Manager during the *Custom Functional Testing* step of a full stack pipeline.

**Guidelines:**

- Include details of integration test classes
- Include an analysis of the settings and configurations in the module's POM `(it.tests/pom.xml)`, including a description of what functionality the specific configured plugins do, and the constraints/guardrails they provide. DO NOT list all module dependencies in the POM.

---

##### ui.tests
---
**Description:** UI tests module. Uses Cypress to run end-to-end tests against running AEM instances. Executed by Cloud Manager during the *Custom UI Testing* step of a full stack pipeline.

**Guidelines:**

- Include Docker, Cypress, reporter configs and test modules

---

##### all
---
**Description:** FileVault content package. Includes all other FileVault packages for easy deployment.

**Guidelines:**

- Include an analysis of the settings and configurations in the module's POM `(all/pom.xml)`, including a description of what functionality the specific configured plugins do, and the constraints/guardrails they provide. DO NOT list all module dependencies in the POM.
- Include an analysis of the module's Vault filter settings including the constraints and implications of each filter's mode, and include/exclude elements (`all/src/main/content/META-INF/vault/filter.xml`)

---

##### acl
---
**Description:** Defines base user groups and ACLs. Based on *Netcentric - Access Control Tool for Adobe Experience Manager*, version 3.0.10 (https://github.com/Netcentric/accesscontroltool/tree/3.0.10)

**Guidelines:**

- Include details of user group/ACL configurations in `acl/src/main/content/jcr_root/apps/shrss/acl/dam-groups.yaml`
- Include an analysis of the module's Vault filter settings including the constraints and implications of each filter's mode, and include/exclude elements (`acl/src/main/content/META-INF/vault/filter.xml`)

---

##### config
---
**Description:** CDN rules and maintenance task configurations

**Guidelines:**

- Include details of CDN rule and maintenance task configuration files under `config`

---

## 2. Cross-Layer Interaction Architecture
> “How the system actually behaves” 
>
> A scenario-based description of how frontend components, backend models, services, servlets, and external integrations collaborate at runtime to produce application behavior.
>
> This section documents **execution flow, data movement, responsibility handoffs, and failure paths** across layers. It does not redefine component responsibilities—that is the role of **Structural Architecture**.

### Cross-Layer Interaction Architecture — Entry Template (Agent Ready)

```java
### Interaction: <Scenario Name>
<One sentence describing the user or system-triggered behavior>

---

#### Trigger
- <User action, system event, or request type>
- <e.g., HTTP GET /locations, page render, client-side filter change>

---

#### Participating Elements (Ordered)
> List elements in the order they participate at runtime.

1. <Frontend component / client>
2. <AEM component (HTL)>
3. <Sling Model>
4. <Servlet / API>
5. <OSGi Service(s)>
6. <External system (if any)>

---

#### Execution Flow
> Step-by-step, present tense, no speculation.

1. <What initiates the flow>
2. <What component/model is invoked and why>
3. <What data is passed or transformed>
4. <What service or API is called>
5. <What is returned and to whom>
6. <What is rendered or delivered to the client>

---

#### Data Flow & Ownership
- **Primary data owner**: <system/component>
- **Read-only consumers**: <list>
- **Transformations**:
  - <where data shape changes>
- **Caching points**:
  - <dispatcher, CDN, service cache, browser>

---

#### Contracts & Assumptions
> These must be true for the interaction to remain valid.

- <e.g., JSON schema stability>
- <e.g., required headers, tokens, tags>
- <e.g., component policy guarantees>

---

#### Error & Failure Paths
> What happens when things go wrong?

- <External API unavailable>
- <Token expired>
- <Invalid authored configuration>
- <Network / timeout failure>

For each:
- Detection point
- Fallback behavior (if any)
- User-visible impact

---

#### Performance & Scale Considerations
- <Synchronous vs async>
- <Expected frequency>
- <Hot path? yes/no>
- <Known bottlenecks>

---

#### Security & Access Boundaries
- Authentication context (anonymous / authenticated)
- Authorization assumptions
- Secret handling (if applicable)
- Prohibited behaviors

---

#### Related Structural Elements
> Explicit linkage back to Structural Architecture.

- <Component: X>
- <Sling Model: Y>
- <Service: Z>

---

#### References
- `SOLUTION_DESIGN.md` ⟦SDD §x.x⟧
- `DECISIONS.md` ⟦DR-xxxx⟧
- <Code paths / tickets>
```
