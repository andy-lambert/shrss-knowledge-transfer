---
description: "Enforce agent session start/close discipline and checklist acknowledgement"
alwaysApply: true
---

## What

This rule enforces mandatory session hygiene for all agent work related to
analysis, architecture, and documentation tasks.

---

## Why

Long-running analytical tasks degrade rapidly without:
- consistent context loading
- explicit scope confirmation
- durable handoff artifacts

This rule prevents:
- drift
- speculative problem-solving
- loss of context across sessions
- undocumented assumptions

---

## Scope

Applies to:
- analysis
- task execution

---

## Enforcement

### Session Start (Mandatory)

Before performing any work, the agent MUST:

1. Execue macro: `docs/ai/macros/SESSION_START.md`
   
2. State explicitly:
   > “Session initialized per agent-session-governance rule.”

Failure to do so invalidates all subsequent work.

---

### Session Close (Mandatory)

Before ending a session, the agent MUST:

1. Update `@AGENT_SCRATCH_NOTES.md`
2. Update `docs/ai/CURRENT_FOCUS.md`
3. Add or update `docs/ai/DECISIONS.md` entries (if applicable)
4. Summarize:
   - findings
   - open questions
   - recommended next actions

If any step cannot be completed, the agent must state why.

---

## Consequences

Ignoring this rule results in:
- unreviewable output
- loss of architectural trust
- forced re-analysis

This rule is non-negotiable.
