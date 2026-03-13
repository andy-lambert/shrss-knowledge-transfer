# AEM Canonical References

Version: 2.0.0 Applies To: AEM as a Cloud Service (AEMaaCS)

------------------------------------------------------------------------

# Purpose

This document defines the authoritative documentation sources for Adobe
Experience Manager (AEM) work performed by AI agents and developers.

It acts as the canonical index of trusted references within the AEM AI
Reference System and identifies the primary documentation sources agents
should consult when researching AEM behavior, architecture, and
implementation patterns.

This file links only to primary sources:

-   Adobe Experience League
-   AdobeDocs GitHub repositories
-   Apache upstream project documentation
-   Adobe reference implementations

Agents should use this document to determine which sources are
authoritative before performing research.

------------------------------------------------------------------------

# Relationship to the AEM AI Reference System

This document is part of the coordinated framework defined in:

AEM_REFERENCE_SYSTEM.md

Related artifacts include:

-   AEM_TOPIC_ONTOLOGY.md
-   experience-league-agent-research-playbook.md
-   ADOBEDOCS_SEARCH_INDEX.md
-   AEM_ARCHITECTURE_KNOWLEDGE_PACK.md
-   AEM_AGENT_REASONING_PROTOCOL.md
-   AEM_AGENT_EXECUTION_TEMPLATE.md
-   AEM_TASK_PATTERNS.md

Agents should treat this document as the authoritative documentation
source index.

------------------------------------------------------------------------

# Canonical Source Hierarchy

When conflicting guidance exists, prefer sources in the following order:

1.  Project governance and repository rules
2.  AEM AI reference system files
3.  Adobe Experience League
4.  AdobeDocs GitHub repositories
5.  Apache upstream project documentation
6.  Adobe public GitHub repositories
7.  External sources (blogs, forums, etc.)

------------------------------------------------------------------------

# Version Target

This document targets AEM as a Cloud Service (AEMaaCS).

AEM 6.5 documentation may be referenced when the concept remains
identical or when Cloud documentation does not yet exist.

Agents must not assume AEM 6.5 patterns are valid in Cloud environments.

------------------------------------------------------------------------

# Primary AdobeDocs Repositories

  Repository                              Scope
  --------------------------------------- --------------------------------
  experience-manager-cloud-service.en     AEMaaCS platform documentation
  experience-manager-dispatcher.en        Dispatcher documentation
  experience-manager-core-components.en   Core Components
  experience-manager-learn.en             tutorials and examples
  experience-manager-65.en                legacy documentation reference

------------------------------------------------------------------------

# Core Platform Architecture

Architecture Overview
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture

AEM Technical Foundations
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies

Development Guidelines
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines

------------------------------------------------------------------------

# RepoInit

RepoInit Configuration
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-repo-init

RepoInit Syntax
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-repo-init#syntax

Guidance:

DO - Use RepoInit for users, groups, ACLs, and service users

DO NOT - Package users or ACLs via content packages

------------------------------------------------------------------------

# Component Development

Core Components
https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction

Developing Components
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/components-templates/components

HTL Overview
https://experienceleague.adobe.com/en/docs/experience-manager-htl/using/overview

Guidance:

DO - Extend Core Components - Keep logic in Sling Models

DO NOT - Embed business logic in HTL

------------------------------------------------------------------------

# Sling Models

Apache Sling Models
https://sling.apache.org/documentation/bundles/models.html

AEM Sling Models
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/full-stack/sling-models

------------------------------------------------------------------------

# OSGi and Services

Apache Felix https://felix.apache.org/documentation/index.html

OSGi Configuration
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-osgi

Sling Servlets
https://sling.apache.org/documentation/the-sling-engine/servlets.html

------------------------------------------------------------------------

# Dispatcher

Dispatcher Overview
https://experienceleague.adobe.com/en/docs/experience-manager-dispatcher/using/dispatcher

Dispatcher in AEMaaCS
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/dispatcher/overview

Dispatcher Configurations
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/dispatcher/dispatcher-configurations

------------------------------------------------------------------------

# Querying and Indexing

Query Best Practices
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices

Apache Oak Queries https://jackrabbit.apache.org/oak/docs/query/

Indexes in AEMaaCS
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/indexing

------------------------------------------------------------------------

# Assets and DAM

AEM Assets Documentation
https://experienceleague.adobe.com/en/docs/experience-manager-assets

Assets API
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/assets-api-overview

Dynamic Media
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media

------------------------------------------------------------------------

# Headless and Structured Content

Content Fragments
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/overview

GraphQL APIs
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/graphql

------------------------------------------------------------------------

# Adobe Reference Implementations

Adobe GitHub https://github.com/adobe

AEM Project Archetype https://github.com/adobe/aem-project-archetype

Core Components Repo https://github.com/adobe/aem-core-wcm-components

WKND Reference Project https://github.com/adobe/aem-guides-wknd

------------------------------------------------------------------------

# Relationship to Task Patterns

Common implementation patterns are defined in:

AEM_TASK_PATTERNS.md

Agents should:

1.  classify the task
2.  locate canonical references in this document
3.  apply the task pattern
4.  validate using official documentation

------------------------------------------------------------------------

# Design Goal

This document ensures agents prioritize official Adobe documentation,
ground implementation decisions in authoritative sources, and avoid
relying on non-canonical guidance.
