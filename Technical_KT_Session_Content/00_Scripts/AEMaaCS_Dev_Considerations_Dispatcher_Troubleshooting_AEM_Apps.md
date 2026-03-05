### Section 1 — Development considerations for AEM as a Cloud Service (10–12 minutes)

**Slide intent:** Set guardrails for how to build and operate on AEMaaCS; highlight what’s *different* vs 6.5/AMS.

------

**Opening (30–60 seconds)**

- “In this section, I want to anchor on how AEMaaCS changes the way we design and implement code.
  Think of this as the ‘do and don’t’ list that should inform every design review and PR from this point on.”
- “You’ll see recurring themes: *cluster‑aware, stateless, immutable code base, mutable content only where allowed*.”

------

**1. Cluster‑aware code (2–3 minutes)**

- “First, assume the application is *always running in a cluster* of pods. There isn’t a single ‘primary’ we can safely cheat against.”
- “Pods are recreated and replaced continuously—during rolling deployments you can have old and new code running side‑by‑side against the same content.”  
- “Practically, this means:
  - No assumptions that ‘this instance’ is the only one running a job or workflow step.
  - Code must tolerate content written by previous code versions and vice versa.
  - Anything that depends on a ‘leader’ needs to use cluster primitives, like Sling Discovery, rather than hand‑rolled flags.”
- “Adobe’s development guidelines explicitly call out cluster awareness and resilience to pod recycling.”

*Key reference: **AEM as a Cloud Service Development Guidelines** – cluster‑aware code, state handling
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines*

------

**2. No state in memory, no state on local filesystem (3–4 minutes)**

- “Second, *do not* treat in‑memory or local filesystem state as durable.”
- “Pods are ephemeral. If a pod disappears, anything you stored in a static map, a cache, or `/tmp` that you care about is gone.”
- “Good patterns:
  - Persist important state to the repository (JCR) or a proper external system (database, search, queue).
  - Use short‑lived in‑memory caches only as *derivative* state you can recompute.
  - For ‘jobs’, rely on Sling Jobs or workflows designed to be resumable and idempotent.”
- “On filesystem usage:
  - Local disk is strictly for small, request‑scoped temporary files.
  - No writing business data or user‑generated content to local disk.
  - Anything you write to the filesystem must be considered disposable and bounded in size, otherwise you’ll impact quotas and risk failures.”

*Same reference as above – sections on **State in Memory** and **State on the Filesystem**.*

------

**3. Immutable code, mutable content (2 minutes)**

- “AEMaaCS enforces a clean separation:
  - `/apps` and `/libs` are *immutable* at runtime; you cannot ‘hot‑fix’ code on a live cloud environment.
  - All code and configuration changes are shipped via Cloud Manager pipelines as part of a versioned artifact.”
- “Mutable content includes:
  - Site content under `/content`.
  - Some ‘baseline’ project configuration/content under `/conf`, `/var`, certain `/content` subtrees.
  - Things you define via repo init (service users, ACLs, index definitions).”
- “If you’re used to logging into `/system/console` and editing configs, that’s a local SDK‑only behavior. In the cloud, that must come from `ui.config` and repo init, committed to Git and deployed.”

*Key reference: **Logging for AEM as a Cloud Service** and **Development Guidelines** both reinforce ‘all config from Git’.
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines*

------

**4. Idempotency & background work (2–3 minutes)**

- “Because multiple pods can pick up work, anything asynchronous must be **idempotent**:
  - Sling Jobs may be retried.
  - Workflows can be restarted or re‑executed after a failure.
  - Schedulers may run on multiple nodes, depending on configuration.”
- “Practical implications:
  - Design operations so ‘running them twice’ is safe: check for existing resources, use upserts, avoid blind appends.
  - Avoid ‘exactly‑once’ semantics unless you enforce them via persistent locks or external systems.
  - For heavy or long‑running work, push it into:
    - AEM processing microservices (e.g., Assets, if relevant),
    - queues,
    - or external worker systems, and keep AEM’s role orchestration‑heavy rather than CPU‑heavy.”

------

**5. Local SDK vs Cloud environments (1–2 minutes)**

- “Local AEM SDK is your ‘full‑access lab’:
  - You can write to `/apps` and `/libs`.
  - You have full OSGi web console and CRXDE Lite.
  - Use it to iterate quickly, but don’t build patterns that only work locally.”
