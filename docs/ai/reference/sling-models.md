# Sling Models – Definition, Usage, and Best Practices

> **Purpose**
> This document defines **canonical Sling Models patterns** for AEM projects.
> It is intended for **agents and developers** to ensure Sling Models are used correctly,
> efficiently, and safely across components and backend services.
>
> This file is **authoritative** when referenced from AGENTS.md`.

---

## 1. What Sling Models Are (and Are Not)

### Sling Models ARE
- Lightweight **view models** for rendering content
- A clean separation between **HTL (presentation)** and **Java logic**
- Adaptable representations of request, resource, or repository state

### Sling Models are NOT
- Business logic engines
- Workflow executors
- Data mutation layers
- Long-running or network-bound services

> **Rule of thumb:** Sling Models should be *fast, deterministic, and side‑effect free*.

---

## 2. Common Adaptables (When to Use Which)

### `@Model(adaptables = Resource.class)`
**Use when**
- Rendering depends only on repository data
- You do not need request-specific context (selectors, suffix, query params)

**Typical scenarios**
- Most component rendering
- DAM metadata read-only access
- Page structure introspection

```java
@Model(
  adaptables = Resource.class,
  defaultInjectionStrategy = DefaultInjectionStrategy.OPTIONAL
)
public class TeaserModel {

  @ValueMapValue
  private String title;

  @ValueMapValue
  private String description;

  public String getTitle() { return title; }
  public String getDescription() { return description; }
}
```

✅ Preferred for most components

---

### `@Model(adaptables = SlingHttpServletRequest.class)`
**Use when**
- Request-scoped context is required
- You need selectors, suffix, query parameters, headers, or request attributes
- You need request-scoped memoization of expensive work (carefully)

```java
@Model(adaptables = SlingHttpServletRequest.class)
public class RequestAwareModel {

  @Self
  private SlingHttpServletRequest request;

  public String getSelector() {
    return request.getRequestPathInfo().getSelectorString();
  }
}
```

⚠️ Use sparingly — increases coupling to request context

---

### Multiple adaptables
```java
@Model(adaptables = { Resource.class, SlingHttpServletRequest.class })
```

**Use only when**
- The model must support both authoring and rendering contexts
- You document which adaptable is expected in each case

---

## 3. Injection & Lifecycle Best Practices

### Preferred injection styles
- `@Self` for the adaptable (`Resource`, `SlingHttpServletRequest`)
- `@ValueMapValue` for properties
- `@ChildResource` for structured content
- `@OSGiService` for service access

```java
@OSGiService
private MySearchService searchService;

@Self
private Resource resource;
```

### Avoid
❌ Heavy work in `@PostConstruct`  
❌ Repository writes  
❌ Network calls  
❌ Starting workflows  
❌ Enqueuing jobs from rendering models  

---

## 4. Good vs Bad Patterns

### ✅ GOOD: Model delegates to a service
```java
@OSGiService
private SearchService searchService;

private List<Item> items;

@PostConstruct
protected void init() {
  items = searchService.findItems(resource.getPath()); // bounded + cached in service if needed
}
```

- Model stays thin and render-focused
- Business logic stays in services
- Easier to test

---

### ❌ BAD: Business logic + mutation in a model
```java
@PostConstruct
protected void init() {
  Session session = resource.getResourceResolver().adaptTo(Session.class);
  Node node = session.getNode("/content");
  node.addNode("foo"); // ❌ mutation during render
}
```

Why this is bad:
- Side effects during rendering
- Not idempotent
- Cloud-unsafe and restart-unsafe
- Hard to test / debug

---

## 5. Sling Models and HTL Usage

```html
<sly data-sly-use.model="com.example.core.models.TeaserModel">
  <h2>${model.title}</h2>
  <p>${model.description}</p>
</sly>
```

Rules:
- HTL should not contain business logic
- No repository access in HTL
- No service lookups in HTL

---

## 6. Performance & Caching Guidance

### Do
- Memoize expensive work **per request** (request attributes), if needed
- Keep model getters cheap (avoid re-computation)

### Do NOT
- Use static fields for caching request/user-specific data
- Store `ResourceResolver`/`Session` in long-lived fields beyond model lifetime
- Run repository-wide searches in models

---

## 7. Testing Sling Models

### Recommended
- Use **AEM Mocks**
- Adapt from mocked `Resource` or `SlingHttpServletRequest`
- Mock **services**, not the model

```java
TeaserModel model = context.currentResource().adaptTo(TeaserModel.class);
assertEquals("Expected title", model.getTitle());
```

### Prohibited
❌ Mocking the Sling Model itself  
❌ Tests whose primary value is verifying mock interactions  

> If the test passes when the production logic is removed, it’s not a real test.

---

## 8. When NOT to Use Sling Models

Do not use Sling Models for:
- Background processing
- Repository mutation
- External system integration
- Workflow steps or schedulers
- Cross-repo data aggregation that requires unbounded queries

Use OSGi services, Sling Jobs, or workflows instead.

---

## 9. Content Fragment (CF) Sling Model Patterns

Content Fragments are powerful, and they’re also a frequent source of **slow rendering** when models treat the repository like a database.

### 9.1 Preferred approach
Sling Models that render CF data should:
- Adapt from the **component resource** (or request) and locate the CF reference
- Adapt the referenced resource to `ContentFragment` (CFM API)
- Read only the required elements/variations
- Delegate expensive operations (searching, resolving related content, localization mapping) to a service

### 9.2 Typical component contract
A component stores a CF reference as a property, for example:
- `fragmentPath` (string) or
- `fragment` (path reference) or
- `cq:fragmentPath` (varies by implementation)

The model reads that property and resolves the CF resource.

### 9.3 Example: CF-backed teaser (Resource adaptable)
```java
import com.adobe.cq.dam.cfm.ContentFragment;
import com.adobe.cq.dam.cfm.ContentElement;
import com.adobe.cq.dam.cfm.ContentVariation;
import org.apache.commons.lang3.StringUtils;

