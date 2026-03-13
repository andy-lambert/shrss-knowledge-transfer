# AEM Topic Ontology for AI Agents

Purpose: Provide a controlled vocabulary for Adobe Experience Manager
(AEM) concepts so that AI agents can consistently classify tasks, route
research, and locate the correct documentation repositories.

Agents should use this ontology during **task analysis and planning** to
determine which documentation sources and reference artifacts to
consult.

------------------------------------------------------------------------

# How Agents Should Use This Ontology

When analyzing a task:

1.  Identify the **primary topic category**
2.  Identify **secondary subtopics**
3.  Use those topics to determine:
    -   which AdobeDocs repository to search
    -   which reference artifacts to consult
    -   which implementation patterns apply

Example:

Task: "Create a Sling Model for a component that reads a Content
Fragment"

Classification:

Primary Topic: - Component Development

Secondary Topics: - Sling Models - Content Fragments - Headless /
GraphQL (possible)

Repositories: - experience-manager-cloud-service.en -
experience-manager-learn.en (examples)

------------------------------------------------------------------------

# Primary Topic Categories

## Platform Architecture

Topics:

-   AEM platform architecture
-   Sling request processing
-   JCR repository model
-   OSGi runtime
-   resource resolution
-   content repository structure

Primary documentation repo:

experience-manager-cloud-service.en

------------------------------------------------------------------------

## Component Development

Topics:

-   Sling Models
-   HTL (Sightly)
-   AEM components
-   resource types
-   dialog definitions
-   editable templates
-   client libraries (clientlibs)

Typical documentation areas:

help/implementing/developing/components

------------------------------------------------------------------------

## Backend Services

Topics:

-   OSGi services
-   Sling servlets
-   listeners
-   schedulers
-   workflows
-   event handling

Repositories:

experience-manager-cloud-service.en

------------------------------------------------------------------------

## Dispatcher and Caching

Topics:

-   dispatcher filters
-   cache rules
-   cache invalidation
-   flush agents
-   CDN integration

Primary repo:

experience-manager-dispatcher.en

------------------------------------------------------------------------

## Cloud Manager and Deployment

Topics:

-   CI/CD pipelines
-   code quality gates
-   environment promotion
-   pipeline configuration
-   build and deployment rules

Primary repo:

experience-manager-cloud-service.en

Directory patterns:

help/implementing/cloud-manager

------------------------------------------------------------------------

## Content Architecture

Topics:

-   content fragments
-   experience fragments
-   tagging
-   metadata
-   multi-site manager (MSM)
-   localization
-   content modeling

Primary repos:

experience-manager-cloud-service.en experience-manager-learn.en

------------------------------------------------------------------------

## Headless Delivery

Topics:

-   GraphQL APIs
-   content fragment models
-   headless AEM
-   API delivery patterns

Typical documentation directories:

help/headless

------------------------------------------------------------------------

## Assets / DAM

Topics:

-   asset ingestion
-   metadata management
-   asset processing
-   renditions
-   asset workflows

Primary documentation:

help/assets

------------------------------------------------------------------------

## Security

Topics:

-   permissions
-   access control
-   service users
-   repository security
-   dispatcher security

Primary repos:

experience-manager-cloud-service.en experience-manager-dispatcher.en

------------------------------------------------------------------------

## Performance and Operations

Topics:

-   performance tuning
-   monitoring
-   logging
-   scaling behavior
-   operational best practices

Typical directories:

help/operations

------------------------------------------------------------------------

# Cross-Cutting Topics

Some concepts appear across multiple categories.

Examples:

-   Sling Models → Component Development + Backend Services
-   Content Fragments → Content Architecture + Headless
-   Dispatcher → Security + Performance
-   Cloud Manager → Deployment + Operations

Agents should identify **all relevant categories**, not just one.

------------------------------------------------------------------------

# Mapping Topics to Reference Artifacts

Agents should combine this ontology with the reference system.

Recommended workflow:

1.  Classify task using this ontology

2.  Consult:

    -   AEM_REFERENCE_SYSTEM.md
    -   experience-league-agent-research-playbook.md

3.  Use:

    -   ADOBEDOCS_SEARCH_INDEX.md

4.  Apply:

    -   AEM_ARCHITECTURE_KNOWLEDGE_PACK.md
    -   AEM_AGENT_REASONING_PROTOCOL.md

------------------------------------------------------------------------

# Example Classification

Example task:

"Configure dispatcher cache invalidation for published pages."

Topic classification:

Primary:

-   Dispatcher and Caching

Secondary:

-   Performance and Operations
-   Security

Likely documentation repo:

experience-manager-dispatcher.en

Agent research target:

help/using/ help/security/

------------------------------------------------------------------------

# Design Goal

This ontology helps agents:

-   classify technical tasks correctly
-   select the correct documentation repositories
-   reduce exploration time
-   improve architectural reasoning
-   generate more accurate implementation guidance

Agents should treat this ontology as a **task classification layer** for
AEM-related work.
