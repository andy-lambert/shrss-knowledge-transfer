# AEM as a Cloud Service – Developer Console Access & Troubleshooting Guide for SHRSS

### 1. Purpose & Audience

This guide is for **developers, technical architects, and AEM admins** using **AEM as a Cloud Service** at SHRSS. It covers:

- How to **configure roles and product profiles in Adobe Admin Console** so users can access:
  - Cloud Manager
  - AEM environments
  - AEM Developer Console
- How to **open and navigate Developer Console**
- A reference to **all main tools/views in Developer Console**
- **Hands‑on exercises** to learn the console
- **Concrete troubleshooting scenarios** where Developer Console is the primary diagnostic tool

------

## 2. Access & Permissions – Admin Console Setup

### 2.1 Conceptual model

Access to Developer Console relies on three layers:

1. **Adobe Admin Console**
   - Grants access to:
     - **Cloud Manager** (program & pipelines)
     - **AEM as a Cloud Service** environments (author/publish, RDE)
   - Done via **Product Profiles** and user groups
     *Reference: Admin Console cheat sheet for AEM CS shows that AEM as a Cloud Service access is managed from Admin Console and mapped into AEM product profiles.*
     [Mastering the Adobe Admin Console](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Delivery Support Resources/Competencies/CJM (AC, AJO, MKTO)/Practice Circle/Marketo/04. Deskside Coaching Activity Files/Admin Console/Mastering the Adobe Admin Console.pptx)
2. **Cloud Manager roles**
   - Control **who can see environments and pipelines** and open Developer Console.
   - Roles per program:
     - **Developer**
     - **Deployment Manager**
     - **Program Manager**
     - **Business Owner**
3. **AEM Author/Publish roles**
   - Product profiles such as:
     - `AEM Administrators - author - Program <id> - Environment <id>`
     - `AEM Users - author/publish - Program <id> - Environment <id>`
   - These profiles map to groups inside the AEM instance.

### 2.2 Recommended SHRSS personas & required access

Use this table as the baseline for SHRSS:

| Persona                      | Typical responsibilities                                  | Admin Console product profiles (minimum)                     | Cloud Manager role                                           | AEM in-product access                                        |
| ---------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Admin**                    | Environment governance, security, overall troubleshooting | - `Cloud Manager – System Admin` or Product Admin for Cloud Manager - `AEM Administrators - author` for all non-prod & prod envs | Program Manager or Deployment Manager                        | Full admin on AEM (author), read access to publish as needed |
| **Technical Architect (TA)** | Solution design, deep diagnostics, code/config reviews    | - Cloud Manager: Developer or Deployment Manager - `AEM Administrators - author` for non-prod, at least read on prod | Developer (and Deployment Manager if they trigger pipelines) | Admin on non-prod AEM                                        |
| **Developer**                | Feature implementation, debugging in dev/RDE              | - Cloud Manager: Developer - `AEM Users - author` for dev & RDE | Developer                                                    | Developer-level access on dev/RDE author                     |

> **Note:** Exact profile names differ per tenant/program, but structure should follow the patterns above. Use existing `AEM Administrators` / `AEM Users` / Cloud Manager profiles rather than creating bespoke ones where possible.
> [Internal DAM role examples](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Libraries/Customer Library/G/Groupe Technologies Desjardins _276750/202508_Tool Workflow and Governance Optimization_Assets/Customer Documents/100 - DAM - Personas_3c6b3264a68e497ca1a3d28ab4d8cca1-280825-1103-926.pdf)

### 2.3 Step-by-step: configuring access in Admin Console

These steps assume you are a **System Admin** or **Product Admin** for AEM and Cloud Manager.

#### 2.3.1 Verify Cloud Manager product access

1. Go to **Admin Console** → **Products**.
2. Open **Cloud Manager**.
3. For the SHRSS IMS org/program:
   - Ensure you have product profiles corresponding to Cloud Manager roles:
     - `Cloud Manager – Developer`
     - `Cloud Manager – Deployment Manager`
     - `Cloud Manager – Program Manager`
