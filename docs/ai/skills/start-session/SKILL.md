---
name: start-session
description: Ensures that, before engaging with human or starting new tasks, agents have reviewed all important project context, decisions, progress, and next steps from the prior working session and are fully informed snd prepared for optimal human interaction and task execution.
---
# Start Session

## Purpose

Ensures that, before engaging with human or starting new tasks, agents have reviewed all important project context, decisions, progress, and next steps from the prior working session and are fully informed snd prepared for optimal human interaction and task execution.

This skill prevents:
- context loss across chats
- repeated re-planning
- scope creep, AI hallucinations, and drift
- forgotten decisions

---

## When to Use

Run this skill:
- before making suggestions to human or making any changes at the beginning of sessions
- after switching topics or features
- after long pauses (hours/days)

This skill **MUST** be executed at the beginning of every work session.

If unsure, **run it anyway**.

---
## Instructions
---

### Inputs

- Current working branch (if Git repo is configured for the project)
- Files modified during the last session
- `@docs/ai/SESSION_COMPLETION_SUMMARY.md`
- `@docs/ai/SESSION_RESUME.md`
- `@docs/ai/CURRENT_FOCUS.md`
- `@docs/ai/DECISIONS.md`
- `@docs/ai/AGENT_SCRATCH_NOTES.md` 

---

### Steps

#### 1. Review Context-Critical Documentation

- `@docs/ai/SESSION_COMPLETION_SUMMARY.md`
- `@docs/ai/SESSION_RESUME.md`
- `@docs/ai/CURRENT_FOCUS.md`
- `@docs/ai/DECISIONS.md`
- `@docs/ai/AGENT_SCRATCH_NOTES.md` 

Internally summarize:

- What were the goals of the last session?
- What was completed in the last session?
- What are the goals for this session?
- After reviewing all the documentation, do I have any questions or required points of clarification for the human to address?

> [!IMPORTANT]
>
> **Non-negotiable:** Do not skip this step — it informs context for all tasks and human interaction during the session.

---

#### 2. Review/Update `@docs/ai/AGENT_SCRATCH_NOTES.md` (Required)

Add an entry to `@docs/ai/AGENT_SCRATCH_NOTES.md` summarizing your understanding of the information and instructions reviewed during step 1.

> [!IMPORTANT]
>
> **Non-negotiable:** **ALWAYS** follow instructions in `@docs/ai/AGENT_SCRATCH_NOTES.md` strictly adhering to template requirements defined in the document.

---

#### 3. Execute Start Session Macro

Execute macro: `@docs/ai/macros/SESSION_START.md`

---

## Success Criteria

You have complete situational awareness and context to intelligently and efficiently proceed with human interaction and project tasking.

> [!IMPORTANT]
>
> Ask yourself these two questions and answer with brutal, objective honesty:
>
> - Do I fully understand the objectives and goals of this project?
> - Do I feel 100% confident to move forward with project tasking?

---

## Reminder

- `@AGENTS.md` defines required rules, in addition to the rules files defined in the project **rules directory**.
- When defined in the project **skills directory**, skill files define procedures
- *This* skill ensures context completeness for optimal task execution, positive human and agent interaction, and session success.