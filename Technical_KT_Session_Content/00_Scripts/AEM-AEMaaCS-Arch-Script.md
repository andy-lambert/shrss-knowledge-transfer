### Slide 1 — Title & Session Framing

**Title:** AEM & AEM as a Cloud Service – Architecture Overview

**Script**

“Let’s start with a quick framing of this session.  

The goal for this first block is to align everyone on *how* AEM works under the hood and what actually changes with AEM as a Cloud Service.

I’ll walk through:

- The core AEM platform stack: JCR, Oak, Sling, OSGi, Granite.
- The classic author–publish–dispatcher model.
- How AEM as a Cloud Service re-platforms this into a Kubernetes-based, always-on service.
- Cloud services concepts: IMS orgs, Cloud Manager programs, environments, and entitlements.

This is deliberately high level but technical. The intent is to give developers, admins, and ops a mental model they can use throughout the rest of the KT.”

------

### Slide 2 — AEM Platform at 10,000 ft

**Title:** What is AEM?

**Script**

“Adobe Experience Manager is Adobe’s content platform for:

- **Sites** – web & headless experiences  
- **Assets** – DAM at enterprise scale  
- **Forms** – digital enrollment & document of record  
- **Screens** – digital signage

Underneath, it’s a **Java web application** built on three key open-source technologies:

- **Apache Jackrabbit Oak / JCR** – hierarchical content repository  
- **Apache Sling** – RESTful web framework mapping URLs to repository content  
- **Apache Felix / OSGi** – modular runtime and configuration system

On top of that, Adobe adds the **Granite platform** and **Coral UI** for the admin/authoring experience and a set of application features for Sites, Assets, and Forms.”  

