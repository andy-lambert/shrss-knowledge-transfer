# AEM Agent Role Guides

Purpose: Define how different AI agent roles should interact with the
AEM Reference System when performing tasks involving Adobe Experience
Manager (AEM).

This guide helps orchestrated or multi-agent workflows coordinate
effectively by assigning clear responsibilities to each agent type.

The roles defined here are logical roles. A single agent may perform
multiple roles, but the reasoning behavior should follow the guidance
for the active role.

------------------------------------------------------------------------

# Relationship to the AEM Reference System

All agents must follow the reference system defined in:

`AEM_REFERENCE_SYSTEM.md`

The reference system provides:

-   task classification
-   documentation discovery
-   architecture grounding
-   structured reasoning

This file defines **how specific agent roles apply that system**.

------------------------------------------------------------------------

# Core Agent Roles

## Architect Agent

Primary responsibility:

Design system architecture and implementation strategies that align with
official AEM platform guidance.

Key reference artifacts:

-   `AEM_TOPIC_ONTOLOGY.md`
-   `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`
-   `experience-league-agent-research-playbook.md`
-   `AEM_AGENT_REASONING_PROTOCOL.md`

Primary activities:

-   classify tasks using the ontology
-   identify architectural domains
-   locate authoritative Adobe documentation
-   design solutions aligned with AEM platform patterns

Typical questions addressed:

-   What is the correct architectural approach?
-   Which AEM capabilities should be used?
-   What constraints apply in AEM as a Cloud Service?

Architect agents should prioritize **platform alignment over
implementation detail**.

------------------------------------------------------------------------

## Developer Agent

Primary responsibility:

Implement code, configurations, and components aligned with official AEM
development practices.

Key reference artifacts:

-   `experience-league-agent-research-playbook.md`
-   `ADOBEDOCS_SEARCH_INDEX.md`
-   `AEM_AGENT_REASONING_PROTOCOL.md`
-   `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`

Primary activities:

-   search documentation for implementation patterns
-   generate Sling Models, servlets, services, and components
-   follow recommended Adobe development practices
-   validate code against official guidance

Typical questions addressed:

-   What annotations should be used for a Sling Model?
-   Where should an OSGi configuration be placed?
-   What is the correct pattern for a component implementation?

Developer agents should avoid generating implementations without
documentation validation.

------------------------------------------------------------------------

## Debugging Agent

Primary responsibility:

Diagnose issues in AEM implementations using logs, configuration
analysis, and platform behavior documentation.

Key reference artifacts:

-   `experience-league-agent-research-playbook.md`
-   `ADOBEDOCS_SEARCH_INDEX.md`
-   `AEM_TOPIC_ONTOLOGY.md`

Primary activities:

-   classify the operational domain of the problem
-   locate relevant documentation
-   identify likely root causes
-   recommend configuration or implementation fixes

Typical questions addressed:

-   Why is a Sling Model not resolving?
-   Why is Dispatcher caching incorrectly?
-   Why did a Cloud Manager deployment fail?

Debugging agents should prioritize **operational documentation and
platform constraints**.

------------------------------------------------------------------------

## Documentation Agent

Primary responsibility:

Produce clear technical documentation aligned with official Adobe
terminology and platform concepts.

Key reference artifacts:

-   `experience-league-agent-research-playbook.md`
-   `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`

Primary activities:

-   extract terminology from official documentation
-   describe architectural patterns
-   document configuration and implementation approaches
-   ensure consistency with Adobe product language

Typical outputs:

-   architecture documentation
-   implementation guides
-   onboarding documentation
-   operational runbooks

Documentation agents should avoid introducing terminology not used in
official Adobe documentation.

------------------------------------------------------------------------

## Code Review Agent

Primary responsibility:

Evaluate implementations for alignment with AEM best practices and
project governance rules.

Key reference artifacts:

-   `AEM_AGENT_REASONING_PROTOCOL.md`
-   `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`
-   `experience-league-agent-research-playbook.md`

Primary activities:

-   verify code follows documented patterns
-   detect architectural anti-patterns
-   confirm compliance with project governance rules
-   identify potential operational or security risks

Typical checks:

-   use of Sling Models vs legacy patterns
-   proper service user configuration
-   dispatcher rules consistency
-   Cloud Manager deployment compatibility

Code review agents should validate both **implementation correctness and
architectural alignment**.

------------------------------------------------------------------------

# Multi-Agent Workflow Example

Example scenario: Implement a component that exposes content fragments
via GraphQL.

Workflow:

1.  Architect Agent
    -   classify the task
    -   determine architecture approach
    -   identify relevant documentation
2.  Developer Agent
    -   implement Sling Model and component logic
    -   follow documented patterns
3.  Debugging Agent
    -   test runtime behavior
    -   identify operational issues
4.  Code Review Agent
    -   validate alignment with architecture and documentation
5.  Documentation Agent
    -   produce implementation and architecture documentation

------------------------------------------------------------------------

# Design Goal

These role guides help ensure that:

-   agents specialize in appropriate responsibilities
-   research and reasoning remain grounded in official documentation
-   implementations follow supported AEM patterns
-   architectural consistency is maintained across projects

Agents should treat this document as the **coordination layer** for
multi-agent AEM development workflows.
