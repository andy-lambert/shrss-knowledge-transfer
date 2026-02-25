# Session Notes — Locations — 2026-02-23

**Session:** Locations  
**Date:** February 23, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260223_130200 (Part 1)  
**Duration:** 49m 15s (Part 1)  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context

- Location content fragments from DPLT. Title in CF = location ID by default; can be changed; recommend bulk metadata update to property legal name (or chosen field). Read-only fields = DPLT; editable = image, type of destination, type of vacation, is delivery (cafes), delivery partners, is venue + venue CF (hotels).
- Delivery widget (cafe): delivery partners from location CF. Links open in new tab. Image field in location CF = used in destinations and venues component (e.g. Hard Rock Hotel Cancun). Same component on find-a-venue and destinations pages. Lisa: image specs for that component. Rick: image on destinations too? Yes, same component.
- Destination search and filters: find a venue vs destinations = different variation. Sort by = meeting room, max capacity, total square feet, guest rooms (from venue CF). Regions = North America, etc., from location CF data. New field (e.g. meeting room view) = update venue CF model + add to component dialog + front-end component update—gap (Mayte: overcomplicated; need optimized way). Lisa: filters also hard-coded? Same concept. Gonzalo: regions filter on hardrock.com prod not working—different component (Google Map). Lucas: SHRSS documents gaps; Confluence questions feed funnel; Adobe doesn’t document SHRSS gaps.

---

## What was covered

1. **Location CF** — DPLT; title = location ID; bulk update to legal name etc. Editable: image, destination/vacation type, is delivery, delivery partners, is venue, venue CF ref.
2. **Delivery** — Cafe; author checks “is delivery” and adds partners; widget on delivery page.
3. **Destinations and venues** — Location image from CF; venue CF for meeting rooms, capacity, etc. Sort by = venue CF fields. New field = model + component + front end—gap.
4. **Regions** — From location CF; component config. Filters/sort by = hard-coded to current venue fields.
5. **Gap documentation** — SHRSS documents gaps; questions/needs on Confluence feed that; Adobe shows framework, doesn’t build gap list for SHRSS.

---

## Questions, comments, and answers (captured)

*See **Locations** sheet in tracker.*

- New location from DPLT: is delivery = author manually checks.
- Image: hotels; destinations and venues component; specs to Confluence.
- Links in delivery: open in new tab.
- New sort-by or filter field: CF model + component dialog + front end—gap; Mayte: document.
- Regions in prod (hardrock.com): Google Map component = different; cover when covering Google Map.
- Gap list: SHRSS to document; Confluence = questions/needs.

---

## Product Director — own questions

1. **Governance:** Who maintains location CF data when DPLT updates? Who can add new “sort by” or filter fields (model + component)?
2. **Authoring:** When new location arrives from DPLT, checklist: bulk update title? Set image, delivery, venue as needed?
3. **Tagging:** Do locations use tags for filtering in this component or only DPLT/region data?
4. **Gap analysis:** “Optimized way” to add venue/location fields—configurable list? Author-managed options?
5. **Permissions:** Who can edit location and venue CF models and component configuration?

---

*End of session notes. All Q&A rows in **Locations** sheet.*
