# SHRSS Technical Design Documentation

## Audience

This documentation is for **SHRSS technical stakeholders** taking ownership of the SHRSS AEM Sites & Assets platform, including:

- Technical managers
- Technical architects
- Developers (backend, frontend, full-stack)
- System administrators
- Quality assurance engineers
- External consultants (e.g. Adobe or other partners) supporting the platform

## Purpose

These documents provide **technical design and architecture** of the current implementation to support:

- **Development** — New features, defect resolution, and refactoring
- **Run-and-operate** — Deployment, configuration, monitoring, and troubleshooting
- **Onboarding** — New technical employees or consultants joining the team
- **Knowledge transfer** — Reference during and after formal KT sessions

The documentation describes **what exists**, **how it is structured**, and **how components interact at runtime**. It is derived from implementation analysis of the codebase and configurations, with a focus on architecture and behavior rather than assessment or grading.

## How to Use This Documentation

1. **Start with the summary** — `SHRSS_Technical_Design_00_Summary.md` gives an overview of the platform, key modules, and pointers to each detailed document.

2. **Go deep by layer or concern:**
   - **Backend (Java, OSGi):** `SHRSS_Technical_Design_01_Backend_Architecture.md`
   - **Frontend (components, clientlibs, Webpack):** `SHRSS_Technical_Design_02_Frontend_Architecture.md`
   - **Integrations (Workday, DPLT, GraphQL, third-party):** `SHRSS_Technical_Design_03_Integrations.md`
   - **Dispatcher and CDN:** `SHRSS_Technical_Design_04_Dispatcher_Configurations.md`
   - **Runtime behavior (flows, data movement):** `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md`

3. **Live sites** — For context when reading the docs:
   - Hard Rock corporate site: https://www.hardrock.com
   - Reverb: https://reverb.hardrock.com
   - Careers (Stage, customer QA/UAT): https://aem.careers.stage.hardrock.com/

4. **Source of truth** — The implementation code and configurations in the SHRSS AEM repository are the source of truth. Counts (e.g. Sling models, servlets, AEM components) in these documents are aligned to the current codebase and should be updated when the implementation changes.

## Document Set

| Document | Description |
|----------|-------------|
| `SHRSS_Technical_Design_00_Summary.md` | Platform overview, modules, and navigation |
| `SHRSS_Technical_Design_01_Backend_Architecture.md` | Core bundle (models, services, servlets, OSGi config) |
| `SHRSS_Technical_Design_02_Frontend_Architecture.md` | ui.apps, ui.frontend, components, clientlibs |
| `SHRSS_Technical_Design_03_Integrations.md` | External systems and APIs |
| `SHRSS_Technical_Design_04_Dispatcher_Configurations.md` | Apache and Dispatcher configuration |
| `SHRSS_Technical_Design_05_Cross_Layer_Interactions.md` | Scenario-based runtime flows and interactions |

## Repository and Conventions

- **Codebase:** SHRSS AEM projects repository (e.g. `shrss-aem-projects`), branch `develop`.
- **Paths in this doc set:** File paths are relative to the repository root unless otherwise noted.
- **AEMaaCS:** Adobe Experience Manager as a Cloud Service. Configuration is immutable and source-code based; deployment is via Cloud Manager.

---

*This documentation set is maintained as part of the SHRSS Knowledge Transfer and platform handoff. For questions, contact the SHRSS technical leadership or the delivery team that produced the documentation.*
