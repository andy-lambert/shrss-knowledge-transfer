**DAM Content Architecture**

- How the DAM is structured

- How and where to store assets in the correct hierarchy

- Best practices

- Architecture realignment roadmap (shrss → shrss-primary)


**Assets Metadata**

- Metadata schemas
- Folder metadata schemas
  - Supports search of assets in a folder. "Photography" for example
  - Folder has photography, so will return assets in that folder in search results
- Metadata profiles
  - property/value applied to every asset in the folder w/ that profile, regardless of whether property is defined in asset metadata schema
- Best practices

**DAM Operations**

- How to upload, version, and manage assets
- How to avoid breaking references
- How asset updates flow to live pages
- Best practices

**Dynamic Media**



Current state



Integration roadmap



DAM content arch restructure

- Gut photography
  - Move into new structures
- 
- 
- 
- First, get restructured assets working from DAM
  - CAUTION: Migrated content where asset source is in RTE
- Second, focus on DM



DM

- Export Excel report of all assets in corporate -> photography
  - Review assets by path, other metadata fields to define new folder structure
- Content component migration to DM components
- Restructure DAM optimized to DM
  - Create "migrated assets" folder
    - A-Z subfolders
      - Move assets by name
    - 0-9 subfolders
      - Move assets by number
    - Create nested folders as needed to for < 1000 max per folder requirement.
      - MAYBE by asset type here
  - Renovator as a possible tool for restructure en masse: https://adobe-consulting-services.github.io/acs-aem-commons/features/mcp-tools/renovator/index.html
  - Test first with subset of one letter or subset of letter
- Publish assets to DM

> [!TIP]
>
> If you are hunting assets by browsing folders in the DAM, you're doing it the hard way. Search by metadata and tags.

