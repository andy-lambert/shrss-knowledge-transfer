### Session: Search & Indexing in AEM as a Cloud Service

**Audience:** AEM developers, architects, sys admins
**Duration:** 15–25 minutes (core content ~18 minutes + 5–7 minutes Q&A/demo)

------

## 1. Session goals (1–2 minutes)

*By the end of this session, you should:*

- Understand **how AEMaaCS indexing works** and how it differs from AEM 6.x.
- Know **how to safely customize OOTB Lucene indexes** like `damAssetLucene-*`.
- Be able to **define fully custom Lucene indexes** for project‑specific queries.
- Recognize **best practices, anti‑patterns, and gotchas** that affect performance and Cloud Manager.
- Know the key **index configuration options** and when to use them.

**Speaker notes (short talk track):**

> In this block we’re going to focus on how search and indexing work in AEM as a Cloud Service, and what that means for your project.  
>
> We’ll look at how to customize OOTB indexes such as `damAssetLucene`, how to create new custom Lucene indexes, and what you need to avoid so you don’t hurt performance or break Cloud Manager pipelines.  
>
> I’ll keep this practical and tie it back to common query patterns you actually have in the application.

------

## 2. AEMaaCS indexing fundamentals (3–5 minutes)

### 2.1 What changed vs AEM 6.x

**Key points:**

- **Only Lucene indexes** are supported for customer-managed indexes.
  - Index type must be `lucene` and `compatVersion={Long}2`.
- **No Index Manager UI** in cloud:
  - No `/libs/granite/operations/content/diagnosistools/indexManager.html` on AEMaaCS.
  - Indexes are **managed as code** and deployed via **Cloud Manager pipelines**.
- **Rolling / blue‑green deployments**:
  - New code → new index version is created → reindex happens → traffic switches to new image.
  - Two sets of indexes can exist during a deployment.
- Indexes live under `/oak:index` in the repo, but in AEMaaCS they are **owned by the code package**, not mutable content.

**Speaker notes:**

> In AEMaaCS, indexing is part of your deployment story. You don’t tweak indexes on a single instance and hit “reindex” anymore.  
>
> All custom or customized indexes are Lucene, compat version 2, and they live under `/oak:index`. You ship index definitions with your code, and Cloud Manager handles deploying them, waiting for reindexing, and only then flipping traffic to the new version.  
>
> There’s no Index Manager UI in Cloud Service; instead, we rely on code, pipelines, and the Developer Console for diagnostics.

**References:**

