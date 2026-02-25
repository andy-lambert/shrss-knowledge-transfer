# Session Notes — Careers — 2026-02-12

**Session:** Careers  
**Date:** February 12, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260212_130224-Meeting Recording  
**Duration:** 1h 53m 20s  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context

- **KT calendar / question backlog:** Lucas shared Confluence KT calendar (content authoring, technical enablement, adoption, platform expansion). Questions not in-session will be parked in question backlog and moved to the right agenda; many will feed gap analysis / platform expansion (last two weeks).
- **Publish delay / jobs:** Andy provided update: stage publish delays under investigation; support ticket; indexing job may have been slow. **Gonzalo:** Manual job CF—create, publish, not showing on jobs page; other CFs work. **Gonzalo:** Workday sync “get all job IDs” includes manual jobs (is not API data); sync deletes them in ~30 min. Andy: team aware; email with recommendation coming; will use tech sync (Tue/Thu) to drill in.
- **Today’s focus:** Careers-website components—promotions (hiring events), video card (testimonials), video component, card (icon variation). Then any specific careers pages.

---

## What was covered

1. **Promotions content fragment** — ID and name (required), title, status (active/inactive), card image + alt, banner image (required), date format (date only, with start/end time, or **override text** e.g. “every Tuesday 12:50”), promo types (loyalty/slot—casino-specific), description, location/venue, **location override text**, CTAs, LD JSON. Model was built for casino; used for careers hiring events for override capability. **ID:** Author-entered unique ID; used by content fragment card to show one promotion; no path picker—must copy ID from CF. Uniqueness validated on save. **Gap:** Don’t want ID; want source/path picker (Gonzalo); authors can’t manage IDs at scale.
2. **Content fragment card (no filter)** — To get a single promotion on page without filter: enter promotion ID. No way to pick from folder/path. **Promotion search** = promotions only; has filters + search bar; can’t remove search; if all filters removed, bar still shows (gap). Filter options (category, venue, date range) hardcoded in component; author can’t manage (gap). **Single folder path** only (can’t pick two folders). **Content fragment card list** = events/news only today; gap = add promotions so list/carousel without filter+search.
3. **Promotions vs events** — Events: DPLT location only; no date override. Promotions: location override, date override. Hiring events use promotions for that reason. Events have one detail page + event ID; promotions = create open page and link from CF. If events had override fields, could use events for hiring events.
4. **Promotion dates** — Start/end date and time = **display only**, not scheduling. Schedule = “now” or “later” (activation date) in Manage Publication. Edit after schedule: Daniela to confirm if edit keeps schedule (to test).
5. **Promo types** — In content fragment model; add options = model editor (permissions); component dropdown = dev.
6. **Image / card** — Image position tab on image components (desktop/tablet/mobile). In promotion search (list), no per-row image position; crop outside or use rendition (DAM session gap).
7. **Job components on other sites** — Job listings (and other components) are global; can use on hotel/casino pages; theme drives styling. Still **one root path** (gap).
8. **Promotion detail page** — No promotion detail template; open page + link in CF. Daniela to show casino example from integration env. Banner image in CF = for when promotion has its own page (casino use).
9. **Video card** — Thumbnail, external URL (DAM file, YouTube, Vimeo), or third party (YouTube/Vimeo with video ID). **Width** = modal size (number, no “px”). **Third party** gives fixed/responsive, aspect ratio, loop, autoplay, mute; **external URL** does not—gap. Thumbnail specs needed (Lisa). Styling: none/black/white; white description display issue (Daniela to check). Video card **not** in card carousel/hero carousel allowed components—gap.
10. **Card (icon variation)** — Icon variation used on careers; responsive breakpoints = manual per viewport (gap).
11. **Diversity / executives (careers vs hardrock.com)** — Same content; experience fragment = update once, same styling on both. Content fragment = same content, can style differently per site. For “exact same,” use experience fragment.
12. **Hide component** — Layout → Hide component: still in tree, still in DOM/crawled (Mayte). Not like Sitecore “disable” where it’s not rendered. **Gap:** Store components “disabled” without rendering for reuse (evergreen swap).
13. **Locations (careers vs brand)** — Careers locations page = accordion/text (migrated); brand = map component linked to DPLT CFs. Can copy map component to careers page. Mayte: want all location listings from DPLT so one source; no manual maintenance.

---

## Questions, comments, and answers (captured)

*See **Careers** sheet in SHRSS Adobe KT Session Follow-Up Tracker.*

- Manual job CF not showing on publisher; Workday sync deleting manual jobs (is not API data). Andy/Gonzalo follow-up; tech sync.
- Promotion ID: author-made, unique; no dropdown/path—copy from CF. Gap: source/path picker; don’t enhance ID (Mayte).
- Promotion search: filters + search always; can’t remove; filter options hardcoded; single path. Gaps.
- Content fragment card list: add promotions as type so list without filter (gap).
- Events location = DPLT only; promotions = free text override. Events without DPLT location = gap.
- Promo types: model vs component; who can add (permissions).
- Start/end date in promotions = display only; schedule = activation.
- Edit scheduled CF: confirm schedule preserved (Daniela to test).
- Image position: on image components; not on list; rendition/crop = DAM gap.
- Job listings on other sites: works; theme; still one path (gap).
- Promotion detail: no template; open page + link; casino example to come.
- Video card: external URL vs third party options; thumbnail specs; hide = in DOM; video card not in carousel—gaps.
- Card responsive: manual per breakpoint—gap.
- Experience fragment vs content fragment (same content vs same look).
- Hide component = still rendered; need “store but don’t render” for reuse—gap.
- Locations: copy map component; DPLT as single source for all location listings.

---

## Product Director — own questions and points of clarification

1. **Governance — promotion IDs and filter options:** If we keep promotion ID for now, who owns the list of IDs (e.g. HE1, HE2) and how do we avoid collisions across authors? For filter options (category, venue, date range), what is the process to add or change options (dev ticket, generic list, permissions)?
2. **Authoring — hiring events end-to-end:** Single checklist: create promotion CF → where to use it (card by ID vs promotion search) → create detail page if needed → link from CF → what to publish and in what order. Include when to use events CF vs promotions CF.
3. **Tagging:** Do promotions use tags for filtering or only folder path? If we add “promotions” to content fragment card list, will it support tag-based selection like events?
4. **Gap priorities for careers go-live:** Which of today’s items (ID vs path picker, filter/search removal, card list for promotions, video card in carousel, thumbnail specs, hide vs disable) are in scope for careers vs deferred to platform expansion?
5. **Permissions:** Who can edit the promotions content fragment model (e.g. add promo types) and who can edit the promotion search component configuration (e.g. filter labels)? Admin-only or roles?

---

*End of session notes. All Q&A rows are in the **Careers** sheet of the tracker.*
