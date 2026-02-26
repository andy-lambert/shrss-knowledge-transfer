# Session Notes — Shared Data — 2026-02-19

**Session:** Shared Data  
**Date:** February 19, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260219_130217  
**Duration:** 1h 31m 52s  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context

- Updates: Component specs page under review (2/19); vanity URL process (page path + desired URL + .html; multiple allowed). Redirect vanity URL checkbox—Daniela to confirm (302 redirect). Card carousel: tablet field removed (logic always 2 for non–full width); gap if tablet-specific needed.
- Shared data: when to use content fragment vs experience fragment. Content fragment = same content, can display differently per site. Experience fragment = same content + same look; update once, roll out. Header/footer = experience fragments.

---

## What was covered

1. **Vanity URLs** — Page properties; full page path + desired URL + .html (dispatcher rule strips extension). Multiple vanity URLs per page. Redirect vanity URL = 302 (Daniela to confirm use cases).
2. **Content fragment (bio example)** — New CF model (name, title, bio, image); store once; content fragment component shows text elements (image needs custom component). Default value on model for image possible. Card component can reference CF.
3. **Experience fragment (benefits)** — Original + variation as live copy; cancel inheritance on specific elements; roll out to selected variations. Same content, same presentation; one update, roll out.
4. **Default image in CF model** — Yes; new CFs get default; author can override. Custom component (e.g. card) would show it.
5. **Break variation / reorder** — Edwin: break connection to use as regular component or reorder on page? Daniela to confirm (break inheritance vs new component).

---

## Questions, comments, and answers (captured)

*See **Shared_Data** sheet in tracker.*

- Redirect vanity URL checkbox: 302 redirect; Daniela to confirm when to use.
- Multiple vanity URLs: yes; good for print vs long URL.
- Card carousel tablet: field removed; always 2; gap if need tablet config.
- CF default image: yes; custom component shows it.
- CF vs EF: CF = same content different styling; EF = same content same styling, roll out.
- Break variation / reorder: follow-up.

---

## Product Director — own questions

1. **Governance:** Who can create new content fragment models for shared data? Who can create experience fragment variations and roll out?
2. **Authoring:** Decision tree: “shared content, same look” → EF; “shared content, different look” → CF; “one-off page” → components on page?
3. **Tagging:** Do shared CFs/EFs use tags for filtering or only for organization?
4. **Gap analysis:** Card carousel tablet control—in scope for platform expansion? Vanity URL 302 vs 301?
5. **Permissions:** Who can add vanity URLs (page level)? Who can create EF variations and roll out?

---

*End of session notes. All Q&A rows in **Shared_Data** sheet.*
