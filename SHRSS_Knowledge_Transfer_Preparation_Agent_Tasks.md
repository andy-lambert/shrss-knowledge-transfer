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