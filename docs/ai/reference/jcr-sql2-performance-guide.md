# JCR-SQL2 Performance Guide (Priority Playbook)

**Date:** December 20, 2025  
**Scope:** AEM/Oak query optimization for large DAM sets; emphasizes SQL2 patterns, indexing, and caching.  

## Priority Best Practices (Most Impact → Least)
1. **Constrain by path**: Always use `ISDESCENDANTNODE(asset, '<root>')` with the smallest viable roots. Avoid repository-wide scans.
2. **Index-friendly predicates**: Filter on indexed properties only; avoid functions on property values. Add property indexes for high-cardinality filters (dc:format, dc:category, dc:retouched, cq:tags, custom facets).
3. **Bound result windows**: Cap `LIMIT`; avoid large offsets. Prefer keyset pagination over deep offset paging.
4. **Keyset pagination**: Use `WHERE asset.[sort] < ?` (desc) or `>` (asc) plus tie-breaker on path; keeps traversal minimal and stable between pages.
5. **Order by indexed fields**: Only `ORDER BY` properties marked `ordered=true` in indexes (e.g., `@jcr:created`, `@lastModified`). Otherwise, Oak will sort in-memory.
6. **Avoid wildcard/leading-like**: `CONTAINS` is fine when needed; avoid `LIKE '%foo%'` on unindexed props. Escape user input.
7. **Prefer simple AND/IN over OR chains**: Use `IN (…)` for multi-values. Large OR chains can degrade plans.
8. **Exclude known non-targets early**: e.g., `asset.[jcr:content/contentFragment] IS NULL` to skip fragments.
9. **Limit selected columns**: `SELECT asset.*` is typical; avoid joins. Do not fetch blobs/renditions.
10. **Explain and validate**: Use `explain`/`oak-run` to ensure indexes are used and traversals avoided.

## Index Recommendations (damAssetLucene overlay)
- Ensure the following properties are indexed and orderable where used:
  - `jcr:content/metadata/dc:format`
  - `jcr:content/metadata/dc:category`
  - `jcr:content/metadata/dc:retouched` (or similar flag)
  - `jcr:content/metadata/cq:tags` (multi-valued)
  - `jcr:content/metadata/dc:title` (if searched/sorted)
  - `jcr:created`, `jcr:content/jcr:lastModified` (ordering)
- Enable `ordered=true` on the primary sort fields (default `jcr:created desc`), plus tie-breaker on `jcr:path` if using keyset.
- Add property indexes for any additional high-traffic predicates (e.g., custom category facets).
- Validate analyzers for `cq:tags` (exact match) vs fulltext fields; consider faceting if needed.

## Query Construction Tips
- Start with path + exclusion of content fragments.
- Apply property/tag predicates with `IN` for multi-values.
- Date range: `property >= start` / `<= end` when provided.
- Fulltext: `CONTAINS(asset.*, 'term')` only when present; avoid combining with non-indexed ORDER BY.
- Sorting: default to indexed fields; if custom order requested on unindexed field, override to safe default to avoid slow plans.

## Pagination Strategy
- Prefer keyset using the primary sort field (e.g., `jcr:created`) and asset path as tie-breaker.
- When offset is required for compatibility, cap limit and warn if deep offsets requested.
- Return cursor tokens (last sort value + path) for subsequent pages when possible.

## Caching Recommendations
- **SearchCache (in-memory):** Keep; key by normalized predicates + user groups + orderby. Track hit/miss metrics.
- **HTTP Cache (ACS AEM Commons):** Use cautiously. Only consider for public, non-personalized `.results-v2.html` fragments; likely disable for authenticated users.
- **Result set reuse:** Cache computed facets/metadata per predicate signature when feasible.

## Safeguards
- Reject/short-circuit queries lacking a path when default root is disabled.
- Enforce max page size; normalize/escape all literals.
- Log skipped predicates (unknown ops) at debug; avoid noisy warns.
- Regularly run `explain` on representative queries to catch regressions after index changes.
