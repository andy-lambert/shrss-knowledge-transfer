# AEM AI Reference System

Purpose: Provide a single entry point that explains how AI agents should
use the Adobe Experience Manager (AEM) reference artifacts included in
this repository.

This document orchestrates the reference files located in
`docs/ai/reference/` and defines the order in which agents should
consult them during planning, research, implementation, and
documentation tasks.

The reference system combines:

-   Topic classification
-   Documentation discovery
-   Architectural grounding
-   Structured reasoning

Agents should treat these documents as a **coordinated framework**, not
as isolated references.

------------------------------------------------------------------------

## Reference Artifacts

The AEM reference system consists of the following files:

-   `AEM_TOPIC_ONTOLOGY.md`
-   `AEM_CANONICAL_REFERENCES.md` – authoritative documentation index
-   `experience-league-agent-research-playbook.md`
-   `ADOBEDOCS_SEARCH_INDEX.md`
-   `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`
-   `AEM_AGENT_REASONING_PROTOCOL.md`
-   `ADOBEDOCS_AGENT_TOOLS_SPEC.md`
-   `AEM_AGENT_ROLE_GUIDES.md`

These documents together provide classification, research strategy,
knowledge grounding, and execution discipline.

------------------------------------------------------------------------

## System Design

The system operates in layers.

| Layer| Artifact | Purpose |
| ---- | ---- | ---- |
| Task Classification | `AEM_TOPIC_ONTOLOGY.md` | Identify the technical domain of the task |
| Documentation Entry | `AEM_CANONICAL_REFERENCES.md` | Identify authoritative Adobe sources |
| Research Strategy | `experience-league-agent-research-playbook.md` | Explain how to search Adobe documentation |
| Repo Routing | `ADOBEDOCS_SEARCH_INDEX.md` | Quickly map topics to documentation repos |
| Architecture Guidance | `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md` | Reinforce official architecture |
| Execution Discipline | `AEM_AGENT_REASONING_PROTOCOL.md` | Enforce structured reasoning |
| Tool Integration | `ADOBEDOCS_AGENT_TOOLS_SPEC.md` | Define optional automation tools |

> [!IMPORTANT]
>
> Agents should move through these layers sequentially when solving
> AEM-related tasks.

------------------------------------------------------------------------

## When Agents Should Use This System

Agents **must** use this reference system whenever tasks involve:

-   Adobe Experience Manager (AEM)
-   AEM as a Cloud Service
-   Sling models, servlets, services, listeners, schedulers
-   OSGi configuration
-   Dispatcher configuration
-   Cloud Manager pipelines
-   AEM component development
-   AEM authoring architecture
-   AEM Assets / DAM
-   Content fragments and headless delivery
-   Deployment or operational topics

------------------------------------------------------------------------

## Bootstrap Phase — Repository Understanding

When an agent begins work in an unfamiliar repository, it MUST first perform a project bootstrap analysis using:

`@docs/ai/reference/AEM_PROJECT_BOOTSTRAP_GUIDE.md`

The bootstrap process determines:

- AEM platform type (AEMaaCS vs AEM 6.5)
- project archetype structure
- dispatcher configuration
- content architecture
- deployment model
- major integrations

Agents should produce and provide a short **Project Bootstrap Summary** before proceeding with implementation tasks.

Bootstrap analysis should only be performed when:

- the repository has not previously been analyzed
- the agent does not understand the project structure
- a new agent session begins in the repository

---

## Recommended Workflow

Agents should follow this workflow when performing AEM-related work.

------------------------------------------------------------------------

### Step 1 — Classify the Task

Begin by identifying the **technical domain** using:

`AEM_TOPIC_ONTOLOGY.md`

Purpose:

-   Classify the task into a primary topic area
-   Identify secondary topics
-   Determine which documentation repositories are most likely to
    contain the relevant guidance

Example:

Task: "Create a Sling Model that reads a Content Fragment."

Classification:

Primary Topic: - Component Development

Secondary Topics: - Sling Models - Content Fragments - Headless Delivery

Likely repositories:

-   `experience-manager-cloud-service.en`
-   `experience-manager-learn.en`

This step determines where the agent should perform research.

------------------------------------------------------------------------

### Step 2 — Consult Canonical References

Next review:

`AEM_CANONICAL_REFERENCES.md`

Purpose:

-   Identify authoritative Adobe documentation sources
-   Confirm preferred documentation repositories
-   Establish the research starting point

Agents should prefer official Adobe sources over blogs or community
posts.

------------------------------------------------------------------------

### Step 3 — Follow the Research Playbook

Consult:

`experience-league-agent-research-playbook.md`

Purpose:

-   Learn how to search AdobeDocs repositories
-   Understand Experience League repo structure
-   Navigate documentation directories efficiently

This document defines the **research behavior agents should follow**.

------------------------------------------------------------------------

### Step 4 — Route to the Correct Repository

Use:

`ADOBEDOCS_SEARCH_INDEX.md`

Purpose:

-   Map the topic identified in Step 1 to the correct documentation
    repository
-   Identify common directory patterns
-   Reduce exploration time

Example:

Dispatcher caching → `experience-manager-dispatcher.en`

------------------------------------------------------------------------

### Step 5 — Apply Architecture Knowledge

Consult:

`AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`

Purpose:

-   Reinforce canonical architectural concepts
-   Ensure generated designs align with official Adobe patterns
-   Avoid outdated or unsupported approaches

This step grounds implementation decisions in platform architecture.

------------------------------------------------------------------------

### Step 6 — Execute the Reasoning Protocol

Follow:

`AEM_AGENT_REASONING_PROTOCOL.md`

Required reasoning loop:

1.  Identify the task
2.  Extract the technical topic
3.  Search official Adobe documentation
4.  Review best practices
5.  Plan implementation
6.  Generate code or configuration
7.  Validate against official guidance

Agents must follow this process before generating implementation
guidance.

------------------------------------------------------------------------

### Step 7 — Use Documentation Tools (Optional)

If the environment supports automated documentation tooling, consult:

`ADOBEDOCS_AGENT_TOOLS_SPEC.md`

Purpose:

-   Define standardized tools for documentation retrieval
-   Enable automated querying of AdobeDocs repositories

---

### Step 8 — Apply Role Guidance

If multiple agents are collaborating, consult:

AEM_AGENT_ROLE_GUIDES.md

------------------------------------------------------------------------

## Example Agent Workflow

Example task:

Implement a Sling Model for a component.

Workflow:

1.  Classify topic using `AEM_TOPIC_ONTOLOGY.md`
2.  Review canonical documentation sources
3.  Follow the research playbook
4.  Use the search index to locate documentation
5.  Review architectural patterns
6.  Follow the reasoning protocol
7.  Generate the implementation

------------------------------------------------------------------------

## Reference Hierarchy

When multiple sources provide guidance, follow this precedence order:

1.  Project repository rules and governance documents
2.  Files in `docs/ai/reference/`
3.  Official Adobe Experience League documentation
4.  AdobeDocs GitHub repositories
5.  External sources (blogs, forums, etc.)

Project-specific rules always take precedence unless explicitly
overridden.

------------------------------------------------------------------------

## Design Goal

This reference system ensures that AI agents:

-   classify tasks correctly
-   route research efficiently
-   prioritize official Adobe documentation
-   follow supported architectural patterns
-   avoid outdated AEM practices
-   produce consistent implementation guidance
-   reduce hallucination risk during development tasks

Agents should treat this reference system as the **authoritative
framework for AEM-related work**.
