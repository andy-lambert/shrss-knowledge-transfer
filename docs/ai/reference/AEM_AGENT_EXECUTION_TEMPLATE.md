# AEM Agent Execution Template

Purpose: Provide a standardized execution structure that AI agents
should follow when performing tasks related to Adobe Experience Manager
(AEM).

This template ensures that all agents:

-   classify the task correctly
-   ground decisions in official Adobe documentation
-   follow architectural best practices
-   validate implementations before completion

Agents should use this template when planning, implementing, debugging,
reviewing, or documenting AEM solutions.

---

## Execution Structure

Agents should structure their reasoning and outputs using the following
sections.

------------------------------------------------------------------------

### 1. TASK

Clearly describe the task being performed.

Examples:

-   Implement a Sling Model for a component
-   Configure dispatcher caching
-   Create an AEM component using Core Components
-   Diagnose a Cloud Manager deployment failure

The task definition should be concise and precise.

------------------------------------------------------------------------

### 2. CONTEXT

Summarize any relevant context:

-   project requirements
-   architecture constraints
-   existing implementation details
-   repository structure
-   platform version (AEMaaCS vs older versions)

Agents should identify assumptions and missing information here.

------------------------------------------------------------------------

### 3. TASK CLASSIFICATION

Use the ontology defined in:

`AEM_TOPIC_ONTOLOGY.md`

Identify:

Primary Topic

Examples:

-   Component Development
-   Dispatcher and Caching
-   Content Architecture
-   Cloud Manager and Deployment

Secondary Topics

Examples:

-   Sling Models
-   Content Fragments
-   GraphQL
-   Security

This classification determines where research should begin.

------------------------------------------------------------------------

### 4. RESEARCH

Follow the guidance in:

-   `experience-league-agent-research-playbook.md`
-   `ADOBEDOCS_SEARCH_INDEX.md`

Agents should:

-   locate relevant AdobeDocs repositories
-   identify official Experience League documentation
-   review architecture guidance
-   identify supported implementation patterns

Research should be documented briefly in this section.

------------------------------------------------------------------------

### 5. ARCHITECTURE ALIGNMENT

Consult:

`AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`

Confirm that the planned solution aligns with:

-   Sling architecture
-   OSGi runtime behavior
-   AEMaaCS constraints
-   Dispatcher architecture
-   Cloud Manager deployment model

Agents should identify architectural patterns being used.

------------------------------------------------------------------------

### 6. IMPLEMENTATION PLAN

Describe the planned solution before writing code.

Examples:

-   Sling Model structure
-   service layer interactions
-   dispatcher rule configuration
-   component architecture

Plans should reference documentation or platform patterns when possible.

------------------------------------------------------------------------

### 7. IMPLEMENTATION

Generate the implementation.

Examples:

-   Java code (Sling Models, services, servlets)
-   HTL templates
-   OSGi configuration
-   dispatcher configuration
-   CI/CD pipeline configuration

Agents should ensure the implementation follows Adobe best practices.

------------------------------------------------------------------------

### 8. VALIDATION

Follow the reasoning protocol defined in:

`AEM_AGENT_REASONING_PROTOCOL.md`

Agents should verify:

-   implementation matches documentation patterns
-   architecture aligns with AEM platform guidance
-   deployment model works for AEM as a Cloud Service
-   security and performance considerations are addressed

If uncertainty remains, agents should document the risk.

------------------------------------------------------------------------

### 9. OUTPUT

Provide the final output.

Examples:

-   code
-   configuration
-   architectural guidance
-   troubleshooting recommendations
-   documentation

Outputs should be clear, structured, and aligned with Adobe terminology.

------------------------------------------------------------------------

## Example Execution Flow

Example: Create Sling Model.

Agent execution:

1.  TASK\
    Implement Sling Model for component

2.  CONTEXT\
    Component reads Content Fragment

3.  TASK CLASSIFICATION\
    Primary: Component Development\
    Secondary: Sling Models, Content Fragments

4.  RESEARCH\
    Locate Sling Model documentation in AdobeDocs

5.  ARCHITECTURE ALIGNMENT\
    Confirm Sling Model injection patterns

6.  IMPLEMENTATION PLAN\
    Define model class and annotations

7.  IMPLEMENTATION\
    Generate Java class

8.  VALIDATION\
    Confirm patterns match documentation

9.  OUTPUT\
    Provide final code implementation

------------------------------------------------------------------------

## Design Goal

This execution template ensures that AI agents:

-   follow a repeatable reasoning structure
-   ground solutions in official documentation
-   produce implementations aligned with AEM best practices
-   reduce hallucinations during development tasks

Agents should treat this template as the **standard execution format for
AEM-related work**.
