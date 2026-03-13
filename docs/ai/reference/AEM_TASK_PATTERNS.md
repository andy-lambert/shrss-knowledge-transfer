# AEM Task Patterns for AI Agents

Purpose: Provide canonical implementation patterns for common Adobe
Experience Manager (AEM) development and architecture tasks.

These patterns act as solution blueprints that agents can follow when
executing tasks. They complement the reasoning workflow defined in:

-   AEM_AGENT_EXECUTION_TEMPLATE.md
-   AEM_AGENT_REASONING_PROTOCOL.md
-   AEM_ARCHITECTURE_KNOWLEDGE_PACK.md

Agents should use these patterns to accelerate solution generation while
remaining aligned with official AEM practices.

------------------------------------------------------------------------

# How to Use Task Patterns

When executing an AEM task:

1.  Classify the task using AEM_TOPIC_ONTOLOGY.md
2.  Locate the closest task pattern in this document
3.  Follow the pattern as a structural blueprint
4.  Validate the implementation using AEM_AGENT_REASONING_PROTOCOL.md
5.  Adjust the pattern to fit project-specific requirements

Task patterns provide starting structures, not rigid templates.

------------------------------------------------------------------------

# Pattern: Create AEM Component

## Classification

Primary Topic: Component Development

Secondary Topics: Sling Models, HTL, Client Libraries

## Pattern

1.  Create component directory:

/apps/`<project>`{=html}/components/`<component-name>`{=html}

2.  Define component properties:

\_component.xml

3.  Create dialog definition:

/cq:dialog/.content.xml

4.  Create HTL template:

component.html

5.  Add Sling Model if business logic is required.

## Best Practices

-   Prefer Sling Models over logic in HTL
-   Extend Core Components when possible
-   Avoid custom code for functionality already available in Core
    Components

------------------------------------------------------------------------

# Pattern: Implement Sling Model

## Classification

Primary Topic: Component Development

Secondary Topics: Backend Services

## Pattern

1.  Create Java class:

com.`<org>`{=html}.`<project>`{=html}.core.models

2.  Annotate model:

@Model( adaptables = Resource.class, defaultInjectionStrategy =
DefaultInjectionStrategy.OPTIONAL )

3.  Inject properties using Sling annotations.

4.  Add getters for template usage.

## Best Practices

-   Avoid heavy business logic inside models
-   Delegate complex logic to services
-   Keep models focused on data access and transformation

------------------------------------------------------------------------

# Pattern: Create OSGi Service

## Classification

Primary Topic: Backend Services

Secondary Topics: OSGi

## Pattern

1.  Create service interface:

com.`<org>`{=html}.`<project>`{=html}.core.services

2.  Create implementation using OSGi annotations.

3.  Inject service into Sling Models or servlets.

## Best Practices

-   Use services for reusable business logic
-   Avoid embedding complex logic in components

------------------------------------------------------------------------

# Pattern: Configure Dispatcher Caching

## Classification

Primary Topic: Dispatcher and Caching

Secondary Topics: Security, Performance

## Pattern

1.  Configure cache rules in dispatcher.any

2.  Define allowed paths.

3.  Configure invalidation rules.

4.  Ensure proper cache headers from AEM.

## Best Practices

-   Cache all publicly accessible content
-   Avoid caching personalized content
-   Ensure proper cache invalidation mechanisms

------------------------------------------------------------------------

# Pattern: Implement Content Fragment Model

## Classification

Primary Topic: Content Architecture

Secondary Topics: Headless Delivery

## Pattern

1.  Define Content Fragment Model in AEM.

2.  Configure fields and validation rules.

3.  Use fragments within pages or headless APIs.

4.  Access fragments via Sling Model or GraphQL API.

## Best Practices

-   Use fragments for structured content
-   Avoid embedding business logic in fragments
-   Design models for reuse across channels

------------------------------------------------------------------------

# Pattern: Configure Cloud Manager Pipeline

## Classification

Primary Topic: Cloud Manager and Deployment

Secondary Topics: CI/CD

## Pattern

1.  Configure pipeline in Cloud Manager.

2.  Ensure repository includes:

pom.xml ui.apps ui.content core

3.  Define build and quality gates.

4.  Deploy to dev → stage → prod environments.

## Best Practices

-   Maintain high code quality scores
-   Use automated testing
-   Avoid manual environment changes

------------------------------------------------------------------------

# Pattern: Debug AEM Issue

## Classification

Primary Topic: Operations

Secondary Topics: Logs, Configuration

## Pattern

1.  Identify failing component or request.

2.  Review logs such as error.log and request.log.

3.  Identify stack traces or configuration errors.

4.  Cross-reference documentation.

5.  Implement fix and validate.

## Best Practices

-   Reproduce issues in lower environments
-   Avoid debugging directly in production
-   Document root cause

------------------------------------------------------------------------

# Design Goal

Task patterns help agents:

-   start with known implementation structures
-   reduce exploration time
-   maintain architectural consistency
-   align generated solutions with AEM best practices

Agents should treat this document as a library of common AEM solution
blueprints.
