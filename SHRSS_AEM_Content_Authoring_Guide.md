# SHRSS AEM Content Authoring Guide

*This guide summarizes how to author SHRSS content in AEM as a Cloud Service, based on your KT sessions, and ties each topic to AEM’s standard authoring concepts and public documentation.*

------

## 1. Authoring Fundamentals (Context for All Topics)

Before we go into Jobs, Events, etc., all topics share some core concepts:

- **Pages vs. Content Fragments (CFs)**
  - **Pages** are what visitors see (URLs in the browser). You author them in the **Sites** console using the Page Editor and components.
  - **Content Fragments** are **structured content records** (jobs, events, news, promotions, locations, etc.), stored under **Assets** and reused by multiple pages/components.
- **Components**
  - Components are the building blocks on pages (text, images, cards, lists, navigation, etc.).
  - Many SHRSS components are **custom** but follow AEM’s general rules: you **configure them** in dialogs, and they often **reference CFs, tags, and assets**.
- **Tags & Shared Data**
  - Tags and shared CFs drive **filters, search, lists, and navigation**. Getting these right is key for Jobs, Events, News, Locations and “Navigation and Data Display”.

For a basic refresher:

- **General page authoring & components**
  - [Overview of Authoring in AEM Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/aem-sites-authoring-overview)  
  - [Authoring a page in AEM Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/page-authoring-overview-feature-video-use)  
  - [Components (AEM as a Cloud Service)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/components)
- **Content Fragments**
  - [Content Fragments (AEM as a Cloud Service)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/content-fragments)  
  - [Working with Content Fragments – Concepts and Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/overview)  
  - [Authoring Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/authoring)

------

## 2. Jobs

### 2.1 Purpose & High-Level Model

Jobs on SHRSS are powered by **Job Content Fragments** that originate from **Workday** plus some **author-controlled fields**.

There are two patterns:

1. **API-driven jobs (Workday-fed)**
   - Created and updated automatically by Workday.
   - Most fields are **read-only** for authors and are overwritten on sync.
2. **Manually-authored jobs**
   - Created by authors directly as Job CFs.
   - Must stay consistent with the taxonomy (job categories, locations) used by Workday-fed jobs.

### 2.2 Where Job Content Lives

- **CF location** (example pattern from KT):
  `Assets > Files > SHRSS > Content Fragments > Jobs > <region>/<country>/<property or location>`
- **Folder structure** often mirrors **location hierarchy** (region / country / property) to make it easier to find jobs tied to specific properties.

### 2.3 Fields & Author-Controlled Settings

From the KT:

- **System / Workday-controlled fields** (examples)
  - Job ID / Job Requisition ID
  - Job title
  - Job URL (Workday job posting URL)
  - Location fields (country, state, city, property)
  - These are **overwritten** whenever Workday sync runs.
- **Author-controlled fields** (not overwritten by Workday)
  - **Job image** – used on job cards/details.
  - **Hot job flag** – to visually highlight specific jobs.
  - **SEO / LD-JSON override** – for structured data overrides where necessary.
  - **“Is API Data” toggle**
    - When **on**: CF is treated as Workday/API-managed; Workday fields are authoritative.
    - When **off**: CF behaves as a purely manual job entry.

> Rule of thumb: anything Workday sends is treated as **source of truth**; authors only enrich with additional display-only fields (images, flags, overrides).

### 2.4 Creating & Editing Jobs

**To create a job (manual job)**

1. Go to **Assets > Files > SHRSS > CF > Jobs** and navigate to the correct folder (region/country/property).
2. Click **Create > Content Fragment**.
3. Choose the **Job** model.
4. Fill required fields:
   - Job title, description, location, categories, etc. (some fields may be Workday-like; just follow the model).
5. Set **“Is API Data” = false** for fully manual jobs.
6. Fill any **optional display fields**:
   - Image, Hot job flag, SEO/JSON-LD overrides.
7. Save and **Publish** the CF.

**To edit a Workday job**

- You typically only change:
  - Image, Hot job flag, overrides.
- Avoid changing **Workday identifiers**; they will be overwritten or may break sync.

### 2.5 How Jobs Show on the Site

There are typically two job-facing components:

