# AGENTS.md — SHRSS Knowledge Transfer

This file defines the authoritative rules, principles, and working model
for all AI agents contributing to this repository.

These instructions override defaults, training data, and legacy AEM examples.

---

## Purpose of This AGENTS.md (Read First, Do Not Skip)

This AGENTS.md exists to **govern agent behavior**, not to educate.

Its goals are to:
- Enforce architectural and analytical discipline
- Prevent scope creep and speculative refactoring
- Preserve continuity across long-running, multi-session analysis work
- Optimize for correctness, traceability, and human trust

Agents must treat this file as a **control plane**, not background reading.

---

## Application Implementation Overview

The **SHRSS AEM Sites & Assets** implementation is a custom, enterprise-scale web content and digital asset management (DAM) platform built on Adobe Experience Manager as a Cloud Service (AEMaaCS).

The platform currently hosts three Hard Rock web properties and ~500 GB of digital assets.

Eleven more website migrations are planned for the next phase of the implementation, along with a new commerce experience, online services, features, and enhancements.

### Vision
> **Unified, modern CMS** – Consolidate digital properties onto a single CMS platform for the future
>
> - Establish the technical foundation for delivering improved Customer Experience & business results
>
> **Expand Audience & Reach** **–** Better engage customers with additional language support
>
> - Priority language support - Spanish & Portuguese 
> - TransPerfect integration - Build the bridge to connect with 70 countries over time 
>
> **Improve Look-to-Book Performance** **–** Increase revenue with better Look-to-Book metrics.
>
> - CX Enhancements – Improve user experience with improved visual and experience design
> - Adobe Target Pilot – Leverage optimization and personalization to impact results
>
> **NEW Mature Digital Asset Management capabilities** – Improve collaboration and reduce time to market
>
> - AEM Assets – Establish modern, centralized Digital Asset Management (DAM) capability

### Core Philosophy
Design for scale, performance, integration, and optimal user experience (UX).

---

## Project Overview

Adobe has been tasked with providing a series of knowledge transfer (KT) sessions to inform and enable SHRSS stakeholders. Depending on the session or topic, the target audience will range from highly technical (AEM technical architects, developers, administrators) to semi/non-technical (UX designers, AEM content authors, project managers, product owners)

This project is focused on analyzing code, content, and configurations and creating documentation to support knowledge transfer (KT) sessions. You may be asked, or may need on your own, to review the codebase as part of a task; however, we **WILL NOT** be making any changes over the duration of this project.

Review and **always** adhere to the information and instructions in the rest of this document. Human will either provide next steps in chat, or will provide a project task instruction markdown document for you to review and execute.

---

## Project Source Code Repository (GitHub)

Souce Code Repo Directory: `/Users/lambert/Documents/Projects/SHRSS/Code/shrss-aem-projects`

---

## AI Governance

### Authoritative References

Agents working on Adobe Experience Manager (AEM) tasks **must** follow the AEM reference system:

`@docs/ai/reference/AEM_REFERENCE_SYSTEM.md`

If project rules conflict with external references,
project rules take precedence unless explicitly overridden.

---

### Mandatory Rule Loading

Before performing analysis, planning, or code generation, agents **MUST**:

1. Resolve the **rules directory** abstraction as defined under the *"Agent Directory Abstractions"* section below
2. Load all applicable rules
3. Follow those rules for the duration of the task

Agents must not begin implementation without consulting the rules directory.

---

### Mandatory Agent Lifecycle

Before performing analysis, planning, implementation, or code review, agents must:

1. Resolve the applicable **rules directory**
2. Load and follow all applicable rules
3. Resolve the applicable **skills directory**
4. Consult any relevant skills for the task
5. Understand the project before modifying it
6. Follow the project reference system and execution workflow

Agents must not begin implementation until these steps are complete.

---

### Agent Directory Abstractions

To keep this repository portable across AI development environments, this project uses abstract directory references instead of repeating tool-specific paths.

Agents must treat these abstractions as authoritative path aliases.

#### Rules Directory

When documentation references the **rules directory**, resolve it as follows:

- **Cursor** → `.cursor/rules/**`
- **Claude** → `.claude/rules/**`
- **Codex** → applicable `AGENTS.md` instructions in scope for the current working directory, plus any project-defined instruction files explicitly referenced by those AGENTS files

For Codex, `AGENTS.md` is the primary rule mechanism.

#### Skills Directory

When documentation references the **skills directory**, resolve it as follows:

