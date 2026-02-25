# Session Notes — News — 2026-02-20

**Session:** News  
**Date:** February 20, 2026  
**Recording:** SHRSS Adobe Knowledge Transfer-20260220_130127  
**Duration:** 1h 19m 41s  
**Primary presenter:** Daniela Tea (Adobe)

---

## Session context

- List component (footer and elsewhere): build by tags (match all / any), search query (text in props and on page), fixed list, or child pages. Tags = page property level; create in Tagging console. Exclude tags? Not OOTB; Daniela to take back. List: order by title or last modified; number of columns. Logo styling (image component)—Daniela to check JIRA. Redirect vanity URL: 302 when checkbox; doc to be shared. Transparent background on card = for primary/tertiary styles.
- News: Create news homepage from scratch (e.g. careers news). Structure CF > news > [LOB] > year > month. News CF model; default image at component level (news search results). Default image by category/tag (e.g. casino vs hotel)—gap; need requirements. News categories = tags (news categories namespace).

---

## What was covered

1. **List component** — Tags (match all/any), search query, fixed list, child pages. Exclude certain tags (e.g. “do not use”)—not OOTB; gap. Order: title or last modified. Columns configurable.
2. **Logo styling** — Image component; Daniela to confirm from JIRA (footer vs multi-logo pages).
3. **Redirect vanity URL** — Checkbox = 302 redirect; doc provided; technical enablement for deeper redirect management.
4. **News** — Folder structure LOB > year > month; create CF; required/optional fields; default image at component level for items without image. Default image per category/tag = gap + requirements.
5. **News categories** — Tag-driven (news categories in tagging).

---

## Questions, comments, and answers (captured)

*See **News** sheet in tracker.*

- List: exclude tags? Not OOTB; take back.
- List: what dictates columns/order? Order by title or last modified; column count in config.
- Logo styling: check JIRA.
- Redirect vanity URL: 302; doc in chat.
- News default image: at component level. By category/tag = gap.
- News CF: default image in model? Can be added; component-level default shown today.

---

## Product Director — own questions

1. **Governance:** Who can add news categories (tags) and change news CF model? Who manages list component source (tags vs query)?
2. **Authoring:** Checklist for new news LOB (e.g. careers): create folder structure, create CFs, create news page, configure component (path, default image)?
3. **Tagging:** News categories = tags; who governs that list? Can authors add to news categories or admin only?
4. **Gap analysis:** Exclude tags in list—priority? Default image by category—requirements and logic (multiple tags)?
5. **Permissions:** Who can create news CF model and news folders?

---

*End of session notes. All Q&A rows in **News** sheet.*
