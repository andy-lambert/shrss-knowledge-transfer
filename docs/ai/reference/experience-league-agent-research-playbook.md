# Experience League Agent Research Playbook

Purpose: Teach AI agents how to use Adobe Experience League documentation repositories as a primary research source while thinking, planning, coding, validating, and documenting technical work.

This playbook is intentionally broader than a topic index or reasoning protocol. It tells the agent how to behave during execution when it needs Adobe best practices, implementation guidance, architecture patterns, or operational documentation.

---

## Why This Playbook Exists

Agents working on Adobe Experience Manager and related Adobe Experience Cloud tasks should not rely primarily on generic search engine results, random blog posts, or memory alone.

Agents should prefer:

1. Project-specific governance and repo rules
2. Canonical internal reference documents
3. Official Adobe Experience League documentation
4. AdobeDocs public repositories
5. Other sources only when the above are insufficient

This playbook helps agents reach those sources quickly and consistently.

---

## Scope

Use this playbook when the task involves any of the following:

- AEM architecture
- AEM as a Cloud Service
- AEM Sites
- AEM Assets / DAM
- Sling Models, servlets, services, schedulers, listeners
- OSGi configuration
- Dispatcher and caching
- Cloud Manager and deployment
- Content Fragments / Experience Fragments
- Headless delivery / GraphQL
- Authoring, templates, components, clientlibs
- Security, performance, and operational guidance
- Adobe Experience League learning/tutorial content that may supplement product docs

---

## Primary Repository Families

Agents should understand the difference between repo types.

### 1. Product Documentation Repositories

These are usually the best source for official behavior, supported patterns, constraints, and platform guidance.

Examples:

- `AdobeDocs/experience-manager-cloud-service.en`
- `AdobeDocs/experience-manager-dispatcher.en`
- `AdobeDocs/experience-manager-core-components.en`
- `AdobeDocs/experience-platform.en`
- `AdobeDocs/experience-cloud.en`

Use these first for implementation and architecture decisions.

### 2. Learn / Tutorial Repositories

These are useful for walkthroughs, examples, and learning-oriented guidance.

Example:

- `AdobeDocs/experience-manager-learn.en`

Use these when product docs are too terse, when you need example flows, or when you need task-oriented learning content.

### 3. Experience League Site / Tooling Repositories

These are generally not the first place to look for product guidance.

Examples:

- `adobe-experience-league/exlm`
- related site/tooling repos

Use these only when working on Experience League site behavior, rendering, repo mapping, or publishing mechanics.

---

## Priority Order During Execution

When agents need Adobe guidance, follow this priority order:

1. Project-local rules and governance docs
2. Canonical AEM reference docs in the project
3. Official AdobeDocs repositories
4. Experience League page source mapping
5. External web results only if still necessary

Rule: if project rules conflict with external guidance, project rules win unless explicitly overridden.

---

## Fast Search Strategy Without a URL

When the agent has not been given a specific Experience League URL, it should search by topic.

### Step 1: Identify the technical topic

Extract the smallest accurate topic description.

Examples:

- "Sling Models optional injection"
- "AEM dispatcher cache invalidation"
- "Cloud Manager pipeline quality gates"
- "AEM content fragment models"
- "OSGi config in AEM as a Cloud Service"

### Step 2: Choose the likely repository family

Use this rough routing logic:

- AEM platform, development, operations, architecture → `experience-manager-cloud-service.en`
- Dispatcher, filters, caching, invalidation → `experience-manager-dispatcher.en`
- Core Components usage and component capabilities → `experience-manager-core-components.en`
- Learning/tutorial examples for AEM → `experience-manager-learn.en`
- Experience Platform / cross-solution docs → `experience-platform.en` or `experience-cloud.en`

### Step 3: Search by topic + repo/domain

Example query patterns:

- `site:github.com/AdobeDocs/experience-manager-cloud-service.en sling models`
- `site:github.com/AdobeDocs/experience-manager-dispatcher.en cache invalidation`
- `site:experienceleague.adobe.com AEM Cloud Manager pipeline`
- `site:github.com/AdobeDocs/experience-manager-learn.en content fragments`

### Step 4: Prefer markdown source when possible

If both a rendered Experience League page and a GitHub markdown source are available, prefer the source repo for:

- path awareness
- repeatable lookup
- structured navigation
- repository-based reasoning
- future automation

### Step 5: Read nearby files, not just the first hit

Once a likely file is found, inspect adjacent directories and sibling files. Adobe docs are structured, and the neighboring docs often contain the exact supporting detail the agent needs.

---

## Directory Heuristics

Agents should use directory names as clues.

Common high-value patterns:

- `help/overview/`
- `help/implementing/`
- `help/implementing/developing/`
- `help/implementing/developing/components/`
- `help/implementing/deploying/`
- `help/implementing/cloud-manager/`
- `help/operations/`
- `help/security/`
- `help/sites/`
- `help/assets/`
- `help/headless/`

Interpretation:

- `overview` → architecture, concepts, platform model
- `developing` → implementation patterns, APIs, code guidance
- `deploying` / `cloud-manager` → CI/CD and environment guidance
- `operations` → runtime behavior, monitoring, admin/ops guidance
- `security` → constraints and secure implementation patterns
- `sites` / `assets` → feature-area guidance
- `headless` → APIs, GraphQL, content model delivery patterns

