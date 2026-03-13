# SHRSS AEM Developer Console Training Deck Outline

### Slide 1 – Title

**Title:** SHRSS – AEM as a Cloud Service Developer Console
**Subtitle:** Access, Troubleshooting & Hands‑On Practice
**Audience:** Developers, Technical Architects, Admins
**Presenter:** <Your name / team>
**Version/Date:** <v1.0 – <date>>

------

### Slide 2 – Agenda

1. **Concepts & Terminology**
2. **Roles, Permissions & Admin Console Setup**
3. **How to Access AEM Developer Console**
4. **Tour of Developer Console Tools & Views**
5. **Troubleshooting Scenarios**
6. **Hands‑On Exercises for SHRSS**
7. **Next Steps & Recommended Practices**

------

### Slide 3 – What Is the AEM Developer Console?

- **Per‑environment diagnostic console** for AEM as a Cloud Service (Author/Publish/Preview).
- Provides **read‑only** introspection of:
  - OSGi bundles, components, configs, services.
  - Oak indexes, Sling jobs, servlets, queries.
  - Repository structure (via Repository Browser).
- **Replaces on‑prem `system/console` for debugging** in cloud environments.  
- **Not the same as Adobe Developer Console** (developer.adobe.com) which manages API credentials and App Builder projects.

*Source: [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)*

------

### Slide 4 – Where Developer Console Fits (SHRSS View)

- **Admin Console**
  - Manages users, product licenses, and product profiles.
  - Grants AEM access and Cloud Manager roles.
- **Cloud Manager**
  - Manages programs, environments, and pipelines.
  - Primary launch point for **AEM Developer Console**.
- **AEM Developer Console**
  - Per‑environment debugging and inspection.
  - Used during **incident response, performance tuning, and deployments**.
- **AEM Author/Publish**
  - Where authors and end‑users work.
  - Developer Console never modifies runtime directly; it inspects state.

------

## Section 1 – Roles, Permissions & Admin Console Setup

### Slide 5 – Key Concepts: IMS Org, Products & Profiles

- **IMS Org (Tenant)** – SHRSS’s organization in Adobe Identity Management (e.g., `…@AdobeOrg`).
- **Products**
  - *Adobe Experience Manager as a Cloud Service*
  - *Cloud Manager* (within AEM CS).
- **Product Profiles**
  - Define groups of permissions (e.g., *Developer – Cloud Service*, *AEM Users*, *AEM Administrators*).
- **Direct User Assignment vs Groups**
  - For some roles (e.g., Cloud Manager Developer), **users must be assigned directly** to the product profile; groups may not work reliably.