- “Cloud environments:
  - No write access to `/apps`/`/libs`.
  - Developer Console + Repository Browser give a *read‑only* view of runtime state and repository.
  - All changes come from deployments and content operations, not manual tweaking.”

*Key reference: **Local Development Environment for AEM as a Cloud Service**
https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview*

------

**Close (30 seconds)**

- “So the key mental shift is: *assume multiple pods, assume they can vanish, assume code is immutable, and assume everything important must be persisted or externally managed.*
  If we design with those constraints in mind, our code will behave predictably in AEMaaCS.”

------

### Section 2 — Dispatcher/CDN (10–12 minutes)

**Slide intent:** Explain how Dispatcher + CDN work in AEMaaCS, and what patterns SHRSS devs must follow.

------

**Opening (30–45 seconds)**

- “Next, let’s look at the web tier: Dispatcher and CDN.
  This is where performance, cache behavior, and a big chunk of your security posture live.”
- “In AEMaaCS, Dispatcher is *part of your codebase* and tightly integrated into Cloud Manager deployments and validation.”

------

**1. Multi‑layer cache: CDN → Dispatcher → Publish (2–3 minutes)**

- “On publish, we have at least two caching layers:
  - Adobe‑managed CDN at the edge.
  - Dispatcher (Apache HTTPD + Dispatcher module) in front of Publish.”
- “Dispatcher:
  - Caches responses from AEM Publish to reduce load and response times.
  - Applies filters, rewrites, and access rules as a security layer.
- “CDN:
  - Uses standard HTTP caching headers: `Cache-Control`, `Surrogate-Control`, `Expires`.
  - Is controlled largely by what you configure in Dispatcher vhosts or in your application’s HTTP responses.”

*Key reference: **Caching in AEM as a Cloud Service**
https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/caching*

------

**2. Dispatcher configuration as code (2–3 minutes)**

- “Dispatcher configuration lives in your Git repo under the `dispatcher` module—this is deployable, versioned infrastructure‑as‑code.”
- “Key points:
  - Folder structure and file names matter (e.g., `conf.d`, `conf.dispatcher.d`, and specific `filters/filters.any` naming).
  - Configs are validated by the Dispatcher Tools SDK and by Cloud Manager:
    - Unsupported modules/directives or invalid syntax will break the build.
  - Immutable base config is provided by Adobe; we extend via allowed include files only.”
- “For SHRSS, any changes to:
  - **filters** (what paths are allowed/denied),
  - **cache rules**,
  - **vhosts** and headers must go through PR review and pass dispatcher validation locally before the pipeline.”

_Key references:  

- **Dispatcher in the Cloud** – structure, tools, validation
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/disp-overview  
- **Configuring Dispatcher when moving to AEM as a Cloud Service** – hands‑on patterns & validator
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/dispatcher_

------

**3. Filters & security (2–3 minutes)**

- “Dispatcher filter rules are our first line of defense:
  - Deny by default, then explicitly allow what’s required.
  - Block `/system/console`, `/crx/*`, `/bin/*` except whitelisted endpoints.
  - Block authoring URLs and internal APIs at the publish Dispatcher.”
- “When you introduce a new servlet or endpoint:
  - Think: ‘Do we ever want this callable from the public internet?’
  - If not, keep it on author only, or protect it behind auth, and do not open it in Dispatcher filters.
  - If yes, add the *minimal* allow rule with appropriate method and path restrictions.”
- “Security reviews should always include a quick pass over `filters.any` and vhost definitions.”

------

**4. Cache rules & TTLs (2–3 minutes)**

- “Caching is where we trade freshness for performance.
  - HTML, JSON, static assets: use cache headers to control lifetime.
  - Use `enableTTL` in Dispatcher when you want it to honor origin TTL headers and refresh automatically.”
- “For AEMaaCS:
  - CDN cache is driven by `Cache-Control` / `Surrogate-Control` / `Expires` headers.
  - Dispatcher cache is driven by its `cache` rules plus optional TTL behavior.”
- “Patterns:
  - Long TTL for stable assets (CSS/JS/images) with cache‑busting file names.
  - Reasonable TTL for pages and GraphQL persisted queries, combined with explicit invalidation when content changes.
  - Avoid caching responses that set cookies or are highly personalized for individual users.”
