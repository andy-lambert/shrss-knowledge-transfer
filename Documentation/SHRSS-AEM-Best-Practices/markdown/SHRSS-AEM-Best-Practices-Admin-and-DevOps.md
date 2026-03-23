# AEMaaCS Admin & DevOps Best Practices

*Admins, SREs, DevOps – SHRSS Volume*

------

## 1. Role & Responsibilities

As an AEMaaCS admin/DevOps engineer for SHRSS, you:

- Own the **health and reliability** of AEM environments.
- Manage **Cloud Manager, pipelines, environments, access, and logging**.
- Serve as the **first line of triage** for production issues (performance, availability, security).
- Enforce guardrails so engineering and authoring teams operate safely.

Use the **Consolidated All‑Roles Volume** for shared concepts.

------

## 2. Environment & Program Management

### 2.1 Programs, Environments, and RDEs

- Keep environments clearly labeled and documented:
  - **DEV** – daily integration testing.
  - **STAGE** – pre‑production validation.
  - **PROD** – live traffic.
  - **RDE** – rapid experimentation and troubleshooting.
- Use **consistent run modes** and avoid environment‑specific hacks; all differences should be in configs.

**References**

- [Manage environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments)  
- [Rapid Development Environments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/rapid-development-environments)

#### SHRSS Overlay

- SHRSS relies heavily on **external integrations** (Workday, DPLT, translation). For each environment:
  - Maintain clear mapping of endpoints and credentials (e.g., Workday sandbox vs production).
  - Use environment variables and OSGi configs; never let devs embed URLs in code.
- Document:
  - **Which integrations are active in which envs** (some may be disabled in DEV).
  - Any **data anonymization** or subset rules in non‑prod.

------

## 3. Cloud Manager Pipelines

### 3.1 Pipeline Types & Usage

- **Non‑production pipeline**
  - Builds and deploys to DEV.
  - Runs code quality, security, functional tests.
- **Production pipeline**
  - Deploys to STAGE then PROD.
  - Includes performance and experience audits.
  - Requires approvals and change management alignment.

**References**

- [CI/CD Pipelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/overview/ci-cd-pipelines)

### 3.2 Quality Gates as Policy

- Treat quality gates as **policy**, not suggestions:
  - Code quality: no Critical or Major issues without documented exceptions.
  - Security: no open critical vulnerabilities.
  - Performance: monitor regressions.

#### SHRSS Overlay

- Given SHRSS’s heavy reliance on **Jobs/Events search**:
  - Monitor code quality findings related to **index definitions** and **query patterns**.
  - If a pipeline fails on custom index rules, escalate to engineering rather than bypassing.
- Ensure **integration tests** in `it.tests` validate:
  - Jobs listing behavior for basic filters.
  - At least one happy‑path flow per integration (Workday sync, DPLT sync) where possible.

------

## 4. IAM, Access & Permissions

### 4.1 Product Profiles & AEM Groups

- Use **Adobe Admin Console** for identity and group management:
  - Product profiles: `AEM Users`, `AEM Administrators`.
- Map identity groups to AEM groups for permissions:
  - E.g., `shrss-authors` → `content-authors-shrss` group in AEM.

**References**

- [Assigning AEM Product Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem)

#### SHRSS Overlay

- Codify a **role mapping table**:
  - Marketing authors, Recruiters, DAM librarians, Admins, etc.
  - Map each to AEM groups and product profiles.
- For Jobs & Events:
  - Restrict who can publish to **production-critical CF folders** (e.g., Jobs/Events CFs).
  - Implement review/approval workflows where legally required (e.g., job postings).

------

## 5. Dispatcher & Security

### 5.1 Dispatcher Configuration

- Store all dispatcher configs under the `dispatcher` module; manage via pipelines.
- Key files:
  - `conf.d/enabled_vhosts` – virtual hosts.
  - `conf.dispatcher.d/enabled_farms` – farms, cache rules, filters.

**References**

- [Dispatcher Configurations in Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/en/docs/events/tech-sessions/2025/dispatcher-configurations)  
- [Dispatcher Overview](https://experienceleague.adobe.com/en/docs/experience-manager-dispatcher/using/dispatcher)

### 5.2 Security Filters

- **Block by default**, then explicitly allow:
  - Block `/system/console`, `/crx/*`, `/bin/*` except whitelisted endpoints.
  - Block author/publish admin endpoints from public internet.
- Ensure HTTPS and HSTS are enabled as required by policy.

#### SHRSS Overlay

- SHRSS has custom endpoints for:
  - Jobs/Events/News APIs, GraphQL persisted queries, integration callbacks.
- For each endpoint:
  - Confirm it is **explicitly allowed** and **properly cached or non‑cached** in dispatcher.
  - Validate:
    - No author‑only endpoints are exposed.
    - No Workday/DPLT webhook endpoints are reachable without appropriate access control if applicable.

------

## 6. Monitoring, Logs & Troubleshooting

### 6.1 Logging Strategy

- Use Cloud Manager to:
  - Download logs for historical investigation.
  - Set up **log ingestion** into central observability solutions if available.
- Use Developer Console for:
  - Live log tail.
  - Health checks, status dumps.

**References**

- [Debugging AEM as a Cloud Service with the Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)

### 6.2 Performance & Query Tools

- Use:
  - **Query Performance Tool / Query Analyzer** for slow queries.
  - **Oak logs** and warning messages such as “query without index detected.”
- Coordinate with engineering to:
  - Add or refine index definitions.
  - Simplify or constrain high‑cost queries.

#### SHRSS Overlay

- Periodically examine top queries on **Jobs**, **Events**, and **News**:
  - Look for scans over `/content/dam` without path constraints.
  - Look for fulltext queries without appropriate indexes.
- When Jobs search performance regresses:
  - First check queries via Query Analyzer.
  - Then ensure the `damAssetLucene-*` customizations deployed for SHRSS are in place and not reversioned.

------

## 7. Change & Release Management

- Tie every deployment to a **change record** with:
  - Description, risk, rollback strategy.
- Maintain a **runbook** for:
  - Common incidents (slow Jobs search, missing Events, dispatcher cache issues).
  - Rolling back to previous artifacts and invalidating caches.

#### SHRSS Overlay

- Ensure runbooks include:
  - Paths to critical CF folders (Jobs, Events, News, Locations).
  - Index names and locations for SHRSS customizations.
  - Known troubleshooting flows (e.g., how to verify Workday sync status and logs).

------

## 8. Admin & DevOps SHRSS Overlay Summary

- Treat SHRSS as a **search‑heavy, integration‑heavy AEMaaCS solution**, not just basic WCM.
- Invest in **pipeline quality**, **dispatcher security**, and **index monitoring** as first‑class ops concerns.
- Keep **clear documentation** of environment differences, integration endpoints, and runbooks.

Use this alongside:

- The **Consolidated All‑Roles Volume**.
- The **Engineering Volume** (for code‑level practices).
- The **Indexing & Performance Volume** (for query/index ops details).