4. For each SHRSS user:
   - Assign them to the appropriate Cloud Manager profile based on the persona table.

#### 2.3.2 Verify AEM environment product profiles

1. Still in **Admin Console** → **Products**, open **AEM as a Cloud Service**.
2. For each SHRSS program:
   - You will see product profiles in the style:
     - `AEM Administrators - author - Program 130352 - Environment 1363656`
     - `AEM Users - author - Program 130352 - Environment 136827`
     - `AEM Users - publish - Program 130352 - Environment <id>`
       See the Desjardins example for this naming pattern.
       [DAM Personas / AEM Admin groups example](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Libraries/Customer Library/G/Groupe Technologies Desjardins _276750/202508_Tool Workflow and Governance Optimization_Assets/Customer Documents/100 - DAM - Personas_3c6b3264a68e497ca1a3d28ab4d8cca1-280825-1103-926.pdf)
3. For each persona:
   - **Admins / TAs**
     - Add them to `AEM Administrators - author` for dev, stage, and prod environments where they need console access.
   - **Developers**
     - Add to `AEM Users - author` for dev/RDE (and **not** prod, unless explicitly needed).
4. Wait a few minutes for provisioning to propagate.

#### 2.3.3 Quick validation

For any given user:

- They should see the **Cloud Manager card** under **experience.adobe.com**.
- In Cloud Manager:
  - They should see the **SHRSS program**.
  - In the program’s **Environments** view they should see at least the **dev** environment tile.