@Model(
  adaptables = Resource.class,
  defaultInjectionStrategy = DefaultInjectionStrategy.OPTIONAL
)
public class CfTeaserModel {

  @Self
  private Resource resource;

  @ValueMapValue
  private String fragmentPath;

  @ValueMapValue
  private String variation; // optional: "en", "fr", "master", etc.

  private ContentFragment fragment;

  @PostConstruct
  protected void init() {
    if (StringUtils.isBlank(fragmentPath)) {
      return;
    }
    Resource cfRes = resource.getResourceResolver().getResource(fragmentPath);
    if (cfRes == null) {
      return;
    }
    fragment = cfRes.adaptTo(ContentFragment.class);
  }

  public boolean hasFragment() { return fragment != null; }

  public String getTitle() {
    return getElementAsString("title");
  }

  public String getDescription() {
    return getElementAsString("description");
  }

  private String getElementAsString(String elementName) {
    if (fragment == null) return null;

    ContentElement el = fragment.getElement(elementName);
    if (el == null) return null;

    // Variation handling
    if (StringUtils.isNotBlank(variation)) {
      ContentVariation v = el.getVariation(variation);
      if (v != null && v.getValue() != null) {
        return v.getValue().getValue(String.class);
      }
    }
    // Fallback to master
    return el.getContent();
  }
}
```

✅ Characteristics of a good CF model:
- Reads a *known CF reference* (no searching)
- Bounded access (single CF read)
- Variation handling with sane fallback
- No writes, no external calls

### 9.4 Request-adapted CF models (when justified)
Use `SlingHttpServletRequest` when:
- Variation/locale is derived from request context (selector/suffix/URL language root)
- You need request-scoped memoization (e.g., same CF referenced multiple times on a page)

Example: derive variation from a language root and fall back safely.

```java
@Model(adaptables = SlingHttpServletRequest.class)
public class CfRequestAwareModel {

  @Self
  private SlingHttpServletRequest request;

  @Self
  private Resource resource;

  @ValueMapValue
  private String fragmentPath;

  @OSGiService
  private CfVariationResolver variationResolver; // your service

  private String variation;

  @PostConstruct
  protected void init() {
    variation = variationResolver.resolveVariation(request, resource); // bounded + cacheable
  }

  public String getVariation() { return variation; }
}
```

### 9.5 When to use each adaptable (CF-specific)
- **Resource adaptable:** simplest, fastest, preferred for most CF components (path reference → read elements)
- **Request adaptable:** when variation/locale/personalization is request-derived
- **Do NOT** use request adaptable just because “it’s available”

### 9.6 Avoid these CF anti-patterns

#### ❌ Anti-pattern: searching for the CF during render
```java
// ❌ QueryBuilder search in @PostConstruct to "find a fragment"
```
Why it’s bad:
- slow and unbounded on large repos
- unpredictable indexing behavior
- creates production-only failures

✅ Better: store an explicit `fragmentPath` in component content.

#### ❌ Anti-pattern: iterating related fragments with per-item resolver calls
```java
// ❌ for each related fragment path: resolve + adapt + read + repeat (N+1)
```
✅ Better: delegate relation resolution to a service that can page/batch/cache.

#### ❌ Anti-pattern: mixing writes with reads
- updating CF metadata during render
- creating variations on the fly
- “self-healing” content structure

### 9.7 MSM + multilingual + translation automation considerations (CF/EF)
If your project relies on OOTB translation automation that expects mirrored structures:
- CF/EF folder structure may need to **mirror page structure** to preserve mapping
- Models should not “guess” language mappings by broad searches
- Prefer explicit mappings (or a dedicated resolver service) that understands your MSM blueprint/live-copy conventions

### 9.8 Testing CF models (pragmatic guidance)
- Unit tests should validate:
  - missing/invalid fragment path handling
  - element retrieval and fallbacks
  - variation behavior when present/missing
- Mock **dependencies** (variation resolver service), not the model
- For pure unit tests, you can simulate CF resources using AEM Mocks + minimal adapters
- For higher confidence, add integration-style tests where CF APIs are available (project-dependent)

---

## 10. Architectural Contract (Non-Negotiable)

Sling Models must:
- be read-only
- be fast and deterministic
- delegate complex logic to services
- respect cloud immutability and restart safety
- remain testable

Violations are **architecture defects**, not style issues.

---

**This document is intentionally opinionated.  
Consistency and predictability matter more than cleverness.**
