# AEM Project Bootstrap Guide for AI Agents

Purpose: Help AI agents quickly understand an unfamiliar Adobe
Experience Manager (AEM) codebase.

This guide defines a standard inspection workflow agents should follow
when entering a repository for the first time. The goal is to rapidly
determine:

-   AEM platform type (AEMaaCS vs 6.5)
-   project structure
-   deployment model
-   dispatcher configuration
-   content architecture
-   integration patterns

This document complements:

-   AEM_AGENT_EXECUTION_TEMPLATE.md
-   AEM_TOPIC_ONTOLOGY.md
-   AEM_REFERENCE_SYSTEM.md

Agents should use this guide **before beginning implementation tasks**
in a new repository.

------------------------------------------------------------------------

## Bootstrap Workflow

Agents should perform the following steps when analyzing a new AEM
project.

First, review the `AEM_DELTAS_6_5_vs_AEMaaCS.md`.

------------------------------------------------------------------------

### Step 1 — Identify AEM Platform Type

Check for indicators of **AEM as a Cloud Service**.

Look for:

The AEMaaCS SDK (`aem-sdk-api`) dependency in the project root POM.xml file:

```java
<dependency>
  <groupId>com.adobe.aem</groupId>
  <artifactId>aem-sdk-api</artifactId>
  <version>${aem.sdk.api}</version>
  <scope>provided</scope>
</dependency>
```

Cloud Manager folder in repo

    .cloudmanager/

If these patterns exist, it is an **AEMaaCS** project.

------------------------------------------------------------------------

### Step 2 — Identify Project Archetype Structure

Most modern AEM projects follow the Adobe archetype. The current archetype and prior versions live here: https://github.com/adobe/aem-project-archetype.

The archetype is made up of modules, all of which are created automatically when using the archetype.

- **[core](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/core)** is a Java bundle containing all core functionality like OSGi services, listeners, and schedulers, as well as component-related Java code such as servlets and request filters.
- **[it.tests](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/it.tests)** are Java-based integration tests.
- **[ui.apps](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.apps)** contains the `/apps` and `/etc` parts of the project, i.e. JS and CSS clientlibs, components, and templates.
- **[ui.content](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.content)** contains sample content using the components from the ui.apps module.
- **[ui.config](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.config)** contains runmode-specific OSGi configs for the project.
- **[ui.frontend.general](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.frontend.general)** contains the artifacts required to use the general Webpack-based front-end build module (optional).
- **[ui.frontend.react](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.frontend.react)** **(optional)** contains the artifacts required when using the archetype to create a SPA projects based on React (optional, depends on build parameters).
- **[ui.frontend.angular](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.frontend.angular)** **(optional)** contains the artifacts required when using the archetype to create a SPA projects based on Angular (optional, depends on build parameters).
- **[ui.tests](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/ui.tests)** contains Selenium-based UI tests.
- **[all](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/all)** is a single content package that embeds all of the compiled modules (bundles and content packages) including any vendor dependencies.
- **[dispatcher.ams](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/dispatcher.ams)** contains the basic dispatcher configurations for AMS/on-prem projects(optional, depends on build parameters).
- **[dispatcher.cloud](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/dispatcher.cloud)** contains the basic dispatcher configurations for AEMaaCS projects (optional, depends on build parameters).

Agents should map responsibilities of each module.

------------------------------------------------------------------------

### Step 3 — Inspect Sling Model Layer

Search for:

    core/src/main/java/**/models

Identify:

-   Sling Model classes
-   injection patterns
-   dependency usage
-   service integrations

Confirm models are used instead of business logic in HTL.

------------------------------------------------------------------------

### Step 4 — Inspect Component Structure

Check:

    ui.apps/src/main/content/jcr_root/apps/

Identify:

-   component hierarchy
-   resource types
-   dialogs
-   HTL templates

Determine whether components:

-   extend Core Components
-   are custom implementations

------------------------------------------------------------------------

### Step 5 — Inspect Dispatcher Configuration

Locate:

    dispatcher/
    dispatcher/src/conf.d/

Review:

-   filter rules
-   cache rules
-   invalidation configuration
-   virtual hosts

Confirm:

-   default-deny filters
-   cache coverage for public content

------------------------------------------------------------------------

### Step 6 — Inspect Content Architecture

Look for:

-   Content Fragments
-   Experience Fragments
-   Templates
-   Page structures

Paths to inspect:

    /conf
    /content
    /apps

Identify whether the project is:

-   traditional Sites, Assets, or both
-   headless
-   hybrid

------------------------------------------------------------------------

### Step 7 — Inspect OSGi Configuration

**AEM 6.5/6.5 LTS On-Premis/AMS**

Search:

    ui.apps/src/main/content/jcr_root/apps/**/config*

**AEMaaCS**

Search:

    ui.config/src/main/content/jcr_root/**/config*/**

Identify:

-   service configurations
-   environment-specific configs
-   runmode usage

In AEMaaCS, configuration should be immutable and deployed via code.

------------------------------------------------------------------------

### Step 8 — Inspect Integrations

Search for:

External APIs Adobe services Authentication mechanisms

Look for:

-   HTTP clients
-   service integrations
-   external endpoints

------------------------------------------------------------------------

### Step 9 — Determine Deployment Model

Inspect:

    pom.xml

and build configuration.

Look for:

-   Cloud Manager integration
-   Maven modules
-   deployment packaging

Confirm deployment pipeline expectations.

---

### Step 10 — Apply Repository Heuristics

After identifying project structure, apply:

`@docs/ai/reference/AEM_REPO_HEURISTICS.md`

This detects architectural risks and modernization opportunities.

------------------------------------------------------------------------

## Bootstrap Output

After performing the inspection, agents should produce a short project
profile containing:

Platform

-   AEMaaCS or AEM 6.5

Project structure

-   archetype modules
-   custom modules

Architecture style

-   Sites
-   Headless
-   Hybrid

Dispatcher configuration status

-   caching strategy
-   filter model

Content architecture

-   fragments
-   templates
-   page hierarchy

Integration points

-   external services
-   APIs

------------------------------------------------------------------------

## Example Project Summary

Example output:

Platform

AEM as a Cloud Service

Project modules

core ui.apps ui.content ui.frontend dispatcher

Architecture

Hybrid Sites + Headless

Dispatcher

Default-deny filters present Caching enabled for public content

Content architecture

Content fragments used for headless delivery

------------------------------------------------------------------------

## Design Goal

This guide enables agents to:

-   understand unfamiliar AEM repositories quickly
-   detect architectural patterns
-   identify platform constraints
-   ground implementation decisions in project structure

Agents should perform this bootstrap analysis before executing
development tasks.