- “For GraphQL/headless, persisted queries are key for cacheable, GET‑based requests.”

_Key references:  

- **AEM Publish service caching** – CDN + Dispatcher behavior
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/publish  
- **How to enable CDN caching** – using vhost headers to control CDN
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/how-to/enable-caching_

------

**5. Local dispatcher tools and validation (1–2 minutes)**

- “Locally, you should use the Dispatcher Tools from the AEM SDK:
  - Run a Docker‑based dispatcher.
  - Use the dispatcher validator to ensure config is compatible before pushing.”
- “A broken Dispatcher config will fail your Cloud Manager pipeline, so catching issues locally saves time.”
- “For SHRSS, the expectation is:
  - Any Dispatcher change is validated locally.
  - Config is reviewed for both correctness *and* security before merge.”

_Key references:  

- **Local Development Environment for AEM as a Cloud Service** – Dispatcher runtime
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview  
- **Cloud 5 AEM Dispatcher Validator** – quick video walkthrough
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/expert-resources/cloud-5/cloud5-aem-dispatcher-validator_

------

**Close (30 seconds)**

- “The takeaway: treat Dispatcher and CDN as part of your application architecture, not just ‘a config somebody else maintains’.
  Every new feature should ship with its Dispatcher implications clearly thought through.”

------

### Section 3 — Troubleshooting AEM applications in the IDE (IntelliJ/Eclipse + Local SDK) (8–10 minutes)

**Slide intent:** Show how developers should debug locally with logs and remote debugging before jumping to cloud.

------

**Opening (30 seconds)**

- “Before we touch real cloud environments, most application issues should be reproduced and debugged locally using the AEM SDK plus your IDE—IntelliJ, Eclipse, VS Code, whatever you prefer.”
- “The flow is: reproduce locally → logs → debug / breakpoints → fix → commit → pipeline.”

------

**1. Local runtime + project wiring (1–2 minutes)**

- “We’ll assume:
  - You have the AEM SDK running locally (author and possibly publish).
  - Your SHRSS project is opened in IntelliJ/Eclipse and built with Maven.”
- “Local development environment is three pieces:
  - The AEM project (code/config/content).
  - Local AEM runtime (Quickstart JAR).
  - Local Dispatcher runtime (optional but recommended for web‑tier issues).”

*Key reference: **Local Development Environment for AEM as a Cloud Service**
https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview*

------

**2. Logs as the first line of debugging (2 minutes)**

- “Logs are still the primary source of truth:
  - Local AEM logs live under `crx-quickstart/logs`, typically `error.log` for Java logs.
  - Ensure your project’s Sling Logger configs route custom logs to `error.log` with appropriate log levels.”
- “Patterns:
  - Use `DEBUG` level in dev for your project packages; `WARN/ERROR` in higher environments.
  - Log enough context (IDs, paths, key parameters) to reconstruct what happened.”
- “In practice:
  - Tail `error.log` in a terminal, reproduce the issue in the browser, and watch for stack traces or WARN/ERROR lines from your code.”

*Key reference: **Debugging AEM SDK using logs**
https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/logs*

------

**3. Remote debugging from IntelliJ/Eclipse (3–4 minutes)**

- “For deeper issues, attach your IDE’s debugger to the local AEM JVM.”
- “General steps:
  1. Start AEM SDK with remote debug enabled (e.g., `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005`).
  2. In IntelliJ/Eclipse, create a ‘Remote’ run configuration pointing to `localhost:5005`.
  3. Set breakpoints in your Sling Models, servlets, or services.
  4. Trigger the behavior in the browser and step through the code.”
- “Use this for:
  - Understanding complex request flows or resolver logic.
  - Inspecting service references and configuration at runtime.
  - Verifying edge cases around nulls, concurrency, or conditional branches.”

*Key reference: **Debugging AEM SDK** – including remote debugging
https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/overview*

------

**4. OSGi web console & CRXDE Lite (1–2 minutes)**

- “Locally, you still have full access to:
  - `/system/console/bundles` – bundle states and exported/imported packages.
  - `/system/console/configMgr` – effective OSGi configs.
  - `/crx/de` – repository browser with read/write access.”
- “These are extremely helpful to:
  - Check if your bundle is installed/active, or missing dependencies.
  - Verify that `ui.config` and repo init are producing the expected configurations.
  - Inspect content and ACLs directly when debugging repository issues.”

