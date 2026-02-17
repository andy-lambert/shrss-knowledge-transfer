# Tagging, Taxonomy & Metadata Governance — Proposed Session Content

**Purpose:** Proposed talking points and SHRSS-specific implementation details for the KT session agenda. Aligned to implementation analysis, content package review, and Adobe Experience League references.

**Authoritative references used:**
- [Taxonomy and tagging best practices for AEM Assets](https://experienceleague.adobe.com/en/perspectives/taxonomy-and-tagging-best-practices-for-aem-assets)
- [Tags, taxonomy, and metadata best practices: high-level summary (Site hierarchy)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/expert-advice/site-hierarchy)
- Implementation analysis: `/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`
- Content package: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`

---

## 1. Tag Taxonomy

### 1.1 How taxonomy was configured for this implementation

- **Taxonomy root:** Tags are stored under the standard AEM taxonomy root. The content package filter includes `/content/cq:tags/shrss`, indicating a **shrss** namespace for SHRSS-specific tags.
- **Path-to-tag mapping (site/content context):** The implementation uses **TagsPathMappingConfigService**, which reads a path-to-tag mapping from an **ACS Commons Generic List** at `/etc/acs-commons/lists/path-tags-mapping/jcr:content/list`. Each list item has:
  - **jcr:title** = content path (e.g. site or section path)
  - **value** = tag ID (e.g. a tag under the taxonomy)
  - This allows the system to **derive tags from the current page path** (e.g. for alerts or context-specific content) without authors selecting tags manually on every page.
- **Content Fragments and assets:** Content Fragments and DAM assets store tag references in metadata. For CFs, the **categories** field (multi-value) holds tag IDs used for filtering in dynamic lists. DAM assets use the standard **cq:tags** property on `jcr:content/metadata` (with `cq:Taggable` mixin). Sample content shows tags such as `properties:orientation/square` and namespaced tags like `shrss:regions/latam`, `shrss:event-categories/entertainment`.
- **Tag namespaces in use (from code and test data):** `shrss` (e.g. `shrss:regions/apac`, `shrss:event-categories/entertainment`, `shrss:hotel/new-york`), and standard OOTB namespaces such as `properties` (e.g. `properties:orientation/portrait`).

### 1.2 How tags are structured across Brand / LOB / Property

- **Namespace as top level:** Under `/content/cq:tags/shrss`, tags can be organized by brand, LOB, or property using **child tag hierarchies** (e.g. regions, event-categories, hotel/property names).
- **Observed structure (from implementation and test data):**
  - **Region/destination:** e.g. `shrss:regions/latam`, `shrss:regions/apac`
  - **Event/content type:** e.g. `shrss:event-categories/entertainment`
  - **Property/venue:** e.g. `shrss:hotel/new-york`
- **Path–tag mapping:** The ACS Commons list maps **site/section paths** to **tags**, so a given brand or property section can be associated with one or more tags for automatic context (e.g. which alerts or content to show). This supports “tags by brand/LOB/property” without duplicating taxonomy; the same tag taxonomy is reused and mapped per path.

### 1.3 Best practices and taxonomy strategy

- **Sites (hierarchy and governance):** Use folder structure and permissions to control who can access which areas; use tags for **structural metadata** (categorization, related content, navigation). Prefer a **defined taxonomy** over ad-hoc tags to keep search and filtering predictable. See [Site hierarchy, taxonomy, and tagging guide](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/expert-advice/site-hierarchy).
- **Assets:** Use a **hierarchical taxonomy** (namespaces → tags → sub-tags) so authors can select from consistent keywords; this improves findability and faceted search. Make taxonomy **additive to** (not duplicative of) folder structure and metadata. Consider **Smart Tags** to reduce manual tagging. Govern who can create/edit tags via permissions. See [Taxonomy and tagging best practices for AEM Assets](https://experienceleague.adobe.com/en/perspectives/taxonomy-and-tagging-best-practices-for-aem-assets).
- **SHRSS-specific:** Keep path–tag mapping in the ACS Commons list documented and maintained when site structure or brands change. Use the **shrss** namespace for all SHRSS-specific taxonomy; use standard namespaces (e.g. **properties**) only where they add value (e.g. orientation, format).

---

## 2. Tag Management

### 2.1 Governance — Rules for tag governance (who creates, who maintains, who approves)

- **Recommended model (align to your organization):**
  - **Create:** Limit tag creation to a small group (e.g. admins or a “taxonomy steward”) so the hierarchy stays consistent.
  - **Maintain:** Designate owners per namespace or domain (e.g. regions, event-categories); they review and prune unused or duplicate tags.
  - **Approve:** For sensitive or brand-critical namespaces, require approval before new tags go live (process outside AEM or via workflow if needed).
- **AEM mechanics:** Use **permissions on the tag tree** (`/content/cq:tags`) to restrict create/update/delete by group. Restrict the **path–tag mapping list** (`/etc/acs-commons/lists/path-tags-mapping`) to admins so only authorized users change which paths map to which tags.
- **Documentation:** Keep a short governance doc: who can create/edit tags, who maintains the path–tag list, how to request new tags or mappings, and where the taxonomy is documented (e.g. Tagging console, spreadsheet, or wiki).

### 2.2 Creating, updating, deleting tags

- **Creating:** Tagging console → select parent namespace or tag → Create Tag. Provide **Title** (and optional **Name**, **Description**). For SHRSS, create under `/content/cq:tags/shrss` or the appropriate sub-hierarchy.
- **Updating:** Tagging console → select tag → Edit. Change Title/Name/Description. Moving tags (Move) can break references; plan and communicate.
- **Deleting:** Tagging console → select tag → Delete. Container tags may require children to be moved or deleted first. **References** should be reviewed before delete so content is retagged if needed.
- **Publishing:** Tags must be **published** to be available on publish; use Publish/Unpublish from the Tagging console. Path–tag mapping content (ACS Commons list) must also be published if author and publish use it.

### 2.3 Best practices

- **Standardize:** Use a single vocabulary/glossary; avoid synonyms as separate tags unless using thesaurus features.
- **Avoid over-tagging:** Too many tags per asset/page dilutes value; define guidelines (e.g. max tags per content type).
- **Re-evaluate:** Periodically audit tag usage and merge or retire unused tags.
- **Path–tag list:** Treat the ACS Commons path–tag list as governed configuration; change only with approval and document each path–tag pair for troubleshooting.

---

## 3. Application of Tags in SHRSS Authoring & Asset Management

### 3.1 Component and asset metadata mapping

- **Assets (DAM):** Metadata schema is defined at `conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`. The **Tags** field is typically bound to `jcr:content/metadata/cq:tags`. Authors pick tags from the taxonomy when editing asset metadata; tags are stored as string array on the asset.
- **Content Fragments:** CF models (e.g. News, Events) include a **categories** (or similar) field that stores tag IDs. This is used by **CF Card List** and related components to filter by tags. Map this field in the CF model to the same taxonomy used in the Tagging console.
- **Pages:** Page properties can expose **Tags/Keywords** (cq:tags) for SEO and for components that use page context (e.g. Alert Aggregator uses path–tag mapping derived from current page path).
- **Path–tag mapping:** Not a component field; it is authoring-time configuration in the ACS Commons list. It maps **paths** (e.g. `/content/shrss/hotel/en/...`) to **tag IDs** used by backend services (e.g. **TagsPathMappingConfigService.getAllTagsByPath(currentPage.getPath())**).

### 3.2 How tags impact dynamic content queries

- **CF Card List (listType = tags):** When authors choose **List by tags**, they configure **tagsList** (tag IDs) and **tagsRootFolder** (e.g. `/content/dam/shrss`). The backend builds a Query Builder map that:
  - Restricts to DAM assets that are Content Fragments under the root folder.
  - Filters by **content fragment model** (e.g. Event, News).
  - Adds **group property** conditions on the **categories** property matching each tag in **tagsList** (OR logic between tags).  
  So only CFs whose **categories** metadata contains at least one of the selected tags appear in the list.
- **Path-derived tags:** **Alert Aggregator** uses **TagsPathMappingConfigService.getAllTagsByPath(currentPage.getPath())** to get tags for the current page path, then uses those tags to decide which alerts to show. So **path–tag mapping** directly drives which content appears on a given page/section.

### 3.3 Category filters

- **CF Card List:** The same **tagsList** used for the list query can be exposed as category filters in the UI (e.g. news search result filters by category/tag). Tag titles are resolved via **TagUtils.getTagNameTitleMapByTagNames** / **TagManager** for display.
- **Asset search:** In Assets, the Tags predicate in search (e.g. Search Rail) can be configured with a **root tags path** (e.g. `/content/cq:tags/shrss`) so authors filter by the SHRSS taxonomy.

### 3.4 Search results

- **Assets:** Tags are indexed with asset metadata; search on `jcr:content/metadata/cq:tags` (or equivalent) returns assets that have the given tag(s). Match-all vs match-any is configurable in the Tags predicate.
- **Content Fragments:** The **categories** field is part of CF metadata and is queryable; tag-based CF lists and search use this for filtering.
- **Pages:** If page properties store cq:tags, those can be used in page search and for SEO (meta keywords).

### 3.5 Content inheritance across sites

- **No JCR inheritance of tags:** Tags are not inherited from parent pages by default; each page/asset holds its own tag references.
- **Path–tag mapping as “inheritance”:** The path–tag list effectively encodes “sections of the site and their tag context.” When a page’s path is under a mapped path, **getAllTagsByPath** returns the tags for that path (and any parent path that has a mapping). So “inheritance” of tag context is via **path prefix matching** in the mapping list, not via JCR hierarchy.

### 3.6 Card and page visibility

- **Cards (CF Card List):** Visibility is driven by **tagsList** and **tagsRootFolder** plus CF model type. Only CFs with matching **categories** (tags) under the root folder appear. Wrong or missing tags on CFs, or wrong tagsList/tagsRootFolder on the component, will hide cards.
- **Page visibility:** For components that use **path–tag mapping** (e.g. Alert Aggregator), visibility depends on the current page path having a mapping and the mapped tags matching the content (e.g. alert tags). Missing or incorrect path–tag entries will cause content not to appear on that section.

---

## 4. Additional Topics (brief)

- **Tag performance (query efficiency, indexing):** Tag properties are indexed when standard AEM/Oak indexing is used. Queries that filter by `cq:tags` or CF **categories** should use indexed properties; avoid large OR sets of tags in a single query when possible. Path–tag mapping is a small list read once per request; keep the list size reasonable.
- **Troubleshooting content not appearing in listings/filters:** (1) Confirm the CF or asset has the expected tags in **categories** or **cq:tags**. (2) Confirm component config: **tagsList**, **tagsRootFolder**, and list type (e.g. tags vs fixed list vs root path). (3) For path-driven content (e.g. alerts), confirm path–tag mapping exists for the page path and is published. (4) Confirm tags are published. (5) Check Query Builder or service logs if queries return no results.
- **Scheduling or lifecycle states:** Tags themselves do not change with scheduling; they are static metadata. If “visibility” is time-based, that is usually implemented via **publish date / end date** on the CF or page, or via workflow state, not via tag changes. Tags can still be used **together** with date filters (e.g. Event CF list filtered by tag and by event date range).

---

## Document control

- **Version:** 1.0 (draft for KT session)
- **Source:** Implementation analysis, content package review, Adobe Experience League references above.