1. **Job Search / Listing component**
   - Displays a list of jobs with filter and search controls.
   - Filters usually include:
     - Job category (based on tags or category field).
     - Location (derived from location fields or tags, e.g., region/country/property).
   - Can show “Hot job” visual treatments based on the flag.
   - Has configurable **labels and messages**:
     - “No jobs found” message.
     - Button labels and headings.
2. **Job Detail / Job Card component**
   - On a detail page, reads a specific Job CF (often via URL parameter or configured reference).
   - Displays full description, location details, and any structured data needed by search engines.

> If a job is missing in listings:
>
> - Confirm the CF is **published**.
> - Confirm **tags/categories** match filter settings.
> - If Workday-driven, confirm the job is still active in Workday.

### 2.6 Best Practices

- **Do not change Workday IDs** in Workday-sourced jobs.
- Use the **Hot job flag** sparingly to keep emphasis meaningful.
- **Archive or unpublish** jobs that should no longer be visible; Workday generally handles expiry for Workday-sourced jobs.
- Ensure **tags** (job categories, properties) are kept consistent; they drive filters and search.

### 2.7 References

- Content Fragments as data records:
  [Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/content-fragments)  
- Headless/structured authoring basics:
  [AEM Headless Content Author Journey](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/journeys/author/overview)

------

## 3. Events

### 3.1 Purpose & High-Level Model

Events are also modeled as **Content Fragments**, powering:

- **Event calendars and listings** (date- and filter-based).
- **Event detail pages** (single-event experiences).
- Optional **promotional cards** for “hiring events” and similar promotions.

### 3.2 Event Content Fragment Model

From the KT, the Event CF model typically includes:

- Core fields:
  - Title, Description, Long/Additional details.
  - Start date and time (and often end date/time).
  - Event status (e.g., scheduled, cancelled, postponed).
  - Status message (e.g., “Cancelled”, “Rescheduled”).
- Location fields:
  - Reference to a **Location CF** (from DPLT-driven locations).
- Media:
  - Hero image / card image.
  - Optional hero override text.
- Control flags:
  - “Generated event” / “API event” flag to distinguish system-generated events from manually created ones.

### 3.3 Storage & Folder Structure

- **CF location** (pattern from KT):
  `Assets > Files > SHRSS > Content Fragments > Events > <year>/<month>/…`

This is mainly for **author convenience**; the listing components filter by **CF fields and tags**, not by folder name.

### 3.4 Creating / Editing Events

1. Navigate to the Events CF folder for the correct year/month.
2. Click **Create > Content Fragment** and choose the **Event** model.
3. Fill:
   - Title, Description, Status.
   - Start date/time (and end date/time if used by design).
   - Location (pick an existing Location CF; see Locations section).
   - Hero/card image and optional overrides.
4. Set **status** and **status message** (e.g., “Cancelled”, “Sold Out”) as needed.
5. Save and **Publish** the CF.

> Unpublishing an Event CF removes it from the calendar and detail view once caches clear.
> If you want to **retain the page but mark as cancelled**, use status + status message instead.

### 3.5 Event Calendar & Detail Pages

Three main pieces:

1. **Event Calendar / Listing component**
   - Configured on an Events page to:
     - Point to a CF folder (root for Events).
     - Define filters (region, location, category, event type, etc.).
     - Define which Event detail page template is used for links.
   - Uses CF **fields** (not folders) to filter and display events.
2. **Event Detail component**
   - Lives on the Event detail page template.
   - Reads the Event CF selected via URL or configuration and renders:
     - Full title and description.
     - Date/time range.
     - Location details (via referenced Location CF).
     - Status and status message.
     - Hero image / banner.
3. **Promotional cards and banners**
   - For hiring events or special campaigns, you can:
     - Use **Promotion CFs** (from the Careers model) to create special cards.
     - Link them to Event details via URLs or CF references.

### 3.6 Best Practices

- Keep **event status** in sync with reality; don’t delete events just to cancel them.
- Always use a **Location CF reference** to ensure consistent address/venue data.
- Use tags (event type, region, audience) to make filters meaningful.

### 3.7 References

- General CF use and delivery:
  [Delivering Content Fragments in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/content-fragments/content-fragments-delivery-feature-video-use)

------

