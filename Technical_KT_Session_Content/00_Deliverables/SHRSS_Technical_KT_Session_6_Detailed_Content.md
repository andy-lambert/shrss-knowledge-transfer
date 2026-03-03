# Session 6 — DevOps Part 2, Conclusion / Q&A / Customer topics

**Duration:** 2 hours  
**Presenters:** Andy Lambert, Vinay S A  
**Agenda reference:** `SHRSS_Technical_KT_Main_Agenda.md`  
**Exercises:** `SHRSS_Technical_KT_Exercises_Supplemental.md` (Session 6)

---

## DevOps — Part 2 (Andy) — 32 min

### Pipelines deep dive (build, quality, security, deployment) — 14 min

- **Build step:** Maven build (or configured build command); compiles `core`, builds `ui.frontend`, packages `ui.apps`, `all`, etc. Output: deployable artifacts. Failures: dependency issues, test failures, frontend build errors.
- **Quality step:** Code quality (e.g. SonarQube); may fail on quality gates (coverage, bugs, vulnerabilities). Address by improving code or adjusting gates (per policy).
- **Security step:** Dependency and/or code scanning. Critical/high vulnerabilities can fail the pipeline. Fix dependencies (upgrade, replace) or document exceptions per process.
- **Deployment step:** Deploys to the target environment (e.g. Stage, Prod). May include content deployment or skip if code-only. Rollback = redeploy previous artifact per Cloud Manager.
- **Custom testing steps:** **Custom Functional Testing** runs `it.tests` (integration tests); **Custom UI Testing** runs `ui.tests` (Cypress). Configured in pipeline; failures fail the pipeline. Reference task doc and implementation analysis for SHRSS pipeline configuration.

**SHRSS-specific:** 4 integration tests, 8 UI tests (exec summary); pipeline runs them in custom steps. Reference `00_EXEC_SUMMARY.md` and testing staging docs.

---

### Logs and monitoring (Cloud Manager, AEM logs) — 10 min

- **Cloud Manager:** Pipeline logs per step (build, quality, security, deploy, test). Use for build failures, test output, deployment errors. Logs are retained per Adobe policy.
- **AEM logs:** Developer Console or Cloud Manager → Logs for author/publish. Stream or download; filter by level and logger. Use for runtime errors, performance, and integration issues.

**Reference:** Experience League — Cloud Manager pipelines and logging; AEM Developer Console.

---

### Troubleshooting failed pipelines and deployments — 8 min

- **Build failure:** Read build log; fix compilation, test, or frontend errors. Run same Maven command locally if possible (`mvn clean install -pl core`, etc.).
- **Quality/Security failure:** Address reported issues or adjust gates; document exceptions.
- **Deployment failure:** Check deployment log; may be environment-specific (config, permissions, resource limits). Retry or roll back.
- **Test failure:** Open Custom Functional or UI test log; fix failing test or fix product code. Run tests locally when possible (`it.tests` against running AEM; `ui.tests` Cypress).

**Exercise cross-reference:** Exercise 4.3 — Open pipeline logs in Cloud Manager (homework).

---

## Testing (Andy / Vinay) — 38 min

### Unit tests — 12 min

- **Scope:** JUnit tests in `core` for models, services, servlets, utils. SHRSS: 193 tests, 59.2% file coverage; **models 93.8%**, **services 94.1%** (excellent). Schedulers, listeners, workflows: 100% file coverage but test quality gaps (idempotency, error handling) — Phase 3 finding.
- **Run locally:** `mvn clean test -pl core` (or per project README). Run in pipeline as part of build step.
- **Best practices:** Mock external services and ResourceResolver where appropriate; test idempotency for schedulers/listeners/workflows; no hardcoded credentials in test or production code (GraphQLUtils P0).

**Repo paths:** `core/src/test/java/com/shrss/core/`; example `CardImplTest.java`. **Exercise 4.1** — Run unit tests locally.

**Reference:** `00_EXEC_SUMMARY.md` (coverage); `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md` (test quality, ISSUE-TESTING-*).

---

### Integration tests — 10 min

- **Framework:** AEM testing client; tests run against a running AEM instance. In SHRSS: `it.tests` module; 4 tests. Executed in Cloud Manager during **Custom Functional Testing** step.
- **Purpose:** Validate component or API behavior in real AEM (author/publish). Setup/teardown of test content; use of real or mock services per test design.
- **Run locally:** Typically need running AEM (local SDK or RDE) and Maven profile or command to run `it.tests` (see project README/pom).

**Repo path:** `it.tests/`. **Exercise 4.2** — Locate integration test entry points (homework).

---

### UI tests — 10 min

- **Framework:** Cypress in `ui.tests` module. 8 Cypress tests for 95 components (minimal coverage — exec summary). Executed in Cloud Manager during **Custom UI Testing** step.
- **Purpose:** End-to-end UI behavior (e.g. page load, component visibility, navigation). Run in pipeline after deployment to test environment.
- **Run locally:** Cypress runner against deployed URL; see `ui.tests/` config and README.

**Repo path:** `ui.tests/`. **Exercise 4.2** — Locate UI test config and sample spec (homework).

---

### Where tests run in the pipeline and how to run locally — 6 min

- **Pipeline:** Build step runs unit tests (Maven test phase). Custom Functional Testing runs `it.tests`; Custom UI Testing runs `ui.tests`. Order: build (unit) → deploy → (optional) functional → (optional) UI. Failure in any step can fail the pipeline.
- **Local:** Unit: `mvn test -pl core`. Integration: as documented (AEM + it.tests). UI: Cypress against target URL. Reference exercise supplemental and project docs.

**Reference:** Task doc; `00_EXEC_SUMMARY.md`; `staging/testing/STRUCTURAL_TESTING.md` if available.

---

## Conclusion / Q&A / Customer topics — 48 min

### Open Q&A — 20 min

- Reserve time for questions on any session topic: architecture, code structure, backend, frontend, integrations, Dispatcher, DevOps, testing. Use main agenda and detailed session docs as reference.

---

### SHRSS-prioritized topics — 18 min

- **From authoring sessions (Answer 3):** Any topics identified during authoring KT (Gonzalo, TJ, Tim) that should be reinforced or clarified for technical stakeholders. No additional SHRSS topics beyond those (Answer 4).
- **Examples:** Specific integrations (Workday, DPLT, GraphQL), security remediation (P0 servlet auth, hardcoded creds, test servlets), migration prep for 11 sites, Unity/headless roadmap. Use implementation analysis and Optimized SDD for remediation priorities (e.g. 14 P0 issues, quality grade C+).

**Reference:** `00_EXEC_SUMMARY.md` (critical gaps, remediation); `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md` (roadmap); authoring transcript `KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md`.

---

### Next steps and follow-up — 10 min

- **Suggested next steps:** Remediate P0 issues (security, Dispatcher auth, GraphQL syntax/creds); add idempotency tests and fix idempotency in schedulers/listeners/workflows; increase integration/UI test coverage where valuable. Use implementation analysis remediation roadmap.
- **Follow-up:** Share refined agenda, exercise supplemental, and session detailed content with participants. Point to Experience League and `docs/ai/reference/` for ongoing learning. Confirm ownership of backlog (Jira, Confluence) and who drives next-phase migrations.

---

*End of Session 6 detailed content. Adjust timings in this document and in the main agenda as needed during delivery.*