*Source: [Developer Console – IMS Architecture, Configuration and FAQ](https://wiki.corp.adobe.com/display/WEM/Developer+Console+-+IMS+Architecture%2C+Configuration+and+FAQ), [AEM API Integrations Developers](https://wiki.corp.adobe.com/display/WEM/AEM+API+Integrations+Developers)*

------

### Slide 6 – Personas & Required Access (Customer-Friendly)

| Persona            | Primary Tasks                             | Required Profiles (Typical)                                  |
| ------------------ | ----------------------------------------- | ------------------------------------------------------------ |
| **System Admin**   | Overall license & access management       | System Administrator (Admin Console), Cloud Manager Business Owner / Deployment Manager |
| **AEM Admin / TA** | Configure AEM, investigate prod issues    | AEM Administrators (Author for relevant envs), often Cloud Manager Developer – Cloud Service |
| **Developer**      | Debug code, inspect bundles/configs, APIs | Cloud Manager **Developer – Cloud Service**, AEM Users or Administrators on target environments |
| **Support / Ops**  | Triage incidents, collect status & dumps  | Same as AEM Admin, plus any internal Adobe roles as needed   |

*Note: Exact mapping for SHRSS can be tailored to their own role names.*

------

### Slide 7 – Access Requirements (Production vs Sandbox)

**For Production programs**

- To **log in** to AEM Developer Console:
  - Member of **Cloud Manager – Developer – Cloud Service** product profile
    *and*
  - Member of **AEM Users** or **AEM Administrators** product profile for the relevant AEM instance (author/publish).
- To **run status dumps & use Repository Browser**:
  - Cloud Manager Developer role is required across all programs.

**For Sandbox / non‑prod programs**

- Any AEM access product profile may allow basic login,
  but for full features (status dumps, repository browser), **treat the requirements as for production**.

*Source: [Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console), [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)*

------

### Slide 8 – Step‑by‑Step: Assigning a Developer/TA in Admin Console

**Goal:** Give an SHRSS developer access to AEM Developer Console for specific environments.

1. **Log into Admin Console**
   - Go to `https://adminconsole.adobe.com`.
   - Select the **SHRSS IMS Org** in the org switcher.
2. **Assign Cloud Manager Developer Role**
   - Navigate: **Products → Adobe Experience Manager as a Cloud Service → Cloud Manager** (product context name will include the tenant).
   - Open product profile **Developer – Cloud Service** (or equivalent).
   - On the **Users** tab, click **Add User** and add the developer **directly**.
3. **Assign AEM Product Profiles**
   - Still in Admin Console, under **Adobe Experience Manager as a Cloud Service**, locate the product profile for each relevant environment (e.g., `AEM Administrators – author – Program X – Environment Y`).
   - Add the developer to **AEM Users** or **AEM Administrators** for:
     - Dev Author (at minimum)
     - Stage/Prod Author as needed for troubleshooting.
4. **First Login to AEM**
   - Ask the user to log in once to the AEM environment (Author).
   - This syncs the IMS user/profile into AEM.
5. **Verify**
   - Optionally, in AEM Author: `Tools → Security → Users` to confirm the user/group is visible.

*Source: [Developer Console – IMS Architecture, Configuration and FAQ](https://wiki.corp.adobe.com/display/WEM/Developer+Console+-+IMS+Architecture%2C+Configuration+and+FAQ), [AEM Cloud Service, Admin Console, Developer Console and Business Platform](https://wiki.corp.adobe.com/display/WEM/AEM+Cloud+Service%2C+Admin+Console%2C+Developer+Console+and+Business+Platform)*

------

### Slide 9 – Common Setup Pitfalls (for Admins)

- Developer **added via user group only**, not directly to the product profile ⇒ login fails.
- Developer in Cloud Manager role but **not in AEM Users/Admins** ⇒ can see environments but **status dumps return 401**.
- User not yet logged into AEM ⇒ IMS user not synced; Dev Console gets 401 on AEM calls.
- Wrong IMS Org selected in the org switcher (multi‑org customers).
- Recently‑changed roles – allow a few minutes, then have the user log out/in again.

------

## Section 2 – Accessing the Developer Console

### Slide 10 – Access via Cloud Manager (Recommended Path)

1. Go to: `https://experience.adobe.com`.
2. Choose **Cloud Manager** for the SHRSS org.
3. Open the **Program** that contains the AEM environment.
4. Go to **Environments**.
5. On the desired environment (Dev/Stage/Prod):
   - Click the **⋯ (More)** menu.
   - Select **Developer Console**.
6. A new tab opens at the Developer Console login for that environment’s namespace.

*Source: [Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)*

------

### Slide 11 – Access via CLI (Optional for Power Users)

- Pre‑requisite: `@adobe/aio-cli` installed and configured.
- Command pattern:

```bash
aio cloudmanager:open-developer-console <ENVIRONMENT_ID> --programId <PROGRAM_ID>
```

- Opens the browser at the Developer Console URL for the given environment.
- Useful for automating environment‑switching during investigations.

*Source: [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)*

------

### Slide 12 – Login & Environment Selection

- Authentication uses **Adobe IMS** (same corporate login).
- After login, Dev Console typically shows:
  - The **namespace** (e.g. `ns-team-…`).
  - A list of **programs/environments** accessible to the user.
- For each environment, you can:
  - See status (Running / Hibernated / Starting).
  - Open **Author** or **Publish** status and tools.
- For hibernated dev envs:
  - Dev Console may allow **starting/de‑hibernating** the environment (depends on configuration).

------

### Slide 13 – Access Troubleshooting (For SHRSS Helpdesk)

Symptoms & checks:

- **“Login failed / Unable to login”**
  - Confirm user is in:
    - Cloud Manager **Developer – Cloud Service** profile.
    - AEM Users or Administrators for the environment.
  - Try incognito window to clear stale tokens.
- **Environment not listed**
  - User has Cloud Manager Developer role in org **A**, but environment is in org **B**.
  - Check org switcher & product profile org.
- **401 Unauthorized on status dumps**
  - User not in AEM Users/Admins for that AEM instance.
  - User has never logged into that AEM instance (no local user yet).

*Source: [Developer Console – IMS Architecture, Configuration and FAQ](https://wiki.corp.adobe.com/display/WEM/Developer+Console+-+IMS+Architecture%2C+Configuration+and+FAQ), [Developer console – troubleshooting section](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)*

------

## Section 3 – Tour of Developer Console Tools & Views

### Slide 14 – High‑Level Navigation

Typical (classic) Developer Console sections:

- **Status**
  - Status dumps for bundles, components, configs, indexes, jobs, etc.
- **Java Packages**
- **Servlets**
- **Queries**
- **Integrations**
- **Repository Browser**

New **Developer Console (Beta)** adds a more interactive UI but surfaces the same core capabilities.

*Source: [Rebuilding the Dev Console](https://wiki.corp.adobe.com/display/WEM/Rebuilding+the+Dev+Console), [AEM as a Cloud Service Developer Console (Beta)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-developer-console)*

------

### Slide 15 – Status Dumps (The Workhorse View)

From the **Status** tab, SHRSS can select:

- **Bundles**
  - List of OSGi bundles, versions, and states (Active/Resolved/Installed).
- **Components**
  - OSGi components and their satisfaction state (satisfied/unsatisfied).
- **OSGi Configurations**
  - Applied configurations (both product and custom).
- **OSGi Services**
  - Registered services and references.
- **Oak Indexes**
  - Index definitions and status (e.g., async progress).
- **Sling Jobs**
  - Queues and job counts (useful for stuck processing).

For each:

1. Select **Category** (e.g., Bundles).
2. Choose **Output Format**: Text or JSON.
3. Click **Get Status** to fetch a snapshot.

*Source: [AEM as a Cloud Service Development Guidelines – Dev Console section](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)*

------

### Slide 16 – Java Packages

- **Purpose:** Find which bundle provides a given Java package or class.
- Typical SHRSS use cases:
  - Resolving **“Class not found”** or **package import** issues.
  - Verifying which version of a library is active in a given environment.
- Workflow:
  1. Search by package name (e.g., `com.shrss.custom`).
  2. See which bundle exports the package.
  3. Cross‑check with `Bundles` status dump for version and state.

------

### Slide 17 – Servlets

- **Servlet Resolver view**:
  - Map **URL or resource type** to the actual servlet handling the request.
- Use cases:
  - SHRSS custom endpoints returning unexpected results.
  - Conflicts between multiple servlets for the same path/resource type.
- Typical steps:
  1. Input path or resource type.
  2. See matching servlet, script, and component.
  3. Adjust content structure, resource types, or Sling mappings accordingly.

------

### Slide 18 – Queries & Explain Query

- **Queries tab** integrates with AEM’s query performance tools.
- Capabilities:
  - Execute and measure **JCR‑SQL2 / QueryBuilder** style queries.
  - Retrieve execution time and result counts.
  - Link to **Explain Query** to see:
    - Which **index** is used.
    - Estimated vs actual cost.
- SHRSS scenarios:
  - Investigating slow searches.
  - Validating that a custom Oak index is being used.

*Source: [Debugging AEM as a Cloud Service with the Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)*

------

### Slide 19 – Integrations (Technical Accounts & APIs)

- Historically used to:
  - Create **technical accounts** (service credentials) for server‑side APIs.
  - Download JSON credentials used to obtain IMS access tokens.
- Today:
  - New OpenAPI‑based AEM APIs and OAuth S2S credentials are increasingly managed via **Adobe Developer Console**.
- SHRSS relevance:
  - For legacy or existing server‑side integrations, use Integrations view to:
    - Verify that a technical account exists.
    - Confirm it maps to the right AEM environment and has necessary permissions.

*Source: [AEM Cloud SDK – Developer Console](https://wiki.corp.adobe.com/display/WEM/AEM+Cloud+SDK+-+Developer+Console), [AEM on IO Developer Console – existing APIs](https://wiki.corp.adobe.com/display/WEM/AEM+on+IO+Developer+Console+-+existing+APIs)*

------

### Slide 20 – Repository Browser (Cloud‑Safe CRXDE Replacement)

- **Read‑only tree view** of the JCR repository for:
  - Author, Publish, and Preview tiers.
  - Dev, Stage, and Prod environments.
- Key features:
  - Navigate `/content`, `/conf`, `/var`, etc.
  - Inspect **node properties** and mixins.
  - View **effective ACLs** via Permissions tab (in newer builds).
- Why SHRSS should use it:
  - Safely inspect content/problem areas in Prod without write access.
  - Understand structure and permissions in a controlled way.

*Source: [AEM as a Cloud Service Development Guidelines – CRXDE Lite and Repository Browser](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines), [Permission UI | Developer Console | Repository Browser](https://wiki.corp.adobe.com/display/WEM/Permission+UI+|+Developer+Console+|+Repository+Browser)*

------

### Slide 21 – Logs & Other Tools (Context)

- Developer Console focuses on runtime **state**; logs are managed separately:
  - **Cloud Manager – Logs**
    - Download or tail `aemerror`, `aemrequest`, dispatcher/CDN logs.
  - **CLI log tailing**
    - `aio cloudmanager:tail-log …` for author/publish.
- Typical workflow:
  1. Use **Cloud Manager logs** to see stack traces and errors.
  2. Use **Developer Console** to verify bundles/configs/indexes/jobs for the same timestamp.
  3. Correlate findings.

*Source: [Logging for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/logging), [Debugging AEM as a Cloud Service using logs](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/logs)*

------

## Section 4 – Troubleshooting Scenarios for SHRSS

### Slide 22 – Scenario 1: 500 Errors on a Key SHRSS Page

**Context**

- SHRSS reports intermittent 500 errors on a critical page (e.g., `/content/shrss/en/apply.html`).

**How to use Developer Console**

1. **Reproduce & capture time**
   - Note exact time & environment (Dev/Stage/Prod).
2. **Check logs**
   - From Cloud Manager, download/tail `aemerror` around that time.
3. **Inspect bundles & components**
   - In Dev Console:
     - Run **Status → Bundles** – look for custom SHRSS bundles in non‑Active state.
     - Run **Status → Components** – filter for custom components showing unsatisfied references.
4. **Check OSGi configs**
   - Verify config for failing module exists and is correct (e.g., connection endpoints, credentials).

**Outcome**

- Often reveals missing OSGi configuration, incorrect service user mapping, or a bundle resolved but not active.

------

### Slide 23 – Scenario 2: Slow Queries / Timeouts on Search

**Context**

- SHRSS search or listing pages are slow; AEM shows high CPU and slow responses.

**How to use Developer Console**

1. **Capture slow query**
   - From logs or code, identify the JCR‑SQL2 or QueryBuilder query.
2. **Run in Queries tab**
   - Execute the query against Author/Publish in Dev Console.
   - Record execution time and result count.
3. **Use Explain Query**
   - From Dev Console, open Explain Query for the same statement.
   - Confirm:
     - Which **Oak index** is used.
     - If query is falling back to traversal (very expensive).
4. **Plan fix**
   - Create or adjust custom Oak index definition.
   - Re‑test via Queries + Explain Query.

**Outcome**

- Concrete evidence that an index is missing or mis‑configured, and a way to validate the improvement once deployed.

------

### Slide 24 – Scenario 3: Custom Component Not Working After Deployment

**Context**

- SHRSS team deploys new code; a custom OSGi service or Sling Model appears not to run.

**How to use Developer Console**

1. **Check bundles**
   - Status → Bundles:
     - Confirm the new bundle is present, version is correct, and state is **Active**.
2. **Check components**
   - Status → Components:
     - Look for the class or PID.
     - Is it **satisfied** or are references unsatisfied (e.g., missing service, config)?
3. **Check configs**
   - Status → OSGi Configurations:
     - Verify that required config (e.g., `com.shrss.core.impl.MyService`) exists and values look correct.
4. **Correlate with logs**
   - Look at `aemerror` for activation errors for that bundle/component.

**Outcome**

- Quickly determines whether the issue is deployment (bundle missing), configuration, or dependency related.

------

### Slide 25 – Scenario 4: Permissions Issue on a Content Path

**Context**

- A specific SHRSS user or group cannot access `/content/shrss/secure/*` despite being in “SHRSS‑Authors” group.

**How to use Repository Browser**

1. **Navigate to path**
   - Repository Browser → `/content/shrss/secure`.
2. **Open Permissions tab (if available in your build)**
   - See:
     - Explicit ACLs on the node.
     - Effective ACLs for a particular user or group.
3. **Compare against expectation**
   - Check whether the IMS group mapped from Admin Console is a member of a group that has sufficient privileges.
4. **Plan fix**
   - Adjust group → AEM group mapping or ACLs in lower environments and deploy.

**Outcome**

- Data‑driven conversation about permissions; no guessing.

------

### Slide 26 – Scenario 5: Server‑to‑Server Integration Fails (401 / 403)

**Context**

- A SHRSS backend service calls AEM APIs and receives 401/403 errors.

**How to use Developer Console**

1. **Check Integrations / Technical Account**
   - Confirm a technical account exists for the relevant environment.
2. **Check technical account permissions**
   - Ensure it is associated with the correct **product profile** in Admin Console (e.g., AEM Users/Admins for that environment).
3. **Verify repository presence**
   - Repository Browser:
     - Check if the technical account has required ACLs on the target content paths.
4. **Cross‑check logs**
   - `aemerror` for the 401/403 events; verify which principal is failing.

**Outcome**

- Confirms whether the issue is in IMS/permissions vs network/config.

------

## Section 5 – Hands‑On Exercises (For SHRSS Workshops)

### Slide 27 – Exercise 1: Getting Into Developer Console

**Objective:** SHRSS developers practice accessing Dev Console and verifying their permissions.

**Steps**

1. Log into **Admin Console** and review your own product profiles (demo only – guided by SHRSS admin).
2. From **Cloud Manager**, open the Dev environment’s **Developer Console**.
3. Verify you see:
   - Environment list.
   - Status tab, Java Packages, Servlets, Queries, Repository Browser.
4. Run a simple **Bundles** status dump:
   - Filter for a known product bundle (`com.adobe.granite…`) and a custom SHRSS bundle (if present).

**Debrief**

- Discuss what each persona should (and should not) see in Dev vs Stage vs Prod.

------

### Slide 28 – Exercise 2: Debugging a Broken Component

**Prerequisites**

- A small “broken” component prepared in SHRSS Dev (e.g., missing config or unsatisfied reference).

**Steps**

1. Open the SHRSS sample page that uses the broken component and confirm the error condition.
2. In Developer Console:
   - Run **Status → Components** and locate the component’s class/PID.
   - Confirm whether it is satisfied.
3. Check **Bundles** status for the component’s bundle.
4. Examine **OSGi Configurations** to spot missing/mis‑typed values.

**Goal**

- Participants identify the root cause and propose a configuration or code fix.

------

### Slide 29 – Exercise 3: Query Performance & Indexing

**Objective:** Show how to validate query performance and index usage.

**Steps**

1. Identify a simple but non‑trivial query (e.g., “all pages under `/content/shrss/en/news` tagged ‘press‑release’”).
2. In **Queries**:
   - Run the query and record execution time.
3. Use **Explain Query**:
   - Confirm which index is being used.
4. Optionally, demonstrate what happens when the query is written in a way that **forces traversal**.

**Goal**

- Participants learn to diagnose and prevent slow queries before they reach production.

------

### Slide 30 – Exercise 4: Using the Repository Browser Safely

**Objective:** Familiarize SHRSS with read‑only inspection of content and ACLs.

**Steps**

1. In Repository Browser:
   - Navigate to a representative content subtree (e.g., `/content/shrss/en`).
2. Inspect node properties for:
   - A page.
   - A component under `/content/shrss/en/.../jcr:content`.
3. If Permissions UI is enabled:
   - View effective ACLs for a test user/group at that node.

**Goal**

- Participants understand how to inspect live content structure without write access.

------

### Slide 31 – Exercise 5: End‑to‑End Incident Drill

**Objective:** Practice a full incident investigation using Dev Console.

**Scenario**

- Trainer or facilitator introduces a mock incident:
  - “On Dev, page X shows a 500 when loaded by anonymous users.”

**Steps**

1. Reproduce and capture time.
2. Download or tail `aemerror` via Cloud Manager.
3. Use Dev Console to:
   - Inspect relevant bundle/component/config.
   - Check repository structure at the problematic path.
   - Optionally simulate a query or permission check.

**Goal**

- Build confidence and muscle memory around the **Logs + Developer Console** workflow.

------

## Section 6 – Recommended Practices for SHRSS

### Slide 32 – Operational Do’s & Don’ts

**Do**

- Use **Dev** and/or **Sandbox** for hands‑on investigation; Stage/Prod only when needed.
- Keep **access minimal**:
  - Only those who need Dev Console on Prod should have it.
- Correlate:
  - Always correlate log timestamps with Dev Console status snapshots.

**Don’t**

- Treat Developer Console as a write‑time tool (no “quick fixes” in Prod).
- Rely solely on Dev Console for performance; always check logs and metrics as well.
- Use admin accounts casually in Stage/Prod; follow change‑management processes.

------

### Slide 33 – How SHRSS Should Roll This Out

- **Phase 1 – Enablement & Access**
  - Identify SHRSS personas (Admin, Dev, Ops).
  - Configure Admin Console & Cloud Manager profiles.
  - Run internal workshop using these slides + exercises.
- **Phase 2 – Integrate into Incident Playbooks**
  - Update SHRSS runbooks to explicitly call out:
    - “Open Dev Console → run Bundle/Component/Index status dump…”
  - Define when Stage/Prod Developer Console is allowed to be used.
- **Phase 3 – Continuous Improvement**
  - Collect examples where Dev Console helped resolve issues.
  - Refine queries, standard status dumps, and quick checks.
  - Track any gaps where additional observability is required.

------

### Slide 34 – References & Further Reading

**Public documentation**

- [Debugging AEM as a Cloud Service with the Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)  
- [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines)  
- [Logging for AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/logging)  
- [Debugging AEM as a Cloud Service using logs](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/logs)

**Internal (Adobe-only)**

- [Developer Console – IMS Architecture, Configuration and FAQ](https://wiki.corp.adobe.com/display/WEM/Developer+Console+-+IMS+Architecture%2C+Configuration+and+FAQ)  
- [Rebuilding the Dev Console](https://wiki.corp.adobe.com/display/WEM/Rebuilding+the+Dev+Console)  
- [AEM Cloud SDK – Developer Console](https://wiki.corp.adobe.com/display/WEM/AEM+Cloud+SDK+-+Developer+Console)  
- [Permission UI | Developer Console | Repository Browser](https://wiki.corp.adobe.com/display/WEM/Permission+UI+|+Developer+Console+|+Repository+Browser)

------

### Slide 35 – Q&A

- **Questions from SHRSS developers/admins**
- Capture follow‑ups:
  - Additional exercises needed?
  - Specific SHRSS scenarios to codify into runbooks?