## 4. Careers

### 4.1 Purpose

The Careers area ties together:

- Job search and detail (from Jobs).
- **Promotions** (campaigns, hiring events, specialty content).
- **Testimonials / videos** and curated content that sit around jobs.

### 4.2 Promotions Content Fragment Model

From the KT, Promotions are defined by a CF model with fields like:

- Identification & status:
  - ID / internal name.
  - Status (active/inactive).
- Display fields:
  - Title, subtitle/summary.
  - Card image + alt text.
  - Banner image + alt text.
- Date behavior:
  - Start/End dates **and/or** a **date override string** (for freeform “Fall 2026”, “Limited time” copy).
- Targeting:
  - Promotion type (e.g., “Hiring event”, “Dining”, “Hotel”).
  - Optional location references (link to Location CF).
- Details:
  - Long description, terms & conditions, link URLs.

### 4.3 Authoring Promotions

1. Go to the **Promotions CF** folder.
2. **Create > Content Fragment** using the Promotion model.
3. Fill:
   - Title, card image, status.
   - Either:
     - Start/End dates, **or**
     - A **date override text** (if the campaign shouldn’t show literal dates).
4. Link to locations, jobs, or relevant pages as needed (URL fields).
5. Publish the CF.

### 4.4 Promotion Components in Careers

Typical components you’ll see:

- **Promotions List / Search component**
  - Lists Promotions CFs based on:
    - Type (e.g., “Hiring” promotions) and/or tags.
    - Active date range or status.
  - Used on **Careers landing pages** to surface hiring campaigns.
- **Promotion Card / Banner component**
  - Renders a single Promotion CF as a hero, banner, or inline card.

### 4.5 Testimonials & Video Cards

Careers often includes **video testimonial cards**:

- Backed by:
  - A CF (or page properties) storing video title, description, thumbnail, and video URL (YouTube/Vimeo or DAM video).
- Displayed by:
  - A **video card component** configured with:
    - Reference to the CF or direct video asset.
    - Optional quote text and attribution.

### 4.6 Best Practices

- Use **Promotions CFs** for anything that may appear in more than one place (homepage, Careers, Events).
- Prefer **date overrides** only when literal dates are not appropriate; otherwise, use real start/end dates so lists can be time-based.
- Ensure alt text is always filled for images (accessibility and SEO).

### 4.7 References

- Promotions as structured content:
  [Working with Content Fragments – Concepts and Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/overview)

------

## 5. Shared Data

### 5.1 Concept

“Shared Data” refers to **central content** reused across pages and features:

- **Shared CFs** (e.g., bios, global disclaimers, benefit descriptions).
- **Location CFs** (DPLT-sourced).
- **Tags and taxonomies** that unify Jobs, Events, News, and components.

### 5.2 When to Use CFs vs. Experience Fragments

From KT:

- Use **Content Fragments** when:
  - You need structured, channel-agnostic data (bios, hours, categories, attributes).
  - Data should be reused in multiple renderings (cards, lists, APIs, etc.).
- Use **Experience Fragments** when:
  - You need a **visually-designed block** (hero, promo banner, complex layout) reused across pages.
  - Structure is more about layout + components than raw data.

### 5.3 Shared Data Examples

Common shared data patterns:

- **Biography / “Women of Hard Rock”** profiles
  - CF model with fields like Name, Role, Bio text, Image, Tags (region, LOB).
  - Rendered in cards and detail pages; reused in listings.
- **Global disclaimers & legal text**
  - Simple CF model or Experience Fragment used in footers, forms, and campaign pages.
- **Category dictionaries**
  - Lists of allowed categories for Jobs, Events, News (often reflected as tag hierarchies).

### 5.4 Tagging & Taxonomy

From Tagging & Taxonomy KT:

- Tags are used for:
  - **Filtering and facets** (job category, event type, news category).
  - **Audience targeting** and navigation.
- General guidance:
  - Use **existing tag vocabularies** (e.g., brand, LOB, region, topic).
  - Avoid creating ad-hoc tags for one-off use; prefer reusing existing categories.
  - Assign tags on:
    - CFs (Jobs, Events, News, Locations) to enable cross-cutting searches.
    - Pages (for teasers, related content, dynamic lists).

