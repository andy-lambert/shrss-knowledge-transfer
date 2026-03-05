### Slide 1 — AEM & AEM as a Cloud Service – Architecture Overview

- Session goals
  - Recap AEM technical foundation
  - Explain AEM as a Cloud Service architecture
  - Align on org/program/environment concepts
- Audience: developers, sys admins, DevOps

------

### Slide 2 — What is AEM?

- AEM capabilities
  - Sites, Assets, Forms, Screens
- Built on:
  - Java web application
  - Apache Jackrabbit Oak (JCR)
  - Apache Sling (REST framework)
  - Apache Felix / OSGi (modular runtime)
- Adobe platform layer:
  - Granite, Coral UI, workflows, security

------

### Slide 3 — Classic AEM Deployment Model

- Author instance
  - Content creation, workflows, admin
- Publish instances
  - Read-only, public-facing content
- Dispatcher
  - Apache/IIS + dispatcher module
  - Caching and load balancing
- Content flow: Author → Replication → Publish → Dispatcher

------

### Slide 4 — JCR & Oak – The Content Repository

- Java Content Repository (JCR)
  - Nodes, properties, hierarchical tree
- Apache Jackrabbit Oak
  - Implementation of JCR
  - Support for TarMK / Segment store / Document store
- Features
  - Versioning, access control
  - Queries & indexing

------

### Slide 5 — OSGi & Apache Felix

- OSGi container
  - Apache Felix
- Concepts
  - Bundles (JARs with metadata)
  - Components & services
  - OSGi configurations
- Used for:
  - Product features and custom code
  - Runtime configuration

------

### Slide 6 — Sling – URL to Resource to Component

- Resource-centric model
- URL resolution into JCR resources
- `sling:resourceType` → component
- Scripts
  - HTL, JSP, servlets
- Works for page-based and headless APIs

------

### Slide 7 — Granite Platform & AEM Applications

- Granite platform:
  - Coral UI, authoring console
  - Workflows, launches, translation
  - Security & permissions
  - Ops tooling & maintenance
- Applications:
  - Sites, Assets, Forms, Screens
- Same platform basis in AEMaaCS

------

### Slide 8 — Why AEM as a Cloud Service?

- Goals
  - Always on (no planned downtime)
  - Always at scale (auto-scaling)
  - Always current (continuous updates)
  - Cloud-native operations
- Big shift:
  - Adobe operates infrastructure
  - Customer focuses on code, config, content

------

### Slide 9 — AEM as a Cloud Service – Logical Architecture

- Tiers per environment
  - Author
  - Preview
  - Publish
- Supporting services
  - Content Repository Service
  - Replication / distribution service
  - CDN (Fastly) for caching & security
  - Assets Compute, Document of Record
  - Cloud Manager, IMS

------

### Slide 10 — Containerized Runtime (Kubernetes)

- Adobe container management platform
  - Kubernetes-based
- Environments
  - Namespaces & pods per environment
- Characteristics
  - Stateless app containers
  - Auto-scaling author & publish
  - Rolling updates for Adobe + customer releases

------

### Slide 11 — Persistence in AEMaaCS

- Author tier
  - MongoDB-based document node store
  - Shared blob storage for binaries
- Publish tier
  - Local Oak segment stores per node
  - Shared cloud segment store
  - Golden Master publish model
- Content distribution
  - Event-based pipeline / queues

------

### Slide 12 — Assets Storage & Processing

- Storage
  - Binaries in cloud blob store (shared)
- Processing
  - Assets Compute Service for renditions
  - Scales independently of core AEM
- Net effect
  - Familiar DAM UI
  - Cloud-native scale & resilience

------

### Slide 13 — Orgs, Programs, Environments & Entitlements

- IMS Organization (Org)
  - Tenant in Adobe identity
  - Users, product profiles, licenses
- Entitlements
  - Purchased SKUs (Sites, Assets, etc.)
  - Capacity & environment limits
- Cloud Manager Program
  - Logical application (e.g. Sites, Assets)
  - Own repos, pipelines, environments
- Environments
  - Prod, Stage, Dev, Sandboxes, RDEs

------

### Slide 14 — Cloud Manager Paradigms

- Repositories
  - Full stack project structure (core, ui.apps, ui.content, ui.config, dispatcher, tests)
  - Config-as-code (OSGi, dispatcher, CDN, ACLs, logging)
- Pipelines
  - Non-prod pipelines
  - Production pipelines (dev → stage → prod)
  - Quality gates, security & performance tests
- Immutable environments
  - No direct changes in prod
  - All via pipeline

------

### Slide 15 — What Stays the Same

- Unchanged for developers/admins
  - JCR/Oak, Sling, OSGi, Granite, HTL
  - Author/publish model, dispatcher/CDN
  - AEM archetype & module structure
- What changes
  - Infra is fully managed by Adobe
  - All changes via Cloud Manager pipelines
  - Design for stateless, cloud-friendly patterns
- Lead-in to next KT sections
  - Codebase walkthrough
  - Pipelines & dev workflow

---

### References

- [AEM Architecture](https://wiki.corp.adobe.com/display/obujpn/AEM+Architecture)
- [AEM Technical Foundations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-technologies)
- [Architecture of AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/architecture)
- [Security Overview](https://wiki.corp.adobe.com/display/aempresalesjp/Security+Overview)
- [AEMaaCS Training Doc](https://wiki.corp.adobe.com/display/AdobeDAM/AEMaaCS+Training+Doc)
- [[Read This First\] KT – AEM Cloud Service – An orientation walk](https://wiki.corp.adobe.com/display/DMSArchitecture/[Read+This+First]+KT+-+AEM+Cloud+Service+-+An+orientation+walk)
- [AEM Organization Basics / Terminology](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/terminology)
- [Overview – Admin Console, Cloud Manager & Developer Console](https://wiki.corp.adobe.com/pages/viewpage.action?pageId=2924790756)
- [TSM KT: Adobe Cloud Manager](https://wiki.corp.adobe.com/display/PremierSupport/TSM+KT%3A++Adobe+Cloud+Manager)