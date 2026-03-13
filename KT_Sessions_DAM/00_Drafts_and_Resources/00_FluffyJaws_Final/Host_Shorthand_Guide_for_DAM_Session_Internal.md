- # Host Shorthand Guide – SHRSS DAM Session (Internal Only)

  *Keep this on a second monitor. Bullets = key points, prompts, and decisions to capture.*  

  ------

  ## 0. Open & Frame (0–5 min)

  - **Goal pitch (short):**
    “Today is about how we **actually use** the DAM: folder structure, tags, metadata, and day-to-day operations — and capturing what we want to change in the next iteration.”
  - **Key outcomes:**
    - Shared understanding of **current structure**.
    - Agreement on **“golden path”** for authors (folder + tags).
    - Short list of **cleanup items + schema enhancements**.

  ------

  ## 1. DAM Structure Under `/content/dam/shrss` (5–15 min)

  **Key points**

  - Top-level: `cafe`, `cf`, `corporate`, `hotel`, `reverb`, `training`.
  - `cf` = content fragments; **not a general file dump**.
  - `training` = sandbox, not production.

  **Ask**

  - “Does everyone agree that assets for [cafe/hotel/reverb/corporate] should live under these brand roots?”
  - “Is anything in `/training` currently used in production or close to it?”

  **Decisions to capture**

  - ✅ Confirm **no production assets in `/training`** (or list exceptions to move).
  - ✅ Confirm **no new top-level folders** without DAM architect approval.

  ------

  ## 2. Tagging Strategy – `shrss` Namespace (15–30 min)

  **Key branches to show**

  - `shrss/lob` → line of business.
  - `shrss/properties` → properties/cities.
  - `shrss/country` → countries.
  - `shrss/category` → imagery/content categories.
  - `shrss/news-categories`, `shrss/event-categories`.
  - `shrss/venues-and-branded-experiences`, `shrss/brands`.

  **Known issues to mention briefly**

  - Typos: `guadalaraja` vs `guadalajara`, `northernindiana` vs `northern-indiana`.
  - Encoded names: `_x0032_4k-boutique`, `lobby-bar-gmt_x002b_1`.
  - City `wroclaw` under `country`.

  **Golden-path pattern to propose**

  - For any brand asset:
    - `lob + property + country + category` (+ news/event category when relevant).

  **Ask**

  - “If we say ‘minimum tags = lob + property + country + category’, does that work for you?”
  - “Which branches are **author-facing** vs. **admin-only**?”

  **Decisions to capture**

  - ✅ Minimum tag set for authors.
  - ✅ Who approves **new tags** and how requests are made.
  - ✅ Which branches (e.g., `lob`, `properties`, `country`, `category`) are the **primary focus**.

  ------

  ## 3. Metadata Schema – `shrssmetadataschema` (30–40 min)

  **Key points**

  - Current schema = mostly **technical**:
    - Image: Width/Height, optional Location.
    - PDF: Pdf Title.
    - Video: Size, Duration, Bitrate, Codec.
  - Very little business metadata (no rights, owner, campaign, etc.).
  - Business context currently lives mostly in **tags**, occasionally in spreadsheets.

  **Ask**

  - “When you’re deciding if an image is safe to use, where do you look now?”
  - “What’s the biggest metadata pain point today — rights, owner, or something else?”

  **Decisions to capture**

  - ✅ Top **2–3 business fields** to add first (e.g., Usage rights, Content owner, Primary brand).
  - ✅ Whether these should be **global** or **folder-specific** (e.g., careers vs. general marketing).

  ------

  ## 4. Operations & Governance (40–50 min)

  **Key points**

  - Authors should:
    - Upload under proper brand + property + language.
    - Tag at minimum with `lob + property + country + category`.
    - Use versioning and Reference Search before deleting/moving.
  - DAM Architect:
    - Owns folder structure + tag governance + metadata roadmap.
  - Author leads:
    - Train their teams; funnel changes/requests.

  **Ask**

  - “What’s the current process when a new property opens or a new campaign launches?”
  - “Where do authors feel most uncertain today – folder choice, tags, or metadata?”

  **Decisions to capture**

  - ✅ RACI for:
    - Folder changes.
    - New tags.
    - Metadata changes.
  - ✅ Agreement to use/update **Author Quick Guide** and **Do/Don’t** as the canonical rules.

  ------

  ## 5. Dynamic Media & Future Work (50–55 min)

  **Key points**

  - DM provisioned but **not** used in production yet.
  - We can still **design the DAM** so DM adoption later is smooth.

  **Ask**

  - “What types of content would we want dynamic renditions or smart crops for first?”
  - “Is DM adoption a priority in the next 6–12 months?”

  **Decisions to capture**

  - ✅ Is there a **DM discovery/POC** in the next cycle?
  - ✅ Any folder/tag conventions we should enforce now to help later (e.g., `hero` image patterns)?

  ------

  ## 6. Wrap & Backlog (55–60 min)

  **Recap out loud**

  - “Here’s what we agreed on for **folders**, **tags**, and **metadata**.”
  - “Here are the top **cleanup items** and **enhancements** we’ll take into the backlog.”

  **Backlog buckets**

  - Tag cleanup (typos, duplicates, encoded names).
  - Metadata schema enhancements (rights, owner, etc.).
  - Folder cleanup (move content out of `/training`, normalize patterns).
  - Author enablement (update quick guide, record a short walkthrough).
  - Potential Dynamic Media POC.

  ------

  *Use this cheat sheet to keep the session moving and ensure you always end sections with a decision or a clearly logged follow-up.*
