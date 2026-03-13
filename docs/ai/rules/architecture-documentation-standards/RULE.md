---
description: "STOP Protocol should be used any time we plan to add or modify any code (or key documentation during analysis projects/tasks).  It helps avoid re-work and creating extra technical debt, and forces us to work smarter, not harder.""
alwaysApply: true
---
# NON-NEGOTIABLE ARCHITECTURE DOCUMENTATION STANDARDS
   - ❌ **No diagrams without prose** (diagrams must reduce complexity, not decorate)
  - When prose and diagrams conflict, **prose is authoritative**.

- ❌ **No component listings without flow**
- ❌ **No “calls into” or “handles logic” language**
- ✅ Every interaction must:
  - Have a **trigger**
  - Name **data ownership**
  - Describe **failure behavior**

> [!IMPORTANT]
>
> If the interaction cannot be expressed as a numbered execution flow, it is incomplete.

## Analysis Anti-Patterns (Explicitly Prohibited)

Agents **MUST NOT**:

- Rewrite documentation structure without approval
- Normalize or “clean up” architecture during analysis
- Introduce new abstractions while documenting existing ones
- Optimize for elegance over accuracy
- Collapse uncertainty instead of recording it in `@docs/ai/DECISIONS.md`

Analysis favors **fidelity over aesthetics**.

## Scope Governance

Any recommendation that would require touching more than one module MUST be logged as a **Decision Candidate**, not a recommendation.