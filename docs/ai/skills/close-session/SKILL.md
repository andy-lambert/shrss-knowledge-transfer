---
name: close-session
description: Ensures that all important context, decisions, progress, and next steps
from the current working session are documented.
---
# Close Session

## Purpose

Ensure that all important context, decisions, progress, and next steps
from the current working session are documented so
work can resume later without loss of continuity. It is IMPERATIVE that the documentation is thorough and current.

This skill prevents:
- context loss across chats
- repeated re-planning
- architectural drift
- forgotten decisions

---

## When to Use

Run this skill:
- before ending a Cursor / Codex / Claude Code session
- before switching topics or features
- before long pauses (hours/days)
- before asking another agent to continue the work

This skill **MUST** be executed at the end of every work session.

If unsure, **run it anyway**.

---
## Instructions
---

### Inputs

- Current working branch
- Files modified during the session
- Decisions made regarding documentation structure and content
- Open questions or uncertainties
- Planned next steps
- Notes generated during work session in `docs/ai/AGENT_SCRATCH_NOTES.md`

---

### Outputs

Before ending a session, update the following documents according to the instructions in the **Steps** section below:

- `docs/ai/AGENT_SCRATCH_NOTES.md` 
- `docs/ai/SESSION_COMPLETION_SUMMARY.md`
- `docs/ai/SESSION_RESUME.md`
- `docs/ai/CURRENT_FOCUS.md`
- `docs/ai/DECISIONS.md`

No session should end without these artifacts being current.

---

### Steps

#### 1. Summarize the Session (Internal)

Internally summarize:
- What was the session goal?
- What was completed?
- What changed compared to the start?

Do not skip this step — it informs all updates below.

---

#### 2. Review/Update `docs/ai/AGENT_SCRATCH_NOTES.md` (Required)

Follow instructions in `dcs/ai/AGENT_SCRATCH_NOTES.md` using required template.

---

#### 3. Update `docs/ai/SESSION_COMPLETION_SUMMARY.md` (Required)

### Purpose (Do not skip)

This document is the **authoritative record of what actually happened in this session**.
 Future agents, humans, and orchestrators will rely on it to understand:

- What progress was made
- What did *not* get done (and why)
- What changed compared to the start of the session
- Whether the session succeeded, partially succeeded, or is blocked

If this document is vague, incomplete, or inaccurate, **cross-session continuity fails**.

### Instructions

- **Adhere strictly to `SESSION_METADATA.md`**
  - Do not restate metadata here
  - Ensure all references (session ID, scope, agents) are consistent
- Populate **every required section** in the template
- Prefer **concise, factual bullets** over narrative prose
- Write as if **you will not be present** in the next session

### Required content guidance

- **Executive Summary**
  - State the original objective
  - State the actual outcome
  - Explicitly call out deltas between intent and reality
- **What Was Done**
  - List concrete actions, artifacts, or decisions
  - Avoid vague phrases like “worked on” or “looked into”
- **What Was NOT Done**
  - This is mandatory if *anything* was deferred
  - Include the reason (time, dependency, scope decision)
- **Artifacts**
  - Enumerate all created, updated, or deprecated files
  - This is how future agents know what changed without guessing
- **Decisions**
  - Reference `docs/ai/DECISIONS.md`
  - Do not re-argue decisions here—record outcomes only
- **Exact Resume Point for Next Session**
  - This must be precise enough that a new agent can resume in under 5 minutes

### Tone and intent

- This is **not a journal**
- This is **not a justification**
- This is a **durable operational record**

If you feel tempted to write “see scratch notes,” stop and summarize instead.

------

## 4. Update `docs/ai/SESSION_RESUME.md` (Required)

### Purpose (Do not skip)

This document is the **single entry point for the next session**.
 It exists to prevent cold starts, rework, and context loss.

If this document is weak, the next session will:

- Re-read too much
- Re-decide settled questions
- Miss critical constraints
- Waste time reconstructing intent

### Instructions

- **Treat this as a handoff document**
  - Assume the next agent has *not* read scratch notes
  - Assume minimal patience and limited context window
- **Align with `SESSION_METADATA.md`**
  - Session identity, scope, and constraints must match
- Update the document *after* completing the completion summary

### Required content guidance

- **🔥 30-Second Summary**
  - This should be readable in under 10 seconds
  - If this section is unclear, the rest will be ignored
- **MUST READ (In Order)**
  - Limit to the *minimum viable set* (3–5 items)
  - Each item should justify *why* it must be read
- **Current Objective**
  - One primary goal only
  - No multi-goal hedging
- **Success Criteria**
  - Measurable, binary conditions when possible
- **Where to Pick Up (Exact Resume Point)**
  - File path
  - Section / function / line range
  - First concrete action
  - This is the most important section in the file
- **Open Questions / Risks**
  - Only include unresolved, actionable items
  - Avoid speculation or narrative

### Tone and intent

- This document should read like **instructions, not commentary**

- Optimize for **speed, clarity, and confidence**

- The goal is that the next agent says:

  > “I know exactly where to start and what not to redo.”

------

> [!IMPORTANT]
> ***Non-Negotiable Rule** (Applies to Both SESSION_COMPLETION_SUMMARY.md and SESSION_RESUME.md)*
>
> *If you cannot clearly explain what changed this session and exactly how to continue, you are not done closing the session.*
>
> ***Closing the session is part of the work—not overhead.***

---

## 5. Update `docs/ai/CURRENT_FOCUS.md` (Required)

Update or append the following sections:

- Today’s objective
- Work completed
- Session Metrics
- Current State
- What’s next (prioritized)
- Open Questions / Blockers

Be concise but explicit. Assume the next reader has *not* seen this session.

---

## 6. Record Decisions (If Any)

If any decision affected project artifacts  (code, documentation, digital content/assets, etc.)

Then:

- Add an entry to `docs/ai/DECISIONS.md`
- Include:
  - date/time
  - context
  - decision
  - follow-ups
  - references

If no decisions were made, explicitly note:
> “No new decisions in this session.”

---

### 7. Final Session Summary

At the bottom of  `docs/ai/CURRENT_FOCUS.md`, add a short summary under *Final Session Summary* section:

- Focused on outcomes, not implementation details
- 5–7 bullet points sumarizing session
- Immediate next steps
- New tasks/recommendations/considerations/issues from notes capured during this session's work and/or documented in `docs/ai/AGENT_SCRATCH_NOTES.md`


This summary is optimized for:
- future you
- another agent
- long gaps between sessions

---

### 8. Execute Close Session Macro

Execute macro: `docs/ai/macros/SESSION_CLOSE.md`

---

## Guardrails

- Do NOT invent progress that did not happen
- Do NOT silently skip decision logging
- Do NOT leave TODOs only in chat history
- Prefer over-documenting to under-documenting

---

## Success Criteria

A new agent (or the same agent days later) should be able to:

- understand the current state in under 5 minutes
- know exactly what to do next
- avoid re-making decisions
- continue work without asking basic context questions

If this is not true, the session was not properly closed.

> Answer these two questions with brutal honesty:
> - If this were handed to a new agent, could they continue without questions?
> - If ***I*** had never worked on this project and this were handed to ***me***, could ***I*** execute effectively and confidently without questions?

---

## Reminder

- `@AGENTS.md` defines required rules, in addition to the rules files defined under `.cursor/rules/*` / `.claude/rules`
- When defined, skill files define procedures: `.cursor/skills/*` /  `.claude/skills/*`
- *This* skill preserves continuity.