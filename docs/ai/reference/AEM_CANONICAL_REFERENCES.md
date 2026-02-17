# AEM Canonical References
**Version:** 1.0.0  
**Last Updated:** 2025-12-29  
**Applies To:** AEM as a Cloud Service (AEMaaCS)

## Purpose
This document is the **authoritative canonical reference index** for:
- AI agents operating in AEM codebases
- Human developers
- Governance, standards, and design reviews

It intentionally links **only to primary sources**:
- Adobe Experience League
- Apache upstream projects (Sling, Oak, Felix)
- Adobe public GitHub repositories

## Canonical Source Hierarchy (Authority Order)
1. **Adobe Experience League** – Product behavior & constraints
2. **Apache Project Docs** – Sling / Oak / OSGi fundamentals
3. **Adobe GitHub** – Reference implementations (not specs)

Agents **MUST** prefer higher-ranked sources when conflicts exist.

---

## 1) RepoInit & Bootstrap Configuration (AEMaaCS)
### Canonical Docs
- RepoInit (AEMaaCS)  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-repo-init
- RepoInit Syntax  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-repo-init#syntax

### AI Agent Guidance
**DO**
- Use RepoInit for users, groups, ACLs, and service users
- Treat RepoInit as environment-safe, idempotent configuration

**DO NOT**
- Package users or ACLs via content packages in AEMaaCS
- Assume RepoInit exists in AEM 6.5

**CLOUD ONLY**
- RepoInit is mandatory in AEMaaCS and ignored in AEM 6.5

---

## 2) Component Development (HTL & Core Components)
### Canonical Docs
- Core Components Overview  
  https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction
- Developing AEM Components
 https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/components/developing-components?utm_source=chatgpt.com
- HTL Overview  
  https://experienceleague.adobe.com/en/docs/experience-manager-htl/using/overview
- Touch UI Concepts (for authoring UI context)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/introduction/touch-ui-concepts

### AI Agent Guidance
**DO**
- Prefer extending Core Components before creating net-new custom components
- Keep business logic in Java (Sling Models / services), keep HTL as a view layer

**DO NOT**
- Embed business logic in HTL templates
- Introduce legacy JSP patterns for new work
---

## 3) Frontend & Clientlibs Development (JS/CSS)
### Canonical Docs
- Front-End Development with the AEM Project Archetype  
  https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/front-end
  
- Using Client-Side Libraries  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/introduction/clientlibs
  
- Review the full-stack AEM project's 'ui.frontend' module

  https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/enable-frontend-pipeline-devops/review-uifrontend-module

---

## 4) Sling Models (Backend Contract Layer)
### Project Rules (Non-Negotiable)

- `@sling-models.md`

### Canonical Docs

- Sling Models (Apache)  
  https://sling.apache.org/documentation/bundles/models.html
- AEM Sling Models (6.5 guidance)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/components/sling-models

### AI Agent Guidance
**DO**
- Use constructor injection and keep models cohesive
- Prefer interfaces and small models, compose in services when needed

**DO NOT**
- Build “god models” that traverse large parts of the repository
- Depend on request attributes set by unrelated filters/servlets

---

## 5) OSGi, Services & Runtime Constructs
### Canonical Docs
- Apache Felix (OSGi)  
  https://felix.apache.org/documentation/index.html
- OSGi in AEM 6.5  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/platform/osgi
- OSGi in AEMaaCS  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-osgi

### Runtime Constructs (Upstream)
- Sling Servlets  
  https://sling.apache.org/documentation/the-sling-engine/servlets.html
- Sling Filters  
  https://sling.apache.org/documentation/the-sling-engine/filters.html
- Sling Jobs / Eventing  
  https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html
- Scheduler Service  
  https://sling.apache.org/documentation/bundles/scheduler-service.html
- Sling Post Processor  
  https://sling.apache.org/documentation/bundles/post-processor.html

### AI Agent Guidance
**DO**
- Externalize configuration; assume immutable deployment patterns in AEMaaCS
- Keep services stateless; store state in repository or external systems where appropriate

**DO NOT**
- Persist mutable state in OSGi singletons
- Use runmode-dependent code paths as a Cloud strategy

---

## 6) Service Users & Security
### Canonical Docs
- Service Users (6.5)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/platform/service-users
- AEMaaCS Security Overview  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/security

### AI Agent Guidance
**DO**
- Use least-privilege service users with subservice mappings
- Prefer ResourceResolverFactory + service user auth patterns

**DO NOT**
- Use administrative sessions
- Use deprecated SlingRepository login approaches

---

## 7) Workflows & Custom Workflow Development
### Canonical Docs
- Custom Workflow Steps (6.5) 
  - https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/extending-aem/custom-workflow-steps
  - https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/extending-aem/extending-workflows/workflows-step-ref
  - Implementing a custom workflow process step: https://experienceleague.adobe.com/en/docs/experience-manager-learn/forms/custom-workflow-component/custom-process-step-aem-workflow
  
- Workflows in AEMaaCS  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/workflows

### AI Agent Guidance
**DO**
- Keep workflow steps idempotent and retry-safe
- Design with asynchronous execution and transient failures in mind (Cloud)

**DO NOT**
- Depend on local filesystem access
- Assume long-running synchronous steps are safe in Cloud

---

## 8) Dispatcher
### Canonical Docs
- Dispatcher Overview  
  https://experienceleague.adobe.com/en/docs/experience-manager-dispatcher/using/dispatcher