- From that tile, they should see the **Developer Console** option (details in the next section).
  If they see AEM itself but **Developer Console says “Login failed / unable to login”**, it’s almost always a roles/profile mismatch. See the public access doc:
  [AEM Developer Console Access](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console.html?lang=en#developer-console-access) (linked in internal Slack guidance: [Developer Console access troubleshooting](https://adobe.enterprise.slack.com/archives/C02JN4EJN/p1618985919.126000)).

------

## 3. Opening Developer Console

### 3.1 From Cloud Manager UI (recommended for SHRSS)

1. Sign in at **Experience Cloud**: `https://experience.adobe.com`.
2. Open **Cloud Manager**.
3. Select the SHRSS **program**.
4. In **Environments**:
   - Locate the target environment (e.g., `dev`, `stage`, `prod`, or `RDE`).
   - Click the **ellipsis** (`…`) or environment actions menu.
   - Choose **Developer Console**.

If roles and profiles are correct, a new tab with Developer Console opens and logs you in via SSO. If you see **“Login failed / Unable to login”**, go back to Section 2.3 and confirm product profile assignments.
[Developer Console access issue example](https://adobe.enterprise.slack.com/archives/C02JN4EJN/p1618985919.126000)

### 3.2 Direct URL pattern

For reference or docs:

- Developer Console URL pattern is:

```text
https://dev-console-<namespace>.<cluster>.dev.adobeaemcloud.com/#release-<service-id>
```

This is derived from the author/publish URL by replacing the host with `dev-console-…`.
Documented in AEM CS design best practices:
[AEM Cloud Service Design Workshop – Developer Console URLs](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Delivery Support Resources/Success Accelerators/Launch Advisory/Launch Advisory Delivery templates/AEM AWPs/MS3 Design/Launch Advisory AEM Cloud Services Design Best Practices.docx)

### 3.3 Cloud Manager CLI shortcut (for power users)

Developers can open Developer Console via the **Cloud Manager CLI**:

```bash
aio cloudmanager:open-developer-console <ENVIRONMENT_ID> --programId <PROGRAM_ID>
```

Requires:

- Cloud Manager access (Developer or higher)
- `aio` CLI installed and authenticated

Same command is documented in internal AEM CS design best practices.
[Cloud Manager CLI – open developer console](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Delivery Support Resources/Success Accelerators/Launch Advisory/Launch Advisory Delivery templates/AEM AWPs/MS3 Design/Launch Advisory AEM Cloud Services Design Best Practices.docx)

------

## 4. Developer Console Overview – Tools & Views

Developer Console provides **real-time diagnostics per environment** (author/publish).
Key description from internal docs:

> Tabs include **Status, Java Packages, Servlets, Queries, and Integrations**. On the Status tab, a “Status Dump” drop-down lets you select datasets (e.g., Bundles) and output format (Text/JSON) to retrieve OSGi bundle state, configuration, etc. There’s also a collapsed **AEM ADMIN LOGIN** section for direct author login when needed.
> [AEM CS Developer Console overview (Slack)](https://adobe.enterprise.slack.com/archives/CCCG5K2JH/p1747911978.032149)

### 4.1 High-level layout

- **Header**
  - Program & environment
  - Current pod (e.g. `cm-p10961-e19892-aem-author-69f8dc7b7d-hxckv`)
  - Status (e.g. `starting`, `running`), with info banner when instance is booting
- **Main tabs**
  - **Status**
  - **Java Packages**
  - **Servlets**
  - **Queries**
  - **Integrations**
  - (plus newer tabs as features evolve, e.g., Logs, depending on rollout)
- **AEM Admin Login**
  - Collapsed panel allowing SSO jump into the author UI as an admin.

### 4.2 Status tab – Status Dumps

Key elements:

- **Status Dump dropdown**
  - Common datasets:
    - `Bundles` – OSGi bundle states
    - `Components` – OSGi components/services
    - `Configurations` – OSGi configurations (PIDs & values)
    - `Jobs`/`Schedulers` – depends on version; job details may be limited in CS
- **Output format**
  - `TEXT` – human-readable
  - `JSON` – machine-friendly, useful to diff between releases or feed into tools
- **Get Status**
  - Executes the dump for the current pod

Internal examples describe use for bundles and configuration inspection.
[How to use Developer Console for status dumps](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1588348664.063200)

### 4.3 Java Packages tab

- Shows exports/imports of OSGi bundles at the Java package level.
- Useful for:
  - Identifying **missing packages** or version mismatches causing `Import-Package` resolution errors.
  - Checking that a custom bundle exports expected packages.

### 4.4 Servlets tab

- Lists registered servlets and their mappings. Typically includes:
  - Registered **paths**
  - **Selectors**
  - **Extensions**
  - Owning component/bundle
- Use cases:
  - Determine which servlet serves `/bin/...` or some API endpoint.
  - Diagnose path/selector conflicts when a request returns unexpected output or 404.

### 4.5 Queries tab

- Allows running **JCR-SQL2 or query builder** queries against the repository.
- Often includes:
  - Query text
  - Execution time
  - (Depending on version) index information or plan details
- Use cases:
  - Reproduce slow queries reported by logs.
  - Verify which index is being used.
  - Validate repository structure/content without CRXDE.

### 4.6 Integrations tab

- Lists configured **integrations** (varies by version):
  - E.g., eventing, external endpoints, or AEM CS–internal integrations
- Use cases:
  - Verify that expected integrations are present and in a good state.

### 4.7 Logs & related diagnostics

Blocked-queue and other errors surface in:

- **Content Distribution UI** (in AEM author)
- **Error logs accessible via Developer Console**

Internal SRE notes:

> “Customers can view error logs when a content distribution queue becomes blocked. Logs appear in the Content Distribution UI and in the AEM logs accessible through the Developer Console.”
> [Blocked queues & Developer Console logs](https://adobe.enterprise.slack.com/archives/C01MSQMC16K/p1728895177.797039)

For more extensive logging, complement with Cloud Manager log downloads and CLI tailing:  

- [Managing logs in AEM CS](https://adobe.enterprise.slack.com/archives/C0143J81A9E/p1621925532.055600)  
- [Tail logs via Cloud Manager CLI](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1741193329.434119)

------

## 5. Tool/Tab → Use-case Reference

Use this table when training devs/TAs/admins:

| Tab/Tool                         | What it shows                                                | Primary users  | Typical uses                                                 |
| -------------------------------- | ------------------------------------------------------------ | -------------- | ------------------------------------------------------------ |
| **Status → Bundles**             | All OSGi bundles + state (Active, Resolved, Installed)       | Dev, TA, Admin | Check custom bundle deployment after pipeline; find bundles stuck in `Installed` or `Resolved`; verify versions |
| **Status → Components**          | Declarative Services components, activation state, references | Dev, TA        | Identify unsatisfied references, cyclic dependencies, and why a service is not active |
| **Status → Configurations**      | OSGi configs (PIDs, properties)                              | Dev, TA, Admin | Confirm that environment-specific configs (e.g. loggers, endpoints) are present and correct in CS, particularly when behavior differs from SDK |
| **Status → Jobs/Schedulers**     | (When available) scheduled jobs summary                      | TA, Admin      | Rough verification of scheduled jobs; note that detailed sling job console is not exposed in CS (confirmed internally) [Sling jobs status limitation](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1695657321.155189) |
| **Java Packages**                | Import/export package view                                   | Dev, TA        | Debug classloading and missing package issues (e.g., `NoClassDefFoundError` after deploying new libs) |
| **Servlets**                     | Registered servlets and mappings                             | Dev, TA        | Debug `/bin`/`/services` endpoints; confirm which servlet handles a path/selector; detect conflicts |
| **Queries**                      | Query execution on repository                                | Dev, TA        | Reproduce slow queries and align index configuration; confirm data existence and structure |
| **Integrations**                 | Integration metadata (varies by version)                     | TA, Admin      | Confirm configuration of external integrations supported by AEM CS |
| **Logs (via Developer Console)** | Error/other logs for current pod                             | TA, Admin      | Spot stack traces for blocked queues, startup failures, etc. Complements Cloud Manager logs |
| **AEM Admin Login**              | SSO entry into AEM author                                    | Admin, TA      | Quick jump from environment context into author UI for follow-up changes |

------

## 6. Learning Exercises for SHRSS Teams

You can run these as a **half-day enablement workshop**.

### Exercise 1 – Access & Environment Check

**Goal:** Confirm that roles and access are correct, and understand the environment header.

1. Log into **Cloud Manager** and open **Developer Console** for the **dev author** environment.
2. In the header, note:
   - Program ID
   - Environment ID
   - Pod name (e.g. `cm-pXXXXX-eYYYYYY-aem-author-<hash>`)
3. While the dev environment is restarting, observe:
   - Status banner (`starting`) and time to become `running`.

✅ **Success criteria:** Everyone can reach Developer Console without login errors and can identify the pod/environment they’re inspecting.

------

### Exercise 2 – Verify a Custom Bundle After Deployment

**Goal:** Learn to validate deployments from the runtime side, not just from pipeline status.

1. Trigger a **non-production Cloud Manager deployment** to the dev environment.
2. Once deployment is done:
   - Open Developer Console → **Status** tab.
   - Choose **Status Dump: Bundles**, **Output: TEXT** → **Get Status**.
3. Search the output for your project’s bundle name (e.g. `com.shrss.core`).
4. Check:
   - **State** should be `Active`.
   - Version corresponds to your latest build.

If the bundle is **not Active**, capture:

- The bundle’s state (e.g., `Installed`).
- Any related errors in logs (Developer Console logs or Cloud Manager aemerror.log).

This pattern is documented in internal conversations about using the console for bundle checks.
[Developer Console status dumps for bundles](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1588348664.063200)

------

### Exercise 3 – Inspect OSGi Configuration in the Cloud

**Goal:** Understand how to confirm which configuration values are really applied in CS.

1. In dev, open Developer Console → **Status** → `Configurations`.
2. Output as **TEXT** or **JSON**.
3. Locate:
   - A known custom configuration, e.g. logging PID for your project (`com.shrss.logging.*`) or a service endpoint PID.
4. Compare:
   - Values from **source control (config files)** vs. those shown in the dump.
5. Note any differences and link them back to:
   - Environment-specific OSGi config behavior in CS (e.g. using env vars) documented here:
     [Debugging OSGi configs & loggers in AEM CS](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1604438064.156900)

✅ **Success criteria:** Team knows where to look if “it works on SDK but not on Cloud.”

------

### Exercise 4 – Servlet Resolution Drill

**Goal:** Be able to debug “wrong servlet is responding” and `/bin/...` 404s.

1. Identify a known custom servlet (e.g. a simple `/bin/shrss-demo` endpoint).
2. In Developer Console → **Servlets**:
   - Search by:
     - **Path** (`/bin/shrss-demo`)
     - Or owning bundle/component.
3. Confirm:
   - Correct path
   - Selectors/extensions (if any)
4. Call the endpoint in a browser and observe:
   - Status code
   - Response body
5. Change something in code (e.g., update a response string), redeploy, and re-check.

✅ **Success criteria:** Everyone can trace a request to the correct servlet and confirm its mapping.

------

### Exercise 5 – Query & Index Inspection

**Goal:** Practice using the Queries tab to diagnose potential index issues.

1. Identify a **read-only JCR-SQL2 query** (no mutations) used by SHRSS.
2. In Developer Console → **Queries**:
   - Paste the query and execute it.
3. Observe:
   - Execution time
   - (If available) index / plan details
4. Compare:
   - Execution time vs. expectations from local SDK.
5. Document:
   - Whether index tuning might be needed and how you’d validate that via AEM CS documentation.

------

### Exercise 6 – Logs & Blocked Queue Simulation (read-only)

> Do *not* intentionally block a queue in production. Use a **dev environment** and read-only investigation.

1. In dev author, trigger some content activations.
2. Review:
   - **Content Distribution UI** for queue status.
   - **Developer Console logs** (or error logs via Cloud Manager) to find distribution-related messages.
3. Identify:
   - How a blocked queue would surface in logs.
   - Where stack traces would appear for customer-facing debugging.
     Internal note: errors are visible both in the Content Distribution UI and AEM logs exposed through Developer Console.
     [Blocked queue logs in Developer Console](https://adobe.enterprise.slack.com/archives/C01MSQMC16K/p1728895177.797039)

✅ **Success criteria:** Team knows how to correlate a blocked queue UI state with logs in Developer Console.

------

## 7. Common Troubleshooting Scenarios Using Developer Console

### Scenario A – Pipeline succeeded, but feature doesn’t work on Cloud

**Symptoms**

- Cloud Manager pipeline shows **green**.
- On AEM dev:
  - A feature is missing
  - Or errors appear where SDK worked fine.

**Steps in Developer Console**

1. **Bundles**
   - Status → `Bundles` → check custom project bundles:
     - Are they **Active**?
     - Are versions correct?
2. **Components**
   - Status → `Components`
   - Look for:
     - `unsatisfied` components
     - Missing service dependencies
3. **Configurations**
   - Status → `Configurations`
   - Verify environment-specific configs (e.g. endpoints, feature flags).
4. **Logs**
   - Use Developer Console logs or Cloud Manager `aemerror` log to find stack traces around startup or requests.

**Likely root causes**

- Missing config in CS (present locally).
- Different Java package versions / classloading issues (check **Java Packages** tab).
- Component unsatisfied due to a missing service or wrong PID.

------

### Scenario B – Job works on SDK but not in Cloud (Schedulers / Jobs)

**Context**

- Developers often use Sling jobs/scheduler in SDK.
- In AEM CS, sling job console is not exposed, but you can still:
  - Inspect components
  - Inspect configs
  - Rely on targeted logging.

**Steps**

1. **Configs**
   - Status → `Configurations`
   - Confirm scheduler/job PID exists and is enabled in CS.
2. **Components**
   - Status → `Components`
   - Verify the relevant scheduler/job component is active.
3. **Logs**
   - Add **DEBUG** logging to relevant packages instead of relying on root logger, per AEM best practices:
     [Targeted debug logging recommendation](https://adobe.enterprise.slack.com/archives/C0AQ7T6VD/p1721655726.074299)  
   - Remember: **TRACE is not supported in AEM CS; DEBUG is the max level**.
     [AEM CS logging – max DEBUG](https://adobe.enterprise.slack.com/archives/C0734RQAZRR/p1756377247.484209)

------

### Scenario C – 500 error on a specific endpoint after release

**Symptoms**

- 500s on e.g. `/bin/shrss-api/...` or a page with custom servlet.

**Steps**

1. **Servlet mapping**
   - Developer Console → **Servlets**
   - Confirm the endpoint path/selector/extension is mapped to the expected servlet.
2. **Bundles & Components**
   - Check if owning bundle is Active and component is satisfied.
3. **Logs**
   - Tail `aemerror` via Cloud Manager CLI or download logs.
   - Identify stack trace for that endpoint.
4. **Config check**
   - If error mentions missing config, verify via **Configurations** status dump.

------

### Scenario D – Content distribution queue blocked

**Symptoms**

- Authors see blocked queue in Content Distribution UI.
- Pages not appearing on publish.

**Steps**

1. **Logs via Developer Console**
   - Identify error entries for distribution handlers.
   - Confirm **which items** and **which queue** are impacted.
2. **Template for analysis**
   - Capture:
     - Error messages
     - Stack traces
     - Timestamps
   - These are the same logs customers can see; SRE note confirms they have access in Developer Console.
     [Blocked queue error visibility](https://adobe.enterprise.slack.com/archives/C01MSQMC16K/p1728895177.797039)
3. **Next actions**
   - Depending on root cause pattern, you may:
     - Advise configuration changes in code.
     - Instruct customer how to clear or unstick the queue, referencing official runbooks (outside this doc).

------

### Scenario E – Environment “Starting / Dehibernating” for too long

**Context**

- Sometimes customers see an environment stuck in “dehibernating/starting” in UI, while back-end indicates it’s actually healthy.

**Steps**

1. From Cloud Manager & Developer Console:
   - Confirm if the author/publish is actually responding.
2. If the environment is:
   - **Healthy from platform perspective but UI still shows “dehibernating”**:
     - This may indicate a Developer Console / environment status mismatch.
     - Internal guidance is to involve the appropriate AEM Developer Console / Skyline team.
       [Dehibernate state & Developer Console](https://adobe.enterprise.slack.com/archives/CCCG5K2JH/p1752575509.816329)

This scenario is more about identifying **where the problem is not**; Developer Console helps show if AEM itself is up.

------

## 8. Best Practices & Guardrails

1. **Least privilege access**
   - For most developers, grant:
     - Cloud Manager **Developer**
     - `AEM Users - author` for dev/RDE only.
   - Reserve `AEM Administrators` and deployment roles for TAs/admins.
2. **Use targeted loggers, not root DEBUG**
   - Follow guidance:
     - Create dedicated loggers at package level (e.g., `com.shrss.core`) instead of switching root (`error.log`) to DEBUG, which can grow huge and risk disk issues.
       [GraphQL logging example – “Always better to create a new logger”](https://adobe.enterprise.slack.com/archives/C0AQ7T6VD/p1721655726.074299)
3. **Remember CS logging limits**
   - **DEBUG is the max level**; TRACE is unsupported. Don’t attempt TRACE in CS.
     [Debug is maximal verbosity in AEM CS](https://adobe.enterprise.slack.com/archives/C0734RQAZRR/p1756377247.484209)
4. **Prefer RDE for rapid iteration**
   - Use **Rapid Development Environments (RDE)** to experiment and then promote code through standard Cloud Manager pipelines to dev/stage/prod.  
   - RDE guidance is available in internal RDE enablement docs.
     [RDE overview & use](https://fieldreadiness-adobe.highspot.com/items/67005626445664ae064fd1b6)
5. **Combine Developer Console with Cloud Manager logs**
   - Developer Console is **runtime introspection**.
   - For pipeline/build/startup issues, always also pull:
     - `aemerror`
     - `aemrequest`
     - dispatcher logs (via Cloud Manager or Splunk if applicable).
       [Build & deployment debugging with logs](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1603322959.276900)

------

## 9. Quick Checklist for SHRSS Admins

Use this as your “one-page” setup checklist:

1. **Admin Console**
   -  Confirm SHRSS admins are **System Admin** or **Product Admin** for AEM & Cloud Manager.
   -  Ensure Cloud Manager product profiles exist for **Developer**, **Deployment Manager**, **Program Manager**.
   -  Ensure AEM CS product profiles exist for `AEM Administrators - author` and `AEM Users - author/publish` for each SHRSS environment.
2. **Assign Personas**
   -  Map SHRSS admins to `AEM Administrators` and Cloud Manager `Program Manager` / `Deployment Manager`.
   -  Map TAs to Cloud Manager `Developer` or `Deployment Manager` + `AEM Administrators` on non-prod.
   -  Map developers to Cloud Manager `Developer` + `AEM Users - author` for dev/RDE.
3. **Validation**
   -  From a dev user account, open Cloud Manager → program → **Developer Console** for dev author.
   -  Confirm access without “Login failed” message.
   -  Run a **Bundles** status dump and find project bundle.
4. **Enablement**
   -  Run the exercises in Section 6 with your team (bundle check, config check, servlet drill, queries).
   -  Document any SHRSS-specific patterns (e.g., standard bundle names, critical scheduled jobs) in an internal Confluence/Wiki page.

------

### References

- **Developer Console overview & usage**
  - [How to use the Developer Console for Status Dumps in AEM](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1588348664.063200)
  - [AEM CS Developer Console – Status, Bundles, etc.](https://adobe.enterprise.slack.com/archives/CCCG5K2JH/p1747911978.032149)
  - [Debugging AEM as a Cloud Service – Developer Console (Experience League)](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console.html?lang=en#configurations)
- **Access & Admin Console**
  - [Mastering the Adobe Admin Console](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Delivery Support Resources/Competencies/CJM (AC, AJO, MKTO)/Practice Circle/Marketo/04. Deskside Coaching Activity Files/Admin Console/Mastering the Adobe Admin Console.pptx)
  - [Developer Console Access Troubleshooting](https://adobe.enterprise.slack.com/archives/C02JN4EJN/p1618985919.126000)
- **Design & Dev best practices (includes Dev Console URL & CLI)**
  - [AEM Cloud Service Design Best Practices – Developer Console](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Delivery Support Resources/Success Accelerators/Launch Advisory/Launch Advisory Delivery templates/AEM AWPs/MS3 Design/Launch Advisory AEM Cloud Services Design Best Practices.docx)
  - [AEM CS Development Guidelines](https://adobe.sharepoint.com/sites/FieldEngineeringOrg/Delivery Support Resources/Success Accelerators/Launch Advisory/Launch Advisory Delivery templates/z. Archived Templates/Launch Advisory Premier Support AWP Templates/ALL SOLUTIONS Deliverable Templates including KO, A&R, & Engagement Summary/Translations - Japanese/LFS V2 AEM Cloud Service Design Workshop Checklist Guide Best Practices JP.docx)
- **Logging, blocked queues, & limitations**
  - [Blocked queue logs visible in Developer Console](https://adobe.enterprise.slack.com/archives/C01MSQMC16K/p1728895177.797039)
  - [GraphQL debug logging – prefer custom loggers](https://adobe.enterprise.slack.com/archives/C0AQ7T6VD/p1721655726.074299)
  - [AEM CS logging – DEBUG as max level](https://adobe.enterprise.slack.com/archives/C0734RQAZRR/p1756377247.484209)
- **Cloud Manager logs & deployment debugging**
  - [Managing logs in AEM Cloud Service](https://adobe.enterprise.slack.com/archives/C0143J81A9E/p1621925532.055600)
  - [Cloud Manager deployment debugging tips](https://adobe.enterprise.slack.com/archives/C012DL53XPG/p1603322959.276900)

------