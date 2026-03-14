# Presentation Image Inventory — Unlocking Adobe AI with AEMaaCS for SHRSS

**Task:** TASK_GENERATE_SHRSS_AEM_AI_PRESENTATION_COLLATERAL.md  
**Template:** Adobe_Presentation_Starter-Deck_2025_Layouts_for_Agents.md  
**Blueprint:** Presentation_Blueprint_Unlocking_Adobe_AI_with_AEMaaCS_for_SHRSS.md  
**Output dir:** `Documentation/Generated/Presentation/Images`  
**Naming:** `NN_Company_Short_Description.ext` (e.g. `01_Hard_Rock_Logo_Globe_Cafe.png`)

---

## 1. Blueprint × Template Mapping

| Slide | Blueprint title | Layout (template) | Theme | Image placement | Agent image prompt / instruction |
|-------|-----------------|-------------------|-------|------------------|----------------------------------|
| 01 | Title & Objectives | Title slide Image right | Dark | Right ~60% | Digital globe, neon icons (hotel, cafe, guitar, shopping cart), Adobe red + Hard Rock purple |
| 02 | Why AI, Why Now | Image on right 1/2 | Dark | Right 50% | Bottleneck breaking into stream of data, red/blue streaks |
| 03 | Adobe AI Ecosystem | Title and content, 3 columns | Light | Icons per column | AEM, Firefly, Commerce icons (or pen, vault, cart) |
| 04 | AEM Sites – AI Assistant | Image on right 1/2 | Light | Right 50% | AEM AI Assistant UI / dashboard mockup, magic wand |
| 05 | AEM Assets & DAM | 2×2 Image grid | Dark | Four cells | (1) Hard Rock burger moody (2) same burger beach (3) metadata/tags visual (4) AEM Assets dashboard |
| 06 | Adobe Commerce AI | Title and content | Light | Bottom/right | E-commerce data flow, shopping cart + profiles, analytics |
| 07 | Next Steps – Phase 2 | Buckets (3) | Dark | Icons above buckets | Sticky note, bullseye, rocket (minimalist neon) |

---

## 2. Image Search Priorities (per task)

- **Hard Rock:** Highest value = logo + corporate branding. Use: hardrock.com, cafe.hardrock.com, hotel.hardrock.com, entertainment.hardrock.com, careers.hardrock.com, reverb.hardrock.com.
- **Adobe:** Highest value = product(s) featured on slide (AEM, Firefly, Experience Platform, Agent Orchestrator, Commerce). Second = Adobe-branded/corporate. Use: business.adobe.com (AEM, Firefly, AEP, Agent Orchestrator), experienceleague.adobe.com.

---

## 3. Target list for 10 candidate images

Candidates should support the 7 slides alone or combined; flexibility for an agent to generate final art.

| # | Slide(s) | Company | Description (search intent) | Filename example |
|---|----------|----------|-----------------------------|-------------------|
| 1 | 01 | Hard_Rock | Logo or brand mark (globe/cafe/hotel) | 01_Hard_Rock_Logo_Global_Brand.png |
| 2 | 01 | Adobe | Corporate or product (AEM/Experience Cloud) | 01_Adobe_Experience_Cloud_Red.png |
| 3 | 02 | Adobe | Abstract tech/velocity/digital transformation | 02_Adobe_Digital_Velocity_Data_Stream.png |
| 4 | 03 | Adobe | AEM product icon or UI | 03_Adobe_AEM_Product_Icon.png |
| 5 | 03 | Adobe | Firefly product icon or imagery | 03_Adobe_Firefly_Icon.png |
| 6 | 04 | Adobe | AEM Sites / authoring UI or AI Assistant | 04_Adobe_AEM_Sites_UI_Assistant.png |
| 7 | 05 | Hard_Rock | Food/venue (burger, cafe, high-end) | 05_Hard_Rock_Cafe_Burger_Table.png |
| 8 | 05 | Adobe | AEM Assets / DAM dashboard or Smart Tags | 05_Adobe_AEM_Assets_Dashboard.png |
| 9 | 06 | Adobe | Commerce / shopping / analytics visual | 06_Adobe_Commerce_Shopping_Data.png |
| 10 | 07 or multi | Hard_Rock | Entertainment/venue (guitar, neon, nightlife) | 07_Hard_Rock_Entertainment_Neon.png |

---

## 4. Layout size reference (from template)

- **Title slide Image right (Slide 8/10):** Right image placeholder ~60% width.
- **Image on right 1/2 (Slide 16/20):** 50/50 split; right = image.
- **2×2 grid (Slide 50/54):** Four equal placeholders.
- **Title and content:** Optional bottom/right contextual graphic.
- **Buckets:** Icon/small graphic above each bucket.

Images will be resized/cropped by the user or Gemini to fit; candidates should be high quality and on-brand.

---

## 5. Source URLs

**Adobe:**  
https://business.adobe.com/products/experience-platform/agent-orchestrator.html  
https://business.adobe.com/products/experience-manager/adobe-experience-manager.html  
https://business.adobe.com/products/firefly-business.html  
https://business.adobe.com/products/experience-platform/adobe-experience-platform.html  
https://business.adobe.com/  
https://experienceleague.adobe.com/en/home  

**Hard Rock (SHRSS):**  
https://www.hardrock.com/  
https://careers.hardrock.com/  
https://reverb.hardrock.com/  
https://entertainment.hardrock.com/  
https://hotel.hardrock.com/  
https://cafe.hardrock.com/  

---

## 6. Completion (2026-03-13)

- **Collected:** 10 candidate images in `Documentation/Generated/Presentation/Images/`.
- **Hard Rock (9):** From hardrock.com and cafe.hardrock.com via Playwright: logos (3), hero, cafe food, Rock Shop, hotel check-in, entertainment promo, cafe event.
- **Adobe (1):** Adobe logo (auth.services.adobe.com). business.adobe.com and www.adobe.com returned `ERR_HTTP2_PROTOCOL_ERROR` in browser; AEM/Firefly/Commerce product imagery could not be collected. User may add from those sources manually.
- **Manifest:** See `Documentation/Generated/Presentation/Images/README.md`.