### 5.5 Authoring Steps for Shared CFs

1. Go to the shared CF folder (e.g., `Assets > Files > SHRSS > Content Fragments > Shared`).
2. Create a new CF:
   - Select appropriate model (Bio, Disclaimer, Generic Content).
3. Fill fields:
   - Structural fields (name, role, text).
   - **Tags** (brand, region, topic).
4. Publish and then reference via:
   - CF components on pages.
   - Cards / lists configured to filter by model + tags.

### 5.6 References

- CF models and management:
  [Managing Content Fragment Models](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/managing-content-fragment-models)

------

## 6. News

### 6.1 Purpose & Model

News is modeled as CFs, powering:

- **News listing pages** (with category filters, archives).
- **Article detail pages**.
- **Related articles** and sidebar lists.

### 6.2 News Content Fragment Model

From the KT:

Typical News CF fields include:

- Core:
  - Title, Subtitle.
  - Short summary / standfirst.
  - Main article body (rich text).
- Metadata:
  - Author.
  - Published date.
  - Category (news category field and/or tags).
- Media:
  - Card image (for listing).
  - Hero image (for article detail).
- Optional:
  - Related tags (topic, property, LOB).
  - External link overrides if a news item links off-site.

### 6.3 Authoring News Articles

1. Navigate to the **News CF** folder.
2. Create a **News** CF via `Create > Content Fragment`.
3. Fill:
   - Title, summary, body text.
   - Published date.
   - Category and tags.
   - Card and hero images.
4. Save and **Publish**.

### 6.4 Connecting CFs to News Pages

Depending on implementation, you typically have:

1. **News listing page**
   - Uses a **News List / Search component** that:
     - Points to a News CF folder or model.
     - Filters by:
       - Category / tags.
       - Date range for archives.
     - Displays card image, title, summary, published date.
2. **News article page template**
   - Contains a **News Content Fragment component**:
     - Reads a specific News CF based on URL or config.
     - Renders hero image, title, author, published date, full body.
3. **Category / archive navigation**
   - Category listing components that:
     - Show all categories (maybe from tags).
     - Render archive lists by year/month based on CF published date.

### 6.5 Best Practices

- Always fill **published date** – used for archive lists and sorting.
- Use **consistent categories and tags** so lists and “related news” behave predictably.
- Ensure **card image** works well at small sizes; hero image can be richer.

### 6.6 References

- Page authoring with CFs:
  [Content page authoring with Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-65-lts/content/sites/authoring/authoring/content-fragments)

------

## 7. Locations

### 7.1 Purpose & Data Sources

Locations represent **physical properties and venues**, mostly driven by **DPLT / shared location services**. They are the backbone for:

- Location pages.
- Event locations.
- Job locations.
- Cafe, hotel, and venue widgets.

### 7.2 Location Content Fragment Model

From the KT, the Location CF model typically includes:

- Identifiers:
  - Location ID / DPLT ID.
  - Brand / property codes.
- Names:
  - Formal property name.
  - Display name(s).
- Address:
  - Street, city, state/province, postal code, country.
- Attributes:
  - Type of destination (hotel, cafe, casino, live venue, etc.).
  - Type of vacation (family, nightlife, etc.).
  - Booleans: isDelivery, isVenue, isHotel, etc.
- Media:
  - Primary location image(s).
- References:
  - Linked **Venue CFs** (for specific venues within a location).

Most of the **core identity and address fields** are considered **system-of-record from DPLT** and should not be manually altered unless the process explicitly allows it.

### 7.3 Folder Structure

From KT:

- Typical path pattern:
  `Assets > Files > SHRSS > Content Fragments > Locations > <region>/<country>/<property>`

You may rename CF **titles** for author usability (e.g., property long name), but keep IDs intact.

### 7.4 Authoring Location Data

Because Locations are mostly sourced externally:

- **Do not** change core fields that are synchronized from DPLT (ID, official names, base address).
- You can often enrich:
  - **Marketing images** (hero, card).
  - **Type of destination / type of vacation** fields.
  - Boolean flags (e.g., “isVenue”, “hasDelivery”), as defined in the KT.

Whenever you update a Location CF:

