# Session Notes — Events — 2026-02-11

**Session:** Events  
**Date:** February 11, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260211_130309-Meeting Recording  
**Duration:** 1h 55m 18s  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context

- Session opened with **Confluence Q&A process**: Adobe asked for more time to review Jobs questions; onshore will review before offshore; highlight rows for follow-ups; add follow-up questions to same row. **Question backlog** page for questions that belong to other sessions (e.g. video testimonials); questions will move to the right agenda when that topic is covered.
- **SHRSS-assigned questions** (TJ, Shoab): Scott to take offline; Confluence tagging may be missed—nudge via Webex/other.
- **Events focus:** Event content fragments, event calendar component, event detail page. Folder structure: line of business → property → language → year → month → events (ease of authoring). New CF editor will default to “old” editor via support ticket (new editor has rendering differences). Location reference from DPLT (content fragment–based); categories from Event Categories tags.

---

## What was covered

1. **Event content fragment** — Title, start/end date and time (end date optional if same as start), banner image + alt, detail-page image (required), event status, event status message, description, additional detail, CTA links (default = link to event detail page), categories (tags), location reference, featured checkbox, event ID (read-only, for URL / duplicate prevention). Publish CF to see on calendar.
2. **Event calendar component** — Content fragment folder path (single path); event page base path for detail links. Filters: region, location (roll-up from CFs in path). Calendar shows cards; default CTA = “more info” to detail page. Featured events appear first for the month.
3. **Event detail page** — Single page template; event detail component; content populated by event ID in URL. Default hero; banner image in CF overrides. Author configures default hero, error message when no event.
4. **Publishing** — Publish CF for new/updated event to appear; calendar page must also be published (once per calendar). View as published (author) shows CF changes after CF publish; publisher can have delay (Gonzalo’s issue; Andy investigating failed publish logs).
5. **Unpublish** — Unpublish CF removes event from calendar; detail URL then shows configured “no events” message (user cannot see content). Daniela confirmed behavior.
6. **Hiring events (careers)** — Use **promotions** content fragment model (not events model) for date override and location override; events model does not have those overrides.
7. **Content Fragment card list** — Can display events (or news) outside calendar; by path or by tag (e.g. “dinner and a show”). Event calendar = one folder path only; cannot select multiple folders for one calendar.
8. **Tomorrow** — Modified agenda: careers-focused (hiring events, video testimonials, etc.); Daniela to post updated Confluence.

---

## Questions, comments, and answers (captured)

*See **Events** sheet in SHRSS Adobe KT Session Follow-Up Tracker for full list.*

- **Publish delay (author vs publisher):** Gonzalo—changes visible in “view as published” but not on publisher; Andy investigating failed publish logs; will monitor.
- **Date override (e.g. “every Wednesday through February”):** Not in event CF; promotions has it; gap. Same for location override.
- **Multiple images in event CF:** Defaults to first; others not used.
- **Event status + date logic (presale → on sale):** Currently manual; gap to associate status with date range so it auto-changes.
- **Hide CTA when no extra info:** Toggle to hide “more info” = gap.
- **Location reference restricted by user:** Root path limits which events show; wrong location in CF still populates filter; restrict by user = gap.
- **Default image for event card:** CF requires image to save; component-level default (like jobs) = potential gap.
- **Event detail page / careers / Hard Rock Live:** Same event detail template used for all sites; not careers-only.
- **Friendly event URL (artist name not ID):** Event ID read-only; editable/friendly URL = gap; Mayte: need smart CMS behavior (like WordPress/Sitecore).
- **Event detail hero:** Default on page; CF banner overrides.
- **Event statuses driving content (presale hide CTA, etc.):** Status changes label/flag; event status message separate; no auto hide/show by status.
- **Preview before publish / PDF for approval:** View as published doesn’t show CF changes until CF published; Andy: preview tier exists, not configured; export/screenshot process = gap.
- **What to publish when (fragment, detail page, calendar):** One event detail page per calendar; publish once. New event = publish CF; calendar page publish needed for event to show on publisher (and can take time).
- **Unpublish:** Unpublish CF removes from calendar and detail URL shows “no events”; confirmed.
- **Mix-and-match locations for one calendar (subset of properties):** Not supported; one folder path only = big gap.
- **Pull events to other pages (by tag, venue, category):** Content Fragment card list can show events by path or tag.
- **Filter on careers hiring events:** Careers uses content fragment card (no filter); promotions component has filter; can swap on landing page.
- **Pull jobs to property page (e.g. Tampa, exclude category):** Root path = e.g. Tampa folder; cannot exclude category in component.
- **Tags on event cards (21+, free, phone-free):** Edwin to send example; Daniela to take to tech team.
- **Preview link for unpublished:** Unpublished CF not visible; preview tier / approval workflow = gap.

---

## Product Director — own questions and points of clarification

1. **Governance — event categories and location reference:** Who owns the Event Categories tag taxonomy and the DPLT location list? If a property or venue is added/renamed, what is the process so authors see the right options and filters stay correct?
2. **Authoring — one event, many places:** We heard that in Sitecore we do it once and it populates everywhere. In AEM we have event CF + calendar page + detail page and optional use of promotions model for hiring events. Can we get a one-page “event authoring checklist” (what to create, what to publish, in what order) and when to use events CF vs promotions CF?
3. **Tagging:** For events, categories (tags) drive filters; “tags” are internal. For pulling events into other pages by “dinner and a show,” is that an existing tag taxonomy we should use or something we need to define? Who governs event tags used for filtering vs. for queries?
4. **Gap analysis — events vs promotions:** Hiring events use promotions (with date/location override); events do not. What is the decision criteria for “use events CF” vs “use promotions CF” for a given section, and which gaps (date override, location override, multi-folder calendar, friendly URL) are in scope for which model?
5. **Permissions:** Who can create or edit Event Categories tags and who can add/change location reference options (DPLT)? Is that admin-only or can we assign by property/line of business?

---

## Final thoughts

- Strong ask to prioritize careers and to understand “events” vs “promotions” and what authors can/cannot do. Agenda pivot to careers-focused next session.
- Recurring themes: manual steps (status, publish order), need for preview/approval, single folder path for calendar, friendly URLs, and consistency with “do it once, show everywhere” expectations.

---

*End of session notes. All Q&A rows are in the **Events** sheet of `SHRSS_Adobe_KT_Session_Follow_Up_Tracker.xlsx`.*
