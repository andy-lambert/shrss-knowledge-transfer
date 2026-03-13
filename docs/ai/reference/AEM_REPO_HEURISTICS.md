# AEM Repository Heuristics for AI Agents

Purpose: Provide a set of heuristics that AI agents can use to quickly
assess the quality, risks, and architectural characteristics of an Adobe
Experience Manager (AEM) codebase.

These heuristics help agents detect:

-   architectural anti-patterns
-   outdated AEM practices
-   performance risks
-   dispatcher misconfigurations
-   Cloud compatibility issues

This document complements:

-   AEM_PROJECT_BOOTSTRAP_GUIDE.md
-   AEM_TOPIC_ONTOLOGY.md
-   AEM_AGENT_REASONING_PROTOCOL.md
-   AEM_TASK_PATTERNS.md

Agents should apply these heuristics **after performing project
bootstrap analysis**.

------------------------------------------------------------------------

# Heuristic Categories

Agents should evaluate repositories across the following domains:

1.  Project Structure
2.  Component Architecture
3.  Sling Model Usage
4.  OSGi & Service Design
5.  Dispatcher Configuration
6.  Query & Indexing Behavior
7.  Content Architecture
8.  Frontend Integration
9.  Cloud Compatibility
10. Operational Readiness

------------------------------------------------------------------------

# 1. Project Structure Heuristics

## Healthy Indicators

-   Maven multi-module structure
-   Standard archetype modules present:

core\
ui.apps\
ui.content\
dispatcher\
ui.frontend (optional)

-   Clear separation between Java logic and content packages

## Risk Indicators

-   Large monolithic modules
-   Business logic inside ui.apps
-   Missing core module

------------------------------------------------------------------------

# 2. Component Architecture

## Healthy Indicators

-   Components extend Core Components
-   Business logic implemented through Sling Models
-   HTL used strictly as view layer

## Anti‑Patterns

-   Business logic embedded in HTL
-   Large component hierarchies with duplicated logic
-   Custom components replicating Core Component functionality

------------------------------------------------------------------------

# 3. Sling Model Usage

## Healthy Indicators

-   Small cohesive models
-   Constructor or annotation injection
-   Models primarily handle data transformation

## Anti‑Patterns

-   "God models" traversing large repository sections
-   Business services implemented inside models
-   Heavy repository querying inside models

------------------------------------------------------------------------

# 4. OSGi & Service Design

## Healthy Indicators

-   Stateless services
-   Configuration externalized via OSGi configs
-   Services injected via dependency injection

## Anti‑Patterns

-   Persistent state inside services
-   Environment‑specific logic embedded in code
-   Manual service lookup patterns

------------------------------------------------------------------------

# 5. Dispatcher Configuration

## Healthy Indicators

-   Default‑deny filter rules
-   Explicit allow rules for public endpoints
-   Dispatcher configuration managed via Git

## Risk Indicators

-   Wildcard allow filters
-   Missing cache invalidation rules
-   Large cache bypass areas

------------------------------------------------------------------------

# 6. Query & Indexing

## Healthy Indicators

-   Custom Oak indexes for large queries
-   Keyset pagination used for large result sets
-   Queries validated using explain plans

## Performance Risks

-   Traversal queries
-   Large unbounded query results
-   Frequent repository scans

------------------------------------------------------------------------

# 7. Content Architecture

## Healthy Indicators

-   Structured content models
-   Content Fragments used for reusable structured data
-   Experience Fragments used for reusable layout fragments

## Risk Indicators

-   Business logic encoded in content structure
-   Deep page hierarchies with duplicated content

------------------------------------------------------------------------

# 8. Frontend Integration

## Healthy Indicators

-   Dedicated ui.frontend module
-   Client libraries properly categorized
-   Modern JS build pipeline (webpack, etc.)

## Anti‑Patterns

-   Inline JS inside HTL templates
-   Clientlibs containing unrelated bundles

------------------------------------------------------------------------

# 9. Cloud Compatibility

## Healthy Indicators

-   Immutable configuration deployment
-   RepoInit used for users and ACLs
-   Dispatcher configs deployed via Cloud Manager

## Anti‑Patterns

-   Runtime configuration changes
-   Local filesystem assumptions
-   Long synchronous workflow steps

------------------------------------------------------------------------

# 10. Operational Readiness

## Healthy Indicators

-   Logging strategy defined
-   Health checks implemented
-   Integration tests present

## Risk Indicators

-   No automated tests
-   Logging disabled or minimal
-   Production debugging patterns in code

------------------------------------------------------------------------

# Heuristic Evaluation Output

After applying heuristics, agents should produce a short evaluation
summary.

Example:

Platform: AEMaaCS\
Architecture: Sites + Headless Hybrid

Findings:

-   Components extend Core Components ✔
-   Dispatcher filters follow default‑deny ✔
-   Several large Sling Models detected ⚠
-   No custom Oak indexes for high‑traffic queries ⚠

Risk Assessment:

Moderate performance risk due to query patterns.

------------------------------------------------------------------------

# Design Goal

These heuristics allow AI agents to:

-   identify architectural weaknesses quickly
-   highlight modernization opportunities
-   improve implementation guidance
-   reduce long‑term technical debt

Agents should use these heuristics as part of repository analysis and
code review workflows.
