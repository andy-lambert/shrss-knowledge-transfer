# Task - Analyze Customer Knowledge Transfer (KT) Questions

## Task Objective

Categorize and, when possible, answer the questions submitted to Adobe by the customer following each of the knowledge transfer (KT) sessions, flagging those that are too ambiguous or require more information/context to be meaningfully, accurately addressed. In addition, flag questions that are likely AI-generated.

## Background for Context (IMPORTANT! Do not skip.)

Adobe Professional Services is providing the SHRSS customer with a set of knowledge transfer (KT) sessions to enable their authors and DAM admin/architect/librarian with the skills and information they need to effectively:

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

### SHRSS AEMaaCS Implementation Documentation

Complete end-to-end analysis and technical documentation for the current SHRSS implementation.

See all markdown files under`/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`:

- `00_EXEC_SUMMARY.md`
- `01_STRUCTURAL_ARCHITECTURE.md`
- `02_CROSS_LAYER_INTERACTIONS.md`
- `03_SOLUTION_DESIGN_TRUE_UP.md`
- `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md`
- `05_INDEX_AND_NAVIGATION.md`

### SHRSS AEM Content

#### Prod Content

> [!IMPORTANT]
>
> Contains pages, experience fragments (XF), content fragments (CF)/content fragment models, configurations/policies, and metatadata schemas for sites currently in production (https://www.hardrock.com, https://reverb.hardrock.com)

`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`

- **Configurations (page templates, etc.), content fragment models, asset metadata schemas:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/conf`
- **Pages:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/shrss`
- **Experience Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/experience-fragments`
- **Content Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/dam/shrss/cf`

##### Prod Assets (DAM)

> [!IMPORTANT]
>
> Can analyze referenced assets in questions pertaining to particular component/image display issues in pages and experience fragments, for example. (Based on image or other component configurations on the specific page or XF)

`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-assets-PROD-1.0/jcr_root/content/dam`

#### Stage Content - Careers Site

> [!IMPORTANT]
>
> Contains pages, experience fragments, content fragments/content fragment models, configurations/policies, and metatadata schemas for the Careers site. The Careers site is currently in customer QA/UAT in their stage environment (https://aem.careers.stage.hardrock.com/)

`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0`

- **Configurations (page templates, etc.), content fragment models, asset metadata schemas:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/conf`
- **Pages:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/shrss`
- **Experience Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/experience-fragments`
- **Content Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/dam/shrss/cf`

##### Stage Assets (DAM) - Careers Site

> [!IMPORTANT]
>
> Can analyze referenced assets questions pertaining to particular component/image display issues in pages and experience fragments, for example.

NOTE: The path for Careers asset below points to the **production** assets folder. This is intentional. Assets in this folder are up to date with content on **stage**.

`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-assets-PROD-1.0/jcr_root/content/dam/shrss/corporate/careers`

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
  - MCP_DOCKER
    - Includes browser tools (wrappers for Playwright: https://hub.docker.com/mcp/server/playwright/tools)



## Task Details

You are a seasoned, expert Adobe Experience Manager (AEM) / AEM as a Cloud Service (AEMaaCS) senior technical architect/developer with a deep understanding of the SHRSS AEMaaCS implementation (based on access and analysis of the resources provided in the *"Task Resources"* section above)

For this task, you will be analyzing and updating the "Research" spreadsheet in the Excel workbook here: `/Users/lambert/Documents/Projects/SHRSS/KT_Session_Follow_Up_Questions_RESEARCH_WORKING.xlsx`

I would like for you to analyze the questions in the spreadsheet and attempt to accomplish **two distinct goals**, defined below as subtasks to be completed in order.

> [!IMPORTANT]
>
> **Non-negotiable**
>
> Before starting:
>
> 1. Review and always adhere to the rules, instructions, and other information in @AGENTS.md (`/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/AGENTS.md`)
> 2. Review the following SHRSS AEMaaCS implementation architectural documents in `/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`:
>    - 01_STRUCTURAL_ARCHITECTURE.md
>    - 02_CROSS_LAYER_INTERACTIONS.md
> 3. After reviewing the rest of the task as defined below, pause, provide me with a summary of your understanding of the task/subtasks along with any questions or required points of clarification. I will review, provide feedback, and give the go ahead and to proceed with task execution.

### Subtask 1 - Identify AI-Generated Questions

The questions are listed in the "Research" sheet in this Excel workbook: ``/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/KT_Session_Follow_Up_Questions_RESEARCH_WORKING.xlsx``.

Identify the questions that are likely to have been generated by AI (ChatGPT, Microsoft Copilot, Claude, Perplexity, etc.). For those that qualify as potentially AI-generated:

- Populate the *"AI-Generated Question?"* column with *"TRUE"*
- Populate the *"Confidence"* column with a percentage of how confident you are that the question was AI-generated ranging from 1-100%
- Populate the *"Reasoning"* column with a short summary explaining why the question was identified as likely AI-generated and for the assigned confidence percentage value.

#### Cross-Reference Session Questions and Transcripts

It appears that the author instructed AI to analyze the transcripts and derive questions by both **repeating/rewording any question asked during the session**, and **making up additional questions based on the transcription content**.

Do a deep cross analysis of each question with its corresponding session dialog in `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md`.  Look for matching phrases, multiple matching words used in a sentence, etc. to identify where snippets were taken from the transcript and fed to AI.

The first column (*"Session"*) in the questions sheet matches each **question** to its corresponding **KT session**. See the table below for `"Session"` column values and transcript session section headings:

| Session Section Heading in Transcript    | "Session" Column Value        |
| ---------------------------------------- | ----------------------------- |
| Session: Jobs — 2026-02-10               | Jobs                          |
| Session: Events — 2026-02-11             | Events                        |
| Session: Careers — 2026-02-12            | Careers                       |
| Session: Tagging & Taxonomy — 2026-02-17 | Tagging_Taxonomy_Metadata_Gov |
| Session: DAM — 2026-02-18                | DAM_Training_Usage_Admin      |
| Session: Shared Data — 2026-02-19        | Shared_Data                   |
| Session: News — 2026-02-20               | News                          |
| Session: Locations — 2026-02-23          | Locations                     |

#### Additional Considerations

Also include in your consideration (but do not limit to):

- Wording and phrasing
  - AI-centric (consider the markers that hint at ChatGPT, Microsoft Copilot, Claude, Perplexity, etc. specific responses)
  - Highly technical, architectural
  - Too deep into AEM technology, AEM buzzwords (example: Sling model, OSGi, query builder, search index)
  - Irrelevant to session topic
- The supposed "author" of these questions is an AEM author. Not technical, beyond some limited level of UX design and frontend development. NO understanding of HTL, or other AEM technical paradigms

### Subtask 2

Using all of the resources specified above in the "Task Resources" section, attempt to answer the questions. For those that you can confidently answer, populate the *"Answer"* column with the answer, and the *"Answered By*" column with *"Adobe"*.

For each question, as applicable:

- Analyze the specific page, experience fragment, content fragment or configuration in the relevant content directory (refer back to the *"SHRSS AEM Content"* section above), and related assets as needed in the assets directory/directories.
- Analyze corresponding code in the Git repo
- Search Adobe resources via the MCP servers
- Use the browser tools in the MCP_DOCKER MCP server review page in production (https://www.hardrock.com, https://reverb.hardrock.com) and stage (https://aem.careers.stage.hardrock.com/)

**Constraints:**

- Skip questions that are actually declarative sentences or paragraphs (ending with period, or no question mark)
- Skip questions begining with the word "Why"