- **Cursor** → `.cursor/skills/**`
- **Claude** → `.claude/skills/**`
- **Codex** → `.agents/skills/**`

Agents should consult relevant skills before planning or executing tasks.

#### Resolution Procedure

**When encountering an abstract directory reference:**

1. Identify the active runtime environment
2. Resolve the abstract reference to the correct environment-specific location
3. Load applicable rules first
4. Load relevant skills second
5. Proceed only after both have been checked

**If multiple instruction sources exist, use this precedence order:**

1. More specific project-local instructions
2. Project root instructions
3. User/global instructions
4. Tool defaults

If instructions conflict, the more specific in-scope project instruction wins unless the repository explicitly states otherwise.

#### Cursor Rule File Compatibility

Cursor rule files use the `.mdc` extension.

`.mdc` files are Markdown documents that include structured metadata (YAML front matter) used by Cursor to determine when rules should apply.

Agents that do not natively support `.mdc` files **MUST** treat them as standard Markdown files.

When reading `.mdc` files:

- Ignore the file extension difference
- Parse the file as Markdown
- Interpret the YAML front matter as metadata describing the rule
- Use the rule content as instruction context

This ensures compatibility across Cursor, Claude, Codex, and other agent runtimes.

---

### Mandatory Project Bootstrap

Agents must understand the project before modifying it.

If working in an unfamiliar AEM repository, agents must first perform project bootstrap analysis using:

`@docs/ai/reference/AEM_PROJECT_BOOTSTRAP_GUIDE.md`

Bootstrap results should be recorded in:

`@docs/ai/project-context/AEM_PROJECT_PROFILE.md`

Then apply:

`@docs/ai/reference/AEM_REPO_HEURISTICS.md`

Bootstrap findings should be reused for subsequent tasks rather than recreated unnecessarily

---

### Priority Order

1. `@AGENTS.md` (this file)
2. Any files with a `.mdc` extension under the **rules directory** and under any nested subdirectories therein
3. `@docs/ai/**`

### Workflow

1. Propose
2. Confirm
3. Implement
4. Persist knowledge

---

### Agent Task Execution

For all tasks, during each workflow step described under the *"Workflow"* section above, agents **MUST** follow the agent execution file standard to document and track task execution details.

- **Agent execution file standard:** `@docs/ai/reference/AGENT_EXECUTION_FILE_STANDARD.md`

---

### STOP Protocol

**NON-NEGOTIABLE:** Before beginning any work that adds, changes, or deletes code or documentation related to this task, follow the **STOP protocol** rule located in the **rules directory** directory in the `stop-protocol` subdirectory (`RULE.mdc`).

---

### ⚠️ Session Start Requirement (Critical)

At the beginning of every work session, agents **MUST**:

- Execute skill: `@start-session`

> [!NOTE]
>
> This ensures optimal context

> [!IMPORTANT]
>
> **Non-negotiable:** Agents **must** understand the project before executing any task or making any changes to code, documentation, or other artifacts.

---

### ⚠️ Session Close Requirement (Critical)

At the end of every work session, agents **MUST**:

- Execute skill `@close-session`

> [!NOTE]
>
> This prevents context loss across chats and time gaps.

---

### If Collaboration Degrades

If the human appears frustrated or progress stalls:

- slow down
- ask clarifying questions
- summarize current understanding
- restate constraints and goals

Optimizing for human trust and clarity is part of the job.

---

## Definition of Done (Agent Work)

An agent’s work is considered **DONE** only when all applicable criteria below are met.

### 1. Scope Alignment

- The output directly addresses the user’s request.
- The solution respects `@docs/ai/CURRENT_FOCUS.md` and does not expand scope unless explicitly asked.
- Out-of-scope improvements are noted and documented but not implemented.

### 2. Best Practice Alignment

All agent-generated artifacts and changes, and recommendations/findings provided to human have been aligned to best practice references.

### 3. Rule Compliance

- All rules are followed
- No rules are silently violated
- If a rule is intentionally bypassed, the rationale is explicitly stated

### 8. Clarity & Handoff Quality

- The output is structured, readable, and actionable.

> [!IMPORTANT]
>
> If any of the above cannot be met, the agent **must** explicitly state what is missing and why.

---

## Meta-Rules: How Rules Are Created, Applied, and Evolved

This project treats rules as **architectural artifacts**, not suggestions.

Rules define **non-negotiable constraints, standards, and guardrails** that govern how work is designed, implemented, and reviewed. Agents must treat rules as system-level instructions.