---

## Research Modes by Agent Activity

### While Thinking / Planning

Search for:

- architecture overviews
- supported patterns
- constraints
- product terminology
- implementation boundaries

Goal:

- form a plan grounded in official platform behavior before coding

### While Coding

Search for:

- recommended implementation patterns
- examples
- annotations
- configuration placement
- deployment/runtime constraints

Goal:

- generate code that aligns with supported Adobe approaches

### While Validating

Search for:

- limitations
- security requirements
- deployment rules
- operational implications
- related configuration docs

Goal:

- make sure the proposed implementation is viable in AEMaaCS

### While Documenting

Search for:

- official terminology
- product names
- architecture phrasing
- best-practice language

Goal:

- produce documentation that matches Adobe vocabulary and platform concepts

---

## AEM Topic Routing Guide

| Need | First Repo to Check | Typical Areas |
|---|---|---|
| Architecture / platform model | `experience-manager-cloud-service.en` | `help/overview/` |
| Sling Models / component development | `experience-manager-cloud-service.en` | `help/implementing/developing/components/` |
| OSGi / config / deployment behavior | `experience-manager-cloud-service.en` | `help/implementing/deploying/`, `help/operations/` |
| Cloud Manager / pipelines | `experience-manager-cloud-service.en` | `help/implementing/cloud-manager/` |
| Dispatcher | `experience-manager-dispatcher.en` | `help/using/`, `help/security/` |
| Core Components | `experience-manager-core-components.en` | repo content / component docs |
| Content Fragments / headless | `experience-manager-cloud-service.en` | `help/headless/`, `help/assets/` |
| Tutorials / examples | `experience-manager-learn.en` | `help/cloud-service/` and related learning paths |

---

## How to Use Experience League Pages to Find the Repo

If the agent lands on an Experience League page first:

1. Look for the page's edit/pencil link if available.
2. Use that to identify the backing GitHub repo and markdown file.
3. Navigate the repo directly from that point forward.
4. Read nearby files to expand context.

This is often the fastest way to convert a rendered doc page into a reusable repo path.

---

## Evidence Rules for Agents

Agents should distinguish between:

### High-confidence evidence
- Official AdobeDocs markdown
- Official Experience League content
- Clear Adobe examples and recommendations

### Medium-confidence evidence
- Learning/tutorial content that is clearly Adobe-authored
- Repo-adjacent examples that align with product docs

### Low-confidence evidence
- Generic blogs
- Forum discussions
- Unverified code snippets
- Outdated AEM 6.x guidance when the task is AEMaaCS

Rule: do not let low-confidence evidence override current Adobe product docs.

---

## Anti-Patterns to Avoid

Agents should avoid the following:

- Jumping straight to implementation from memory without checking docs
- Using older AEM on-prem patterns for AEMaaCS tasks
- Treating tutorial content as stronger than product docs
- Relying on one isolated doc without checking surrounding docs
- Using generic blog guidance when an AdobeDocs source exists
- Producing code that ignores Cloud Service constraints

---

## Recommended Execution Loop

Use this loop during task execution:

1. Identify the task
2. Extract the technical topic
3. Choose likely repo
4. Search official AdobeDocs / Experience League
5. Read the primary file and nearby files
6. Extract supported patterns and constraints
7. Plan the implementation
8. Generate code/config/docs
9. Validate against official guidance
10. Document assumptions and any unresolved uncertainty

---

## Relationship to Other Reference Files

This playbook does not replace the other artifacts. It complements them.

Recommended usage:

- `AEM_CANONICAL_REFERENCES.md` → umbrella reference entry point
- `experience-league-agent-research-playbook.md` → how to search and use AdobeDocs during execution
- `ADOBEDOCS_SEARCH_INDEX.md` → fast topic-to-repo lookup
- `ADOBEDOCS_AGENT_TOOLS_SPEC.md` → tool contract / automation model
- `AEM_ARCHITECTURE_KNOWLEDGE_PACK.md` → curated domain knowledge
- `AEM_AGENT_REASONING_PROTOCOL.md` → mandatory reasoning workflow

---

## Recommended AGENTS.md Reference Pattern

Example:

```md
## Authoritative References

Agents should prefer these sources over general web results or older blog posts.

- Adobe AEM best practices and canonical Adobe guidance
  - See `@docs/ai/reference/AEM_CANONICAL_REFERENCES.md`
  - See `@docs/ai/reference/experience-league-agent-research-playbook.md`
  - See `@docs/ai/reference/ADOBEDOCS_SEARCH_INDEX.md`
  - See `@docs/ai/reference/AEM_ARCHITECTURE_KNOWLEDGE_PACK.md`
  - See `@docs/ai/reference/AEM_AGENT_REASONING_PROTOCOL.md`

If project rules conflict with external references, project rules take precedence unless explicitly overridden.
```

---

## Bottom Line

Agents should use Adobe Experience League repositories as a structured, authoritative knowledge source during execution.

The agent should not merely "look things up." It should:

- route to the correct repo quickly
- read official guidance before implementation
- use repo structure to expand context
- validate generated output against documented Adobe patterns
- fall back to generic web sources only when necessary
