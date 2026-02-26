# Session Notes — Locations, Day 2 — 2026-02-24

**Session:** Locations, Day 2  
**Date:** February 24, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260224_130151  
**Duration:** 1h 50m 12s  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context

- Follow-ups from News session: Edwin’s question on CF list path for category listing—path determines *child level* displayed (e.g. year folders if path ends at EN under news). Daniela demonstrated on stage; Edwin confirmed that covered it. News page template/name field to be covered in Page Templates session.
- Delivery widget follow-up: Hard Rock Casino Rockford showing in delivery list—line of business in DPLT is Cafe, so it appears. Delivery widget shows only locations with line of business = Cafe and delivery checked. Lisa: casino misclassified as cafe; need right contact. Kerry: DPLT team (Vipul Patel); classifications must come from DPLT; if misclassified, take to Vipul’s team. Daniela: once DPLT fixes line of business, location should drop from list even if delivery info remains.
- Locations Day 2 agenda: booking widget, booking offers, find a location, Google Map, location list. Continued from Day 1 (computer issues).

---

## What was covered

1. **Category listing (news)** — Content fragment list path: last item in path = parent; component shows *children* of that parent (e.g. years if path = …/news/corporate/EN).
2. **Delivery widget** — Driven by line of business (Cafe) and delivery partners in location CF. Misclassification = DPLT fix (Vipul’s team).
3. **Booking widget** — Same as Book Now; modal vs on-page; group name, destination, destination URL, destination value (e.g. 59391); rooms/adults/children. Rick: black border on modal; can we match booking widget size/background to modal? Daniela: note as gap (configurable). Lisa: destination value from where? Rick: Senex/Vizergy; in booking links (e.g. hotel=68…). Lisa: do authors need that number? Rick: once set they don’t change; may need for restore if someone changes it. Daniela: casino booking not finalized (pre-pause); Vizergy migrated values in dialog.
4. **Booking widget — add (rooms, adults, children)** — “Add” = add more groups/destinations in dialog; order = display order. Lisa: adding a *different* field (e.g. balcony)? Daniela: would require development (field type, UI, parameter passing; booking engine side too).
5. **Booking offers** — Group name, default destination, booking URL, arrival/departure dates (optional), booking window start/end (display only). Rick: hide booking window section? Daniela: tried; window still present, fields blank; hide label = potential gap. Lisa: unchecked = no user date fields; checked = user can pick dates; booking window always visible. Rick: newer logic (booking window constrains calendar) may be in component; Daniela: display-only in what we saw.
6. **Find a location** — Label, placeholder, search button text, view all text, empty input message, page path (search and view all both go to this path). Lisa: change background color? Daniela: currently fixed in code; change would need code update for author-configurable background.
7. **Google Map** — Author sees “oops, something went wrong” in author/view as published when domain not whitelisted; publisher works. API key in env vars (dev); authors can’t change. Element ID, radius, center lat/long, zoom (e.g. up to 15), style JSON (map look), map type (default, area guide, franchise). Map data: description, area guide header (area guide only), regions (group title, region, featured countries), hide other locations, location addresses (area guide), markers (cafe, casino, hotel, etc.), search/filter/results (find your location, placeholder, result count, no results text). Gonzalo (yesterday): regions dropdown blank in prod—today fixed (permissions/generic list). Gonzalo: North America first in config but Central America on top on prod—order in dialog = display order; republish page; if regions were blank, author properly (Lucas: ACS Commons on prod). Lisa: filter map not in config but filters showing? Daniela: filter map adds filters on map; made copy to demo; no results vs no locations—different messages. Lisa: carousel dots not centered (Rick too)—Daniela noted for fix.

---

## Questions, comments, and answers (captured)

*See **Locations_Day_2** sheet in tracker.*

- CF list path (category listing): path = parent; children displayed; Edwin confirmed.
- Delivery: Rockford casino = cafe in DPLT; Lisa to take to Vipul’s team.
- Booking modal: black border/size match = gap (configurable).
- Destination value: from migration/Vizergy; authors may need for restore; casino booking not finalized.
- Booking widget new field (e.g. balcony): development required.
- Booking offers: hide booking window? Label/field hide = gap; window always visible today.
- Find a location background color: code change for author control.
- Google Map: whitelist for author view; regions dropdown = permissions (Template Authors + read on generic list); North America order = republish + ensure regions authored.
- Filter map vs regions: filter map adds filters on map; regions order = dialog order.
- Media gallery / image gallery: covered in Media session.

---

## Product Director — own questions

1. **Governance:** Who owns DPLT classification (line of business) and who is the SHRSS contact for misclassification (e.g. casino as cafe)?
2. **Authoring:** Single checklist for “new location from DPLT”: verify line of business, delivery, title, then publish?
3. **Gap:** Configurable modal background/size for booking widget; hide booking window (and label) in booking offers.
4. **Permissions:** Which groups need read/write on generic list “regions” for Google Map dropdown?
5. **Gap:** Author-configurable background color for Find a location component.

---

*End of session notes. All Q&A rows in **Locations_Day_2** sheet.*
