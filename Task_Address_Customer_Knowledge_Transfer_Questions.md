# Task - Address Customer Knowledge Transfer (KT) Questions

## Task Objective

Categorize and, when possible, answer the questions submitted to Adobe by the customer following each of the knowledge transfer (KT) sessions, flagging those that are too ambiguous or require more information/context to be meaningfully, accurately addressed. In addition, flag questions that are likely AI-generated.

## Background for Context (IMPORTANT! Do not skip.)

Adobe Professional Services is providing the SHRSS customer with a set of knowledge transfer (KT) sessions to enable their authors, DAM admins/architects/librarians, and developers (eventual owners of the platform) with the skills and information they need to effectively:

- conduct role-specific day-to-day tasks and operations
- have a holistic, comprehensive understanding of their implementation in its current state
- make informed decisions when assessing and prioritizing requirements to provide Adobe to conduct the next wave of development and web property migrations:
  - Enhancements/fixes based on experiences to date of stakeholders mentioned above
  - New custom features/components
  - Adoption of new/additional AEMaaCS capabilities
  - Integration of additional 3rd party services

To date, KT sessions have been conducted for the following topics:

- Jobs
- Events
- Careers
- Tagging_Taxonomy_Metadata_Gov
- DAM_Training_Usage_Admin
- Shared_Data
- News
- Locations

After each KT session, Adobe/SHRSS agreed that any related follow up questions from SHRSS would be provided for Adobe to address. We have run into an issue where the customer is posting ~100 questions per session. While some of the questions are highly relevant, valid, contextual inquiries, many are the opposite - not relevant to the session content and are highly vague/ambiguous. 

In fact, it appears that one of the authors has uploaded the transcripts from the sessions to ChatGPT and asked for 100 questions per session to ask Adobe, maybe asking the agent to review and curate questions from the perspective/persona of an AEM technical expert.

## Task Resources

### Task Relevant Files

| Resource              |                                                              |
| --------------------- | ------------------------------------------------------------ |
| Session transcripts   | `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md` |
| Questions spreadsheet | `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/KT_Session_Follow_Up_Questions_RESEARCH_WORKING.xlsx` |

### SHRSS AEM Content

#### Prod Content

> [!IMPORTANT]
>
> Contains pages, experience fragments, content fragments/content fragment models, configurations/policies, and metatadata schemas for sites currently in production (https://www.hardrock.com, https://reverb.hardrock.com)

`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`

- **Configurations (page templates, etc.), content fragment models, asset metadata schemas:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/conf`
- **Pages:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/shrss`
- **Experience Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/experience-fragments`
- **Content Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/dam/shrss/cf`

##### Prod Assets (DAM)

> [!IMPORTANT]
>
> Can analyze referenced assets questions pertaining to particular component/image display issues in pages and experience fragments, for example.

`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-assets-PROD-1.0/jcr_root/content/dam`

### SHRSS Implementation Sourcecode / Git

**Git Repo:** `/Users/lambert/Documents/workspace/SHRSS/Customer-Git/shrss-aem-projects`

**Working branch:** `develop`

### MCP Servers

You have access to the tools/services defined in these MCP servers, currently enabled in Cursor:

- Adobe Developer Assistant (ADA)
  - `ask_ada` tool to search Experience League and internal docs
- singularity
  - `ask_docs` tool to deep search Adobe docs, repos, Jira, Confluence
- Adobe Wiki Confluence
  - Multiple tools to search Adobe internal Confluence
- Corp GitHub
  - Multiple tools
  - NOTE: you have access to AEM repos here:
    - https://git.corp.adobe.com/Granite
    - https://git.corp.adobe.com/CQ
    - https://git.corp.adobe.com/CQ/platform
    - etc.



## Task Details

I would like for you to analyze the questions in the questions spreadsheet and attempt to accomplish two distinct goals, defined below as subtasks to be completed in order.

### Subtask 1

Identify the questions that are likely to have been generated by AI (whether ChatGPT, Microsoft Copilot, or other). For those that qualify as potentially AI-generated, popuate the "AI Generated" column with "TRUE", and the "Confidence" column with a percentage of how confident you are that the question was AI-generated ranging from 1-100%

### Subtask 2

Using all of the resources specified above in the "Task Resources" section, attempt to answer the questions, populating the "Answer" column with the answer, and the "Answered  By" column with "Adobe".

Constraints:

- Skip "questions" that are actually declarative sentences or paragraphs (ending with period, or no question mark)
- Skip questions begining with the word "Why"
- Focus on those that are non-implementation specific. Meaning, you will not be able to answer questions about their custom components, but may be able to answer those that are related to OOTB AEMaaCS functionality, core components, or authoring instructions
