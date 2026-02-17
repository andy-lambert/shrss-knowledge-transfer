# Asset Metadata Fields Configured for Tag Selection

**Source:** `/conf` in content package  
`Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/conf`

All metadata fields below use a **tagfield** (values selected from the tag taxonomy). Widget: `cq/gui/components/coral/common/form/tagfield` with `metaType="tags"`.

---

## 1. DAM Asset Metadata Schema (Assets UI)

**Configuration path:**  
`/conf/global/settings/dam/adminui-extension/metadataschema/shrssmetadataschema`

Applied to assets in the Assets console (metadata form). Stored under `jcr:content/metadata/`.

| Field label | Metadata property | Tag root path (selection scope) |
|-------------|--------------------|---------------------------------|
| **Tags** | `cq:tags` | *(not set – full taxonomy)* |
| **Brand** | `shrssbrands` | `/content/cq:tags/shrss/brands` |
| **Venues & Branded Experiences** | `shrssvenues` | `/content/cq:tags/shrss/venues-and-branded-experiences` |
| **Line of Business** | `shrsslob` | `/content/cq:tags/shrss/lob` |
| **Property Names (Locators / City Drop)** | `shrssproperty` | `/content/cq:tags/shrss/properties` |
| **Type** | `shrsstype` | `/content/cq:tags/shrss/type` |
| **Category** | `shrsscategory` | `/content/cq:tags/shrss/category` |
| **Product** | `shrssproduct` | `/content/cq:tags/shrss/products` |

---

## 2. Content Fragment Models (CF authoring)

**Configuration path:**  
`/conf/shrss/settings/dam/cfm/models/<model>`

Used when editing Content Fragments. Values stored in the CF model data (e.g. `jcr:content/data/master/`).

### Events model  
`conf/shrss/settings/dam/cfm/models/events`

| Field label | Property name | Tag root path |
|-------------|--------------|----------------|
| **Categories** | `categories` | `/content/cq:tags/shrss/event-categories` |

### News model  
`conf/shrss/settings/dam/cfm/models/news`

| Field label | Property name | Tag root path |
|-------------|--------------|----------------|
| **Categories** | `categories` | `/content/cq:tags/shrss` |
| **Tags** | `tags` | `/content/cq:tags` |

---

## Summary list (all metadata fields that use tag selection)

1. **DAM metadata (shrssmetadataschema):** Tags (`cq:tags`), Brand (`shrssbrands`), Venues & Branded Experiences (`shrssvenues`), Line of Business (`shrsslob`), Property Names (`shrssproperty`), Type (`shrsstype`), Category (`shrsscategory`), Product (`shrssproduct`).
2. **Content Fragment – Events:** Categories (`categories`) — root: `shrss/event-categories`.
3. **Content Fragment – News:** Categories (`categories`) — root: `shrss`; Tags (`tags`) — root: full taxonomy.

**Note:** “Smart Color Tags” and “Smart Tags” (predictedTags) are tag-related but not manual tag selection; they are system/AI-driven and are not included in this list.