1. Save your changes.
2. **Publish** the CF.
3. Validate on:
   - Location pages.
   - Job/Event listings that reference that location.

### 7.5 Location-Driven Components

Common components include:

- **Location / Property card lists**
  - Show filtered lists of locations (e.g., “Hotels in Florida”).
  - Filters based on Location CF fields (brand, region, type of destination).
- **Destination and Venues components**
  - On a property page, show its **venues** using references:
    - The Location CF’s `isVenue` or `venues` references.
- **Delivery / order widgets**
  - Depend on flags like **isDelivery** and external links stored against location or shared data CFs.

### 7.6 Best Practices

- Treat Location CFs as **system-of-record**. Make only agreed enrichments.
- Use **consistent naming** so authors can easily find the right location in picker dialogs.
- Test changes in **lower environment** when possible, especially for flags that control feature visibility (delivery, booking, etc.).

### 7.7 References

- Structured content and CF modeling:
  [Authoring Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/authoring)

------

## 8. Page Templates

### 8.1 Purpose

Page templates define:

- Page **structure** (header, footer, main layout).
- **Initial content** (pre-placed components).
- **Allowed components** in each region.
- Sometimes **style variations** (via Style System).

For SHRSS, templates cover:

- Home / landing pages.
- Standard content pages.
- News / article pages.
- Careers and Jobs pages.
- Location / property pages.
- LOB-specific microsites.

### 8.2 Authoring Using Templates

As an author, you don’t edit templates; you **use** them:

1. Go to **Sites** console.
2. Navigate to the folder where you want a page.
3. Click **Create > Page**.
4. Pick the appropriate **template**:
   - E.g., “Standard Content Page”, “News Article Page”, “Location Page”, “Careers Landing Page”.
5. Set **Title** and **Name (URL)**.
6. Open the new page and start authoring within allowed regions.

### 8.3 Template Structure & Locked Areas

From KT sessions:

- **Header and Footer** are typically built as **Experience Fragments** and locked in the template.
- Templates often include:
  - A hero region (with default hero component).
  - A main content region (layout container with allowed components).
  - Sidebar regions for navigation or lists.

> If you can’t move or delete a component, it’s likely part of the **template structure**; you can only configure it, not remove it.

### 8.4 For Template Authors / Super Authors

If you have access to define templates:

- Use the **Template Editor** to:
  - Add layout containers and components to the structure layer.
  - Configure **policies** (which components are allowed, what options they expose).
  - Set **initial content** (pre-configured components to appear on all new pages).

Public reference:

- [Templates to Create Pages that are Editable with the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/templates)

------

## 9. Media

### 9.1 AEM Assets Basics

Media (images, videos, PDFs) live in **AEM Assets** and are used across:

- Hero components.
- Cards (Jobs, Events, News, Promotions).
- Galleries and carousels.
- Background images for sections.

You access media via the **Assets rail** in the Page Editor.

- [AEM Assets videos and tutorials](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/overview)

### 9.2 Uploading & Managing Assets

- Store SHRSS media in a **logical DAM hierarchy** (by LOB, site, campaign).
- Use **clear naming conventions** and set:
  - **Title** and **Description**.
  - **Alt text** (either on the asset or component) for accessibility.
  - Tags for brand, region, LOB, etc. where helpful.

### 9.3 Image & Media Components

Core concepts:

- **Image component (Core Component)**
  - Used for most images on the site.
  - Supports:
    - **Inherit featured image** from page.
    - Direct image selection from Assets.
    - Alt text overrides.
    - Responsive renditions and lazy loading.
- **Dynamic Media (if enabled)**
  - Smart crops, dynamic renditions, and interactive viewers.

Public docs:

- [Image Component (Core Components)](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/wcm-components/image)  
- [Using Dynamic Media with AEM Sites Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/dm-with-aem-sites/dynamic-media-core-components)

### 9.4 Galleries and Carousels

From DAM & Media KT:

- **Media Gallery / Image Grid components**
  - Typically configured with:
    - A **folder path** or explicit list of assets.
    - Layout (grid, masonry, carousel).
  - Best used for:
    - Event/gallery recaps.
    - Property photo galleries.
- **Hero Carousel / Slideshow components**
  - Used for top-of-page experiences.
  - Each slide may reference:
    - An asset (image/video).
    - A CF (Promotion, Event) for text.

