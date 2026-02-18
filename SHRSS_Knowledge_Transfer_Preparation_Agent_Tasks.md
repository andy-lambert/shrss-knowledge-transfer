# SHRSS Knowledge Transfer Preparation Tasks

## Getting started

1. Review and adhere to all aspects of @AGENTS.md throughout all aspects and tasking for this project.
2. As you proceed through task steps, keep notes in the agent scratch notes file for yourself and future agents working on the project: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/AGENT-SCRATCH-NOTES.md`. Include key aspects of the current implementation and content from steps 3 and 4 below so that future agents will have sufficient knowledge to proceed without having to repeat steps 3-4 below, but can reference the artifacts from 3-4 as needed for more comprehensive analysis/comprehension.
3. Understand current implementation architecture by reviewing the results of the implementation analysis project. See markdown documents here: `/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`, starting with `00_EXEC_SUMMARY.md`
4. Understand current content template policies, asset metadata schemas, tagging taxonomy, and content currently in customer's production environment
   - A content package has been extracted here for review/analysis: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`
5. After completing prior steps, pause and let me know you're ready to proceed.

---

## Task 1 - "Tagging, Taxonomy & Metadata Governance" KT Session Prep

For this task, we will be working in this folder: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Tagging_and_Taxonomy`

There are currently two documents in the folder:

- `AAEMDAM-3860_Tagging_Taxonomy_and_Metadata_Governance.pdf`: Defines the agenda for the session
- `AAEMDAM-3860_Tagging_Taxonomy_and_Metadata_Governance_JIRA.docx`: Export of the Jira ticket that describes the requirement for the session

Task Objective: Create artifacts for session including host script, diagrams/outlines, and other useful materials to support the session agenda.

Task Steps:

1. Review:

   - `AAEMDAM-3860_Tagging_Taxonomy_and_Metadata_Governance.pdf`: Defines the agenda for the session
   - `AAEMDAM-3860_Tagging_Taxonomy_and_Metadata_Governance_JIRA.docx`: Export of the Jira ticket that describes the requirement for the session

2. Create a markdown version of `AAEMDAM-3860_Tagging_Taxonomy_and_Metadata_Governance.pdf` for us to use as a working draft of the main session guide for me as the host/instructor

3. Based on your analysis of the archicture and content, create a document with proposed content to fill in for the following sections of the agenda. Use the links included below along with the resources in authoritative references to help inform content (`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/docs/ai/reference`)

   - Tag Taxonomy
     - How taxonomy was configured for this implementation
     - How tags are structured across Brand / LOB / Property
     - Best practices and taxonomy strategy
       - Sites: https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/page-authoring/expert-advice/site-hierarchy
       - Assets: https://experienceleague.adobe.com/en/perspectives/taxonomy-and-tagging-best-practices-for-aem-assets

   - Tag Management
     - Governance
       - Rules for tag governance (who creates, who maintains, who approves)
     - Creating, updating, deleting tags
     - Best practices

   - Application of Tags in SHRSS Authoring & Asset Management
     - Component and asset metadata mapping
     - How tags impact:
       - Dynamic content queries
       - Category filters
       - Search results
       - Content inheritance across sites
       - Card and page visibility

---

## Task 2 - Create content/tag mapping spreadsheet

I need an Excel spreadsheet listing all content resources from the exported content package and that resource's assigned tags. Exclude content resources with no tags

Please create an Excel file (.xlsx) file with a sheet containing the following columns:

- Content Type: (`Page`, `Experience Fragment`, `Content Fragment`)
- Path: path to content item in JCR starting at `/content`. For example: `/content/shrss/corporate/hardrock/en`
- Tag IDs (pipe-delimited). Example: `shrss:brands/hri|shrss:country/united-states|shrss:regions/na`
- Tag Paths (pipe-delimited). Take Tag ID value and replace `shrss:` with `/content/cq:tags/shrss/`.     Example: `/content/cq:tags/shrss/brands/hri|/content/cq:tags/shrss/country/united-states|/content/cq:tags/shrss/regions/na`
- Tag Property: (`cq:tags`, or other component or asset metadata property names as applicable. `categories` for any content fragments is a good example)

---

## Task 3 - Scrub all asset nodes from content package content

### Task Objective

Modify FileVault content package to contain **only** the folder structure and associated metadata nodes for a given path in the customer's AEM Assets instance (DAM), with no asset nodes remaining in the package contents (i.e. no nodes having a `jcr:primaryType` property value of `dam:Asset`). 

The customer should be able to install this package on an AEM instance via Package Manager and, as a result, the exact, empty hierarchical folder structure will be created in the DAM.

### Task Details

There is an extracted FileVault content package zip file here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/dam-shrss-folder-structure-1.0`. (FileVault documentation: https://jackrabbit.apache.org/filevault/overview.html)

This directory contains the hierarchical set of subdirectories and files that define the JCR nodes, properties, and other attributes of resources in the customer's DAM starting at path `/content/dam/shrss` (absolute path: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/dam-shrss-folder-structure-1.0/jcr_root/content/dam/shrss`). NOTE: For the remainder of this task we will refer to this directory as "the working folder".

Each subdirectory under the working folder, and the working folder itself, has a child XML file named `.content.xml`. These files define what type of node the directory represents, based off of the value of the `jcr:primaryType` defined inside the directory's `.content.xml` file.

Our goal is to remove all subdirectories with a `jcr:primaryType` property value of `dam:Asset` (and their child directory structures), leaving only folder nodes in the content package definition. 

* See more instruction and examples under "Folder Nodes" and "Nodes to Remove" sections below.

To get started:

1. Analyze the contents the working directory and compile a list of all asset node directories to be removed.
2. Add the directory paths to a new Excel (.xlsx) file in this directory: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM`
   - In addtion to the path columns, include a "type" column that specifies the directory's `jcr:primaryType` property value based on the configuration in the directory's immediate child `.content.xml` file.
3. Pause and prompt me to review and with any questions or points of clarification. I will review, make adjustments, and reply with feedback and next steps.

#### Folder Nodes

The package will include all folder nodes having a jcr:primaryType property value matching any of the following values/constraints:

- nt:folder

- sling:Folder

- nt:unstructured CONSTRAINT: ONLY `nt:unstructured` nodes having node name: `folderThumbnail.dir`. These define the content nodes under folders representing the parent folder node's corresponding image thumbnail)

  - Example thumbnail folder node definition directory: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/dam-shrss-folder-structure-1.0/jcr_root/content/dam/shrss/corporate/_jcr_content/folderThumbnail.dir` 

  - Example thumbnail folder node definition directory XML in the folder's `.content.xml` file

    - ```xml
      <?xml version="1.0" encoding="UTF-8"?>
      <jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:dam="http://www.day.com/dam/1.0" xmlns:nt="http://www.jcp.org/jcr/nt/1.0"
          jcr:primaryType="nt:file">
          <jcr:content
              dam:folderThumbnailPaths="[/content/dam/shrss/corporate/logos/Hard Rock_News_logo.jpg,/content/dam/shrss/corporate/logos/2025-bmc-logo-v2.jpg,/content/dam/shrss/corporate/logos/ecolab-logo-sm.jpg]"
              jcr:primaryType="nt:unstructured"
              bgcolor="{Long}-1"
              height="{Long}200"
              width="{Long}240"/>
      </jcr:root>
      ```

#### Nodes to Remove

Example asset node directory: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/dam-shrss-folder-structure-1.0/jcr_root/content/dam/shrss/corporate/photography/05-guitar-smash-1536x1024.jpg`

Snippet from directory's `.content.xml` file including `jcr:primaryType` property with value equaling `dam:Asset`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:dam="http://www.day.com/dam/1.0" xmlns:tiff="http://ns.adobe.com/tiff/1.0/" xmlns:nt="http://www.jcp.org/jcr/nt/1.0" xmlns:mix="http://www.jcp.org/jcr/mix/1.0" xmlns:cq="http://www.day.com/jcr/cq/1.0" xmlns:dc="http://purl.org/dc/elements/1.1/"
    jcr:mixinTypes="[mix:referenceable]"
    jcr:primaryType="dam:Asset"
    jcr:uuid="f40b0e8a-e516-4088-b15b-356cf65019fb">
    <!-- <jcr:content> -->
</jcr:root>
```

---

## Task 4 - Create complete mapping of CF Card List component to page and experience fragment usage

### Task Objective

Create comprehensive documentation of current CF Card List component usage in pages and experience fragments.

### Task Details

In a prior session, we created a document containing a sampling of pages where the CF Card List component is configured on the page: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Tagging_and_Taxonomy/CF_Card_List_Page_Examples_KT_Reference.md`

In this task, we will create another version of this markdown document that will be provided to the customer as an inventory of pages and experience fragments that use the CF Card List component.

In addition, we will generate a new Excel spreadsheet file (.xlsx) also containing the inventory.

> [!IMPORTANT]
> In the document content, do not mention anything about the KT session. This will serve as a deliverable artifact.

 Follow the task guidance below to create the deliverable artifact.

### Content Sources

We want to capture usage in the two sites currently in production, as well as the Careers website, which is in customer QA/UAT and targeted to go to production on March 16, 2026.

#### Sites currently in Production

Analyze/include content for the following two sites from the **production** content folder here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`:

- `/jcr_root/content/shrss/corporate` (https://www.hardrock.com)
  - NOTE: Exclude the `/jcr_root/content/shrss/corporate/careers` directory. Though the Careers content is structured under the `corporate` site hierarchy, it will actually be hosted as a standalone site at https://careers.hardrock.com. The Careers site content IS NOT currently up to date on production. We will account for it via the content package from the Stage environment below.

- `/jcr_root/content/shrss/reverb` (https://reverb.hardrock.com/)

#### Sites currently in Stage (In customer QA/UAT)

Analyze/include content for the following site from the **stage** content folder here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0`:

- `/jcr_root/content/shrss/corporate/careers` (https://aem.careers.stage.hardrock.com/)

#### Page versus Experience Fragment Locations

- **Pages** are located under `/jcr_root/content/shrss`
- **Experience fragments** are located under `/jcr_root/content/experience-fragments/shrss`

### Markdown Document Organization

Structure the inventory by Site, then site subsections underneath when applicable, then sub-subsections/pages at the same level, and so on. I am open to your thoughts how best to organize. Experience fragments

For each section, organize the relevant pages/EFs into a table with the following columns (see "Appendix - Table examples from CF_Card_List_Page_Examples_KT_Reference.md" below for quick reference to tables in the original version of this file):

- **Type** ("Page" or "Experience Fragment")
- **Path** (Page or EF path starting at `/content`.)
  - Examples:
    - Page: `/content/shrss/corporate/hardrock/en/blog`
    - Experience Fragment: `/content/experience-fragments/shrss/corporate/hardrock/en/header/master`
- **Site/Context** (See appendix, 'Best for “List by tags” demo' table for example)
- **CF Card List Config** (See appendix, 'Best for “List by tags” demo' table for example)
- **Notes** (See appendix, "Other pages with CF Card List" table for example)

### Excel File

Use the same columns/values from the markdown document tables in the Excel file

> [!NOTE]
>
> The relevant pages and experience fragments (ef) can be found based one of the nested child nodes under `<page or ef node>/jcr:content/**` having a `sling:resourceType` property with a value of `shrss/components/cfcardlist`. For example: `/content/shrss/corporate/hardrock/en/blog/jcr:content/root/container/container/white-bg-container/white-bg-container/featured-blog-posts-grey-container/featured-blog-posts-container/cfcardlist`. 
>

> [!IMPORTANT]
>
> DO NOT rely solely on the name of the node to determine whether it is an instance of the CF Card List component or not (i.e. `cfcardlist`). In theory, the component node name could be something else

### Task 4 - Agent Clarification Questions

1. One row per page/EF vs per component

   When a page has multiple CF Card List instances, should the deliverable have:

   - One row per page/EF (Notes/Config describe all instances), or

   - One row per component instance (same page path can appear multiple times, with one config per row)?

   ANSWER: One row per component instance. Yes, please add an "Instance" column. Great idea!

2. Output location

   Where should the two deliverables live?

   - Option A: DAM/ (with other DAM KT artifacts).

   - Option B: Tagging_and_Taxonomy/ (next to CF_Card_List_Page_Examples_KT_Reference.md).

   - Option C: Another path you specify.

   ANSWER: Option B: Tagging_and_Taxonomy/ (next to CF_Card_List_Page_Examples_KT_Reference.md).

3. Experience fragments scope

   Confirm we include EFs under /content/experience-fragments/shrss that belong to:

   - corporate (excluding careers) and reverb from PROD, and

   - corporate/careers from STAGE,
   - and that we only include EFs that actually contain at least one shrss/components/cfcardlist instance.

   ANSWER: Confirmed all

4. File names

   Preferred base name for the two files? For example:

   - CF_Card_List_Usage_Inventory.md and CF_Card_List_Usage_Inventory.xlsx, or

   - Something like AAEMDAM-3736_CF_Card_List_Usage_Inventory.md / .xlsx?

   ANSWER: CF_Card_List_Usage_Inventory.md and CF_Card_List_Usage_Inventory.xlsx

---

## Task 4 - Appendix - Table examples from CF_Card_List_Page_Examples_KT_Reference.md

> ## Best for “List by tags” demo
>
> | Page path (JCR)                                 | Site / context             | CF Card List config                                          |
> | ----------------------------------------------- | -------------------------- | ------------------------------------------------------------ |
> | **`/content/shrss/corporate/hardrock/en/blog`** | Corporate Hard Rock → Blog | **listType:** `tags` • **tagsList:** `shrss:news-categories/featured-news` • **tagsRootFolder:** `/content/dam/shrss/cf/news/corporate/en` • **type:** news • **categories:** false (card config) |
>

> ## Other pages with CF Card List
>
> | Page path (JCR)                                         | Notes                                                        |
> | ------------------------------------------------------- | ------------------------------------------------------------ |
> | **`/content/shrss/reverb/en/tbd/en/cf-card-list-page`** | Dedicated CF card list page. Contains **two** CF Card List components: one **Events** (listType=rootPath, rootFolder=events path), one **News** (listType=rootPath, rootFolder=news path). Good for comparing rootPath vs. tags. |
> | **`/content/shrss/reverb/en/tbd/en/event-list-reverb`** | Events list (rootPath-style; eventBasePath set).             |
> | **`/content/shrss/corporate/hardrock/en/home`**         | Home page with CF Card List (categories=false).              |
> | **`/content/shrss/corporate/hardrock/en/corporate`**    | Corporate section with CF Card List.                         |
> | **`/content/shrss/hotel/en/home`**                      | Hotel home with CF Card List.                                |
>

---

## Task 5 - Consolidate and Rename Tagging Structure Package Files
### Task Objective

Create a single `.content.xml` file that represents the entire SHRSS tagging structure.

### Task Details

I have extracted an AEM content package containing the SHRSS tag structure here. For this task, this directory will be referred to as **"the source directory"**: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM/00_Drafts_and_Resources/tag_working_directory/_cq_tags/shrss`

I have created a new directory that, for this task, will be referred to as **"the target directory"** here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM/00_Drafts_and_Resources/tag_working_directory/shrss_tag_structure_definition_files`

### Task Steps

1. Copy `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM/00_Drafts_and_Resources/tag_working_directory/_cq_tags/shrss/.content.xml` to the target directory
2. Traverse all directories under the source directory, extracting the content in each directory's direct child `.content.xml` file between the opening/closing `<jcr:root>` tags and pasting it into its respective location in the target directory's `.content.xml` file.
3. Continue following this pattern until the tag configurations in all nested subdirectories under the target directory are populated into the target directory's `.content.xml` file.

Example:

The `_cq_tags/shrss` directory's `.content.xml` file contains the following:

```xml
<global/>
<hotel/>
<casino/>
<cafe/>
<categories/>
<brands/>
<venues-and-branded-experiences/>
<regions/>
<lob/>
<properties/>
<type/>
<category/>
<news-categories/>
<event-categories/>
<country/>
<products/>
```

- The `_cq_tags/shrss/global/.content.xml` file doesn't contain any tag placeholders, so we would leave it unchanged in the target directory `.content.xml` file.

- The `_cq_tags/shrss/brands/.content.xml` file contains three entries. So, the matching `<brands/>` element in the target `.content.xml` file would get expanded to include these elements:

  - ```xml
    <hri/>
    <sga/>
    <shr/>
    ```

---

## Task 6 - Create a markdown document with SHRSS DAM structure in outline form

### Task Objective

Create a markdown document and Excel spreadsheet containing a complete visual model of the current SHRSS DAM architecture. 

### Task Details

Use the updated package defintion we created in "Task 3 - Scrub all asset nodes from content package content"

At minimum, the document should include the folder structure in outline form. Am also interested in your ideas on additional visual representations (diagrams, tables, etc.)

Please also generate a spreadsheet that conveys the current DAM structure. For an example of what the customer has seen before, see the "Asset Folders" sheet in this workbook: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/SHRSS-Content-Architecture-Workbook-v1_3.xlsx`. Note this sheet is likely out of date.

Save the markdown file here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/DAM`
