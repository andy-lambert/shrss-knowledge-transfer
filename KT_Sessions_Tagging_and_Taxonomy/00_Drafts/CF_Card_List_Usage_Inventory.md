# CF Card List Component — Usage Inventory

Inventory of pages that use the **CF Card List** component (`shrss/components/cfcardlist`). One row per component instance.

**Content sources:** Production (Corporate excl. Careers, Reverb); Stage (Careers).

---

## Corporate Hard Rock (en)

| Type | Path | Site/Context | Instance | CF Card List Config | Notes |
|------|------|---------------|----------|---------------------|-------|
| Page | `/content/shrss/corporate/hardrock/en/blog` | Corporate Hard Rock (en) → Blog | 1 | **listType:** `tags` • **tagsList:** `[shrss:news-categories/featured-news]` • **tagsRootFolder:** `/content/dam/shrss/cf/news/corporate/en` • **type:** `news` • **categories:** `false` • **cards:** `2` • **cardLayoutStyle:** `cf-list--col-2` • **ctaLabel:** `Read More` • **description:** `false` • **enableSecondCta:** `true` • **location:** `true` • **time:** `false` | Tag-driven list: News CFs with tag featured-news. |
| Page | `/content/shrss/corporate/hardrock/en/home` | Corporate Hard Rock (en) → Home | 1 | **listType:** `tags` • **tagsList:** `[shrss:news-categories/press-releases]` • **tagsRootFolder:** `/content/dam/shrss/cf/news/corporate/en` • **type:** `news` • **categories:** `false` • **cards:** `2` • **cardLayoutStyle:** `cf-list--col-2` • **ctaLabel:** `Continue Reading` • **description:** `true` • **enableSecondCta:** `true` • **location:** `true` • **time:** `false` • **fileReference:** `/content/dam/shrss/corporate/photography/12569996-imagemediumwidth.jpg` | Home page with CF Card List (categories=false). |
| Page | `/content/shrss/corporate/hardrock/en/corporate` | Corporate Hard Rock (en) → Corporate | 1 | **listType:** `tags` • **tagsList:** `[shrss:news-categories/press-releases]` • **tagsRootFolder:** `/content/dam/shrss/cf/news/corporate/en` • **type:** `news` • **categories:** `false` • **cards:** `2` • **cardLayoutStyle:** `cf-list--col-2` • **ctaLabel:** `Continue Reading` • **description:** `true` • **enableSecondCta:** `true` • **location:** `true` • **time:** `false` • **fileReference:** `/content/dam/shrss/corporate/photography/12569996-imagemediumwidth.jpg` | Corporate section with CF Card List (tags, press-releases). |

## Reverb (en)

| Type | Path | Site/Context | Instance | CF Card List Config | Notes |
|------|------|---------------|----------|---------------------|-------|
| Page | `/content/shrss/reverb/en/tbd/en/cf-card-list-page` | Reverb (en) → CF Card List Page | 1 | **listType:** `rootPath` • **rootFolder:** `/content/dam/shrss/cf/events/cafe/pittsburgh/en/2025/02` • **type:** `event` • **eventBasePath:** `/content/shrss/us/en/qa-home-page/home-page/qa-testing/event-page-new` • **categories:** `true` • **cards:** `2` • **cardLayoutStyle:** `cf-list--col-2` • **ctaLabel:** `Learn More` • **description:** `true` • **enableSecondCta:** `true` • **location:** `true` • **time:** `true` | Two instances: Events (rootPath) and News (rootPath). Good for comparing rootPath configs. |
| Page | `/content/shrss/reverb/en/tbd/en/cf-card-list-page` | Reverb (en) → CF Card List Page | 2 | **listType:** `rootPath` • **rootFolder:** `/content/dam/shrss/cf/news/corporate/en/2024/10` • **type:** `news` • **categories:** `true` • **cards:** `2` • **cardLayoutStyle:** `cf-list--col-2` • **ctaLabel:** `Learn More` • **description:** `true` • **enableSecondCta:** `true` • **location:** `true` • **time:** `true` |  |
| Page | `/content/shrss/reverb/en/tbd/en/event-list-reverb` | Reverb (en) → Event List Reverb | 1 | **listType:** `fixedList` • **rootFolder:** `/content/dam/shrss-old/content-fragment/content-for-cf-cards/events-cf` • **type:** `event` • **eventBasePath:** `/content/shrss/reverb/en/HomePage/events-page-reverb` • **cards:** `3` • **ctaLabel:** `Read More` | Events list (fixedList; eventBasePath set). |

## Careers (en)

| Type | Path | Site/Context | Instance | CF Card List Config | Notes |
|------|------|---------------|----------|---------------------|-------|
| Page | `/content/shrss/corporate/careers/en/knowledge-transfer` | Careers (en) → Knowledge Transfer | 1 | **listType:** `rootPath` • **rootFolder:** `/content/dam/shrss/cf/promotions/careers/en` • **type:** `event` • **categories:** `false` • **cards:** `2` • **cardLayoutStyle:** `cf-list--col-3` • **ctaLabel:** `Learn More` • **description:** `true` • **enableSecondCta:** `true` • **location:** `true` • **time:** `false` |  |
| Page | `/content/shrss/corporate/careers/en/kt-other` | Careers (en) → KT Other | 1 | (no config set) |  |