### 9.5 Best Practices

- Prefer **DAM assets** over uploading images directly inside components.
- Always set **alt text** for images, either on the asset or the component.
- Use **Dynamic Media** smart crops where available to ensure images look good across devices.

------

## 10. Navigation and Data Display

*(This KT ran over two days; below is the consolidated view.)*

### 10.1 Global Navigation & Footer

These are usually defined in templates using:

- **Experience Fragments** for:
  - Global header (logo, primary navigation, utility links).
  - Global footer (copyright, links, social, legal).

As an author:

- You **do not** change the structure of global nav/footer on individual pages.
- Changes are made by editing the **shared Experience Fragment**, which then updates everywhere.

### 10.2 Local Navigation & Page Structure

Components used:

- **Breadcrumbs**
  - Show the user’s path based on site hierarchy.
  - Require correct placement of pages in the Sites tree.
- **Local navigation / section menus**
  - Configured per section to:
    - Show child pages.
    - Or show a curated list of pages via manual selection.
- **Tabs / accordions**
  - Used to display multiple data sets (e.g., multi-LOB content) in a compact way.

### 10.3 Data Display Components

These are key for Jobs, Events, News, Shared Data, and Locations:

- **List / Card list components**
  - Configured to:
    - List items by **path**, **tag(s)**, or **CF model**.
    - Render as cards, simple lists, or other layouts.
  - Typical usage:
    - News cards, Event cards, Job cards, Location cards, Promotion cards.
- **Filtered tabs / Card filter components** (from Additional Components KT)
  - Provide:
    - A set of **filters (tabs)** at top.
    - Card grid below, filtered by:
      - Tags (e.g., LOB, region, category).
      - Data model (e.g., specific CF model).
  - Good for:
    - LOB-specific views (Hotel/Cafe/Casino).
    - “Explore by category” experiences.

### 10.4 Wiring Data Display to Shared Data

Most data-display components rely on:

- **CF model type** (Jobs, Events, News, Promotions, Locations).
- **Tags / taxonomy** (category, region, LOB).
- Optional **paths** (folder root) to limit scope.

From the KT sessions:

- If a listing doesn’t show expected items:
  - Verify CFs are **published**.
  - Verify **tags/categories** are set correctly.
  - Verify component **configuration**: model, root path, filters.

### 10.5 References

- Components overview:
  [Components](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/components)  
- Authoring with Core Components:
  [Authoring with Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/get-started/authoring)

------

## 11. LOB Specific Components

### 11.1 Purpose

LOB (Line-of-Business) components provide **specialized functionality** for:

- Cafes and restaurants.
- Hotels and resorts.
- Live venues and events.
- Specific campaigns (e.g., “Messy Burger” page).

They typically wrap or integrate with **external systems** (OpenTable, delivery partners, reservation systems) and rely on **Location CF** data.

### 11.2 Cafe & Delivery Components

From LOB KT:

- **Delivery widget component**
  - Uses location-related flags and potentially shared data CFs:
    - “isDelivery” flag on Locations.
    - Links to external delivery partners (Uber Eats, DoorDash, etc.).
  - Displays partner logos and “Order Now” links when available.

### 11.3 Dining Reservation / OpenTable Components

- **Reserve table / booking components**
  - Use:
    - Location or LOB-specific configuration (OpenTable restaurant IDs, URLs).
  - Often configured at **template or shared component level**, not per individual page.

### 11.4 Hotel / Microsite Navigation

- **Microsite navigation component**
  - Provides local navigation for a hotel microsite (e.g., sections like Rooms, Dining, Amenities, Offers).
  - Often uses:
    - Manual configuration of section links.
    - Or path-based listing of child pages within the hotel section.

### 11.5 Campaign-Specific Components (e.g., “Messy Burger”)

From KT:

- “Messy Burger” demo page uses a **special template and component** to highlight:
  - Campaign-specific hero and content layout.
  - Strong use of images, video, and copy.

Author guidance:

- Treat these as **fixed design patterns**:
  - You configure content (images, text, links) but do not change the underlying layout.

### 11.6 Best Practices