- [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [AEM Project Structure](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure)  
- [Missing Index Manager on AEMaaCS](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-23195)

------

## 3. Customizing OOTB indexes (focusing on `damAssetLucene`) (5–8 minutes)

### 3.1 Index categories & naming

**Three categories:**

1. **OOTB index** – shipped by Adobe, e.g.:
   - `/oak:index/damAssetLucene-10`
   - `/oak:index/cqPageLucene-2`
2. **Customization of OOTB index**
   - Copy OOTB definition, add your properties.
   - Name pattern:  
     - `damAssetLucene-10-custom-1` (or `-custom-2`, etc.)
3. **Fully custom index**
   - Not based on product index; add a **prefix** to avoid collisions:  
   - `/oak:index/acme.product-1-custom-1`

**Important rule for Assets:**

- Do **not** create separate fulltext indexes on `dam:Asset` under `/oak:index/*` if you can avoid it.
- Recommended: **customize the existing `damAssetLucene-\*`** index instead.

**Speaker notes:**

> You’ll see index nodes under `/oak:index` like `damAssetLucene-10` or `cqPageLucene-2`. Those are product indexes.  
>
> If you need additional metadata on assets to be searchable, don’t create your own parallel “assets index” – instead, copy the current `damAssetLucene-*` version, rename it to `damAssetLucene-<productVersion>-custom-1`, and apply your changes there.  
>
> This avoids conflicts with product features and ensures future upgrades can merge your customizations.

**References:**

- [Content Search and Indexing – Index Names and Customization](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [Generic Lucene Index Removal](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/removal-generic-lucene-index)

### 3.2 Practical: customizing `damAssetLucene` (step‑by‑step)

**Scenario:** You need a custom asset metadata property (e.g. `myapp:category`) to be full‑text searchable and filterable.

**Process:**

1. **Discover current version of the index** on a Cloud Service environment:

   - Use CRX Package Manager (`/crx/packmgr`) to download a package containing `/oak:index/damAssetLucene-*`.
   - Identify the latest version, e.g. `damAssetLucene-11`.

2. **Copy and rename in your codebase**:

   - In `ui.apps/src/main/content/jcr_root/_oak_index/` create:
     - `damAssetLucene-11-custom-1/.content.xml`
   - Paste the OOTB definition as a starting point.

3. **Ensure Cloud Service‑compatible properties**:

   - At the root of the index definition:
     - `jcr:primaryType="oak:QueryIndexDefinition"`
     - `type="lucene"`
     - `compatVersion="{Long}2"`
     - `async="[async,nrt]"` or `async="[async]"` / `"[fulltext-async]"` as appropriate.
   - Preserve the `tika` node that exists in cloud but not local SDK.

4. **Add your property under `indexRules`** for `dam:Asset`:

   *Example snippet (inside `<indexRules><dam:Asset><properties>`):*

   ```xml
   <myCategory
       jcr:primaryType="nt:unstructured"
       name="jcr:content/metadata/myapp:category"
       nodeScopeIndex="{Boolean}true"
       propertyIndex="{Boolean}true"
       analyzed="{Boolean}true"/>
   ```

   - `propertyIndex=true` – property can be used for equality/ordering.
   - `nodeScopeIndex=true` – include in fulltext search.
   - `analyzed=true` – tokens, lowercasing, etc.

5. **Deploy via Cloud Manager**:

   - Commit the `ui.apps` change.
   - Run a non‑prod pipeline; Cloud Manager:
     - Deploys code and new index definition.
     - Waits for reindexing to complete.
     - Then promotes the new version.

6. **Verify usage**:

   - Use Explain Query (`/libs/granite/operations/content/diagnosistools/queryPerformance.html`) on SDK.
   - In Cloud, use Developer Console “Oak Indexes” status dump and logs to ensure `damAssetLucene-11-custom-1` is used.

**Speaker notes:**

> The key pattern for customizing `damAssetLucene` is: copy from Cloud → rename to `-custom-1` → add properties under `indexRules/dam:Asset/properties` → deploy via Cloud Manager.  
>
> Always start from the current product definition in Cloud, not the SDK, because Cloud will include extra configuration such as `tika` that the SDK doesn’t have.  
>
> Once deployed, use Explain Query and the Developer Console to confirm your custom index version is actually being used.

**References:**

- [Content Search and Indexing – Preparing the New Index Definition](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)  
- [Lucene Index – Index Definition](https://jackrabbit.apache.org/oak/docs/query/lucene.html)

------

## 4. Creating fully custom indexes (4–6 minutes)

### 4.1 When do you really need a custom index?

**Use a fully custom index when:**

- You have **custom node types** or specific paths (e.g. `/content/myapp/jobs`) that:
  - Are not efficiently served by any OOTB index (`cqPageLucene`, `damAssetLucene`, etc.).
  - Require special ordering, facets, or function‑based indexing.
- You want to **restrict indexing** to a small subtree for performance:
  - E.g. a big DAM where OOTB `damAssetLucene` is too broad, and you need a specialized sub‑root index.

**Before creating one:**

- Use **Query Performance / Explain Query** to see:
  - Which index is used today.
  - Whether configuring `cqPageLucene` or `damAssetLucene` would be sufficient.

**References:**

- [Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)  
- [Search and indexing in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/search-and-indexing)

### 4.2 Example: fully custom index definition (Lucene)

*Example use case*: custom node type `acme:Job` under `/content/acme/jobs`, with queries:

- Filter: `WHERE [acme:jobType] = 'full-time'`
- Sort by `@acme:postedDate` descending.

**Index definition (simplified):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jcr:root
    xmlns:jcr="http://www.jcp.org/jcr/1.0"
    xmlns:nt="http://www.jcp.org/jcr/nt/1.0"
    xmlns:acme="http://www.acme.com/jcr/acme/1.0"
    jcr:primaryType="oak:QueryIndexDefinition"
    type="lucene"
    compatVersion="{Long}2"
    async="[async]"
    evaluatePathRestrictions="{Boolean}true"
    includedPaths="[/content/acme/jobs]"
    queryPaths="[/content/acme/jobs]">

    <indexRules jcr:primaryType="nt:unstructured">
        <acme:Job jcr:primaryType="nt:unstructured">
            <properties jcr:primaryType="nt:unstructured">
                <jobType
                    jcr:primaryType="nt:unstructured"
                    name="acme:jobType"
                    propertyIndex="{Boolean}true"/>
                <postedDate
                    jcr:primaryType="nt:unstructured"
                    name="acme:postedDate"
                    propertyIndex="{Boolean}true"
                    ordered="{Boolean}true"
                    type="Date"/>
            </properties>
        </acme:Job>
    </indexRules>
</jcr:root>
```

**Key configuration choices:**

- `includedPaths` / `queryPaths`:
  - Restricts the index to `/content/acme/jobs` – keeps it small and cheap.
- `evaluatePathRestrictions=true`:
  - Query path restrictions are handled in the index instead of post‑filtering.
- `propertyIndex=true`:
  - Efficient property filter + sorting.
- `ordered=true` on `postedDate`:
  - Enables efficient `ORDER BY acme:postedDate`.

**Speaker notes:**

> For custom node types or very specific paths, it can be more efficient to create your own Lucene index.  
>
> The pattern is similar: create an index definition under `_oak_index`, choose a unique prefix and name, set `type=lucene`, `compatVersion=2`, and then define `indexRules` for your node types.  
>
> Be very deliberate about `includedPaths` and `queryPaths` so you’re not indexing the entire repository for a query that only ever touches `/content/acme/jobs` or a similar subtree.

**References:**

- [Lucene Index – Canonical Definition & Index Rules](https://jackrabbit.apache.org/oak/docs/query/lucene.html)  
- [Indexing – Customizing OOTB and Fully Custom Indexes](https://jackrabbit.apache.org/oak/docs/query/indexing.html)

------

## 5. Best practices, anti‑patterns, and gotchas (5–7 minutes)

### 5.1 Best practices

**Core best practices (Cloud-friendly):**

- **Start from queries, not from indexes**:
  - Use Explain Query and Query Performance Tool on SDK.
  - Verify whether an OOTB index already serves your use case.
- **Prefer customizing OOTB indexes** where possible:
  - `cqPageLucene` for pages, `damAssetLucene` for assets.
  - Easier upgrades; Cloud handles merging `-custom-*` versions.
- **Keep indexes lean**:
  - Index only the properties you actually filter on or sort by.
  - Use `includedPaths`/`queryPaths` to keep scope small.
- **Use correct async settings**:
  - AEMaaCS supports: `[async]`, `[async,nrt]`, `[fulltext-async]`.
  - Wrong `async` / `async-previous` values can prevent proper reindexing or performance improvements.
- **Manage indexes as code and via pipelines**:
  - No `reindex=true` in custom index definitions in AEMaaCS.
  - No manual edits under `/oak:index` in cloud environments.

**References:**

- [Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)  
- [Content Search and Indexing – Current Limitations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
- [Custom index reindexing issues in AEM as a Cloud Service - Sites](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25698)

### 5.2 Anti‑patterns & Cloud Manager constraints

**1. Directly modifying OOTB indexes in place**

- Don’t modify `/oak:index/damAssetLucene-10` directly.
- Always create `damAssetLucene-10-custom-1` and apply changes there.
- Future product upgrades rely on this versioning & merging behavior.

**2. New generic fulltext indexes over large trees**

- Avoid large generic indexes like `lucene-*` on all `nt:base` under `/`.
- Generic Lucene index is deprecated and removed; such patterns hurt performance and get blocked.
- Instead, create **targeted** indexes for the exact node types and paths.

**3. Indexes on `dam:Asset` that conflict with `damAssetLucene`**

- Additional fulltext indexes on `dam:Asset` can:
  - Confuse index selection & cost estimates.
  - Compete with the product index, causing performance/regression issues.
- Recommended: **extend `damAssetLucene` only**.

**4. Prohibited index properties & patterns in AEMaaCS**

Cloud Manager custom code quality rules treat the following as issues:

- `type != "lucene"` or missing `compatVersion=2`.
- `reindex` property present in a custom index.
- `seed` property present.
- Custom search indexes:
  - Deployed in `ui.content` instead of the **code package** (`ui.apps` / `_oak_index`).
  - Missing `indexRules` node.
  - Child nodes that aren’t `nt:unstructured`.
  - Mis‑named `damAssetLucene` custom indexes (need `damAssetLucene-*-custom-*` naming).
- Custom `damAssetLucene` index with **`queryPaths` set** (blocked).
- Custom analyzers and tokenizers that don’t use the required `tokenizer` name, or non‑standard analyzers.

These can **fail pipelines** starting from specific Cloud Manager releases.

**References:**

- [Custom Code Quality Rules](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/using/custom-code-quality-rules)  
- [Generic Lucene Index Removal](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/removal-generic-lucene-index)

**5. Misconfigured async / Tika / reindexing**

- Using wrong `async` or `async-previous` values can prevent proper reindexing and lead to queries returning 0 results, especially for CF indexes.
- Missing `tika` configuration when copying indexes from SDK to Cloud can break text extraction.
- Fix by:
  - Aligning `async` with `damAssetLucene` or OOTB examples.
  - Copying `tika` configuration from a Cloud environment.

**Reference:**

- [Custom index reindexing issues in AEM as a Cloud Service - Sites](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25698)

------

## 6. Configuration options & when to use them (3–5 minutes)

### 6.1 Key index-level properties

*From Oak Lucene docs; most common ones in AEMaaCS:*

- `type="lucene"`  
  - Required for all AEMaaCS‑compatible custom indexes.
- `compatVersion={Long}2`  
  - Required; ensures modern Lucene behavior.
- `async`  
  - `[async]` – standard async indexing.  
  - `[async,nrt]` – near real‑time; faster but more resource‑intensive.  
  - `[fulltext-async]` – for fulltext‑only indexing scenarios.
- `evaluatePathRestrictions={Boolean}true`  
  - Use when your queries include `ISDESCENDANTNODE` or path predicates and you want path filtering in the index rather than post‑filtering.
- `includedPaths` / `queryPaths`  
  - Use to **limit** the index scope; always set both together.
  - Avoid setting these on custom `damAssetLucene` (Cloud Manager rule).
- `maxFieldLength`  
  - Default 10000; raising it increases index size and cost. Only adjust if you have a concrete need.

**References:**

- [Lucene Index – Canonical Definition & Options](https://jackrabbit.apache.org/oak/docs/query/lucene.html)

### 6.2 Property-level options (under `indexRules`)

Common properties under `indexRules/<nodeType>/properties/<propertyName>`:

- `name`  
  - JCR property path (`"jcr:content/metadata/dc:title"`, etc.).
- `propertyIndex={Boolean}true`  
  - Enables efficient equality filters and sorting.
- `nodeScopeIndex={Boolean}true`  
  - Include property in fulltext (contains()).
- `analyzed={Boolean}true`  
  - Tokenize/normalize (important for fulltext).
- `ordered={Boolean}true` + `type="Date"` or `"String"`  
  - Required for efficient `ORDER BY` queries.
- `facet={Boolean}true`  
  - Enable faceting on this property (counts per value).
- `useInSuggest={Boolean}true` / `useInSpellcheck={Boolean}true`  
  - Enable suggestions & spellcheck features.
- `function="fn:lower-case(...)"`  
  - For function‑based indexes (e.g., for keyset pagination or case‑insensitive ordering).

**When to use:**

- Use **`propertyIndex=true`** whenever you filter or sort on a field.
- Use **`nodeScopeIndex=true`** when the property should contribute to fulltext search.
- Use **`ordered=true`** only when you actually have ordered queries; each ordered field adds cost.
- Use **function‑based indexing** when you need efficient queries such as:
  - Case‑insensitive ordering: `fn:lower-case(@lastName)`.
  - Pagination key on calculated values.

**References:**

- [Lucene Index – Indexing Rules and Property Definitions](https://jackrabbit.apache.org/oak/docs/query/lucene.html)  
- [Query Engine – Keyset Pagination & Function-based Indexing](https://jackrabbit.apache.org/oak/docs/query/query-engine.html)

------

## 7. Suggested demo / Q&A flow (5–7 minutes)

If you have time for a short demo:

1. **Explain Query on SDK:**
   - Run a real query your application uses.
   - Show which index is chosen and why.
   - Discuss how you’d change or create an index for that query.
2. **Show a `damAssetLucene` customization:**
   - Open your `ui.apps/_oak_index/damAssetLucene-*-custom-1/.content.xml`.
   - Point out one or two additional properties you’ve indexed and explain why.
3. **Developer Console in Cloud:**
   - Open Developer Console for dev.
   - Show “Oak Indexes” status dump and highlight:
     - That your custom index version exists.
     - That it’s updated and active.
4. **Q&A prompts:**
   - “Which queries are currently slow or important to you?”  
   - “What new properties or node types do we foresee needing indexes over in the next 6–12 months?”

------

## 8. Additional references for deeper learning

- **AEMaaCS index architecture & operations**
  - [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)  
  - [Search and indexing in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/search-and-indexing)  
  - [Index Converter](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/refactoring-tools/index-converter)
- **Best practices & troubleshooting**
  - [Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)  
  - [Foundation for Optimizing Indexes with AEM Cloud Service](https://experienceleague.adobe.com/en/docs/events/tech-sessions/2023/adobe-experience-manager-office-hours/optimize-indexes-aemcs)  
  - [Custom index reindexing issues in AEM as a Cloud Service - Sites](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25698)  
  - [Generic Lucene Index Removal](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/removal-generic-lucene-index)
- **Oak internals**
  - [Lucene Index](https://jackrabbit.apache.org/oak/docs/query/lucene.html)  
  - [Indexing](https://jackrabbit.apache.org/oak/docs/query/indexing.html)  
  - [Query Engine](https://jackrabbit.apache.org/oak/docs/query/query-engine.html)

------

### AEMaaCS Indexing & Query Troubleshooting (15–25 minutes)

#### 0. Session goals (1 minute)

**Objective for the audience**

By the end of this block, participants should be able to:

- Understand *when* they need a custom index vs using/adjusting an OOTB one.
- Safely customize indexes like `damAssetLucene` in AEMaaCS.
- Design and deploy custom Oak Lucene indexes “as code”.
- Use **Performance / Query tools** (Developer Console), **Query Analyzer / Explain Query**, and **Query Builder Debugger** to troubleshoot and optimize queries.

------

### 1. Quick recap: Indexing in AEMaaCS (2–3 minutes)

**Key points to restate**

- AEM uses **Apache Jackrabbit Oak** under the hood; all search is backed by **Oak indexes**.
- In AEM as a Cloud Service:
  - Only **Lucene** indexes are supported for custom work.
  - Indexes live under `/oak:index` but are **managed via code** and deployed through **Cloud Manager pipelines**, not edited on a running environment.
  - Rolling deployments create **two index generations** (old/new) and only switch traffic once reindexing succeeds.[Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
- Indexes are fundamental for performance: queries without a suitable index fall back to traversal and may trigger “Query Without Index Detected” alerts.[Adobe Experience Manager: Handle “Query Without Index Detected” Alert](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27862)

**Speaker note (short)**

> I’ll focus less on “what is an index” and more on practical decisions: when to customize, what to change, and how to debug queries using the Cloud Service tooling.

------

### 2. Customizing OOTB indexes (e.g. `damAssetLucene`) (4–5 minutes)

#### 2.1 What you *can* and *cannot* do

**Allowed (Cloud Service)**

- You *can*:
  - Add **properties** and **rules** to OOTB Lucene indexes by creating a **new versioned index** following the naming conventions.
  - Restrict or refine **paths**, **node types**, or **aggregates** to better match your content.
  - Adjust **async modes** (`async`, `async,nrt`, `fulltext-async`) within supported values.[Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
- You must:
  - Treat the index definition as **code** in your project and deploy via Cloud Manager.[Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)  
  - Always use `compatVersion=2` and **Lucene** as `type`.
  - Follow Cloud Manager code-quality rules for index naming / placement (e.g. custom indexes directly under `/oak:index`, lucene type, no `reindex` or `seed` properties in the definition).[Custom Code Quality Rules](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/using/custom-code-quality-rules)

**Not allowed**

- Directly editing `/oak:index` on Cloud Service instances.
- Using non-Lucene index types, custom analyzers, or “ensure” index definitions.
- Modifying certain critical OOTB indexes (e.g. `nodetypeLucene`, `authorizables`) that Cloud Manager explicitly forbids customizing.[Custom Code Quality Rules](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/using/custom-code-quality-rules)

#### 2.2 Safe customization pattern for `damAssetLucene`

**Speaker walkthrough**

1. **Inspect current behavior**
   - Use a local SDK or a dev environment and the **Query Performance / Explain Query** tools to identify how `damAssetLucene` is used for your DAM searches.[Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)
2. **Copy the latest definition**
   - Export the current `damAssetLucene-*` definition from an environment running the current AEMaaCS version (or use the Index Converter guidance if you came from 6.x).[Search and indexing in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/search-and-indexing)
3. **Create a new, versioned index**
   - Name it following Cloud Service conventions, for example:
     - `damAssetLucene-1-custom-1` → later `damAssetLucene-1-custom-2`, etc.[Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
4. **Add only what you need**
   - Add index rules for your custom DAM metadata properties.
   - Scope `includedPaths` to the relevant DAM subtree if appropriate (e.g. `/content/dam/your-project`).
5. **Deploy via pipeline & validate**
   - Deploy to dev using Cloud Manager.
   - Monitor the **indexing step** in the pipeline logs and confirm reindex completes.
   - Use the **Query Performance / Explain Query** tool to verify the new index is being used for your key queries.[Search and indexing in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/search-and-indexing)

------

### 3. Designing custom indexes (5–7 minutes)

#### 3.1 Precondition: prove you need an index

**Speaker emphasis**

> Never start by designing an index. Start with a **real query** that’s slow or unindexed.

- Use **Query Performance / Query Analyzer** to:
  - Find slow or frequently executed queries.
  - Inspect the **query plan** and see whether an index is used or a traversal is happening.[Query and Indexing Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)
- Use **Explain Query** to:
  - Paste the query (XPath or SQL2).
  - See the **cost**, chosen index, and whether a traversal is occurring.[Other tools for debugging AEM SDK](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/other-tools)

If an OOTB index already supports the query (or could with a small property addition), prefer extending it rather than creating a brand‑new one.

#### 3.2 Index design checklist

When you decide a custom index is required:

- **Scope by path**:
  - Use `includedPaths` or `queryPaths` so the index only covers the content subtree needed.
- **Scope by node type**:
  - Configure `indexRules` for specific node types (e.g. `cq:Page`, `dam:Asset`, your custom mixins).[Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)
- **Define only needed properties**:
  - Explicitly list properties under `indexRules/.../properties` and mark:
    - `propertyIndex = true` for property constraints and sorting.
    - `analyzed = true` only where full-text analysis is needed.
    - `nodeScopeIndex = true` only when broad full-text across node content is truly required.[Essential Tips and Best Practices for AEM Lucene Search](https://experienceleague.adobe.com/en/docs/events/adobe-customer-success-webinar-recordings/2025/aem2025/aem-lucene-search)
- **Async configuration**:
  - Use supported `async` values (`async`, `async,nrt`, `fulltext-async`) and avoid ad‑hoc combinations.[Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
- **Versioning**:
  - Treat each change as a *new* index node (e.g. `acme.product-1-custom-1` → `acme.product-1-custom-2`) rather than editing in place.[Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)

#### 3.3 Anti-patterns & gotchas

Call these out explicitly in your talk:

- **Indexing everything**
  - Overly broad full-text (`nodeScopeIndex=true` everywhere) and wide aggregates blow up index size and reindex times.
  - Rule of thumb: if total index size more than doubles vs baseline, you likely over-indexed.[Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
- **Missing path and type restrictions**
  - Queries without `path` and node type restrictions are fragile and usually need redesign, not just an index.
- **Using indexes to hide bad repository design**
  - If query predicates are complex because content hierarchy is arbitrary, fix the **taxonomy** first.[Query and Indexing Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)
- **Toggling `reindex` on Cloud Service**
  - In Cloud Service, you don’t set `reindex=true` at runtime; you redeploy index definitions through pipelines and let the platform reindex during deployment.

------

### 4. Troubleshooting queries & indexes – tools and techniques (7–10 minutes)

This is the new part you asked to emphasize: include it as a dedicated section in the session.

#### 4.1 Performance & query consoles: where to look

**AEM as a Cloud Service – Developer Console**

- Accessible from Cloud Manager’s environment view.[Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)
- Relevant features:
  - **Query Performance Tool**:
    - Lists **slowest** and **most popular** queries.
    - Lets you **Explain** queries to see the index used and query plan.
    - Allows ad‑hoc query execution for testing.
  - **Index statistics**:
    - Export Oak index status (for example, to confirm reindex completion, see index sizes).

**Local SDK / AEM 6.5-style consoles**

- **Operations Dashboard → Performance**
  - `Request Performance`: slowest page requests.
  - `Query Performance`: slowest queries (with stats from Oak’s `QueryStats` MBean).
  - `Explain Query`: **Query Analyzer** UI that shows the execution plan and chosen index for a given XPath/JCR‑SQL2 query.[Operations Dashboard](https://experienceleague.adobe.com/en/docs/experience-manager-65-lts/content/sites/administering/operations/operations-dashboard)

Use the SDK to reproduce and analyze locally, then push fixes via code to Cloud Service.

#### 4.2 Query Analyzer / Explain Query: how to read it

**Workflow**

1. Take an actual query:
   - From logs, your code, or the Query Builder Debugger (more below).
2. Convert to XPath or JCR‑SQL2 if necessary (Query Builder Debugger can do this).
3. Paste into **Explain Query / Query Analyzer** and run *Explain*, not full execution.

**What to look at**

- **Index name**
  - Confirm the query uses the *expected* index (e.g. your custom `acme.product-1-custom-2` rather than a generic Lucene index).
- **Cost estimate**
  - High cost or “traversal” flags indicate missing or unsuitable indexes.
- **Warnings**
  - Node traversal warnings or full repository scans are red flags.
- **Node count / execution time**
  - Use these to validate improvements when you tune the query or index.[Query and Indexing Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)  
  - See also the SDK tooling summary.[Other tools for debugging AEM SDK](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/other-tools)

#### 4.3 Query Performance / “Performance console” for slow queries

**Use-case**

> “Authors say search is slow” or “a page using QueryBuilder is timing out.”

**Steps**

1. **Identify slow queries**
   - Open **Query Performance** in the Developer Console (Cloud Service) or Operations Dashboard (SDK).
   - Sort by duration or frequency to find:
     - Queries with very long average execution times.
     - Queries called very frequently (even if each run is relatively fast).[Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)
2. **Explain the worst offenders**
   - Use the built-in **Explain / Query Analyzer** to inspect the plan and chosen index for those statements.[How to investigate search related issues in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/troubleshooting/how-to-investigate-search-related-issues)
3. **Decide on the fix**
   - Simplify or refactor the query:
     - Add path restrictions.
     - Avoid expensive predicates or wildcards.
     - Reduce result size with sensible limits.
   - Or design/update an index so that:
     - The query is fully satisfied by a single index.
     - Sorting and filtering properties are explicitly indexed.
4. **Re-measure**
   - After deploying index or code changes, re-check Query Performance and Explain Query to confirm cost and execution time improvements.

#### 4.4 Query Builder Debugger & IDE workflow

**Query Builder Debugger**

- Web UI for running and tuning **QueryBuilder** queries.
- Shows:
  - QueryBuilder parameters.
  - Generated XPath/JCR‑SQL2.
  - Result count and timing.[Troubleshooting Slow Queries](https://experienceleague.adobe.com/en/docs/experience-manager-65-lts/content/implementing/developing/bestpractices/troubleshooting-slow-queries)

**How to use it in practice**

1. Start from the code:
   - Locate the `Map<String, String>` or `PredicateGroup` you’re passing to `QueryBuilder` in your Sling Model/servlet.
2. Reproduce the query in Query Builder Debugger:
   - Paste the same parameters and run.
   - Inspect the generated XPath/SQL2.
3. Send that XPath/SQL2 to **Explain Query / Query Analyzer**:
   - This connects the dots from developer code → QueryBuilder → underlying index usage.
4. Adjust:
   - Simplify QueryBuilder predicates.
   - Update index definitions if needed.

For day‑to‑day dev in IntelliJ/Eclipse:

- Use **AEM SDK logs** and `query.log` (DEBUG for `org.apache.jackrabbit.oak.query` and `com.day.cq.search`) to capture real queries, then feed them into Explain Query.[Oak Queries and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/deploying/deploying/queries-and-indexing)

#### 4.5 End-to-end troubleshooting “playbook” (you can present this as a slide)

**Scenario:** Page or API is slow due to queries.

1. **Detect**
   - Use **Request Performance** (SDK) and/or monitoring to identify slow URLs.
   - Confirm the slow requests correlate with search or listing components.
2. **Capture queries**
   - Enable short-lived DEBUG logging for:
     - `org.apache.jackrabbit.oak.query`
     - `org.apache.jackrabbit.oak.plugins.index`
     - `com.day.cq.search` (for QueryBuilder).[Oak Queries and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/deploying/deploying/queries-and-indexing)
   - Or use the **Query Performance** view in Developer Console.
3. **Analyze**
   - For each candidate query:
     - Run in **Explain Query / Query Analyzer** and inspect the index, cost, and traversal.
     - Decide whether to:
       - Improve query structure (path restrictions, limits, reduced joins).
       - Extend an OOTB index or create a dedicated custom index.
4. **Implement as code**
   - Add/adjust index definitions in your AEM project under `/oak:index` package (Lucene, `compatVersion=2`, correct naming).[AEM Project Structure](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure)
   - Refactor the query in the component/service.
5. **Validate**
   - Deploy to SDK or dev via Cloud Manager.
   - Use **Query Performance** and **Explain Query** again to confirm:
     - The expected index is used.
     - Execution time and node count are acceptable.
   - For critical paths, add automated tests (integration/performance).

------

### 5. Optional: 5-minute live demo idea

If you want to turn this into a quick demo:

1. Pick a **real SHRSS query** used in a component (e.g., listing jobs, events, or assets).
2. Show the **Sling Model or servlet** in IntelliJ.
3. Mirror the query in **Query Builder Debugger**, show the generated SQL2/XPath.
4. Copy that into **Explain Query / Query Analyzer**:
   - Show which index is used and whether it’s efficient.
5. Show the relevant **index definition** in the project and point out:
   - `indexRules`, `properties`, and key flags (`propertyIndex`, `analyzed`, `nodeScopeIndex`).
6. Close by showing **before/after** costs or times in the Query Performance tool.

This keeps the session firmly grounded in *their* code while teaching them the Cloud Service indexing and troubleshooting patterns.

---

### References

- [Content Search and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/indexing)
- [Query and Indexing Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/query-and-indexing-best-practices)
- [Indexing best practices in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/development/understand-indexing-best-practices)
- [Search and indexing in AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/search-and-indexing)
- [Developer console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)
- [Other tools for debugging AEM SDK](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-sdk/other-tools)
- [Operations Dashboard](https://experienceleague.adobe.com/en/docs/experience-manager-65-lts/content/sites/administering/operations/operations-dashboard)
- [Troubleshooting Slow Queries](https://experienceleague.adobe.com/en/docs/experience-manager-65-lts/content/implementing/developing/bestpractices/troubleshooting-slow-queries)
- [How to investigate search related issues in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/troubleshooting/how-to-investigate-search-related-issues)
- [Oak Queries and Indexing](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/deploying/deploying/queries-and-indexing)
- [Essential Tips and Best Practices for AEM Lucene Search](https://experienceleague.adobe.com/en/docs/events/adobe-customer-success-webinar-recordings/2025/aem2025/aem-lucene-search)
- [AEM Project Structure](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure)
- [Adobe Experience Manager: Handle “Query Without Index Detected” Alert](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27862)