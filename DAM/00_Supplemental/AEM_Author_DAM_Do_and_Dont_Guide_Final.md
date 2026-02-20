# AEM Author DAM Do & Don’t Guide (SHRSS / Hard Rock)

*Short, opinionated rules for everyday use of AEM Assets.*

------

## 1. Folders

### Do

- **Do** upload assets into the right brand folder:
  - Cafe → `/content/dam/shrss/cafe/...`
  - Hotel → `/content/dam/shrss/hotel/...`
  - Reverb → `/content/dam/shrss/reverb/...`
  - Corporate (incl. careers) → `/content/dam/shrss/corporate/...`
- **Do** use property/location subfolders where provided:
  - `/cafe/amsterdam/en/photography`
  - `/hotel/davos/en/photography`
  - `/reverb/atlanta/en/photography`
- **Do** keep language-specific assets under `en` (or other language) consistently.

### Don’t

- **Don’t** put raw images directly under `/cf` — that branch is for Content Fragments.
- **Don’t** create new top-level folders under `/content/dam/shrss` without alignment with the DAM architect.

------

## 2. File Naming

### Do

- **Do** use descriptive filenames:
  - `hotel-davos-exterior-night-hero-2026.jpg`
  - `reverb-atlanta-rooms-king-bed-hero.jpg`
- **Do** include brand or property in the name where it helps:
  - `cafe-amsterdam-menu-spring-2026.pdf`

### Don’t

- **Don’t** keep camera or stock default names like `DSC_00123.JPG` for assets used in Sites.
- **Don’t** rely only on naming instead of tags; name + tags work together.

------

## 3. Tagging

### Do

- **Do** apply **at least** these tags when relevant:
  - `shrss/lob/<lob>` — line of business (cafe, hotel, casino, etc.)
  - `shrss/properties/<property>` — when property-specific
  - `shrss/country/<country>`
  - `shrss/category/<category>` — logo, lifestyle, rooms, suites, awards, philanthropy, etc.
- **Do** use `shrss/news-categories` or `shrss/event-categories` for news/event-related assets.
- **Do** ask your author lead or DAM architect if you’re unsure which tag to use.

### Don’t

- **Don’t** create new `shrss` tags unless you’ve been explicitly told you can.
- **Don’t** guess between near-duplicate tags (e.g., `northernindiana` vs `northern-indiana`) — ask which is correct.
- **Don’t** ignore tags; they are required for searchability and reuse.

------

## 4. Metadata Fields

### Do

- **Do** fill in **Pdf Title** on PDFs with something meaningful:
  - `Hard Rock Cafe Amsterdam Menu - Spring 2026`
- **Do** optionally fill **Location** on images when it adds value:
  - `Davos Lobby` or `Reverb Atlanta Studio`

### Don’t

- **Don’t** assume that metadata replaces tags; both matter.
- **Don’t** leave mandatory metadata fields blank if they’re added in the future (e.g., Usage rights).

------

## 5. Approvals, Changes, and Cleanup

### Do

- **Do** create new versions when updating images that are already used on live pages.
- **Do** check references (Reference Search) before deleting or moving an asset.
- **Do** notify the appropriate site owner if you change a frequently used asset (hero images, homepage graphics, etc.).

### Don’t

- **Don’t** delete assets you didn’t upload if you’re not sure who uses them.
- **Don’t** move large sets of assets between folders without coordinating with the DAM architect or a developer.

------

## 7. When to Ask for Help

Reach out to your **DAM architect** or **author lead** if:

- You can’t find the correct tag for a new property or venue.
- You’re not sure where a new type of asset should live.
- You’re planning to bulk upload or bulk move assets.
- You suspect a tag or folder structure is wrong or confusing.

*End of Do & Don’t Guide.*
