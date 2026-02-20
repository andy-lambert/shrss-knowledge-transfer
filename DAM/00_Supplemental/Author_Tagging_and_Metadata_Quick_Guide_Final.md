- # SHRSS Author Tagging & Metadata Quick Guide

  *Primary audience: AEM Sites/Assets authors at SHRSS/Hard Rock*
  *Goal: Make it fast and safe to upload, tag, and maintain assets.*

  ------

  ## 1. Where Should I Store My Assets?

  Always upload into `/content/dam/shrss`, under the right **brand and property**.

  ### 1.1 Brand Folders

  | Brand/site        | Folder root                    | Example path                                          |
  | ----------------- | ------------------------------ | ----------------------------------------------------- |
  | Cafe              | `/content/dam/shrss/cafe`      | `/content/dam/shrss/cafe/amsterdam/en/photography`    |
  | Hotel             | `/content/dam/shrss/hotel`     | `/content/dam/shrss/hotel/davos/en/photography/media` |
  | Reverb            | `/content/dam/shrss/reverb`    | `/content/dam/shrss/reverb/atlanta/en/photography`    |
  | Corporate         | `/content/dam/shrss/corporate` | `/content/dam/shrss/corporate/careers/en/photography` |
  | Content Fragments | `/content/dam/shrss/cf`        | `/content/dam/shrss/cf/locations/europe/france`       |
  
  **Do**
  
  - Use the **brand folder** that matches the site/page.
  - Use the **property subfolder** where available (e.g., `amsterdam`, `davos`, `atlanta`).
  - Use `en` and `photography`/`logos` subfolders consistently.
  
  **Don’t**
  
  - Don’t add images to `/cf` — that branch is for **Content Fragments**.
  
  ------

  ## 2. How Do I Tag Assets Correctly?

  Tags live in the `shrss` namespace. You apply them in the asset’s **Properties → Basic → Tags** area.

  ### 2.1 Minimum Tagging Standard (per asset)

  For all major brand assets (cafe, hotel, reverb, corporate):

  1. **Line of business (LOB)**
     - Example:  
       - `shrss/lob/cafe`  
       - `shrss/lob/hotel`  
       - `shrss/lob/casino`  
       - `shrss/lob/entertainment`
  2. **Property (if property-specific)**
     - Example: `shrss/properties/amsterdam`, `shrss/properties/davos`, `shrss/properties/atlanta`
  3. **Country**
     - Example: `shrss/country/netherlands`, `shrss/country/switzerland`, `shrss/country/united-states`
  4. **Category**
     - Example:  
       - `shrss/category/logo`  
       - `shrss/category/lifestyle`  
       - `shrss/category/rooms` / `suites`  
       - `shrss/category/awards` / `philanthropy`
  
  > **Rule of thumb:** If you can’t find a good tag, **ask** the DAM architect or your author lead rather than creating a new one on your own.

  ------

  ### 2.2 Common Tagging Patterns (Examples)

  #### A. Cafe hero image (e.g., Amsterdam exterior)

  - **Folder:** `/content/dam/shrss/cafe/amsterdam/en/photography`
  - **Tags:**
    - `shrss/lob/cafe`
    - `shrss/properties/amsterdam`
    - `shrss/country/netherlands`
    - `shrss/category/lifestyle` or `exterior-shots`
  
  #### B. Hotel room shot (Davos)

  - **Folder:** `/content/dam/shrss/hotel/davos/en/photography/media`
  - **Tags:**
    - `shrss/lob/hotel`
    - `shrss/properties/davos`
    - `shrss/country/switzerland`
    - `shrss/category/rooms` or `suites`
  
  #### C. Corporate/careers headshot

  - **Folder:** `/content/dam/shrss/corporate/careers/en/photography`
  - **Tags:**
    - `shrss/brands/hri` or relevant brand
    - `shrss/category/headshots`
    - `shrss/category/careers` (if used)
  
  #### D. News/press release photo

  - **Folder:** close to corporate photography root
  - **Tags:**
    - `shrss/news-categories/press-releases` or `hard-rock-news`
    - `shrss/lob/<relevant-lob>`
    - Optional: property/country if specific to a location
  
  ------

  ### 2.3 Tags to Use Carefully

  - Tags with **typos or odd encoding** (e.g., `guadalaraja`, `_x0032_4k-boutique`, `lobby-bar-gmt_x002b_1`, names ending in `-`) may be slated for cleanup.
  - If you see **two very similar tags** (e.g., `northernindiana` vs `northern-indiana`), ask which one is officially approved.
  
  ------

  ## 3. How Do I Use Metadata Fields?

  Most business meaning is in **tags** today. Metadata fields are mostly **technical** plus a few content fields.

  ### 3.1 Images (JPEG/TIFF)

  On **Properties → Metadata → Basic tab**, you will commonly see:

  - **Width** (read-only)
  - **Height** (read-only)
  - **Location** (free text)
  
  **What you should do**

  - Use `Location` only if it’s **useful for search** (e.g., “Davos Lobby”).
  - Don't rely on `Location` alone to indicate property/country — always use **tags** for that.
  
  ### 3.2 PDFs

  - **Pdf Title**: Enter a clear title that makes sense in search results.
    - Example: `2026 Hard Rock Cafe Amsterdam Menu - Spring`
  
  ### 3.3 Videos

  - Fields like **Size, Duration, Bitrate, Video Codec** may appear.
  - These are generally technical; you usually **don’t need to edit them**.
  
  **Reminder**

  - If new fields appear later (e.g., Usage rights, Owner), they’ll be documented and communicated separately.
  - When in doubt, **ask your author lead or DAM architect** before leaving important required fields empty.
  
  ------

  ## 4. Author Do / Don’t Checklist (Daily Use)

  ### 4.1 Folders

  - **Do**
    - Upload assets into the correct **brand + property** folder.
    - Use `en/photography` or `en/logos` patterns consistently.
  - **Don’t**
    - Don’t put raw images in `/cf` (that area is for Content Fragments).
  
  ### 4.2 Names
  
  - **Do**
    - Use descriptive filenames: `reverb-atlanta-rooms-king-bed-hero.jpg`
  - **Don’t**
    - Don’t leave camera-generated names like `DSC_1234.JPG` for assets that will be searched and reused.
  
  ### 4.3 Tags
  
  - **Do**
    - Apply at least **LOB + property + category** where relevant.
  - **Don’t**
    - Don’t create new tags unless you’re explicitly allowed to.
    - Don’t guess between near-duplicate tags; ask which one is correct.
  
  ### 4.4 Metadata
  
  - **Do**
    - Fill in `Pdf Title` for PDFs.
    - Use `Location` on images if it helps others search.
  - **Don’t**
    - Don’t assume metadata fields replace tags; **you need both**.
  
  ------
  
  ## 5. Quick 5-Step Upload Flow
  
  1. **Pick the right folder** (brand + property + language).
  2. **Upload** your asset(s).
  3. Open **Properties → Basic**:
     - Add tags: `lob`, `property`, `country`, `category`, plus news/event tags if applicable.
  4. Open **Metadata tab**:
     - For PDFs, fill `Pdf Title`.
     - For images, optionally fill `Location`.
  5. Save and, if used on a page/CF, ensure references are **created or updated**.
  
  *End of author quick guide.*
