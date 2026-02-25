---
description: "STOP Protocol should be used any time we plan to add or modify any project artifact (code, documentation, digital content/assets).  It helps avoid re-work and creating extra technical debt, and forces us to work smarter, not harder.""
alwaysApply: true
---
## *MANDATORY* Infrastructure Analysis (STOP Protocol):
   Before creating ANY project artifact, you MUST complete the STOP protocol:

   **S** - **Search** for existing implementations or versions
   - Use provided tools for searching project artifacts
   - Also consider using grep and a few variations on wording to be comprehensive
   - Understand what dependencies we have and if they have any impact

   **T** - **Think** about why existing artifacts might not work:
   - Document what exists and why it might be insufficient
   - Regarding code artifacts, check if standard libraries solve the problem or if we're using one that is out of date
   - Verify if existing artifacts can be extended/modidfied instead of creating new abstractions

   **O** - **Outline** how your solution integrates with existing patterns:
   - Show how it fits with established patterns
   - Confirm it follows existing configuration, organizational, or design patterns (defined best practices, design principles, logging, telemetry, localization, organization/naming conventions, documentation standards)
   - For code, verify it uses existing validation frameworks and commons utilities

   **P** - **Prove** that a new abstraction or artifact is necessary:
   - For code changes, document unique business logic that justifies custom implementation
   - Explain why existing resources or artifacts are insufficient (with evidence)
   - Confirm this is the simplest solution that could work