- Understand whether a LOB component reads from:
  - CFs (Locations, Promotions).
  - Environment variables / OSGi configs (restaurant IDs).
  - Page properties (microsite context).
- For changes that appear **“global” to that LOB**, work with the central team, not per-page overrides.

------

## 12. Additional Components

### 12.1 Overview

“Additional Components” are the supporting pieces that make pages rich and interactive:

- Buttons and button groups.
- Modals and pop-up dialogs.
- Generic card components.
- Tabbed grids and filters.
- Miscellaneous content blocks.

### 12.2 Buttons & Button Groups

From KT:

- **Button component**
  - Standard link with text, URL, and style variations (primary, secondary, etc.).
  - Can link to:
    - Internal pages.
    - External URLs.
    - Anchors on the same page.
- **Button group component**
  - Renders several buttons together (e.g., “Book Now”, “View Menu”, “Get Directions”).
  - Configuration can include:
    - Orientation (horizontal/vertical).
    - Button styles.

### 12.3 Modals & Dialogs

- Some buttons can be configured to **open modals**:
  - Modals often contain:
    - Simple text or forms.
    - Embedded Experience Fragments for richer content.

Authoring pattern:

1. Create or configure the content to appear in the modal (component or Experience Fragment).
2. Configure button to **open modal** and reference that content.

### 12.4 Generic Card Components

From Additional Components KT:

- **Card component**
  - Can be configured in different modes:
    - Image + title + text + link.
    - Variation with overlay text or icon-only cards.
  - Often used wherever there is **no specialized card** (generic promotions, information blocks).
- Authoring options typically include:
  - Image reference.
  - Title and description text.
  - CTA button text and URL.
  - Style variations (via Style System).

### 12.5 Tabbed Cards / Filter Components

(Also relevant to Navigation & Data Display)

- **Tabs / Card Filter component**
  - Provides:
    - A row of tabs (each tab tied to a filter rule).
    - A card grid filtered by current tab.
  - Filter rules are based on:
    - Tags.
    - CF types.
    - Or manual lists.

Authoring:

1. Define tabs and their filters in the component dialog.
2. Ensure content (CFs or pages) has matching tags.
3. Confirm that the root path or data source is correctly set.

### 12.6 Best Practices

- Prefer specialized components (Jobs, Events, Promotions) when available; use generic Card components for **miscellaneous content**.
- When using filters, keep tag sets **small and meaningful** so authors and visitors both understand them.
- For modals, ensure content is accessible (keyboard navigable, close buttons, focus management handled by component).

------

## 13. Putting It All Together

When authoring on SHRSS:

1. **Identify the right content type**
   - Job? Event? News? Promotion? Location? Shared content?
   - Use the corresponding **CF model** whenever it exists.
2. **Create or update the CF**
   - In the **Assets** area:
     - Use correct folder and model.
     - Fill structured fields and tags.
     - Publish.
3. **Place or configure components on pages**
   - In the **Sites** area:
     - Choose the right **page template**.
     - Use appropriate components (Job listing, Event calendar, News list, Card filter, etc.).
     - Configure them to point at the correct CF folders, models, tags, and paths.
4. **Leverage shared data and tags**
   - Reuse CFs and tags to avoid duplication and ensure consistency.
5. **Validate end-to-end**
   - Preview page, navigate through filters, and verify that lists and detail pages show expected content.

------

## 14. Core Public References Summary

Here are the most generally useful public docs for your authors:

- **General authoring**
  - [Overview of Authoring in AEM Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/aem-sites-authoring-overview)  
  - [Authoring a page in AEM Sites](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/page-authoring-overview-feature-video-use)
- **Components & templates**
  - [Components](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/components)  
  - [Core Components Introduction](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction)  
  - [Authoring with Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/get-started/authoring)  
  - [Templates to Create Pages that are Editable with the Page Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/page-editor/templates)
- **Content Fragments**
  - [Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/content-fragments)  
  - [Working with Content Fragments – Concepts and Best Practices](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/overview)  
  - [Authoring Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/authoring)
- **Assets / Media**
  - [AEM Assets videos and tutorials](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/overview)  
  - [Image Component (Core Components)](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/wcm-components/image)
- **Navigation & structure**
  - [Organizing Pages](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/sites-console/organizing-pages)