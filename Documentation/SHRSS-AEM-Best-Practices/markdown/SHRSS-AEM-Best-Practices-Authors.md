# AEMaaCS Authoring Best Practices

*Authors & Content Designers – SHRSS Volume*

> This volume assumes the `SHRSS AEM Content Authoring Guide` exists as the “how‑to” manual. Here we focus on **advanced tips, tricks, and real‑world patterns** beyond Experience League.

------

## 1. Authoring Mental Models

- **Pages vs Content Fragments (CFs)**
  - Pages = where layout and storytelling happen.
  - CFs = the “records” for Jobs, Events, News, Locations, Shared Data.
- **Components**
  - Components are your building blocks. Many SHRSS components are based on **Core Components**, so patterns are consistent.
- **Tags & Shared Data**
  - Tags and shared CFs ensure **Jobs, Events, News, and Locations** all “speak the same language” for filters, cards, and navigation.

For basic tutorials, see:

- [Authoring a page in AEM Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/page-authoring-overview-feature-video-use)  
- [Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/content-fragments)

------

## 2. Jobs Authoring – Advanced Patterns

### 2.1 When to Create Manual Jobs vs Wait for Workday

- Use **Workday jobs** for real, externally posted roles.
- Use **manual jobs** only when:
  - A job is not yet in Workday but needs visibility (e.g., immediate event hire).
  - You need a special promotional job not tracked in Workday.

**Tip:** Keep manual jobs aligned with Workday’s taxonomy (departments, locations, job types) so lists and filters behave consistently.

### 2.2 Working with Job CFs

Key patterns from the authoring guide:

- Jobs CFs live under:
  `Assets > Files > SHRSS > Content Fragments > Jobs > <region>/<country>/<property>`
- Two types:
  1. **API-driven (Workday)**
     - Fields like Job ID, title, Workday URL, location data are controlled by Workday.
     - You only adjust **image, hot job flag, SEO/JSON-LD overrides**.
     - “Is API Data” toggle = ON.
  2. **Manual**
     - You control all fields.
     - Must maintain tags and categories manually.
     - “Is API Data” toggle = OFF.

**Tips & Tricks**

- Do **not** change Workday IDs in Workday jobs; they are the “primary key” that syncs data.
- Use **Hot Job** sparingly; if everything is “hot”, nothing is.
- When jobs don’t appear:
  - Check CF is **published**.
  - Check **category and location tags** match the filters used on the Jobs listing component.
  - Check **post date/expiration date** fields: expired jobs are often auto‑filtered.

### 2.3 Jobs on Pages – Components

Typical components:

1. **Job Search / Listing**  
   - Driven by CF queries (or GraphQL persisted queries).  
   - Filters: department, job type, location, sometimes tags.  
   - Authorable settings often include:
     - Default filters.
     - “No results” message.
     - Page size (# of jobs per page).
2. **Job Card / Job Detail**  
   - Reads a single Job CF (from URL or component config).  
   - Shows description, requirements, location, and structured data for SEO.

**Advanced Tips**

- If a particular property or region wants a custom jobs view:
  - Create a **section landing page** and configure the listing component to filter to that region/property via tags. Avoid creating separate job CF folders unless IA requires it.
- For SEO:
  - Use the override fields only when necessary; try to keep them aligned with Workday titles so analytics remains consistent.

------

## 3. Events Authoring – Advanced Patterns

### 3.1 Events CFs

Events are CFs that typically include:

- Title, summary, long description.
- Start/end date & time, status (scheduled, cancelled, postponed).
- Status message (e.g., “Cancelled – weather”).
- Location reference (Location CF).
- Hero/card image.

**Tips**

- Use **status + status message** rather than editing the title to show “Cancelled” – this keeps URLs and analytics stable.
- For multi‑day events, be consistent in how you set start/end times; filters and calendar views depend on this.

### 3.2 Events on Pages

Components:

- **Event List / Calendar**
  - Often filterable by date range, event type, location.
- **Event Detail**
  - Pulls all CF fields, including structured location and images.

**SHRSS Overlay Tips**

- “Hiring events” may reuse Events CFs but be shown in Careers context:
  - Ensure tags **bridge Jobs and Events** (e.g., same property tags).
- Past events:
  - Often left visible for SEO but clearly marked as “Past.”  
  - Coordinate with the PM on whether old events should be auto‑archived from lists.

------

## 4. News Authoring – Advanced Patterns

### 4.1 News CFs vs Pages

- CFs capture:
  - Headline, summary, publish date, author, category, hero image.
- Pages handle:
  - Long-form content, layout, related content teasers.

**Tips**

- Use CF fields for any property that appears in **cards or lists** (e.g., category, publish date).
- Avoid “hiding” critical metadata in the page body; it won’t be queryable.

### 4.2 News Lists

- News list components typically allow:
  - Filter by category and date.
  - Sorting by publish date.
- For property or brand‑specific news:
  - Use tag filters rather than separate pages/folders wherever possible.

------

## 5. Locations Authoring – Advanced Patterns

### 5.1 Location CFs Driven by DPLT

- Locations CFs are **not arbitrary**:
  - They map to DPLT location records.
  - Contain address, geo coordinates, display names, and sometimes contact info.

**SHRSS Tips**

- If a location is wrong, don’t fix it in AEM:
  - Raise a request to update it in **DPLT**, then let sync update AEM.
- When creating content (Jobs/Events/News) tied to a location:
  - Always use the **Location CF reference**, not copy‑pasted text.

### 5.2 Location on Pages

- Location components:
  - Map view + list.
  - Detail views with address, hours, amenities.
- Use shared location components consistently:
  - Avoid manual, free‑form address blocks spread across pages.

------

## 6. Navigation & Data Display

### 6.1 Understanding Shared Data

- Shared Data CFs and tags unify:
  - Jobs → property, department, job type.
  - Events → property, event type, brand.
  - News → category, property, brand.

**Tips**

- Before inventing a new tag:
  - Check if there is an existing tag or Shared Data CF that fits.
- Avoid synonyms:
  - “Front office” vs “Front-of-house” – pick one and standardize.

### 6.2 Navigation Components

- Many navigation components are data‑driven:
  - Mega menus, careers navigation, property pickers.
- When navigation seems wrong:
  - Check the underlying **Shared Data CFs** and **tags**, not just the menu component.

------

## 7. General Authoring Hygiene

- Use **View as Published** to review pages; WCM mode vs published mode can differ (personalization, targeting).
- Keep **page titles and URLs stable**; prefer redirects over deleting/recreating pages.
- Clean up **orphaned CFs** and assets periodically with DAM governance support.

------

## 8. Authoring SHRSS Overlay Summary

For SHRSS authors:

- Think in **CFs first** for Jobs, Events, News, and Locations.
- Use **tags and Shared Data** to make content discoverable and filterable.
- Respect integration boundaries:
  - Workday is the authority for jobs.
  - DPLT is the authority for locations.
- Use your `SHRSS AEM Content Authoring Guide` for step‑by‑step tasks, and this volume for “why” and “how to do it like an expert.”

Use alongside:

- The **Consolidated All‑Roles Volume**.
- The **DAM Volume** for folder structure and metadata practices.