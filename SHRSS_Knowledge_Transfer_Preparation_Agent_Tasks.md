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

