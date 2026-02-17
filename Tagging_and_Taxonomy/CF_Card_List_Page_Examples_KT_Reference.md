# CF Card List Component — Page Examples (KT Quick Reference)

Pages in the exported content package that contain the **CF Card List** component (`shrss/components/cfcardlist`), for use during the Tagging, Taxonomy & Metadata Governance KT session.

---

## Best for “List by tags” demo

| Page path (JCR) | Site / context | CF Card List config |
|-----------------|----------------|---------------------|
| **`/content/shrss/corporate/hardrock/en/blog`** | Corporate Hard Rock → Blog | **listType:** `tags` • **tagsList:** `shrss:news-categories/featured-news` • **tagsRootFolder:** `/content/dam/shrss/cf/news/corporate/en` • **type:** news • **categories:** false (card config) |

**Why use it:** Shows a **tag-driven** list: only News CFs that have the tag `shrss:news-categories/featured-news` in their categories appear. Ideal for demonstrating how tags control which content appears in the list.

---

## Other pages with CF Card List

| Page path (JCR) | Notes |
|-----------------|--------|
| **`/content/shrss/reverb/en/tbd/en/cf-card-list-page`** | Dedicated CF card list page. Contains **two** CF Card List components: one **Events** (listType=rootPath, rootFolder=events path), one **News** (listType=rootPath, rootFolder=news path). Good for comparing rootPath vs. tags. |
| **`/content/shrss/reverb/en/tbd/en/event-list-reverb`** | Events list (rootPath-style; eventBasePath set). |
| **`/content/shrss/corporate/hardrock/en/home`** | Home page with CF Card List (categories=false). |
| **`/content/shrss/corporate/hardrock/en/corporate`** | Corporate section with CF Card List. |
| **`/content/shrss/hotel/en/home`** | Hotel home with CF Card List. |

---

## How to open in Author

- **Sites** → navigate to the path (e.g. **Corporate** → **Hard Rock** → **en** → **Blog** for the blog page).
- Open the page for **Edit** and select the CF Card List component to view or edit **List type**, **Tags**, **Tags root folder**, and **Type** (News/Events).

---

## Component config recap (for tags-based list)

- **List type:** **Tags**
- **Tags:** one or more tag IDs (e.g. `shrss:news-categories/featured-news`)
- **Tags root folder:** DAM path under which to search CFs (e.g. `/content/dam/shrss/cf/news/corporate/en`)
- **Type:** **News** or **Event** (CF model)

Stored in the component node as `listType`, `tagsList` (or tags picker), `tagsRootFolder`, and `type`.
