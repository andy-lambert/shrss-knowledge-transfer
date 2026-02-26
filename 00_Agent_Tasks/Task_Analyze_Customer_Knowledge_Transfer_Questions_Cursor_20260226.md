# Task - Analyze Customer Knowledge Transfer (KT) Questions

## Task Objective

Flag KT session questions that are likely AI-generated, providing level of confidence and reasoning.

## Contextual Information / Background

To date there have been 543 questions submitted for the nine sessions held to date. That is an inordinate number of questions given the number of participants and sessions. The vast majority of the questions were submitted by the stakeholder for which your persona was based for the "session participation" task, and were submitted late in the evening hours after the each session after we provided the session recording and transcript. 

For one session, "News", we didn't send the recording/transcript. Tellingly, we only received four total questions for the "News" session, and those were all submitted by a differerent participant within minutes after the session ended. Note that "News" functionality is a very high priority topic for SHRSS. If the "Shared Data" session had 97 questions, "News" should have had 100!

Many of the questions are highly relevant and important in terms of timely, accurate follow up by Adobe. However, the majority constitute noise:

- Duplicate question phrased differently (indicating the question was asked by a human, then also formulated by AI)
- Questions formulated from chunks of dialog, or from a couple of sentences spoken by the host or a participant, but not really clear contextually or representative of the issue/topic being discussed
- Ambiguous/vague in nature

**Examples of reformulating questions from transcript snippets:**

| Question                                                     | Transcription snippet                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Is there any scenario where delivery links would be **internal** instead of **external**? | **Daniela Tea** 9:56 (Part 1) So. So for this particular section, everything is going to open up a new<br/>window. I I don't think these are ever going. **These would *<u>never</u>* be like<br/>an <u>internal</u> link, right**? So I believe that's why it was just baked in.<br/>These are always like 90. Like **I can't imagine an instance where this<br/>would be an internal link**. So it's it's baked into the component to<br/>automatically. |
| **Lisa Cardia** 10:57 (Part 1) **When a new location's added to the DPLT**, this part **is delivery only<br/>would be checked** if the author **manually** went in and did it right. Like<br/>we wouldn't. OK, that was my first question and my second one was not<br/>to derail from delivery, but we quickly glanced over the image. | **When a new location is added to DPLT**, does the author need to **manually** check “Is Delivery”? |
| Are delivery links automatically configured to **open in a new tab**? | Lyon, Rick (Director of Digital Experience)** 9:38 Sorry, I was still muted. I didn't see an option to open the links in a<br/>new window, so I assume that they will all **automatically** open in new<br/>windows. **Daniela Tea** 9:39...it<br/>**opens up in a new tab,** yeah. |

**Other Examples:**

Multiple technical/AEM terms; formal/AI-style phrasing; long,  formal question; typical AI-generated taxonomy question:

> What is the current intended taxonomy architecture under the  SHRSS namespace (Categories, Category, Event Categories, Properties, Property  Names, etc.)?

Long,  formal question; phrases match transcript (reworded into question):

> How do we dynamically query and display events in other  components (carousel, grid, homepage modules) outside of the Event Calendar  component?

Combines AEM terms into a question that into a non-sensical question. Out of context. Too technical for the stakeholder to have asked:

> To what extent do CF‑ or XF‑driven pages get indexed differently?
>

AI-phrasing, too technical in wording

> What is the versioning strategy for XFs used on multiple sites  with different publish cycles?

## Task Detail

I have copied all session questions into a single sheet named "All_SHRSS_KT_Questions" in this workbook: `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/KT_Session_Question_Analysis/SHRSS_KT_Session_Questions.xlsx`. The second column (*"Session"*) in the sheet maps each **question** to its corresponding **KT session**. See the table below for `"Session"` column values and transcript session section headings:

| Session Section Heading in Transcript                        | "Session" Column Value        |
| ------------------------------------------------------------ | ----------------------------- |
| Session: Jobs — 2026-02-10                                   | Jobs                          |
| Session: Events — 2026-02-11                                 | Events                        |
| Session: Careers — 2026-02-12                                | Careers                       |
| Session: Tagging & Taxonomy — 2026-02-17                     | Tagging_Taxonomy_Metadata_Gov |
| Session: DAM — 2026-02-18                                    | DAM_Training_Usage_Admin      |
| Session: Shared Data — 2026-02-19                            | Shared_Data                   |
| Session: News — 2026-02-20                                   | News                          |
| Session: Locations — 2026-02-23; Session: Locations, Day 2 — 2026-02-24 | Locations                     |

Analyze the questions in the sheet and identify those that are likely to have been generated by AI (ChatGPT, Microsoft Copilot, Claude, Perplexity, etc.). For those that qualify as potentially AI-generated:

- Populate the *"AI-Generated"* column with *"TRUE"*, otherwise populate with "FALSE"
- Populate the *"Confidence"* column with a percentage ranging from 1-100% indicating level of confidence that the question was AI-generated
- Populate the *"Reasoning"* column with a summary the reasoning for why the question was identified as likely AI-generated, as well as for the assigned confidence percentage value

In addition to the reasons and examples given above, use these guidelines to help identify candidates:

Do a **deep cross analysis of each question with its corresponding session dialog** in `/Users/lambert/Documents/Projects/SHRSS/SHRSS_Knowledge_Transfer/KT_Session_Transcripts/SHRSS_Adobe_KT_All_Session_Transcripts_Consolidated.md`. **This is important**, because most of the AI-generated questions appear to have come from rewording content into questions.

Also include in your consideration (but do not limit to):

- AI-type wording and phrasing (consider the markers that hint at ChatGPT, Microsoft Copilot, Claude, Perplexity, etc. specific responses)
- Highly technical, architectural (remember that the stakeholder participant that submitted the suspect questions is non-technical and does not know AEM to any degree of depth)
- Too deep into AEM technology, AEM buzzwords (example: Sling model, OSGi, query builder, search index)
- Irrelevant to session topic
- Illogical or nonsensical

Maybe before starting, do some quick research on forensic/linguistic methods, classic signs and signals, etc.