(Reference: [AEM Architecture](https://wiki.corp.adobe.com/display/obujpn/AEM+Architecture), [AEM Technical Foundations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies))

------

### Slide 3 — Classic AEM Topology: Author, Publish, Dispatcher

**Title:** Classic AEM Deployment Model

**Script**

“Before we talk cloud, it’s useful to anchor on the classic AEM topology.

Traditionally you have:

- **Author tier** – where authors and admins log in, create content, manage assets, run workflows.
- **Publish tier** – read-only instances that serve live content to end users.
- **Dispatcher** – an Apache or IIS web server with the dispatcher module for caching and basic load balancing in front of publish.

Content flows:

1. Authors work in the **author** instance.  
2. When content is ready, it’s **replicated** to publish.  
3. The **dispatcher** caches responses and serves them as static HTML/JSON where possible.

This separation gives us security (author is not public), performance (dispatcher cache), and operational control.”  

(Reference: [WCMS Ops – AEM Overview](https://wiki.corp.adobe.com/pages/viewpage.action?pageId=2677803806))

------

### Slide 4 — AEM Core Stack: JCR & Oak

**Title:** JCR & Oak – The Content Repository

**Script**

“At the bottom of AEM is the **Java Content Repository (JCR)**, implemented by **Apache Jackrabbit Oak**.

Key ideas:

- Content is stored as a **tree of nodes and properties** – think of it like a hierarchical filesystem.  
- Paths like `/content/site/page` or `/content/dam/asset.jpg` are just JCR nodes.  
- The repository supports:
  - Versioning  
  - Access control  
  - Full-text and structured queries (SQL-2, XPath)  
  - Indexing for performance

In classic deployments, Oak can use:

- **TarMK / Segment store** – high-performance local segment files.  
- **Document store (MongoDB, RDB)** – for clustered authors.

AEM as a Cloud Service still uses Oak and JCR, but with a **cloud-optimized persistence setup** we’ll get to in a bit.”  

(Reference: [AEM Technical Foundations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies))

------

### Slide 5 — AEM Core Stack: OSGi & Felix

**Title:** OSGi & Apache Felix – Modular Java Runtime

**Script**

“The AEM runtime is an **OSGi container** implemented by **Apache Felix**.

Concepts you’ll keep running into:

- **Bundles** – versioned JARs with OSGi metadata. These are the deployment units.  
- **Components & services** – Java classes registered in the OSGi service registry.  
- **Configurations** – runtime configuration bound to components, typically managed through OSGi config files or the Web Console.

In practical terms, for developers and admins:

- AEM product features and your custom code are both deployed as **OSGi bundles**.  
- Most runtime settings are **OSGi configurations** – in AEMaaCS those are managed as code and deployed via Cloud Manager, not tweaked directly in production.”

(Reference: [AEM Introduction – OSGi](https://wiki.corp.adobe.com/display/AdobeDAM/AEM+Introduction), [AEM Technical Foundations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies))

------

### Slide 6 — AEM Core Stack: Sling & Resource Model

**Title:** Sling – URL to Content to Component

**Script**

“On top of the repository and OSGi, AEM uses **Apache Sling** as the web framework.

Sling has a few fundamental ideas:

- **Everything is a resource** – URLs are resolved to a resource in the JCR.  
- The resource has a `sling:resourceType` that points to a **component**.  
- Sling picks the appropriate **script** (HTL, JSP, or servlet) to render that resource.

For example:

- `/content/mysite/en/home.html` resolves to a page node.  
- That page’s components have `sling:resourceType` values like `mysite/components/teaser`.  
- Sling then runs the HTL script and Sling Model for that component to render HTML or JSON.

This resource-centric model is what makes AEM flexible for both **page-based** and **headless** use cases.”  

(Reference: [AEM Technical Foundations – Sling Request Processing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies))

------

### Slide 7 — Granite, Coral & AEM Applications

**Title:** Granite Platform & AEM Applications

**Script**

“On top of the open-source stack, Adobe provides the **Granite platform** – this is the shared foundation that all AEM solutions build on.

Granite includes:

- **Coral UI** and the touch-optimized authoring UI.  
- **Workflows**, launch and translation frameworks.  
- **Security, permissions, user/group management**.  
- **Operations tooling** – logging, health checks, maintenance tasks.

Then the product layers on:

- **Sites** – page editor, templates, Core Components, MSM, headless APIs.  
- **Assets** – DAM, metadata, renditions, Asset Compute integration.  
- **Forms / Screens** – built on the same core platform.

All of that architectural heritage is still there in AEM as a Cloud Service; cloud just changes how it’s deployed and operated.”  

(Reference: [AEM Architecture Stack – Intro video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/underlying-technology/introduction-architecture))

------

### Slide 8 — Why AEM as a Cloud Service?

**Title:** Why Move AEM to Cloud Service?

**Script**

“Now let’s pivot to AEM as a Cloud Service and what changes.

The design goals for AEMaaCS are:

- **Always on** – no planned downtime for upgrades or deployments.  
- **Always at scale** – automatic horizontal scaling up and down based on load.  
- **Always current** – continuous, low-friction product updates, rather than big-bang upgrades.  
- **Cloud-native operations** – CI/CD pipelines, immutable infrastructure, and strong isolation between customers.

For you as developers and admins, the key change is:

- You **don’t manage servers or clusters** anymore.  
- You **build code, configs, and content**; Adobe runs the platform on a Kubernetes-based infrastructure and handles patches, scaling, and failover.”

(Reference: [[Read This First\] AEM Cloud Service – Orientation Walk](https://wiki.corp.adobe.com/display/DMSArchitecture/[Read+This+First]+KT+-+AEM+Cloud+Service+-+An+orientation+walk))

------

### Slide 9 — AEMaaCS High-Level Architecture

**Title:** AEM as a Cloud Service – Logical Architecture

**Script**

“At a high level, each **AEM as a Cloud Service environment** still has the familiar tiers:

- **Author** – collaborative authoring, workflows, admin.  
- **Preview** – optional, private publish tier for pre-production review.  
- **Publish** – horizontally scaled tier for serving live traffic.

Around those tiers, there’s a set of managed services:

- A **Content Repository Service** – shared repository backing author and publish.  
- A **Replication / Distribution service** – pushes content changes from author into publish tiers.  
- A **CDN service** – Fastly-based, for global content delivery and security.  
- **Assets Compute** – cloud-native microservices for asset renditions and processing.  
- **Cloud Manager** – the CI/CD and environment management layer.  
- **IMS (Identity Management)** – user identity and SSO.

So the conceptual model is recognizable, but the implementation is fully cloud-native and multi-tenant.”  

(Reference: [AEM as a Cloud Service – Architecture Overview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture), [Security Overview](https://wiki.corp.adobe.com/display/aempresalesjp/Security+Overview))

------

### Slide 10 — AEMaaCS & Kubernetes: Runtime Model

**Title:** Containerized Runtime (Kubernetes)

**Script**

“Under the hood, AEMaaCS runs on Adobe’s container management platform built on **Kubernetes**.

A few important points for the technical audience:

- Each environment (dev, stage, prod, RDE) maps to **Kubernetes namespaces and pods** for author, publish, and supporting services.  
- The AEM application containers are **stateless** – session state is kept minimal and persistence is offloaded to shared services.  
- **Auto-scaling** is driven by metrics like CPU, memory and traffic; both author and publish can scale out and in without manual intervention.  
- Rolling updates are used for both **Adobe product releases** and **your code deployments**, maintaining availability.

You’ll rarely need to think in terms of pods and clusters day-to-day, but it’s useful to know that this is what enables the ‘always on, always at scale’ behavior.”  

(Reference: [AEMaaCS Training Doc – Architecture & Kubernetes](https://wiki.corp.adobe.com/display/AdobeDAM/AEMaaCS+Training+Doc), [Core Runtime](https://wiki.corp.adobe.com/display/WEM/Core+Runtime))

------

### Slide 11 — Persistence in AEMaaCS

**Title:** Persistence: Mongo, Segment Store & Blob Storage

**Script**

“Persistence is one of the biggest architectural differences in Cloud Service.

- **Author tier:**
  - Uses a **MongoDB-based document node store** for JCR nodes – good for clustering and high write throughput.  
  - Stores **binaries (assets, renditions, large files)** in a cloud **blob store** (Azure Blob or S3), shared with publish.
- **Publish tier:**
  - Each publish node has its own **segment store** (segment-based Oak store) for local read performance and resilience.  
  - There’s a **cloud segment store** plus the concept of a **‘Golden Master’** publish:
    - Golden Master writes to the shared store.  
    - Other publish nodes sync from that through the distribution service.
- **Content distribution:**
  - Content updates from author are turned into **events on a queue**; publish nodes subscribe and apply those changes incrementally.

The net effect is:

- Author is optimized for multi-user authoring and writes via Mongo.  
- Publish is optimized for fast reads and horizontal scale via local segment stores, while still staying in sync with author.”

(Reference: [AEMaaCS Training Doc – Persistence](https://wiki.corp.adobe.com/display/AdobeDAM/AEMaaCS+Training+Doc))

------

### Slide 12 — Assets Storage & Processing

**Title:** Assets Storage & Processing in the Cloud

**Script**

“For Assets specifically, there are two distinct concerns:

1. **Storage**
   - Asset binaries live in **cloud blob storage**.  
   - Both author and publish access the same underlying binaries, which is what enables high scale and options like multi-region publish.
2. **Processing**
   - Asset ingestion and rendition generation are offloaded to **Assets Compute Service** – a microservices-based processing pipeline.  
   - That allows AEM to autoscale asset processing independently from page delivery and keeps the core AEM nodes lighter.

From your perspective, the authoring UI and DAM folders feel like classic AEM, but storage and processing are backed by cloud-native services tuned for scale and cost.”  

(Reference: [AEMaaCS Training Doc – Assets](https://wiki.corp.adobe.com/display/AdobeDAM/AEMaaCS+Training+Doc), [Security Overview – Related Services](https://wiki.corp.adobe.com/display/aempresalesjp/Security+Overview))

------

### Slide 13 — Adobe Org, Programs & Environments

**Title:** Orgs, Programs, Environments & Entitlements

**Script**

“Now let’s talk about how AEMaaCS is carved up logically from a customer point of view.

- **IMS Organization (‘Org’)**  
  - This is your tenant in Adobe Identity Management.  
  - All users, product profiles, and licenses live under an Org.
- **Entitlements**  
  - The commercial SKUs you’ve purchased – e.g. Sites Ultimate, Assets Prime – are provisioned as **entitlements** on your Org.  
  - Those entitlements control what you can create in Cloud Manager: number and type of **programs**, **environments**, storage, content request limits, etc.
- **Cloud Manager Program**  
  - A **program** is a logical application: typically “Sites”, “Assets”, or a major initiative.  
  - Each program has its own Git repositories, pipelines, and environments.
- **Environments**  
  - Within a program you have environments: **prod**, **stage**, **dev**, plus optional **sandboxes** and **RDEs**.  
  - Each environment is a full stack: author, publish, dispatcher/CDN, and the backing services we discussed.

So the hierarchy is: **Org → entitlements → programs → environments**. That’s the mental model we’ll use in the rest of the KT.”  

(Reference: [AEM Organization Basics / Terminology](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/terminology), [AEM Romania – Org/Program/Environment Definitions](https://wiki.corp.adobe.com/display/aemro/AEM+Romania+Home), [CTAG – Admin Console, Cloud Manager & Developer Console](https://wiki.corp.adobe.com/pages/viewpage.action?pageId=2924790756))

------

### Slide 14 — Cloud Manager Paradigms

**Title:** Cloud Manager – Repos, Pipelines & Deployments

**Script**

“Everything you do in AEMaaCS from a dev/ops perspective flows through **Cloud Manager**.

Key concepts:

- **Repositories**
  - Git repositories owned by the customer or Cloud Manager that hold:
    - AEM project code (core, ui.apps, ui.content, ui.config, dispatcher, tests, etc.).  
    - Config as code (OSGi, dispatcher, CDN rules, ACLs if modeled, log forwarding config).
- **Pipelines**
  - Non-production pipelines – build, test and deploy to dev. Often used for feature branches and validation.  
  - Production pipelines – full build, quality gates, security & performance tests, then **blue‑green-style** rolling deploy to stage and prod.
- **Immutable environments**
  - You **do not** SSH into servers or install packages via Package Manager in prod.  
  - All code and configuration changes go through a pipeline, which:
    - Builds your code against the latest Adobe baseline image.  
    - Runs automated checks.  
    - Performs a zero-downtime rollout.

From today onward, when you think ‘change AEM’, think: ‘update code/config, push to Git, run Cloud Manager pipeline’.”  

(Reference: [Cloud Manager Overview – CTAG](https://wiki.corp.adobe.com/pages/viewpage.action?pageId=2924790756), [TSM KT: Adobe Cloud Manager](https://wiki.corp.adobe.com/display/PremierSupport/TSM+KT%3A++Adobe+Cloud+Manager))

------

### Slide 15 — What *Doesn’t* Change for You

**Title:** What Stays the Same for Developers & Admins

**Script**

“To close out, I want to highlight what **doesn’t** change when you move from classic AEM to Cloud Service:

- You still build on the **same core stack**: JCR/Oak, Sling, OSGi, Granite, HTL, Sling Models.  
- You still have the **author/publish mental model** and dispatcher/CDN in front of publish.  
- You still structure projects with the **AEM archetype**: `core`, `ui.apps`, `ui.content`, `dispatcher`, tests, etc.

What *does* change is:

- You no longer manage infrastructure – you manage **code, configuration, and content**.  
- You treat environments as **immutable**; all changes go through Cloud Manager.  
- You design solutions to be **stateless and cloud‑friendly** – no local file writes, no assumptions about single nodes, and so on.

That’s the foundation we’ll build on in the rest of these KT sessions as we get into the actual codebase, pipelines, and day‑to‑day operational practices.”

“Let’s pause here for questions on the architecture before we move into the development and pipeline details.”