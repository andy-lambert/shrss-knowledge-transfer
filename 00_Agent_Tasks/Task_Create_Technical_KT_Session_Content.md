# Task: Prepare Content for Technical SHRSS Knowledge Transfer (KT) Sessions

## Task Overview

During this task, we will be curating the detailed agendas and content for each technical KT session. We will organize session content into timeboxed blocks to ensure the optimal balance of topic coverage and management of allocated session time.

The sessions will be conducted over Microsoft Teams. Presenters will share their screens to walk through code, Adobe Cloud Service consoles, etc. For exercises, we would like to have one of the participants share their screen and complete a task. For example, have a participant create a new IAM group in Adobe Admin Console (https://adminconsole.adobe.com/), add an IAM user, then add the IAM group to a native AEM group in the DEV author cloud environment.

### Target Audience

The audience for the technical KT sessions are the SHRSS technical stakeholders that are taking ownership of the platform, including new development (new features + defect resolution), system adminstration, and CI/CD. Participating SHRSS stakeholders will include developers, system adminstrators, quality assurance team members, and technical managers.

Some of the participants have minimal knowledge of AEM, some have minimal hands-on experience, and one participant has taken an official Adobe training: `"Develop Websites and Components in Adobe Experience Manager (AEM)"`. An overview of this training is available here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/00_Resources/SHRSS_Training/Develop_Websites_and_Components_in_Adobe_Experience_Manager/Develop_Websites_and_Components_in_AEM_Course_Overview.md`


### Presenters

The KT sessions will be conducted by the following Adobe subject matter experts:

- Andy Lambert – Principal Technical Architect, Adobe
  - AEMaaCS application and cloud service paradigms, DevOps instructions, best practices
- Vinay S A – AEM Technical Architect, Adobe
  - SHRSS implementation details, backend code, configurations, AEM authoring components
- Deepkamal Narang – Senior Technical Consultant, Adobe
  - Frontend code, UX implementation, AEM authoring components

### Agenda

A total of ten (10) hours have been scheduled for technical knowledge transfer, to be conducted over five (days).

I have put together a strawman agenda outline that includes the main topics to be covered, along with some subtopics for each here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/00_Resources/SHRSS_Technical_KT_Main_Agenda.md`

Ideally, this agenda can be organized similar to the following:

| Session(s)                                                   | Duration |
| ------------------------------------------------------------ | -------- |
| Introduction/overview, AEM Application Development Parts 1 & 2 | 2 hours  |
| AEM Application Development, Parts 3 & 4                     | 2 hours  |
| AEM Application Development, Parts 5 & 6                     | 2 hours  |
| Change and Release Managemen, DevOps Part 1                  | 2 hours  |
| DevOps Part 2, Conclusion/Q&A/Customer Topic                 | 2 hours  |

---

## Inputs/Reference Artifacts

- Technical KT main agenda outline: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/00_Resources/SHRSS_Technical_KT_Main_Agenda.md`

- Solution design (Optimized version created post-implementation as part of implementation analysis exercise. Provides context): `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/00_Resources/SHRSS_Optimized_SDD.md`

- Implementation notes: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/00_Resources/SHRSS_AEM_Implementation_Notes.md`

- Implementation analysis: `/Users/lambert/Documents/Projects/SHRSS/Implementation_Analysis_Project/Documentation/Implementation-Analysis/final`:

  - `00_EXEC_SUMMARY.md`
  - `01_STRUCTURAL_ARCHITECTURE.md`
  - `02_CROSS_LAYER_INTERACTIONS.md`
  - `03_SOLUTION_DESIGN_TRUE_UP.md`
  - `04_IMPLEMENTATION_QUALITY_ASSESSMENT.md`
  - `05_INDEX_AND_NAVIGATION.md`

- Source code Git repo (`develop` branch currently checked out. Includes production code and Careers code): `/Users/lambert/Documents/workspace/SHRSS/Customer-Git/shrss-aem-projects`

- Production Content (https://www.hardrock.com, https://reverb.hardrock.com)

  > [!IMPORTANT]
  >
  > Contains pages, experience fragments (XF), content fragments (CF)/content fragment models, configurations/policies, and metatadata schemas for sites currently in production (https://www.hardrock.com, https://reverb.hardrock.com)

  `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0`

  - **Configurations (page templates, etc.), content fragment models, asset metadata schemas:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/conf`

  - **Pages:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/shrss`

  - **Experience Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/experience-fragments`

  - **Content Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-PROD-1.0/jcr_root/content/dam/shrss/cf`

  - **Production Digital Assets (DAM)**
   `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-assets-PROD-1.0/jcr_root/content/dam`

- Stage Content - Careers Site (https://aem.careers.stage.hardrock.com/)

  > [!IMPORTANT]
  >
  > Contains pages, experience fragments, content fragments/content fragment models, configurations/policies, and metatadata schemas for the **Careers** site. The Careers site is currently in customer QA/UAT in their stage environment (https://aem.careers.stage.hardrock.com/)

  `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0`

  - **Configurations (page templates, etc.), content fragment models, asset metadata schemas:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/conf`

  - **Pages:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/shrss`

  - **Experience Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/experience-fragments`

  - **Content Fragments:** `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-content-minimal-assets-STAGE-1.0/jcr_root/content/dam/shrss/cf`

  - **Stage Digital Assets (DAM) - Careers Site**

    - NOTE: The path for Careers asset below points to the **production** assets folder. This is intentional. Assets in this folder are up to date with content on **stage**:

      `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Content/shrss-assets-PROD-1.0/jcr_root/content/dam/shrss/corporate/careers`

### MCP Servers

You have access to the tools/services defined in these MCP servers, currently enabled in Cursor:

- Adobe Developer Assistant (ADA)
  - `ask_ada` tool to search Experience League and internal docs
- singularity
  - `ask_docs` tool to deep search Adobe docs, repos, Jira, Confluence
- MCP_DOCKER
  - Includes browser tools (wrappers for Playwright: https://hub.docker.com/mcp/server/playwright/tools)

---

## Task Details & Execution

> [!IMPORTANT]
>
> Use the resources from the *"Inputs/Reference Artifacts"* section in this document, along with canonical AEM reference files/links in `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/docs/ai/reference` to help refine the session topics/subtopics and information provided during each.
>
> Always adhere to AGENTS.md (`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/AGENTS.md`)
>
> Throughout task execution, maintain detailed notes in AGENT_SCRATCH_NOTES.md (`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/AGENT-SCRATCH-NOTES.md`)

### Subtask 1 - Refine the Agenda

Analyze the strawman agenda `(/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/00_Resources/SHRSS_Technical_KT_Main_Agenda.md`). Based on the target audience, the SHRSS implementation, etc. make opinionated recommendations for enhancing/optimizing the agenda by recommending additional topics/subtopics, order of topics, and any other ideas that come to mind. Think both from the perspective of an AEM expert and of the SHRSS stakeholders that will ultimately own the code and the infrastructure (i.e. the SHRSS platform in AEMaaCS (Cloud Manager + Admin Console)). What will they need to know?

Create a new copy of the agenda file and populate with the refined agenda. Pause and prompt me to review the refined agenda along with any questions or points of clarification. I will review, provide feedback, and then we can either refine futher or move on to the next subtask.

### Subtask 2 - Create & Timebox Detailed Session Content

> [!IMPORTANT]
>
> I have copied the refined agenda here: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content/SHRSS_Technical_KT_Main_Agenda.md`. We will refine this version into the final main agenda draft. It is essentially complete. We just need to update with the topic/subtopic durations that we come up with during this subtask.
>
> NOTE: I also copied the exercise supplemental file to this directory. Please place all newly generated files in this directory (`/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/Technical_KT_Session_Content`)

First, take an initial pass at timeboxing each topic/subtopic for each session. Update the main agenda document, adding durations after each topic/subtopic.

Next, for each session in the main agenda, create a separate markdown file. Populate each file with the respective session topics/subtopics from the main agenda file, and then create/add content for each topic/subtopic to provide as comprehensive an understanding of the topic/subtopic as possible given the time constraints (proposed durations). As you go, adjust topic/subtopic durations and content to achieve the best possible balance across all.