*Key reference: **Debugging AEM SDK using the OSGi web console**
https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/osgi-web-consoles*

------

**Close (30 seconds)**

- “The goal is that most bugs are found and fixed locally with full tooling—logs, debugger, OSGi consoles—*before* they show up in dev/stage/prod.
  That keeps pipeline cycles and production troubleshooting to a minimum.”

------

### Section 4 — Troubleshooting with AEM as a Cloud Service Developer Console (8–10 minutes)

**Slide intent:** Show how to debug in cloud environments when an issue only happens on DEV/STAGE/PROD.

------

**Opening (30–45 seconds)**

- “Finally, let’s talk about debugging in the *actual* cloud environments using Developer Console.
  This is your read‑only window into what’s really running inside the pods for a specific environment.”

------

**1. Positioning Developer Console in the workflow (1–2 minutes)**

- “You use Developer Console when:
  - The issue cannot be reproduced locally.
  - The behavior depends on cloud‑only aspects: clustering, actual data volumes, dispatcher/CDN, or environment‑specific configs.”
- “It gives you:
  - Visibility into bundles, OSGi configs, services, Sling jobs, Oak indexes.
  - Status dumps and repository browser.
  - Integration tokens (local dev tokens, service credentials in some flows).”

_Key references:  

- **Debugging AEM as a Cloud Service**
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/overview  
- **Debugging AEM as a Cloud Service with the Developer Console**
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console_

------

**2. Accessing Developer Console (1 minute)**

- “To open it:
  1. Go to Cloud Manager → Program → Environments.
  2. For the environment, click the three dots (…) and choose *Developer Console*.
  3. Log in with your Adobe ID that has:
     - Cloud Manager Developer role, and
     - AEM Users/Admins product profile for that environment’s author/publish.”
- “You can switch between author/publish and different pods using the UI controls.”

------

**3. Typical debugging flows (4–5 minutes)**

- “Some common patterns you’ll use a lot:”

1. **Bundle/OSGi issues**
   - “If a feature isn’t working at all:
     - Check *Bundles*: is the project bundle active? Any imports unresolved?
     - Check *OSGi Configurations*: is the expected configuration present with the correct values?
   - If a bundle is ‘Installed’ rather than ‘Active’, it usually indicates a missing dependency version.”
2. **Servlet / request mapping issues**
   - “When a servlet or endpoint isn’t being hit:
     - Use the *Servlet resolution* / *Package resolution* tools to see which servlet is mapped to a path.
     - Confirm your resource type or path is actually resolved to your code.”
3. **Jobs, queues, background work**
   - “For background processing:
     - Use *Sling Jobs* or *Status dumps* to see job queues, failures, retry patterns.
     - This is crucial for long‑running or clustered workloads.”
4. **Repository inspection**
   - “Use the *Repository Browser*:
     - Read‑only view into `/content`, `/conf`, `/oak:index`, etc.
     - Helpful for verifying content structure or that repo init/ACLs applied correctly.
   - Remember: no writes here; fixes still need to come from code/content changes and deployments.”
5. **Status dumps**
   - “Status dumps provide a snapshot of critical subsystems:
     - Bundles, components, configs, indexes, Sling jobs.
   - They’re often what support asks you for when troubleshooting more complex issues.”

------

**4. Logs and Cloud Manager (1–2 minutes)**

- “Developer Console is complemented by logs in Cloud Manager:
  - For each environment, you can download `aemerror`, `aemaccess`, `aemrequest`, and dispatcher logs.
  - Use the pod IDs in the logs to correlate with what you see in Developer Console.”
- “Pattern:
  - Hit the issue in the environment.
  - Pull logs for the time window.
  - Use Developer Console to inspect runtime state (bundles/configs/indexes/jobs) for the same period.”

_Key references:  

- **Debugging AEM as a Cloud Service using logs**
  https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/logs  
- **Logging for AEM as a Cloud Service**
  https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/logging_

------

**Close (30 seconds)**

- “So the layered troubleshooting approach is:

  1. Reproduce and debug locally with IDE + SDK.
  2. If it only occurs in the cloud, move to Developer Console + Cloud Manager logs.
  3. Only if needed, escalate with status dumps and support.

  If we stick to that discipline, we keep cloud environments stable and still have enough observability to fix hard issues quickly.”