- Dispatcher in AEMaaCS  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/dispatcher/overview
- Dispatcher Configurations in AEMaaCS  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/dispatcher/dispatcher-configurations

### AI Agent Guidance
**DO**
- Use default-deny filters and explicitly allow required paths
- Treat dispatcher config as immutable and Git-delivered in AEMaaCS

**DO NOT**
- Modify dispatcher directly on running Cloud environments

---

## 9) Querying, Indexing & Performance
### Project Rules (Non-Negotiable)

- `@jcr-sql2-performance-guide.md`

### Canonical Docs

- Query and Indexing Best Practices: 

  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices

- Keyset Pagination
  
  https://jackrabbit.apache.org/oak/docs/query/query-engine.html#Keyset_Pagination
  
- Apache Oak (JCR & indexing)  
  https://jackrabbit.apache.org/oak/docs/
  
- Query Builder (AEM 6.5)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/platform/query-builder
  
- Indexes in AEMaaCS  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/indexing

### AI Agent Guidance
**DO**
- Explain/measure every query (use “explain query” tooling)
- Add explicit indexes for new high-traffic queries
- Implement keyset pagination for large result sets

**DO NOT**
- Rely on traversal queries
- Modify OOTB indexes in AEMaaCS (prefer additive custom indexes)

---

## 10) Touch UI, Granite/Coral UI & UI Extensibility
### Canonical Docs
- Touch UI Concepts (6.5)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/introduction/touch-ui-concepts
- Granite UI (6.5)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/components/granite-ui
- Cloud UI Extensibility Overview  
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/extensibility/ui/overview
- Adobe Developer Console – AEM UI Extensions  
  https://developer.adobe.com/uix/docs/services/aem-cf-console-admin/extension-development/

### AI Agent Guidance
**DO**
- Use supported extensibility points (UI Extensions) for Cloud consoles
- Prefer React Spectrum for Cloud extension UIs

**DO NOT**
- Inject arbitrary JS/CSS into Cloud authoring consoles as a customization strategy

---

## 11) React Spectrum (Modern UI Layer)
- React Spectrum  
  https://react-spectrum.adobe.com/
- Spectrum Design System  
  https://spectrum.adobe.com/

---

## 12) Assets (DAM), Metadata, APIs & Dynamic Media
- AEM Assets (entry point)  
  https://experienceleague.adobe.com/en/docs/experience-manager-assets
- Assets API Overview (AEMaaCS)  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/assets-api-overview
- Metadata Schemas (6.5)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/metadata-schemas
- Metadata configuration concepts (6.5)  
  https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/managing/metadata-config
- Dynamic Media (AEMaaCS)  
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media

---

## 13) Adobe AEM 6.5 Documentation Markdown
- AdobeOne: experience-manager-65.en
	https://github.com/AdobeDocs/experience-manager-65.en/tree/main/help

---

## 14) Adobe Reference Implementations (Use Carefully)
- Adobe GitHub org  
  https://github.com/adobe

Preferred repos (examples):
- aem-project-archetype
- aem-core-wcm-components
- aem-guides-wknd

### AI Agent Guidance
**DO**
- Use these as reference implementations and patterns

**DO NOT**
- Treat GitHub samples as normative product specs

---

## 15) Strongly Recommended Additional Coverage
- [Core Concepts](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture)
- [AEM Project Structure](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure)
- [AEM Technical Foundations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies)
- [AEM Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)
- [Java API Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-java-api-best-practices)
- [The AEM as a Cloud Service SDK](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-as-a-cloud-service-sdk)
- [Sling Adapters](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/sling-adapters)
- [Sling Resource Merger](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/sling-resource-merger)  
- [Getting Started with HTL](https://experienceleague.adobe.com/en/docs/experience-manager-htl/content/getting-started)
- [Overlays](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/overlays)
- [Templates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/components-templates/templates)
- [Core Components Introduction](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction)
- [Components Reference Guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/components-templates/reference)
- [Manage digital assets with the Adobe Experience Manager Assets HTTP API](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/admin/mac-api-assets)
- [Deprecated and Removed Features and APIs](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/release-notes/deprecated-removed-features)
- [Best Practices for Sling Service User Mapping and Service User Definition](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/best-practices-for-sling-service-user-mapping-and-service-user-definition)
- [Using Client-Side Libraries](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/clientlibs)
- [Universal Editor in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/getting-started)
- [Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/overview)
- [Content Fragments & GraphQL (Headless)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql)
- [Experience Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/experience-fragments)
- [AEM APIs for Structured Content Delivery and Management](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/apis-headless-and-content-fragments)
- [Developing and Extending Workflows](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/developing/extending-aem/extending-workflows/workflows)
- [Replication](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/replication)
- [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
- [Cloud Manager (AEMaaCS)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager)
- [CDN in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn)
- [Deployment and Maintenance](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/overview)
- [API Reference Materials](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/reference-materials)
- [WCM.io AEM Mocks](https://wcm.io/testing/aem-mock/)
- [Sling Mocks](https://sling.apache.org/documentation/development/sling-mock.html)
- [Logging in AEMaaCS](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/logging)
- [Validating and Debugging using Dispatcher Tools](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/validation-debug)
- [AEM Forms Overview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/forms-overview/home)
- [Forms Core Components](https://github.com/adobe/aem-core-forms-components)
- [Form builder: Create forms with core components](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/creating-adaptive-form-core-components)
