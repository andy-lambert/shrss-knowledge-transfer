# AEM Agent Reasoning Protocol

Purpose: Ensure AI agents working on Adobe Experience Manager (AEM)
tasks produce solutions aligned with official Adobe architecture
guidance and best practices.

This protocol defines the required reasoning workflow agents should
follow when planning, implementing, or documenting AEM solutions.

------------------------------------------------------------------------

# Core Principle

Agents must ground architectural and implementation decisions in
**official Adobe documentation** before generating solutions.

Primary documentation sources:

-   AdobeDocs GitHub repositories
-   Experience League documentation
-   Project-specific governance documents
-   Internal architecture standards

Agents should treat these sources as **authoritative knowledge**.

------------------------------------------------------------------------

# Standard Agent Reasoning Loop

Agents should follow this sequence when performing technical work.

1.  Identify the task or problem.
2.  Extract key technical topics.
3.  Search AdobeDocs repositories for relevant documentation.
4.  Review documentation to identify best practices.
5.  Plan the implementation based on official guidance.
6.  Generate code, configuration, or documentation.
7.  Validate the output against documented patterns.

Example:

Problem: Implement Sling Model.

Agent reasoning flow:

-   Identify topic: Sling Models
-   Search AdobeDocs repo
-   Review documentation patterns
-   Apply annotations and injection patterns
-   Generate implementation

------------------------------------------------------------------------

# Documentation-First Development

Agents should follow this rule:

**Search documentation before generating implementation code.**

Required workflow:

    1. Identify technical topic
    2. Locate documentation
    3. Extract best practices
    4. Generate solution

This reduces hallucinations and aligns output with Adobe-supported
approaches.

------------------------------------------------------------------------

# Example Application

## Dispatcher Configuration

Agent workflow:

1.  Identify dispatcher-related task.
2.  Search dispatcher documentation repository.
3.  Locate cache and filter configuration guidance.
4.  Generate dispatcher configuration aligned with documentation.

Agents should avoid producing dispatcher rules not supported by official
documentation.

------------------------------------------------------------------------

## Sling Model Development

Agent workflow:

1.  Identify Sling Models usage.
2.  Locate official Sling Model documentation.
3.  Follow recommended annotations and injection patterns.

Preferred approach:

-   Use Sling Models
-   Avoid JSP or legacy code patterns

------------------------------------------------------------------------

## Cloud Manager CI/CD

Agent workflow:

1.  Identify deployment requirements.
2.  Locate Cloud Manager pipeline documentation.
3.  Follow CI/CD structure recommended by Adobe.

Agents should align build processes with Cloud Manager standards.

------------------------------------------------------------------------

# Validation Step

Before completing a task, agents should verify:

-   Architecture aligns with AEM best practices.
-   Generated code follows recommended patterns.
-   Configuration matches official documentation examples.

If a conflict exists:

1.  Project-specific governance rules take precedence.
2.  Otherwise follow official Adobe documentation.

------------------------------------------------------------------------

# Usage in Agent Systems

This protocol should be referenced by:

-   AGENTS.md
-   orchestration agents
-   implementation specialists
-   documentation generators

It ensures consistent reasoning across all agent workflows.