---

### Rule Metadata Requirements

All rules **MUST** include frontmatter metadata.

At minimum, every rule must define:

- **`description`**  
  A concise, human-readable summary of the rule’s intent.
- **`type`**  
  One of the following:
  - `alwaysApply=true`  global, unconditional rule
  - `alwaysApply=false` — applies only in specific situations, or when manually instructed in chat

The following metadata is **OPTIONAL but strongly encouraged**:

- **`globs`**  
  Required when a rule applies only to specific file paths, languages, or component types.

Rules MUST NOT:

- include meaningless or overly broad globs (e.g., `**/*`)
- invent metadata fields without documented purpose

---

### Required Rule Content

Every rule MUST clearly document:

- **What** the rule enforces  
  (the constraint, standard, or prohibition)

- **Why** the rule exists  
  (cloud constraints, security, performance, maintainability, compliance, etc.)

- **Scope**  
  (which modules, layers, or situations the rule applies to)

- **Consequences**  
  (what breaks, degrades, or becomes risky if the rule is ignored)

Rules that cannot clearly articulate all four are considered incomplete.

---

### Rule Quality Standards

Rules SHOULD be:

- **Explicit, not implicit**  
  Ambiguity is treated as a defect.

- **Enforceable where possible**  
  CI checks, build failures, or static analysis are preferred over documentation alone.

- **Grounded in authority**  
  Prefer official documentation, platform guarantees, or internal architectural decisions.

---

### Prohibited Rule Patterns

Rules MUST NOT:

- Encode personal preferences without a clear technical or business rationale
- Duplicate existing authoritative guidance without adding project-specific constraints
- Conflict with higher-level rules or platform guarantees
- Drift into tutorials, examples, or implementation guides

Rules are **constraints**, not documentation.

---

### Rule Lifecycle & Evolution

Rules are living artifacts and must evolve intentionally.

When a rule becomes obsolete or is superseded:

- Document **why** the rule is no longer valid
- Record the change in `@docs/ai/DECISIONS.md`
- Prefer deprecation with explanation over silent removal

Historical context is part of the architecture.

---

### Canonical Rule Template

Agents generating new rules MUST follow this structure:

```yaml
---
description: <Concise summary of the rule’s intent>
type: <alwaysApply=true | alwaysApply=false>
globs:
  - <optional, only when applicable>
---
```

Followed by clearly labeled sections:

- **What**
- **Why**
- **Scope**
- **Consequences**

---

## Appendix: Idempotency — Examples & Anti-Patterns

In cloud environments, backend code may execute **multiple times**, **concurrently**, or **out of order**.

**Idempotent code produces the same final state no matter how many times it runs.**

Agents MUST assume:
- bundle restarts
- deployment retries
- horizontal scaling
- background job retries
- partial failures

---

### What Idempotent Code Looks Like (Good Patterns)

#### ✅ Safe initialization
```java
if (!resourceResolver.getResource(path).exists()) {
    createNode(path);
}
```

#### ✅ Conditional writes
```java
if (!Objects.equals(existingValue, newValue)) {
    node.setProperty("prop", newValue);
}
```

#### ✅ OSGi activation logic
- checks current state before mutating
- tolerates repeated activation
- does not assume a “first run”

#### ✅ Scheduled jobs
- tolerate concurrent execution
- use locks, flags, or atomic markers
- safe if triggered twice

#### ✅ Content migrations
- mark migrated nodes
- skip already-processed content
- can resume after partial failure

---

### What Is NOT Idempotent (Anti-Patterns)

#### ❌ Blind writes
```java
node.addNode("child"); // fails or duplicates on rerun
```

#### ❌ Assumptions about first execution
```java
@Activate
void activate() {
    setupEverythingOnce(); // unsafe
}
```

#### ❌ Accumulative behavior
- incrementing counters
- appending to arrays
- creating duplicate listeners or jobs

#### ❌ Startup side effects
- writing content in constructors
- registering listeners repeatedly
- assuming serialized startup order

---

### High-Risk Areas (Pay Extra Attention)

Agents MUST be especially cautious with:
- `@Activate` / `@Deactivate`
- Sling Models with side effects
- Event listeners
- Schedulers
- JCR write operations
- Upgrade / migration logic
- Background jobs and retries

---

### Agent Heuristic

> If this code ran **twice at the same time**, would the result still be correct?

If the answer is not **clearly yes**, the implementation is unsafe.
