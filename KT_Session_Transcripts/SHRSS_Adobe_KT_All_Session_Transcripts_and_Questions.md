---
title: SHRSS Adobe Knowledge Transfer — All Session Transcripts (Consolidated)
source: KT Sessions (Microsoft Teams meeting recordings)
sessions: Jobs, Events, Careers, Tagging & Taxonomy, DAM, Shared Data, News
dates: 2026-02-10 through 2026-02-20
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

# SHRSS Adobe Knowledge Transfer — Consolidated Transcripts


## Session: Jobs — 2026-02-10

**SHRSS Adobe Knowledge Transfer-20260210_130301-Meeting Recording**

February 10, 2026, 6:03PM

1h 53m 23s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:11 All right folks, thanks for joining this afternoon and being patient
while we've been working out the the logistics to to get these
knowledge transfer sessions on the calendar and I think we're we're in
a good enough consensus between Adobe and SHRSS leadership that we can
get these. These started. So given that Daniela T is going to be running this
session, I think we're putting the early sessions with a focus on
careers, you know, with the jobs components that we have. Given the careers work stream that's happening in parallel. So with
that, Daniela, is there anything else you need me to kick off before you
start?

**Daniela Tea** 0:56 I think Luke, if we just want to remind everyone that for the end of
these sessions we'll be having essentially like a gap analysis phase,
if you just want to mention that really quickly.

**Lucas Nelson** 1:10 Yeah, no, that's a good point. Both individually to Daniella. It's
worth noting on these calls that we're going to have, we'll get
through our material that Daniella has, you know. Created and and and reviewing with you guys and we'll have each session
will have a a little bit of a retrospective Q&A for one. But what
Danielle is talking about as well is the intention at the end of these
knowledge transfer sessions. Is that that there there's a oh, I heard some back feed. Sorry. OK,
cool. At the at the end of these knowledge transfer sessions the the
last week or so of the seven week schedule. We're going to be supporting you know Seminole Hard Rock you you guys
with with with filling in the backlog for gaps and noted functionality
that that you you would have documented from having these this baseline
knowledge transfer. Work stream that we have so so we we can put together together the you
know full list or as comprehensive as a list as we can of the of the
gaps that the platform doesn't currently have implemented.

**Daniela Tea** 2:17 Yeah.

**Scott Sorel** 2:21 Yes.

**Lucas Nelson** 2:35 And so that's the, that's the intention that we want to get to the
desired outcome from these knowledge transfer sessions. So Danielle,
thanks for calling that out. And if there's other questions on that,
Scott, as we're going through these sessions, you and I can work to,
you know, make sure we address them. OK, Scott.

**Scott Sorel** 2:55 Yes, Sir.

**Lucas Nelson** 2:57 Alrighty, Danielle, anything else before I hand it to you?

**Daniela Tea** 3:01 Yep, I think we're good to go. So let me go ahead and share my screen
and we can get started. Um, let's confirm.

**Lucas Nelson** 3:03 Alright, thanks.

**Daniela Tea** 3:09 If you guys can just confirm you guys can see my screen, we should be
looking at a Conflence page.

**Lisa Cardia** 3:16 Yes.

**Scott Sorel** 3:17 Yep, looks good to me.

**Daniela Tea** 3:18 Perfect. Thank you guys. All right. So thank you everyone. Good
afternoon. Today what we have planned is to review the job-related
components specifically because we are aware of the fact that the
careers website, the intention is to have that to be going live sometime
next month. I know.

**Scott Sorel** 3:19 Yeah.

**Daniela Tea** 3:38 That currently it's in the QA phase with SHRSS team. So today what
we'll be reviewing are those job components as well as the job content
fragment, which is the data source for essentially all of these
components. Earlier this week I had also posted. Some additional agenda items for some future sessions. To be clear, the
the reason why we I selected these here is because I wanted to make sure
that we had time to really get into the content fragment driven
components. So we will have of course additional agendas, additional sessions which
will cover other items. Want to make sure that you were aware that the
items I'm trying to prioritize first in these this first week of
sessions are things related to content fragments. So taking a quick quick look at this Confluence page, the other thing I
wanted to call out is that what our intention is, is we understand that
you may have questions about the components or you know, just just some
some things you might need to verify with us. And what we're asking you to do is if you are able to come up with
those questions during the session or if we run out of time, we would
like for you to gather those questions within the specific Confluence
page for that session. So for example, anything that you may think of
when it comes to jobs while like say you're eating dinner tonight or
something if you could. Please just add a comment to this page. What our team will be doing is
we will be reviewing the questions and our goal is to be able to either
answer them directly within this Confluence page or if it's something
that needs to be, say, demonstrated further, then we want it to allocate
some time. Just going to go to this next. Agenda here allocate some time at the beginning of each future session
to to review those questions and and make sure that you get those
updates. So that's what we're just asking for this team here is any
questions that you may have, please make sure to add it to the specific
Confluence page. All right. OK, so let's go ahead and get started. I am now going to
navigate to the stage environment. And we're going to take a look at our jobs content fragment. All right,
so here I am in stage and I'm going to go to Assets and Files and I'm
going to go to the SHRSS folder. And then the content fragments folder. Here we can see here there is a
folder called jobs and what I wanted to point out is that this jobs
folder will contain all of the jobs that are coming in from Workday. So
what you see here are essentially a folder structure. That will show, say, like the country US, you'll see like the state, in
this case Florida, and then you'll see the location or the property
name. And then from underneath there will be all those related job
postings for that specific location. So to be clear, all this here that
you see is actually coming. In from Workday, this is not something that an author has created. So in
terms of like adding a new job post or something, my understanding is
that this is supposed to be from Workday and so this you'll see here
that this will continuously be modified and published as the sync is
being run from the connection. Between Workday and AEM. So you might notice that some folders do not
have anything in them, and that's because what might have happened is
there were previously jobs for this location. However, those jobs may
have been removed in Workday for whatever reason, so the folder
structure will still be intact in AEM. However, the job postings content fragments will no longer be available.
And to be clear, we're on the stage environment and right now we are
connected to, I believe, the QA API for Workday. So these jobs, of
course, there's certainly much more jobs available. Once we make the connection to prod, however, right now down in stage
and as the QA team is doing their testing, you're going to see a a much
smaller subset of jobs. So this will certainly be much bigger once we go
to production. Right, so now I'm just going to navigate to a folder and I'm just
using Tampa because I was looking at this earlier and there's multiple
jobs. I'm going to open up one of these content fragments, so selecting
it and then clicking on edit. OK. And let's take a look at each of these different fields. Some of
these fields again are going to be coming from Work Day and some of
these are actually going to be something that the author would consider
updating. So let's walk through each one of these. And then what we'll do is we will map these fields to some of these job
components to see how the information is actually being displayed to the
end user. So I'm actually going to zoom in just a little bit so
everyone can see. All right. So we see here the job ID, job unique ID. These are coming in from
Workday. Here we have our image field. This is something that is not
going to come from Workday and it's something that's going to be
inputted by the author.

**Don Middlebrook** 9:12 OK.

**Daniela Tea** 9:14 There is a way, yes.

**Mayte Eme** 9:14 Question you have two ID's. You have job unique ID and then you have
job ID. Which one are you using?

**Daniela Tea** 9:24 So right now this is both information coming in from Workday. What's
being displayed to the end user is going to be the job ID.

**Mayte Eme** 9:31 OK, that's the wrong one.

**Daniela Tea** 9:33 So that I'm aware that there is a ticket, I believe that mentions the
job ID. This is something that I believe our developers have taken a
look at. So if that needs to be updated, that is something that will be
handled with that ticket.

**Mayte Eme** 9:48 OK, and then this image thing you meant that's not mapped to pick up
automatically the right image like we currently have right now.

**Daniela Tea** 9:57 So right now what I'm showing you is the actual image field within the
content fragment. Later on in this session, we're going to take a look
at the image configuration page where you would be able to set up the
images for all the locations in advance. However, keeping in mind that
we are aware that in some instances. Images might need to be overwritten by the author and or. We've also
seen on the live site itself that some some job job postings do not have
images at all. So this here is a way for the author to be able to
overwrite whatever is coming from that configuration page and or remove
an image entirely if that is desired.

**Mayte Eme** 10:38 OK. Thanks.

**Daniela Tea** 10:39 Yep, we'll take a look at that image configuration page shortly. Yep.
OK, so let's keep going down to the remaining fields that we have in
our content fragment. So we see here.

**Lisa Cardia** 10:50 But Daniella, sorry, sorry to interrupt, but regarding the image, how
you said we have the option to override and I am aware that there's the
the mapping with the configurations. Does the override replace the image
we see on the card and the listing or just the card? if we if we choose to override it.

**Daniela Tea** 11:10 If you choose to override it, it should update the image that's used in
the job listings component, which is the cards I believe you're
referencing, and then also the job search component which lists the
results as like longer horizontal cards.

**Lisa Cardia** 11:26 OK, all right. Something we'll take back then because we typically do
two different like logo on listings, property shot on let's say
homepage and the hiring events page. So just want to make or hot jobs
page I guess because that's what's pulling in.

**Daniela Tea** 11:27 So that's so this is Yep. OK.

**Lisa Cardia** 11:42 So I'll just note that and we can move forward. Thanks.

**Daniela Tea** 11:42 OK. Okay, sure. All right.

**Mayte Eme** 11:46 And one more thing when because this there's a sync right that I guess
runs every so often. If there's an update to the job and you've over
reading something, I assume that doesn't get updated again after the
sync or we lose the override.

**Daniela Tea** 11:52 Yes. So the only fields that get over that would OK, so just to be clear,
anything that's coming from workday. So we're going over those workday
fields, those will get overwritten by workday. However, the field say
for example image and then another field down here for hot job and the
LD JSON field we've seen on our content fragments, these. These are not fields that are coming in from Workday. So if you set this
or if you put an image, nothing from Workday will overwrite that.
However, if you try to say add additional content here or any of these
other fields then that will get overwritten by Workday.

**Ramona Harris** 12:36 Daniella, a quick question. As far as the size for the logo image, I see
two different sizes. What is the standard size of the logo that should
be uploaded?

**Daniela Tea** 12:45 Yeah. So that is still information that I think we would need to get
back to you on. As of right now, we were using, I believe, whatever was
already in the dam for the Sage website. So we don't have those exact
measurements at this moment.

**Ramona Harris** 13:02 OK.

**Daniela Tea** 13:04 It. OK, so let's keep going here. So as mentioned earlier, these other
fields, job title, job portal, URL, etcetera, all the way up to here are
going to be coming in from Workday. You'll notice this toggle that says
is API data. This is signifying that this. Particular content fragment is something that's coming in from Workday,
and so again, it's going to overwrite this information. When we've
initially wrote the requirements for jobs content, we were informed that
there have been some instances where say a job. Not necessarily like a job that would be coming in from Workday or ISIMs
in your current instance, but you might need to have a job posting
that's created by an author. If that's the case, you can. You do have
the ability to do that. This would not be turned on because this is
not. This is not coming in from any sort of API. However, that was one of the
use cases that we have previously heard when we were documenting
requirements. So to be clear, you can create a job as an author.
However, these are here that we all see currently right now within stage
are all going to be jobs that are coming in from. Work day.

**Mayte Eme** 14:22 And how would you do that? Do you just?

**Daniela Tea** 14:26 So if you just wanted to create a new job yourself, you can do create
and then do content fragment and then you could select jobs with the
title test job CF create.

**Mayte Eme** 14:26 Uh.

**Daniela Tea** 14:41 And then you would just fill out all that information yourself.

**Mayte Eme** 14:46 And is there any feed of the category so it goes with the other ones? So
you have to know them. Those are not drop downs, right?

**Daniela Tea** 14:54 These are not dropped up, correct. These are not drag downs because
these were the under. The understanding is that these are supposed to be
coming in from work day. So if you did need to match something, you
would need to make sure that you had the exact category like in this
case casino sales.

**Mayte Eme** 15:10 OK, so you have OK.

**Daniela Tea** 15:12 Mhm. Hang on a second. OK, sorry, something from teams just popped up. All
right, so let me go back to.

**Mayte Eme** 15:21 Is there? Sorry to ask again, but just checking. Is there a schedule?
Like if you're adding a job, as soon as you publish, it goes live.
There's no scheduling, right?

**Daniela Tea** 15:24 Yep. So if you have published, I'm going to click on publish here. You can
see there's the now functionality and then there's the schedule. So
when you click on schedule and you can have the activation date. So and
to be clear though, I might say and because these are all coming in from
workday, they do get published as they're like.

**Mayte Eme** 15:38 Oh. Um. Oh.

**Daniela Tea** 15:51 Coming into AEM, but I guess are you asking specifically for like a like
a authored content fragment? OK, yeah, so you do have the ability to to
schedule content fragments, but in the case of jobs, anything from
Workday is going to get published without any intervention from the
author. Like you can see this just got.

**Mayte Eme** 15:53 Mhm.

**Daniela Tea** 16:10 Modified 6 minutes ago is another one and published 6 minutes ago
because it's coming in from that API.

**Mayte Eme** 16:17 And they drop off based on workday, right? If it's manual, there's no
drop off. You have to manually delete it.

**Daniela Tea** 16:24 That is correct, yes.

**Lucas Nelson** 16:26 Gonzalo has his hand up, Daniella.

**Daniela Tea** 16:27 Yeah, go ahead, Gonzalo.

Gonzalo Calasich (SHRSS)** 16:33 Hi, can you guys see me?

**Daniela Tea** 16:34 Yes.

Gonzalo Calasich (SHRSS)** 16:36 Yeah, following on my test question. So so the the way this process
works is that you wipe out all the job postings every time that you do a
sync.

**Daniela Tea** 16:51 Sorry, cause I'll what was the sorry, what was the question?

Gonzalo Calasich (SHRSS)** 16:54 Once again, so every time that you do a sync from work day, do you
delete all the job postings from Adobe?

**Daniela Tea** 17:01 Oh, are you talking like, does an author have to manually delete all of
this? Is that what you're asking?

Gonzalo Calasich (SHRSS)** 17:06 No, what I'm trying to understand, for example, let's say when a job
is no longer active and should no longer should be showing the website,
I mean that that needs to happen from work day. So let's say this work,
this, this job posting is already fulfilled and work day they will do a
change.

**Daniela Tea** 17:11 Oh. Yes, that. Hmm.

Gonzalo Calasich (SHRSS)** 17:23 And that will not be part of the sync. So that means that next time the
sync runs, that job will automatically be removed, correct?

**Daniela Tea** 17:32 That is correct, yes. And I'm not sure if you if you were part of the
discussion earlier, but for example, like this immocally folder is here,
but there's no jobs underneath. When this was initially set up, there
were likely going to be there were likely jobs that were here. So just
to be clear, do we not set up any of these? These are coming. Directly from Workday, so the folder structure will remain intact, but
the job postings will come and go depending on what is happening in
Workday.

Gonzalo Calasich (SHRSS)** 18:02 OK. Thank you.

**Daniela Tea** 18:03 I am going to now go back to our content fragment and I want to just
also highlight one thing that you could see here. What I'm showing here
right now is the city, the state, the country. And I'm just going to drag it to the right and have the folder
structure here on the left. So as you can see, the way that this folder
structure was set up is based off of the information that's being that
was coming in for this particular job. So we can see here US job location country US you can see FL FL is the
state and then for the city is Tampa and so Tampa is right here and
that's why this particular job 6150. Here is located in there. So every single job post that you see here is
going to be sorted based off of their country, state and then city. So
that's how this was created. Alright.

**Mayte Eme** 19:06 One more question about this thinking. There's been situations where we
had to remove a job. It takes a while for ISAMS to do it. I don't know
about workday, but we had to immediately hide it from the website. Is
there that? Do we have an option to do that?

**Daniela Tea** 19:22 So. An author could technically delete a job, but to be clear, because of
the sync and it's going to constantly republish, that's obviously not
a viable solution. So your question is, would you be able to say say
this particular job is no longer something that you need to show right
now? And and you want to make sure it's hidden. At the moment, I don't
think you would be able to just simply remove it because the sync is
continuous and the expectation is that all of the changes would be
coming in through work day versus happening in AM.

**Mayte Eme** 20:00 Right. But there's been situations that it takes a while, especially on
weekends, right, to remove a job where they won't reply until Monday or
you can get hold of somebody and we need to remove that posting. So we
can do that in cycle, but seems an E and we we don't have that yet.

**Daniela Tea** 20:15 Yeah. So Macy, let me check with the development team to see if like for
example, if we were to say turn off the as API data, is that something
that could potentially say freeze the sync? So let me check in with our
development team tomorrow. We can capture this as a question and then in
our next session I can get back to you on their response.

**Mayte Eme** 20:35 OK, it doesn't happen quite often, so don't like freak out, but it's
happened enough that we had to do those emergency things that wouldn't.

**Daniela Tea** 20:35 Once. Yeah, understood. Right. And sorry, just out of out of curiosity, curiosity might say who
who updates the jobs and work like is that your team or is that a
completely different team?

**Mayte Eme** 20:58 Well, before it.

**Ramona Harris** 20:59 That would be me, Danielle.

**Daniela Tea** 21:01 But sorry, who was speaking? Sorry, I couldn't see.

**Ramona Harris** 21:05 Oh, no, that would be me.

**Lisa Cardia** 21:06 Yeah, so well, so Mona, yeah, yeah, I'd I'd say the content team does
part of the equation, which is getting a a hiring event and a hot job
posted on the home page as well as where it feeds into the other two
pages.

**Daniela Tea** 21:06 OK.

**Mayte Eme** 21:07 Yes, it will be Lisa's team week.

**Daniela Tea** 21:21 Uh.

**Lisa Cardia** 21:21 But our team doesn't manage any of the actual work today job postings.

**Ramona Harris** 21:27 Right.

**Daniela Tea** 21:27 OK. OK. So so basically like all this information that's coming in from
Work Day, that's not your your team's responsibility, Lisa, but making
sure it's appearing on certain pages like displaying as like a card
that is your team's responsibility, is that right?

**Lisa Cardia** 21:28 Right.

**Mayte Eme** 21:42 No, Lisa's team. I mean, yes and no. Yes, of course they're supposed
to make sure they're they're displayed, but she does. She's not
responsible for functionality, right? She's just making sure the
events, the hot jobs are tagged properly, but making sure these plays
that will be product, right? Which we don't own this yet, so I would
say IT.

**Lisa Cardia** 21:42 Correct. Oh, well, yeah.

**Daniela Tea** 21:44 Oh. Uh.

**Mayte Eme** 22:01 Until it's transferred.

**Daniela Tea** 22:06 OK. All right. OK. So we'll get back on that question about the the,
the not as common edge case, but still something that you guys have seen
Mayte where you need to remove a job. I'll get back to you guys on on
that for tomorrow. Now what I want to do is essentially show how this content fragment is
going to display within our job components. So I am going to switch over
just to a page that I created. This is within the careers section of the
site. And So what I'm going to do is I'm going to go through this page, but
we can also create a brand new page and add these components as well so
you can see how they look like when you are initially configuring. But
for this particular purpose, I do want to show how these fields map to
something that's already configured. OK, so this here is our job search component. We have 1/2, just counting
how many components we have 3-4. We have four different job components
which is dependent on this content fragment. So the job listing one as we know is on the I'm sorry, the job search
component as we know is on the search page. So let's take a look at
what our content fragment maps to. So here we have the job ID which is
currently being posted right here. My understanding is it should be
something different. It seems like it should be the unique ID, but again, this is something
that was captured within a JIRA ticket so our team can take a look at
it. But you can see for right now it's pointing to the job ID. We have
our image field. In this case this one was authored by someone and you
can see there are instances where you don't have an image and there are
instances. You do if you do have an image and it will display here to the left. We have our job title, so casino host. I'm gonna actually find casino
host on here. Here we go. Casino host. The job portal URL is the
destination link when you click on the on actual. Results the updated date. We take this and we post the duration of time
since it has been since the job was available. So in this case this is
about a month ago. We have our job category casino sales also listed
here. On the results, job type full time. This is not something that's listed
on the result, but it is something that affects the filters. Job types
full time. Then we have the address and we showed how the address does
dictate the. Folder structure that's in the DAM. And then we have here the job properties, Seminole Hard Rock Hotel and
Casino Tampa. And here's an example of how the job property is
displayed here within the results. Those fields are also going to affect
the filters as we saw before job category. It is in this section. Select properties. These are all the ones where
results are existing. Select locations. This here is a combined field
based again off of the. In this case this is the country. So in this case this is Canada, but here we you know US the job
location, state and then also the city. So that this is a concatenation
of those 3 fields. I'm going to pause here and see if there's any
questions. On how the content fragment fields map to the job search component.

**Mayte Eme** 25:54 Notice.

**Lisa Cardia** 25:55 Just me again. Oh, sorry, my turn. If you want to go, it doesn't
matter. You can go ahead. OK. I was just gonna say to reiterate all of
the the fields that you just mentioned if we were to override if needed.

**Mayte Eme** 25:58 Yeah. Go, Google.

**Lisa Cardia** 26:10 They'll get overridden when the sync happens again. Just to be clear,
it was what 3 fields don't get overridden. I guess the the point is
like, I don't know if we should touch these if it's gonna resync every
what, 30 minutes? Like does that?

**Daniela Tea** 26:13 Yes. The fields that.

**Don Middlebrook** 26:21 G.

**Daniela Tea** 26:22 The only so the fields that an author can touch and would not get
overwritten by sync is this image field and then also the is hot job and
that's sorry, just realized this is one thing. So these three of course
have the is hot job toggle set and that would be something that comes
from an author.

**Lisa Cardia** 26:43 Yes. So it was just, it was just Image Field and hot job.

**Daniela Tea** 26:49 Yes, that's correct.

**Lisa Cardia** 26:51 You said three, so I just want to make sure if I.

**Daniela Tea** 26:53 So LD JSON also that's that's not something that's going to be
displayed here, but just want to be clear, this is something that is
included. I believe in the other content fragment models again not
coming in. This field is not going to have any information coming in
from Work Day. It is something that an author could author if needed, so
this would not get overrated. Neither.

**Ramona Harris** 27:16 Daniella, are the select locations under the job search component? Are
those locations pulling in from AEM?

**Lisa Cardia** 27:17 Got it. Thank you.

**Don Middlebrook** 27:19 Sh.

**Daniela Tea** 27:22 Yes. You're talking about this portion? Yes, yes. So this here is coming in
from. It's a combination of the country field, the state field, you can
see FL and then the city field. Let me find Tampa. Here we go. So.

**Ramona Harris** 27:29 Yes. And that was pulling in from OK. OK. I was just asking because I didn't see Ottawa on the back end of
AEM and I was.

**Daniela Tea** 27:46 US I fell in Tampa.

**Ramona Harris** 27:54 That just brought to my attention because I was thinking if there's a
new property, is the author responsible for adding that property and
then that property will pull into this area here under select locations
as well?

**Daniela Tea** 28:07 So when new properties are created, so let's say in work day, I guess a
a new property is created and a new job is created for that property.
That folder structure should be because this because these content
fragments.

**Ramona Harris** 28:10 OK.

**Daniela Tea** 28:23 Are being populated from Workday. What's happening is the folder
structure is set up based off of those fields as well. So an author
would not have to create this, nor would an author have to update
anything in this section because this is all coming in from the fields
that are within the content fragment.

**Ramona Harris** 28:42 OK. OK. Thank you.

**Daniela Tea** 28:43 Yeah, and I see Don's hand up, I think.

**Don Middlebrook** 28:47 Yeah, so for the image component, you may have already said this, but so
where exactly is that image coming from? Is it coming from workday? How
is it authored?

**Daniela Tea** 28:50 Mhm. Oh, so yeah, so this particular image.

**Don Middlebrook** 29:01 It's uh, it's it is in the dam, so.

**Daniela Tea** 29:04 Yeah, this is this is coming in from the dam, so this so I don't want
to X out of it just because it's in stage. But yeah, if I click on add
asset I would be able to select any other image from the dam instead.

**Don Middlebrook** 29:08 Sure. Right. So if this asset's already there and we haven't changed it and let's
say I move the asset, is it going, we're going to lose that reference?

**Daniela Tea** 29:26 The reference should update, but I am going to take that down as well.
Don, just to confirm and I can report back tomorrow, but it should
update the reference if this gets moved. If it gets deleted then this
would break, but if it were to get moved then yeah it's it moved or
renamed.

**Don Middlebrook** 29:29 OK. Sure. Yeah. Yeah. Right, right. No, definitely, yeah.

**Daniela Tea** 29:45 Then the references should be updated as well.

**Don Middlebrook** 29:47 Should say, OK, I just wanna make sure. I mean, I I knew that was the
case, but I just wanna make sure that that's where it's coming from
exactly so.

**Daniela Tea** 29:53 Yeah, absolutely.

**Don Middlebrook** 29:55 Thank you.

**Daniela Tea** 29:56 Sure. Okay.

Charles Baugh (SHRSS)** 29:56 I had a question. My hand raising isn't working for some reason. I keep
trying to raise my hand and and it won't do it. I had a question about
the sequence. So I'm assuming the sequence is all by I guess by the
date value, right? Is that the way that it's arranged? Like so when you
look at the page you see that there's a sequential order, right? You
have 13 days ago, a month, month, whatever.

**Daniela Tea** 30:00 Oh, no problem, Charles. Go ahead. Sequence. Yes.

Charles Baugh (SHRSS)** 30:16 Is it? How is that sequence determined? And if you wanted to reorder
something, how would you do that?

**Daniela Tea** 30:22 So we have there is a filter that's associated with this component.
Right now I'm viewing this in essentially published mode, but I will
now go back over to the editor and we can configure this component to
see what was set. So I'm just going to open this up. You'll see here on the sort filter we have most recent job title and
location. These values are coming in these. These are not something that
an author touched. These are something that will already be part of the
job search configuration. If additional sorting is available in the
future then that. Is certainly something that could be added by an author by simply
clicking add, but these were the ones that we were informed about so
they are added here by default. So in this case here most recent is what
was the default was selected and so that's why it's being displayed
like that. However as a user if I want to do job title. It's going to sort everything outside of the hot jobs O location. Oh, OK, so it does. Sorry. When I say it sorts everything outside of the
hot jobs, what I mean is the hot jobs will should always stay at the
top. However, these will sort amongst itself. It's separate from from
the portion underneath. I want to make sure that's clear.

Charles Baugh (SHRSS)** 31:42 OK. And then after that I'm assuming it's by property and then the
most recent in that property.

**Daniela Tea** 31:48 After that, so you're saying most recent if we were to do sorry, like
you mean like if we did job title or?

Charles Baugh (SHRSS)** 31:54 Right. Yeah. If you so if you just did job title, is that gonna be like
in alphabetical order by a job title?

**Daniela Tea** 32:01 Yes. So based off of this, like assistant general assistantship, I'm
trying to see if there's OK, here we go. So like bartender, same, but
Hard Rock Cafe Barcelona, Spain has precedence over Edinburgh, United
Kingdom. Yep.

Charles Baugh (SHRSS)** 32:13 OK. OK. All right. No problem. OK. Thank you.

**Daniela Tea** 32:16 Mhm. Yeah, sure. OK. So I think since we're looking at the job search
component, let's do that. And what we'll do, just to be clear, when we
go over the other components, we can also take a look at how they map to
the content fragment. But since we're talking about job search, let's go ahead and look at
the configuration for this. And I'm also going to open up another page
and we're going to create a new page and then just add this on there to
see what it looks like by default. So give me one moment to be able to
add that new page. We're just going to create a page using the open page template. And this is knowledge transfer job search. So just putting something random here just to get this to have a link
page. OK, all right. So now what I'm going to do is I'm going to add a
couple of spacers on here simply because this particular template you
would typically use. Say a hero image or so, but I'm not going to put one in here since I'm
just trying to test some components. So in order to kind of take up that
space, I'm just simply adding some spacers, so I'm just going to add
the job search component. Here and we can see I dropped it on the page and this is how it looks.
And let's see what the configuration was by just dropping it on the
page. Just putting this over to the right here. OK, so. Our job search component is again pulling in all those jobs that are
currently in AEM, so author doesn't need to necessarily do anything
from that through this configuration window. You can see how it appeared
with me just dropping this on there since there's an. Associated query with this component, but what an author can do is we
can see here I'm able to edit these specific text fields, for example
the title. Refine your search. That's what's being displayed here on
the left for the filters. We have different button labels like clear all which is displayed here,
the placeholder text search, our category labels, job categories,
properties, job types and locations. So this is these are the default
values here. We had that sort label that we had taken taken a look at. So sort by I
believe is displayed in mobile so we can see that when we look at the
mobile view. But our sort filters currently have three options by
default with most recent as the default selected. We have our properties label that is select properties and you'll see
here singular and plural. So as I'm starting to select things, if I
select one, I'll say one property selected. If I say if I select
multiple then that's when it would display this version instead. Job types. Locations. So all these labels are associated with the filters here and
the apply filters label. There's apply filters button I believe in
mobile. So again we'll take a look at that and then again more more
labels for when a job is found. Singular and plural. Here we have results per page. Right now you can
see it's 50. Since there's 30 jobs, then there's not going to be a
pagination. However, if I were to say change this to 10 and I hit done,
I'm going to hit preview and I Scroll down, you can see that pagination
will begin. Depending on on how many results I want to show. Now keep in mind that
as of right now the pagination I have put 10 and so it does show 10
results here. It also will show the hot jobs in addition to those 10
results. So the 10 results is saying OK 10 on here and then also to show the hot
jobs. I am going to change this back to 30.

Angelika Akopyan (SHRSS)** 36:31 Do we display the hard jobs on each of the pages or just on the first
one?

**Daniela Tea** 36:31 Save this. I believe, sorry, let me change that back. I believe it only shows it on
the first one, but we're gonna, we're gonna look at that right now. So
I've set it back to 10 and I hit next. So now it's gonna show 10 on
each of these additional pages without the hot jobs at the top.

Angelika Akopyan (SHRSS)** 36:38 OK. Yes.

**Daniela Tea** 36:56 O The first page is going to be 10 plus hot jobs on top. All right, let me now let's take a look at how things will render when
we look at it in. I think iPhone would be the most appropriate here. So
we'll see here that we have our refine your search button. Second, yeah. And so when I have refine your search, you'll notice
things are a little bit a little bit different. However, it's. This is how the user will be able to interact with it. So let's take a
look at the configuration. So Yep, the title again here it's it's a
title, but it's also now serving as the link to display the filters. Um, and then all right, one second. OK. See if I were to select things. Yep. So you'll see here this is this is
what's the this is what's being pulled in from the plural selected or
singular selected. These are all things that were configured by the
author. Jobs found, job categories selected. Et cetera. All right. And then here's our apply filters button. Keep in mind I'm
viewing this in in the emulator. That's why this is so long. Of course
on the phone, if your review is on actual device, apply filters is not
going to be, you know, like on this long scroll bar. But this is where
the apply filters button comes in and one of the things that we. Had seen that an author would, um, be able to configure. So where is it? So here you go, the apply filters label. Hey. All right. Any questions about what we're seeing here with job search?

**Mayte Eme** 38:59 Not the search, but the cards. When I click on an actual card, what's
that we need to track these clicks, right? So I remember in cycle we
used to have. I don't know if we did a custom or we just had something
hard coded, but they had unique IDs, right? Not.

**Daniela Tea** 39:04 Mhm.

**Mayte Eme** 39:17 And friendly so we can track them. So when I click on them, what data I
send to the Tillium data layer?

**Daniela Tea** 39:24 So in terms of the data alert, that is that is something that we can
capture as a question for our tech team. The link that's populating
this as we saw is coming in from. Uh, the content fragments. I really pull that up again.

**Mayte Eme** 39:43 So OK the link I get but the ID of the you know like each course you
have their own like name or ID something.

**Daniela Tea** 39:45 Yeah. Right. You're you're saying like for example this here should be like
say like ID one and then another one be like ID2 etcetera, like in
unique individual for each of these results. That's what you're asking
for, correct?

**Mayte Eme** 40:00 Yes, mhm.

**Daniela Tea** 40:02 One second, let me uncheck this just so we can see more. So in terms of
these all having unique IDs as as something from like the author
standpoint that is not currently set up within the configuration section
as you can see here. But I will check in with the tech team with regards to what's actually
being passed, because I do believe these should still have unique ID's
since they are coming in from unique content fragments, but I will get
more information. More information on that one and we can follow up on that during
tomorrow's Q&A portion before we start with the next portion. Does that
sound good, Maiti? OK, all right. OK. Any. Yeah, go ahead. Sure.

**Mayte Eme** 40:43 OK, Yep.

Angelika Akopyan (SHRSS)** 40:47 Yeah, I can Daniel, we have one quick question related to the actual
job. I understand that the job runs every 30 minutes, but is there any
option to run the job on demand if we need to run for whatever reason in
between?

**Daniela Tea** 41:01 Any option to run the job on demand? So I actually I actually want to
check in and I'm not sure. I'll check in with our dev team, but my
understanding is actually this is running more than 30 minutes. I
don't. I think it was running as much as like every 5 minutes or so I
I.

Angelika Akopyan (SHRSS)** 41:03 Thank you, ma'am. Anything is.

**Daniela Tea** 41:21 I will confirm the numbers on that, but your question is would you be
able to run it on demand? Since I think it was it was such a short time,
I'm not sure if we have that particular functionality because you can
see here like it's been less than 30 minutes and this is already
updated.

Angelika Akopyan (SHRSS)** 41:21 Oh, OK.

**Daniela Tea** 41:41 So I I'm not quite clear the exact duration, but I will check in on
that and then also ask that question about an on demand update for these
jobs.

Angelika Akopyan (SHRSS)** 41:48 I wonder how how long will be the period for the in production also 5
minutes or it will be increased to 30 minutes. I don't know even in
staging or in a low environment they just did it 5 minutes so that we
can test.

**Daniela Tea** 41:51 Uh. Mhm. Right. Because there's because there's way less jobs. Yeah, that's
that's definitely something. I think we would need to check in on it.
Go ahead, Gonzalo, maybe you have some insights on that.

Angelika Akopyan (SHRSS)** 42:04 And. And I wonder how long it takes if we have. Currently we have around 800
jobs in production. How long will it take the whole thing to happen? OK.

**Daniela Tea** 42:24 Gonzalo, did you? Did you have?

Gonzalo Calasich (SHRSS)** 42:27 No, I will wait. I will wait for you guys to answer Angelica first.

**Daniela Tea** 42:28 Oh.

Angelika Akopyan (SHRSS)** 42:31 No, I think I'm done. I just asked my questions. You can go ahead,
Gonzalo.

Gonzalo Calasich (SHRSS)** 42:36 What your question would answer, Angelica?

Angelika Akopyan (SHRSS)** 42:39 No, I think Danielle will check it out.

Gonzalo Calasich (SHRSS)** 42:41 Oh, OK, cool.

**Daniela Tea** 42:41 Yes, that's something I'll need to check in on, Gonzalo.

Gonzalo Calasich (SHRSS)** 42:44 OK, so on the on the search page I noticed when you select something on
the filter it doesn't really append something on the URL. Is is that
something that you guys because the the current one we we have every
time that you select a filter it will append the.

**Daniela Tea** 42:51 Mhm.

Gonzalo Calasich (SHRSS)** 43:04 To the URL. So that that means that if I copy that URL and put it
someplace else, it's going to do the filter automatically. Is that
something that is going to happen? And the reason has been because I I
think you know somewhere on the sites I think they have a hardcoded you
know categories or property. Locations that will need to be in the filter automatically, so I
haven't seen the the filters being added on the URL on the on the URL.

**Daniela Tea** 43:31 Right. Yeah, so.

**Mayte Eme** 43:35 Yes, thank you, Gonzalo. We do need deep links and we need them to be
friendly. Not those weird numbers, letters that we have right now.

**Daniela Tea** 43:44 Yeah. So in terms of what you guys like as we can see like you're
you're pointing out Gonzalo not appending to the URL and yes, there are
definitely instances I believe. Let me see, let me take a look. There are instances on the the website where you guys are leaking. Yeah,
yeah, sorry.

**Mayte Eme** 44:02 So just to give you an example, we have exactly properties will go to
their specific property or we will go by category or we might go by
region, right? If it's like depend depending on the use case.

**Daniela Tea** 44:11 OK, yeah. So yeah, let's take a look like, I guess like if we were going to Hard
Rock Digital, uh, if you all.

**Mayte Eme** 44:22 No, they have their own hiring. We usually don't. Don't LinkedIn,
yeah.

**Daniela Tea** 44:25 Oh, do they? Oh, 'cause I I think, right? I think you're.

Angelika Akopyan (SHRSS)** 44:29 My pictures if you go to my cages.

**Mayte Eme** 44:30 They have they they feed into work day, but they have their own thing
too, so that's not a good use case.

**Daniela Tea** 44:34 I see. OK. Um, what would be a good one then?

**Mayte Eme** 44:39 A property. I mean if you go to a property website, they link to right
now to the career site and you learn on that specific property like
Brighton will link to this research results page filtered by Brighton or
it could be filtered by Brighton and a category or and you know.

**Daniela Tea** 44:53 So I do.

**Mayte Eme** 44:59 I don't know whatever we want to do, we can mix and match any of those
filters.

**Daniela Tea** 45:04 I see something. Yeah so this is because I know that even without even throughout this
site there are instances where the URL is going to have like something
like this with some parameters at the end. In this case here like I I
copy this from whatever link we were just on in this case here this.

45:11 I.

**Daniela Tea** 45:26 Does not exist with the QA data, so that's why it's not able to show
something doesn't exist. I know it says 30 jobs found because the
default behavior is that if it's not going to show anything instead of
saying 0, it's just going to load the jobs as is.

**Mayte Eme** 45:39 Right.

**Daniela Tea** 45:43 So this is definitely something I, you know, I I I want to talk to the
tech team on because we were working with such a small subset of data.
But yeah, definitely want to confirm how the filtering works with
regards to the URL because as it stands right now, I'm just going to go
to the search for.

**Mayte Eme** 45:53 Oh.

**Daniela Tea** 46:02 Jobs page, right? As you're clicking on filters, it's not going to
append that to the URL, but it sounds like that's what you guys need.

**Mayte Eme** 46:07 Well, to be to be honest, we don't want the filters to append to the
URL, we just want a deep link. So because every time you append to the
URL, you literally create a new URL. So our analytics now has 1000 URLs
for the same page.

**Daniela Tea** 46:15 OK. Mhm.

**Mayte Eme** 46:24 Just because of the filter options. So we don't want it to append to
the URL, we just want to have the ability to deep link so we can add to
the URL and land on the page filtered. We don't want users to be, you
know, clicking everywhere and changing the URL.

**Daniela Tea** 46:37 OK, OK. So let me talk to the tech team on that one too, because I know
that was we were we were testing in in terms of authoring certain pages
and we saw that the URL on the live site had those filters appended to
to it. So let me make sure and confirm how that's going to work with the use
case that you described might say for those other property websites. So
we're going to take that one back and we'll get back to you guys
hopefully tomorrow on that one, OK. Now I'm going to, I'm going to just get out of this, this particular
page so that way I can focus on the editor. Yeah, go ahead.

**Mayte Eme** 47:16 One last question about this, just because you never know right with our
technology, if for whatever reason the sync goes wrong and it's not
connecting or whatever, do we have an error message?

**Daniela Tea** 47:29 Do we have an error message if the sync goes wrong? So if the I think if
the sync goes wrong, if there's existing jobs in there, that would
still display because that's already in AEM, right? So like it.

**Mayte Eme** 47:40 OK. So if you display the last sync, it doesn't OK and if for whatever
reason you can't display the data.

**Daniela Tea** 47:45 Yes, that's correct, right.

**Mayte Eme** 47:52 It's just blank.

**Daniela Tea** 47:55 I believe this would just we do have a no jobs found message.

**Mayte Eme** 48:01 OK.

**Daniela Tea** 48:02 So that this display right now you're gonna see this if if I were to
delete all the content drivers right now it would say no jobs found. But
if I were to like try and do some weird selection of filters, it would
say no jobs found. So you're saying if.

**Mayte Eme** 48:08 Mhm.

**Daniela Tea** 48:17 There's an instance where it's not waking.

**Mayte Eme** 48:19 For whatever reason it cannot pick, it cannot read, it cannot display
anything. Instead of just showing blank in like we should have like you
know like that message, no jobs found. I mean something better than
that, but you know like a custom message that we can display.

**Daniela Tea** 48:38 OK, yeah, so I'm trying to think of when there could be an instance
because like I mentioned, these would all still be here. So as long as
there's jobs in AEM, something would display in this section. If you if
there was no jobs in AEM, it would display no jobs found. So this is
custom, but it sounds like what? What you're saying might say is like say another field if there's like
an error, not just if there's no jobs found because of weird filters.

**Mayte Eme** 48:59 Mm.

Gonzalo Calasich (SHRSS)** 49:02 Yes.

**Mayte Eme** 49:04 Like, yeah, and I remember when we were testing Isense, we had that we
we had them break it to see what would happen, right? And we got a blank
page. So we just adapted to have a an error message in case that ever
happens.

Gonzalo Calasich (SHRSS)** 49:14 Yes. Any. That.

**Daniela Tea** 49:21 Sorry, someone saying sorry, someone speaking.

Gonzalo Calasich (SHRSS)** 49:25 Anyways.

**Mayte Eme** 49:25 I think that was background.

**Daniela Tea** 49:26 Oh, OK, got it. All right, so yup, heard what you said in terms of
essentially something separate from no jobs found, more like a specific
error message for when something can't load instead. That certainly
sounds like something that we'd want to cover during the gap analysis,
so.

**Mayte Eme** 49:28 OK.

**Daniela Tea** 49:46 We'll make sure that that's something that we're taking note of. I'm
going to hit cancel.

**Mayte Eme** 49:51 Yeah. To be fair, I don't know when that would happen. I mean, the odds
are low, just, you know, having some business continuity in case
something goes wrong.

**Daniela Tea** 49:58 Yeah, yeah. No, understood. All right. OK. So I think we we talked about
with regards to the job search component, essentially, you know some of
the things that you can see the differences in mobile. And in desktop, the configuration and how the fields are mapping. Are
there any questions with the job search component before we move on to
our next component?

**Lisa Cardia** 50:27 Um, just from me, I know we're going uh component by component today,
but as it relates to like a new page needed for careers, what template
should we be using? And is that on our? Forgive me if it was on the
agenda to go over just building a regular page for.

**Daniela Tea** 50:31 Mhm.

**Lisa Cardia** 50:42 For careers, so we know which template to use.

**Daniela Tea** 50:45 Yeah, so Lisa, for all of these pages you're gonna be using essentially
the open page template and it's just like how I did here. So it's
always gonna have like the the header and the footer established and
then the middle area for the content with whatever components you need
to add to it.

**Lisa Cardia** 50:58 OK. But that was always open page.

**Daniela Tea** 51:05 Yes, that's correct. Yes. Yep.

**Lisa Cardia** 51:06 OK. Thank you.

**Mayte Eme** 51:08 I do have one more question about filters because I know we did that
wrong and we had to fix it during the Sprint when we did items. When you
select the filters, do they update each other? Angelica, I don't know
what word we use if you remember, but if I select like you're doing now
properties, types and locations get.

**Daniela Tea** 51:25 Uh huh.

**Mayte Eme** 51:27 Ulated so you only see.

**Daniela Tea** 51:29 Yeah, so you can see actually how like I had selected multiple here, but
then when I selected a property, it kind of removed those filters. I
don't know, conditional filter. I'm not quite sure what the correct
term is, but you can see how like when I unchecked properties, the
categories came back, right? Is that what you're referring to?

**Mayte Eme** 51:42 Uh. Yep. Yeah, I I see it. Thank you. Exactly. Thank you.

**Daniela Tea** 51:49 My day. Okay. Yep. Sure thing. All right. OK, guys, let me Scroll down now and let's take a look at
our next component. OK, so this is our job listings component and I'm going to pull back
up. Uh, my. Sorry, my my random job posting here the CF again so we can see how this
maps to the content fragment. Let me close out of my test one and I'm
just going to jump back to author. OK, here we go. So this is the job
listings component. So the job listings component actually can display in two ways. In this
instance, I'm showing all the jobs, limiting it to a certain number of
jobs I want to show, but I'm showing everything versus showing just the
hot jobs. But let's take a look first at this job listings all and just really
quickly here. We're going to see again this card is comprised of our image that's
set here or with the image configuration page, which again I will be
showing. We see the title of the job and then also the property. Listed here and then we have the Apply Now button which is pulling in
this particular link. OK, so let's take a look at how this is
configured to be showed the way it is right now. As mentioned, I can select between all jobs and hot jobs. In this
instance I have shown all jobs for the layout style. I chose 3 columns.
You have an option of 123 or four. My route path is pointing to a
specific folder in the dam. In this case I had selected, I went to SHRSS CF jobs US and I selected
Florida. So that way it will pull in all of these particular folders
from Florida and display within this component. If I wanted to say
narrow it down to just Tampa, I could do that and. It would just show the items here, but in this case I chose everything
from Florida. I can also select my maximum job cards. So say I only want to show like
3 jobs in Florida. I'm not sure you know there might be a use case that
you have like you only want to show a certain number. You can do that by
setting this here. So if I were to change this to say 4, I'm going to
hit done. You can see it changed. Yeah, go ahead.

**Mayte Eme** 54:29 Does it only does it only go like Florida as a state or does can you can
select properties because what we our real use case would be South
Florida Cocoa Classic. Oh OK, you can check.

**Daniela Tea** 54:37 Yeah, so if I were to select Orlando instead and I do this, you can see
this is only showing things from Orlando, so.

**Mayte Eme** 54:45 And you can do multiple properties, right? I saw checkboxes.

**Daniela Tea** 54:47 So in this case you you would show um one. Uh, you can do multiple
properties.

**Mayte Eme** 54:54 Because we would do the three, the what is it? They have a name for the
three in Florida, the three big S or whatever they call it. And it's
Coco, Classic and Hollywood. We we do job first for those 3.

**Daniela Tea** 55:06 Classic and hot. So you're saying like like in your instance, you would
probably show these two together. Is that what you're saying, Maiti?

**Mayte Eme** 55:18 Yeah, I see that you can select more than once, I think so.

**Daniela Tea** 55:20 Oh no, no. So you cannot select more than one. Be clear, you can only
select one time. However, in this instance, like if you, this is not
going to be the most elegant solution. However, if I want to show those.

**Mayte Eme** 55:23 Oh. You just remove the headings and put them one after the other.

**Daniela Tea** 55:38 Yes, correct. Yeah.

**Mayte Eme** 55:40 Yeah, but then you can't sort them properly.

**Daniela Tea** 55:45 When you say sort, I guess what kind of sorting are you talking about?

**Mayte Eme** 55:47 Yeah. Well, if you want to sort them by, you know, by category or division or
whatever, you can't, it's property, then the division. OK, so we'll just know this is another gap.

**Daniela Tea** 56:02 Select.

**Lisa Cardia** 56:03 I think I do have a question on this too though. What are the steps that
you chose? So you can also choose the columns, but you said you can
choose like the Max cards. Is there any way? And this this occurs quite
a bit on like very similar components outside of careers.

**Daniela Tea** 56:05 Sure. Mhm. Uh.

**Lisa Cardia** 56:19 If we had less, like we always have three being the typical 11 row, but
if there is less than three, there's no way to like center the two
cards or center that one card so that like so they're not always left
aligned I guess is my question.

**Daniela Tea** 56:26 Mhm. And. I see what you're saying. Um.

**Lisa Cardia** 56:37 So like that fourth card that you just had when you did 4 listings was
like all the way to the left, but the rest were center. So it's.

**Daniela Tea** 56:40 Yeah. So.

**Lisa Cardia** 56:45 Is there a way to keep it that way?

**Daniela Tea** 56:45 Yeah, so let's see. So not currently. So in this case here I I
understand what you're asking. You would want these to be centered, but
let me confirm something though. You would want this to be centered
without changing the width of the cards, is that correct?

**Lisa Cardia** 56:54 Yeah. I'll have I'll defer to the UX team to to comment on the width of the
cards. I would think we'd want them to to not get larger because then
that might distort what they look like, but at least centered.

**Daniela Tea** 57:15 Yeah, so that. So that's currently not there, but I was asking because
that would certainly be something that we would discuss during the gap
portion, but something like understanding if this number were to change,
like for example if this was one, oops.

**Lisa Cardia** 57:30 Yeah, 'cause it's one, it's one in the section below. So that's why
I was like saying it looks a little bit odd when or when you just had
you just had Coconut Creek or something selected at this point and it
was showing just one. Yeah, so so one by itself especially looking.

**Daniela Tea** 57:31 This is 1. Uh huh. Oh, when I had two, two together too. Yeah. Mm-hmm.

**Lisa Cardia** 57:48 You know.

**Daniela Tea** 57:49 Yeah, no, understand what you're saying. And yes, so this sounds like a
gap. However, when we discuss the gap, that would be something, you
know, like we would need to understand if there's less numbers, what
happens to the card? Does it stay the same width? Would it increase? It
would be centered and it would increase, you know, like if I were to put
two here is the. Expectation that this would take up 100% of this width right here or
that this would just simply be centered. So those are the kinds of
things that we would need to to discuss during the gap portion. But
certainly understanding though that is that the desire is that at least
at the bare minimum the alignment is something that is missing from this
component.

**Lisa Cardia** 58:16 Right. Yeah, I guess the reason why I bring it up, especially not just to be
like nitpicky, but because of the hot jobs in the hiring events that we
saw on the home page, those ones centered, the hot jobs actually got
bigger, but it stayed center aligned. You know, they're all working
differently. So it's like although we're we're having a set of.

**Daniela Tea** 58:37 Hey. Yeah.

**Lisa Cardia** 58:46 Grid cards, they all display different, so it just doesn't look very
like neat and consistent. That's my concern.

**Daniela Tea** 58:54 OK. OK. Yeah, these are all definitely, these are definitely the topics
that we want to talk about when we go over the gaps for the job listings
though. So in this case here I had chosen Orlando, I had chosen
previously I had chosen Florida.

**Lisa Cardia** 59:00 Yeah.

**Daniela Tea** 59:11 Simply because I knew I had more cards. Just do this. So yeah, so you
can see here it's going to list out everything within my columns of
three because that's what I selected. The button label apply now
that's just, you know, dictates what's being displayed here, but
again, as mentioned before.

**Lisa Cardia** 59:22 Yeah.

**Daniela Tea** 59:31 The URL, the destination URL for this is coming from the individual
content fragment. So this is going to link to that specific page for
Hostess is going to the general manager, etcetera, etcetera. And here
you can see a job's default image. So if say you did not put any image within the content fragment here,
you're able to set something so that way when it's displayed as cards
here, it will at very bare minimum have this this image that's listed
in the card. So if I were to of course clear this, it done. And you can see it's not going to show anything, so I'm able to to set
whatever default image I want for this particular component. That apostiary, yeah.

**Lisa Cardia** 1:00:18 And that doesn't work. That doesn't work the same for the listings we
saw with the search, because like the ones that appeared with nothing
didn't have.

**Daniela Tea** 1:00:26 Right, so this the search and that's where we're going to take a look
at the configuration page, but there is no default image set up within
the job search at this time. Let me open this. Let's confirm. So we talked about jobs type when
it's all jobs. We talked about the layout style, the root path, and how
you can only select one, but it can be very specific for property. It
could go up to any portion of this hierarchy setting setting the. The maximum number of jobs, our CTA button label, and what populates the
link opening a new tab, as well as our default image here. OK, so this
is for yeah.

**Lisa Cardia** 1:01:12 Sorry Danielle, the the apply now link. So is there a a purpose for it
then? If that always gets added as the content fragment, like why do we
what would we? What would happen if we put different text there? What is
that gonna do?

**Daniela Tea** 1:01:15 Yes. Oh, well. So this is what dictates the button text.

**Lisa Cardia** 1:01:29 OK, so that always has to be filled out and can only be the the same
there, but then the actual URL is what gets generated in the fragment.

**Daniela Tea** 1:01:39 Yes, that is correct.

**Lisa Cardia** 1:01:40 OK.

**Daniela Tea** 1:01:41 Yeah. All right, OK, so that is for all listings. Let's take a look at the
exact same component, but in this case, this is specifically for hot
jobs. OK, so you can see here same. I put Florida and I selected three column
and I selected yeah.

**Lucas Nelson** 1:02:00 Daniela, sorry, this you wanted to leave that different text.

**Daniela Tea** 1:02:05 That's fine. Yeah, this is. Oh, just to be clear guys. So this isn't
stage, but it is. It is a test page, so so don't worry and we will
certainly be removing it. So it would not appear on production. Yeah,
no, no problem.

**Lucas Nelson** 1:02:05 I don't know if the test page for you. OK, thanks. OK. All right. Thanks. Sorry.

**Mayte Eme** 1:02:20 I have to select a location. Sir, can we have the path as the road?
Because hot jobs would be every hot job, not specific to our location.

**Daniela Tea** 1:02:20 So here, yeah. So you're asking for hot, like, say, say you selected multiple hot jobs
for anywhere, right? So you would just move up the location of where you
wanted that to be. Yeah, in this case, I chose. I chose Florida just
because that's where I knew the hot jobs were. But yes, you could set
it higher up in order to choose those hot jobs.

**Mayte Eme** 1:02:39 Good job. OK, so that works. OK. And if there are no hot jobs, like let's say you leave it like this,
right? And we have a bunch, but at one point we don't have anything.
Does it just hide by itself or blank with a message?

**Daniela Tea** 1:03:04 So right now I believe it would be blank, but there is no message at the
time. I think we saw that again because we were using QA data. And just
to confirm, I take you're saying there are instances where you guys
will not have hot jobs or will there always be at least one I guess from
y'all's end?

**Mayte Eme** 1:03:24 We don't have hot jobs as often as you may think, so we don't want
like hot jobs title and then blank. Nothing, you know, it's.

**Daniela Tea** 1:03:28 OK.

Angelika Akopyan (SHRSS)** 1:03:31 Yeah, my TV tested this and if there are no hard jobs, then what will
happen? The section is still there and you'll have the section name,
but the the whole section will be empty.

**Daniela Tea** 1:03:31 OK.

**Mayte Eme** 1:03:45 What do you mean the whole section? Something like the title like
everything and it's just a.

Angelika Akopyan (SHRSS)** 1:03:47 The time you will have you have the the the hot jobs title as a section
title right? But there will not be cards underneath.

**Daniela Tea** 1:03:53 Yeah, so this here. Right. So like pretend this type. So this title is there's.

**Mayte Eme** 1:03:59 So there's no message saying no jobs or nothing.

**Daniela Tea** 1:04:02 There would not. There's currently not, um, a message that displays if
there's no hot jobs.

**Mayte Eme** 1:04:09 Or the component or the module hides. OK, so that's.

Angelika Akopyan (SHRSS)** 1:04:12 No, it doesn't hide. It doesn't hide. It will stay there. It is a
title, but blank, blank.

**Mayte Eme** 1:04:16 OK. OK, it's just another up.

**Lisa Cardia** 1:04:22 Yeah, so if you went to production today, team, you would see that we
you might have scraped the site and a hot job existed, but hot jobs no
longer has any listings currently. So the title of hot job section comes
down automatically when there's no listings.

**Daniela Tea** 1:04:36 Mm. Hmm. OK. OK, alright. OK.

**Mayte Eme** 1:04:45 Do we have a back for that, Angelica?

Angelika Akopyan (SHRSS)** 1:04:46 We have a. Yes, I have a for this. Mm-hmm.

**Daniela Tea** 1:04:47 Yeah.

**Mayte Eme** 1:04:48 OK, good.

**Daniela Tea** 1:04:49 Yes, there is a jury ticket for that. Yep. OK, alright, so that is the
job listings component. We covered how that would be set up for hot jobs
or if we needed to show all jobs. Let's take a look now at our.

**Lisa Cardia** 1:05:04 And I think, I think Danielle will, unless you want me to add it to the
confluence page. The take away there though is the fact that for the hot
jobs we usually put an image of the property, but we wouldn't want to
override the logo image in the listings. So although we're going to
pull in the hot jobs here, Tampa should show the Tampa property.

**Daniela Tea** 1:05:05 Yep. Mhm.

**Lisa Cardia** 1:05:23 Coco should show the Coconut Creek exterior image, but then if we were
to look at the same job as the hot job listing at the top, it would
still show the logo.

**Daniela Tea** 1:05:24 Mhm. Uh huh. I see. OK. So yeah, that I think so we are, since we are recording this
and that's what we're going to be reviewing essentially things that we
acknowledged as a gap, I think Lisa. So I think we have it covered since
I'll be checking out the transcription, but let me make sure I I
confirm this. You are saying that there are instances where if something is a hot job,
you might have a different logo than when it's within the actual job
listing itself. Is that correct?

**Lisa Cardia** 1:06:01 Yeah, it won't be a logo, but rather we like to use like an image of
the property. But then when it's in this like search component, that's
when we're pulling in a logo.

**Daniela Tea** 1:06:06 OK. The logo. OK, OK, got it. OK, understood. All right, let's see. OK, so
now we're going to take a look at job filters after that job category,
category cards, and then the job image page. So let's take a look at job filters. All right, and actually I'm going to pull U. Sorry, I meant to do this
for the other component. I know that this is my this is my test. My new test page I had created
with the job search component. I'm going to delete that and I'm just
going to put in. I realize I didn't show this. I'm gonna go play in job listing so you
guys can see what it looks like by default. So I just put it in, put in
a new component. So by default it's showing hot jobs for column. It has
this root path, so these are the default values and then of course as
you can. Figure it. You can change it to however you need. If you want it to show
all jobs instead, that's where you would do it here. Change that route
path to show exactly where you want versus the overall jobs, etcetera,
etcetera. So just want to make sure that the team was aware of what
values are here by default. And also how things can look after you configure it.

**Lisa Cardia** 1:07:36 So that one was set to 8 and four or what was this set to the one that
we're just looking at?

**Daniela Tea** 1:07:37 OK. Yeah, sorry, this one was set to by default it's four column hot jobs,
4 column pointing to the root path of jobs, meaning every every location
and then a maximum of eight.

**Lisa Cardia** 1:07:55 Yeah, if you just had done, I'm just curious, like I would like to know
as an author what? So like if it's four, they have like a bit of a
skinnier view. If it's three, they have more of the like wider view. If
it's two, are they going to get very wide? Like is is the number of
columns, what's shading the size of the card? Because it's not like would go in.

**Daniela Tea** 1:08:18 OK, so I'm going to change this one to two because I'm showing more
things here. So you can take a look. You can see that the cards does get
wider to fill in the width of this component.

**Lisa Cardia** 1:08:23 Thank you. OK.

**Daniela Tea** 1:08:31 Yeah, so we saw how it looked like at 2:00 and then this is how it looks
like at three. Sorry, it shifted, but this is how it looks like at 3:00.

**Lisa Cardia** 1:08:41 Got it. So it's the columns that's dictating the size of the cards.
Number of cards are always going to left align no matter how many.

**Daniela Tea** 1:08:41 Yep. Yes. That is correct, yes. All right. OK, so now let's go on to our job filters component so we
can see how I configured this and we'll see how it looks like upon
initial configuration. All right, so just join to the left. This is the filters that you see on
the homepage of the careers website. Here as an author, I'm configuring
what I want the search jobs button to to go to. In this case, you can
see I've sent it to our jobs page. I have the labels that are displayed here, job categories, select
properties, select job types, select locations, as well as the singular
and plural labels like we had seen earlier. So that's that's for all
four of these drop downs. We're just going to Scroll down. A little bit more. We have our button text of search jobs and then of
course when you view this particular component in mobile, there is a
title that gets displayed on top of this that the author would be able
to configure here. Let's take a look at how that is. Find it. Here you go. So find your career is the title that I figure
within the component, only displayable in mobile. OK, so this is the job filter. So let's take a look at how it is when
you just drag it on the page and remove my job listings component. Job filters. So by default it looks pretty much the same, but the search
page is something that you would need to configure. You can see right
now it's pointing to just like a random location with an SHRSS because
your search page could be anywhere. So this is certainly something that
an author would need. To make sure it's configured properly. In terms of the labels, you will
likely keep the majority of this information the same, but perhaps the
button text instead of search jobs, you might need to put something
else, but just wanted to make sure that the authors. Confirm that the job search page is indeed pointing to the correct
search page that you need it whenever you use this component. Great. OK.

**Mayte Eme** 1:11:18 Why do we have to configure the search page? We only have one search
page.

**Daniela Tea** 1:11:23 So when this the way that this is working right now is the on on the
current website right now in stage it is pointing to the right search
page. So an author at this moment would not have to change anything if
you were to ever have to use this component say I don't. I'm not quite clear why you would use it on say like a cafe site or
something, but if you need to use it somewhere else, that search page is
going. The job search page is not going to necessarily be in the same
location for every site I would imagine. So what we're just saying here
is that. You don't have to change anything right now as it is because it's been
migrated, but if say you have another search page you need to point to
instead when you're using this component, you have the ability to
change that as an author.

**Mayte Eme** 1:12:03 Mhm. But even if we put this widget somewhere else, we would go to the same
search page. Can that be defaulted?

**Daniela Tea** 1:12:22 It certainly can, but keep in mind whenever you default values, I guess
the question is like having the flexibility for an author to be able to
change things. If we're talking about like a default value, sure,
that's fine. However, if you were to change the structure, you know, I
guess, or if there's another search page, you want to just.

**Mayte Eme** 1:12:26 Uh.

**Daniela Tea** 1:12:41 Make sure that the author has that flexibility to be able to update it.

**Mayte Eme** 1:12:45 Yeah, I I mean, I do like the flexibility and that that that's good.
I'm just saying if we're gonna use it somewhere else, we pretty much. 99.9999% of the time we'll go to the same search page, so defaulting
the value is just one step less. That is a content author that I will
have to do, you know, the easiest for them, the faster and the better
for all of us.

**Daniela Tea** 1:13:08 So I I think, yeah, so it sounds like then for right now things should
be fine. There's the default value as we saw is something that is a
little bit different since you know if you is is a little different if
you ever use it. Just as it is. However, if we were to take a look again at what is
currently going to be, I think it's on, it should be on home. Yeah, so
this should be set up as is. And I guess my say if if like there's no
reason to use this component anywhere else for the time being, this
should be fine the way it is then. This is what's currently on your stage website configured properly.

**Mayte Eme** 1:13:48 OK, we'll just log it and I guess identify, you know, another gap and
we'll fix it later.

**Daniela Tea** 1:13:54 Great. OK, now I wanted to move on. Oh, sorry. Actually, before we move
on, quick look at the UI portion of the. So I'm just trying to find my
published view of the page. OK, yeah, so this is. My test page, but on the state website. So just just to be clear here
again, we can see how this operates. This is pulling in that information
from those content fragments. So like the location we saw, that's the city essentially from the
content fragment, the category, the values there are being rolled up
into these drop downs here. I. Alright. OK, so now let's move on to job category cards and this here is what is
also on the homepage, I believe on the current live site. Let's take a
look at what I have configured. All right, singular results label, one job, plural results label, 9
jobs. Number of cards to display. I put six sort results. It could
either be by the number of jobs, highest to lowest or alphabetical
order. In this case I chose alphabetical order. And to your point, Mayte, the job search page, this is again, I know you
you're saying there will only be one. In this case here, it's being
pointed to that one job search page within the corporate careers
website. And so that's what we have here. Let's take a look at how
this component is when you configure it from scratch. So I'm going to jump on over to my other test page. Just remove this. I'm going to add job category cards. Alright, so by default you'll see
it's pulling in the information on. These are the this information's
coming in from our content fragments, right? These are our categories,
so it's pulling all that in. You'll notice here it says undefined, undefined, undefined, and that's
because I don't have how many cars I want to display and I also do not
have the search page added. So if I were to just put a number in this
case. I think. Just going to put 9 and then the job search page is under corporate
careers, English and then jobs. I hit select once I hit done. You can see here how now it displays the correct label and it's also
sorted. I believe I've had it sorted by default by number of jobs,
highest to lowest. So this is what it is when you drag the components
for the first time to a page. So again, if you want to change that to
output order. That would just be something the author configures.

**Mayte Eme** 1:17:02 How do you change the categories? Because we don't. Um. I wanna say and Angelica, please correct me if I'm wrong, but we can
change the categories that we want I think.

**Daniela Tea** 1:17:18 So I guess my take, can you sorry, can you elaborate on?

**Mayte Eme** 1:17:21 Does it have the ability? Like what if I don't want to put food and
beverage right? I want to promote some other category. How do I change
that?

**Daniela Tea** 1:17:29 What if you don't want to promote food and beverage you want? So
you're just say you want to like pick and choose which categories
versus everything that's within that's currently stored in in EEM.
That's what you're asking. Is that correct? OK.

**Mayte Eme** 1:17:36 Yeah. Mhm.

**Daniela Tea** 1:17:46 So I guess if you wanted to simply pick and choose right now with this
component as is, you do not have that ability if say you wanted to show
like the top three that had the most jobs. You could do that with the current implementation. Right now I'm only
showing these are the ones that have the most jobs available. But if you
say wanted to show, I'm going to go back to 9 so I can see more if you
want to show like casino sales and housekeeping. And just those two currently with the implementation of the component,
you would not be able to do that. I guess, um, is that something currently that you all are doing today
with the live site?

**Mayte Eme** 1:18:32 I wanna say we have the ability because we started having gaming jobs
and then we added more and we tweaked them. But honestly, this component
I would have not developed because we're gonna kill it so we can.

**Daniela Tea** 1:18:40 Mm. OK.

**Mayte Eme** 1:18:48 Um. We can just move on.

**Daniela Tea** 1:18:52 OK, sure. All right. OK. Any other questions, um, for anyone else on the
job category cards? OK, so now let's take a look at the promised configuration page. So
what I'm going to do now is I'm just going to go back to just the
admin view of AEM and I'm going to click on Adobe Experience Manager. And I'm going to click on the hammer here and then I'm going to click
on ACS AEM Commons and I am going to click on content packagers. So what
this is going to do is this is going to take me to this configuration
section where we are able to. To put images for specific properties, I'm going to select the image
config. I'm going to hit edit. Alright, so you see here we have this component called Job Images and it
looks like it's just a title. However, when we click on the
configuration icon, you'll see here what's actually being stored in
this component is the job property as well as. The image that we wanted for the specific property. You can see that
this dropdown, yeah.

**Mayte Eme** 1:20:17 What is? What is the job property? Is that the? Because it doesn't
read. Is it like specific name that we?

**Daniela Tea** 1:20:26 This is what's. So let me navigate back to a content fragment so we can
see where that's coming in one second.

**Mayte Eme** 1:20:28 Yeah. Thank you.

**Daniela Tea** 1:20:35 Yep, alright.

**Mayte Eme** 1:20:36 Is it like the work they name or something?

**Daniela Tea** 1:20:39 Yeah, So what I believe what our our tech team did is took the job like
this is that field, that value that's stored here in job property,
right. So the way this configuration works is it's going to check like
for example Hard Rock Cafe Orlando.

**Mayte Eme** 1:20:48 Mhm.

**Daniela Tea** 1:20:55 Any jobs, new jobs that get added with Hard Rock Cafe Orlando will then
have this particular image stored as the image for that particular job. So this here this value, if it matches what's stored here in the job
property, then the image that's that you can see referenced here will
will be stored here in this image section.

**Mayte Eme** 1:21:28 And let me assume all of the locations have been created and already.

**Daniela Tea** 1:21:28 OK, so. Yeah, so yeah, you can, excuse me, you can see this is a pretty long
list and you um.

**Mayte Eme** 1:21:37 It doesn't seem long. That's what is scaring me because we have way
more locations than that, no.

**Daniela Tea** 1:21:40 Oh, it's it doesn't seem as long as you think. Yes, so this is
something that.

**Lisa Cardia** 1:21:44 I think the concern too is that like Seminole Casino Coconut Creek is in
this list with a logo referenced, but that was one of the ones that
showed up without a logo.

**Daniela Tea** 1:21:53 Yeah, so let me explain that. So with regards to this configuration
page, anything that has been like any job that has been added before the
configuration page was set up does not automatically inherit. This. The reason why is because when we were first working on these
components, to be clear, we were told that there are instances where
jobs do not have images. There are also instances where again, the
author would want to overwrite the image. So because of that, this does not automatically get added to make sure
that it's not overwriting whatever an author actually wants. However,
if you were to, once we move over to production, all those jobs that
will be in production once we have the production connection. It will check the property match here, the value here with this and any
of those jobs should then display whatever image is being referenced
here. So I understand right now in stage because keep in mind when we
were working on some of like the configuration page for example, some
jobs are already coming in because. I think was made before we handed off the site, and so that's why
you're probably seeing some jobs that do not have any images. However,
when we move to production, those images, as long as the job properties
match, those images should appear within those content fragments and
displayed and say like the job search results component. Night.

**Mayte Eme** 1:23:33 So who's doing all that mapping and who's getting every name for every
location out there when we go by?

**Daniela Tea** 1:23:39 So this yeah. So this is at least the initial setup of this. This is
something that that I know our technical team handled. I'm not clear I
guess from the SHRSS side who would be handling adding additional
properties for example like if if something else gets added or if a. Logo needs to change.

**Mayte Eme** 1:23:57 I mean new locations I understand but existing right where we we already
have that in cycles so who we need that and what I'm concerned is if
were they. Where to change their internal name? Because I don't know why they have
HRC Washington DC. It should be Hard Rock Cafe Washington DC. Is that
going to break this because the name is not going to map anymore on the
next sync?

**Daniela Tea** 1:24:22 So then what would happen if the property doesn't match this? Like so
you're saying if in Work Day for example, if they were to change this
to Hard Rock Cafe, Washington DC, what would need to happen is a new
entry would need to be added with that specific property value and with
the desired logo.

**Mayte Eme** 1:24:32 Mhm. A new entry or just updating this one?

**Daniela Tea** 1:24:44 So I guess, I guess if the jobs that are existing or saying that those
jobs should also, I guess there would be no references of this anymore.
Is that what you're?

**Mayte Eme** 1:24:53 Oh, you're saying if all jobs have their own name, OK. Yeah, this mapping is concerning. It seems very, very manual. And it's not even a third or a fourth or a fifth of all the locations
that we have.

**Daniela Tea** 1:25:12 I think then what? Because I I'm not quite clear exactly where we got
the list of locations. Perhaps it was when we it might be when we had
worked on the integration. I can check on this with the tech team, but
they we did do the initial setup. Perhaps if there's a separate list or something, we can take a look at
that, but I think we were working with information that was provided to
us when we were discussing the integration. So this is the process for
adding additional properties. To your point, Mayte, if we are missing
some, I think we would just need to. Understand where that you know like where this list um like where there
is a full list.

**Mayte Eme** 1:25:56 Yeah, we have over 500 locations.

**Lucas Nelson** 1:25:57 Daniella, we can provide our, we can provide our point of view as an
answer tomorrow after we follow up with Vinay on what where we were
getting the initial mapping from, OK.

**Daniela Tea** 1:26:06 Yeah, Yep, definitely. I'll check in with with our team tomorrow.
Again, understanding I can report back during our next session. Yep.

**Lucas Nelson** 1:26:14 Yeah, I just want to time check. There's 30 minutes left. I know we
wanted to leave time for a retro for the call. Is there any? How are we
tracking, Danielle?

**Mayte Eme** 1:26:15 Hey, I'm. And.

**Daniela Tea** 1:26:24 Yeah, let me.

**Mayte Eme** 1:26:24 Wait, hold on, let me just ask Scott, if you can take a task please with
IT that work with with the vendor on this to make sure that we have
every location in that mapping because we have over 500 and I don't
think I even saw 100.

**Scott Sorel** 1:26:42 Well, I think it's just coming through the interface, my data. It's
nothing anybody's going to hard code there.

**Mayte Eme** 1:26:43 Yes. Well, it has to be added in Adobe, right? Like copy paste the name so if
we can get the list of locations from workbase, somebody from IT can go
and start mapping those ahead of time.

**Scott Sorel** 1:26:59 They have to actually be done. They don't. They don't come in as part
of the interface.

**Lisa Cardia** 1:27:04 No, that's what Daniela just showed us.

**Mayte Eme** 1:27:05 No, that's what they just showed us. It's not automatic. You have to.
There's another panel where you have to paste the name that has to
match work day and then add the image and then you got to go 1 by 1 by
1.

**Scott Sorel** 1:27:15 Oh yeah, yeah.

**Lisa Cardia** 1:27:17 It's like Workday recognizes the mapping, but the mapping has to be
manually added. That's the missing part.

**Mayte Eme** 1:27:17 I know. Mhm.

**Scott Sorel** 1:27:26 Who added the ones that are in there now?

**Daniela Tea** 1:27:31 Adobe the Adobe technical team did.

**Scott Sorel** 1:27:34 OK. OK. So we can ask so, so I wouldn't be out of bounds Luke asking
Vinay to do something like that.

**Daniela Tea** 1:27:42 I I think what we need though, Scott, is we need to understand what that
full list is. We were operating off of information that was given, but
according, you know, the team is saying it's not full. So we just need
to understand where is that full list.

**Lucas Nelson** 1:27:48 Yeah.

**Scott Sorel** 1:27:48 Yeah. Yeah, we need to figure out where it comes from, right? Who's the
source of the full? Like, you know who is the source of the full list?

**Daniela Tea** 1:27:57 That's correct.

**Lucas Nelson** 1:27:57 Exactly. We're gonna confirm.

**Scott Sorel** 1:28:04 Who can give us that full list?

**Lisa Cardia** 1:28:07 That's what we're asking if you can connect with IT on.

**Scott Sorel** 1:28:10 It's like a circle. We just say IT is like it's like it's it's like
a nebulous cloud. At least I I can start asking around. I I will start
poking around. Maybe. Uh, OK.

**Lucas Nelson** 1:28:22 Yeah, Scott, we're only confirming with Vinay what what what we got
initially, but if it's not a full list, we don't have visibility to
that.

**Scott Sorel** 1:28:23 Some.

**Daniela Tea** 1:28:26 Mm.

**Scott Sorel** 1:28:28 Yeah, I'll ask Michael. Maybe he knows. It's OK. I'll put it on my To Do List. It's fine. We'll figure it
out. I'm somebody asked to have it. This must exist, right?

**Daniela Tea** 1:28:34 Right.

**Lisa Cardia** 1:28:41 Probably whoever handed it off the first time.

**Daniela Tea** 1:28:44 Yeah, we'll, we'll when we discuss with Vinay, you know, we'll try to
track down where it came from and then we can confirm, you know, if
there's a bigger, if there's more information that we can gather from
that particular individual, but.

**Scott Sorel** 1:28:44 Yeah.

**Daniela Tea** 1:28:59 OK.

**Scott Sorel** 1:28:59 Yeah, I don't know who. I'll, I'll, I'll take it upon myself.

**Daniela Tea** 1:29:05 Right. OK. All right. OK. So just confirming what we had scheduled for
today's session. So I think we did cover search categories, filters.
Yep. So we covered all the topics that were listed here. I had put time
for. Perspective and also of course Q&A. And again the reminder for any
burning questions you may come up with later on tonight, tomorrow before
the next session, you know we we ask that you please put them within
this confluence page. That way we can keep track and also respond. With in the comments as well. So I guess I'll pause here though and see
Luke, how you want to handle this, this next step with the retrospective
portion.

**Mayte Eme** 1:29:53 And before we get into retro because I just wanna make sure you didn't
miss anything. We didn't see the career events or the job first.

**Daniela Tea** 1:30:00 Oh, so yeah, sorry, the what was the second part?

**Mayte Eme** 1:30:04 They're the same thing. I mean different names, but the same thing.

**Lisa Cardia** 1:30:05 Yeah, the hot, the hiring events. And then we didn't see those pages
that are supposed to have the same cards on them. So there's a hot jobs
page and there's a hiring events page, and then both those cards exist
on the home page.

**Daniela Tea** 1:30:05 Oh. Yeah. So with regards to hiring events, that was my plan was to have
that actually within the events session because it's not a specific
component related to jobs, right? So like these here that we were
covering today were job specific components.

**Mayte Eme** 1:30:48 OK.

**Daniela Tea** 1:30:48 With regards to the events content fragment. So that is something we are
planning on covering, but that was not for today's session.

**Mayte Eme** 1:30:48 OK.

**Lisa Cardia** 1:30:54 And then those pages though. So obviously like the the hot jobs are
getting pulled in from the hot jobs tag into that section on the home
page, but they aren't. Are they also getting funneled into the the hot
jobs page as well? So if you browse all hot jobs, do we have to add them manually to every
location or is that pulling from the same feed?

**Daniela Tea** 1:31:15 Um, yeah. So this here, let's take a look at that. I'm going to just navigate to this specific page. We'll iter this
looks like it's about jobs. Let's take a look at the configuration of
the components on here. So this is just using that job listings component, right? And it's, you
know, selecting my hot jobs. So you anything that's marked as a hot job
should appear here on the hot jobs page. And then also if we were to go
back to the home page. Because you there's that section there.

**Mayte Eme** 1:31:55 And before you move from the hot jobs page, where's the filtering for
the hot jobs and the searching and all those things?

**Daniela Tea** 1:32:01 So the filtering is something that we had identified. I believe there
was an open ticket for that. The filtering is not something that's
currently part of the component, so it so we had identified that as a
gap, but that is something that was being tracked in JIRA.

**Mayte Eme** 1:32:07 Oh.

**Daniela Tea** 1:32:17 So yeah, you can see you can see here with hot jobs, this is using the
same component job listings with that configuration of hot jobs. So
Lisa, I believe your question was if you would have to do it twice and
the answer is no, you wouldn't have to make any updates. It's just
adding that hot job toggle to jobs within the content fragment itself.

**Scott Sorel** 1:32:20 OK. And.

**Daniela Tea** 1:32:37 Elf.

**Lisa Cardia** 1:32:38 OK, but might be a different story for the hiring events below. I know
you said we're going to do events tomorrow, but is this also getting
fed?

**Daniela Tea** 1:32:42 Green. So this here, yeah, let's let's cover this tomorrow because this is
using a a a different content fragment. It's not using jobs. So this
one we can talk more about how this is going to work and how we can
potentially try to reuse, you know, like say using experience
fragments. Or something like that to make it so you only have to update it once.

**Lisa Cardia** 1:33:12 Yeah, you can just see though like in comparison when these are both
pretty similar cards on the production site, a hot job versus a hiring
event, how now looking at the hiring event, they're they're different
widths and heights than what is standardized with the hot jobs like. Carousel or grid, if you will. And then even like the lengths here when
there's like 3. See how they're not like an equal. It's just little
things because we're using the same type of concept of a card in one
section and a card in another, but they look so, so different.

**Scott Sorel** 1:33:38 8.

**Daniela Tea** 1:33:43 No. Mm-hmm.

**Mayte Eme** 1:33:50 And to check also for tomorrow, are we going to go over the queries and
when we're bringing in different, you know, like properly like
throughout the pages, we have different cycle queries right to bring
different content that we're going to go through that.

**Scott Sorel** 1:33:57 Sure. Sure. Uh.

**Daniela Tea** 1:34:06 Um.

**Lucas Nelson** 1:34:06 Daniela, do you wanna pull up the agenda for tomorrow so we have a clear
expectation set?

**Daniela Tea** 1:34:10 Yeah. Yeah, sure. OK, so tomorrow's supposed to be all about events. So
again, reviewing the event content fragments, the the template page
that's used for displaying events. The event detail component and the event calendar components. Um, I
guess, Mighty, can you repeat what you were hoping to see?

**Mayte Eme** 1:34:34 So when we go, we have. Other pages in the career side right where we pull queries of content
that already exists in other websites so we don't have to reuse them.
So we need to go through those too.

**Daniela Tea** 1:34:49 I guess I need to understand like example like you're saying I I guess.
Can you provide like very clear examples for us to be able to take a
look at first?

**Mayte Eme** 1:34:51 OK. Yeah, like we have content in Cycord for that already exists somewhere
else. So why do it again, right? We'll manage the same thing twice so
we can just write a query. I don't know how you call them in Adobe,
right? But we we call them scopes in Cycord and you say get me the cards
from this folder and it displays on the page.

**Scott Sorel** 1:35:12 OK.

Angelika Akopyan (SHRSS)** 1:35:17 Danielle, you can go to our brands. I can show you what we're talking
about. Go to cafes or casinos. Scroll down. Yeah, even more. Yeah,
where? Which page you want?

**Mayte Eme** 1:35:17 Yes.

**Daniela Tea** 1:35:20 Sure. OK. Oh.

**Scott Sorel** 1:35:28 Sign.

**Daniela Tea** 1:35:29 This is on our brands. Is that what you you asked for?

Angelika Akopyan (SHRSS)** 1:35:32 You go to a casino under our brands menu. You go to casinos or cafe
cafes.

**Daniela Tea** 1:35:40 Um. Uh.

**Lisa Cardia** 1:35:42 I think that's the getting the those are the children pages, Angelica,
of getting the name.

Angelika Akopyan (SHRSS)** 1:35:46 Yeah, yeah, I'll get here. Sorry, get in the game. Yeah. But if you go
to the casinos, right, Scroll down. So for example, there are three,
three cards we display and they display the same cards if you go to,
let's say now to the you know where you go to cafes, cafes or hotels.

**Daniela Tea** 1:35:47 Oh, OK. Sure, sure, sure. Yes.

Angelika Akopyan (SHRSS)** 1:36:03 We display the same key cards looks like.

**Daniela Tea** 1:36:04 OK. Yeah, so, so this is actually, yeah, so this is, this is something that
I believe we were going to explore the use of experience fragments for
because I I understand what what you're saying and I was reviewing some
of the tickets. I believe there are about 18 or so where you guys
identified pages that have. Have some shared content. In this case, for this section here, it looks
like these cards are essentially all shared amongst all these pages. And
then for the art brands, I believe there's a section of cards here that
should be shared across all the pages. Is that that's what you're
referring to, Angelika and Mayte, is that correct?

**Mayte Eme** 1:36:43 Yeah, the yeah, the component. I mean all the functional different
career side, those the video cards. I think there's a form somewhere, but no, we killed that, so never
mind.

Angelika Akopyan (SHRSS)** 1:36:54 Reason that we can reuse, right? Instead of creating on each page
separately, we would like to reuse.

**Mayte Eme** 1:37:01 Like the navigation, right? Um.

**Daniela Tea** 1:37:01 Right, So what I had and actually what I had done, I should have
scrolled down. Yeah, so like I because I remembered seeing that ticket
and what I was going to show you guys just to make sure and and see if
this covered the needs is that instead of using a card carousel on the
page, what I did was I set up. An experience fragment and then put up that card carousel and then just
point it to it instead. So that way I could update the cards and then
any pages that's referencing the experience fragment would also have
the update. So like if I were to change Seminole Gaming to like Seminole
Gaming 2026. In in the experience fragment, anything that has this experience
fragment would also have Seminole Game 2026 and I that's what I wanted
to understand is that that's what you guys are are looking for. Is that
correct?

**Lisa Cardia** 1:37:53 That would definitely solve our issue of needing to use like if we
updated one card that existed on 10 pages that it gets updated in one
spot. But there is something separate that we do have to log that
Angelica might have logged, which is that these cards that are related
to when you were on the get in the game, for example that showed all.

**Daniela Tea** 1:38:02 Yes.

**Scott Sorel** 1:38:06 Yeah.

**Daniela Tea** 1:38:06 OK.

**Lisa Cardia** 1:38:13 All of our lines of businesses, the way that they should actually act is
with a little bit of logic so that when you're on the casino's page,
you wouldn't actually see the casino's cards now in that listing. So
it shows all children of the get in the game, excluding the page you're
on, if that makes sense. So it's taking what you just said, but.

**Daniela Tea** 1:38:15 Uh huh. OK.

**Lisa Cardia** 1:38:33 Also a step further of something we would would like to know, but it's
definitely useful at least to get a shared source, you know, just in
case we change the amount of casinos listed or something and then that
only gets updated once of course. But I do want to mention that there is
like additional logic with these queries.

**Daniela Tea** 1:38:34 I see. Yeah. I see. OK. Yeah.

**Lisa Cardia** 1:38:53 that Maite brought up.

**Daniela Tea** 1:38:54 OK, understood. So I think it sounds like then the experience fragment
approach takes you guys like halfway there in the sense that reusable
right now the way that this was set up on with an AEM is I think because
during the migration it probably.

**Scott Sorel** 1:39:00 Oh.

**Lisa Cardia** 1:39:04 Yeah.

**Daniela Tea** 1:39:14 You know, it probably had like some. It saw that the logic was that the
cards weren't exactly the same. So that's why these cards are all
locally configured. So I think in terms of how you guys can do this, you
guys can use the experience fragment. It would not have the additional
logic for go live or you can.

**Scott Sorel** 1:39:18 Yeah.

**Daniela Tea** 1:39:34 Keep it as is where you're able to control it locally on each page. So
that way it essentially is not showing like you're saying the casinos
page would not be in here because this would just be a local instance of
that carousel. So I think that's something you know. I understand definitely the appeal of the experience fragment. We want
to update it once, so that way any page that's having it will then also
be updated it. If that's the route you do want to take, knowing that in
this case here it would show like the casino's card because you'll be
referencing the same experience fragment on all of these pages, then
this would need to be just replaced.

**Scott Sorel** 1:39:54 OK.

**Daniela Tea** 1:40:10 With an experience environment component. So there would be some
authoring involved with that, but I think that would just have to be a
decision that Hard Rock would have to make.

**Lucas Nelson** 1:40:15 So.

**Mayte Eme** 1:40:20 OK, Scott, then we need to follow up because this should have been set
up properly, right? So we need a fix before we go live and we we're
done.

**Scott Sorel** 1:40:27 Well, obviously.

**Mayte Eme** 1:40:31 OK. I mean it should. I mean I thought it was when Mohsin told us it was as
is. We assume at least this site would get a structured better knowing
that most of our content is shared across everywhere. So let's put a
task for that one please. I have Moses figured that out.

**Scott Sorel** 1:40:52 Sure.

**Mayte Eme** 1:40:57 Oh. Oh.

**Daniela Tea** 1:40:57 Sorry, Charles, I didn't see that. I'm sorry.

Charles Baugh (SHRSS)** 1:40:57 Yeah, yeah, it's it's OK. That was a very lively conversation. I
needed that to go first.

**Scott Sorel** 1:41:01 Yeah, that's fine, Charles. I just. I felt bad. I'll ignore you, man.
Sorry.

Charles Baugh (SHRSS)** 1:41:06 Yeah, my question was a logic question and I might have missed the
answer to it in the very beginning when we talked about when we imported
items from the API that the publishing happened immediately, right. So
pretty much whenever that happened is live time. So say that we had 13
items, 13 jobs that got imported immediately. We realized after the fact
like oh shoot, we need the.

**Daniela Tea** 1:41:16 Yes. Yes.

Charles Baugh (SHRSS)** 1:41:27 Take three of these down and reschedule them for later. Do would would
it? What would be the best way to go about doing that? Would it be to
resubmit through Workday and have them pull in 10 and purge? Or is it to
purge those three? Is it a way to just go to those three individual and
reschedule them manually? What would be the easiest way to take care of that?

**Daniela Tea** 1:41:48 Yeah. So this is one of our takeaways that we're going to discuss with
our tech team. So as of right now, like you mentioned Charles, these are
going to be coming in from Workday. So the Workday is the source of
truth. It's pushing everything to A EM. So all these are coming from
there if, if. You were to make a change in here right now and try to publish it. Work
day changes would eventually override it because it's continuously
syncing. So what we did want to check though with our our team is like
for example, my team had called out earlier in the call of some
instances where you might need to take down a job just like you're
describing.

Charles Baugh (SHRSS)** 1:42:13 Uh, OK.

**Daniela Tea** 1:42:25 So we are going to check in and see if there's any way that you can do
it through the AEM side, anything you know for an author to be able to
handle those particular use cases, but we will not have that answer
until the earliest tomorrow. So definitely making sure though that we
will discuss that with our team. OK.

Charles Baugh (SHRSS)** 1:42:46 OK. Thanks. Yeah, I must have missed that. Sorry. Thank you.

**Daniela Tea** 1:42:48 Oh, no problem. No problem. Yeah. And I sorry, I think I saw somebody
else's hand was off, but I missed it. OK, thank you.

**Lucas Nelson** 1:42:51 Joseph has their hand up.

Joseph Brondolo (SHRSS)** 1:42:56 Yeah, can we go back to the the the job search real quick?

**Daniela Tea** 1:43:01 Yes, um. OK. Yeah, sure.

Joseph Brondolo (SHRSS)** 1:43:08 Um, no, the I mean the filter from the Uh from the homepage careers
homepage.

**Daniela Tea** 1:43:11 Oh. Look the filter from the homepage. You're talking about this section
here.

Joseph Brondolo (SHRSS)** 1:43:18 Yes, yes. Can we go into configuration real quick? And where is the job
category label located where it says job category label job category?

**Daniela Tea** 1:43:20 OK. Yes. Uh, yeah, this one. Um, let's see.

Joseph Brondolo (SHRSS)** 1:43:38 And there there's one for each one. There's, you know, the properties
label.

**Daniela Tea** 1:43:46 Let me see. Sorry, man, I lost it one second. So we're asking about
where is this specific field and you said the job prompt like where are
these specific fields?

Joseph Brondolo (SHRSS)** 1:44:00 Yes, exactly. There's four of them because there's four categories
there.

**Daniela Tea** 1:44:02 Let's see. I might need to check on how this is on how this is mapped to the UI.

**Scott Sorel** 1:44:09 OK.

Joseph Brondolo (SHRSS)** 1:44:12 Yeah, I had. I had a story for this and I I couldn't find those four
labels there.

**Daniela Tea** 1:44:15 Um.

**Scott Sorel** 1:44:16 Thank you.

**Daniela Tea** 1:44:17 OK. OK, let me see if I wonder. Actually, hang on, I wonder if this is
actually. I might have to get back to you on this. This might be something that
that is potentially being used, like you like a user won't be able to
see it, but it might be something that's within the markup. So let me
get back to you on that one, Joseph. I'll add that to the list for
things to cover at the beginning of tomorrow's session.

Joseph Brondolo (SHRSS)** 1:44:31 Oh. Mhm. Mhm. OK, great.

**Daniela Tea** 1:44:49 Great. Thank you. OK, Luke, did you want us to?

**Lucas Nelson** 1:44:54 Yes. Yeah, I mean, I I it's not gonna be like an official retro board or
anything like that. Yeah, I just, uh, oh, yeah, go ahead, my too. Sure.

**Daniela Tea** 1:44:58 Oh, OK.

**Mayte Eme** 1:45:01 One more question. Sorry, one more question. Luke, I'm sorry, I'm
seeing those huge logos. So did we ask you for the specs for the images?
So we don't have that issue because some of the the things you were
showing had like the images.

**Lucas Nelson** 1:45:07 You're good.

**Mayte Eme** 1:45:18 Even corrupt at at some point.

**Daniela Tea** 1:45:22 Yeah, that's something I think is is still that we're we're still
looking into that my day. We do not have the spec sheet detailed out as
of yet.

**Mayte Eme** 1:45:27 Oh, OK. OK, but since this site is going live soon, are we going to then who's
going to go back and fix those images so they don't look, you know,
like this when we're going to go live?

**Lucas Nelson** 1:45:55 What is happened as a take away, Daniela, to talk with Vinay and you
know, whoever's supporting him with authoring might say, yeah, sorry,
I.

**Daniela Tea** 1:46:01 OK.

**Scott Sorel** 1:46:02 Yeah.

**Lucas Nelson** 1:46:06 Any other questions?

**Lisa Cardia** 1:46:09 So are our questions just getting looked at in tandem with the like
things that Angelica and team have already reported? Cause I think like
a few of my questions go hand in hand with what she's reported.

**Daniela Tea** 1:46:09 Mm.

**Lucas Nelson** 1:46:21 Yeah, I think there's some synergies there Lisa and honestly Scott and
Angelica, I hope you know we we we have a little bit of you know clarity
from this call as well when when we have syncs with you guys moving
forward at our tactical level that that'll.

**Daniela Tea** 1:46:28 Yeah.

**Scott Sorel** 1:46:34 This.

**Lucas Nelson** 1:46:41 Address some of the ones that we kinda have parked right now. So we'll
we'll see though how that goes. But yeah, Lisa, um, they're they're
they're kind of addressed in tickets and and you guys touched on on
this call to answer your question.

**Scott Sorel** 1:46:46 Yeah.

**Lisa Cardia** 1:46:54 OK. Thanks. Sorry. Yeah, go ahead.

**Mayte Eme** 1:46:54 And I do have one. Oh, go ahead. No, you go.

**Lisa Cardia** 1:46:58 It's OK. You're you're fine. Got it.

**Mayte Eme** 1:47:01 OK, maybe I don't know who's this for Adobe or or our IT team, but I
was looking at pagination, right? I I remember in Daniela was like 3 or
10 or 30. Is there any recommendation? Because I know we've done that
before and we have performance issues. So have you guys tested and know what's the Max number of listings we
should have on a page knowing we have like, I don't know how many
Angelica, we have like hundreds of jobs.

Angelika Akopyan (SHRSS)** 1:47:32 800.

**Mayte Eme** 1:47:34 Yeah, so knowing we have 100, you know 30 seems like too few right to go
like 30 by 30. And I know there's filtering, I know they're searching,
but is there a recommendation on the Max number of jobs we should list
per page based on your testing?

**Daniela Tea** 1:47:48 But.

**Lucas Nelson** 1:47:51 Are you asking Adobe that question, Maite?

**Daniela Tea** 1:47:51 Mhm.

**Mayte Eme** 1:47:54 I I don't know who did that performance and the load or stress testing.
So that's why I said maybe Adobe or TJ, one of you guys should know the
answer.

**Lucas Nelson** 1:48:02 Scott, I think you're gonna have to take it back and talk with with TJ
and Mohsin. We we we don't currently have a performance testing
resource. Yeah, right.

**Scott Sorel** 1:48:10 Yeah, I don't think that's a yeah, I I don't I that that's not on
the radar at all my day. I I don't know why that would be an issue. It
seems like chump change Rogers 30 or 800 or even 1500 as far as as far
as listings when you think of like you know content I I that's not
that's not heavy listing.

**Mayte Eme** 1:48:27 I I hope you're right. We had that issue before that we're like, oh,
great, let's put 50 and boom, it crashes, right? So if we can just get
an answer, please.

**Lucas Nelson** 1:48:36 Just to be clear, from the Adobe perspective, we're not qualifying it
as light or anything. We just don't have any resource scope for it,
Maite. Just wanted to be clear on our point of view.

**Mayte Eme** 1:48:42 Mhm. OK. OK. Thank you.

**Lucas Nelson** 1:48:47 No problem. Last call. Any questions?

**Scott Sorel** 1:48:53 Hey, so Luke, just with a couple minutes left. So how did you guys, you
know, I'm just kind of curious on the side side, how do we think this
went? Did we, did we get through Daniella, what you're hoping to get
through for one session? Do we go slower? Do we go faster?

**Lucas Nelson** 1:49:03 Yeah, Scott that that that that that's a perfect foray. I I was gonna
give my my point of view on a on the on the retro of this. We did get
through Daniella's intended topics on on this. And which is good. So we're tracking, which is great. We're going to
have to take a, you know, keep the retros going as we see how we do
using the A I notes and then and and making sure we're capturing. Follow-ups accordingly from the questions answered here, Scott. So
that's something for you and me to to make sure you know we're we're
not leaving too many gaps. The other part about this call that I think
might be slightly different than the other calls is Careers is an
in-flight site that that it's going to go live next month.

**Scott Sorel** 1:49:39 Mhm.

**Lucas Nelson** 1:49:54 So there's a lot of extra heat and scrutiny on careers compared to just
level setting on, you know, knowledge transfer of how the platform has
been implemented. So I just wanted to make sure everybody's clear on
that, like these questions that you've been asking. It's great to hear them. I I we had no issue with that, Scott, from our
point of view, especially given on careers, OK.

**Scott Sorel** 1:50:17 Mhm. Yep, Yep.

**Lucas Nelson** 1:50:21 So yeah, so that that that that's that that's what my point of view is
on how this went. But you know open to to hear any other feedback from
you guys that that that you know you want us to hear, yeah.

**Scott Sorel** 1:50:31 Yeah, I I I do feel like it was rushed. I I I yeah. So I was just
curious about Daniela in her mind's eye. She probably laid out what she
would hoping to get through and if she got through it.

**Lucas Nelson** 1:50:42 Yeah, she she's she's good. She knows she's a she's a seasoned pro.
So Yep, we appreciate Daniella. Any other feedback from you guys?

**Scott Sorel** 1:50:49 OK.

**Lucas Nelson** 1:51:09 Yeah.

**Lisa Cardia** 1:51:09 Is I think that we're gonna start piling up, if I'm being honest.

**Lucas Nelson** 1:51:13 I I completely agree in the background saying the same thing, Lisa,
it's the tab's going to be quite big at the end of it with the gap
analysis, but that's what we need to identify, right? Like we need to
get it all out. You guys need that full baseline understanding.

**Scott Sorel** 1:51:19 OK.

**Lisa Cardia** 1:51:25 Yeah.

**Lucas Nelson** 1:51:28 That's what our intention is here. Yeah, so.

**Lisa Cardia** 1:51:30 I think like this first week is gonna be the true test. If we make it
through what, 4 sessions this week, you'll see what that list becomes.
And then it's like gonna paint the picture of how the rest of these
like weeks are gonna go if they can go in the same manner.

**Lucas Nelson** 1:51:35 Mhm.

**Scott Sorel** 1:51:37 Mhm.

**Lucas Nelson** 1:51:42 Mhm.

**Scott Sorel** 1:51:44 S.

**Lucas Nelson** 1:51:45 Yeah, yeah, exactly, Lisa. Yep. Good feedback. Anything else, guys? All right, cool. Well, we appreciate your time, Daniela. Great job as
always, and we'll look forward to seeing what you have in store for us
tomorrow, OK?

**Daniela Tea** 1:52:05 Alright, thank you everybody for doing.

**Lucas Nelson** 1:52:06 All right. Thanks, folks.

Angelika Akopyan (SHRSS)** 1:52:07 Thank you so much.

**Lisa Cardia** 1:52:08 Thank you. Thank you. Thank you, bye.

**Daniela Tea** 1:52:09 Goodbye. Thank you.

**Lucas Nelson** 1:52:09 Right.

Charles Baugh (SHRSS)** 1:52:09 Thank you.

Gonzalo Calasich (SHRSS)** 1:52:09 Thank you. Thank you. Bye.

Charles Baugh (SHRSS)** 1:52:10 Everyone.

**Don Middlebrook** 1:52:12 Thank you.

**Scott Sorel** 1:52:12 Thank you.

Lucas Nelson** stopped transcription



## Session: Events — 2026-02-11

**SHRSS Adobe Knowledge Transfer-20260211_130309-Meeting Recording**

February 11, 2026, 6:03PM

1h 55m 18s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:11 OK, sounds good. Recording started. As we said yesterday, we would start
this call by just kind of briefing on the the, the, the questions and
and what answers we were able to to to to provide so far. To provide so far on the the Confluence page, we did, we did want to
make sure we acknowledge that yes, we saw all the questions and we're
working through trying to provide answers and that's what we wanted to
start with. Daniela, I think is just kind of. Propose how we want to handle the number of questions we're seeing. Is
that right?

**Daniela Tea** 0:49 Yeah, yes. Let me go ahead and share the confluence page. So thank you
everyone for providing your questions and especially in this tabular
format, I think this is great. They were able to clearly see what's
being answered and by whom. So right now I have this sorted by the rows are sorted by answer. So you
can see there are still things that our team is planning on reviewing.
We just of course need just a little bit more time. We understand that
you know that these questions are going to come after these knowledge
transfer session like the knowledge transfer session. That we just attended. So what our plan is in order to be able to make
sure that we're answering things as accurately as possible and with the
proper context, we are just asking for a little bit more time for us to
be able to go through these questions. The onshore team will be reviewing these after the page is complete. So
Maite, I do appreciate you tagging me to let me know when the questions
were in a pretty good state because as I was refreshing, I was seeing
more added. I wanted to make sure you guys were at a good stopping
point. So what that means is we would need some time for us to be able to
review them and then we also need to connect with our GDC team members
to be able to ensure that they are also providing answers where
necessary, specifically with the technical questions. And as we're responding, we also recognize that there might be
instances where, for example, you'll see here we have tagged some other
folks to to be able to chime in. So there are times where we will need
somebody else to address the part of the question that Adobe is not able
to answer. And also we also recognize that based off of the response that you're
getting asynchronously, you might have a follow-up or something still
related to that or perhaps need some clarification. What we're asking
with with those kinds of instances is if you could perhaps highlight the
specific row, take this for example. If this is something where you have a follow-up question on, if you
could highlight the row and add your follow-up question to the existing
row, then our team knows OK, this is something that we need to look back
at and address. So that would just make it easier for us to be able to
group things together as well as be able to understand what is still. Needing to be answered. I'll pause here to see if there's any comments
or questions about this process.

**Mayte Eme** 3:24 Makes sense and and thank you. I know there was a lot and I tried to
combine everything. At one point I just kept my name because it was
easier copy pasting and I deleted a few that I thought were duplicate.
So hopefully that helped and I was thinking I I'm seeing in your screen
and and I glance at it in the morning the ones that are assigned.

**Daniela Tea** 3:33 Yeah. OK. Mhm.

**Mayte Eme** 3:44 To SHRSS, should we put them in a separate table or tag them somehow so
they say separate from the ones assigned to you as in you know Adobe
Team versus SHRSS for answers?

**Daniela Tea** 3:56 Right. So I guess, yeah. So let's take a look at these. For example,
like you mentioned Mighty, they are a couple of these are all all
something we would need SHRSS inputs on and I think we need to
understand for example, we've tagged Shoab and and TJ here. I believe
TJ is on the call. What is the best way to get these questions? To you is confluence appropriate to tag and then have you review and
answer here. Is this something that needs to be brought out to a
separate location? Yes. Sorry, is TJ on the call? Sorry, I can't actually see the attendee
list. Oh, OK.

**Scott Sorel** 4:40 He was. He was. He's here. I see his name.

**Daniela Tea** 4:44 Yeah, I think we just need to understand because you know, we could
certainly tag them here, but if this is, if Confluence is not the right
place to be able to get those answers from those individuals, we we want
to make sure these aren't getting answered, but they need to be
directed in the.

**Scott Sorel** 4:58 Well, I I think, yeah, Danielle, I have a suggestion in that like for
example, there were some for show up, right. So I I I hit them up on
Webex chat before we started and I think that we're going to have to do
something like that because I don't think you get too many emails from
councils of it's very easy to miss them and we really want to make the
best use.

**Daniela Tea** 5:04 Yes, that's correct. OK. Yeah.

**Scott Sorel** 5:17 Of time and not be waiting. So yeah, so I guess when we get we get done,
I I can just take it upon myself and take a look really there and try
and nudge people of, you know, do your homework. But I don't know. TJ,
what do you suggest? Because like I reached out the show, but he didn't
answer me and he's not here.

**Daniela Tea** 5:19 Sure.

**Scott Sorel** 5:36 That's not really going to get us where we want to be. If anybody else has a suggestion on, you know.

**Lucas Nelson** 5:45 Scott, let's not spend the paces here. Can you have an offline with TJ
and Shob and?

**Scott Sorel** 5:48 OK, Yep, I'll have it offline. But Luke, in general, just like you did
with me before earlier, if there's somebody who's not really leaning
in or we need something, let me know and I'll just go start rattling
cages until we get answers. All right.

**Lucas Nelson** 5:58 Let let me know what the outcome is about how you want to handle that
and and then we can follow suit with how you're gonna handle SHRSS
assigned items. OK, Scott.

**Scott Sorel** 6:00 Yeah. Yeah. Yeah. Yeah, yeah.

**Lucas Nelson** 6:11 All right. Thank you. All right. Keep going, Danielle.

**Daniela Tea** 6:11 Yeah, sure. And Yep, the other point I wanted to to mention is we also
realize that some of these questions, since we're trying to have them
isolated to just the specific session that we had and while I I know
that a lot of these questions are related to the careers website.

**Scott Sorel** 6:13 Let's get going, Daniel.

**Daniela Tea** 6:31 There are times where, for example, like with the video testimonials,
which are video cards, that's going to be covered in a separate
session. So what we are planning on doing is we're going to have
essentially like a question backlog page and filter out those questions
and put them there so that way they can be moved to the appropriate
agenda. End of page when we actually cover it. So there will be visibility as to
which questions have been removed from this table and there will be
moved to that backlog page. And then once those new agendas are
appearing, for example, we have say like a card component. Pretend we have a card component training session. We'll be adding any
questions related to cards that were not answered within this agenda
added to that specific agenda. So I'm going to pause here to see if
there's any questions or comments about how some of these questions are
going to be removed from here, but we will be addressing them in the
future. OK. Great. Okay. Was that? Yeah.

**Lisa Cardia** 7:33 If you don't mind, sorry, if you don't mind, I just wanted to add and
it was just like one that I happened to glance over. So some of the
questions that we did include here, I hope that you don't feel like we
did answer that in the call. This was more so to make sure we have in
writing in case anyone else came through with the same question and
since it was explicitly asked in the call, we might have added it here
just for that.

**Daniela Tea** 7:39 Mhm.

**Lisa Cardia** 7:52 Answer. We noticed like something wasn't the same answer as what we got
in the recording, so.

**Daniela Tea** 7:57 Right. Yeah. So Lisa, that's where I was saying we need a little bit
more time. So that way our teams can can have a connect session with the
offshore team. So the onshore, onshore team and offshore team will be
connecting. That's why we just need another extra 24 hours. before we will be putting the answers to these questions.

**Lisa Cardia** 8:18 OK, but not I'm talking about ones that like had the answer answered on
answered by not blank ones. So I just wanna make sure it's not like a
disconnect there.

**Daniela Tea** 8:26 Yeah. Yeah. So, so we actually did connect after some of these were filled out
and as we were reviewing some of the answers and responses, we that's
why we recognize that, oh, we do need to make sure that we have our sync
time before we are just posting things on here because keeping in mind
that for example, our offshore team isn't necessarily on the call. Not be interpreting the question the same way that it was asked within
the call itself with some additional context. That's why our proposal
is for the onshore team to go through first before we hand things off to
our offshore team to answer any other technical questions. So if you're
seeing discrepancies on some of these answers, we're hoping to get that
resolved with the.

**Lisa Cardia** 9:09 OK.

**Daniela Tea** 9:09 Process. Yep. Any anything else before we move on and and just to confirm that the
team is because I'm not clear if you all are are getting notifications
when these are being responded to or if you guys are able to review this
or or or were notified that this page was updated with some answers. Just want to make sure that your team also has time to review these
answers as well and I see Gonzalo's hand is up.

Gonzalo Calasich (SHRSS)** 9:49 Thank you. So I I do have a question. So does it means that we need to
go first to this confluence space to put a question or or for example
will this be for components that we already went through or or we can
raise the questions here?

**Daniela Tea** 10:04 So these questions here are specifically for the session that we had. So
ideally, you know, we'll certainly try to answer as many as we can
during our actual call. However, we do realize that that the team needs
time to also come up with additional things. However, the intention of
this is for questions related to the session. And anything that's not related to the session, we're planning on
adding to our question backlog, which will be a new page added here. And
as we continue to cover more topics and we create more agendas, those
questions will be moved from the question backlog to that specific
agenda page.

Gonzalo Calasich (SHRSS)** 10:41 OK. Thank you.

**Daniela Tea** 10:43 Yep. Great. OK. So I think in terms of after actions, I think Luke, if we can just
put a reminder when we send out the recording and transcript for the
process with regards to like highlighting and that sort of things and
then also perhaps a link to the question backlog and I can we, I can
work with you on that after the call, but we can send.

**Lucas Nelson** 11:06 Yeah, right, right on. Sounds good.

**Daniela Tea** 11:07 That out as a follow up. OK, perfect. Awesome. Thank you guys. All right, so let's go ahead and
get started then with our next session, which is events, and I'm going
to pull up all my test pages and such over here. So one second as I get
situated. Alright, OK. OK, so let's go start from the very beginning as if we were just
logging to AEM for the first time. What I'm going to do first is I'm
going to review the event content fragments and we're going to create a
new one and also review some existing ones just so you can see. See some of the data that's there and then also we're going to take a
look at our event related components, specifically the event calendar
and the event detail page. We're also going to create a new event
detail page using the event detail template. All right, so oops, did not mean to click that. OK, so now I'm going to
navigate first to the DAM to where our content fragments are located. So
I clicked on Assets and Files and we are in our SHRSS folder and then we
are in CF. And just like we saw with jobs, there's a separate folder for events
here and we're going to take a look at the existing structure and I
just want to to explain how this was previously set up during the
migration. So here right now we have cafe and hotel events and the breakdown for
those as you guys can see is the line of business, the specific
property, the specific language and then it gets broken down by date and
month. And then finally based off of the month, this is where all the
events get dumped in. So to be clear, this particular structure is actually set up for ease of
authoring. The understanding is that yes, there can be several events,
you know, per month, per year, and so this here is broken down. So that
way it's easier to be able to find events. So you're not dealing with an infinite scroll. So, so just to be clear,
that's the reason why in some cases you know like in in here you don't
see like 2026, you don't see previous months or anything like that
because during migration the perhaps there were no events for that time
frame. But if if for whatever reason you need to say change the structure, this
is this is a structure that we had set up for the ease of authoring and
being able to find events based off of a specific month. So we have
followed that. For all the locations for across hotels and cafes, we followed that
structure, but just wanted to make sure that you're aware. And Don, if
you're listening, especially if if you are, you know, thinking about
how this could be modified in the future, just want to let you know this
is this was a set up we had, but it was. Use of authoring. OK, all right. So with that being said, what you can see here is I've
created a folder called KT and so this the way that this would work is
if for example say you all have a new hotel or something, you would put
it within hotel, you would put it within cafe, but if you all have. Have say a separate line of business entirely, it would probably make
sense to create a completely different folder. So that's what I've
done here and I just tried to follow the structure that we had
previously just so that way I could keep track of the events that I was
creating. So in this case you can see I have.

**Scott Sorel** 14:39 OK. No.

**Daniela Tea** 14:53 My month folder 02 and 03 within 2026 and so then I just put some
content fragments here. So what I'm going to do now is just within this
02 folder I'm going to create a new content fragment. Using the event model. And let's just call this test event. And I hit create and now the content fragment is created. Now one thing
I want to note is that by default the editor is displaying in the new
content fragment editor and so you you may notice if you have ever
toggled this off that there are actually. A few differences between the new editor and the old editor. So just to
show you, you can see it's it's laid out a little bit differently and
I did want to inform the team here that we are actually having a support
ticket created with the product team, so that way it will default to the
old. So that way an author does have to change it. The reason why we're
doing that is because within the new editor there are some differences
within the way a field is rendered, and as we were doing our testing, we
wanted to make sure that authors are not running into any issues or. Discrepancies by using the new editor. So once the support ticket has
been fulfilled, we'll notify the team. But the way that you would be
able to see content fragments moving forward is with this view. So I
want to make sure that the team was aware of that. That's something
that's in progress from the Adobe side. OK, so for the time being though, I'm going to just show when you open
up a content fragment, it's going to look like this. I'm going to
toggle it by switching from new to old just for the time being now. In
the future you will not have to do that, OK. So here is my new content fragment for test event. Just going to open
this up a little bit wider and let's take a look at the fields that we
have here from top to bottom, and then we'll take a look at the event
calendar and see how this all maps out. All right, so for my title, I'm just going to put my test event. Again,
I can name this anything. It doesn't have to match, but in this case
I'm just going to put it here. I'm going to put my start date. I'm
just going to set it for, let's say, February 15th. I have my start time which is a required field. I click here I can put
the hours and minutes set AM to M. So let's say 9:00 AM. You'll notice end date is not a a required
field, and that's because if your start date and end dates are the
same, you don't need to fill it out again. However, you do need an end
time. O I'm going to just put. 12:00 PM, 12:00 PM All right, so now let's move on here to the banner
image and banner image alt text. And I'm just going to set an image
here. I'm just going to take something from the dam. So this is going to be something random I'm just going to select just
for the purpose of this and I can put my alt text here. And then here is another image field. This image field is going to be
displayed on the event details page, which I will pull up once this
event is created so you can see how it maps and I'm going to set
another image from the dam. So I'm just going to choose something. Let's choose that. And this was, I think it was Rock City. OK, so this is a required field.
The banner image is not and I'll show why in a second. But we as an
author, we need to make sure this field is set up so it's displayed on
the event detail page. As I continue to Scroll down, we do have event status. I'm not going to
set that right now since it's not required, but we will edit this event
content fragment so we can see how that gets displayed. Here's an event
status message, also not required. Description is though, however. We also have an additional detail section which appears underneath the
card and it's not required, so I'm going to leave it blank just for
the time being. The CTA links are also not required. That's because by
default if you don't put anything here, it should have a link. That will take you to the event detail page. So for right now, let's
let's leave this blank and then we can see how that gets populated. We also have categories and from here this is actually pointing to a
specific event category tag section. So there in the tagging structure
there's a folder called Event Categories and these were the tags that
have been identified for events. I recognize and realize that there could be additional tags you might
need in the future, and so the way that that would be updated is by
adding those tags within the tagging section. Right now though, this is
the list that's currently under this folder, so I'm just going to
check something for the time being. And then for location reference, what this is going to do is as an
author you are going to select which location that you want your event
to be associated with. And this is all content fragment based coming in
from DPLT so. In this case, I'm just going to select this. I recognize that here this
ID that's coming in. This is, you know, it's not clear to me exactly
what this location is. So I and I understand that that may be, you know,
difficult as an author to be able to choose. For the time being right now the way that I have been checking is by
clicking on edit and then seeing what the property legal name is for
that particular content fragment. And I lost all my information because I forgot to do my new dev. So one
second. All right, we're going to make this really fast. All right. So that is something that I believe would make sense to put on that gap
list is to perhaps have that information for the title on on the content
fragments for ease of authoring use. And I'm going to go back and check my category. And then I'm going to select a location here. I'm just going to select
the the hotel here at Maya, which I believe was just here. I'll just
use this. It's fine, OK. Underneath here you'll see there is a featured check box. If I check
this, and again we'll show this in a bit once there's a couple more
events. If I check this, what this means is that this particular event
will appear at the beginning of the calendar for the specific month that
I'm viewing. So in this case we're in the month of February, so. Even though the calendar will display chronologically, if I put this as
feature, this will be the first event depending on if there's other
featured events. So we'll see that in a second. You'll also see here
this event ID. This is a read only field. This is getting. Generated as it's passed as part of the URL which on the event details
page and we'll see how that is right now since it's read only.
Obviously you're not able to change that. If that's something that is
desired in the future, that is something that we would want to discuss
during the gap analysis portion. The reason why we have this generated event field though is to prevent
any sort of duplicates from occurring. OK, so I'm going to go ahead and
save my event content fragment and I'm going to close this. So we can see here this is my test event and I am going to publish it.
So that way when I look at the calendar I'll be able to actually see it
on there. So I'm actually going to pull this over here and I'm going
to navigate to my test calendar page that I had created. So I went to sites, SHRSS, corporate careers, English and you can see I
created some test calendar events and I'm just going to open up my page
here. And you're going to see right now that my specific event that I just
created is not appearing here because I did not publish it. O let's go
ahead and publish the event. OK, so I'm publishing it. It's saying OK, this is the content fragment
model of the content fragment I'm just publishing. When I refresh this
page, I'm also going to view it as published, but when I refresh this
page. Now I can see that my test event has appeared, so I want to make sure
that process was clear. I'm creating events. You may think why is it
not on the calendar. You want to check and make sure that the event is
actually published and then when you refresh your page you should see it
there. I think I saw a hand up, but not sure who it was. Sorry.

Gonzalo Calasich (SHRSS)** 24:56 Hi, this is Gonzalo. How are you? So we are seeing that you're using
the view as publish and we're seeing that changes come really fast, but
when you actually navigate to the publishing environment, they take too
long to to show up.

**Daniela Tea** 24:57 Sure, go ahead. Mhm.

Gonzalo Calasich (SHRSS)** 25:14 For example that the jobs right when you were demoing the jobs so they
they were coming really fast but we were trying we were playing with the
jobs and we created a new one or make a change but we couldn't see the
the changes. If we if we use the view as published this yes we will be
able to see it but we will not be.

**Daniela Tea** 25:20 Mhm.

Gonzalo Calasich (SHRSS)** 25:33 Be able to see it on the published environment. Is there a way so we
can, you know, expedite that publishing or we just have to wait the 5
minute rule because we waited more than 5 minutes many times?

**Daniela Tea** 25:45 So. Right. So I think this would be something we would need a little bit
more information on Gonzalo like you know to to take a look at like for
example, is it something that's being cached? Is it because someone
else is publishing the page? You know that I'm not quite clear exactly
like this the exact situation. But it sounds like to me you guys said on the actual. So if we were to
go to like like you're talking about this publisher like, is that
correct?

Gonzalo Calasich (SHRSS)** 26:16 Correct, yes.

**Daniela Tea** 26:17 OK. And what you're saying is that when you added a new job, was it
through Workday or was it through just like a content fragment?

Gonzalo Calasich (SHRSS)** 26:18 Oh. This is just like a contract requirement.

**Daniela Tea** 26:27 OK, so you're saying when you added a new job, you're unable to see
the job appear on here even after you published the content, correct?

Gonzalo Calasich (SHRSS)** 26:29 Oh. Correct, correct and we were able to see it on the on the authoring
using the view as published, but it was not reflecting in this in this
page.

**Daniela Tea** 26:37 I. Mhm. OK.

**Andy Lambert** 26:47 Is it ultimately showing up, Gonzalo, or just or is it not showing up at
all or is it taking time to show up?

Gonzalo Calasich (SHRSS)** 26:53 No, I'm not showing up at all.

**Andy Lambert** 26:55 OK, so then now there's some kind of blocker happening in the
environment.

Gonzalo Calasich (SHRSS)** 26:58 Most likely it looks like cash.

**Andy Lambert** 27:02 Well, it depends if the page is. I would have to check with Vinay on how
this page is loaded, but if it's if it's front end then it shouldn't
be cached. If you publish the content fragment right, it should just
show up if it's enabled and all of that so.

Gonzalo Calasich (SHRSS)** 27:20 Yeah, I just wanted to bring it up that because I know that you are
using content fragments. So I just wanna if you can show us on the on
the publishing and see if that if the events are having the same issue.

**Andy Lambert** 27:21 And. Yeah.

**Daniela Tea** 27:24 Mhm. Yeah, so let's actually publish this page. OK, so this page to publish
and let's take a look. What do I call this corporate KT calendar?

**Andy Lambert** 27:33 No.

**Daniela Tea** 27:47 So this is the first time I published this event, so there's absolutely
no cache. So this would certainly, you know, be displayed pretty
quickly. But Gonzalez, throughout this call, because I will be adding
some more events, we can certainly kind of monitor that to just see, you
know, if we're experiencing any issues with. Publishing new events and how quickly it's getting to this publisher
link. OK, Yep, sure thing. OK, so let me navigate back though to the
actual components. That way we can take a look at how our content
fragment maps to this and we'll continue monitoring the published link.
So I'm going to open up again.

Gonzalo Calasich (SHRSS)** 28:11 Thank you.

**Daniela Tea** 28:27 My test event. And we are going to take a look at this test event here, which is on my
calendar so we can see. I'm going to make this smaller second, OK. So we can see here test event is appearing here on as a title of the
card. We have our start date of 2/15/2026, 9:00 AM, 12:00 PM. So that
appears here within the time section. Here we have our location. This is based off of that location reference
that I had selected. It's pulling in the address and you can see when I
hover over this, there is a URL associated with it. In this case it's
Playa del Carmen. So that that information is coming based off of the location reference
that I had made. And then here you'll see, as I had mentioned before, I
did not put anything within the CTA links by default. What's going to
happen, it's it's going to show a. Another a CTA button here which is going to link to the event details
page if you leave that blank.

**Scott Sorel** 29:38 OK.

**Daniela Tea** 29:41 Oh, and then also the image that I selected here, my guitar smash,
that's what's being displayed here. So this image field corresponds
with the image just displayed in the card. I'll pause here to see if
there's questions about how the content fragment fields translate to
what we see in the event calendar.

**Lisa Cardia** 30:01 Yes, Daniela, I have some authoring questions that I think might be
useful at this time.

**Daniela Tea** 30:07 OK, sure.

**Lisa Cardia** 30:08 OK, to start, is the there availability for us to put a override for the
date field? There's a lot of times we have events where we like to
change it out to not say the actual month and day and the time, but
rather. Rather, every Wednesday through the month of February, something like
that. Do we have an override?

**Daniela Tea** 30:30 So that's not available within the event content fragment right now.
When we take a look at promotions, there is that field and I think
that's probably the behavior that you're that you would like to see
here in events too and and we can kind of confirm that if that's the
kind of behavior you would want in events. Um, during the gap portion, but we will take a look at promotions, Lisa,
I think in like 2 days or so.

**Lisa Cardia** 30:54 OK, the same question would go for the location. I know that those would
be two placements that authors like to override from time to time, just
requested from properties. And then my second question is the option for
the image. It looks like we could add.

**Daniela Tea** 30:57 Mhm. OK, mhm. Mm-hmm. OK.

**Lisa Cardia** 31:12 Additional What happens if we add an additional? There was another add
below image.

**Daniela Tea** 31:17 I believe it just defaults to the first one. I can certainly test that
out later to see. Usually as we've been when we were doing the
migration and such it was only using just one image. But this yes this
is a multi field but I don't think it's going to take into
consideration the other images but we can confirm that.

**Scott Sorel** 31:26 Yeah. OK.

**Lisa Cardia** 31:36 OK, I'm just writing this down at the same time. I'll hold off on my
other question related to banner image. I know you didn't get to the
actual more info page yet, so my my question is going to be related to
why we would even have this as an option. Would it override it if it's
configured from the page template? So we can skip that one.

**Daniela Tea** 31:42 Mm.

**Scott Sorel** 31:43 Mhm.

**Daniela Tea** 31:45 Yep. Mm-hmm. Sure. Yeah, we'll take that.

**Lisa Cardia** 31:54 But for events, for the event status, is there a way that we can do some
sort of logic so that if presale we have very specific presale dates
which would then show you know a presale disclaimer of a password. But
then once that presale date and time have passed, we revert, we
basically revert back to a.

**Daniela Tea** 31:58 Mhm.

**Lisa Cardia** 32:14 Where the card might just say on sale. So is there any logic I guess is
my question behind the event status labels because typically we fill out
all at once an announce date and on sale date and pre sale dates.

**Daniela Tea** 32:17 Mhm.

**Lisa Cardia** 32:29 And then it will know and recognize the state of the the date in which
it's presale and then go back to normal state. Does that make sense?

**Scott Sorel** 32:37 Oh.

**Daniela Tea** 32:38 OK. So yeah, let me let me reiterate what I've heard. It sounds like
what you're saying is that if you were to create a new event, you are
aware of the different event statuses and the and how long those would
be displayed. And so the ask is to be able to associate multiple event
statuses with a date. So that way you would just automatically display
on. To the card without the author having to come in every single time to
change the status. Is that correct?

**Lisa Cardia** 33:03 Exactly because like probably events are our most frequented item I'd
say. So for content author to only have to add the event once filling
out every field so that we don't have to remember at 9:00 AM do we need
to go change the state of this at 10:00 AM did it change back kind of
thing especially cause pre-sale dates.

**Daniela Tea** 33:04 OK. Hello.

**Scott Sorel** 33:23 So.

**Lisa Cardia** 33:23 Can be way outside of business hours or weekends, so just something to
take into consideration, but I can move on. The other question was the
call to action link that is the more info.

**Scott Sorel** 33:25 OK.

**Daniela Tea** 33:26 1. Yes, yes.

**Lisa Cardia** 33:40 We skipped it because it's automatically getting populated. There are a
lot of times that we don't make a landing page associated with the card
just because there's not more information for that that person to get.
A lot of these entertainment acts are like very local level artists, so
we don't give them more than what it is of date time.

**Daniela Tea** 33:43 Mhm.

**Lisa Cardia** 34:00 An event location, so we would hide that call to action. Is there a way
to hide that button so that if we're not putting one, there just is
none?

**Daniela Tea** 34:09 I see. OK. I believe that the way that this was we were doing the
initial requirements. The understanding was that there was going to be
an event detail page associated with it and that's why this is the
default. Even if you put anything sounds like it would be useful that
if. There was say like some sort of toggle or something to be able to just
hide it entirely. So I guess Lisa, to be clear, like in terms of say
sending out the event to like people like that means that you wouldn't,
you would have to send out the full calendar. Is that currently what the
team is doing right now?

**Lisa Cardia** 34:33 Yes. Yeah, so there's some property sites that will use event calendars just
to show weekly free entertainment. And so it doesn't really give them
much to to click more when when we don't build out pages for those
artists outside of like the very ticketed events that we can share much
more detail.

**Daniela Tea** 34:51 Ah, OK. I see. OK.

**Lisa Cardia** 35:02 So it's just having the flexibility there so that we don't force a
user to click more info and then ultimately they don't receive more
information.

**Daniela Tea** 35:10 I see. OK, yeah, so so to your point, I understand the use case now.
Right now it will default and it will just essentially just if there was
no, say there was no like additional details or you know you didn't,
you didn't set anything else, then it would show basically the exact
same information. On its own page, but we like, I understand what you're asking for to be
able to actually prevent that by not having that that display. I see.
OK, yeah. So yeah, definitely that would be something that would be
added to the gap since that would be a slight change from what we have
right now.

**Scott Sorel** 35:31 Right.

**Lisa Cardia** 35:36 Exactly. It's just more for the user's experience. Um. Great. And then my other question is related to the location reference,
since every property would essentially need to know their number from
the DPLT until that there is a way that we would know that 3150 is
whatever property.

**Daniela Tea** 35:53 Mhm. Yes.

**Lisa Cardia** 36:04 Is it at least limited by user access? Because my assumption would be if
you've already built the content fragments in the correct property
folder and timeline that we wouldn't need to then select the property
again somewhere as the source. So I would just hate for someone to
choose the wrong location reference and have access to. Amsterdam if they're adding a Mexico event. So my question is the
location reference, is there a way to limit it to the user so that
they're only, especially in cafe world, only adding events for their
location and not by mistake?

**Scott Sorel** 36:28 No.

**Lisa Cardia** 36:39 Controlling someone else's? Or does that not get impacted if the wrong
one is selected here? I just am finding it difficult to follow along if
we've already put the content fragment in the right folder path, how
it's getting picked up by a property location reference.

**Daniela Tea** 36:48 Mm. Mm. OK, so let's take a look at, yeah, so the location reference you can
actually see here and I think we're taking a look at the event calendar
configuration right now is is hopefully going to be able to shed some
light. So the location reference, this is not actually something that you even
need to fill out right now. What you're asking for is if I as an author
am just a cafe owner specifically for say this Mexican location, you're
saying I ideally I would not be able to have. To even select it, is that correct?

**Scott Sorel** 37:30 Oh.

**Lisa Cardia** 37:32 Yeah, I just don't understand if we've already built it in the path
that it needs to be while now we need to also reference it. But if
that's for the filter, I guess that makes sense. It's just now I want
to make sure that no one has access to put a different location or else
we're going to see, we're going to see mistakes being made, if that
makes sense.

**Daniela Tea** 37:39 I see. Yes. Yeah. Right. So yeah, this location reference because you can see I when I
created my content frag, sorry, one second, I'm trying to open up. OK,
here we go. You can see in my content fragment what I was trying to
highlight here. You can say put Valley here because I was just showing
this similar structure even though I put Valley here.

**Lisa Cardia** 38:07 Yeah, right.

**Daniela Tea** 38:10 Obviously I did not create a Bali event and that's simply for, you
know, authoring organization like like you like you saw here. Yeah, this
was necessary, correct. That's correct. And if I wanted to, let me show
this here right now, the reason why it's showing.

**Lisa Cardia** 38:17 Got it. So this is necessary for it to actually work, but the rest was
organization.

**Daniela Tea** 38:29 All my events, regardless of the location, you can see I actually had. I
have four events located in this folder. Those four events are from
different locations. You can even see them displayed here. This is
Ontario. This is Mexico, Indonesia and Florida.

**Lisa Cardia** 38:37 Mhm.

**Daniela Tea** 38:46 And because those four content fragments are from different locations,
the location filters and populate it with each location that they're
from. Same thing with region, right? And then categories, it's a roll
up. So I think in the instance of say like a specific cafe, what would
happen is that this content.

**Lisa Cardia** 38:55 Mhm.

**Daniela Tea** 39:05 Content fragment folder path should only point to the events for that
specific location and if there is a mistake within the content fragment,
that is something that would have to be updated within the content
fragment itself, but you would be able to see it based off of what if
anything else were to appear on.

**Lisa Cardia** 39:06 Yes. Mhm.

**Daniela Tea** 39:25 On here if that makes sense. So the concern about like say this
particular content fragment appearing in in the in someone else's
section that is being prevented by the root path of the content fragment
folder.

**Lisa Cardia** 39:35 Yeah. So it won't show up on someone else's site, but it will still
mistakenly add that location to this site's filtering.

**Daniela Tea** 39:46 That's correct, yes.

**Lisa Cardia** 39:48 OK, so it's probably still something we want to look into, but I I
understand now.

**Daniela Tea** 39:50 Yeah, understood. OK, right.

**Lisa Cardia** 39:55 Sorry, was Scott saying something?

**Daniela Tea** 39:57 Yeah, I heard someone else. Did someone have a comment? No. OK. Umm

**Lisa Cardia** 40:04 OK.

**Scott Sorel** 40:04 Probably me just talking to myself. Sorry, I should mute myself.

**Lisa Cardia** 40:06 And then and then I my my last question, cause I can just and yeah, it
just sounds like you're sighing to be honest. The last question I'll.

**Daniela Tea** 40:07 Oh, no problem.

**Scott Sorel** 40:15 No, I'm I'm multitasking. Thanks to Luke. Got me in trouble, Luke.

40:19 My bad.

**Daniela Tea** 40:25 Sure. Mhm.

**Lisa Cardia** 40:32 Associated image. Do we have an ability to just populate A defaulted
image and then we override when there is a specific one in in use? Not
select a generic, but rather default to generic.

**Daniela Tea** 40:32 M. Default generic. So right now I don't think that is added because this
specific image. Hang on, so I'm just going to. Open this up. We're just taking a look now at the event detail page so
I can show you that specific image was all supposed to be here. But what
you're saying, Lisa, is that because of the nature of some of these
events, there would this might not need to change out for many of them.
And so you want the ability to not have to fill this out every time and
instead. The component side set like a default kind of like how we I believe we
can do that like we saw with the what was it the jobs listing component
is that correct?

**Lisa Cardia** 41:27 Yeah, it's it was just more so for convenience of author to make sure
that we're not ever running into an issue if a blank image or anything
of that nature, if they didn't select one. So there was just always
something in its place, but I can add it to the sheet and I I apologize,
I know I derailed a lot, but I thought my questions were beneficial to
most people on this call.

**Daniela Tea** 41:40 I see. Oh, it's OK.

**Lisa Cardia** 41:47 So I'll I'll let the rest of the crowd speak so you can move on with
the other event components.

**Daniela Tea** 41:52 So so just to be clear though, this content fragment cannot be like I
and I understand what you're saying about a default, but the concern
about an image not being filled out, this can't be saved unless an
image is there, just to be clear. So if there is like a default.

**Lisa Cardia** 42:07 OK.

**Daniela Tea** 42:10 Like in the DAM, if there's like a default section or image that can be
used for the time being. If the concern is that an image might not be
used, they can't save it or ublish it without an image here.

**Lisa Cardia** 42:21 OK, understood.

**Daniela Tea** 42:22 OK. All right. Let me go back to the calendar component. Let's get
ourselves situated and oriented first. Just resize this. OK. All right.
So we took a look at how these. Existing fields are mapping to the calendar portion. Now I'm going to
open up the details page that I had just shown you guys so we can see if
there's anything else on here that that we had mapped that wasn't
present on the first page. Going to Scroll down. So here we can see the description description of
test event that has now appeared here when you actually view the
specific event details page and that is that is actually it for
additional information because I left everything else blank. As I populate this, we'll publish it and then we'll refresh this to
see what happens. But going back here now, let's take a look at these
filters that we have here. As mentioned before, the region and location
filter is Yep.

**Mayte Eme** 43:28 Good question because I just got confused. What you just showed us, you
said it was a detail page, but it looked like a card. I mean it it.

**Daniela Tea** 43:36 This is this is so you can see here I have this is the page URL KT event
if I were to go to AEM which let me do that on. going to just open.

**Mayte Eme** 43:47 But is this what you're showing supposed to be the details of the event
or just another listing of events?

**Daniela Tea** 43:51 This is the details of the event. Yes, this is the details of the event.

**Mayte Eme** 43:55 Why does it look like that? Looks like a card listing.

**Daniela Tea** 44:03 They pull up. My page. So what I had done for this detail event page is I had created
a new page and we're we can do that right now actually. So this is this
is the KT event page that you can see right here and then you can see
this is the ID of the event. That I'm viewing that we had just created so.

**Mayte Eme** 44:25 OK, but why does it look like? I mean, are we supposed to? Sorry, I just
want to make sure levels are here. Are we looking at careers? Because
this is Hard Rock Life and we cannot use this for Hard Rock Life.

**Daniela Tea** 44:35 This is the way that the event details page looks.

**Mayte Eme** 44:40 How?

**Daniela Tea** 44:45 So I am just going to create a new event detail page so we can see it
from scratch. So I clicked on page and I'm going to select event page.
This is the template I'm going to hit next. And we're going to create a KT test page. Actually, I want to make sure this is meant. Yeah. Event page. Yeah, so this is just essentially the same page I'm going
to be creating here, but you can see what it looks like from scratch. So
you'll see here on this particular page what gets added is this event
detail component. Yes, because I am in the career section of this, I can copy this page
and I can put it anywhere else. And what might change a little bit is
like the color of say like the header or something. But this like I we
can do that right now. Let's go ahead and do that right now.

**Mayte Eme** 45:31 But it says careers. And.

**Daniela Tea** 45:48 I'm just gonna go to, let's go, let me go somewhere else. I'm going
to create another page and say this.

**Mayte Eme** 45:58 Let me let me ask again, are we supposed to use this for all our sites
for events or is this just a work around for career events?

**Daniela Tea** 46:08 No, this is what's being used currently for all the events. So if we if we look at say this Amsterdam event calendar. Oh, sorry, there's no events. Let me see. I think Valley has events
that are active. Hello. So if we look at this.

**Mayte Eme** 46:37 So another question then, if you can drop this into a page, we don't
have to drop this. I might as well just have an RTE and have something
that. Works. Um. OK, let's just I'll just write the questions because I'm going to
take too long trying to figure out this.

**Daniela Tea** 47:03 Yeah. Let's see here. So this is actually while we're here, while we're
looking at Valley, this is just an example. Let's take a look at this
configuration. So as mentioned before, you can see the content fragment folder path is
only going to pull in content fragments from whatever we selected here.
In this case we have pointed to the EN folder of Valley under cafes and
we've also set the event page base path, which is what I was creating
in the previous tab. Essentially this means that the event details will be loading within
this page that has been created. I'm going to hit cancel really quickly
though, so you can see here in this case there's only one region, Asia
Pacific, there's only one location Valley because I have. Pointed everything, every content fragment within the content fragment
path I had selected has value associated with it. OK. And then taking a look at the event page for here, this is how the
event details page looks with this specific event. You can see the
information is pretty similar to what we we had here, just you know,
additional text and such. But this is an example of the event pages being used with cafes as
well. Alright, I'm going to close out of some of this. Um, some of these
tabs, yeah.

**Lisa Cardia** 48:35 Question on the the event detail page I believe it is. I'm trying to
see where I had my note. My question is the URLs that you pointed out.
So a lot of our events end up needing like a clean URL so that they're
shared for.

**Daniela Tea** 48:41 Yes, yes. Mhm.

**Lisa Cardia** 48:55 Like promotional purposes, so advertisements, radio. So it'll be very
clear to say property.com slash Kid Rock slash what have you. Will that
work instead of like numbers 1234.

**Daniela Tea** 49:08 Hey. I see. So, um, one second. Yeah. So in terms of your, it sounds like
you're talking about like a like some sort of vanity URL. Does that
sound accurate?

**Mayte Eme** 49:22 No, no, no, not vanity. Right now in all our sites when we create an
event and we have a detail page, the detail page has the name of the
artist of the show, whatever the contract tells us to put. So these
numbers, that's what this is asking. This is just.

**Daniela Tea** 49:28 Hmm.

**Mayte Eme** 49:39 I don't know. In the works or a bug, we're gonna have real names,
right?

**Daniela Tea** 49:43 No. So this is where I was saying right now the event ID it gets auto
generated. This is to prevent. This was previously added to prevent
duplicates. It sounds like what is needed is as a enhancement to this. Being having the ability to change it, so making this not read only and
then being able to change the ID so it's something that's a little bit
more user-friendly.

**Mayte Eme** 50:09 I don't. I don't think we expect content authors to be changing. Can
you just pick up the name of the page that we're creating, like
WordPress or site coders?

**Daniela Tea** 50:23 So so when you say creating the page, keep in mind this is one
individual page I have created. This page is going to be used for every
event based off of the ID. So what I so I'd say like let's say this
is.

**Mayte Eme** 50:32 But.

**Daniela Tea** 50:38 The event, right? So in the future what I'm saying is this is something
that I could see happening where the event ID instead of being the
numbers, you would want it to be say like the name of the event. Is that
correct?

**Mayte Eme** 50:52 Yes, but not that way. I think we need to identify it as a gap because
the way this is working, it's very labor intensive and not you know
with a smart CMS that can you just create event and it just populates
everywhere that we have it now. Um. So let's just add it to the list for when we launch any other side and
careers. We'll figure out what to do with careers because that this
digital page is not working for careers for the events.

**Daniela Tea** 51:25 OK, uh.

**Edwin Aquino** 51:27 Question, Daniela, with these event detail pages, the homepage hero that
we have there, is that a standard hero across all of the event details
pages or is that something we can customize per page?

**Daniela Tea** 51:28 Yes. What? Let me confirm. We're talking about this portion right here. Yes. So if
I were to go back to, sorry, I lost the page. If I were to go back to
this event detail page in the author, I'm gonna do that right now.

**Edwin Aquino** 51:41 Correct, yes.

**Daniela Tea** 51:54 Sure, OK. Uh, So what I had done here is I can set. In the event detail page I can set a default hero banner, but I can also
override it with that banner image and alt text field here within the
content fragment. So an yeah, so an example of that.

**Edwin Aquino** 52:15 Perfect. OK.

**Daniela Tea** 52:18 And sorry guys, we're jumping around. I'm just trying to find my tabs.
An example of that. Let me take a look. I think this one I set something
differently. No, was it this one? One of these? One of these I set
differently. But basically as long as you put, yeah, this one you can
see I set differently. If you put something within the content fragment, it will override it.
If you leave it blank, it will just inherit essentially whatever you had
put in the event detail page when you set up this page. Does that does
that answer the question?

**Edwin Aquino** 52:47 Yeah, that answers it. Thank you.

**Daniela Tea** 52:49 OK, perfect. Yeah, so let's actually take a look at this component.
I'm going to go back to the empty page I had just created, which is
right here. So by default what you'll see is the event page title. We
have a pre-populated text of Hard Rock live event counter that can
certainly be changed. Changed and configured the description, title, event details, the
default hero banner image which can be selected based off whatever you
want to show for anything that doesn't have a banner and then an error
message if say there's no events or something happens and you can put
an error message here to be displayed. So this is what is here the moment you create the page and then of
course the author can change out as needed. But the process of this is
that you create one event page and then the as of right now what happens
is that the content fragment details will populate this page. By passing in the specific ID. And then I'm filling in the rest of the information on the page. I will pause here to see if there's any questions about this event
detail component which is being used on the event page template.

**Mayte Eme** 54:11 I got so many questions. I'll I'll put them in confluence. I'll I'll
try to regroup, probably rewatch this and make sure I don't bombard you
with too many questions. I know it is what it is. So just let us digest
this and if we even, you know, need to use this or come up with.

**Daniela Tea** 54:26 Yeah, understood.

**Mayte Eme** 54:30 Something else, because it's just, you know, not what we need.

**Daniela Tea** 54:35 All right, so now what I'm going to do is I want to actually show. You
can see here this has a couple of other things filled out that we did
not see previously on my other details page, and that's because I
filled out more fields on this specific content fragment. So I'm
actually going to pull up this content fragment. So we can see what was filled out for those to appear. So this one, Saint Patrick's Day. So you'll notice again, just to
highlight, I had put this in 03 because as I was testing I wanted this
to be Saint Patrick's Day, which is obviously not in February. However,
I changed the date. In the content fragment itself, the way that the calendar works is it's
going to be basing it off of what you put in the start date. So again,
no bearing off the folder structure. This was just for ease of authoring
use for organization.

**Mayte Eme** 55:32 I quick question, I don't see time zone. So is is that a site setting
or we still don't have that?

**Daniela Tea** 55:32 OK, I'm going to, yes. So time zone wise, I was discussing this with our TA this morning and
let me check my notes. You do not set a time zone here. This is based
off of the user time. So viewed on the browser February 20th, 3:00,
that's.

**Mayte Eme** 55:56 Mhm. Wait based on the user.

**Daniela Tea** 56:01 I'm sorry, what was that?

**Mayte Eme** 56:04 Based on the the the event time is based on the property, not the user.

**Daniela Tea** 56:09 No, as in this visibility is determined based off of the user's time
zone. As in if I see this like because this there's no time zone
associated with this February 20th, 2026, 3:00 PM for Eastern Time. Is obviously different from say like India or California and it's
visible based off of the local time is my understanding.

**Mayte Eme** 56:33 No, that's not what we have to do by country. We have to put the time
zone of the location. So if I'm in China, I still see 8:00 PM Eastern
Time because the event is in Miami.

**Daniela Tea** 56:34 Yeah. Yeah, so let's get that into our Confluence page. I will talk to our TA
to get a get something that's document on there to hopefully be able to
explain a little bit better with some examples. So we'll note that one for something for follow up within our
Confluence page. OK.

**Lisa Cardia** 57:08 I think the only thing that unless I'm sorry when I was taking notes,
missed it was the tags again. It's something that we kind of always
skim over that that's just for internal purposes and for like Don's
organization. Not the categories tags.

**Daniela Tea** 57:23 So like, oh, oh, sorry, the tag you're talking about like right here.
Yeah, these tags are not. Yeah, these tags are not, um, uh, being used
within the calendars. And like, like you're saying, Lisa, you could
certainly add tags for organization purposes, but.

**Lisa Cardia** 57:28 Yeah.

**Daniela Tea** 57:40 The calendar is not dependent on the tags that are added.

**Lisa Cardia** 57:44 So tags are is like an internal use.

**Daniela Tea** 57:47 Correct. In this case, yes. The categories though, which are tags, as
you know, are dependent on to fill up the filter. Yep.

**Lisa Cardia** 57:49 OK. Right. Confusing to say tags twice, but tags is typically internal
category tags. It's meant for the filtering in the cards. Thank you.

**Daniela Tea** 58:02 That is correct. Yes. Yes. Yeah. OK. So let's take a look at this here.
So some slight differences that you'll see here is this, for example,
this sold out status. That is based off the offense status and I I again, Lisa, I understand
what you're asked was here. In this case I have one selected for sold
out and so it's being displayed. So this will not change out unless I
were to change it again. We also see the event status message. This is sold out. That appears
here.

**Mayte Eme** 58:36 Can we go over the statuses? Are those all manual or can we actually
schedule the pre sale, the announcement, the rescheduled?

**Daniela Tea** 58:46 Yeah. So this was the discussion that we were having earlier. Currently
it is going to be manual what you select, but the understanding that I
heard which will be discussed and covered more in the gap is that it
sounds like each one of these statuses needs to have a specific like
time frame associated with it. So that we would change without an author
having to.

**Mayte Eme** 58:50 Oh.

**Daniela Tea** 59:06 Manually come into the content fragment and republish.

**Mayte Eme** 59:09 Not all of them, because we don't know when it's sold out right until
they tell us or cancelled or postponed. But it's more than that. I
mean, they actually drive and hide different content. So is it doing
that? I guess we just want to understand right now what it does. Like if I
choose preset, does it hide the CTA? Does it change it? Does it add the
description that we usually have or the code or is just a little flag on
the corner?

**Daniela Tea** 59:37 So right now, if I were to click on a presale, let's save this and
again, I'm going to republish to have those changes visible. I'm just
republishing it and then I'm going to refresh my event detail page. You
can see that the presale. Flag has changed, so that's what the event status does. Yeah, that's
because because what I did was, you know, let me open that back up
again. I didn't change out my event status message. So this is separate
from whatever the event status is.

**Mayte Eme** 59:57 It is. So you have to do all the money. Okay.

**Daniela Tea** 1:00:18 See.

**Lisa Cardia** 1:00:19 I actually had a question just about what the process you just showed
about like publishing to see those changes. So if we're a content
author and we're making changes and we accidentally selected the wrong
label or something and we needed to see it, we would have to make it
published in order.

**Daniela Tea** 1:00:24 Yes. So let's so I've just, yeah.

**Lisa Cardia** 1:00:41 And then we needed to change before we go ahead and publish. We didn't
push something wrong.

**Daniela Tea** 1:00:47 Yeah, no, understood. So yeah, let's let's let's demonstrate how that
works currently. So you can see I've like updated the title. I changed
this to cancel. I hit save. I did not hit publish. So viewing the view
as published side, you can see how I've refreshed it and it hasn't
reflected those changes. So I would not be able to see those changes until I actually published
it.

**Lisa Cardia** 1:01:12 Even just internal to yourself.

**Mayte Eme** 1:01:15 So how do we preview to make sure it's looking right? Because there's
so many manual steps we need to see it before we publish because we
might publish the wrong thing.

**Daniela Tea** 1:01:28 Oh, so let's see here. So.

**Mayte Eme** 1:01:33 And not to mention, we probably have to like export it as a PDF to send
it to somebody. If it's a big one, then it's approval because we still
don't have the preview links, so we got to come up with a process to
get approvals.

**Daniela Tea** 1:01:48 Uhuh. And I and I think in terms of because I believe that was a question that
we saw and also I think we're also going to we answered it, but I think
we also want to cover that during the gap analysis portion, the preview
server and the preview links. But for this section right here currently
the way it works is that.

**Mayte Eme** 1:02:01 Yeah.

**Daniela Tea** 1:02:09 You would not see the changes until you publish the content fragment.
However, keep in mind I have not actually published the page.

**Mayte Eme** 1:02:22 But if we need to send something for approval and we need to send the
whole page.

**Daniela Tea** 1:02:22 Right. So what I'm saying though is the so the previous server is something
that's completely separate. That's something.

**Mayte Eme** 1:02:30 We. No, right, right, right. I'm just saying like we gotta come up with a
process, right? So right now the process is doing a full page screenshot
and send it in as a JPEG or a PDF. So how do we get that? If we have to publish and go live to see a full page and there's no
internal review when I'm logged in into AM.

**Lucas Nelson** 1:02:55 Andy, are you aware of any export ability that that AEM has
out-of-the-box just by chance?

**Andy Lambert** 1:03:03 For exporting.

**Lucas Nelson** 1:03:05 Like this page to a PDF, like the entire page, the the use cases
they're trying to figure out a process while other things in the gap
analysis will be in flight to be able to send these pages as previews to
like vendor partners or.

**Mayte Eme** 1:03:09 Me.

**Andy Lambert** 1:03:17 Mhm.

**Lucas Nelson** 1:03:22 Whoever their other stakeholders are before they actually, uh, publish
changes on a public site. Just curious if you've had that use case
before with exporting.

**Andy Lambert** 1:03:28 Let me. No, not a specific ask for like a screenshot almost, but let me take a
look and see what the latest and greatest is on cloud services and see
if there's something that's available. We'll come back to you.

**Mayte Eme** 1:03:45 And to be to be fair, I mean we can just do plug in Chrome or whatever
and screenshot the whole page, right? And it saves as a JPEG or a PDF.
So not asking for an export feature, but a way to at least preview in
the browser so we can do our screenshots.

**Andy Lambert** 1:03:54 Mhm.

**Lucas Nelson** 1:04:03 So a browser preview and and and.

**Mayte Eme** 1:04:05 No.

**Andy Lambert** 1:04:05 Wouldn't that be from using just view as published or using your
preview tier? So you have in in cloud services you've got in addition
to your dev QA stage prod. For each of those environments there is a
preview tier that you guys I don't think are using right now.

**Mayte Eme** 1:04:11 Yes.

**Andy Lambert** 1:04:22 Um, that might serve that purpose where it's only visible to you.

**Mayte Eme** 1:04:22 Hmm.

**Lucas Nelson** 1:04:27 Yep, Andy, the problem. It's not configured yet.

**Mayte Eme** 1:04:29 OK, but is there a preview like what Danielle is showing right now?
Let's say we wanted to send this page that she has right now. At least
we can see the page. We can say ignore the toolbar on the top like
something to see the page, but it seems like for the event detail pages
that doesn't exist at all.

**Andy Lambert** 1:04:30 Um.

**Daniela Tea** 1:04:45 So sorry, let me you're asking, sorry, I'm trying to make sure I
understand the question because I made changes here, right? And you're
like, how do I get those changes to be seen here without having this go
out to the public? So that way they aren't seeing a bunch of.

**Mayte Eme** 1:04:47 I Yes. Yes.

**Daniela Tea** 1:05:03 You know, junk. Um, So let me actually pull up this page in the
publisher. Alright, one second.

**Mayte Eme** 1:05:06 Yeah. OK.

**Daniela Tea** 1:05:12 OK, one second. One second. Um. What is this called? QT Calendar, I think. OK, so right now we're
reviewing this in the publisher and I'm going to click on more info to
open up my details. Oops. Oh, I don't think I I don't think I I I
didn't publish this, did I? One second. Yeah, so let me let me publish this version. And publish this version first. OK. Let's publish. Let me also double check to see what the event details
are for this. So right now, uh, OK, it's cause I was, I was messing around. I was
messing around with that link. OK, I'm actually going to save this one
and I'm going to publish this one. Alright, So what I was just doing
was I was changing one of my destination links. I was. I put something else there as I was setting U this page. I
didn't intend for that to happen. So now if I were to go back to our. Publisher link, which I'm going to pull up again. Last KT calendar. See here and let's go back. Let's look at the author version of this
page as well to see what differences that there are. OK, so right now
you'll see I didn't publish this page, I didn't publish KT calendar,
and so I'm able to see this here, right?

**Mayte Eme** 1:06:59 OK.

**Daniela Tea** 1:07:02 I'm able to see more info. I did publish the content fragment, but I
did not publish the page. Makes sense. Like that's why you're not
seeing any of the changes I made where I removed the button or I added
all you know this junk at the end of this title. So the.

**Mayte Eme** 1:07:03 OK. OK. But what are and can you do the same with the?

**Daniela Tea** 1:07:18 Yeah, go ahead.

**Mayte Eme** 1:07:22 Thing that detail page that looks like a card the.

**Daniela Tea** 1:07:26 Oh, so hang on, let's see. Let me confirm what you're asking. So as I
clicked on more info, this is the detail page so I can see the changes
that I made. You're asking for if you can see that here as well. I did
change the destination link for this. One second, I'm actually going to
open up this one.

**Mayte Eme** 1:07:31 So. Yeah, that one.

**Daniela Tea** 1:07:45 I don't think, oh, I never publish. Don't think I published my detail
page from the publisher side. Mayte, one second. And sorry guys for jumping around. I'm just trying to find it in my
section here. Did I ever publish this page? Yeah, so you can see.

**Lisa Cardia** 1:08:01 But this is helpful to know too. Do we have to publish all three, the
fragment, the detail page and the event calendar every time a new
event's added? This is just important for other authors that are going
to be adding to their event calendars.

**Daniela Tea** 1:08:09 So. Yeah, so keep in mind that again, this event page is just one page,
right? So you would only have to publish it once, but I never publish
this. That's why none of these links here in my calendar on the
publisher side are going to work because I never published the KT event
page, right? O hoefully that makes sense. So now what I'm going to do instead is
I'm going to publish my KT event page. On the publisher side, if I were to refresh this, let's see if that has
gone through. So now you can see here the event detail page works and
it's showing information, whereas previously it wasn't because that
page had never been published. But even when I refresh this and I go back to the author side, you can
see there is there is differences. My taste question was if I were to
view this here, let's see what it looks like. OK, so because I
published the page and it probably published a content from again.

**Mayte Eme** 1:09:15 Mhm.

**Daniela Tea** 1:09:22 Let's do this exercise one more time. What I'm going to do is I'm
going to make another edit to the content fragment. Um, just to see, uh,
you know, like what's being displayed here. So one second. Let's go back to my St. Patrick's Day content fragment.

**Mayte Eme** 1:09:39 I am so gonna have to watch this again. There's so many steps.

**Daniela Tea** 1:09:42 Well, this the reason why is because I'd never published a page.
That's why there are some inconsistencies. But one second. OK, so I hit
save and I hit close and let me hit publish and let's see what
happens. So I had published. So this should now say testing. Let's see what it says over here. It
still does not reflect because I never republished the KT calendar page.
If I were to refresh this, you can see here it does not show the new
change of testing. Because I did. I I did not republish. Let's see. Hang on. I didn't.
Wait, hang on. Yeah, so I republished the content fragment, but I did
not republish the event page here.

**Mayte Eme** 1:10:33 To. So when we have the 100 of events, is that how long is it quick right?
Because if we got to republish every time there's a new event or a
change the whole page, does that cause any issues or delays or? And I'm sorry, but going through cycle, like cycle would give us a lot
of issues, right? If we were published the whole event page, that's why
I'm wondering.

**Daniela Tea** 1:10:53 So can you? Yeah. Yeah. Can you repeat the question please, Mayte?

**Mayte Eme** 1:11:02 Yeah, um, when you said you have to publish the event page right for it
to show.

**Daniela Tea** 1:11:10 When I yeah, when I first created this, I had never published it. And so
now this is published. So you can see it was published 3 minutes ago.
OK, sorry, continue.

**Mayte Eme** 1:11:23 Yeah, so um. Maybe you just answered the question. So you don't have to publish that
event page every time a new event is added. It was just that one time
because you didn't publish it.

**Daniela Tea** 1:11:35 That is correct. Yes, I did not have. Yeah, yeah. So like now now if I
were to look at these, like previously these links would not have
worked. Well, the Google one would have worked, but these links would
have worked because that KT event page had never been published. But now
if I were to open it, it should display the content.

**Mayte Eme** 1:11:36 OK, OK, OK, OK.

**Daniela Tea** 1:11:55 Because I published the page. Hopefully that makes sense. And again, Maishi, totally understand. If
you have some additional questions, we can certainly review them also in
Confluence.

**Mayte Eme** 1:12:06 OK, yeah, yeah, that'd be good.

**Lisa Cardia** 1:12:07 So what do things always need to be published? The the fragment and what
else?

**Daniela Tea** 1:12:10 So. Okay, So let's let's do this. I've created a calendar page. I can create a let's create a brand new
calendar page, a brand new event detail page, and then also just, you
know, referencing some content fragments. OK, let's do that.

**Lisa Cardia** 1:12:31 OK, cause like likely the event calendars, my assumption are already
pre-built for properties basically and they're just responsible for the
new events. So if I'm that property and I'm creating the new event, I
just want to make sure I'm publishing all of the right things that need
to be included in the publishing. So that's.

**Daniela Tea** 1:12:36 Yes. Yeah, understood.

**Lisa Cardia** 1:12:49 The fragment.

**Daniela Tea** 1:12:51 OK, so if I were to make some changes, let me add a new content fragment
very quickly with some bare minimum content. Uh, start date. Let's do March. Start time just random. Uh. Going to select my image. So this seems like typically what a content author would do. Correct me
if I'm wrong, Lisa, they right now would be creating an event
specifically for their property, right? So like this, this seems to be
in line with like what a content author would typically do. So I thought
on my image my description. And I'm not going to fill this out, but I will just add a location and
I and in this case I'm just going to choose something here. OK,
alright, so this is the bare minimum right now. And you can see here I've created this within the Ballyen folder just
like the other ones. So if I hit save. And I hit close. Right now we can examine that this particular content
fragment has not been published. So the expectation is that when I view
this calendar, I should not see it on here. So it was a March event. You can see March is not even available once I
published this particular content fragment. Just sorry. Click on this and then I am. Where is my publish button? Uh. Uh. It's this one right? Should be the there we go. OK, so previously you
might have seen that the the ribbon here didn't have my specific tool
quick published, but after I refreshed it and yes it did pop up. So if
that just something to keep note as a content, I'm sorry as a. As an author, depending on how fast you do things, sometimes it might
not appear like right away, but if you refresh the page you will see it.
So I'm going to hit quick publish. Publishing that. So now this is a published content fragment. We can say
I published it a few seconds ago. If I refresh this page here in author,
the expectation is that you will see it appear here now. So I click
March 2026 and you can see that specific fragment is here.

**Lisa Cardia** 1:16:06 OK.

**Daniela Tea** 1:16:07 Now let's go to the same page that was in the publisher's server. So
this is my KT calendar. Let's click refresh on here. So you'll see
that there is no March 2026 event that appeared here. Right. If I publish the calendar page, right? So I'm going to republish
this calendar page. So I've hit publish. There's been published. Um, let me see. OK, so I've hit publish and you'll see my Saint Patrick's Day testing
thing came in and also let's see what else. All right, second this and this I think is what Gonzalo was referring to
in terms of how quickly will we be able to see the changes and so this
is something certainly that we would want to. Confirm. But as we will continue to check this page, the expectation is
that after you publish this page here you the event calendar page, you
should be able to see the same changes like the way that it's that
you're interacting with it here where you see that the filter had been
updated and that new test.

**Lisa Cardia** 1:17:15 Which is the event calendar.

**Daniela Tea** 1:17:27 I created is here after publishing that that should be available then on
the site, but I think it could potentially be a couple minutes and as
Gonzalo mentioned, this is something we certainly want to monitor, but
that is the expected behavior, Lisa. So what I had outlined was.

**Lisa Cardia** 1:17:34 OK.

**Daniela Tea** 1:17:46 Pushing that content fragment and then I also published that calendar
page.

**Mayte Eme** 1:17:51 Yeah.

**Lucas Nelson** 1:17:52 Daniella, can you drop the link that you have the page you published and
it it. Yeah. And then we we can take that in the background for Andy and
Vinay. Thank you. Yeah.

**Daniela Tea** 1:17:54 Oh. Oh, yes. Sure. Yeah. No, thank you. Yeah, that's cool. Yes.

**Lisa Cardia** 1:18:03 And then Daniela, two questions. One's going to be related to careers
and one is going to be related to events in general. We we announce
events sometimes and then get notified from the property. Take it down,
take it down. Artist changed announcement to Friday.

**Daniela Tea** 1:18:12 Sure.

**Lisa Cardia** 1:18:19 So what does that look like to unpublish but not delete? Because we will
use that content fragment, just unpublish and then repurpose it for the
time that's necessary.

**Daniela Tea** 1:18:20 Mhm.

**Mayte Eme** 1:18:33 Yeah, kind kind of like hiding the the card and the detail page so
nobody gets to it.

**Daniela Tea** 1:18:33 So. OK, so let me make sure I understand. Let's take this for example.
Let's pretend Saint Patrick's Day has been canceled and we don't want
it to be displayed.

**Lisa Cardia** 1:18:46 Mhm.

**Mayte Eme** 1:18:46 Not, not canceled. We just got told to pull it down for a few days.

**Lisa Cardia** 1:18:51 And we'll announce it later in the week, yeah.

**Daniela Tea** 1:18:53 OK, so the question is how do I get like what do I what would I do in
order for this to not be live on the site? Is that correct?

**Mayte Eme** 1:19:01 Correct.

**Daniela Tea** 1:19:02 OK.

**Lisa Cardia** 1:19:02 But without deleting it, because we will put it back up Friday.

**Mayte Eme** 1:19:06 Yes.

**Daniela Tea** 1:19:07 OK, alright, so let's go ahead and unpublish Saint Patrick's Day. So this is saying OK are you what do you want to unpublish? OK, I want
to unpublish my event. I don't have to select this, but some in some instances. The reason
I'm just highlighting this is that you will see additional references
where you get to pick and choose what you want to be updated and so just
want to make sure that you guys are aware that in this case there's
only one so it doesn't matter as much, but that's why this is a multi
select. Then I hit unpublish. So it's referenced by three items. Yep, got it.
So I have hit continue and So what that should do. Let's see because
we're still waiting for this to. Um, operate, I think. Yeah, so you can see here in this instance, right? That event has been
removed from the calendar and like you can't see an author because I
unpublished it. Does that make sense?

**Mayte Eme** 1:20:11 What about the? Yeah, what about the detail page? Is that a published
too?

**Daniela Tea** 1:20:16 So the detail page, I guess what you guys are saying is that in this
case here like the URL, I'm gonna take it from the publisher. You're
asking if like this here like would this still be something that they
can access if they have like the specific?

**Mayte Eme** 1:20:26 Yeah. Yes, when we pull it down, we'll pull it out from everywhere.

**Daniela Tea** 1:20:37 I see. Um, let's see here. Oh man, I don't have the ID for it. I I
would need to check the ID, but we can chest. Let's I what I'll be
doing is, yeah.

**Lisa Cardia** 1:20:47 I just want to make sure that the same pages that we're publishing, do
they need to? Do we need to take precaution on extra steps to unpublish
something so that we don't miss everywhere that it it got associated
to?

**Daniela Tea** 1:21:00 Yeah, no, I understand. With regards though to that event detail page,
again keep in mind because it is only one page, you would not be
unpublishing that specifically for the event. However, what I do want to
check once we can see the changes here on the live site, I'm sorry on
the stage website is. If I can still access the previous URL that was stored here, like since
it's removed from here, I I understand that a user if they still had it
stored as like a favorite or something, we want to check to see if
that's accessible, but they would not access it from the event calendar
because it would not be visible in the event calendar.

**Lisa Cardia** 1:21:39 Upon a media unpublished of the fragment.

**Daniela Tea** 1:21:41 Right. So what's we've we've taken this page so we're going to be
investigating this one and that's also going to be something that I'll
be testing. I have the URL currently for this with the ID once this
because we unpublish this. Once this is unpublished and visible as
unpublished on this page, we'll also be accessing. the specific link here to see if it's going to pull up a 404 or if it
still displays the details. So that's something that we will have to
take offline, but I can also report back tomorrow once we get that
looked at. Hi.

**Lucas Nelson** 1:22:18 Sounds good, Danielle. Yeah, we're sleuth in the publishing queue Part
2, so we might have follow up on that tomorrow.

**Daniela Tea** 1:22:23 Yeah. Yes, I believe we will. Yeah. Um, OK.

**Mayte Eme** 1:22:29 So just to recap maybe for for a second to understand how these events
that you have built worked, we can unpublish them and you're going to
confirm the detail page. We can publish them on a specific date and
time, but it's not local to the property. And they will drop off on the I I think I saw an end date right on time.
So they will automatically drop off without any action from our part and
all the event statuses are manual.

**Daniela Tea** 1:23:02 Oh.

**Mayte Eme** 1:23:02 We cannot override dates, we cannot override location because we usually
don't put the address, we put the actual venue, whether it's a career
event or whatever event we.

**Daniela Tea** 1:23:15 Mhm.

**Mayte Eme** 1:23:18 Cannot do a status as a scheduling. What else am I missing? Lisa, we
have to do it like in three times instead of one. Like in Cycord we and
that's pretty much right all the capabilities.

**Daniela Tea** 1:23:32 So.

**Lisa Cardia** 1:23:32 Uh yeah, I probably have other notes on my end that I could add to the
list.

**Daniela Tea** 1:23:37 Yeah, yeah. So one thing I did want to want to point out, let's see
here. And I know that this is, I just want to be clear that the hiring
events that are listed here, we are not currently using. I think like this is like what you're what you're talking about,
right, Maite? So you'll see here, yeah.

**Lisa Cardia** 1:24:02 Well, so if these are, what are these using if they're not using the
events?

**Daniela Tea** 1:24:06 Sorry, no, no, they so sorry. Apologies. I what I meant to say is they
are using the events content fragment. Wait, hold on. Where did it go?
One second.

**Mayte Eme** 1:24:08 And I.

**Daniela Tea** 1:24:21 One second. OK, here we go. All right, let's take a look at this very
quickly and I can see the time. So I I know that we also want to cover.

Gonzalo Calasich (SHRSS)** 1:24:28 Those are the promotion Uh content fragment model.

**Daniela Tea** 1:24:31 Yeah, that's what I wanted to point out that this is, this is what I
believe Mayte is expecting. Is that correct?

**Mayte Eme** 1:24:38 Yeah, but Amazon.

**Daniela Tea** 1:24:39 In terms of the over, in terms of the overriding, like that's what you
were describing.

**Mayte Eme** 1:24:44 Yeah, we can do that for any of our cards.

**Daniela Tea** 1:24:48 Right. So here we have and I believe, yeah, I know Gonzalez, I think you
you had made some edits and such, but let's just pull up one of these.
So yeah, this is a a different content fragment model. This is using the
promotions content fragment model. The reason why we chose to use the
promotion. Content fragment model was because we we saw the examples where this was
something that was overwritten. That's and that feature and capability
is here with date override text and location override text.

**Lucas Nelson** 1:25:13 Mhm.

**Mayte Eme** 1:25:14 OK. But we need that for. So in the event ones we don't have that and we
also don't have venues. I'm just trying to understand if we can actually use that. Um.

**Daniela Tea** 1:25:31 We don't. So.

**Mayte Eme** 1:25:45 Oh. Sorry, my connection was weird, but is there a way we how do we
understand exactly what these cards can do?

**Daniela Tea** 1:25:54 So keep in mind what we went over today is specifically for the events
content fragment model using the event calendar component and the event
details component. What we're seeing here, I I the reason why I was
calling this out is because yes, I know this is hiring events. In order
for us to make these cards, we use the promotions.

**Mayte Eme** 1:25:55 To.

**Daniela Tea** 1:26:14 Content fragment model since that seemed to be more in line with the
fields that were listed here versus using the event content fragment
model. Does that make sense?

**Mayte Eme** 1:26:25 Yeah, it makes sense. But I mean, it's still lacking, you know,
functionality and we we have to address that in in in the gap assessment
that we're going to do. But I was asking more about the events, right?
What is it that we can and cannot do to see if we can even use them?

**Daniela Tea** 1:26:30 Mhm. Yes. Um.

**Lucas Nelson** 1:26:45 Danielle, is there anything else on events that you haven't covered to
show what we have currently implemented?

**Mayte Eme** 1:26:47 Is.

**Daniela Tea** 1:26:52 Um.

**Lisa Cardia** 1:26:53 Also, to be clear, so we're not using events on careers. Sorry, I was
just confused because I thought today was careers focused.

**Mayte Eme** 1:27:00 Yeah.

**Daniela Tea** 1:27:01 No, no. So today was events focused and we wanted to cover everything
related to events. I wanted to call this out though, because this is
actually using a completely different content fragment model. I know the
title says hiring events, but this is not using the event content
fragment model that's using promotions.

**Mayte Eme** 1:27:05 Um. OK, so oh, I thought we were continuing with careers because they were. OK. So we'll just Add all the other questions from careers so we can
wrap that up. And if today was about events, so much so, OK, we'll just
write down our questions.

**Lucas Nelson** 1:27:44 We tried to flash the agenda yesterday. I don't, you know, I'm sure
there's a you're taking it from a fire hose, everybody. But yeah, we
we we flashed it. We were gonna review events.

**Mayte Eme** 1:27:51 Yeah.

**Lucas Nelson** 1:27:56 So yeah, my take, you know, if there's more questions on careers, uh,
we, we, we, we wanna make sure they're captured, yeah.

**Daniela Tea** 1:27:59 I.

**Mayte Eme** 1:28:01 Yeah.

**Daniela Tea** 1:28:01 So actually, Luke, this actually rolls in quite nicely because I think,
you know, yesterday we were kind of doing a retrospective. And So what
I'm hearing from the team is definitely understand the desire to
actually go over more things that are related to careers. Previously, when we had planned out how these sessions would go and
examine what topics were being tracked within JIRA, we were trying to
group things into essentially like, you know, big overview topics like
everything events related. I mean the content fragment and the related
components.

**Mayte Eme** 1:28:18 Mhm.

**Daniela Tea** 1:28:35 However, definitely understand that it sounds like careers is the
desired focus, so we can potentially pivot tomorrow to look at some
additional careers specific components. I believe one of the questions
was like for example the video testimonials. And the fact that here we're using the promotions template, how does
that work in relation to this hiring events section? So what I'm saying
is I can write up a modified agenda to go over some of those different
topics. We can go so it's more career focused versus. Some of the things we had initially planned, if that sounds good with
everyone.

**Lucas Nelson** 1:29:13 Hey, hey, once. Yeah, one second. Daniela, can you pull up the
confluence with the agendas that we sent out last week?

**Mayte Eme** 1:29:14 Yes, but it's big.

**Daniela Tea** 1:29:19 Mhm. Yes, one second. Here we go. Yeah, OK.

**Lucas Nelson** 1:29:28 And I'm not, I'm not pushing back. I'm just, I just want to make sure
I'm I have an understanding. So you were initially going to do news
tomorrow and then locations, but we're talking about pulling in. Tell
me again what you're pulling up forward.

**Daniela Tea** 1:29:42 Taking a look at the careers website and identifying any additional
components like that we had planned for outside of these sessions, we
were trying to cover the content fragment related components first since
this do take a while. So to be clear then there will be a different
agenda.

**Lucas Nelson** 1:29:56 Right. Yeah.

**Daniela Tea** 1:30:02 I'll try to get that prepared after this call and it will be covering
some of the items that we can find on the careers website.

**Mayte Eme** 1:30:11 Oh, question. When you say careers, job sessions one and two, we assume
that's yesterday and today, session one and two. So if we are doing
session three instead of two, can you just let us know when we're
changing that? Because our mindset was on our careers, so we're looking
at events. Trying to figure out how on earth we use this for career events, and it
turns out it was for everything else, not careers that is used in
promotionals.

**Lucas Nelson** 1:30:36 Yeah. My my it was tough to norm on the number of session topics to blocks of
time because they're two hour blocks of time. So So what what our
intention was when when we list out the four bullet points because
we're having four blocks of time, we were covering 2 session topics per
block.

**Mayte Eme** 1:30:44 Mhm. OK, that's no problem.

**Lucas Nelson** 1:30:58 So yesterday we did jobs one and two, today we did events two and or
three and four and and so on and so forth. So that that that's the
intention that that there there's going to be two hour blocks of time
and we were able to try to scope and plan. The the I don't know Danielle was at 42 session topics into those those
planned sessions blocks of time. So I just want to be clear on that if
we were I know that norming is is is a little wonky but that that was
the best we could do given the two block 2 hour blocks of time that we.

**Mayte Eme** 1:31:22 OK.

**Lucas Nelson** 1:31:30 Had already aligned with Scott that you guys had, you know, were
committing to be available. So just Danielle, did I explain that right?

**Mayte Eme** 1:31:35 OK. No, thank you for explaining, Luke. That helps. Good to know because
we didn't know. So, but we are not done with careers. So if you tell
us, hey, go manage that site, we can't. So we'll add the rest of
questions we were holding on thinking today was session two.

**Daniela Tea** 1:31:37 Yeah, I think so.

**Mayte Eme** 1:31:55 Add them to Confluence and we need to revisit that because that's the
site that we got to go live right due to the Workday crazy timeline. So
we got to be prepared to support that. We already have issues with Hard
Rock and Reverb. We don't want to add more to with careers.

**Lucas Nelson** 1:31:58 Yeah, I. Yeah. So Maite, I, you know, hear you, but but here here I I just want to make
sure it it's clear the careers site, we're cross-pollinating topics of
there's a careers work stream and I'm giving it to you from the Adobe
point of view. There there's a careers work stream, there's a
knowledge transfer work stream.

**Mayte Eme** 1:32:26 Mhm.

**Lucas Nelson** 1:32:30 This focus that we have right now with these knowledge transfer sessions
is knowledge transfer across the the components and and the master topic
list that we had. We pulled those master topic lists that they were kind
of agnostic to whatever careers work stream that you guys had. Committed to and and that now the onshore team and Adobe are pulled in
and are supporting start starting to get into the game supporting the
careers work stream. But I to I, you know I say it a lot just want to be
clear like this is knowledge transfer across. Those master topic list and what we've implemented in in your instance
of a EM, we are pivoting and trying to accommodate with with the
knowledge transfer schedule, you know careers focused components from
from the framework.

**Mayte Eme** 1:33:24 Mhm.

**Lucas Nelson** 1:33:25 So hear you loud and clear there. I'm not disagreeing with you that
it's it's of importance, but we still have to be mindful and
specifically me and Scott that we're sticking to the plan and not
falling behind and and and not, you know, finding that we need more
sessions than what we had scope and planned for.

**Mayte Eme** 1:33:30 Hmm.

**Lucas Nelson** 1:33:44 On the schedule for knowledge transfer. So yeah, so we're doing a best
effort to to support that mighty.

**Mayte Eme** 1:33:47 So it's called maybe. Right. And I appreciate that. Look, I do, I do. It's just that clock is
ticking. So can you guys maybe figure it out how we look at the
components used in careers first instead of going through events that we
are not using?

**Lucas Nelson** 1:34:02 That's what Daniella was just saying to you, yeah. Yeah, that's what Daniella was just saying to you. Yeah. So we what
what what we're doing is reacting to that, that ask and and
understanding the careers timeline that we're under and Danielle is
going to try to make a modified agenda is what she just said, yeah.

**Mayte Eme** 1:34:12 Mhm. Okay, thank you for that.

**Lucas Nelson** 1:34:22 Yeah, no problem. Danielle, did I did I over commit you for something or
is that good?

**Daniela Tea** 1:34:23 Oh. No, that that's exactly what I said. But sorry, I just wanted to make
sure before before we got into more retrospective that I was checking
the stage site again. This is that page that we're looking at. You can
see that the unpublished content fragment, that Saint Patrick's when
it's no longer visible on the live site. And then also that new content for everybody created March 2026. You can
see it's also visible on the site here. I didn't republish the details
page or anything like that, but just want to make sure that the team was
clear that you can see it now on the staging website. OK. Um, so going, yeah.

**Lucas Nelson** 1:35:06 That being said, Andy, it should be worth noting on the call that that
we are investigating the delays on stage. Yeah, Andy, I think it's
worth calling out so people know that we're we're trying to be
proactive there, yeah.

Lyon, Rick (Director of Digital Experience)** 1:35:17 Yep.

**Andy Lambert** 1:35:20 Yep. So as you guys were doing the the KT session here and it sounded
like there might be something up behind the scenes. So I went into cloud
services and I see some some failed public well that's related to
publication, some some entries in the log. So looking into that and. Raise a support ticket and we'll keep you guys posted.

**Lucas Nelson** 1:35:44 Yes. So Gonzalo, hope you heard that. And I saw your hand was up
earlier. Gonzalo, I'm sorry if I bogarded the mic. Did you have
anything else, Gonzalo?

Gonzalo Calasich (SHRSS)** 1:35:53 Yeah, this is to Daniela. Were you going through the hiring event
component or that's going to be something for the for the next session?
Because I have a question about that one specifically.

**Daniela Tea** 1:36:04 That was gonna be tomorrow for the new modified agenda, Gonzalo.

Gonzalo Calasich (SHRSS)** 1:36:09 OK, we'll have it for tomorrow. No problem. Thank you.

**Daniela Tea** 1:36:11 Yeah, no, thank you. And and please let me know what your questions are
tomorrow for sure. And Mayte, I know we had also said I had saved the
URL for that specific one that had been unpublished. And so just showing
you this is what would happen if a user went to it. This particular
message here to be clear is something that's configured on the.

Gonzalo Calasich (SHRSS)** 1:36:16 Yep.

**Daniela Tea** 1:36:30 So if I were to take a look at it and the author, you can see I had my
error message. There are no events. So obviously if you want it to just
say this event no longer exists or something that could be something
that can be configured, but when you unpublish the content fragment. And sorry, when you unpublish the content fragment, that specific event
detail URL is also not available to the end user.

**Mayte Eme** 1:36:54 OK, it's good to know how it works. I'll add it as another gap.
That's not the functionality we're expecting, but at least the user
doesn't get to see it. So that's one plus.

**Daniela Tea** 1:37:07 Hi.

Lyon, Rick (Director of Digital Experience)** 1:37:07 Would we still be able to have a preview link to that, Danielle?

**Daniela Tea** 1:37:10 But we still be able to have a preview link. Um, if it's.

**Mayte Eme** 1:37:13 Nora.

Lyon, Rick (Director of Digital Experience)** 1:37:14 Like we had to make updates to the page after we unpublished. We need to
share that out to get approval before we published again.

**Mayte Eme** 1:37:20 That's a good question. So not a preview link as in the ones that we
are identified as a gap, but if we log into AM, can we work on the page
and see it within AM as a logged in user?

**Daniela Tea** 1:37:22 Sorry, I'm I'm. Uh. Uh. Yeah, so keep in mind again, it's one page. Everything's coming in
from the details here. If you publish the content fragment, it doesn't
automatically become visible to the end user. You would have to
essentially republish the. The calendar page. So when you guys are saying the event detail page,
it's just again, it's one page. Like this is just one page. K team. Oh
oh, I'm so sorry. One second.

**Mayte Eme** 1:37:58 Oh, wait, you're not sharing. So an unpublished page. You can still go to the detail page and see it
in AM and screenshot it to get approvals.

**Daniela Tea** 1:38:14 So if I were to on this, uh, not this one. One of my content fragments
was previously unpublished. I can't find it, but. We had unpublished the. Saint Patrick's Day one. This one is unpublished and you can see it's
unpublished. And your question is, would you still be able to see that
in a EM? So if I were.

Lyon, Rick (Director of Digital Experience)** 1:38:43 Yeah, can you send me a link to that? Can you post a link to that in
chat, the unpublished page?

**Daniela Tea** 1:38:46 I see. So if I were to, so you would not see, you would not see the
content fragment within the calendar, nor would you see the event detail
page if it's unpublished. If we were to publish the content fragment,
it would be visible.

Lyon, Rick (Director of Digital Experience)** 1:38:51 Or unpublished details, whatever. OK.

**Daniela Tea** 1:39:05 In the calendar as well as the link to be able to see the details.
However, until I publish this link here, this will not be visible to the
end user. But Rick, for your specific question about the details page,
if I just publish this, let me do that right after this call and then I
can report. Back on on that specific behavior for what you you just mentioned. OK,
yeah.

Lyon, Rick (Director of Digital Experience)** 1:39:26 OK. OK, good. Thank you. I just want to make sure that with content
fragments because they are kind of, you know, data elements that's
pulled into a template page to to render that we have the ability to
preview that before it's built or somehow built but not published, that
kind of thing.

**Daniela Tea** 1:39:35 Mhm. Yes. Yeah, no, understood the need for that. Sure. Yep, I will write back on
the Confluence page then. Yep, thank you guys. So I'll stop sharing and
I think we've agreed then for tomorrow's session, we're going to take
a look at some additional components that are specific to the careers
website, one of the things that.

Lyon, Rick (Director of Digital Experience)** 1:39:50 Perfect. Thank you.

**Daniela Tea** 1:40:07 I we can certainly cover is the how hiring events has been modeled by
using promotions. I believe we also had the video testimonials which are
on a couple of pages and I'm actually going to do a look. After this call to kind of, you know, take see what else is out there
and I'll be posting the new Confluence page prior to tomorrow's call,
which will detail out the other components I'll be covering.

Lyon, Rick (Director of Digital Experience)** 1:40:31 Hey.

**Lucas Nelson** 1:40:34 Daniella, it it. Does this mean we're? Pulling topics forward, so to speak.

**Daniela Tea** 1:40:42 Yeah, that's correct, Luke. Yeah, that's right.

**Lucas Nelson** 1:40:46 OK, we're not adding a session, we're pulling stuff forward.

**Daniela Tea** 1:40:47 So no, no. What we'll be doing, Yeah, what I'll be doing is like my
previous confluence pages where I have like the list of JIRA tickets
that the other reference. I'll be pulling those into my confluence page
as well for whatever's being covered.

**Lucas Nelson** 1:41:01 Yes, yes. This is actually really good. This is good 'cause it it's it's
prioritizing careers like Maite's \*\*\*. So OK, OK.

**Daniela Tea** 1:41:15 Yeah, yeah, absolutely. So yeah, if you guys can just give me a little
bit of time to get that out, we will certainly send it over though once
it's once it's ready to go.

**Lucas Nelson** 1:41:16 So, OK, OK. OK, 15 minutes left. Any any questions or feedback from today's
session, you know, let let let me know. I want to hear it. Anybody on
the call?

**Mayte Eme** 1:41:39 I'm still confused on how to use events, honestly. Um. Seems to have a lot of manual like check, check, checks and and added in
multiple places instead of how easy we have it now that we just do it
once and it populates wherever it has to.

**Lucas Nelson** 1:41:45 Yeah. Yeah, we we definitely want you to understand or as best as you can
might take the the baseline of of what we've implemented and yeah
ultimately with with the with the gap list and and getting the you know
the changes made to the platform on the road map. We want to get it right for you. So you know, encourage you to go back
to the recording because I know Daniella, no fault to her, but you know,
some of it goes pretty fast. There's a lot of information and we'll
look forward to seeing your your, your feedback and and questions and
confluence, OK.

**Daniela Tea** 1:42:20 Yeah.

**Mayte Eme** 1:42:33 Yeah.

**Lucas Nelson** 1:42:36 What? What else, guys?

**Mayte Eme** 1:42:37 And one question I did forget to ask is because we were talking about
events, events and just on that page and it had those filters on the top
for locations. But I assume we can choose or I might be wrong that we
can choose what location show and display it on any website, right? Like
if I'm in the. It's a Seminole gaming website that has six properties. I can only show
events for these six properties. If I'm in, I don't know, a campaign
that has three properties or only hotel and casinos, I can pick events
from those so I can. Set my criteria to show to display whatever events I need from these
venues or that venue. So from this month like mix and match criteria or
is that not possible with AM?

**Daniela Tea** 1:43:24 So right now the the way that the event calendar has been set up is it
points to one specific content fragment folder path. If I'm
understanding what you're saying, like you can certainly select like
the line of business folder so it would show like safe like casinos. It
could show all casinos, but it sounds like what you're asking. Asking for is say you don't want to show all casinos, but you want to
show a subset of casinos. Is that correct?

**Mayte Eme** 1:43:48 Yeah, and it could be, you know, hotel and casinos. It could be just the
Seminole staff, which are casinos likely, but it could be also just
based on location, who it could be a mix and match of different line of
businesses. It could be any big event anywhere, which is what we do in
entertainment.

**Daniela Tea** 1:44:01 OK.

**Mayte Eme** 1:44:05 We have venues across including Harbor Cafe Venue in Orlando. So that's
a cafe. Then you have from hotels like New York and then casinos and
casino hotels.

**Daniela Tea** 1:44:15 OK, yeah, so with the way that it works today is because you're
choosing a specific folder path, you can choose like a something in
higher up in the hierarchy. However, you are not able to select specific
folders from within there. To show multiple folders or build a calendar based off of multiple
folders that is not currently in our system.

**Mayte Eme** 1:44:40 OK. OK, sorry, I was just thinking how to how to do that, but OK, that's a
big gap for any casino, hotel, cafe, entertainment and all the websites
that are left. Can I pull events into somewhere else, something else than that event
page? Or are they logged to a specific template? Like we show events in
carousels across, you know, all the pages you might be in a restaurant
and we might feature events.

**Daniela Tea** 1:45:19 When you say pull events to other pages, you're saying outside of the
calendar. So would you like for example, like say you might want to show
just a specific event? Is that what you're asking Mayte?

**Mayte Eme** 1:45:24 Yes. 6. Yeah, we can go. It could be a venue, right? I could be in a venue page,
a small venue, like, I don't know, council log, right? And I want to
show the events for playing at the council log venue. Or I could be in
the homepage and show just a coming events from X. Category. I could be in the. I don't know. I I might want a show just
to give you a use case, right? The ones that have dinner and a show,
right? So pull all those.

**Daniela Tea** 1:45:52 Mhm. OK, so there is the ability because keep in mind these are content
fragments. We do have some other components outside of the event
calendar component which was strictly made again just to display event. Uh, Events. Uh uh. Event components. I'm going to share my screen really quickly and I
don't think this necessarily addresses exactly what you're saying, but
I'm trying to make sure I understand. So right now I'm showing a
component called the Contact Fabric card list. You can see I can display
a list of either news or events. There are some other things I need to configure to display this, but
because it's a content fragment, I'm able to display things outside of
that that calendar component, so you're not locked into using that, but
for your use case. You're saying like for example, if I want to select a fixed list of
specific calendar events, you could do that through here by choosing the
exact content fragment path. But what you're describing is like say
something by tag maybe. Does that sound right?

**Mayte Eme** 1:47:06 Oh. Um. Yeah, I don't know how you call them in in in EM, but something that we
can say these events, right? Maybe it's a tag that we add like dinner
and a show and then we query, hey, all the events, dinner and a show
from this property show here or within the same site to make it easier,
right?

**Daniela Tea** 1:47:21 Right.

**Mayte Eme** 1:47:28 Um.

**Daniela Tea** 1:47:28 OK, yeah. So if I and just by the way, because I see the time, what I
can do is I'm, I can, I'm going to configure some things, but I can
also share this tomorrow once it's like properly configured. But what
I'm saying is like yes, we could select the route path for the content
fragments and then.

**Mayte Eme** 1:47:41 Mhm.

**Daniela Tea** 1:47:48 If you have tags that are associated with that specific content
fragment, you could select that tag and then it would pull everything
that's related to that. So anything that's say like dinner and a show
or something, if that's A tag, you could pull that and as long as those
content fragments are tagged with that, that then should show up within
this content fragment card list.

**Mayte Eme** 1:48:01 Oh.

**Lisa Cardia** 1:48:08 And did we lose the filter for events? I know we, I know we lost the
filter for careers, but is it just because that was careers specifically
or did?

**Daniela Tea** 1:48:11 Did we lose the filter? No. Oh. So in terms of and with careers, keep in mind the component that we're
using for that is we we used a specific content fragment card component
which we will take a look at tomorrow and that's why there's no filter
on there if we use say the promotions component by default. A filter displays. I'm just going to add it here even though we're not
actually going to use it yet. So this is. I think this is the filter you
were expecting, is that correct?

**Lisa Cardia** 1:48:47 Yes, for events and and promotions.

**Daniela Tea** 1:48:48 Yeah. So to be clear though this the reason why we chose to use a card is
because by default that UI this filter will appear whenever this
component is used. Our understanding of like the careers website where
it shows. I'm just showing it on the live site. What was it? Was it hiring,
hiring events, right? Since there's a filter here, that's why we chose
to use an individual card. Lisa, there's a filter here by with the way
our component works, it does put that filter. I mean, if that's
something that's desired on the homepage, certainly could be changed
out.

**Lisa Cardia** 1:49:11 Thank you.

1:49:11 Mhm.

**Daniela Tea** 1:49:26 But that's the reason why there was no filter on there. And then same
thing with on this page here. Yes, we can switch it out so it's using
that promotions component instead and it would have the filter that I
just showed in the previous page wherever that page is. But we had made a choice, at least for the homepage, to just use a
content fragment card component because we didn't want the filter to
appear on the homepage. Does that make sense?

**Lisa Cardia** 1:49:54 I well, I think it definitely makes sense not to have the filter like in
the section on the home page, but I guess I'm just confused why we lost
it. If we're using the promotion card model and it exists for
promotions, why we wouldn't have had the the filter on that landing
page at least.

**Lucas Nelson** 1:49:59 Yeah.

**Daniela Tea** 1:50:12 So that can certainly be changed out. We can explore that more tomorrow
in terms of whether say for example the filters is matching what you're
expecting is the fact that the search bar for example that we have here,
is that something that you that you want to be displayed in this page
like so those we can definitely discuss this. We'll we'll discuss this more tomorrow, but what I'm saying is if it
if that's perfectly fine after we review the component, that can
certainly be swapped out on this particular page.

**Lisa Cardia** 1:50:34 Mhm.

**Mayte Eme** 1:50:46 OK. And Speaking of careers, since we're on the topic, can I pull
career jobs, like hot jobs or hiring events into a property page? So we
have reverb, let's say that we are hiring for reverb. And I'm just making a use case, but can I pull some of those like maybe
with a tag or location? You know if location is Atlanta, GA and it's
river then show on the river website as maybe a carousel or a grid of
like 3 or 6.

**Daniela Tea** 1:51:13 So.

**Mayte Eme** 1:51:26 Mm.

**Daniela Tea** 1:51:26 Again, you can select the root path of where the jobs are located. I
guess my question is would it be A tag or would it be, you know, kind of
grouped together in one location? So like I can select anything from like say London and I can display it
on any page, right? But if you're what you're asking for is you want
to show like say Great Britain and Spain that currently cannot be done
together in this one component.

**Mayte Eme** 1:51:42 OK. And if it's within a location, let's say property specifically, Tampa
is having a job fair and they're coming up with a landing page because
they do that and we want to show only the Tampa jobs, we can do that or
we can maybe group them. Maybe it's a job fair about we have culinary
job fairs.

**Daniela Tea** 1:52:10 Yeah, so.

**Mayte Eme** 1:52:16 More often than we would like, right? So we want those jobs. Um, only
those.

**Daniela Tea** 1:52:19 So, so here you can see I've selected the Tampa folder and like, so I
what I did was I navigated to the structure in the dam. So all those job
postings again, these are coming in from work day and it's based off of
the state and the country, right? That's how these got structured.

**Mayte Eme** 1:52:25 OK.

**Daniela Tea** 1:52:37 Structured so I can select that specific folder. So in your use case
that you just described, my take Tampa, you want to show any Tampa jobs,
I would select the Tampa folder and then all the jobs that are
underneath that should appear within this component.

**Mayte Eme** 1:52:43 Mm. OK, and if I want to exclude a category under Tampa, I can't. It's
just gonna show everything from Tampa.

**Daniela Tea** 1:52:59 When it's when you say, oh, you mean like, OK, like a category. So
currently that's right, right, right, right. Right. Currently that is
not something that you would be able to do within this component. It
would just show everything that's within this specific folder path.

**Mayte Eme** 1:53:05 Like marketing and food and beverage accounting. OK. OK. And to be fair, we cannot do that right now with the ISAMS job. So I
was just wondering.

**Daniela Tea** 1:53:24 Yep.

**Edwin Aquino** 1:53:26 OK, Daniela, before we have, before we run out of time, there's one
other question. Sometimes with events we have a little field that for
text specifically it's usually empty. We keep it empty, but sometimes
we like include maybe A tag that says 21 plus event or free event or you
know, a phone free event where we can't use our phones.

**Daniela Tea** 1:53:29 Sure. Uh huh.

**Edwin Aquino** 1:53:45 Is there anything like that that we can have on these events
specifically where some way to display A tag of sorts on them?

**Daniela Tea** 1:53:45 OK. Edwin, can you send? I think I I feel like I've seen an example, but
can you actually send me an example of that and I can take a look at
that and discuss that with my technical team? I just want to make sure I
I I understand the exact ask and how it currently looks, if that's OK.

**Edwin Aquino** 1:54:02 OK. OK. Yeah, sure. I'll be more than happy to.

**Daniela Tea** 1:54:08 Thank you. Appreciate that.

**Edwin Aquino** 1:54:10 Of course.

**Lucas Nelson** 1:54:11 All right, I'm calling it. Thanks guys for your time. Appreciate you
again, Daniela, for walking through events today and we'll look forward
to seeing the updated agendas for tomorrow because we're we're
amending it a little bit.

**Daniela Tea** 1:54:28 Yeah.

**Lucas Nelson** 1:54:29 To accommodate careers. So and I'll send out the recording and the the
transcription. Hopefully this time the recording loads correctly so you
guys don't have to ping me about that. And then I think the last point
I'll I'll I'll put out there when I send the e-mail. Daniella was
also calling out the. Highlight on the the questions that we we yeah, I'll I'll put that
instruction as well. Yep.

**Edwin Aquino** 1:54:51 Yes, you.

**Lucas Nelson** 1:54:56 All right. Thanks for your time, guys.

**Daniela Tea** 1:54:56 Awesome. Thank you, everybody. Bye, bye.

**Scott Sorel** 1:54:58 Thank you. OK, bye.

Gonzalo Calasich (SHRSS)** 1:55:00 Thank you. Thank you. Bye.

Scott Sorel** stopped transcription



## Session: Careers — 2026-02-12

**SHRSS Adobe Knowledge Transfer-20260212_130224-Meeting Recording**

February 12, 2026, 6:02PM

1h 53m 20s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:10 Okey doke. Thanks for joining us this afternoon. I'm letting ACN. OK,
cool. Let me share my screen. I'm gonna kick us off and then I'll hand
it over to Daniela for the next. Component she's gonna review. Can you guys see my screen all right,
Scott?

**Scott Sorel** 0:35 Yep, looks good.

**Lucas Nelson** 0:36 All right, cool. So this will look familiar to Scott, but be new to
everybody else in the call. What we tried to do is we tried to put
together a view, notional view of the knowledge transfer calendar.
We're in week 1 here.

Angelika Akopyan (SHRSS)** 0:49 OK.

**Lucas Nelson** 0:53 To kind of plot out where where our KT plan is is tracking towards. This
is out there on Confluence published under KT calendar as the page.
You'll see it over here on the left side. So um. Key call out here as I walk you through the legend. CA is content
authoring. We tried to align language based on the SOWTE is technical
enablement. Scott, you'll notice I have a call out for morning times
for those. So when I get midweek March. 2nd or sometime before if we need more lead time, yeah, probably the
week before because we're going to start them on that Thursday. We want
those those technical ones to be in the morning so Vinay can join
because he's the kind of the source of knowledge on our side, yeah.

**Scott Sorel** 1:47 I. Okay. Yeah. And what what what do you think about then? We'll figure it
out. Okay.

**Lucas Nelson** 1:51 So keep that in mind. Yeah, yeah, yeah, yeah, yeah, no problem. Adopt.
There's an adoption strategy part of this that we've brought Jacob
White, some of you have worked with him in the past on for. We want
those on Thursday and after we're done with the. Content authoring sessions that Daniela is running. We'll dig a little
bit more into those as we get closer and then the big point of what I
want to talk through here just briefly before Daniela gets into her
stuff. Is the platform expansion sessions the last two weeks and and then
we'll you know Jacob will be wrapping up his adoption uh strategy
sessions so. And and these are in the SOW and what we aligned with the intention with
Macario for this entire knowledge transfer work stream is that we're
going to reach decision points for stuff that that that's in the
backlog for this what we've been calling the, you know, the gap list. That that we want to see if we can fit with the with the current
platform or we can modify what's in the current platform or if it's
net new that needs fully new development on the new on the platform so. How this ties in and why I wanted to bring it up now is like
specifically right here where I have underlined and you guys can read
this page whenever you want and if you have questions definitely let me
know after after the call. But we're seeing a lot of questions. It's good. Maite, you're busy at
night and we appreciate the diligence, but we're gonna have to start
leveraging a question backlog. We'll have a different page on here
that'll say question backlog. That that our team's gonna try to park some items in that that are are
going, you know topics and questions that you have that that are
requirements for preparation for that plat platform expansion part of
this work stream. When I say platform expansion, again, it's there'll be tickets that we
want to make sure we have fleshed out in in your Jira instance that are
going to inform what we need to scope for a future, you know, for the
future to to implement on the platform to to cover the. The gaps that you're identifying and these questions, some of them
we're noticing will fill, will fill nicely in to what you guys are
going to provide us and what we'll have some disposition on when we get
into these last two weeks, March 16th and March 23rd. So we just wanted to call that out as we're going through questions.
We're going to keep to what we've talked about. We're going to try to
address in subsequent sessions or or you know respond directly in
confluence where where we can and if further you know collaborations
needed we we called out. Highlighting those will defer to follow-up discussions if they relate to
other content authoring or technical discussions, or for a lot of them,
they're going to be captured as backlog gap analysis or future
consideration, and none of this should be a surprise. Because this is directly from the SOW and it's kind of working as
we've anticipated, although the question there's more questions than
we thought, but it's not necessarily a bad thing, it's just we're
reacting to that and trying to make sure we accommodate it with a
process. Um, yeah. So that's that. That's what I wanted to share with the team
here. Are there any questions like quickly before I hand it over to
Daniela? OK, Daniela, I did I did I give you some time? Are Are you ready to go?

**Daniela Tea** 5:49 Yeah, but sorry. Yeah, thanks, Luke. There's actually just one more
update that I wanted to share and I think Andy was going to take that.
It's with regards to some of the issues that we were seeing yesterday
when we were trying to publish and look at it on the publisher. Andy, I
don't know if you're available to speak on that right now.

**Andy Lambert** 6:11 Yep, sure. Hey everybody. So yeah, if you guys were doing the KT and and
reported and that you were seeing delays and seeing updated content on
the in the published environment, I started looking at the stage logs
and found. A couple of artifacts that I want to actually need to submit the ticket.
I'm going to send a ticket to support just to have them look at the
environment and verify that things are OK now after well even during at
the toward the end of the KT session it said it looked like. Content was showing up that Daniela was publishing and then we did some
testing after and everything looks alright. I'd be interested to know
if you guys have seen any delays today. If so, I'll grab from the logs
and include that in the support ticket, but. Just want to have them check the published environment. It looked like
maybe indexing of content, which is a job that a scheduled job that runs
in the environment from time to time may have been slower than it
necessarily should be and that would cause. The search kit functionality and the the back end stuff that that
surfaces content to be slow and show them updated stuff. So anyway I
just wanted to keep you in in the loop let you know Gonzalo. I'll
actually CC you on the ticket so you have visibility into what how they
respond. But right now the environment looks good. I just it's just for due
diligence to to see where if we need assistance or they need to tweak
anything then that's where we're at.

Gonzalo Calasich (SHRSS)** 7:50 Thank you. We we tested in the morning and we were still facing the same
issue. You say that they should like if we create a a custom job, it
should show up on the jobs page.

**Andy Lambert** 7:55 OK. Yeah, it should. Yeah, I am. Oh, go ahead.

**Daniela Tea** 8:03 So, hey, hang on. Sorry, Andy. Gonzalo, when you're saying, I think
Andy, when you're saying job, is that different from Gonzalo talking
about like the job content fragment?

**Andy Lambert** 8:12 Oh. Oh.

Gonzalo Calasich (SHRSS)** 8:15 Oh, different.

**Andy Lambert** 8:16 So it well, it depends right on the how the I'm not familiar with the
details of how the job's. Danielle, maybe you could speak to it. Is
there any reason why like when you're so this is manually authoring a
job as opposed to it coming in from? The feed the um integration with Workday. or work right, which I read.

Gonzalo Calasich (SHRSS)** 8:39 Yeah, yeah, no, no, this is this is when you we have the the the option
of creating a a new content fragment, right? And we created, we
published, we wait 5 minutes, but still doesn't show up on the job
search page.

**Andy Lambert** 8:47 Mm-hmm. Yeah. OK, but if it's either either yes, there's. My question is would if
you publish other content like a event content fragment or a pay a test
page, I would check to see if it's showing up immediately.

**Daniela Tea** 8:59 So.

Gonzalo Calasich (SHRSS)** 9:03 Thank you. Yeah, it shows up. Yeah, if you if you change, if you change another
content fragment it works, but for for the page job it does not.

**Andy Lambert** 9:13 Then then that. Yeah. Then there's. Then we need to OK, that's helpful.

**Daniela Tea** 9:20 OK, so because yeah, Gonzalo, just to confirm and and so we can check
back on the recording, we are saying that editing a job content fragment
is not visible after you publish it on the job search page. Is that
accurate?

Gonzalo Calasich (SHRSS)** 9:34 Correct. Once I create and I publish the contact fragment and I go to
the jobs page, I shall see the the just created job posting and I'm not
seeing that.

**Daniela Tea** 9:36 OK.

**Andy Lambert** 9:47 Got real quick, Daniela. Oh, go ahead. You do that and then I'll, I've
got to follow up.

Gonzalo Calasich (SHRSS)** 10:02 Yeah, that's correct. Yeah, that's correct.

**Daniela Tea** 10:03 OK. Sorry. Go ahead, Andy.

**Andy Lambert** 10:07 Yeah, so could you paste into the chat if you have it now and if not you
could do it later. Just examples of a couple of URLs for the job, the
content fragments and author. That way I can check the logs against that
and see what we need to find is.

Gonzalo Calasich (SHRSS)** 10:11 Yeah.

**Andy Lambert** 10:23 Where where the the bottleneck is or the the blocker like is it with the
published process? Is there an error happening based on the content
fragment model? You know we need to just basically do some
troubleshooting and find the root cause and then and let you guys know
and then we'll. More remediated.

Gonzalo Calasich (SHRSS)** 10:43 Sure. So So what I can do is I can as soon as I create a couple ones I
can shoot you an e-mail or or maybe in Slack. The the challenge we're
having also is that when we create this custom job postings and we set
the flag to is not API data right?

**Andy Lambert** 11:03 Mhm.

Gonzalo Calasich (SHRSS)** 11:03 The workday process, when it pulls all the job IDs, it's also including
the ones that are manually created, so the process is deleting them. So
that's another thing that we found, right? It seems that.

**Andy Lambert** 11:15 Yep. Yeah, yeah, we need to talk about that.

Gonzalo Calasich (SHRSS)** 11:19 Yeah, it seems that when they are calling this get all job IDs, it's
not excluding the ones that should say no, this is this is not an API
data. So yeah, so so we were having that challenge. So again, right, I
can create a a couple ones and let you know.

**Andy Lambert** 11:30 Yeah.

Gonzalo Calasich (SHRSS)** 11:34 And and then they will disappear in the next 30 minutes because I think
that's how how everything is running.

**Andy Lambert** 11:35 OK. All right, so I'm gonna I'm actually we've been talking about this
internally and are aware that the API is over is you know affecting the
manually created job content fragments and so look for a e-mail from me
related to that and.

Gonzalo Calasich (SHRSS)** 11:46 6.

**Andy Lambert** 11:57 Our recommendation for for you know dealing with that coming up soon.

**Lucas Nelson** 12:01 It. And one more comment on that and then yeah, we'll we'll we'll go
ahead and move on to what we're here for. Andy and Gonzalo, I created
the cadence for the tech sync starting next week, Tuesday, Thursday.
Andy, I think it'd be good to you know. Obviously send the e-mail, but use those sessions as well to to kind of,
you know, drill further into what we're recommending. Does that sound
good?

**Andy Lambert** 12:21 Yep.

Gonzalo Calasich (SHRSS)** 12:25 Yeah

**Andy Lambert** 12:25 Yeah, I'll send it that that way. Yeah, we we touch base on this
morning. I'll send that so that they've got the let up, take, absorb
the e-mail, let it marinate and then we'll get to dig into it on the
first texting.

**Lucas Nelson** 12:37 Perfect.

Gonzalo Calasich (SHRSS)** 12:39 Sweet. Thank you.

**Lucas Nelson** 12:39 That works. Yeah. Yeah. Thanks guys. All right. Um, Danielle, you all
ready?

**Daniela Tea** 12:45 Yeah, sure. OK. All right. Thanks everybody and thanks Andy for that.
Trying to remember if there's any other updates that we need to share,
but I think that was it. So more to come on that particular portion of
of jobs.

**Lucas Nelson** 12:46 Alright.

**Daniela Tea** 13:03 So today we are, as mentioned earlier, we are going to pivot a little
bit. I know the desire is to identify additional components that are
used on the careers website and we'll focus on that. The components
that I had personally identified when I was reviewing it, I'm trying to
find my Confluence page. It is not on this tab. I had identified about four components or so that I wanted to go over
today. And then also since we will certainly have additional time at the
end of that, we can continue to review the careers website and then see
if there's anything on there where we would we would like to take a
closer look at so. Here is what I had to do. I'm going to share my Confluence page. This
is what I identified that's used on the Careers website. We have the
promotion content fragment, but I'm going to be showing promotions as a
whole. This is currently being used for the hiring events, so we'll
see. See how that works right now. I also saw we have the video card
component which is used specifically for the testimonials. I also saw
the video component is being used on a couple pages and we'll take a
look at that and then the card component which we know is being used all
over the place on the careers website. There is the icon variation that's being used, so I wanted to just take
a look at how that was set up. Keep in mind though that we will
certainly review cards additionally since there's certainly more than
one variation on that want to cover exactly what was used. For the careers website. So I think this list, don't worry, this list
can certainly grow as we continue to review the career site, but this is
definitely what I want to talk about first and then we can move on to
other aspects of the careers website. All right. So starting off now with our promotion search and promotion
content fragment, we're going to do something similar to what we did
yesterday and the day before, where we're essentially going to take a
look at the content fragment model. And also some content fragments that are using that model. Then we're
going to take a look at the component that's calling in those content
fragments and displaying them to the end user. So here we are in AEM
going to just navigate to the DAM so we can take a look at that content
fragment model. And I'm going to go to SHRSS and Content Fragments and I'm going to
click on Promotions and I'm going to click on KT just for my test data
and I'm going to hit Create and click Content Fragment. All right, so looking at these templates, I want to select the promotion
template. I'll select that and hit next. And for my title, we're just
going to call it KT. I'm going to hit create. Alright, as a reminder, we are having that support ticket put into
default to the old editor. So for right now I'm just going to manually
switch it to the old editor as we review these page review these
fields. Going to increase the size of my screen a little bit. OK. All right, so let's look at what we have here for our promotions
content fragment model. We can see here a couple of required fields and
some that don't actually need to be filled out. And I'm also going to
pull up after this the some filled out ones that we are using currently
on our careers website. So starting at the top we have the ID and the name of the promotion.
These are required fields. We also have a title and we can see where
these things are displaying on the end user in a bit. We have statuses
of active or inactive, a card image. As well as the alt text associated with the card image, these are
required fields. Banner images for when you interact with the promotion
and see it on a specific page. These are also required the date format.
A couple of different ways you can display the date. If you want only the date, the date with the start time, date with the
end time, or the ability to display override text. So these fields here you'll notice they are not actually required. So
if you just need to use say the date overwrite text field, you can
certainly do that and not fill out anything else. We have our promo types, loyalty or slot. One thing I wanted to comment
on is these this promotions content fragment model was initially created
based off of requirements for the casino's website. So you'll you'll
notice that you know these options are specific to casino. Understand. Is that there is a desire in the future to perhaps leverage this content
fragment model for some other additional use cases outside of casino.
That certainly would be something that we want to make sure is captured
during the gap phase, but just wanna make sure the team is aware that
this specific content fragment model was mainly for the casino. Websites and that's what you'll see here. So I have our description field, location and venue with these options. The ability to override the road location and put just text if it's not
something that's listed in here. We also have some CTAS for to be
displayed on the card when it renders and then that LD JSON field we had
talked about which is going to be present on. The content fragments in general, you'll see this field often. So this
is the initial content fragments before you fill it out. Now I want to
take a look at something that is filled out. Uh, such as this one. I'll take this one right here and then we're
going to see how it looks like on the website. Let me open that up in a
different tab. OK. All right. Here we go. Actually, I'm going to go back and look at the full time one, just so
that way we're not getting confused between the ones that have similar
data. So one second, I'm gonna go back and just open up the full time
one. OK. All right. OK. So let's take a look at what we have here. So we
have our ID field. That's not going to be something that's going to be
displayed to the end user. It's something that's part of the
configuration. But focusing on what we see for the end user, we see
our. Our name and title. We can change one of these to see which one actually
affects this. I can do that right now.

**Lisa Cardia** 20:21 Wait, sorry to already interrupt, Daniela, but what? Where did you get
the ID from?

**Daniela Tea** 20:24 So the idea is of field that's inputted by the by the end user or sorry
by the author.

**Lisa Cardia** 20:31 But like, what would we put?

**Daniela Tea** 20:33 So this is a unique. This is a unique identifier that you would put in
order to be able to display the specific content fragment as say like a
singular card onto your site. So it's a way to be able to. Let's show
that in action.

**Lisa Cardia** 20:34 If it's required.

**Mayte Eme** 20:49 Is that a made-up thing that we do? Do we just make up the stuff?

**Daniela Tea** 20:52 So that is. So that is a field that was identified during the requirements of
something that was needed. So here's an example where I'm calling in
this.

**Mayte Eme** 21:00 But I mean, I for the requirements for the casino promotions, we did not
require a unique ID. We required a unique ID for targeting and
analytics, but that was pretty much it.

**Daniela Tea** 21:14 So. I think we would need to check as to the for that specific bill. Perhaps
that is the reason why. However, you can see here with my content
fragment card component, I'm pulling in the specific promotion that's
listed here using that ID field. So this is one way to be able to display this promotion. We are also
going to show how it will display within the promotions component, but
if you need to display just one singular promotion and feature it, you
know on like a specific page or something, this is the ability. This
gives you the ability to just show that. That one item as needed.

**Lisa Cardia** 21:56 Are there like required letters, numbers, sentence casing left like why
you chose HE?

**Mayte Eme** 21:56 Um.

**Daniela Tea** 21:59 No.

**Mayte Eme** 22:00 Yes.

**Daniela Tea** 22:01 Nope. The only reason why HE was chosen was for hiring events and then
one just for for tracking purposes. There's absolutely nothing there
that is. There's no like text require text requirements here. It's
just like. Like it doesn't have, it could be, you know, like HE or something, but
you want it to be unique, right? Like because when you're referencing
that specific job, I want it to to only show the one that I have here in
this ID field.

**Mayte Eme** 22:24 Yes. OK, let's call this as a gap because we have to fix it and the see that
at least remember what I type. Because honestly, if I'm a content
author, I'm just gonna do blah blah blah, right? So does he remember
that I've used that? So I don't use it again and then pull the wrong thing. Like is it smart
enough to know that there's there's existing set of IDs?

**Daniela Tea** 22:55 So I don't know like sorry I'm I'm like trying to show it but you
can't see it. But there is a message that says checking unique
validity. Like I know it's really fast and it's flashing but when I
like skip off of this you can see that it is checking in this field
whether or not this particular value is unique.

**Mayte Eme** 23:14 And when you.

**Lucas Nelson** 23:15 Daniela, would it let you save if if you used one that already existed?

**Daniela Tea** 23:19 We could try that.

**Lucas Nelson** 23:20 I'm sorry to make you be a QA on this. Sorry.

**Daniela Tea** 23:21 It's OK see, so the value needs to be unique. The same value is also
appearing in a different one.

**Mayte Eme** 23:28 OK. And when you when you thank you look for that and when you paste it
somewhere else this does it, is it smart to tell you, hey these are the
ones that you can select from or you have to like remember it and or
paste it?

**Lucas Nelson** 23:28 Thank you.

**Daniela Tea** 23:40 When you say when you paste the ID or.

**Mayte Eme** 23:44 So I saw that you put it somewhere else, right? I don't know why, but
you had to put it somewhere else. So is that that drop down that you
select or?

**Daniela Tea** 23:50 Are you talking about in this in this component? This is this is a blank
text. This is a regular text field.

**Mayte Eme** 23:58 So it's not as smart.

**Lisa Cardia** 23:59 Yeah, so it's like if I were to add an event, but then someone took it
down and then they went back in because I was like, hey, can you add the
halftime or the hourly rolls event now they would need to know like they
would have to go into the fragment first I guess to check the promotion
ID, copy it. To get it here like we wouldn't be able to like go through a folder
path or anything to grab it, I guess. Is that I guess the way to answer
that? Like how would we know if other authors created the code where we
would go obviously to keep some consistency and organization there too?

**Mayte Eme** 24:21 Mhm.

**Daniela Tea** 24:26 So. Oh. So just keep in mind I'm showing how the content fragment card is using
this promotions content fragment model. Let me add let's actually I
have that here. So this is the actual promotions. The promotions component and So what this is going to do?

**Mayte Eme** 24:52 And one more question, is this ID, sorry to cut you off, but really
concerned now, is this expected to be used for casino promotions or just
for careers because?

**Daniela Tea** 24:53 Is Yep. This was supposed the the intention of this component was initially
created specifically with casinos for casinos.

**Mayte Eme** 25:11 But we're not using it for casinos, right? We'll fix it for casinos
because we deal with a lot of promotions and more than one user. We
can't be remembering made-up by this.

**Lucas Nelson** 25:23 Yeah. So might say definitely capture what, what, what it doesn't
currently have. You know, that's exactly the stuff that we would want
to disposition in those last two weeks. You know what I mean? OK.

**Mayte Eme** 25:32 Yeah, this one is more of something that we didn't ask that got added.
So it's not like a gap, it's like an extra that we don't need.

**Lucas Nelson** 25:41 Yeah, think think of it like at the end of it is you know there there
there's a there's a change in modify piece of it too. There's adding
and then there's change in modifying as well. So if there's something
here that's implemented that's not quite meeting the mark and needs to
be updated, that should be a part of it as well because it would be
updating the. Um, you know, the component that was already delivered. So yeah, but I
hear you.

**Daniela Tea** 26:04 So yeah, so Yep.

**Lisa Cardia** 26:05 And then Daniela, I know you were about to show us it with the filter,
but the reason why I didn't want you to jump quite there yet is because
my question was related to getting it on the page without the filter,
which is what we have right now on the stage site for careers. So while
it might not be needed for the filtering, I just want to know what the
process is like. For a user to get it without the filter before you jump in to say
that's why I didn't want you to jump because we don't have the
filters on the stage site so.

**Daniela Tea** 26:28 Get it without to get it without the filter. Yeah, so I I think my my question though is and I'm actually going to
let's pull up the yeah. So this is where I wanted to understand and why
I want to show the component previously. I think it was yesterday we were talking about how like for example on
this page you did, you guys do want to filter on top and so that's why
it makes sense to use promotions component in order to be able to show
the filter on top and here on the homepage.

**Lisa Cardia** 27:00 Mhm.

**Daniela Tea** 27:03 There's no filter, which is the reason why we use that different
component, the content fragment card. And so in terms of like for
example, say like if if we wanted to capture as a gap that the you
wanted to have promotions but have it have an ability to remove the
filter, that could be something that could be captured as a gap.

**Lisa Cardia** 27:10 Right.

**Daniela Tea** 27:23 Or desired. The reason why we had to use that content fragment card
component is simply to be able to match what we were seeing on the live
site with the components that we had. But yeah.

**Lisa Cardia** 27:32 Yeah, I I just don't want to lose the question of it was just about
around getting this on the page means we can't like sift through
options to know we're selecting the right card. A user needs to go into
the content fragment, find the ID, copy and paste to get it to this
page. So I just wanted to make sure that's clear without the promotions
filter. Those are the steps to get it.

**Daniela Tea** 27:54 Without the promotions filter, if you're using the content fragment
card component, yes, this.

**Lisa Cardia** 27:59 We would need to know that ID like to my taste point, you'd have like
if other authors are in it, or even if I just don't remember what I
made for the code, we can't go through a folder to find it in the
fragments. We have to remember the unique ID, so we just need to make
sure we copy and paste it. From the fragment asset folder to get it here.

Gonzalo Calasich (SHRSS)** 28:22 Yeah, I correct.

**Daniela Tea** 28:22 OK.

**Lisa Cardia** 28:23 There's no other way without having it copied and paste like that.
There would be no other way whether I made it or someone else.

Gonzalo Calasich (SHRSS)** 28:27 I I did.

**Lisa Cardia** 28:32 Sorry, Gonzalo, go ahead.

Gonzalo Calasich (SHRSS)** 28:32 Yeah, no. My suggestion would be ideally like you have this page patch,
you should have something that says source and you will click and you
will navigate to to the content fragment section and pick up the one
that you just created for example right instead of you remembering. That that's how it works now, my two cents.

**Mayte Eme** 28:52 Wait, how do you say it works now? Because we don't have a unique ID.

Gonzalo Calasich (SHRSS)** 28:57 No, what I'm saying is that you don't have to remember the unique ID.
What I'm saying is that you should have like another field that says
source, right? So you add the card.

**Mayte Eme** 29:04 Oh, no, no, sorry, Gonzalo. I I do get that. I mean, I but I'm saying
we don't use that right now. We we don't have to enter an ID for a
promotion.

Gonzalo Calasich (SHRSS)** 29:07 Oh, OK. OK. No, no, no the the source part that's that what what I was explaining
that that's how we have it now.

**Mayte Eme** 29:19 Uh. Oh, OK, cycle source that you can. Got it, got it, got it. Not the use
case. OK.

Gonzalo Calasich (SHRSS)** 29:23 That you not not correct.

**Lisa Cardia** 29:24 Just to get the card on the page. To get the card on the page without a
filter, we would just use the source of the card and find it through a
folder path.

**Daniela Tea** 29:37 Mhm. OK, yeah, no, we understand what the ask is. So right now though, the
way that this does work right now is by selecting what the promotion ID
and you'll see here. So this content fragment card component, keep in
mind it's not just used for promotions, it's also a way to be able to
display events or. To be able to display news. So this is this is not restricted to just
promotions, but for the case of promotions or events it is expecting
that ID. So certainly something that like I mentioned what Gonzalo was
discussing could be identified as and listed as part of the gap analysis
for an enhancement to this. this particular component and that

**Mayte Eme** 30:20 Oh no, no, no, don't, don't. We don't want. We don't need this. So
let's not enhance this to use the unique ID. Just creates more work on
content others. We gotta redo it so. It someone needs.

**Daniela Tea** 30:33 I guess what I what I'm trying to say Mayte is we we understand that
the having to put promotion IDs by any means is not something that's
desired. However, to be able to show a specific event would require and
or I'm sorry, a specific promotion would require say like an additional
field like being able to pull up the dam and then selecting from the
list of content fragments but either. But either way, that is something that we would need to discuss and we
want to discuss during that gap phase.

**Mayte Eme** 31:00 Yeah, let's discuss the right way to do it and not add to this one,
please.

**Daniela Tea** 31:06 I'm going to hit, yeah, I'm going to hit cancel and so Lisa, to your
point, I think we covered like how you would use this component right
now and how it's being used right now in the stage site by putting in
the specific ID.

**Lucas Nelson** 31:06 Sounds good.

**Daniela Tea** 31:23 But I did wanna show, yeah, that the promotion search component. This
particular component is specifically looking for promotion content
fragments. So you'll see here. Sorry, I didn't mean to hit the
configure window. So you'll see here there are three different.

**Lisa Cardia** 31:25 Yes.

**Daniela Tea** 31:43 Promotions that have been added within our folder and you can see that
they're being displayed here. However, with the promotion search
component by default it does display filters. It displays the ability to
switch between the two different views and it also displays a search
bar. So I know one of the questions. Questions. I believe I saw a JIRA ticket or so which asks why hiring
events does not have the filter that can be added. You know this
particular component can be added there if that's desired. However, I
do know that you know perhaps. There might be some instances where you know if you evaluate the
component, you might not want it to have like the filters looking like
this or something, and so that's why we had chosen to do it as a single
single cards instead. So if that's something that you guys want to swap
out, that can be done.

**Mayte Eme** 32:31 So. But we have it right now, right in the current websites, and it was
decided not to do it even though it can be done.

**Daniela Tea** 32:40 So the reason why we're saying this is because these are supposed to be
events, is that correct? These are events, the event calendar as we had,
they are OK, so they're hiring events and so the hiring events could
theoretically be using the event content fragment.

**Mayte Eme** 32:49 They're hiring events not to get confused with.

**Daniela Tea** 33:00 Model. However, there are some capabilities that we know you guys need
for the hiring events to be displayed a certain way, such as the
override text ability and such as I I believe previously we saw like the
event shows the address versus the name of the. The property, etcetera. And so when we were doing our evaluation instead
of using the event content fragment model, that's why we chose the
promotions content fragment model. However, we wanted to make sure we
talked about this with you guys to understand if it makes sense to use a
promotions content fragment. For these hiring events or if that should be switched out to say
calendar and then understanding the limitations of that. So what we have
currently on the stage site right now is we made the choice to do it as
promotions versus using the event content fragment model and that's
what we want to know. Should that be switched out? Should it stay as a
promotion so it.

**Mayte Eme** 33:43 OK.

**Daniela Tea** 33:55 Looks like this that that's a decision we need to understand.

**Mayte Eme** 33:58 I can't answer without understanding what each one does, and I'm not
fully aware yet. Not all events happen at properties. So when you say
address versus property, events happen outside of our properties. So is
that something that both of these components can do or just the one?

**Daniela Tea** 34:17 So with regards to our promotion component and this was, I'm switching
it back to whatever the unique ID was for this. Let's take a look at
this. So where we see here like every Tuesday 10:50, we know right now that
our. We know right now that our events component does not allow you to
display it like this because this is using some overwrite text, right?
So we don't have a date overwrite text field currently in our event
content fragment model. That's one of the reasons why we said OK, this
this is something that's in promotions. You could use promotions to play like that and then here with this
particular venue you can see here that's also using the location
override text versus connecting to the locations content fragment
that's that has data from DPLT.

**Mayte Eme** 35:15 But the locations don't come. I mean, we might go at our Convention
Center, right? Not our location.

**Daniela Tea** 35:20 What I'm saying though here is this gives you the ability to put
whatever the location is. There's absolutely no connection between this
and DPLT. With events though, there is a connection with DPLT since
you're selecting from a list of of locations that are in A EM.

**Mayte Eme** 35:30 OK. Wait, so you're saying events can only have locations from DPLT? So if
the location is not in the DPLT, we what do we display like we can't
display event?

**Daniela Tea** 35:46 So when we when we take a look at, let me pull up an event.

**Mayte Eme** 35:51 Because locations should be in the DPLT, but we all know it takes some
time, so we will need to put events when the location is not yet in the
DPLT and we should, you know, type it, type whatever it is so customers
don't know.

**Daniela Tea** 36:03 So right now you see here the location reference has to point to an
existing location content fragment. This these location content
fragments is data that's being sourced from DPLT.

**Mayte Eme** 36:16 So DPD wasn't been well, OK, OK, we'll just add questions to the page.
I don't want to take all the time on that.

**Daniela Tea** 36:24 So let's let's, uh, where? Where'd it go? Oh. One second. Oh, OK, OK. I think this was it. This was it, alright. Alright, so let's take a look at this promotions search component. And see how some of these other fields are mapping to it. OK, status
active. So we see our card image, card image alt text. The intention for
that of course is to display as a card. We have our banner image, so if
I am clicking on a promotion. And there's a separate page that's going to appear there. I don't
think these are set up for that. My understanding is for the current
hiring events you guys have, I believe it's just correct me if I'm
wrong, but I believe it's just a. It's just like a these are external links. Is that correct?

**Mayte Eme** 37:25 Not always. Sometimes we have events, they create pages and we link to
them.

**Daniela Tea** 37:31 OK, got it. Yeah. So for for this case, I believe this is relevant for
say the if this was used for a casino promotion. My understanding of the
casino promotions is there are additional pages associated with it.

**Mayte Eme** 37:43 Not, not always, especially promotions. Some of them don't even have
detailed pages behind them.

**Daniela Tea** 37:48 OK, well in this case the reason why this was added was again because
promotions was was created with casinos in mind. I'm going to Scroll
down now to our date format. The overwrite text as mentioned is what's
populated here every Tuesday 12:50. But if I wanted to choose like a start date, start time, end date, end
time, I again have the ability to display the date in different ways
based off the fields I fill out. Description. We can see a description is being displayed here on the
card. And let's see. So our CTA labels apply now. So this here is the
promotions content fragment and we can see how it translates, we how it
translates to the cards that's on the page and. In terms of the actual filters, and sorry guys for for jumping from page
to page, but in terms of the actual filters that appear on top of the
component, let's take a look at how that works. But OK. Here we go. I'm going to open U the new page in the author and I'm
just going to close the component to configure it. Right. OK, so here we have the configurations that could be set with regards to
the filters at the top. We can see here it says select category, which
we are going to correct. If you select one or more, this label will
display depending on how many have been selected. The filter options include category, venue and date range, and so you
can see the different placeholders for each of these different types of
filters that you can put. If, for example, you don't need to have any
of these filters, you can remove. Let's go ahead and remove, say venue for example, and I'm going to hit
done. It will remove that specific filter from the component. However,
one of the limitations that we've observed is currently if you remove
all the filters, that's where this bar is still being displayed. Currently there's no way to to hide that. I'll just hit done so you
can see what I what I'm talking about. So that is that is definitely
one thing that we anticipate we would want to discuss further during the
gap analysis portion. Right now I'm just going to. Put in a filter so we can see how that dislays if only one is selected.

**Lisa Cardia** 40:26 Are the options for the filters, are they hard? I mean managed in the
dam or who's managing those if we did a different option?

**Daniela Tea** 40:26 What? No. Who's managing like like who's adding these options within? So that's
within the component code, like the category, venue and date range as
additional options for filters. It sounds like Lisa you're you want to
know like what if you need another filter added to this? Is that is that
like what you're? Yeah, OK.

**Lisa Cardia** 40:50 Yeah, yeah. Like who would we go to for? Or could an author do that? Or
is that, uh, like the dev team?

**Daniela Tea** 40:56 That would be a dev team update since it's updating the component
itself.

**Mayte Eme** 41:01 So we cannot manage our own filter options.

**Lisa Cardia** 41:01 OK.

**Daniela Tea** 41:05 So the way that this particular component currently works is it's I
believe it is using this hard coded list based off of what we had
captured for promotions. However, again if you guys are trying to say
enhance it in the future to include additional filters. So it's potential that this could be moved to say a generic list which
then could be author managed, but as of right now that's not something
that's available for this component.

**Mayte Eme** 41:32 Yeah, he has to. He has to. We have the ability to manage every single
filter we have on.

**Lucas Nelson** 41:38 Yeah, let let's capture it, Mayte. OK, yeah, I Danielle is just being
straight with what what's implemented right now. I just want to, yeah.

**Mayte Eme** 41:42 Sure. Yes. And I'm confirming we have the ability. So this is a gap. So yeah,
let's move on.

**Lucas Nelson** 41:49 Yeah, sounds good.

**Daniela Tea** 41:53 OK, yes. So looking at at the next field we have our default results
display. So this is just saying if you want to display it by default in
list view or if you want to display it in default by grid view you have
the option to select that. Of course as an end user I'm able to select
between that when I'm viewing on the site. But if you have a preference as an author, you're able to select that
here are clear filters, label text, search placeholder text, which is
right here. Search for promos, no search result text. So if you try to
search for something and it doesn't appear, this is the message that
will be there. And then of course we have some pagination set up. In this case here
we're saying 15 results can be on this page before pagination shows up.
If you need to make it smaller, that can certainly be oops, we don't
want negatives. Yeah, there we go. I'm just gonna put 10 here.
Promotion content fragment based path here. If I want to show by default, if I want to show all promotions that
exist in AEM by not filling this out, it's saying OK, let me just find
all promotions. If I want to filter it to say like a certain specific
folder, I am able to do that by selecting where I want within the DAM. So in this case, I just had my folder for like KT, my folder for
careers, and depending on what I select, this component will just show
the ones that are located within that folder. You can see I left it blank and that's why you're seeing options
listed in here. It's just pulling in anything that's using a promotion
content fragment.

**Lisa Cardia** 43:32 And would that be the same thing? I think we may have discovered
yesterday with events. So if it's not necessarily under the same parent
folder, but we want two category folders, we we can't do that at this
time, correct?

**Daniela Tea** 43:41 Mhm. Right. I think yesterday in the example we were talking about the use
case was like say like something that was like tagged, right? Yeah, in
this case here it is based off of where the folder is located while you.
Yeah, while you can choose like say I wanted, you know all the
promotions here, I I can choose promotions.

**Lisa Cardia** 43:53 Yeah. The main folder. Like casino promotions versus like a hotel promotions, like whatever we
wanna filter it to maybe.

**Daniela Tea** 44:08 Yeah, so if I chose promotions, it would show everything down here. If
you wanted, say, just casinos, you would select here. But say there was
like 4 folders here. You only want to show two at this time. Right now
that is not available. Yep, Yep.

**Lisa Cardia** 44:21 Okay, thank you.

**Mayte Eme** 44:23 OK, so that's another gap.

**Daniela Tea** 44:25 Yep. OK, um.

**Mayte Eme** 44:30 How do you remove the the search field from if I just want the filters
and not the search?

**Daniela Tea** 44:36 Yeah, so so that's not something that can currently be removed. That
along with the filters. It sounds like that that would make sense to be
able to hide say the filters in this to be able to display it as this
list using this component. So search will always show.

**Mayte Eme** 44:53 Oh wait, so if you use promotions, it comes with a filter and a search.
We can't remove it.

**Daniela Tea** 44:59 At this time.

**Mayte Eme** 45:00 So we can't have the promotion cards anywhere else on the page, like a
grid or a carrot, like nowhere else. It has to be with a filter and a
search.

**Daniela Tea** 45:10 So.

**Lisa Cardia** 45:11 That's when we use up the ID, the ID of that CF card, so without it.

**Daniela Tea** 45:13 Yes.

**Mayte Eme** 45:16 Yeah, but that's 1 by 1 by 1.

**Lisa Cardia** 45:18 Oh, like a grid of them or a carousel grouping?

**Mayte Eme** 45:20 Yeah, yeah, because there's no way we're gonna be updating them,
right? Like, oh, this one, it drop off. Now I gotta add another one.
That's gonna take forever plus 24/7 support.

**Lisa Cardia** 45:26 Singular, yeah. Yeah.

**Daniela Tea** 45:34 Hmm.

**Mayte Eme** 45:37 So if we're thinking of using, if we're thinking of using these
promotions thing for hiring events.

**Lucas Nelson** 45:38 What else, Daniella?

**Mayte Eme** 45:46 That that's not gonna work.

**Daniela Tea** 45:50 OK, yeah, so taking some notes down here. So one thing I did want to
point out. So this is also something that I wanted to cover in the. Gap portion because it doesn't exist today. So we do have a content
fragment card list component and the reason why I said this will be
considered a gap is because as of right now we because we were focusing
on. Sites that did not use promotions and this was going to be enhanced
later, but this right now here you can see I'm able to pull in a
specific content fragment model. In this case here it's just using
events. But what I'm saying for a gap, having promotions to be an option here
is something that I believe could be captured. And then what would
happen is you're able to again select from say like that root path or
say from like tags or say a specific fixed list. So instead of having to do things one by one with the content fragment
card, it would display as a list. And so I would recommend like this is
the type of component that I would say would be appropriate for the use
case you were describing. I might say, but the reason why I say this gap
is as you can see right now it's only focused on use and events.

**Mayte Eme** 46:56 Mhm.

**Lisa Cardia** 47:14 I did have a few other questions too. With the promotion search, I
don't know if I saw the option to edit the text that said like search
for promos. Was that in there?

**Mayte Eme** 47:16 Yeah.

**Daniela Tea** 47:17 Yep. Mhm. Oh, that that should be there, yes, as the search placeholder text.

**Lisa Cardia** 47:30 Oh, OK. And 2nd for all of the labels, not the not the placeholder I
guess, but the the the things that are hard coded, how would we be able
to?

**Daniela Tea** 47:35 Uh. OK. Mhm.

**Lisa Cardia** 47:48 Like, uh, change that for a language, let's say so like. We have the option to put the placeholder for for the text, but then
there's certain things that are like hard-coded in that search, such as
filters title, the filter CTA. So like the title above select category
looks hard-coded.

**Daniela Tea** 48:10 Mm-hmm. So hang on. So like you're saying like this particular text
that's here where it says filters.

**Lisa Cardia** 48:14 Yeah, certain elements that I didn't see an option to put a placeholder
text because we have some websites that use language. So if we're going
to like write the language, those words would still be in English.

**Daniela Tea** 48:23 Mhm. So, and this is something where yes, I do want to. This is where I would
ask my my TA tomorrow during my discussion. So keep in mind that what I
understand that there are different languages on the site and we're
using the Transperfect. Plugin in order to have the content display like that. With regards to
the actual components, I do know that our development team does have
specific like language strings, so when they build out the component you
know it can translate based off of. What the site is? I need to confirm though, at least for this specific
example, as well as also just examples in general of what portions of
the component have been captured to be translatable versus what's not.
So I do want to check in with my tech team tomorrow about that Lisa,
because definitely understand that the expectations.

**Lisa Cardia** 49:22 Yeah.

**Daniela Tea** 49:23 If this is used on like say a site that has Greek, this should be in
Greek versus in English, right? So.

**Lisa Cardia** 49:28 Yeah, just want to make sure that at least at the minimum we could
override all of the areas.

**Daniela Tea** 49:34 At least at a minimum to be able to override all of the areas. So out of
curiosity though Lisa, like if like you were using this on a site that
was a different language, how like would you put in I guess like
whatever this would be in that different language?

**Lisa Cardia** 49:45 Mhm.

**Daniela Tea** 49:53 OK.

**Lisa Cardia** 49:53 Every word that's not like a branded term.

**Mayte Eme** 49:55 We.

**Daniela Tea** 49:56 I see. OK.

**Mayte Eme** 49:57 Every everything on our website is manageable, edible, edible that you
can edit. We can edit and you can translate it so we can translate
labels, values, pretty much anything. And Speaking of Greek, we're
actually getting ready to start on our website, so more languages are
coming in.

**Daniela Tea** 50:16 Yep, Yep, understood. Yeah. So let me talk to my tech team during my
sync tomorrow specifically about that. And I'm sure, Lisa, if you want
to go ahead and add the question, that would be great. So then I can
also ask him to respond to it. But we definitely want to get back to you
on how that, how that works, but we won't be able.

**Lisa Cardia** 50:31 OK.

**Daniela Tea** 50:36 To get that until at the earliest tomorrow, so please make sure to add
that question though.

**Lisa Cardia** 50:39 OK.

**Mayte Eme** 50:41 And one more thing, Daniela, just so you know, you mentioned
Transperfect. We do use Transperfect, but not all the time. There will
be a lot of manual translations for specific languages, and I know you
your thing supports it, so we should be OK.

**Daniela Tea** 50:44 Hello.

**Mayte Eme** 51:10 OK.

**Lucas Nelson** 51:11 Daniela, is that topic a CA topic or a technical topic?

**Daniela Tea** 51:11 All right. Um, Yep.

**Mayte Eme** 51:11 So.

**Daniela Tea** 51:15 That's a technical topic, yeah.

**Lucas Nelson** 51:17 So we'll just need to make sure we clue in Maite on technical
enablement. Just a call out for Scott more than anybody. Thanks.

Gonzalo Calasich (SHRSS)** 51:26 I do. I do have a question. Let's make sure when we talk about that,
let's include if the transfer perfect plugin that you guys use will
take care of the labels on the component, the ones that are being done
by developers. The reason being that in in Sitecore every label is
content managed and because it's content managed can be, you know, sent
to the.

**Daniela Tea** 51:27 Yeah. Mhm.

Gonzalo Calasich (SHRSS)** 51:46 Transfer through the transfer for plugin. So just want to make sure that
also labels are considered in that topic when we get there. Thank you.

**Daniela Tea** 51:52 Yeah, absolutely, absolutely, Gonzalez. So we'll take the first pass at
the at answering the question that Lisa has and any other additional
follow-ups. It sounds like we would be able to cover that within the
Transperfect knowledge transfer session. So yeah, we'll make sure that that is addressed. So in terms of the promotions search component, I'm just going to open
this up again if there's if there's anything, any specific fields that
we want to additional clarity on. Is there any more questions though
about either the content fragments or? The component itself.

**Mayte Eme** 52:35 So if I understood correctly, you have to create the. Everything is packaged where we cannot decouple anything from that page
and you have to create the yes, the content framework for a promotion.

**Daniela Tea** 52:53 Mm-hmm. So you create a content fragment for a promotion. Currently the
way it works today is you would either be able to display it as an
individual card by consulting the ID. So you can see here. Yes, you can
decouple it individually. I understand that that's not the.

**Mayte Eme** 52:55 Yeah. With that ID thing, OK. Yeah.

**Daniela Tea** 53:12 Desired behavior. One of the gap items that we had mentioned that we
want to cover in the gap is would it make sense to enhance the content
fragment cart list component? Yep, to include that specific type. And
then the third thing is right now you are able to display it within this
promotion search component, but.

**Mayte Eme** 53:14 Right. Yes. I invest. Yeah. Mhm.

**Daniela Tea** 53:32 It does come along with the filters and the search bar.

**Mayte Eme** 53:35 And in the content fragment, and I'm not gonna go too much into this
because I know scheduling is a gap, but I think I saw some dates and you
skipped them. So I just wanna make sure what do we have start?

**Daniela Tea** 53:38 Mhm. OK, yeah, yeah, one second. Let me. Sorry, I I've lost it. Here it is.
OK, yeah. So this start date, start time, end date and end time. These
are the specific fields that would have displayed in.

**Mayte Eme** 53:49 As well, you've not started. Also, that's not scheduling, that's just a display because we can
schedule for tomorrow, but the date is, you know, three days from now.
We don't have that.

**Daniela Tea** 54:01 Good. This, yeah. Sorry, let me repeat what you said. So if this was, yeah.

**Mayte Eme** 54:13 So let's say the event is this Saturday, right at a, I don't know,
Convention Center in Broward, but I'm going to display it today or
sorry, I'm going to, I want it to be displayed tomorrow and the event
is for Saturday. So basically when we publish it, it doesn't publish based on this date,
it just publishes now.

**Daniela Tea** 54:30 Oh, I see. OK. So this here is a display date is is what is what they're. Yeah, this
here is a display date.

**Mayte Eme** 54:39 OK, OK, so those are display only they do nothing with OK.

**Daniela Tea** 54:45 Yeah, this here is a display day. It's not intentional for scheduling.
There is of course that the scheduling just going to do this. There is
of course the scheduling for now or later with the activation date
that's available here. However, the actual content fragment itself
that's just.

**Mayte Eme** 54:46 OK. OK. OK.

**Daniela Tea** 55:04 For dislay purposes.

**Mayte Eme** 55:06 OK. OK. I got excited and I thought that was the scheduling, but OK,
thanks.

**Lisa Cardia** 55:09 If we schedule it for later and we make an edit to the existing, does
that impact anything or do we it? It will still schedule for later, but
we went back in and we maybe changed the location because they they
moved venues or something.

**Daniela Tea** 55:24 Schedule. Uh, OK.

**Lisa Cardia** 55:26 So if if we went in and changed it from the location saying Seminole
Casino, Brighton Bay or whatever, and because they're like we're gonna
have to have it at a Convention Center nearby, but we've already
scheduled it. What does anything happen if we went back in and edited
the same fragment?

**Daniela Tea** 55:33 Mhm, mhm.

**Lisa Cardia** 55:45 Does it maintain the scheduling or would anything get pushed live?

**Daniela Tea** 55:49 So it shouldn't get pushed live in the sense that I'm trying to see if
I can. We can try and do this right now. Let's.

**Mayte Eme** 55:58 Yeah.

**Daniela Tea** 55:59 Let's see. OK, be able to like show this like right here on the call is
going to be a little difficult just because I'm going to have to save
it the manage publication and then save it again. But we can try it. We
can try to do that, alright.

**Mayte Eme** 56:11 But that's exactly what a user would do, right? What you're doing now.

**Daniela Tea** 56:14 Yeah, no, I understand that. I'm saying for the purpose of the call,
because I know we have some limited time, I do want to make sure that
that we're covering the other topics. But let's see here. Let me see
what I can.

**Mayte Eme** 56:15 OK, OK, good.

**Lisa Cardia** 56:25 If it'll be helpful too, I have one more question on the fragment of is
the promo type. I know we said it was the two options were built with
casino in mind and I don't think you selected one for one of the
examples maybe so it's not required, but are those hard coded? Like how
would we get extra promo types?

**Daniela Tea** 56:34 Yes. Yeah, so right now these are these were determined within, so these
should actually be within the content. You should be in the content
fragment wall to be able to add additional ones. However, that's not
going to be something I think is that's going to be accessible to every
user.

**Lisa Cardia** 56:47 Development. OK, we did take the content model fragment class at least the authors,
but I obviously that's like pretty like extensive I guess more so
related. So I think internally we'd have to figure out teams of doing
that or if that's just something maybe the admin authors get.

**Daniela Tea** 57:01 So. M. OK.

**Lisa Cardia** 57:18 Trained on but.

**Daniela Tea** 57:20 Yeah. So, so just really quick. So when it comes to like the content
fragment models, there is you know the ability to to create your own
like depending on like the permission levels that have been set for
that, right. So like I understand Lisa, like you don't want to open
this up to every single person and and change it. And so that of course
is going to.

**Lisa Cardia** 57:37 Yeah, I don't even want my team to like be responsible for breaking the
like UX of how something was built, but like the options for a field, I
would assume we would have had the capability to making new ones.

**Daniela Tea** 57:41 Yeah. Huh.

**Mayte Eme** 57:50 Yeah.

**Daniela Tea** 57:53 So what I guess what I'm saying is when it comes to a content fragment
model, there's a content fragment model editor, right? In terms of who
has access to that, that of course would be determined based off of like
the user groups and such. However, this is this is. Different from say like adding another field to a component where that
would be more of a developer has to go through that, update the
component, do a code deployment, so that way it would be available for
an author to use. So there is more flexibility when it comes to actually
editing a model. Like a content fragment model, but when it comes to actually editing a
component and adding additional drop down fields to that dialogue
window, that is going to be development work.

**Lisa Cardia** 58:45 Thank you. I guess if you want to continue with the scheduling.

**Daniela Tea** 58:48 Yeah, we let's, let's. Oh, sure, go ahead.

**Don Middlebrook** 58:50 I I do have a question around the asset. So when you pull in the the
asset, so I I see that this looks like it's a one to one ratio the
image when it's in the card. So I know we've asked before about the
dimensions that you know that we should be using for these but.

**Daniela Tea** 58:54 Yep. Mhm.

**Don Middlebrook** 59:09 Let's say I pulled in an asset that's a 16 by 9 and how is that going
to be placed? Is it something that we have to adjust if we want to make
sure the proper area of the image is viewed? On the card, let's say you know the Hard Rock, you know that front arts
all the way to the left or the right of the image. We want it centered
in the card. Is that more of the image position?

**Daniela Tea** 59:36 It. Yeah, so it sounds like what you're describing is actually the like,
for example, say you wanted this to be all the way to the right, right?
Like the guitar itself. Is that so like simple?

**Don Middlebrook** 59:45 Yeah, or or the original image is already to the the side. We want it
centered, right? So somebody pulled in.

**Daniela Tea** 59:52 OK, yeah, so so with I believe pretty much every component that has that
that has like an image associated with it, you will find the image
position tab if what I'm understanding is correct.

**Don Middlebrook** 1:00:07 Mhm.

**Daniela Tea** 1:00:07 Like what you're asking, like if this was set to like all the way to
the right, how would you move this to be, you know, more so that way the
the focal point is changed. And so that's what the intention of this
specific tab was, being able to set the position of the image.

**Don Middlebrook** 1:00:15 Yeah. Yes.

**Daniela Tea** 1:00:26 In both desktop and tablet and then also in mobile. So like you know in
mobile sometimes you might not want it to be that you know that way you
want it to be separate. So that's what this tab is for and you're
going to find that on I think probably every image component. I would
assume the card should have it, which we will find here. Yeah, so any.

**Lisa Cardia** 1:00:34 Mhm.

**Daniela Tea** 1:00:45 Component that has an image will be able to have that. So you can make
those manual adjustments. But when it comes to like say a a list of some
sort, that's not something that's going like this is not going to have
that image position because.

**Don Middlebrook** 1:00:54 I need.

**Daniela Tea** 1:01:01 You're essentially having to change all of the image positions versus
just individual like if you would with the content fragment card. Does
that make sense?

**Don Middlebrook** 1:01:09 OK, then I yeah. But then on the other one, how would we adjust that
image? Is it more setting up the smart crops with dynamic media? How?
How? How would?

**Daniela Tea** 1:01:19 Yeah, so currently at currently right now with with this here you are
unable to adjust an individual row within here, so it would have to be
some sort of adjusting the image outside of this component first,
whether it's with.

**Don Middlebrook** 1:01:20 We go that.

**Daniela Tea** 1:01:36 Say if you do Hotosho and you cropped a specific way, that's certainly
one way to do it, but it would not be within the component since there
is no tab. Yeah.

**Don Middlebrook** 1:01:40 Mhm. Yeah, yeah. I guess my preference is that we would not have, you know, a
ton of duplicate type images. We would use the one source image across
all placements. So I guess that's something we have to figure out.

**Daniela Tea** 1:01:51 Yeah, understood. Yep. Yeah. So I I think and one thing I did want to mention is I know next
week I believe we are according to counter, we are hoping to talk a
little bit more about the dam. I realize that we're going to certainly
want to make sure that we are identifying some of those gaps. Sounds
like you know, Don like.

**Don Middlebrook** 1:02:02 OK. And. Mhm.

**Daniela Tea** 1:02:21 Renditions would be a perfect gap that we discussed as to how it would
fit with the components. These are the exact things that we want to make
sure are documented and captured in the gaps. Because right now here,
yes, you do have the ability to set the image position. We also
understand you might want to be able to have.

**Don Middlebrook** 1:02:24 Yeah, yeah.

**Daniela Tea** 1:02:41 Specific rendition that was made for this content frapping card, so it
displayed that way. So yeah, that's that's the exact kind of stuff
that we want to make sure is captured for that for that gap document.

**Don Middlebrook** 1:02:45 Right. And. OK. Yeah, let's talk about that during my session.

**Daniela Tea** 1:02:53 Yeah, absolutely.

**Don Middlebrook** 1:02:56 Thanks.

**Daniela Tea** 1:02:58 OK, Yep, sure thing. Let's see, where am I? I'm gonna close out on
some of these tabs just so we aren't viewing things that are not
relevant. OK. OK. All right. One thing I I actually wanted to to bring up as we're
talking about job components is I know that there's been a lot of
questions about, well, what if I can I use this on say like another
site? Is it locked down to say just the career site? You know, like how do these components work across different sites? And
I did want to show very quickly, for example, yesterday when we were
talking about say, I'm sorry, two days when we were talking about like
the. The jobs listing and the question was like, you know, I saw, I think I
saw a question on the Confluence page that mentioned can that job
listings component be used on like another site that focuses on on those
specific jobs. And So what I just want to show is like this is an
example of I'm going to show where I got this. There's an example of a hotel site, and so when I say a hotel site,
what I mean is a site that is using the hotel sub theme. It's using a
completely different experience fragment path right for the header and
footer. It's hotel specific to this New York hotel. I'm just going to cancel. So I'm in a completely different location
with an AEM from where the career site is located, which is down here in
corporate and I had created just like a a test page called K Careers
KT. And I'm just going to hit edit. And so if I were to just add say like my job listings component and just
ignore the way that this is looking right now. But what I want to show
is that I'm able to use this component. I'm able to call it a repath.
I think so. I guess someone must have put a UAT testing job here.
That's why this is showing. But I'm able to use this component and then, you know, display it on
other sites. So obviously like with like cleaned up data and such, this
would only display anything that was within this New York path. Same
exact features of how many cars you need, the button label, the default
image just like we had reviewed. Previously, so I just wanted to make sure that you guys are seeing these
components. When we say they're quote UN quote global, yes you can use
them in other places. They will look slightly different based off where
you use them because it's dependent on the theme. So in this case
because I'm using this component. Within this New York hotel page, which is using the hotel theme. That's
why the CTA's look a little bit different than they currently do on say
on this page, right? So that's because it's theme dependent. But I
actually am gonna pause here just to see if there's I see you got off
mute, so I just want to give you an opportunity.

**Mayte Eme** 1:06:00 No, I was.

**Daniela Tea** 1:06:02 Has a question or anything?

**Mayte Eme** 1:06:03 Another question I was gonna say, even though they might look different
because of colors or maybe a few styles, they still work right. They
they wouldn't break or miss something. It's just styling. OK, OK.

**Daniela Tea** 1:06:11 Oh, right, that's correct. Yes, it's it's more of like a the themes
are mainly for styling, right? And also when it comes to the actual, let
me go back here again to the.

**Mayte Eme** 1:06:19 OK.

**Daniela Tea** 1:06:27 Homepage. So you would set the theme. You can see here New York and the
theme is set on specifically for this New York page. If I were to go to
my corporate site and my career site, I should see a different theme has
been applied, right? So it's using the Hard Rock theme, so the theme is
applied. At more like a root level and so then all the child pages inherit that
theme as well as inherits the header and footer and the components can
be used across these different sites even though they're in different
locations and these should work as expected when it's configured.

**Mayte Eme** 1:07:03 But we couldn't, if I remember correctly, but we can't choose
multiple, right? And say, hey, Seminole beam is gonna show from the six
floor allocations. OK, OK.

**Daniela Tea** 1:07:06 Mhm. Can't choose multiple. Oh yeah. So that's what. Yeah, exactly. So
that's why I did want to highlight. Yes, we recognize that part as a
gap. I think we we called out a gap on Monday. But what I wanted to just
show though is that this component we previously I know we were just
following the careers. I don't think right now you guys.

**Mayte Eme** 1:07:15 Mhm. OK. Mhm.

**Daniela Tea** 1:07:28 Doing something like this in hotels because OK.

**Mayte Eme** 1:07:29 We did. We did for casinos. We had a page for Tampa when they were
actively hiring in the expansion of Tampa Hollywood. We had a dedicated
page listing all the jobs for only Hollywood, only Tampa. So this serves
that use case of one-to-one.

**Daniela Tea** 1:07:32 OK. Mhm. OK, I see. OK, I see. Got it. Yeah. So so yeah, I wanted to see if there's actual
specific use cases because I believe right now from what I saw it was
mainly just linking out. But if the need does arise where you need to do
that, you know again for specific sites, you do have that ability to do
that with our components.

**Mayte Eme** 1:07:50 Mhm.

**Daniela Tea** 1:08:00 Yep, Yep. All right, so sorry, slight tangent, but I want to make sure
we address something that I remembered seeing the other day. Any other
questions about the content? I'm sorry about the promotions component
and the promotions content fragment before I move on to some other
items.

**Mayte Eme** 1:08:01 OK. That's good. Thank you.

**Lisa Cardia** 1:08:19 Just from me, I I could be jumping the gun. So if you were about to head
this direction, sorry, what would be the step to see the page of this
promotion card?

**Daniela Tea** 1:08:21 Yes. What would be the step to see the page of the promotion?

**Lisa Cardia** 1:08:35 So like the same way when we just did the events, we saw there was the
fragment, the event calendar and the event detail page. So the promotion
page now what like does this automatically populate a page? How do we?

**Daniela Tea** 1:08:38 Oh. Right. OK. Yeah. So, so in this case here based off of at least what I saw from
the casino site, you are able to, you have to create a new page Lisa to
be able to include, you know it's basically like a content page, right.
And then you would link it here. So that way it would. Be accessible after you clicked on the CTA.

**Lisa Cardia** 1:09:09 But there's no, I guess, template for like, is there a promotion? I
thought we had a promotion detail page in our Um. Options, but maybe I dreamt that.

**Daniela Tea** 1:09:19 Let's take let's take a look. I do not believe that there was one. It
would be the open page template and then creating the content page with
the additional information that's needed on there.

**Lisa Cardia** 1:09:32 OK, so we don't have.

**Mayte Eme** 1:09:33 Oh, so when you create that promo that you show us, that doesn't
automatically create that the detail page you have to that?

**Daniela Tea** 1:09:42 So let's take a look at casinos and I like a real world example of a
promotion that we're seeing right now. If you guys could perhaps guide
me to a place that.

**Mayte Eme** 1:09:53 Oh, but not to go to a casino.

**Daniela Tea** 1:09:56 Uh. The name is better.

**Lisa Cardia** 1:09:59 Well, yeah, because it matters because somebody's a third party.

**Mayte Eme** 1:09:59 No, not any.

**Daniela Tea** 1:10:03 Oh.

**Lisa Cardia** 1:10:04 You can just do Hollywood.

**Daniela Tea** 1:10:06 Hollywood. OK, sure. Oh, oh, it must have. Where's it?

**Lisa Cardia** 1:10:10 Great. Yeah.

**Daniela Tea** 1:10:11 Oh, here it is. OK, Yep. All right. Yeah. Just wanna take a quick look
to see how that's set up right now. And then promotions. OK.

**Lisa Cardia** 1:10:19 Yes. So there's the filter with the cards, which we seem to have similar,
but then the learn more. This is where I was asking what populates this.

**Daniela Tea** 1:10:22 That. Mhm. I see. OK, um, let's. I let me go after this call, let me go down to the dev environment. So
just to be clear, I can keep in mind what we have here within stage. You
know we have migrated over the sites that were for like rollout one or
rollout 7. So there are some there's data. That's not in stage because it's not, it's not ready to go, it
hasn't been looked at, et cetera. So I do want to pull up something
that's down in the integration environment for casinos so I can show
how that particular page is set up for any of these casinos that was
migrated down in the integration environment.

**Lisa Cardia** 1:11:23 2.

**Daniela Tea** 1:11:24 We'll get back to you then on this specific details page when it's
used with casinos. So yeah.

**Lisa Cardia** 1:11:30 Because like since we would have sometimes in this case for careers and
a landing page from the promotion, I also saw on the promotion content
fragment like there was the option for the the banner image. So it's
like if we put that, where is that?

**Daniela Tea** 1:11:34 Mhm. Yes. Yeah, that's, yeah, that's exactly why I want to look at it from the
casinos standpoint because since we're kind of using promotions, you
know, not as like a promotion, but more to handle how these hiring
events are, there are some fields that that aren't really used and
they're not being applied.

**Lisa Cardia** 1:11:59 Mhm.

**Daniela Tea** 1:12:04 The way that they that they would be for a casino promotion. So let me
get an example when it comes to actually casinos. So that'll be
probably more filled out and more you'll be able to kind of see like
how that maps one to one when it's actually used for what its intended
use case was. OK, so like right now we're not using everything that's related to the
casino's promotions because this is not a casino promotion, this is
actually a hiring event. However, what the what the promotions content
fragment does provide is the ability to display this similarly to how it
currently is on the live site. That's the reason why we. We chose it, but we can look at an example, not today, but we can look
at an example later when it's actually used with the intention of
casino promotion.

**Mayte Eme** 1:12:51 Is there anything else or maybe the event template that allow us to link
to another page like because we don't do it often, but we do have. Events that we mark as hot jobs or we have to explain more, even
sometimes we have, I don't know, dealer university, right? Like for
like craps or whatever, whatever. So we have to create these detailed
pages for some of the jobs and it seems that promotions cannot do that.

**Daniela Tea** 1:13:17 So. So promotions. So with promotions, keep in mind, yes, you, I mean you
can create links to pages. You can create a page separately like a a
separate open page and put your details there and then you can link it
within the content fragment here, right? But what I'm hearing Lisa
saying is. Because the way that events work is because you have that event ID,
there's only one event detail page and then it's passing all the
information that's already within the content fragment model, right?
Yeah, so.

**Mayte Eme** 1:13:48 Well, yeah, yeah. I was trying to find a walk around because honestly
the we do it is so easy. We just created one and it gives you the part
integrations page. Everything is tied together. So that's a redo for
later. I was just trying to see. How we can do it what you guys have built already?

**Daniela Tea** 1:14:06 Yeah, so you can certainly do this with events, but keep in mind that
some of like like this override text functionality is not available with
the events content fragment. So if you do have like if you wanted this to have its own separate page,
that would be that would make sense if you want to use your event
component, sorry, the event content fragment. But you wouldn't. This
wouldn't say every Tuesday 12:50 right? Like we saw in the calendar, it
wouldn't say that it would be like whatever the Tuesday date is. And it would say 12:50 and then it would also list out the location
based off whatever was linked. So that's why there are differences
between events and promotions in order to try to get it to match as
closely as possible visually to what we saw on the live site. That's
why we chose promotions. Now if there's I guess like this is where like it perhaps it makes
sense to include like that override field within the events and then you
could use events for hiring events as well, right? So these are all the
things that like we need to make sure is documented so we can identify
that for the gap. Which components need that specific enhancement, right? So I guess right
now, does this cover the workaround for linking this to an existing
page? Right now, as it is, you can link to an existing page. I can click
here and I can choose any page I want, however, to have it similar to
how it is with events. Right now, that's a different content fragment.

**Mayte Eme** 1:15:39 Right. And just to make an idea. Oh wait, we don't even have a
scheduling now, so it wouldn't be. We'll have to get creative and figure it out something.

**Daniela Tea** 1:15:52 OK, so let's let's move on though to a couple of other things that I
had noticed on the career site. And then I did want to spend some time
having you guys if there's any specific pages we wanted to take a look
at. And perhaps investigate those components, but let's take a look at the
video card component. This is used with the testimonials. What I'm
showing here are two different variations of the video card component,
depending on if you fill out specific fields. So I'm going. We need to open up this component. We can see a configuration here. This
has the ability to put the thumbnail. Right now you can see we have
external URL. What we're doing is we are referencing a video that's
within the DAM. However, if I'm not mistaken, I believe during the
handoff of the site. It was mentioned that we do recommend from what we saw, the majority of
videos are I believe in Vimeo, if that's correct. So the recommendation
was, you know, if that's the intention to keep all the videos together,
that should be moved to Vimeo and then this external URL would be
replaced. With whatever that link is. So right now we are pointing to it. We're
pointing to a video that was uploaded into the DM as an external URL.
But moving forward, if you're trying to use external URLs, we would
recommend the Vimeo link instead.

**Lisa Cardia** 1:17:21 So if it's Vimeo or YouTube, we just take the the URL path from the
browser. That's what.

**Daniela Tea** 1:17:24 Mhm. That. That should be here, yes. Like you can see here this is referencing like
the specific file dot MP4. Yeah, sorry, go ahead.

1:17:31 Yes.

**Mayte Eme** 1:17:36 Most of our business are in YouTube, so when you say we recommend, you
know, so that's fine, OK.

**Daniela Tea** 1:17:37 On YouTube. OK. Oh, sorry. I think what we saw was like, we were seeing
videos in Vimeo on other sites, other hard work sites. But you're
saying YouTube, it doesn't actually matter Vimeo or YouTube. It's just
since that's external. Yeah, yeah, you know, it wasn't like a
limitation of that. I was using Vimeo because that's what we were
seeing. Yeah.

**Mayte Eme** 1:17:49 OK.

**Daniela Tea** 1:17:56 OK, so in this case here what you will notice is I've left the video
title and the description blank and so you'll notice in this version
I'm going to hit cancel. There's nothing that's appearing underneath,
but in this version here I did fill out the title.

**Mayte Eme** 1:17:57 Yeah.

**Daniela Tea** 1:18:12 And also the description. And so that's how it's being displayed here.
So with with title and description without title, that's just depend on
if you fill out those fields. The close button label is something that
will appear when you actually open up the video and that's what appears
in the top right in that Moodle. So, so that's here and then. Let's see. Let's take a look at how that looks like on the publisher
side. Alright, so I'm just gonna click on like something like this. So this
is where we were saying that the close label is appearing here. So that's where that translates to. And then for the Watch More
testimonials page, you can see here how we were using that video card
component with the descriptions filled out. I'll pause here to see if there's yeah, go ahead, Lisa, please.

**Lisa Cardia** 1:19:02 Yeah, all right. I have a list of questions because I've tested this on
my own. So we we definitely skipped around on a lot of the controls of
the video. So if you went back to your external URL, so now that we know
we can reference a video that's in the dam, Vimeo or YouTube, I saw you
had a with it.

**Daniela Tea** 1:19:13 OK.

**Lisa Cardia** 1:19:22 There. Is that the recommended width or why do we have 846 there?

**Daniela Tea** 1:19:26 So I yeah, so I had I copied this specifically from the existing one
that was listed here. Let's go ahead and change that and see what
happens.

**Lisa Cardia** 1:19:38 And so we don't need like a pixel or anything there, it just accepts a
number.

**Daniela Tea** 1:19:43 Let's do something small and crazy to make sure I believe with the
let's see.

**Lisa Cardia** 1:19:50 I believe it only impacts the modal, but.

**Daniela Tea** 1:19:52 Yeah, that's that's what I was about to say. Like you can see how the
modal got super small, right? And one thing I did want to mention is the
videos do work when you're viewing them on the publisher. When when
we're viewing trying to view like a damn video within the. Author. That's why you're seeing it's not, it's not going to play in
here, but it is something that's visible when you're viewing on the
publisher. But yes, so that width that we just inputted, you can see how
that affected the modal window in terms of like the 8:46, that is
probably something that we were putting to match whatever we saw on the
live site, but that can certainly be changed. Changed.

**Lisa Cardia** 1:20:28 OK. But no pixel required, just the number. OK. And then moving down,
unless you plan on showing us the third party, but there was the options
to do a fixed layout instead of responsive. It was like there was like
fixed layout versus responsive and I think that's if you choose.

**Daniela Tea** 1:20:30 No pets will require. That's correct.

**Lisa Cardia** 1:20:48 Choose the third party. You have these options like you just have very
very different options than what had existed and then it it asks you for
like a a aspect ratio, you know all of those natures.

**Daniela Tea** 1:20:50 Oh, right. I see what you're saying, yeah. So I think you might be thinking about the video component. So with the
video card. Oh, no, I'm sorry. I apologize. You're talking about like
after you select the. Yeah. So this is gonna be very similar. Yes,
correct.

**Lisa Cardia** 1:21:14 This was from selecting third parties so.

**Daniela Tea** 1:21:17 Yeah, so with regards to this, you can see here the video ID. Let's
switch to YouTube since you guys were mentioning YouTube. So the video
ID is that the string or whatever that's at the end of the video, so
that can be inputted here, right? So that way we would just reference
that specific YouTube video here with the layout fixed or responsive I
can. You can try and look for examples where we're actually using this so
you guys can see how it works. So I can pull that off to the side and do
that. But yeah, what this is showing here is you're able to add those
specific. I guess you can configure it so that way it's looping. I
believe we're using that on the homepage for example. Ability to loop this video for it to be able to play without being
muted. It's auto playing, right? So that's what was used in order for
this particular video to be shown. This is using a container. However,
anything that's using a video is going to be very similar to these
specific fields. That's why I'm. Referencing this, um, but these are things that would be configured by
the author and then this. That's how it's like rendering on the page,
right? So this.

**Lisa Cardia** 1:22:26 But those options are only available if we went with the third party.

**Daniela Tea** 1:22:29 If you click on third party, yes the video.

**Lisa Cardia** 1:22:32 So we can't do that. Like I guess I don't understand why we would put
a YouTube link on the external URL with the first example when this is
asking for YouTube as a third party.

**Mayte Eme** 1:22:33 Oh.

**Daniela Tea** 1:22:41 Yeah, so so to be clear, external URL could be if it's something
outside of what's listed in here, then that's when you would use this.
You can't. What I'm trying to highlight is yes, you could
theoretically still use a YouTube URL here. However, when it comes to. Additional features, then yes, it could certainly make more sense for
you to be able to select YouTube from the third party drop down if you
want to have access to all this additional stuff. However, if your
videos were not hosted on YouTube, external URL is what is available for
anything that's not hosted outside of these.

**Lisa Cardia** 1:23:17 But we couldn't do this the configurations with like a hosted internal
video. Sorry Mayte.

**Mayte Eme** 1:23:18 So.

**Daniela Tea** 1:23:22 Into the.

**Mayte Eme** 1:23:22 No, I was going to say the same thing, Lisa. It seems that with external
we missed the configurations that we have on third party. They should be
the same. So that's another gap and that means that we only have to use
YouTube or Vimeo their private.

**Lisa Cardia** 1:23:32 Yeah.

**Mayte Eme** 1:23:40 Otherwise we won't have controls.

**Lisa Cardia** 1:23:45 Yes.

**Mayte Eme** 1:23:48 So OK, yeah, so let's just not use external URL until that's fixed.

**Lisa Cardia** 1:23:53 And then yeah, definitely a take away to let us know that if we were to
use the fixed or responsive, what like our best practices for those like
fields that are included. But if you don't have an example now, I
don't want to waste the time. And my only other question was related to
styling. So if you were you showed us how they looked on on the preview,
but just to see the difference between.

**Daniela Tea** 1:24:02 Mhm. Mhm.

**Lisa Cardia** 1:24:13 None black and white is none is the default. So is that transparent I
guess?

**Daniela Tea** 1:24:15 Oh, right. So let's actually, I'm going to just copy this three times and I'm
going to just put a background color on just for the ease of us being
able to see this, right? This looks absolutely terrible, but let's. Let's set this to be white. Let's set this to be black, and let's see
what happens here. Oops, did I set that white? Interesting. All right, so here you can see the black is showing up on
on on top of the container with the background color, and so it's not
transparent. The white one I'm going to look into because I feel like I
have seen that working. I'm not sure what's going on here, but the
intention is for this to be a white background. Right with the light with the dark text on top of the light background
and then I think by default nothing is selected. And so once we check to
see and understand why white description is not showing on the
background as white, I can get back to you as to whether or not this is
transparent or not, cuz right now it's showing as transparent, but I
need to. Confirm what's going on with the white description.

**Lisa Cardia** 1:25:28 OK, I've gotten the white to work before so I have seen it in action. I
just I just don't know if if not selecting means default is
transparent.

**Daniela Tea** 1:25:31 Yeah, that's that's what it exactly. That's why I'm surprised by
this. Right. No, definitely understand. But yeah, let me look into this, Lisa,
because like I like you're saying the white should be working. I'm not
sure why it's not working right now in this instant. But yes, I can
show a screenshot of actually of the of the three different ones once I
can understand why this is. View uh displaying those this way.

**Lisa Cardia** 1:25:57 Thank you.

**Daniela Tea** 1:25:58 Yep. Um, OK. So 'cause I'm seeing the time I did one. Yeah, go ahead.

**Mayte Eme** 1:26:03 Um. One more question, we how does this work with this component? If I had a
fourth one automatically turns into a carousel like sidecore? Or is
there an extra step to make it agree, agree that it stacks or a
carousel? Because we just got to like click one thing in sidecore and I
didn't see that in the settings.

**Daniela Tea** 1:26:23 Yes. So this particular component it it's.

**Mayte Eme** 1:26:24 Yeah.

**Daniela Tea** 1:26:29 So it's one component that does not automatically go into a carousel.
We do have like card carousels and we have our hero carousel which does
allow you to, you know, do things like add other components to them and
and so let me actually show you. For the video card though, I don't believe that's something that we
are currently adding to carousel, so it might not be an allowed
component. Yeah, so in this case for the card carousel, we had limited
just to cards for the. Hero carousel that was limited to. I'm sorry, one second. Let me get
out of the carousel component. Yeah, for the hero carousel component. I believe we had limited that to just hero banner image and video. So
notice this is not the video card component. This is a different
component. The video is more of a video player. That's what we see
here. This is the video player being used within a hero banner. So right
now the video card component on its own. It does not turn into a carousel. What what I would recommend perhaps is
like say like a gap is with our existing carousel components, perhaps
allowing those video card components to be added to them since right now
they are limited to only specific components and that was by design.

**Mayte Eme** 1:27:51 OK, so yeah, let's component turns into carousel and obviously
everything right, like navigation and things like that. But any any card
can go into a grid that is taxed and is responsive or turns into a
carousel if that's configured when more than you know, three or four,
whatever the.

**Daniela Tea** 1:28:08 Mhm.

**Mayte Eme** 1:28:09 The um, I think I accepts.

**Daniela Tea** 1:28:15 OK. And so the the last thing I wanted to to just show before we start,
if there's anything else that we need to pull, which is that I also
noticed that for this particular site we were using the card component. And again, that's been used obviously everywhere throughout all of the
sites. But in this particular instance, this card, what I just wanted to
highlight, you can see the title bonus programs and you can see the
asset here. This particular card is just using the icon card variation.
That's why it's displaying. Like this, if I were to turn this off, it'll look something like that,
which is not what was matching on the live site. And so I just wanted to
highlight how this particular variation was being used on this site with
the cart component that I know that the authoring team has already used
in several places.

**Mayte Eme** 1:29:07 And if I add again like I'm not gonna ask about the carousel, but how
does it respond if I have like 6 or 9? Does it go like 3 to 1 columns? I
mean automatically or is that a setting? Because I remember from when we
looked at the other sides we have that issue right that you have to
manually go into every little thing and configure how it looks on each
break point.

**Daniela Tea** 1:29:28 Right. So for this particular component, because keep in mind this is
kind of like a standalone component, like you could make this as wide as
you wanted, you can make this as small as you wanted. And then with the
way AEM works, you would basically have to change it in the different
emulators. Now what we understand and definitely understand what you're
describing my table. I know some of our components will automatically do that for you based
off of like say like a carousel. You have the ability to be able to say
all tablet carousels. I want two cards to be displayed, etc. That's
some of that functionality is built in existing components, but
something like say like a card that's. A standalone component. It's not being used within like this carousel
and so this here you would have to manually size it deending on how you
want it within the different viewports.

**Mayte Eme** 1:30:22 OK, so we'll add to the God list.

**Daniela Tea** 1:30:26 OK. So with what we covered here, excuse me, this is was I was going
through the career sites. I know we want to focus on careers and I was
just taking a look at at the things that we have on the careers that we
hadn't really talked about. Is there any specific page that the team
wanted to take a look at and perhaps take a look at? Configuration and talk a little bit more about it.

**Mayte Eme** 1:30:49 We have a page where we list our executives. I think I forget the page,
but that is the same content as that we have in hardrock.com, right?
Like the brand side. So I'm assuming that shirt, right? If we change it
on.com careers automatically.

**Daniela Tea** 1:30:56 OK. Oh. OK.

**Mayte Eme** 1:31:09 Updates.

**Daniela Tea** 1:31:11 So it can't. Sorry, what? Maybe it's here from our team. No, that's
that's not it.

**Mayte Eme** 1:31:12 I'm gonna try to find that, yeah. Any inclusion?

**Lisa Cardia** 1:31:18 Yeah, I was gonna say it might be the diversity.

Lyon, Rick (Director of Digital Experience)** 1:31:18 It's the corporate page on hardrock.com.

**Lisa Cardia** 1:31:21 But the one that's uncovering yours, which one is it here?

**Mayte Eme** 1:31:22 And it's.

**Daniela Tea** 1:31:24 Oh yeah, I'm looking for the one in careers, so um.

**Mayte Eme** 1:31:27 I think inclusion.

Lyon, Rick (Director of Digital Experience)** 1:31:27 Oh.

**Lisa Cardia** 1:31:27 Yeah, I think it might be the diversity, equity and inclusion. Yeah,
yes. So these are the same cards.

**Daniela Tea** 1:31:29 Question. OK, perfect. OK.

**Mayte Eme** 1:31:31 Yeah, that one. So we don't have to maintain it in two places, right?
If you know like Jeff gets another title, it just automatically it's on
both sides.

**Daniela Tea** 1:31:40 So right now I believe it was probably migrated over separate cards. We
can take a look. However, that can be changed, but let's pull up this
page. I think we said divert. Wait. Oh, inclusion. OK.

**Mayte Eme** 1:31:59 Inclusion.

**Daniela Tea** 1:32:03 OK, here it is. Got it. All right. I believe right now these are
probably using card components, right? OK, yeah, so these are using card
components. However, keep in mind these can be moved to experience
fragments. Definitely understand the desire to have that shared content.
Let's. Bring up the Hard Rock website and I'm. Is it corporate? Is that the like the corresponding? OK, yeah, OK, so.

**Mayte Eme** 1:32:32 I think so.

**Daniela Tea** 1:32:37 Oh, looks like some images are a little bit different. Not sure if
that's intentional or not, but if what's pretended is a one for one,
it's completely the same, right? Let's pretend it's completely the
same. What we could do, like what could be done? Get this be shared and you can be moved into Experience Fragments
instead. So that way you are updating it in one location and keeping the
exact same styling for both sites. So if you were to upload say the text
here, say David like you mentioned got a new title or something, you'd
update it in the Experience Fragments section and then it would update
on. Our page was referencing that experience fragment. So this here would be
moved to the experience fragment. This here would be replaced with the
experience fragment. So it's using that shared source and then you as
an author would just update it once. Does that make sense? So right now, as you can see here, these are using just cards, just like
these are likely using just cards or or some other components, but if
the desire is to have it to be shared across both sites with the exact
same styling. And the exact same like data, then that is a perfect candidate to be
moved to an experience fragment instead.

**Mayte Eme** 1:33:57 When you say exact styling, just to understand how Adobe works, if I do
an experience fragment and I want the same content on two or multiple
sites, it has to have the same styling. It can be it's the content the
same but the style apply different per site.

**Daniela Tea** 1:34:09 So. Yeah, so keep in mind. So that the reason why I was emphasizing the
styling is because that's when experience fragments, you know, having
it look exactly the same and and with the same content. However, if
you're just trying to have the same content, that's where it goes
candidate for content fragments instead, right? That's why I wanted to
understand like. Like, are we trying to have like, you know, because I notice, you know,
pictures a little bit different. Not sure if that's intentional or not.

**Mayte Eme** 1:34:36 You. For this use case, like you're right, it should be the same, exactly
the same. I was thinking of already other use cases where they are not
exactly the the content is the same but not how it looks.

**Daniela Tea** 1:34:43 OK. OK. Yeah. OK. Yeah, yeah. So whenever you're trying to have shared content, say a
name, we know that we have a name and we have a title and we have an
image, right? That is a content for a, sorry, that's a candidate for a
content fragment model. Say those exact fields where you're able to
then save that into that location and then. Edit it as a content fragment. You would then use like our content
fragment card component to to display that specific content fragment,
right? However, because we're saying I want this to be the exact same
on both this site and this site, that's to be done inside a content
fragment. That's not like an experience fragment and then you would
edit. One experience fragment and then it would update on both sites.

**Mayte Eme** 1:35:34 OK. Thank you for that.

**Daniela Tea** 1:35:36 Yeah, and I'm sorry if that was a little confusing. We can certainly
get more into experience fragments, which is the intention in a future
session, you know, kind of seeing examples of where we are using
experience fragments on existing sites as well as perhaps some
additional use case candidates that that would make sense. Like this is a perfect use case for experience fragment. We're trying
to do the exact same thing, but that is going to be covered. I believe
if not next week, the week after I need to check the agendas. So just to
be clear, we are going to be talking more about experience fragments.

**Lucas Nelson** 1:36:08 Yeah, Daniela, one of the things we'll do tomorrow is send out what
what the agendas are now that we've kind of amended the plan, right.
So, yeah, so that'll be something I'll see tomorrow, yeah.

**Daniela Tea** 1:36:19 Oh, yes. Yep. Mm-hmm. Yeah, we'll be working on that tomorrow. That's correct. Yep. So I
think might say in team, any other pages we wanted to take a look at
that's in careers, you know, perhaps take a look at behind the scenes
as to how we are rendering it.

**Lucas Nelson** 1:36:23 Yeah.

**Lisa Cardia** 1:36:36 I do want to, I I know I sound like a broken record for probably a lot
of the components we've covered, but I do want to call out that like
for the video card or for the promotions or everything of that nature, I
will document again to say what is the asset necessary for this because
like for the video card, I think that there was like.

**Daniela Tea** 1:36:45 Mhm. Mhm. Yes.

**Lisa Cardia** 1:36:56 Like a the or I forget the the word you used for it. I'd have to go
back to my notes. Let me see video card thumbnail, the thumbnail. So
it's like what? What size is necessary for the thumbnail? I know I just
saw like a recommended size you put maybe for the video, but like.

**Daniela Tea** 1:37:06 So I get the the the yeah, the video thumbnail.

**Lisa Cardia** 1:37:14 It's not really universally understood what would be necessary for that
image right there. And then same thing with that image. A video card
doesn't have the same capability of where we were able to like give it
a focal point I guess. So like to me this one would be important to just
know what's the aspect.

**Daniela Tea** 1:37:19 Yes. Mhm. OK.

**Lisa Cardia** 1:37:31 So that there's no mess ups there. Um. I'm trying to think what else. Obviously same goes for promotions, just
wherever there was like a a banner image field or a promotion card
image. Just knowing again the the basis that's really gonna get us in a
standardization. Good point. You know, just at least implement that from the as we are
dictating what the card looks like versus the card containing in.

**Daniela Tea** 1:37:51 Yeah, yes. About the assets and we want to continue putting that down, you know,
from a component basis. We understand that the fact that this does not
have like say like an image tab or something new feature. You know, documenting all this on process to review during that.

**Lisa Cardia** 1:38:34 Yeah, and it kind of like an overarching theme. Updates to pages and I'd say this might not be as relevant to the
content fragments because I can see how they're stored in the back end
and either published or unpublished. But we're having a lot of issues
when we want to have something added to this page. Let's say it is the
video card.

**Daniela Tea** 1:38:49 Mhm. OK.

**Lisa Cardia** 1:38:55 If we want to keep that another video card on the page, but someone
tells us George isn't with the company, take it down, but then we want
to. I guess that's not the best example. George isn't coming, is
coming down this week, but we want to add George back next week. It's a
pretty big effort to create it, get it sized, get it formatted and
delete it versus at least storing it. On the page level, maybe hidden on the back end. Do we have any sort of
functionality like that? Because we come across that with like the
homepage heroes that constantly get rotated out. Sometimes we'll have
something very temporary go up, but we want to revert back to Evergreen
and not just make like a. It's more so being able to go to basically the component level and get
it stored to the page, but it's not saved on the actual page layout,
but more so in the content tree, so we can always access it from the
tree if necessary. I I know we do that a lot. And then without having to say what did that look like, like do we need
to recreate it? I hope I'm like saying that correctly because that's
like most components that we're having an issue with of like what we do
currently day-to-day. It's really easy for us to grab things that are
just more so disabled or unpublished from the component level.

**Daniela Tea** 1:39:55 Mm.

**Mayte Eme** 1:39:56 Mm.

**Daniela Tea** 1:40:05 Mm.

**Lisa Cardia** 1:40:12 but still stored in the tree.

**Daniela Tea** 1:40:12 Mhm. OK, yeah, I.

**Mayte Eme** 1:40:15 And then, as you know, we do that for everything, for pages, for vans,
for promotions, for cards, for literally everything. We just leave them
there because we know we're gonna reuse them.

**Daniela Tea** 1:40:21 Yeah. Yeah, understood. Um, So what I wanted to actually show.

**Lisa Cardia** 1:40:28 Yeah.

**Daniela Tea** 1:40:33 We'll see. So there's promotions component that's on here. However,
you'll notice that it's actually hidden. What I did was I had layout
and it's. You'll notice that there says hide component.

**Lisa Cardia** 1:40:50 Oh, OK.

**Daniela Tea** 1:40:51 I believe that's what you're asking for, Lisa. So like. OK.

**Lisa Cardia** 1:40:57 It. Which? Something like that exist. I just would hope that that I exist in every
component or is this like?

**Daniela Tea** 1:41:02 Hello. I mentioned perhaps a specific card with it. This is at a component
level like this particular feature on this. I did a link on the layout
and I clicked on the eye and what that does is that. We'll hide component from. Or like you know this, this would come in handy to be able to dictate
what's actually shown in a different device. But what it sounds like
you're asking for is so you wanna hide on every single device. Well,
you can actually do that by using this the same functionality just
hiding the component. But it would still be accessible to tree so you can see I had hidden my
title permissions. If I click on it you are going to see it because
it's hidden, but when I if I go through the layout I'm able to
actually unhide. I did again, right?

**Lisa Cardia** 1:42:10 But it would have to be done across break points.

**Mayte Eme** 1:42:10 OK, so that's one like a CSA's hide. It's still rendered right? And
like you can get crawled and picked up. So it wouldn't have a use case
because when we hide it in cycle, it doesn't get into the HTML, it's
actually gone. So that's.

**Daniela Tea** 1:42:29 Let's see. Yeah, one second. One second. One second. Let's take a look
at.

**Mayte Eme** 1:42:32 You can go.

**Daniela Tea** 1:42:39 One second. Let's take a look. Yeah. So to Majay's point, like you can
see here, the title is still. Yep. Sorry, Majay, you're you're
breaking up. What? Sorry, what was that?

**Mayte Eme** 1:42:43 And also we have to. Sorry, I was gonna say that the amount of that we have like let's say
disable or unpublish, it's not the amount. So hiding, hiding like that,
it's it's not. I mean it might help us Lisa for like a quick fix for
something really urgent, right? But it doesn't have. A long term.

**Lisa Cardia** 1:43:07 Right. I didn't know it was gonna be like in the code.

**Mayte Eme** 1:43:12 Yeah. Because it takes so much manual labor and energy to create something in
Adobe, we don't want to lose those components. That's why we're
asking if we can like store them somewhere so we don't have to recreate
it and spend all the time to accomplish, you know the.

**Daniela Tea** 1:43:36 So it's yeah. So out of curiosity I guess let me because I'm I'm
trying to like process the use case. So it's a concern like I have an
entire layout and now it's like I need to hide certain things.

**Mayte Eme** 1:43:36 The look that we.

**Daniela Tea** 1:43:55 Are you guys talking about perhaps you know like?

**Lisa Cardia** 1:43:57 The the use case could be for example we we push a hero banner to a page
and and the campaign that we're running or push like for a hiring
event. And when we don't have a. We might want to swap that back out to generic, but the generic is set
up with a description, not just like a like zero. So there's already
like.

**Daniela Tea** 1:44:15 OK.

**Lisa Cardia** 1:44:31 We want to like reset up knowing it's just like an Evergreen content,
but we don't necessarily have like scheduling either to say it's going
to be following a very consistent schedule to say make it appear on XY
and Z date. It's kind of like at the request of a stakeholder. So we won't, we wouldn't. We just want to have that evergreen content
available to repurpose in a lot of areas. But that's like my best case
to say.

**Daniela Tea** 1:44:52 Mm.

**Lucas Nelson** 1:44:54 Can you? You know is that. Sounds target a little bit, but maybe not. I don't, I don't know, you
know, maybe if there was a.

**Daniela Tea** 1:45:02 Yeah. But.

**Lucas Nelson** 1:45:07 We if we change the the content architecture too, but I'm just trying
to. That's what I'm hearing. Yeah, you go ahead.

**Mayte Eme** 1:45:15 OK.

**Lucas Nelson** 1:45:29 And.

**Daniela Tea** 1:45:29 Yeah, for sure. And so I I understand the use case that you're
describing, Lisa. I think we need a little bit of time to kind of digest
that and also some time to sync with the tech team tomorrow to see if
perhaps, you know, they have some suggestions as to how we could handle
that.

**Lisa Cardia** 1:45:45 Yeah, cause just like as we're evolving as a team, part of our
initiatives this year have been really to to emphasize like content
refreshness. So like so in order to do so we we're rotating out very
temporary things, but when we don't have temporary things to to push
then we want to be able to rely.

**Daniela Tea** 1:45:48 Mhm. OK, OK.

**Lisa Cardia** 1:46:05 Back on the Evergreen. So it's not like, as easy to say, we're always
following a very standard schedule. So like, I don't think it's just
as as much of targeting at a time being, but being able to default back
to saved elements that aren't just fragments.

**Daniela Tea** 1:46:10 Go ahead. Hmm. OK. All right. Yeah. No, we we will be reviewing this tomorrow
during our discussion. See if we can.

**Lucas Nelson** 1:46:32 Well, either way, I think I don't know if we'll have to be an answer,
but we're hearing the need as part of this like initiative and vision
that Lisa.

**Daniela Tea** 1:46:33 I'm hoping last of these days. No, no.

**Lucas Nelson** 1:46:43 Sent their team, you know, refreshing content. That's good to hear that
like kind of anecdote at least I can. So my point is I don't, I don't know if an immediate answer but we but
we definitely want to consider that when we're talking in going through
our backlog expansion platform expansion discussions. So we're
accounting for that with any future work that we're doing to improve
the plat. Form as it's implemented. So yeah, alright.

**Daniela Tea** 1:47:09 Yeah, yeah. Luke, I guess what I was trying to stress was if there is
something that we can do currently today with the platform, we would,
yeah, certainly, yeah, certainly we want to present that. But to your
point, after our discussion with our tech team, that might have to be,
you know, either like a modify or or something that's completely new.
So yeah.

**Lucas Nelson** 1:47:14 Oh, sure. Yeah, yeah. I don't wanna shortchange that. Yeah, yeah.

**Daniela Tea** 1:47:29 Yeah, we'll definitely learn more after we talk tomorrow and then we
can certainly cover this again in in in our later. Yep, exactly.

**Lucas Nelson** 1:47:29 Yeah. OK. Figure out where it goes. Yeah, right. Yeah. OK.

**Lisa Cardia** 1:47:38 Thank you.

**Daniela Tea** 1:47:39 Yeah, thanks, Lisa.

**Lucas Nelson** 1:47:39 Daniela, I I feel like you're you're you're you're about out of
words here, but our team are there.

**Mayte Eme** 1:47:39 Um.

**Daniela Tea** 1:47:44 My God.

**Mayte Eme** 1:47:44 I we I do have one last question. The locations page in the careers site
is pretty much the same information as the brand site. So I'm assume
that's the same right? Careers is pulling from the DPLD.

**Lucas Nelson** 1:47:48 No problem.

**Daniela Tea** 1:48:00 Let's take a look. I believe this is actually not pulling in from DPLT.
Sorry, I'm just sharing the screen. You're talking about this page
here.

**Mayte Eme** 1:48:09 Yes.

**Daniela Tea** 1:48:10 And this is the same page. Let's find it on the Hard Rock website. One
second. Um, can you navigate me to the?

**Mayte Eme** 1:48:22 Yeah, go to find the location top left in the in the belt on the top.
Yep. So if you scroll below below, that's obviously organized
differently, but it's the same information. So if we have the same
information.

**Daniela Tea** 1:48:25 Oh, Yep, sure. OK. So.

**Mayte Eme** 1:48:37 I assume it was the same component.

**Lucas Nelson** 1:48:40 Mm.

**Daniela Tea** 1:48:41 No. So I believe the way that this is migrated is using accordion and
text components. This here is using a different component which is
connected to the map. I guess my question for you though is like is the
is the intention for it to actually be organized in this way to
essentially reuse what we see here?

**Mayte Eme** 1:48:59 Not organized, but the idea of integrating with the DPLT is that
everywhere we have a listing of locations like that pulls from the DPLT,
so we don't have to maintain it in different places. We don't want to
be maintaining locations, their links, their name changes and all that
stuff. Manually across multiple sites as we keep adding sites to this. So is are we able to grab that accordion from the brand side and put it,
not move it, but copy and have the same in the career side?

**Daniela Tea** 1:49:32 So you can certainly copy the component. I do believe this component is
linked to the map, but we can.

**Mayte Eme** 1:49:39 But that's fine. We can have, we can have the map.

**Daniela Tea** 1:49:43 OK, uh, actually, but I'm one second.

**Mayte Eme** 1:49:48 I mean, to be fair, they actually wanted a map the first time we did it.
We just didn't have enough resources to, you know, like actually do
that work. So we ended up doing just unlisting in Accordions.

**Daniela Tea** 1:49:59 Right. So and and I think that's the reason why it was probably
migrated over that way. But if we were to go to the, excuse me,
locations page here, we can take a look at what that component is. To
your point, Mayte, you're saying, can you just copy it? So you'll see
this is our map component and the reason why you're like, why is it a
placeholder? If it renders an author, it's probably going to slow down the page
significantly. However, this particular component contains all the
different map data, right? You'll see the different group titles, et
cetera, and then it's pulling in the different countries, which is then
this particular component is linked to the content fragments that are
being created from DPLT, right? Right, so you could take this, you can copy this and then you can put it
on the page. Right now I'm gonna put it just on my test page because I
don't know the exact page where it's there. Oops, my bad.

**Mayte Eme** 1:50:49 Mhm.

**Daniela Tea** 1:50:53 Yeah, so you should be able to copy the component and then display it
within a different page because again, these components are global,
right? So yeah, yeah, yeah, let's see if I why does it keep copying
this?

**Mayte Eme** 1:51:02 That's good.

**Daniela Tea** 1:51:09 I'm going to do that and then I'm going to actually because I see a
time, but I'm going to do that. I'm going to post it here and I'm
going to actually ask Luke to send out the page once it's available.
OK, if that's if that sounds good, so you guys can see how it's the
exact same copy of that specific component, OK.

**Mayte Eme** 1:51:17 OK. Yeah. Thank you.

**Daniela Tea** 1:51:26 Alright, yeah, I will stop sharing then. And Luke, yeah.

**Lucas Nelson** 1:51:27 It. Yeah, I I I got just a couple minutes and then I'll let people go. Just
pulling the calendar back up and again, this is published on on
Confluence. I'm sharing my screen, hopefully you see it. So just wanted
to call out that. Tomorrow's session I I I had the intention of having the Friday session
this week. We're gonna we're gonna postpone it and and move sessions
to next week and have a Friday session next week. We we want to have a a
pretty large post-mortem. Internally here, retrospective and and and use the time to collate what
what we've, what we've gone through the last three days, go through
the questions that you guys have had, make sure we have a buttoned up
agenda for next week. So that's why we're going to use the Friday time
for that. So you'll be seeing a calendar update from me for the Friday session
tomorrow and I'll be sending, well, Daniela will be sending. Well,
actually it'll be a mix of Daniela and Andy will be sending the agendas
for next week and I'll be setting up the time blocks. The one to three time period Tuesday through Friday and just want to let
everybody know this that that little bit of housekeeping for me. So
hopefully that makes sense. That's all I had. So thanks for your time
Daniela, as always, I appreciate. The diligence that you put into these knowledge transfer sessions with
everybody, I appreciate everything you're doing, OK.

**Daniela Tea** 1:53:02 Sure. Thank you.

**Lisa Cardia** 1:53:05 Thank you, Daniela.

**Daniela Tea** 1:53:05 Thank you everybody for your participation.

**Mayte Eme** 1:53:06 Thank you.

**Don Middlebrook** 1:53:08 Thanks.

**Lisa Cardia** 1:53:09 Thank you.

**Scott Sorel** 1:53:09 Yeah. Excellent. Thank you.

Lyon, Rick (Director of Digital Experience)** 1:53:11 Thanks everyone.

**Mayte Eme** 1:53:11 Thank you.

Gonzalo Calasich (SHRSS)** 1:53:12 Thank you. Bye.

Lucas Nelson** stopped transcription



## Session: Tagging & Taxonomy — 2026-02-17

**SHRSS Adobe Knowledge Transfer - DAM Sessions-20260217_130312-Meeting
Recording**

February 17, 2026, 6:03PM

1h 2m 28s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:08 Alright, we're off and running on the recording. Andy, if you wanna go
ahead and brief the team on what today's session's gonna be about,
that'd be great. Thank you.

**Andy Lambert** 0:17 Sure. So for today's KT session, we're going to talk about all things
tagging and taxonomy as it pertains to tags and AEM. So it's actually
this. This session will not be 100% or even close to 100% focused on the damn,
though I think that it's critical that Don be here as well as your
authoring folks and anybody else that would be have an interest or stake
in understanding how tagging works as it applies to both. Both sites and offering. So if you wanted to, you know, forward the
invite or just shoot anybody a quick message on teams to have them join
them, you know that would be. Recommended sure, but we'll also have the recording, so anybody that
wants to go back and and check it out can. Now do we do we want to take a minute to invite anybody else or can we
go ahead and get started?

**Don Middlebrook** 1:15 Thank you.

**Lucas Nelson** 1:21 It's up to you, Scott. I think we'll just go ahead and get started here in silence there,
Andy, OK?

**Don Middlebrook** 1:32 Yes.

**Scott Sorel** 1:34 Yeah.

**Andy Lambert** 1:34 OK, sounds good.

**Scott Sorel** 1:35 Yeah, sorry, I was muted 'cause you press record. Let's go.

**Andy Lambert** 1:37 Yep. Alright, so I'm gonna share my screen and kick us off. Let's see if I can do a whole application. No, it's not. Alright, so I maybe go back and forth between sharing some, you know,
individual. Um. Things I have open. So we'll start actually, yeah, this gives us a good overview. So this
is taken from the confluence page that just lays out the agenda for
today. So we're going to be talking about and I did put a note in here
that the objective for today is to and it's just taken directly from
the associated. Ticket for this particular enablement track. The objective is to
understand how tagging, metadata and taxonomy are implemented and how
they drive dynamic content, search filters and cross-site behavior in
AEM. And so we've broken that out. I did put one note that. We're going to have the dam focused session tomorrow where we bring in
a subject matter expert, Chris Lewis, who has some familiarity with the
project going back to the early days and also is an expert in all things
custom metadata schemas and best practices around that. So and and the other agenda items we have lined up for tomorrow. That
said, there will be some crossover. I'll, I'll touch on you know some
critical differences when you're thinking about tagging versus what the
difference is really between. Tagging in a EM versus the concept of metadata schemas and custom
metadata fields and things like that. So we're going to get into tag
taxonomy, which is basically talks about how tagging was implemented or
I should say put into place and structured for this implementation. Tag management, some best practices around governance and some
permissions and things that we can set up that can be set up so that you
have granular control over who's able to. Add, update, delete tags and then we'll talk about the application of
tags and authoring and asset management. So we will touch on assets
there. We will in that area talk about how there are certain asset
metadata fields. Fields in your schema that are populated from tags, so there's some
crossover and functionality there. And then we'll talk about tag
performance considerations and troubleshooting and some of the other
call outs that you guys had in the JIRA ticket. I'm gonna stop sharing that for a second. This is the one that I wanna talk about, so um. And the first talk about tag taxonomy and how it was configured for this
implementation. Before I get started, any questions on the agenda or any
call before we get going?

**Don Middlebrook** 5:00 I don't have anything at this moment.

**Andy Lambert** 5:01 All right, all right, so. You know what? I'm we'll talk through this a little bit and then I'm
actually just gonna share my whole screen. But look, if you ping me on
tag on Slack, I'm not gonna see it. Heads up.

**Lucas Nelson** 5:17 No problem, Andy.

**Andy Lambert** 5:25 Free wheel on it. No, no training wheels, no loop. No look on the back end saying no, no, don't.

**Lucas Nelson** 5:33 I I have faith in you, Andy.

**Andy Lambert** 5:35 All right, that's it. That'll be your demise, buddy.

**Lucas Nelson** 5:39 Yeah, probably.

**Andy Lambert** 5:42 Alright. Oh, can you guys see my screen OK?

**Lucas Nelson** 5:48 Yes.

**Don Middlebrook** 5:48 Yes.

**Andy Lambert** 5:49 I'll take that as we're good. Oh, the reason I shared my entire screen
is I want to be able to hop back and forth. I'll try not to do it super
quick or scroll a lot, but I want to be able to, you know, demo as in
context. So your taxonomy route, I'm not sure if you're familiar, but
in AEM. Um. On to move that guy 'cause we'll be referencing that later. Tags are managed in AEM through a tags console. I'll step back for a
second and go back out to actually just that we have it for the sake of
the recording. So let's say you're coming in as an author and you land
on the the start page for the touch UI also. Refer to as the granite interface. You click on your tools icon and
it's over here under tagging and you can see that there are several the
top level of tags in AEM or and in general in the tagging world are
called namespaces. So some of these are out-of-the-box. This is used for multi-site manager
or translation functionality in a EM. You've got some asset properties
that are out-of-the-box like portrait, landscape, square. Files. You also have variations on experience fragments that are
out-of-the-box where we get into and then some tags that are used for
various workflow processes like site and AEM projects and so forth. So where the rubber hits the road with you guys is we have a namespace
called SHRSS. You can see it in the console and the. The actual path in the JCR is under the hood is forward slash content
CPU tag and then your namespace which is SHRSS. And so here you can see
that there are tags set up for. Your regions, brands. Hotels, some of these are in use currently and some of them are not.
Some of them are set up for the additional site that would be onboarded.
Maybe they got started and were paused or or for whatever reason are
I'm looking at production. So we currently we're looking at production
tags. You got your lines of business news categories. And underneath these you have, you know, more granular levels of the
taxonomy, for example featured news. And just to show an example of
where, for example, featured in addition to tagging an asset or a page
or other resource in a experience fragmentation. Fragment content fragment. You think about back in the old days there
was that website Delicious where it was just one great big tagging cloud
where people could tag content with any descriptive tag that they could
think of to create this massive cloud taxonomy. You have that ability in AEM in a governed way to and we'll talk about
the governance that's in place currently for your tags or tagging
schema, but you can in AEM tags are also used often to drive things like
drop down menus for authoring component properties. Or or even specific asset metadata fields where when you're choosing,
when you upload a NASA and you're applying metadata, you want to have
governance over a finite set of options to describe the. Um. I don't know pick anything really the the the category of for the
asset. That's a greatly a great example for your content. Fragments are
based off of categories. categories um that get applied. And I'll show an example of that
shortly. But for news categories, an example of that is featured news
gets used to populate the blog page on hard drop. So if we go I was just there. Where's news guys?

**Lisa Cardia** 10:30 Down to the bottom, there's a section that's gonna land.

**Andy Lambert** 10:33 Yep.

**Lisa Cardia** 10:34 That'll land us right. There's a direct link to the yeah.

**Andy Lambert** 10:37 Perfect. Perfect. So yeah, so we have under here we have news. And then this is where I'm not. You can see I'm still coming in and
getting familiar with your your architect, your content architecture.
But I think the latest items you could see that there is the Seminole
Hard Rock Hotel and Casino Hollywood.

**Don Middlebrook** 11:09 So are these the tags that are applied to the modules on the page?

**Andy Lambert** 11:11 Yeah. Correct. So so for for this card list, for this section of the page that
we go preview, I can say OK, so that's featured news. I go back to
edit. The content that shows up under featured news is driven by the
content fragment card list component.

**Don Middlebrook** 11:16 Oh, brother.

**Andy Lambert** 11:38 And is based off of the type of news. And somewhere on the hood that's driven by and select the list type. Is tags and then it's set up to the to come from featured news. So
that's how that's component knows where to pull and news items from is
basically they're all tagged with featured news. That makes sense.

**Don Middlebrook** 12:01 Amazing. Yeah, that makes sense. I guess one thing I wanna talk about with those tags, if we can go back
to that page where where you show all the list of the tags.

**Andy Lambert** 12:17 Sure. Mhm.

**Don Middlebrook** 12:23 So right now and I I brought this up before. So we have you know under
the first level underneath the SHRSS we have directory called
categories, we have directory called category, then we have news
categories, we have events categories, so.

**Andy Lambert** 12:38 Hmm.

**Don Middlebrook** 12:42 Can you maybe explain why we have several sets of categories? Maybe why
those aren't all maybe not all nested under cat one directory?

**Andy Lambert** 12:53 Yeah, and they I think that they serve, they they serve different
purposes, but they could be named a little better, right? So so that as
you're reading through this as a human that it would not be so because
that that actually just caught me when I was describing that your
content fragments use category and I was.

**Don Middlebrook** 13:03 Yeah. Yeah.

**Andy Lambert** 13:12 Pointing to this folder, it's not that they're actually driven by this
is the the field that populates. So I think that that comes into play.
We'll talk about best practices for naming here in a little bit and I
think that we can add that as.

**Don Middlebrook** 13:16 Right. Mm-hmm. Yeah. Yeah.

**Andy Lambert** 13:28 As a to do you know for you guys or at some point you know to to do a
little bit of clean up and refinement of the tag structure.

**Don Middlebrook** 13:30 Right. Yeah, definitely, definitely want that. And the same with the property
names because we have all the locations there, but then we have hotel,
casino and cafe and there's locations under there. See there's a few
of the properties, but everything, all the other, all properties are
listed under property.

**Andy Lambert** 13:50 Mhm.

**Don Middlebrook** 13:56 Names further down below, right there.

**Andy Lambert** 14:00 Yeah, it would make sense to consolidate for sure.

**Don Middlebrook** 14:02 Yeah. So it's like, do we need them all in one directory or do we need
to separate them out? What's the best practice for that? How do we move
them properly?

**Andy Lambert** 14:12 I'll take a note to and just calling it out for the transcription for
us later Luke to to take a look and see the like the functional
implications of doing some consolidation on this because it would it
would make sense to try to.

**Don Middlebrook** 14:25 Yeah, right.

**Andy Lambert** 14:28 To merge that so that it's seamless.

**Don Middlebrook** 14:30 Yeah, it it, yeah, just get it all clean and a better organization would
be great. Um, Lisa has a question.

**Lisa Cardia** 14:38 I think it goes hand in hand with what you guys are saying. It's just
if you guys do restructure this, does that break anything currently is
my concern.

**Don Middlebrook** 14:46 You're right, yeah.

**Andy Lambert** 14:47 But I yeah, what we would do is assess whether it breaks anything,
whether it's can. What we try to do is set things up so that there are
no hard coded paths. Now it's not always possible, it's not always the
case, but our. In developing is to make everything as configurable as possible and
follow a configuration as a development implementation model. And I'll
go a little bit under the hood. I'm not gonna spend too much time on
this, but just to give you some perspective on that. There are a bunch of so there's a service on the back end in the in the
source code that gathers content based off of tags and and there are
other types of services like that where the paths that are involved. For
example, here's a here's a good example. Is that we have a very an environment variable that can be set. It
can't be set by like your average author, but it can be changed by, you
know, your AEM administrator, anybody like a TJ or whoever has access to
a cloud services can go in and if you wanted to move say the locations. Root content for your content fragments, your location content
fragments. Then this variable would allow you to change that location
without having to do a code change. And So what we would look at and you know, making these these desired
changes like to your tag taxonomy would be, you know, does that, is it
handled? It doesn't matter at all. Is it does? Is there a variable in
place either in the code or in cloud service environment? Variables that would need to be modified and if not, then the overriding
goal would be to so you all can make these changes without it being a
consideration, you know, so but for us to do it right now as we're sort
of transitioning and we're onboarding new sites and functionality it
would. The due diligence would be for us to at first let you know if there's
any implications from a coding perspective and then give the green light
if you wanted to make changes. But but have you do those changes? So at
this point you guys as much as you can sit on that you know. And be empowered to to do what you want to do without being dependent on
us.

**Don Middlebrook** 17:14 Understood. Understood.

**Andy Lambert** 17:20 So that gives a a pretty good bird's eye view of the taxonomy route and
the and the tagging structure underneath. As I said, there are places in
the code where or in your implementation where. Tagging is used to populate, for example, authoring properties and an
asset metadata. Another area where tags are where there's a mapping
between content and tags. Is these they're called. It uses the functionality from the ACS Commons
library, which we talked about for. I don't know if TJ's on or anybody
from the technical team, but. We're in the process of helping you guys upgrade the ACS Commons
library. A lot of your functionality leverages capabilities from this open source
library. It's just a collection of tools and capabilities that can be
added to an out-of-the-box AEM implementation. And one of those pieces of functionality is one of those features are
called generic lists. And we use generic lists in this implementation to map tag sets to
particular content areas. You can see like I guess when we started
working on paths at some point before one of the pauses before I. I was around and there was map. There are mappings for this Atlantic
City cafe. Property to oversight page to the Atlantic City tag that and this
experience fragment is associated for Kataya is. Associated with this tag set. So as we onboard those sites that this
will be driving functionality I assume as long as it's being done the
same as it was originally planned.

**Don Middlebrook** 19:34 Yeah. And how would we use this?

**Andy Lambert** 19:39 So it what it does is it it governs the tags that will can be used under
a given section. I believe is what the that's typically why this is
used. It's to enforce some kind of a. I shouldn't say that it limits
the number of the tags that can be used. It's to impose it's to. Put some kind of constraint or guardrail in place and I can just take a
note to go back and ask Vinay or if you guys could add it to the
questions list for today, that would be good. Um. When you guys are compiling your questions for the post KP Q&A.

20:20 Yeah.

**Andy Lambert** 20:21 We can see how and I actually looked and I didn't see any really that
affect like the corporate side or careers. For reverb, you know the sites that are alive today. So I don't have a
real world example to show you, but I saw that this is in place when I
did AI did an analysis of the to get my head around the implementation
and stuff. When I came on the project I did a complete analysis and. You know this was called out as a functional a a piece of functionality
where tagging tags and content were mapped together. So for the any AEM admins and then authors with that would have any
interest in this the ACS you get the ACS Commons tools by going again
clicking on the toolbar here or the tool icon and then this listed down
here. And this is where you would go to view those generic lists.

**Don Middlebrook** 21:24 Mm-hmm.

**Andy Lambert** 21:26 There are also, um, generic lists for social media types. This drifts away from tagging and taxonomy a little bit, but I think
it's important to be aware of. But laser mappings for the different social media types that have been
defined and their how they're used on the back end.

**Don Middlebrook** 21:53 OK.

**Andy Lambert** 21:55 Features.

**Don Middlebrook** 21:56 Yeah, we'll we'll definitely need some more information on that.
We'll add that to the questions.

**Andy Lambert** 22:02 Yeah, basically the question is how are dot Howard? What are the generic
lists that are currently configured and what are they being used for
basically? OK. So that's covers this piece of the taxonomy and then a big piece that I
want to talk about are or is the relationship of tagging with your
content fragments and other assets. So um. Yeah, I think I have. So it talks about that basically for content
fragments you have a categories field that holds tag IDs that are used
for filtering in various dynamic lists.

**Don Middlebrook** 22:59 Hmm.

**Andy Lambert** 23:01 Then you also have tagging of course on your assets using the CQ tags
property just like you would on pages. And some examples of that where
they're being used are like to tag by region, tag by event categories. And to give you some perspective on, I did a um, I'll blow this up a
little bit for you to see. And I'm happy to share this with you guys. This is just something to
have as a reference. So I did a I did an export of all of your page
content, experience fragments and content fragments and it's just a
sampling of the corporate assets. From your production author instance, I didn't take into account
whether they were published or not. So this is pretty much everything
and you're definitely using for content fragments more than anything
else. You're using um tagging, so for example this um. This particular article from this is a content fragment news article
news item that's showing hotel news and press releases. If there's
anything relevant that you would like to see from this list, like if I
was looking for a career. But it's not in production yet, so yeah, that would make sense. But this gives it has columns that show that this is what the tag space
looks like from the from a coding or back end perspective. It has the
namespace SHRSS with a colon and then the. The tagging hierarchy, hierarch, hierarchy. Can't talk today, guys. I
would need a drink of water, but and I separated them by pipe just so
that it was easy to see. So there's two tags associated with this
particular news article.

**Don Middlebrook** 25:03 It's alright.

**Andy Lambert** 25:13 And then just for human readable, that actually translates to this path
in the JCR. It's forward slash content. Yeah, basically just to get the tag ID, you replace content CQ tags
SHRSS with SHRSS colon.

**Don Middlebrook** 25:35 OK.

**Andy Lambert** 25:36 And then vice versa. You would replace SHRSS colon with content forward
slash content forward slash CQ tags forward slash SHRSS colon. And then I listed the the tag property. So all of these you could see
your content fragments all are you leveraging that. I assume that's a required field when you're authoring content
fragments. We can take a look and then there are some where it's both
tagged via the categories drop down and the the regular old CQ tags. In the content fragment properties. Let's take a look at that just for context.

**Don Middlebrook** 26:20 Yeah.

**Andy Lambert** 26:25 One thing I wanted to touch on that we just had done, we had a support
ticket for it in place was to at least for now replace the default
content fragment editor with from the Universal Editor and Experience
Cloud with the. Legacy AEM localized editor because you guys are using functionality and
and other things that are not supported yet in the universal editor. So
ideally at some point down the line you would be able to switch back
like failures. Here's the Experience Cloud version that you probably used to see them
pop up when you go to edit a content fragment. Here's the um. Local version. So if I Scroll down through here. The search, yeah, category. So you can see that the category selected
here is hotel, sub category, hotel, line of business hotel. I think these are all tag driven. I can go one way where we can, if you're interested, we can go look at
the content fragment model.

**Don Middlebrook** 27:39 Yeah, let's look at that.

**Andy Lambert** 27:52 So all of your content fragments are based on content fragment models. I
think Daniela touched on that the other day. And let's look at what was it we were just looking at. The location, OK. So all of the dialogue fields that you see when you're editing the
content fragment are defined via the content fragment model. And you can see property ID. You click each of these fields on the left, it shows what the back end
value is or the the type. So here's like. Either uh um number field or multi field. This tab data types is for actually. If I wanted to drag like if I
wanted to add a single line text, I could just drag that over. I'm not
gonna do anything 'cause we're in production, but. So it shows the field label, the back end value that would be used by
code, front end or back end code, placeholder value, a type if it's if
it's a numeric type, the default whether it's an integer or fraction. Fault values. Trying to scroll down on the this side. Anyone. There we go. You can actually specify validation type first over with
the numeric field less than or equal to greater than between. You can
even add custom validation types if you've got you know you can
actually, you know, define. You can get real meta with this here on the development phase. If you
had requirements like for a number field that aren't defined here,
custom error message instructions for user. So you can go down through here and see. Now let's go down to a
category.

**Don Middlebrook** 30:21 Less, yeah. So.

**Andy Lambert** 30:23 Hmm.

**Don Middlebrook** 30:26 So if these are not defined by tags in the list, was that a requirement
to set this up this way or what's the better route to do like?

**Andy Lambert** 30:37 It's helpful. If you could, ideally everything would be nothing would be hard coded
right? Like so. So if it were possible to drive this by, let me go back
to the tags.

**Don Middlebrook** 30:44 Right.

**Andy Lambert** 30:53 Gaming hotels, Featured news, pre-word. here. This is casino, hotel, dining, retail and none. I'm just kinda seeing
if there is a what was that support that's getting in my way. Just wanna see if there's an under these categories. Yeah, there's not really a one to one. So yeah, that's a good question for to be added. Or as a something in the I would say that goes into gap analysis for you
know some enhancements and. But you would have to look and see like what is this? Is this
categorization unique to this this the locations data type or is it
universal enough to where it makes? Sometimes it makes sense if it's
just an enumeration that's specific to one data type you think about.

**Don Middlebrook** 32:04 Yeah.

**Andy Lambert** 32:10 Content fragments. Think about content fragment models just like you
would in a traditional like old school CMS where it's still database
driven and you have a database table for locations, right? And you've
got a field for for location ID or property ID and.

**Don Middlebrook** 32:23 And.

**Andy Lambert** 32:28 Um, legal name, location ID and so forth then um. You know you would say maybe have like a look up table for this and that
that or you may not. It may just be this a standard like like a
numeration set that it's not used anywhere else. So why go through the
it would be potentially over engineering to. Break it out.

**Don Middlebrook** 32:53 Right. So I guess my question would be how is this content fragment utilized
right now? And how these lists populated and that or where it's used?

**Andy Lambert** 33:09 Yeah, while I'm here, I'm just looking to see if any of these are
driven by um. Content problem. Doesn't look like it. The locations are used all over. I go open up the dam. That they're organized by regions and North America, yes. Was the one. This is the one we were just looking at is for. That's
it's a test location. Well, maybe we need a better one.

**Don Middlebrook** 34:02 Mhm.

**Andy Lambert** 34:07 Anybody have a valid one right off the top of their head? It would be nice if these were named uh.

**Don Middlebrook** 34:16 Right.

**Andy Lambert** 34:16 Let's see what they are.

**Lisa Cardia** 34:20 We've asked for that too.

**Andy Lambert** 34:22 Yeah. Luke, don't kill me. This is where I would see you pinging me on Slack
and saying stop being a good idea fairing. Put ideas in their mind. No,
he wouldn't. He wouldn't do it.

**Lucas Nelson** 34:31 No, it's good, Andy. It's good.

**Andy Lambert** 34:35 Yeah, he wouldn't do that. He would just say, Yep, we got that's
enhancement and.

**Lucas Nelson** 34:39 Yeah, yeah.

**Andy Lambert** 34:41 Oh yeah, here's um. Yeah, so this is it's got its location ID which gets coded here or or
encoded here. I should say codified. This is the HR bet Illinois Sportsbook. I guess. And so yeah, these are used all throughout the site. Um. The properties and so, so forth, probably Lisa or my taison.

**Don Middlebrook** 35:09 Alright.

**Lisa Cardia** 35:10 Yeah, I think that this is like, this is something that we took away in
a different session that we had with Daniela that we said this is like
actually an issue for us because it was about getting a certain content
fragment card on a page and that although we built it in the same like
folder structure underneath the property, underneath the line of
business and organized by month. It still required the author to put the location reference ID, which we
thought was, you know, silly and not really user intuitive for people
outside of like maybe this group.

**Andy Lambert** 35:44 Yeah, yeah, I hear you.

**Lisa Cardia** 35:44 But I think we saw that with, um, events. I wanna say I'd have to like,
go back.

**Andy Lambert** 35:53 Yeah, so one way to like quickly see and and I know this doesn't solve
the problem in its entirety is like if you had a separate tab open with
the dam, you can look it up by some some descriptive reference you know
like you might not know exactly HR bit IL sports book but. You know, if you knew it was IO sports book or something like that, it
would help be able to identify it quickly. Your line. You can switch to list view and that's gonna give you the. Or it doesn't that this list view dot is not very helpful, but the like
part of you is. And capture it. Well, we'll have it in the recordings and be captured
as a screenshot. Just if you're keeping like a tips and tricks book or
notebook for your authors and stuff. But. So yeah, let's actually wanna look at and I'm gonna stop sharing my
screen for a second. I wanna do a quick look up. I see my pretty face
keeps showing up. I don't know if it does on your screen every time I
stop sharing and reshare. So hello.

**Lucas Nelson** 37:14 Only I see it, Andy, 'cause only the inside Adobe folks see the Adobe
faces. Yeah, there you go. Now we see your face.

**Andy Lambert** 37:17 Oh, OK. Oh yeah. Hello.

**Lucas Nelson** 37:27 That majestic beard.

**Andy Lambert** 37:30 I guess the yeah, it's it. It was not white before I started today at
Adobe.

**Lucas Nelson** 37:31 The Wizard of AEM. I remember when it wasn't white, yes.

**Andy Lambert** 37:43 All right. Yeah, I'm gonna share my screen again. So I have this put together for you guys and I'll send it out as a
follow up. It basically breaks out where you have asset metadata that's
driven by tags. So obviously you've got your CQ tags field. The brand asset metadata field and maybe I can go find an asset and we
can look at it. So you have for context venues and branded experiences,
SHRSS venues, LOB and you can see on the right which tag namespace those
align to. You guys want to see that in action?

**Don Middlebrook** 38:35 I I mean, I'm familiar, but maybe so everyone else.

**Andy Lambert** 38:43 Help me find an asset so I'm not digging around. I should be able to pick anyone. I completely. Tell you how good my memory works. Yeah, so if I click this for brand. It's take MA to the tag taxonomy for brand. I would go back over to
tags. It's a Hard Rock International, Tunnel Gaming, Tunnel, Hard Rock. Makes sense. So that's Yep.

**Don Middlebrook** 39:49 Mhm. Yeah, you can also type ahead, so.

**Andy Lambert** 39:58 Yeah, I'm not that quick. And then there's the venues and branded
experiences.

**Don Middlebrook** 39:59 Yeah.

**Andy Lambert** 40:04 Uh, I will show you something neat though if we have time where I I'll
use type ahead and you'll see how. I can be pretty expedient with that particular tool. Oh again, same
thing. Then using branded experiences, this starts out at that that root
and the tag taxonomy. That's another form of governance. And then this also lists that um one place where it's event categories
is what's being used for um. For this categories field, let's go back to that asset for a second
actually.

**Don Middlebrook** 40:53 That's they're all on the right column.

**Andy Lambert** 40:58 Thanks.

**Don Middlebrook** 40:59 Yeah, those aren't the same. Tags.

**Andy Lambert** 41:03 Let's say it starts with awards, bars and lounges.

**Don Middlebrook** 41:05 Yeah, those aren't the same, right? Yeah, these these are the ones that
are populated there.

**Andy Lambert** 41:09 It's, uh, this one. So this is where it would make sense like either to rename, rename these
namespaces or like this could be like.

**Don Middlebrook** 41:25 So those are the those are the ones that you used on the content
fragments. So the other ones are the ones we're using I guess for
assets, image assets.

**Andy Lambert** 41:25 Is there a? Mhm. Yeah, it says their event for it. So both the metadata asset property
like if I hit cancel and like category, this should be event category
because that's what drives it.

**Don Middlebrook** 41:48 But this isn't. This isn't. This isn't for. Yeah, this isn't for
events.

**Andy Lambert** 41:48 And then again and then. Oh oh, that's interesting. And then you actually have a totally
different event categories.

**Don Middlebrook** 41:56 Yeah, that's that's why all this needs to be rethought and
reorganized.

**Andy Lambert** 42:01 Mm-hmm. Yeah, that makes a lot of sense.

**Don Middlebrook** 42:04 Because. Yeah, that's where I was getting confused before because I'm going in
and we look at the properties and it's we have these categories, which
is fine because this is what I need for the image assets. But then you
have I guess categories that are only applied to. The content fragments. So that's where I guess the news and events and
these other the categories is applied, I assume. So that's why we need
to figure out what's going on here, how we can get this cleaned up and
organized better.

**Andy Lambert** 42:30 Yeah. Yeah, so we'll take it as an action item, circling back what we said
before to and we'll do it. We'll do this pretty quick. I wanna get an
answer for you so that you can feel comfortable making changes and
knowing that it's not gonna break anything.

**Don Middlebrook** 42:38 Yep. Yeah, yeah.

**Andy Lambert** 42:49 OK. Just close a couple of things. I'm not.

**Don Middlebrook** 42:53 I I assume just moving using the move tool is fine. That's probably
will update everywhere unless it's hard coded, but hopefully nothing's
working.

**Andy Lambert** 42:59 Yeah. Yep, that's correct. It'll yeah, it'll update all your reference pads
for you. So yeah.

**Don Middlebrook** 43:06 Yeah, because I mean, I've been doing that for a while with the assets,
trying to clean up everything that's on stage because we had a lot of
assets that were put in the dam and I've been trying to clean that up,
rename assets, move them to the right directory, so. Trying to get the metadata updated as well so.

**Andy Lambert** 43:29 I think it's a good time, like in general with where things are with
the implementation. Yeah, it would have been great. Like you came in,
Don, like when about a year ago, maybe. Yeah, yeah. And and we're at a
place now where we're doing this whole exercise of these KT sessions
and the true and the.

**Don Middlebrook** 43:39 Year ago, Yeah, 13 months ago, yeah. So it's. Mhm.

**Andy Lambert** 43:49 Gap analysis and like and then ideally moving to the next wave. So for
all of these things that it this is a good opportunity to to make these
adjustments like yeah you're pretty far along there's there's several
you know levels of the taxonomy but it could be a lot worse sometimes
you know if you were if we had four more properties.

**Don Middlebrook** 43:51 OK. Yeah. Right, right. It can.

**Andy Lambert** 44:09 Right.

**Don Middlebrook** 44:10 Yeah, and and there's, you know, the metadata schema we probably need
to look at and make changes to and add things that we don't already
have, things like that. Definitely need to look at. But yeah, this is a,
you know, we should.

**Andy Lambert** 44:25 Yeah.

**Don Middlebrook** 44:26 Make sure that before we do a full launch, we have all this, you know,
organized better, clean it up better. Um. And so forth so.

**Andy Lambert** 44:34 OK, alright. And again, I'm gonna send this. I've got a couple of
different documents I put together. Um. So the one we just looked at that lays out where tags are being used
across asset metadata schemas and all that, and then I'll send you.

**Don Middlebrook** 44:44 OK. Yeah, mm-hmm.

**Andy Lambert** 44:55 Some uh. I'll send you the my actual agenda, my talking points, this document
that I'm referring back to, and then I've got some other things that
just may come in handy, like list of pages where.

**Don Middlebrook** 45:03 OK.

**Andy Lambert** 45:13 The card list is being currently being utilized and stuff like that. So
that may may not be matter that much for you, but for you know authors
that might be useful.

**Don Middlebrook** 45:16 OK. Really. Yeah. Yeah, definitely.

**Andy Lambert** 45:24 Coming back, let's see how much more so I know. Yeah, I need to talk
pretty quick.

**Don Middlebrook** 45:30 You got 12 minutes.

**Andy Lambert** 45:32 No sweat. So yeah, and then we've touched on some a lot of this already
just by walking through. So the tags are organized by under SHRSS or a
high level broken out by things like regions, events, properties. But you could see there's opportunity for some optimization with the
category field specifically or category category fields or spaces. We
talked about the path to tag mapping, how that's that that's it looks
like it was being set up to be used for hotels, cafes. Which are ideally hopefully upcoming migration projects. So then it gets
into talking about some best practices and taxonomy strategy. I pulled a
lot of this content from the. Assets tagging best practices and and sites tagging experience league
pages and those are linked at the top of this document. But we wanted to
talk about permissions specifically so we can. It is possible to. I say it's possible. It makes it sound like it's
some esoteric practice. You have the ability to set permissions at a
granular level on the tag taxonomy. So for example, if you only wanted certain folks to be able to manage
regions, then we use on the permissions console. We could certainly do
that.

**Don Middlebrook** 47:12 Yeah, I think we definitely need to lock that down because we don't
want everybody going in, adding random tags or making messing up
something, deleting that something that's not shouldn't be deleted.

**Andy Lambert** 47:21 Yeah, so. Yeah. So the way that that would work and and we have another session lined up
for user management and and group management and stuff. But essentially
you would like go within a group. You never want to give permissions to
a person that always, even if there's only one person in that group for
the sake of scalability and also if they're. for technical reasons why um you would only want to give it to assign
permissions at the brief level. Oh, let's say and I'm not going to
change anything again because we're in production, yada, yada, yada,
disclaimer, disclaimer. That actually goes to a group. I don't want that. Oh, go there to
permission. Back on that. Go back over here. Here are the permissions. So somewhere in here is probably something that admin briefly can take
just for fun. Yeah, we'll just say this one. And this gives you a granular view of the paths that a particular group
has access to and what level of access they have, what privileges, where
read, write, add children. They delete even CRX replicate means publish whether they can actually
publish or not. So you know you could actually add ads just for that
particular path under. DQ tag. So let's say we only want we gave this group for a cafe. So yeah, you
can do that. Select it. And get ready. If it if they can do everything and then there's shortcut, just do
everything. You can actually specify whether it's a deny or allow.
There are best practices around that that we'll get into during that
session. But Oh yeah, that. Um, that is how you would go about. Getting granular with your permissions. Just go back and make sure that I'm covering exactly. Oh yeah, for governance, that's that's how that would how that would
occur. You put guardrails by defining who can do what. You can also, as
I showed, you can specify whether they can just read the tags in Tag
Manager, whether they can create, update, delete. When you do delete tags, it's gonna tell AEM's gonna tell you that
they're referenced by other resources. So that's baked in. We covered. Pretty much all of it. And there are additional topics. OK. Oh. Yeah, this says I showed using permissions on the tag tree. It talks
about keeping a, you know, a document somewhere, whether it's Excel
file that has permissions for all of your different content types and
and metadata types or just something where you're tracking. And maintaining this um.

**Don Middlebrook** 50:58 What's in the architecture workbook right that we have?

**Andy Lambert** 51:01 Yep, Yep. Yeah. As it was whenever it was last, you know, updated, it
probably. My guess is it probably could be some ugly. Let's see.

**Don Middlebrook** 51:02 Yep. OK. Yeah.

**Andy Lambert** 51:17 So best practices just for everybody. It's you want to use single
vocabulary glossary that everyone's agreed upon and it's part of, you
know, your metadata governance model. Believe it or not, it sounds like
I just made that up or pulled it from somewhere, but it's it's part of
when you're looking at.

**Lucas Nelson** 51:33 Yeah.

**Andy Lambert** 51:36 Especially a DAM capability maturity model, but a content management
capability maturity model. You know, one way of sort of defining or
figuring out where you are along that that CMM path is by looking at the
governance, including documentation that you have in place. And so you know, defining the vocabulary, the lexicon that you work from
is an important aspect of that. And avoiding synonyms with separate tags
is kind of just a general guideline. Avoid over tagging assets and
resources. Always, you know, just like with any CMS resource type, you always
looking to reevaluate and optimize. Yeah, and then this one just talks about that that where the ACS Commons
path tag mapping lists are. That should definitely be a governed thing.
Should not just be like your average author should not be able to come
in here and go to. ACS Commons and modify these lists because they they drive
functionality. So it should be an administrator or super author or
someone that understands. Again, probably just like it sounds like
you're the damn strategist on. It sounds like probably someone would be
designated as.

**Don Middlebrook** 52:44 Right. Mm.

**Andy Lambert** 53:01 at that level of metadata governance, and this will be part of that that
job, that title, you know.

**Don Middlebrook** 53:06 Right. Yeah, I'll just have to. Do some deep dive on that.

**Andy Lambert** 53:17 When we talk to them, let's say. Talked about metadata schemas and how the CS are used there. Talked
about content fragment, talked about pages. As authors, you probably
know you know what tagging looks like when you're on a page. I probably
don't need to go into that, but just for real quick. And like I we're coming close to time. I don't know if you want to tee
you up for close out, but again, just to have you prick up your ears and
I'll work through the rest of.

**Don Middlebrook** 53:44 Mhm.

53:52 Yeah.

**Lucas Nelson** 53:56 Was it you showing anything else, Andy? Wasn't there like some cool tip
you were gonna show? Yeah.

**Andy Lambert** 54:00 Yeah. Yeah, I have a second. So like anyway, this just covered it like so here
for the blog or I don't know Don, if you're familiar with all sites
offering side, but basically this is your general tags fit. Yeah, so you
go into a, you go into a page and that's the blog or new page and
here's the.

**Lucas Nelson** 54:04 Yeah.

**Don Middlebrook** 54:15 No, I but OK, yeah.

**Andy Lambert** 54:22 Property you got tags. This is where you do and you can see this is not
governed at all right now. So right now anybody could apply any you
could go as an author. I could go in and be like, yay, this page is
associated with portraits, no orientation. So I'd totally recommend putting adding some guardrails there, like
stubbing out like what your baseline page tagging is.

**Don Middlebrook** 54:41 Yeah, definitely. OK.

**Andy Lambert** 54:52 Anything else? There's a little more goes into detail about that that content listing
service by tag and I'll send when I send this out, you'll have the you
know more information about that.

**Don Middlebrook** 55:08 OK.

**Andy Lambert** 55:10 Um. Yeah, I'll just sit out the rest of good.

**Lucas Nelson** 55:12 Hey, with that, with the yeah, hey Scott, I I pinged you on chat. Is
there a SharePoint folder you can create for some of this collateral
that Andy's gonna provide? I think it'd be better to have a a link to
your SharePoint versus a.

**Andy Lambert** 55:27 Collateral band.

**Don Middlebrook** 55:28 Um.

**Scott Sorel** 55:30 Yeah, sure, sure. Yeah. Don, do you know where you have a place where
you prefer to have all the damn stuff? So usually I just put it in all
in one. Yeah. So maybe, maybe off the route.

**Lucas Nelson** 55:31 Document floating on e-mail.

**Don Middlebrook** 55:39 I mean. I mean, I can put, I can put it in mine my OneDrive.

**Scott Sorel** 55:43 Yeah, yeah. So I I would say that I would, I would ask in this case, I
would ask, I would defer to Don Luke.

**Lucas Nelson** 55:44 Yeah. Don, you just want us to send you the doc and then you'll handle the
storage. Oh, all right, that's fine. These aren't like big documents,
Andy. They're just note files. Yeah.

**Andy Lambert** 55:51 OK.

**Don Middlebrook** 55:53 Yeah, yeah, I can do that.

**Scott Sorel** 55:54 Perfect. There you go. Yeah.

**Andy Lambert** 55:58 Yeah, then, yeah.

**Don Middlebrook** 55:58 Yeah, but we just wanted to keep everything together, so yeah.

**Scott Sorel** 56:01 Yes, perfect. There you go.

**Lucas Nelson** 56:02 OK. Then that that that's good then that answers that. Thanks, Don.

**Don Middlebrook** 56:06 Yeah, yeah.

**Andy Lambert** 56:07 Yeah. So I think that covers us for tagging and taxonomy. As I said,
we'll get more, we're going to deep dive into metadata ad nauseam
tomorrow. So look forward to that.

**Don Middlebrook** 56:16 Awesome. OK.

**Scott Sorel** 56:17 Sounds fun.

**Lucas Nelson** 56:18 With Chris Lewis. Yeah, yeah. It's good to pull Chris back into it.
Yep.

**Don Middlebrook** 56:21 What was? What was your cool trick?

**Scott Sorel** 56:24 Cool.

**Andy Lambert** 56:26 Oh, yeah, yeah, yeah. Actually, Don.

**Lucas Nelson** 56:28 Yeah, you can't leave it that and then not close it, Andy.

**Scott Sorel** 56:29 Oh, there's a cool trick. Nice call. Nice call out done.

**Andy Lambert** 56:31 My bad. It's called Watch me slip out the side door. No, hold on.

**Don Middlebrook** 56:36 Right.

**Andy Lambert** 56:37 Yeah. Alright, so and Don, you probably know about this already, but uh, for
other folks, it's just. You can manage. Um. All like thousands and thousands metadata for thousands of assets in one
shot by exporting to Excel.

**Scott Sorel** 56:55 So that's. OK.

**Lucas Nelson** 56:58 Yeah.

**Scott Sorel** 57:00 OK.

**Andy Lambert** 57:01 You do that, right? Yeah, you grab this guy and I'll show you where my
handy dandy. Oh, I'm not in for it. That's create. So let's you pick
a folder that you want. Like, let's say I want corporate.

**Don Middlebrook** 57:01 I I already do it. Yeah. Mhm.

**Andy Lambert** 57:18 You go here, export metadata, giving name, SHRSS, corporate. Include assets and subfolders. What you never want to do is select all
properties, so you'll end up with a nightmare of a spreadsheet with
17,000 like arcane fields that you have no idea of what they are. Um,
where most of your.

**Scott Sorel** 57:36 Oh God.

**Don Middlebrook** 57:38 Yeah. Yeah, RDF.

**Andy Lambert** 57:43 A lot of the standard fields are the best way to do this and use a type
ahead, which is what made me think of the. This is actually one I can
use is like a lot of the metadata fields are prefixed with BC title. Oh,
I gotta do the path.

**Don Middlebrook** 57:50 Mhm.

**Scott Sorel** 57:53 Yeah. OK.

**Andy Lambert** 58:00 Content none of the.

**Don Middlebrook** 58:00 JCR, yeah.

**Andy Lambert** 58:04 So it's like that, for example, and back it up.

**Don Middlebrook** 58:10 Type in SHRSS.

**Andy Lambert** 58:13 So do you have some metadata fields that are prep? Yeah, there you go.
So if you have that namespace or you guys are just pre you're not, you
didn't set up as namespace, but they're just prefixed. Yeah, so yeah,
you can grab all these and then just copy and paste this.

**Don Middlebrook** 58:17 Yeah. Right. OK. This would be a good good question to ask. Like right now if I do this
then I I'm having to populate every single time I run this report to do
this. I I normally just export it directly.

**Andy Lambert** 58:37 Yep.

**Don Middlebrook** 58:42 And you're right, it does, you know. Fill up the whole spreadsheet. It takes hours to get this data. So if
there's a way to set this up to where I have a pre populated set of
metadata that I can just choose instead of having to go to add 15
different you know.

**Andy Lambert** 58:52 Is there a? Yeah. Yeah, you and every other damn admin. Chris is gonna talk. Chris is
gonna ask the site or he's gonna say the same thing tomorrow. It is a
pain right now. But yeah, you you do have to go and I just like, I just
keep a text file with on another prop. Got a couple of other damn
projects.

**Don Middlebrook** 59:03 And. OK. Yeah, I mean.

**Andy Lambert** 59:17 And I just keep a text file and just copy, paste, copy, paste, copy,
paste.

**Don Middlebrook** 59:18 Yeah.

**Scott Sorel** 59:23 Yep.

**Don Middlebrook** 59:24 Yeah, I mean, that's what I do, so.

**Andy Lambert** 59:25 Yeah, but anyway, so for everybody else, you can export this. It creates
a a Excel file. You can go in and you know, let's say you've got 10
thousand 50,000 assets in there and you need to change 10,000 of those
50,000 to have the same category. Then you can do a copy replace in that Excel spreadsheet, save it and
then re upload it from anywhere in the DAM. You don't have to pick the
folder again or anything. You browse for that Excel file you just
edited, upload it and within a few seconds it boom updates all of them.
So that's pretty handy.

**Lucas Nelson** 59:43 Hmm.

**Scott Sorel** 59:46 To.

**Don Middlebrook** 59:49 Mhm.

**Scott Sorel** 59:58 Yes.

**Andy Lambert** 1:00:02 That was my trick, but Don already knew about it.

**Don Middlebrook** 1:00:04 Yeah, no, I knew. I've been doing that for a while. Yeah, bro. Yeah, I
mean, I I I got some stuff out of this, so I appreciate your time on
here. Looking for tomorrow.

**Lucas Nelson** 1:00:07 Yeah.

**Scott Sorel** 1:00:07 It was a test. Donna's passed.

**Lucas Nelson** 1:00:08 That you're not surprised Don knew about that, yeah.

**Don Middlebrook** 1:00:19 If we can get that those questions added to the confluence, that'd be
great. I'll add any more if I need anything so.

**Andy Lambert** 1:00:24 Yep. Yep. And I'll take a first pass through them as they're coming up and
then any that need deeper dive, then we'll get into those with the
offshore team and and get them back to you.

**Scott Sorel** 1:00:28 Thanks.

**Don Middlebrook** 1:00:28 Yeah.

**Scott Sorel** 1:00:32 OK, cool.

**Don Middlebrook** 1:00:37 All right, great. Thanks. All right, appreciate it.

**Scott Sorel** 1:00:37 That sounds great. Thank you.

**Andy Lambert** 1:00:39 Thanks everybody.

**Lucas Nelson** 1:00:40 All right. Thanks. Y'all have a good day. Thanks. Bye.

**Scott Sorel** 1:00:40 Thank you, everybody. Thanks. Good stuff. Bye-bye.

Lucas Nelson** stopped transcription



## Session: DAM — 2026-02-18

**SHRSS Adobe Knowledge Transfer - DAM Sessions-20260218_130350-Meeting
Recording**

February 18, 2026, 6:03PM

1h 11m 27s

**Andy Lambert** started transcription

**Andy Lambert** 0:18 Uh, it couldn't give me the recording message. Can you guys hear me
OK? OK, cool. All right, we'll go ahead and get started. So today's
knowledge transfer session follows along nicely with yesterday's topic,
which was.

**Daniela Tea** 0:26 Yes.

**Don Middlebrook** 0:26 Yes, yes.

**Andy Lambert** 0:41 Tagging taxonomy and metadata governance primarily around the uses
current the the various use cases that are in place now with the the
SHRSS input current implementation. Where tags are being used to populate metadata drop down fields in some
cases for asset metadata, in other cases is used for other component
dialogue. Properties or fields. And so we covered all of that and and said
yesterday that we would and there was some crossover with what we're
going to be discussing today, which is going to be heavily focused on
all things dam, which will include. A deep dive into metadata schemas and profiles and all sorts of good
stuff. So we for today's adventure we brought along Chris Lewis, who
has been with Adobe for a good long while and worked with Chris. Danielle and I both have on a number of projects and he and I recently
just worked together on, I know at least one LCBO, right, Chris? And
then maybe, Oh yeah, also another as well. So he's he's honed his chops and he's here to provide subject matter
expertise on on the dam. He and I have met. We met yesterday to talk
about today's session and some of the areas where we think.

Speaker 1** 2:07 Yeah, yes.

**Andy Lambert** 2:25 Where I think he will be able to jump in and far surpass my level of
knowledge, the assets and the art of the possible and the art of
optimizing, you know, evaluating what you have today and and looking for
ways to optimize it, say say hello, Chris.

Speaker 1** 2:40 OK. Hey, hey everyone. Good to be here. Hopefully I can, uh, provide some meaningful insight here. So yeah, get
started and I'll jump in wherever I can.

**Andy Lambert** 2:56 OK. Oh, can everyone see my screen OK?

**Daniela Tea** 3:09 Yes.

**Andy Lambert** 3:10 Everybody's good.

Speaker 1** 3:11 Yeah.

**Andy Lambert** 3:12 All right, so oh one admin matter before we get going on this session is
I did upload the reference docs that I talked about to the. Compluent page for tagging and taxonomy and all that. Uh. Those are I'll show you real quick. There's a PDF. These two are basically different views of the same
thing. It's the lists or inventory of where all the pages that where
you're you currently using the content fragment card list component. So you have it in PDF where it kind of has more like narrative based and
then an actual spreadsheet for your use. You know, I don't know how
much Don you in particularly that that rocks your world, but it may be
of use to Lisa and and my pay is there. Working through things and just just having that holistic bird's eye
view of the content. And then there's also this PDF is the agenda that
you saw me walking through with all of the detailed information
underneath each section, so.

**Don Middlebrook** 4:23 Thank you.

**Andy Lambert** 4:36 Oh, that's this one. And then this one is a spreadsheet of all of your
where everywhere that tags are being applied to a page or experience
fragment or content fragment. Those are all things that we touched on yesterday. As we get started, yeah, I'll ramble. I'm hopped up on caffeine like
you wouldn't believe. So definitely jump in and raise it. Use the hand,
raise hand tool and teams or you know.

**Don Middlebrook** 4:55 Thank you.

**Andy Lambert** 5:10 Danielle, just call me out if, uh, somebody has a question and I'm
walking all over. He loves that. That's why she gave it some. All right, so today we're
talking about we're gonna get a DAM training and usage guide for
admins. And here's the JIRA ticket that was created that sort of
spawned off this KTR defined. KT session and so as I went through and built out the agenda, I just
constantly referred back to this to ensure that along with all the other
information that we've got planned that we covered these essential
asks. And. So and I I you know, where it made sense, I actually copied and pasted
the. To make sure that I had it accounted for and you'll see in certain
places throughout this document where I have it indented like a quote
where I'm quoting directly from one of the goals for that section or
where where it's pertinent. So yeah, if we look at the objective for
the session, we want to. Facilitate Hardrock's understanding of how to properly use the dam to
effectively manage assets, maintain governance, and support property
teams without risking misuse or disorganization. That came right from
the objectives from the JIRA ticket. And I sort of encapsulated the line items from a JIRA ticket in these
bullet points. We're going to start out by reviewing the current state
of the dam structural architecture, IE you know, the folder structure. And then Don, I I know that you had said that for right now the trying
to migrate over to SSSSSHRS primary dash primary was on the back burner
at least. And that we didn't really have to focus on that today, but I did, I
want to touch on it not if not that just not not that specifically
though I think we will come to it, but just talk about what optimal
state, where we are now, what optimal state looks like from your
perspective.

**Don Middlebrook** 7:16 Yeah.

**Andy Lambert** 7:30 From others perspectives and you know how do we get there and that would
include taking a look at of course the folder structure and any metadata
and tag clean up. We touched on the need to do some. Some sanitizing of the the tag structure yesterday and and then talking
about we'll talk about dynamic media readiness. Um.

**Don Middlebrook** 7:50 Mhm.

**Andy Lambert** 8:00 And we'll we'll also walk through the admin authoring processes. A lot
of this like Don may be totally familiar like do it in your sleep, but
you know if there are other folks that aren't in the dam as much and
are really looking at it from a sites perspective and working with the
assets from the dam for pages that they're able to talk about. That and then, um, well, I don't know what this word is.

**Don Middlebrook** 8:21 Yeah.

**Andy Lambert** 8:25 I think it's supposed to be holistic. There we go. Well, I don't know how that's got in there. I guess bothly how? There we go. We'll go with that. We'll talk about, we'll revisit tags and then we're really gonna get,
I know I was gonna restructure the way that that was worded or rephrase
it to be more all-encompassing of of the level of depth that we're
gonna get into as far as even conceptual notions behind. A, you know, asset metadata and tagging and AEM and then we'll capture
any follow-up work for any items that need to be go into the gap
analysis as missing. Right now or or not working as expected or a new feature enhancement and
you know as we're going definitely keep track of your questions like
we've been doing and and those items for gap analysis.

**Don Middlebrook** 9:26 Yeah.

**Andy Lambert** 9:30 Oh, by the way, I seriously doubt we're going to get through all of
this today because each one of these topics is an hour discussion. It
could be. I think that we can touch on it and then or not touch on it,
but we'll get in deep where we need to. And we'll manage time and then we'll see what follow-up looks like.
Does that look like discovery, you know, or what? What does that look
like?

**Don Middlebrook** 9:49 Yeah. Yeah, I I figured there's. I didn't realize we didn't think we could
get everything done in, you know, just an hour time. But yeah, if
there's a potential if we need to. Yeah. Have another session if if if that's possible, you know, make sure we
cover everything.

**Andy Lambert** 10:12 Yeah, well, like we definitely want you to feel, have the keys to the
Kingdom in terms of understanding the current implementation and like we
talked about yesterday, where you can feel comfortable making changes
and then where?

**Don Middlebrook** 10:20 Yeah.

**Andy Lambert** 10:29 You know that there may be coding ramifications or at least
configuration changes that need to happen on the back end to to support
like for example I and Daniela can speak to this move on content
fragments, right? Like let's say you did wanna move forward with. SHRSS primary, one of the first things that we would need to look at is
the way that content fragments function. So you know, that's just one I
can think of off the top of my head where it wouldn't be just as simple
as merging it in, you know?

**Don Middlebrook** 10:47 Right. Mhm. Yeah. Yeah. Well, and just to give you a little bit of background, so that SHRSS
primary was only set up decided that last August because of the way the
assets were originally migrated into the SHRSS directory. At that time I wasn't aware that we could move asset without breaking
reference, so it was and because I wanted to rename all these assets,
but because I didn't know that we could move it without breaking and
renaming assets, I was like let's just keep everything in SHRSS as it.

**Andy Lambert** 11:19 OK.

**Don Middlebrook** 11:38 Is and let me figure out what to do with that. And then we were going to
go and say SHRSS primary would be where all the new assets go. But I
think it makes more sense that we reclaim the SHRSS as the main
directory where we will move forward with. That way you don't have to move those content fragments and it was the
original plan in the architect workbook. That's what was what we were
planning on doing originally, but it seemed like it was going to be a
lot of work to do that from either both mine or and Adobe's side.

**Andy Lambert** 11:57 Any.

**Don Middlebrook** 12:16 To do that work. So we came up with that plan. I believe Daniela, you
were on that call or we had that conversation before, but now that I
know that I can move assets around without really breaking, although it
has broken some, but.

**Andy Lambert** 12:20 I see. Uh huh.

**Don Middlebrook** 12:34 I I just want to keep everything simple, keep it at the SHRSS. Anything
that's in primary I need to move over and then we need to we can, you
know, deprecate, you know, get rid of the primary at some point. And then just move forward with having that. And I've been working on
all the directories and trying to get everything in. So cafe's mostly
done, hotel also have a lot of work to do on, but that's where I am
right now, so.

**Andy Lambert** 12:50 But. OK. Yeah, thanks that. That definitely helps to level set on, you know
where things stand and the background on on how all that came to be. And
I think I So what we're gonna touch on, I keep saying touch on, we're
gonna get into.

**Don Middlebrook** 13:15 Yeah.

**Andy Lambert** 13:22 Maybe a path forward that would. So we're going to talk about, you know
we're looking at what we have today and then what where we might like
to be and that could be like if your goal, if your North Star well is in
fact. And it doesn't sound like it necessarily is like maybe there's some
middle ground, but if it was SHRSS primary, like what what a path might
look like to get there. And one idea that Chris and I went back and
forth with full disclosure is mostly his idea and may just going, yeah,
that's a good idea. Is having a and we've seen this on a lot of projects actually where you
might have a a folder called a root folder called legacy assets, legacy
dash assets or migrated of dash assets. Right. And just for the sake of of levels that clear and clear in the
slate and starting fresh, all of those migrated assets we we take for
example everything out of and Daniela don't freak out. We pull some
thought into this and. Not this is all just up in the air. I can see Daniela. Evil eye, there she goes. Now, but so for example, you've got this
under corporate, you got the photography folder as part of the content
migration process and for other reason that I wasn't around then that
you've got all these assets 1000 plus.

**Don Middlebrook** 14:42 Yeah.

**Andy Lambert** 14:57 You know for corporate in this folder, so it would you could and should
move those out of there and organize them in a form or fashion that
makes sense, but if if you. If you couldn't, if there isn't a a happy path to getting them exactly
into the damn structure that you want right now, but there is a path for
all new stuff, just like you said for the primary folder you had, you
could have like, OK, this is where all the legacy stuff lives. We know
that someday there may be a cleanup or some.

**Don Middlebrook** 15:25 2.

**Andy Lambert** 15:32 Scripting. It could be done with scripting for sure to migrate it all,
eventually clean it up. But you know, moving forward as of this date or
as of the launch of this site, everything or development of this site,
everything goes under the new structure.

**Don Middlebrook** 15:32 Right.

**Andy Lambert** 15:48 Um, Chris, you want?

**Don Middlebrook** 15:49 Yeah. But if you look under cafe, I mean, I've been actually working on
that structure to get it the way it is, you know, compared to the
architecture workbook that you know what we have aligned there. So I've
already moved things around. So that that one is.

**Andy Lambert** 15:51 Yeah. Yeah.

**Don Middlebrook** 16:05 Fairly to the way I need for cafe. I haven't worked on anything else as
far as moving things around. So if you go into properties, if you click
properties and then I'll you know everything's there the way it was.
Originally it was just.

**Andy Lambert** 16:20 I see.

**Don Middlebrook** 16:22 Cafe and then the list of like the properties and then underneath
properties was a language folder and then each language folder were
assets and there's there's duplicates all over the place. There's so
many duplicates in the system right now. And then under Amsterdam, then you'll see the types of PDFs and you
know, so I already have it in the structure that needs to be for cafe.
So I think I'm OK if we just move forward, I mean and put new assets in
there, it's.

**Andy Lambert** 16:50 And let me ask Chris a question real quick, just to sorry to cut you
off, but I wanted while we're right here in this context. So Chris, I
know from a site's perspective and with content fragments and when
we're dealing with localization like multi-site manager translations.

**Don Middlebrook** 16:56 Sure.

**Andy Lambert** 17:07 That you want your you need in order to take advantage of a EM like
automated translation capabilities that you need to have your page
content structure such that it has. Or to open up a site, for example, you would see it's under content
SHRSS EN and I can't remember Danielle or anybody right off the top of
my head if there's AUS in between or not. Yeah, I know, OK. Um, but the while I'm browsing through it to show the example. No, I
don't want to do a user survey. Give me alone Adobe. Um. We gotta incorporate. I got it. And then you can see here that we have English ENFR and ES and then in
the dam you'll see that under CS under each of these.

**Don Middlebrook** 18:04 Right.

**Andy Lambert** 18:15 Skype Cafe maybe. You'll have. So actually this works out. Yeah, you'll have your
translation folders. And so Chris, where I'm going with this is if I
it's been a while since I did MSM with like translating actual assets.
Can you speak to that thumb? Like would you want to follow the same
structure?

**Don Middlebrook** 18:21 And.

Speaker 1** 18:33 Mm-hmm.

**Andy Lambert** 18:40 Sure, or multilingual support with assets besides content fragments.

Speaker 1** 18:43 OK. Yeah. So for typically for any automated language support, you know,
like AM guides or anything like that to do any kind of swap out of
assets based on, you know, localization language, that language folder
typically resides at a top level, right? It's usually under, you know,
maybe under the very first. Level of SHRSS somewhere in there. You typically have a a language
starting here, not US and you're in sights, right? So if you go to the
dam, yeah, if you go there, I mean you typically have a language here
and then all these separate folders underneath the each language, right?
So that.

**Andy Lambert** 19:15 Yeah. Oh, sorry. Mm-hmm.

Speaker 1** 19:25 At a top level, you can easily have the software automatically swap out
language versions if that's a requirement. I'm not sure if your assets
have language versions or not. You can go down lower levels, but
typically what that kind of winds up doing is.

**Don Middlebrook** 19:35 Yeah. I mean, we're.

Speaker 1** 19:44 Is creating a very complex and convoluted folder structure, which may
not be an issue. It all depends on how you're working and how your
organization is in there managing assets. So I mean, you certainly can
do that. It makes the automation a little more difficult because then
you've got to be more specific as to where you're pointing to what
assets you.

**Don Middlebrook** 19:55 Right.

Speaker 1** 20:04 Want to translate, you know, with the along with the site pages. So
that's why it's mostly it's more universal and easier to put that
language at a higher level, right? So yeah.

**Don Middlebrook** 20:05 Right. I think in general for photography or anything like that, we're we're
trying to move away from having any kind of copy baked into the actual
graphic or image. So yeah, the only thing I can think of translated, you
know, we have our our PDFs or menus and things like that.

Speaker 1** 20:16 Yeah. Mm. OK.

**Andy Lambert** 20:27 That's good.

**Don Middlebrook** 20:35 Be translated, but I would probably more rely on metadata to assign if
it's a English or Spanish whatever to manage that rather than having
all the assets in.

Speaker 1** 20:36 Yeah. That's fine. Yeah, that's definitely, that's definitely one way to go about it. If
that works for you, all the folders do is drive automation, right? So if
you have automation software such as AM guides, that's one example. It
it doesn't look at languages on assets. It can't like do that, you
know, because.

**Don Middlebrook** 20:56 Yeah. Right, yeah.

Speaker 1** 21:09 Know where to look for the corresponding version. It could be anywhere
technically, right? Even if it's in the same folder the way you're
storing it, it doesn't know that, right? So it's not gonna do some
granular search throughout the DAM for a comparable asset with the
different tag on it. It relies on a folder structure to find.

**Don Middlebrook** 21:13 Yeah. Yeah.

Speaker 1** 21:28 A specific folder structure that's guiding it. OK, so that's all
you're missing out on. Not doing it that way is any kind of language
translation automation. That's all really. Yeah, so that's fine. And
really some of the use cases for that is not.

**Don Middlebrook** 21:30 Yeah, I see what you're saying.

**Andy Lambert** 21:43 Chris, well.

Speaker 1** 21:48 Just text or language. Some organizations have actual different imagery
for different languages, right? It might be an image of, you know, a
local, you know, area or spot or city or town, and they want to swap out
the actual imagery, right?

**Don Middlebrook** 21:51 Mhm.

Speaker 1** 22:04 Not, you know, text aside, right? Yeah, right. So that that's usually
what that's built out for. But if you don't have a a use case for
that, then it's it's irrelevant to you.

**Don Middlebrook** 22:07 Right, right, right. I I can't think of right now. Maybe someone else has a use case for it,
but yeah, because I'm really just trying to get to where we're
utilizing a single asset for, you know, across the board rather than
having the same asset.

Speaker 1** 22:27 Yeah.

**Don Middlebrook** 22:30 For English, for Spanish, you know pages where it's, yeah, so you just
have one asset that filters across all the sites and pages, so.

Speaker 1** 22:30 What?

**Andy Lambert** 22:31 No.

Speaker 1** 22:33 That certainly makes it easier, yeah. Yeah. Sure. Yeah. So that that's pretty much all the.

**Andy Lambert** 22:42 And move in the direction of your having rendition profile or profiles
for generating all the renditions you need for your components and then
eventually move into dynamic media and doing all that with with preset.

**Don Middlebrook** 22:45 But. Yeah. Yeah. Yeah, and we're gonna talk about renditions right today.

**Andy Lambert** 22:57 And. And actually Daniela pinged me on that earlier and I have not look at
the massive agenda that I created and I have not put renditions in
there. So I think but but.

**Don Middlebrook** 23:09 Yeah 'cause I've tried to create them and I just, I think I've fallen
short on something and it's they're not applying so.

**Andy Lambert** 23:16 But. Because it was called out like it's a hot topic then, but let's let me
step through with your. So for everybody that's on the line, I know
that Don, you're familiar with the current structure of the dam. Just touch on it for I don't know how to anybody that's not been
working on this. You've got your s s, your Hardrock support root folder
in the dam, just like you do under forward slash content for pages.

**Don Middlebrook** 23:39 Yeah.

**Andy Lambert** 23:48 And under forge live content experience fragments slash SHRSS for
experience fragments. And then at the root level you've got a folder
dedicated to content fragments which you guys are using extensively,
which is great. Recommend doing even more of it. Basically, anytime you got a structured data element that's going to be
reused and displayed in different ways throughout the site, the content
fragment is the way to go. That's good, and those are treated as
assets. You might think that's odd that they're treated as assets in
AEM as opposed to something like an experience fragment, but. took a long history behind that. They used to be straight up text files
a long time ago. Totally different. Um So and then you've got your top level site level, Daniela, maybe you
can probably speak the better than I can, but you've got your corporate
which right now pretty much everything from the content migration using
the promo was put into here. And what you know, we just talked about that it would be ideal and and
really I would say required at some point down the road to move this
stuff out of here. You're not going to have like from a performance
perspective on the end user side, a performance issue. But you're certainly going to have from an authoring perspective,
difficulties navigating, you know, trying to get through thousands of of
images and one or assets in one folder. So and there's just all kinds
of taxonomy that we talked about yesterday, governments.

**Daniela Tea** 25:23 Yes.

**Andy Lambert** 25:35 Who can upload images that you know to what sections of the corporate
site. We'll talk about permissioning as part of this there in a bit. So
one thing that is we're getting the other work stream besides the
knowledge transfers that is obviously it's a career site going live and
this is 1 case where under a corporate. Yeah, the careers assets live underneath of corporate, you know, it's a
separate site, yeah. And then the other live site reverb. And then I
guess these are all where work was started on hotels, etcetera.

**Lisa Cardia** 26:12 Could we actually acknowledge, I don't know what happened with careers,
migration of assets, but they all have like very odd names and at least
I can confidently say in site core, which that's where these assets
came from. They did not have these names.

**Andy Lambert** 26:12 And. Yep.

**Don Middlebrook** 26:19 Right.

**Lisa Cardia** 26:31 So is there?

**Andy Lambert** 26:32 Assets uh, content fragment specifically or just the all these asset?

**Lisa Cardia** 26:35 The the photography that we see, I know that Don did some renaming on
his end, so there are a few that have been renamed. But I know like a
lot of these didn't have the the same naming conventions. I think Don,
didn't we call that out that like some of the logos had like a really
weird chain of letters and numbers instead of.

**Andy Lambert** 26:38 OK.

**Don Middlebrook** 26:52 It. Yeah, I mean if you look at the file name for any of these, you know you
might have the title that might be OK, you know and then but the the
file name is like C2D5, you know like.

**Lisa Cardia** 26:55 Just the theme of it.

**Andy Lambert** 26:57 Oh.

**Lisa Cardia** 26:59 Yeah.

**Andy Lambert** 27:05 You got like I I see.

**Lisa Cardia** 27:05 Yeah. Yeah. And so we've we've noticed that for the image sources on the
page. So obviously that's an issue that it it inherited some odd string
of numbers.

**Andy Lambert** 27:10 Yeah, I see it. Whoa.

**Don Middlebrook** 27:19 Yeah, yeah. And that's for a lot of them.

**Andy Lambert** 27:19 Yeah. That's a unique identifier, probably from the prior, um, the prior CMS
system.

Speaker 1** 27:26 OK. It looks like whatever, whatever tool they use to extract that asset
from its original location pulled out some sort of like internal
reference number that you know what they use on that platform and and
kind of appended it to the name, unfortunately.

**Don Middlebrook** 27:36 Yeah.

**Andy Lambert** 27:38 Yeah. Yeah.

Speaker 1** 27:43 There there is a bolt tool that you can use in AM where you can get an
export of all these assets, edit the names in a spreadsheet, a simple
spreadsheet and and you know possibly even apply some sort of Excel
formula to remove that front end part of it and then.

**Don Middlebrook** 27:44 Yeah.

**Lisa Cardia** 27:45 I.

**Don Middlebrook** 27:54 Yeah. Yeah.

Speaker 1** 28:02 Re upload the spreadsheet in the AM and then a bulk operation won't
name everything. Yeah, yeah.

**Don Middlebrook** 28:02 Hey. Yeah, it's that renovator.

**Lisa Cardia** 28:07 I I do want to say though like my my concern is that this was the first
Sitecore site to get migrated. So whoever made the decision of whatever
application you use to migrate them that like this needs to get flagged
or else Don's gonna be cleaning up assets for the rest of his life.

**Don Middlebrook** 28:07 Yeah, I've I've.

Speaker 1** 28:15 Mhm. Yeah. Yes, that's right. Yeah.

**Andy Lambert** 28:22 Yeah, I think that I don't know if it was.

**Don Middlebrook** 28:23 Yeah, there's, yeah.

**Lisa Cardia** 28:23 So, like, we're lucky that careers is such a short, a small amount, but
this is still like, not really acceptable.

**Andy Lambert** 28:29 Here.

**Don Middlebrook** 28:29 But there's and there's still a lot of assets that aren't even
referenced, you know that were pulled over. So I mean I already
identified most of those and I used a metadata, I exported a metadata
sheet and then just re uploaded it to identify the in the title. So I
knew what you know what it was but.

Speaker 1** 28:39 Yeah.

**Andy Lambert** 28:43 Yeah.

Speaker 1** 28:49 Yeah.

**Don Middlebrook** 28:49 Which ones could to move out, yeah.

**Andy Lambert** 28:49 Yeah, on another project I used, actually got copilot to do some of the
heavy lifting. The copilot's not as good as other some other, you know,
LL NS, but.

**Don Middlebrook** 28:58 Yeah. No, I mean, we have to use copilot here, but um, now.

**Andy Lambert** 29:02 But do even with just like some if you use a regex tool or if you're
familiar with regex like you can do a lot just with like exporting CSV,
put it into like copy it, put it into a text file and then do.

**Don Middlebrook** 29:08 Mhm.

**Andy Lambert** 29:18 A search and replace on the file without actually having to open it if
it's huge for example and and then use red tags.

**Don Middlebrook** 29:22 Yeah, I I do some vibe coding with. Yeah, I do some vibe coding with
with Copilot to create Excel automations that will can do that for me.
So I know how to.

Speaker 1** 29:35 Mm.

**Don Middlebrook** 29:38 I I can do that. Yeah. And then

Speaker 1** 29:38 That's the easiest one, but the the nice thing, the nice thing about
renovator is it'll update. You know you don't have to actually
physically move the file, it can. It can just update the name that under
underlying name and republish it and update all references within AM all
in one swoop.

**Andy Lambert** 29:39 That's cool. Yeah, I got it.

**Don Middlebrook** 29:44 Yeah. Yeah. Yeah, yeah. The only the only problem with that is if there's anything
that has the same file name. So in case I wanted to move it to another
everything to a the similar folder, it won't do it. It can only do. So
you have to do it in batches, but.

Speaker 1** 29:56 Right, so. Oh yeah, yeah. Yeah, yeah.

**Andy Lambert** 30:11 Mm.

**Don Middlebrook** 30:12 Yeah, yeah. I I just recently found out about the renovator a couple
weeks ago, so I've been kind of using it somewhat, but yeah.

**Andy Lambert** 30:13 No.

**Don Middlebrook** 30:20 Yeah.

Speaker 1** 30:20 That's a good tool for damn clean.

**Andy Lambert** 30:21 Yeah, Chris ought to get paid. Chris ought to get paid by somebody for
advertising that thing every project.

Speaker 1** 30:25 Hey, as much Dan clean up as I've done. I mean, you know, you you gotta
use the best tools that are available to you and that's definitely one
of them, yeah.

**Don Middlebrook** 30:29 Yeah. Yeah. Yeah, and and when I, you know, I mentioned that there's like a lot of
things with the same file names because we did have all of the structure
of the the different language. Well, some of the same assets are, you
know, in there multiple times and you know with with the previous bulk.

**Andy Lambert** 30:34 Hello.

Speaker 1** 30:40 Yeah. Yeah.

**Don Middlebrook** 30:50 You know, migration, you would have, you know, hundreds of the same
asset in there. So, so and on that note, how can we clean up the dam
with those duplicates easily?

Speaker 1** 30:53 Yeah, it's. Well, that's why it might be good to.

**Andy Lambert** 31:02 Yeah, so.

Speaker 1** 31:06 With duplicates.

**Don Middlebrook** 31:06 'Cause there's there's the same asset with different, you know, that
we're.

**Andy Lambert** 31:10 Let's take a look at you got.

Speaker 1** 31:12 With the same asset name or you're talking about the exact same?

**Don Middlebrook** 31:14 Well, it's the same asset and we're, you know, I've been trying to
rename everything the similar, but it would be the same asset. So in
Sitecore I believe or Visigy, the sites would be set up to where you
would have. You know, like here's a cafe site and there's multiple languages in
it, so there'd be different pages and that same asset would I guess
would be added to each of those folders. So when they were migrated
over, they all had unique file names for each of those. And then you multiply that across all the cafe sites, you would have in
some cases hundreds of assets that are the same.

Speaker 1** 31:53 Mm.

**Don Middlebrook** 31:54 So.

Speaker 1** 31:55 Got it. So, uh, so it's different.

**Andy Lambert** 31:56 Yeah, think of an example right offhand to search. I just wanna kind of
search and have a business.

**Don Middlebrook** 31:58 Just just click on caffeine, go to search and then hit enter.

**Andy Lambert** 32:09 And then list them.

**Don Middlebrook** 32:11 Yeah, probably start seeing them right away. Well. Yeah, you probably have to. So if you go all the way down, so that
additional FOBG, the background image that's in there so many times,
this placeholder 1080 by 1920 is in there a lot of times and there's
certain, you know, photos and other files. It's just.

**Andy Lambert** 32:24 Oh.

Speaker 1** 32:28 Right.

**Andy Lambert** 32:31 Mm.

Speaker 1** 32:33 Oh.

**Don Middlebrook** 32:34 On and on and on like and to give you a back story, there was 130,000
assets brought over. There's only like 25,000 that are referenced right
now and a lot of those are duplicates. So it we probably only have
really half of those that should be.

**Andy Lambert** 32:35 Wow. Yeah, I saw it. It looked like you had pulled the use the assets reports
tool to get a sense of what is that what I saw on prod you were using.

**Don Middlebrook** 32:50 In the dam right now. Yeah, I I've I've done metadata exports to get all the metadata and
then yeah, and I did that. I did that to that to get information.

**Andy Lambert** 33:03 This would be. Yeah, yeah. So I ran one last night to pull all assets on pro. Yep, this
was the. So this one, Chris, was just for the photography folder. And
actually, you know, let me jump back for a second. That's a good segue
back to we're gonna need so many more damn sessions.

Speaker 1** 33:14 The one below that. Oh, OK.

**Andy Lambert** 33:28 But so the thought that Chris had yesterday, maybe Chris, you want to
walk through this like this path of doing like a legacy or migrated
assets folder and.

**Don Middlebrook** 33:28 Yep.

Speaker 1** 33:39 Yeah, right. From that for, for as an example, I was looking at was that
photography folder that had well over 1000 assets. We were even unsure
how many assets were in there. You know that which is, you know, I'm
sure has a ton of duplicates to your point. So the way to typically handle that is to create a migrated assets
folder First off, so that you can start to clean up and have a place to
put the assets you do want to keep, right? So by using that renovator
tool, getting an export of all the assets in that folder, you can then
start to move these in groups. I would recommend by. Like we've we've done out here A through Z, put all the A, you know,
assets starting with the A in one folder, B folder, C folder, so on and
so forth. And then number for any assets that's starting with numbers
or something like that, right? Because what you really want to do
ideally is get these folders down to where they have less than.

**Andy Lambert** 34:29 Mhm.

Speaker 1** 34:34 And and and I mean less than like probably more in the neighborhood of
like 500 assets per folder, no more than that because the user
experience of browsing folders with anything more than that is is hoard,
right. You don't want to do that right and and find assets and so on
and so forth and we can get to more into that searching and finding
assets.

**Don Middlebrook** 34:36 Yeah. Yeah. Right. Right. Yeah.

Speaker 1** 34:54 Process later, but so and then if separating them by first letter
doesn't do enough, well then maybe you start separating them by file
type, like put all the PNGS or all the JPGS in one folder or another
within those letter folders. Or maybe you do it by second letter AA, AB,
AC, so on and so forth. You can get as granular as necessary. Hopefully you don't have to get
too granular, right? Hopefully just that first level, the 1st letter or
character of a asset name is enough, right? So that's just in the clean
up of that and in that process to your point, overriding images that
have the same name and the same folders.

**Don Middlebrook** 35:18 Mhm.

Speaker 1** 35:33 And this whole huge migration effort, you know, that would kind of help
with that because you'd be putting them in a different folder. You'd
be starting net new in a in a folder that's designated saying here's
all these assets that were migrated and they're separated out, you
know, somewhat, you know that we can.

**Don Middlebrook** 35:36 Yeah.

Speaker 1** 35:50 You know, manage them and look at them and kind of go through them in
groups, you know? Yeah, that that's what I've seen done before.
That's been the most successful. I mean, it kind of like whittles it
down. It doesn't make it so overwhelming and just so, Oh my God, I just
have a folder with, you know, 50,000 assets in it or whatever the case
may be.

**Don Middlebrook** 35:53 OK. Alright. Yeah. Yeah.

Speaker 1** 36:09 You know so. You know, and then kind of helps you with that.

**Don Middlebrook** 36:11 Chris. I guess the the thing just kind of throw out there, but since we have
multiple of the duplicates like each of them might be referenced on this
page. So that's where the cleanup is I need to worry about is like.

Speaker 1** 36:16 Yeah. Uh huh. Each other. Yeah.

**Don Middlebrook** 36:29 How do we combine all of that into to reference that one \*\*\*? One
version of that asset is on all of these pages instead of 20 versions of
the asset are on different pages. You know what I'm saying? It's.

Speaker 1** 36:33 Yeah. And maybe, maybe you know this better than I would actually Andy, in
terms of sites, because I don't know about the tools that are available
for sites, but is there a bulk way to reassign like you want to say that
that one on line four image medium width, maybe you want to reassign
every occurrence of that asset across?

**Andy Lambert** 36:44 Yeah.

Speaker 1** 37:02 All pages to a different asset. Can you do that as our tool for that?

**Andy Lambert** 37:08 No, you would typically do it with a script and and or if, but if you
were to.

Speaker 1** 37:10 No. Yeah.

**Andy Lambert** 37:21 Thinking I'm trying to think of a way, a clever way that you could do
it by moving things around, right? Like if you had the correct image
with the right name or something like that where you didn't actually
have to update the page, the components.

Speaker 1** 37:28 Yeah, not.

**Andy Lambert** 37:36 File reference on the in the page config.

Speaker 1** 37:39 Not that I'm aware from a damn perspective. I mean, if you delete an
asset, you know if every single one of these image medium with JPEGs,
wherever it lives is being referenced in a different page location.
They're all different sizes though too, but so I don't know if that is
the.

**Don Middlebrook** 37:55 Yeah, not all of this, not, yeah, not all the solid solid sizes are
referenced. So you see the no reference there. So yeah, in a lot of
cases it's really the large version, but sometimes it's the medium
version that's referenced.

Speaker 1** 37:56 It's not even really it's not. Oh, right, you see no reference, but even.

**Don Middlebrook** 38:11 We also have Web P and AVIF assets in there too that we need to replace
with a JPEG version.

Speaker 1** 38:19 Hmm.

**Andy Lambert** 38:20 Yeah, so you could start to clean it out.

**Don Middlebrook** 38:21 So.

Speaker 1** 38:21 But even those ones with the same name, like like row four, row six have
the same asset name but different sizes. So it's even though it has the
same asset name. Oh, it's got a slightly different name. It's got the
little number in front of it. 1219419 OK.

**Andy Lambert** 38:32 And a 41, but the sizes are different.

**Don Middlebrook** 38:35 Yeah, there's, yeah. And it still could be the same asset, same photo.
That's that's The thing is in these other systems they, you know,
whatever folder I guess is put in, it generated a unique name.

Speaker 1** 38:39 No. OK.

**Don Middlebrook** 38:51 For that asset in that folder and then the next time it was loaded a new
a new file.

Speaker 1** 38:51 Right, OK. So AM does have an out-of-the-box duplicate detection that detects kind
of what you're talking about, even if it has a different asset name and
it detects similar the same asset. Exactly pixel for pixel, the same
access asset, even if it if it looks the same, but let's say it's
cropped slightly different or has an extra row of pixels.

**Don Middlebrook** 39:01 Mhm. Yeah, I've used that. Yeah. Yeah.

Speaker 1** 39:16 Pixels, or even if the metadata inside is different, it'll it'll treat
it as a separate different asset, right?

**Don Middlebrook** 39:22 Yeah, I I enabled that and I got like about 200 reports, so I don't
have time to go through all of those right now.

Speaker 1** 39:27 OK. Right. Yeah. But it has to be identical. Like everything about the image
needs to be identical. Yeah.

**Andy Lambert** 39:29 E Easy peasy, no problem.

**Don Middlebrook** 39:31 Yeah. Yeah, yeah. And that's the other thing. And some of these might be
cropped or there might be a version that is edited slightly. Or yeah,
I've been working with Lisa's team to help clean up some of that, but
it's all manual right now.

Speaker 1** 39:40 Yeah, no easy way around that.

**Andy Lambert** 39:46 Uh.

Speaker 1** 39:46 Yeah. And and that that's the only way when it when the images are different
like that and they're cropped different and all that, that that's a
manual cleanup.

**Andy Lambert** 39:50 Yeah. Yeah, there's some some of it you can do. So a lot of times when we're
doing a a massive down like restructure, we'll treat it like a content
migration project where we and just like with a content migration
project you're gonna have like one off scripts that you use to.

Speaker 1** 39:59 Yeah, absolutely.

**Don Middlebrook** 39:59 Yeah. Mm-hmm. Mhm, mhm. Mhm.

**Andy Lambert** 40:37 Want to try to use AEM's ability to when you move assets to pick up on
that and update all the references and the referencing pages, content
fragments, etcetera. Then for those, there's a section in this doc.
We're not gonna get to it today, but there is a section in this
document. That talks about the exact case scenarios when AEM doesn't
automatically update reference paths. So you'll have that as a you know
if and when we get back together we can dig into that, but you'll have
there's a a lot of information.

**Don Middlebrook** 41:04 Yes. OK.

**Andy Lambert** 41:14 About like what's going on under the hood and you know what case
scenarios that that automation is going to work and when it doesn't
stuff like that. But I wanted to step back to this. So Chris, correct me
if I'm wrong, but does does the renovator tool, is it similar to the? A bulk asset tool of days of old where you you'd start with a
spreadsheet and you do your mappings inside of it? Or does it work
totally different where you do it all through the console? And I'll ask
real quick.

Speaker 1** 41:45 No, you do it. I do them all in the spreadsheet and it only works with
two columns. You have that the column A with the path source and
destination. That's it. But your destination you can have a different
file name and it will rename it.

**Don Middlebrook** 41:48 The stores and destination.

**Andy Lambert** 41:52 OK, nice. Oh, cool. So.

Speaker 1** 41:58 Right. So if you're row two, if you put a column C with a destination
and you call it just, you know, something different, it'll rename that
file name in column B to whatever's in C Yeah, and the path.

**Don Middlebrook** 41:59 Yeah.

**Andy Lambert** 42:11 Yeah, so.

**Don Middlebrook** 42:11 And if there's another, if you wanna move it to another directory, as
long as that directory's there, you can change the path too.

Speaker 1** 42:18 Yeah, yeah, I I'm not positive, but I think it'll also create a a a
directory that doesn't exist, but I could be wrong on that. Yeah, no.

**Andy Lambert** 42:18 Alright.

**Don Middlebrook** 42:27 I don't. I haven't been successful with that.

**Andy Lambert** 42:27 So what you could do is basically so you would start out by generating
like Chris we talked about just starting with this this report right
where you we generated it for the photography folder under this in this
case it was corporate right and then.

Speaker 1** 42:31 OK. Yeah. Yeah. Mhm.

**Don Middlebrook** 42:44 Mhm.

Speaker 1** 42:46 Yep.

**Andy Lambert** 42:47 You would take that spreadsheet. That would be like your master working
workbook, right? And inside of it, maybe create another sheet where
you're doing the mapping that you're talking. Maybe add your
destination column here or create a backup sheet that's just for
migration.

Speaker 1** 42:52 Mm-hmm.

**Don Middlebrook** 42:53 Mhm.

Speaker 1** 42:59 Yep.

**Andy Lambert** 43:03 Data and then you know you start like going through it exercise by
exercise, using AI where you can to get things where you want them to
be. Identify these outliers. For example, you know there are things like
where if it doesn't have a reference at this point, you know maybe
it's again it's a duplicate name. That's a pretty.

Speaker 1** 43:03 Yeah.

**Don Middlebrook** 43:11 Yeah. Yes.

**Andy Lambert** 43:22 Solid candidate for getting 86, right?

Speaker 1** 43:26 And what I would do is like for instance like row two and three, I would
move only one of those, right? Not both. Even if it's both reference, I
would just move from one and put it in your destination folder. So then
at the end of the entire exercise, whatever is left in your original
folder.

**Don Middlebrook** 43:27 Yeah. So.

Speaker 1** 43:44 After you're all done, you know it's a duplicate and should be
deleted. Then you can look at all those assets and get a reference
report and see what is actually being linked somewhere. Go update it to
the new one that you have in the new folder. Then you can safely, once
that's all done, come back and just wipe that folder, right? Because no
longer are there duplicates in there.

**Don Middlebrook** 44:00 Mhm.

Speaker 1** 44:04 They've all been, you know, dealt with and all the references have been
dealt with. So that's how I would go about it, you know, and it's a
long exercise. It's going to take a long time, a lot of work, but
it's.

**Don Middlebrook** 44:09 Right. Yeah. I, well, I I've been doing some of this for the last three months. So
yeah, it's I'm on the right path. It's just there's different ways
to do things. And yeah, and I I'll take a lot of this in consideration
and.

**Andy Lambert** 44:17 Yeah.

Speaker 1** 44:20 OK, good. Yeah. Sounds like you're on the right track. Yeah.

**Don Middlebrook** 44:30 See what we can do. In in most cases, since there was 130,000 assets,
like most of those were moved to the archive that were were not
referenced. And then there are certain files that I knew I didn't need
anymore. I got rid of so I did X.

Speaker 1** 44:39 Hmm.

**Andy Lambert** 44:42 Where's that archive folder?

**Don Middlebrook** 44:49 Get rid of about 30,000 assets.

Speaker 1** 44:52 OK.

**Andy Lambert** 44:52 I don't. I don't see the asset folder. Is it like under the damn root
or where is that located?

**Don Middlebrook** 44:57 The the archives. Yeah, it's under SHRS. There's a top of the.

Speaker 1** 44:57 No, it was under the SHR. Yeah, it was under the the.

**Andy Lambert** 45:02 There it is.

**Don Middlebrook** 45:04 Uh, it's not. Yeah, it's, you know.

Speaker 1** 45:05 Yeah.

**Andy Lambert** 45:09 Oh.

**Don Middlebrook** 45:10 Not as organized as the other upper directories, but yeah.

Speaker 1** 45:10 In the I. And the idea of that archive folder is to have specific group access to
that archive folder of whoever needs to see that, right? So the general,
you know, damn browser population, you know, does not have access or
visibility to what's in there, yeah.

**Andy Lambert** 45:15 Hey, Chris.

**Don Middlebrook** 45:20 Yes. Yeah. Yeah, and and to that point, because definitely do not want this to be
searchable in the content, the the sites rail. So is that really just by
the setting the rules to that?

Speaker 1** 45:37 Yeah.

**Andy Lambert** 45:40 Yeah.

Speaker 1** 45:42 The. Whatever ACLS the user has when they you know who when they log in,
whatever groups they're assigned to, if they don't have visibility or
access to that folder, any search they perform won't show anything at
that. Yeah, Yep.

**Andy Lambert** 45:48 Yeah.

**Don Middlebrook** 45:56 Yeah. OK.

**Andy Lambert** 45:59 There's that and then there's also you got at the at the RBAC role
based access control level with what Chris is talking about. And then
you also have page template policies that can also define what what Dan
paths are allowed and then you have it at the component level, right?

**Don Middlebrook** 46:17 Yeah, OK.

**Andy Lambert** 46:18 In the component dialogue. Hey, hey Chris, can you talk about before?
Well, let me see if there is one last thing and one on this. Oh, two
things. I actually have to step away for just a minute, but I'll be
right back. But Chris, you can take the con and talk about.

**Don Middlebrook** 46:20 OK.

**Andy Lambert** 46:35 In terms of this restructuring and knowing that the customer, they have
dynamic media provision that they bought it, they're they're at some
point ideally going to be implementing it and using it in their
authoring.

Speaker 1** 46:38 Mhm. Mhm.

**Andy Lambert** 46:51 Can you talk about like as far as restructuring and stuff like
considerations for dynamic media? And then the other thing if I'm not
back in time is renditions. So if you want to share your screen or maybe
talk about renditions, I'll be right back.

Speaker 1** 46:59 OK. OK. OK, yeah, all right. So dynamic media. One of the things I'm seeing
right off the bat with the what you have going on here is duplicate file
names. Even across different folders, you can't have duplicate file
names with dynamic media. I mean, you can, but it just gets complicated
and confusing because what's happening under the hood.

**Don Middlebrook** 47:14 Mm.

Speaker 1** 47:24 Is when you know for as an as an example logo dot JPEG, which a lot of
people have, you know at least one asset that's name that right? You
know. So if you have that in folder A and then in folder B of another
logo dot JPEG, but they're different when you go to dynamic media,
what's gonna happen is you know one of two things depending.

**Don Middlebrook** 47:33 Yeah.

Speaker 1** 47:44 Depending on your setting, the default setting is the latter time. You
know an asset is synced to dynamic media is going to append a dash one
to the file name, so you'll have a logo dash one dot JPEG for instance,
right? So. And you won't see that in the dam. But what that will what will happen
is is when you use that asset in a dynamic media component on a page,
Dynamic Media just handles it in the background and knows this is
actually named logo dash one in dynamic media and it'll link to the
correct one but.

**Don Middlebrook** 48:08 OK.

Speaker 1** 48:17 It can lead to confusion, especially like troubleshooting the road.
It's like OK, I'm updating logo dot JPEG, but it's not updating and
that's because it's now named logo dash one in Dynamic Media and it
can get to be a mess. Another setting is across all folders. The latest
one will just overwrite the other, so the last.

**Don Middlebrook** 48:20 Right.

Speaker 1** 48:36 Last time you uploaded logo dot JPEG, it just overwrites the previous
one in whatever folder it is, but that's a setting that you set, right?
But it's gotta be something along those lines. You can't have two logo
dot JPEGS in dynamic media because dynamic media does not pay attention
to the folder structure at all, right?

**Don Middlebrook** 48:47 OK. Right, OK.

Speaker 1** 48:57 It's a flat structure, right? So you just have an image URL that has a
domain prefix to it and then the asset name and then modifiers after
that. That's it, right? So there's no folder reference. So keep that
in mind when building all this out. You don't have to worry about
folders and naming. A lot of organizations are worried about the.

**Don Middlebrook** 49:07 Oh.

Speaker 1** 49:16 Folder path being in the image URL, you won't have to worry about that,
but you do have to worry about duplicates and and that is definitely a a
concern based on what I've seen so far and what you guys have going on
here. Yeah, so yeah.

**Don Middlebrook** 49:23 Right. Yeah, yeah, yeah. I I I think that might not be, you know, a future
issue once everything's cleaned up because the duplicate names that I
was talking about are are the same image, not really the same, you know,
two different images with the same name.

Speaker 1** 49:35 OK. OK.

**Don Middlebrook** 49:46 Because we we we will, you know, work on on that naming structure. But
right now it's like I had moved all of those into the same directory
and whenever I used the move tool, it appended A1 or a two or a three at
the end of it, not a dash, but.

Speaker 1** 49:54 OK. In the dam, yeah, yeah.

**Don Middlebrook** 50:05 Um, just a in the dam. So yeah, but you know, in the end, but.

Speaker 1** 50:09 It's not, so it's it's not as bad when it happens in the dam, you
know, because the assets, AM assets will allow you to have, you know,
the same file names in different folders, right? Logo to JPEG exists and
all over the place, right?

**Don Middlebrook** 50:14 Mm-hmm. Right. Yeah. Yeah. Right, right.

Speaker 1** 50:41 That's good. The other thing too is to think about your folders in a
sense of what you want to be in dynamic media and what you don't, if
that's in fact a situation, because you can set it to where everything
in the DAM syncs to dynamic media and then whatever's published is
published. Facing. Publish in dynamic media as well, right? So there's two layers to
dynamic media. There's syncing and there's publishing, right? So when
you put a dam in the, when you put an asset in the dam, it can either
not sync or sync the dynamic media, and then it can either be published
or not published in dynamic media based on this published date.

**Don Middlebrook** 51:03 Mhm.

Speaker 1** 51:21 In the DAM, right? So you just want to keep that in mind, right? It's
much easier if you just have everything sync, everything just syncs to
dynamic media, but it's only published in public facing when it's
published in the DAM, right? That way because let's say you have a 50
MB or larger couple GB image for whatever reason.

**Don Middlebrook** 51:31 Right. Right.

Speaker 1** 51:41 Reason. You know, and you want to get it published. If in fact it's not synced
to Dynamic Media and you hit publish, then it's got to sync it, which
may take a little bit of time and then it's got to publish it, right?
So, but if it's already synced, then the publishing is instant, right?
So you know, so that's one thing to think about and that's the
setting, you know, once you.

**Don Middlebrook** 51:55 OK. OK.

Speaker 1** 52:02 If you get to the point of configuring dynamic media in your prod
instance, which I saw is not done, then yeah, you would, you know, we
can walk you through the setup and configuration around all that, right?
Yeah, yeah, yeah.

**Don Middlebrook** 52:09 Right. OK, OK, 'cause I'll need that, yeah.

Speaker 1** 52:19 Yeah, dynamic mean is a whole other beast for that. And then you know
you have your your dynamic renditions that are served on the fly in real
time, right? You know you don't have to worry about, you know, setting
up.

52:23 Oh.

**Don Middlebrook** 52:30 Yeah.

Speaker 1** 52:34 Any static renditions, but are you guys using static renditions right
now?

**Andy Lambert** 52:39 I was thinking, Don, if you want to share your screen real quick and
just show like what how you've been going about trying to do these
renditions and maybe Chris can give some pointers here in the last few
minutes of the call.

**Don Middlebrook** 52:39 Yeah. Yeah, I just created one and it didn't really apply, so I have to
remember how to get there. Hold on a second.

**Andy Lambert** 52:54 You got the master on the line with you. He can tell you in two seconds.

**Don Middlebrook** 52:54 Come on.

Speaker 1** 52:56 Yeah, OK. Where you going?

**Don Middlebrook** 53:00 Um. I gotta get in there. Um, I think there's on prod. OK, let's see. It's not. It's not the right screen.

Speaker 1** 53:24 Seeing your Yeah.

**Don Middlebrook** 53:25 Sorry. Not too many things open here.

Speaker 1** 53:31 That's common, yeah.

**Don Middlebrook** 53:32 All right. OK. That would be. It was under assets, right? Um.

Speaker 1** 53:39 Yeah, to set up renditions, that's that's under the processing
profiles there. The second panel, yeah.

**Don Middlebrook** 53:46 OK, yeah, yeah, so. Did I create these? OK, this is maybe not where I created something.
Um. Oh yeah, let's see create. Is this the right place 'cause I don't remember this.

Speaker 1** 54:02 Yeah, yeah, this is where you create renditions, the test, and then
you'd add a new rendition there, and that's where you put in the
width, the height, and the format you want and the quality of the suit.

**Don Middlebrook** 54:03 Alright, let's do test. OK, I went OK. I went around a different path to do something, so I'll
have to like go through this again on my own I guess. But if I created
this one right here, go ahead.

Speaker 1** 54:23 Yeah, so you create your rendition. Like for instance, for rendition
name, just put, you know, sample or something like that, you know, just
put a name in there, you know. Well, that's your profile name, but as a
rendition name. But that's fine too. It's fine. Doesn't matter.

**Don Middlebrook** 54:30 Yeah, sample and oh, OK. OK. All right. Sorry.

Speaker 1** 54:40 Just walking it through you so you know how to to build it out and apply
it.

**Don Middlebrook** 54:42 Sample choose JPEG, say it's 500 by 500.

Speaker 1** 54:46 Yeah, exactly. And then if it's a compression format like JPEG, then
you can do those settings there. Just leave that. You want all images.
You don't want, you know, videos or applications. So that's all set up
for you up the, you know, by default there. You typically don't have to
mess with these.

**Don Middlebrook** 54:49 1280. Oh yeah. OK, so leave that there.

Speaker 1** 55:04 Yeah, and the JPEG compression right now is set to 85 quality, if
that's good for you. I mean, you can adjust that obviously. So, so then
what you would do for that rendition, you know you can add as many as
you want. Then you hit save and then you go to the folder level, the
parent folder level that you want to apply all those renditions to.

**Don Middlebrook** 55:05 OK. Yeah, it's it's fine, yeah. Mhm. Alright, so. That means. Alright, so let's just say to it on corporate whatever. I'm not gonna
do it right now.

Speaker 1** 55:42 Yeah, so let's say you wanted to do corporate and everything, all the
child folders and everything. You do that and you select properties.

**Don Middlebrook** 55:43 Yeah. Yeah. And is it here? No.

Speaker 1** 55:53 And then Yep, processing profile right there. See the second one to the
right? Yep, that one. Then you select the. Well, why is it not showing
up? Hmm.

**Don Middlebrook** 55:58 Uh, OK, yeah. Yeah.

Speaker 1** 56:06 That's weird. Go back over to the other tab that you have open.

**Lucas Nelson** 56:11 Hey, real quick, Chris, do you do you have a hard stop? And and and Don,
if if you're getting value out of this with Chris, totally fine. If
y'all stay on Andy, Daniela and I need to drop for the next call, OK.

Speaker 1** 56:15 Yeah. No, I don't.

**Don Middlebrook** 56:23 OK. Yeah, yeah.

56:26 Yeah. Thanks, Luke.

**Don Middlebrook** 56:27 OK, yeah.

**Lucas Nelson** 56:28 All right. I I we're we're gonna drop, but you guys can stay on. OK.
All right. Thanks.

**Andy Lambert** 56:29 Thank you.

**Don Middlebrook** 56:32 Alright, thanks, Luke.

Speaker 1** 56:32 Yeah, OK. Yeah, do it that way because that that that's kind of odd.

**Lisa Cardia** 56:34 And the rest of the content team is gonna drop for that one as well.
Most a lot of the attendees are dropping for that one.

**Don Middlebrook** 56:42 That's fine. Thank you.

Speaker 1** 56:42 OK.

**Lisa Cardia** 56:42 Thank you.

Speaker 1** 56:44 Yeah.

**Don Middlebrook** 56:45 I mean.

Speaker 1** 56:46 Yeah, so do it there. Go to apply to profile to folder and navigate to
that. Any of those just do like cafe or.

**Don Middlebrook** 56:55 Yeah.

Speaker 1** 56:57 Corporate whatever you whatever you were doing. Hit apply. Yep. Now go
back to the other tab and go to that folder and go to properties and see
if it applied it 'cause it should.

**Don Middlebrook** 56:58 Yeah, and then just apply. We could cache properties.

Speaker 1** 57:13 Go to asset processing. Are are you in prod on both? Is the first time
in prod?

**Don Middlebrook** 57:19 Oh shoot, it stayed. That's why. That's why I just thought it was
wrong. Too many, too many things here. OK, now this should work.

Speaker 1** 57:21 Oh, there you go. That's why. Yeah, OK. Yeah, now I like to navigate to the folder and set it there, but you can
do it in either place. But yeah, and then go to properties and asset.
There you go. So now you have that sample and then what what happens is
any asset you add in that folder or any child folder from this point
forward would get those renditions.

**Don Middlebrook** 57:31 Uh. I did. Yeah.

Speaker 1** 57:50 If you want assets in that folder that are currently in there that have
the renditions, you have to reprocess. Yeah, yeah, you have to do that.

**Don Middlebrook** 57:53 You have to reprocess. OK, so. Let's see, photography. Reprocess.

Speaker 1** 58:06 Yeah. Yeah, another thing real quick too, just to kind of let you know that
under that the root level when you're navigating the folders that has
that bind similar that if if you've got smart tags on all your assets
and you process them with smart tagging.

**Don Middlebrook** 58:22 Mm-hmm.

Speaker 1** 58:28 That's helpful in finding all the assets that are similar but crop
different.

**Don Middlebrook** 58:34 Yeah, I I've used that. It it doesn't OK job from from what from our
asset perspective. So um, it doesn't do all of them.

Speaker 1** 58:40 Yeah. Yeah. The only way that works though is if the all the assets that
you're you're hoping to find have been processed with smart tax.

**Don Middlebrook** 58:51 OK.

Speaker 1** 58:52 Sample dot JPEG. So there's a rendition, yeah.

**Don Middlebrook** 58:53 Right, right, right. There's that render. OK, OK, that's where I was.
OK, I'll have to go back and see what I did before cause that wasn't
OK.

Speaker 1** 59:03 Yeah, you might have been editing. There's another way that used to be
a legacy way to do it in the workflow for asset processing and but you
don't want to do it there.

**Don Middlebrook** 59:12 Yeah. Mhm. OK, so just right.

Speaker 1** 59:16 Yeah.

**Don Middlebrook** 59:19 Yeah, was it first? OK, all right, sample. OK, all right, that's good
to know. And I guess that with that said, we now we create these. Now
how do I apply them to an asset that's an?

Speaker 1** 59:20 Processing from file. Yep. Yeah. Well, if you're using the component, if you're using an AEM component,
a default, not a custom component. And just because I can't speak to
whether the custom component supports it or not, but a default
out-of-the-box image component in AEM site building will automatically
select the rendition that.

**Don Middlebrook** 59:34 But.

Speaker 1** 59:50 That is appropriate for the placement.

**Don Middlebrook** 59:53 Oh, it automatically do it. OK.

Speaker 1** 59:55 Oh, Mac does it. But if you have custom components where you didn't
utilize that functionality in the code, then it may or may not do it
right. So that's kind of you have to build in that support into the
component that you're placing it on. There is a direct URL that you can
manually do to get to that.

**Don Middlebrook** 1:00:03 Yeah.

Speaker 1** 1:00:14 To that rendition, but it it's not straightforward.

**Don Middlebrook** 1:00:15 And then. OK.

Speaker 1** 1:00:18 It's a little cryptic.

**Don Middlebrook** 1:00:21 OK, alright, so just reiterate. So if I created a bunch of different
renditions here and this says it's it's still static, not OK, OK.

Speaker 1** 1:00:23 Yeah. Oh, oh. Yeah, it's static. Because it it actually creates a binary file, a separate binary file
under the hood and stores it for that rendition. That's what it means
by static. You're actually the more static renditions you create, the
more copies of that asset you're creating under the hood.

**Don Middlebrook** 1:00:41 Oh, OK. Mm-hmm. All right.

Speaker 1** 1:00:50 OK, that's what's so good about dynamic media is there's no binary
stored as generated on the fly. Yeah.

**Don Middlebrook** 1:00:53 Right. OK. OK. So yeah, when we get dynamic media implemented and then
that's probably what we need to be doing and then we'll have to have
that.

Speaker 1** 1:01:04 Yeah, and utilizing image presets because image presets function a
little bit like what you're kind of used to with with the static
rendition where you can name a preset sample or whatever. Or typically
you name the preset for the the use case or where it's being consumed
on your site like a carousel or a banner or something.

**Don Middlebrook** 1:01:15 Mhm.

Speaker 1** 1:01:23 You name that preset and in that preset you define all the width, height
parameters and the format and the compression and all that stuff, right?
So then in the image URL you can just reference that preset because the
other way to go about it is actually hard code all the modifiers and the
parameters into the image URL into the component. But if you do that.

**Don Middlebrook** 1:01:24 Yeah. OK. K.

Speaker 1** 1:01:43 You wanna make changes and you have to update the component code and do
code deployments and all that. But if you reference a preset name, if
you reference a preset name and then you need to make changes, you just
go edit the preset and republish it and done. Everything referencing
that preset gets the new parameters, right? So yeah.

**Don Middlebrook** 1:01:47 Yeah, we don't wanna do that, yes. OK, OK, alright, so.

Speaker 1** 1:02:02 Yep. But yeah, for time being, I mean static renditions should help you out
in in a lot of cases and as long as you're offering in in AEM, you know
it'll it'll just do it for you.

**Don Middlebrook** 1:02:15 OK. All right. That sounds good. Yeah. OK.

Speaker 1** 1:02:16 Yeah. Cool. Any other questions? I'm sure we'll have a follow up calls and
talk more about all this good stuff, yeah.

**Don Middlebrook** 1:02:21 Yeah, that's cool. Um. Yeah, I think, I think it's good for today. I appreciate your time and
then looking forward to us having the dynamic media because that's
really what I wanted to really wanted to cover, but since we don't have
it implemented yet.

Speaker 1** 1:02:31 Yeah, no problem. Yeah.

**Don Middlebrook** 1:02:42 Then we just wait.

Speaker 1** 1:02:43 Yeah, I mean it's it's it's connected on your lower environments, but
your prod just isn't connected. It's not set up.

**Don Middlebrook** 1:02:50 Yeah, yeah. So, OK. All right. Well, thank you so much.

Speaker 1** 1:02:53 Alright. OK, talk to you soon. Bye.

**Don Middlebrook** 1:02:57 Alright, alright, bye.

Andy Lambert** stopped transcription



## Session: Shared Data — 2026-02-19

**SHRSS Adobe Knowledge Transfer-20260219_130217-Meeting Recording**

February 19, 2026, 6:02PM

1h 31m 52s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:09 All right, we're off and running. Daniella, if you want to kick us off,
thank you.

**Daniela Tea** 0:12 Yep, thank you for that, Luke. Hey everyone, good afternoon. I wanted to
start today's session with going over just a couple of updates from
yesterday's meeting and I am planning on sending an e-mail reply. To the landing page meeting from yesterday, just so that way anyone who
wasn't able to attend will still be able to see those answers. But want
to provide a few updates. So yesterday there was a question about the
component specs page that our team had provided and. I just wanted to share my screen so you guys can see this here. Our team
is reviewing this page. You might notice if you guys are looking at the
title of analysis under review 219. Just so the team is aware, we are
taking a look at this to essentially verify all the information. That's put here and then if you know anything needs to update, we will
be making those changes to the information here. But I will be letting
you all know when our review is complete. So right now it's in
progress. So more to come on this, but just want the team to be aware
that that's. Something that we are currently doing. The next thing I wanted to share
with the team is there is a question about how to handle vanity URLs for
that specific page and I want to show you guys how that is done after I
talk to the tech team. So right now I'm in the product environment I'm
going. To navigate to the International Women's Month page that I believe the
authoring team have been working on. So let's just take a quick look at
that. So this is my copy. Let me find the other, the actual version. Here it
is. OK, so you can see it's still not published. So we did not publish
these changes, but we did add the beta URL and so I just wanted you guys
to take a look at how this process is done. O I'm going to select the page and click on properties. I'm going to scroll down here. So after talking with the team and I and
we confirmed what was the original rule that was captured for slash
woman. So you'll notice that's not here present in the Vandy URL
section of EEM because that's already being handled. At at the dispatcher level. And so for our best practices, typically you
know if something is being handled somewhere else, you don't want to
replicate it or duplicate it with an AEM. However, since this is a brand
new rule for this empower women URL, that's why you see this one here. So the way that we added the beta URL as you can see is you need to put
essentially the complete page path. So you'll see content SHRSS
corporate Hard Rock EN. That's the exact same section that this
specific page is, although it's hard to see with the percent twos 2FS. But it's in the same exact location. But then at the very end that's
where we put what we want the VAD URL to be empower dash women and then
also putting that extension of dot HTML. The reason why you need this
dot HTML and there's as I mentioned yesterday there were some. URL shortening rules that were put in place and so that's why because
that rule is looking for an extension to then remove. That's why the
when you put this bid URL in place here, you do meet this extension in
order for it to also pass that rule. So moving forward, as the team needs to add additional van URLs, this is
the format it should be. Again, the page path is here of where the page
is located and then also just the desired URL of the page with the
extension. And yes, I can add multiple. In the case, as mentioned before, the reason why I didn't put the women
one here is because that's there's already a rule, existing rule that
we saw that was in place that is active right now. So I'm going to
pause here to see if there's any questions about vanity URLs, the
process to do it and essentially where to go for. Accessing this.

**Edwin Aquino** 4:28 Yes, Daniella, can you explain what the redirect vanity URL checkbox
does as well?

**Daniela Tea** 4:33 Sure. Let's see. I noticed that my tech team member did not put this in
place. Let me get back to you on that one, Edwin, I believe. I don't
want to give you the wrong information, so I'm going to. I'll get back
to you on that. In this case here though, it was not needed and that's
why we didn't put it there, but I'll confirm the exact. Reason and the use cases for when you would use that.

**Edwin Aquino** 4:55 OK. Thank you.

**Daniela Tea** 4:57 Yep. Anything else? OK, all right. So to be clear, this one is in place. So whenever that
page is ready to go and ready to be published, you will not need to add
any additional data URLs. However, of course, if there's something
else, another one you need to add, please do so and then make sure to
publish the page. All right. I'm gonna hit cancel. All right. OK. And then the last
update, there is a question about the card. Yes.

Lyon, Rick (Director of Digital Experience)** 5:25 Hey Danielle, sorry I had to click all the terms and everything on that
last screen you had with the my understanding correctly, you can have
multiple vanity names for that page and they'll all link to it. Oh,
that's pretty cool because they I ironically with this one.

**Daniela Tea** 5:28 Yeah, go ahead. Yes, that's correct. Yes, that's correct.

Lyon, Rick (Director of Digital Experience)** 5:43 We had noticed one URL was in the PDF and a different URL was in the in
another image. So it's like in how many different iterations are there
possibly floating around, you know, before the program launches. So if
we had the ability to add multiples, that would be pretty cool.

**Daniela Tea** 5:55 Hmm. Yeah, you are able to add multiple. I don't. I think the only other
I'm trying to remember what we had saw. So to be clear, there are
there's another location where like redirects of ADRLS can also
potentially be managed those individual roles that have been. Available in Visorj, I believe had just gotten migrated over and
they're in our dispatcher and that's where I believe like the tech
team would be managing those. So I think there are actually additional
redirect rules are probably in place right now, Rick, but but for like
the ones that you, you know don't exist that this is the location.

Lyon, Rick (Director of Digital Experience)** 6:29 Mhm.

**Daniela Tea** 6:39 Where you would want to put them.

Lyon, Rick (Director of Digital Experience)** 6:41 Yeah, the landing page kind of thing, because that happens some you know
where they want, you know, it's a really long page name, but in print
they don't want to print that. So it's just like an abbreviation, 3
letters or something. So be able to add that quickly here as people.

**Daniela Tea** 6:47 Yeah. Right. Absolutely. Yeah. Yep. So yeah, sure thing. All right, so the follow up I have is for the
use cases for redirect bid URL checkbox. I'm gonna hit cancel for right
now and then we wanted to talk about the updates.

Lyon, Rick (Director of Digital Experience)** 6:56 Thank you.

**Daniela Tea** 7:10 To the card carousel. All right. OK, so previously it was asked about
what the Adobe response was for why the UI was getting cleaned up. After
talking to my team, what we had noticed is that, excuse me, based off of
the requirements. That we had seen previously and I can get the exact ticket number in a
second. As mentioned before, desktop and desktop and tablet typically
would have the same sort of view and mobile would be handled separately.
This particular component previously had this separated, however. After that specific requirement was made, what we did was we our
understanding was that card carousel and tablet should always be two if
it's not a full width carousel, if it's a full width carousel, which I
will. Let me see if I can show you when I say full width carousel, I'm
talking about within the hero banner. Let's see if I can find an
example. Something that looks kind of like this. If it's full width, then
you're only going to show one at a time. However, for this instance
here, the fact that I have one this, this particular number does not
actually do anything for tablet. That's the reason why our team had
responded saying that this particular. Field doesn't actually need to be here because there's already logic
baked in without the author having to configure anything. So if I were
to take a look at this page here, we see three here, we see two and this
would technically be tablet and then we see one. So what's being
respected is the. Three and the one that I've put into place, but that middle number for
tablet, there's nothing like this does not take into consideration what
this value is. So if I were to put this as five, you can see nothing
will happen. It'll always be too. And so you know, totally understand if that's not
something that is desired, that's where during the gap portion, if that
if that specific functionality for a tablet needs to be added again. So
that way this actually, you know, a tablet can have something
different. That's something that we would want to make sure is covered in the gap.
But when we said we were going to clean up the UI, we were saying we
were going to remove this field because currently it does not have any
bearing on how it's displayed to the end user and there's already
logic that was added to always show as to. All right. OK. So those were the updates that I had from yesterday. And
any any questions? Yeah, Don, I see your hand up. Not sure if that was
intentional or not.

**Don Middlebrook** 10:00 It was not intentional, sorry.

**Daniela Tea** 10:02 I just, I just happened to glance and see and I was like, oh, OK.

**Don Middlebrook** 10:06 Well, I was gonna do the React thing and I hit the wrong thing, so never
mind.

**Daniela Tea** 10:09 No problem. Thank you. OK. So yeah, any other questions about the page
and actually with regards to the author team, you know, I know that
yesterday it was said that there could be some additional changes. So I
was just wondering if. There is anything else that you guys wanted to talk about with this
specific page for today?

**Edwin Aquino** 10:36 I believe there's not been any large changes yet. It's still possible
for it to be changed, but I I don't. I'm not aware of any large
changes yet, so we should be OK for now.

**Daniela Tea** 10:38 OK, yeah, understand. OK. OK. Thank you very much, Edwin, for that. All right. OK. So let's
jump on over then to the, the, the agenda that I had prepared for today.
So as I've been talking to you guys over the past couple of weeks, you
know I.

**Edwin Aquino** 10:47 OK.

**Daniela Tea** 10:59 I definitely understand that there's going to be a lot of instances
with shared data. So essentially if something on the hardrock.com
website, you might want to also see that on the careers website. I think
we've identified a couple of examples of that and so I think that it
would be good to understand like how to identify. These particular pieces of data that are going to be shared across
multiple websites. Which is the best time to use a content fragment?
What's the best time to use an experience fragment? Once you use a
content fragment with an experience fragment or even experience fragment
with an experience fragment? And so I just wanted to review some of the things that I've identified
that could potentially be useful as the team is authoring pages moving
forward. As you guys know, we had a set number of content fragment
models that we had created. However, that doesn't mean that that's all
you. You guys will end up using. There's gonna be a lot of times where
you're looking and you're seeing, oh, this data has some sort of
structure, it's repetitive. We should create a content fragment model.
So I just wanted to show you guys like some of the things that I
identified and how I would make that into either an experience fragment
or a content fragment and how that could potentially be. Used across multiple sites. In addition to that, you'll notice here
I've called out the components that are used specifically within the
header and our footer, which are some very obvious examples of
experience. I believe we actually have gone through these in a previous session
before when we were reviewing the home pages for corporate, but we can
certainly just take a look at them again today since we are trying to
review experience fragments. And if you guys have any questions about
those, we can certainly get into those too. All right, so I'm going to actually start now with showing just two
examples of what I could think would be some good shared data. Last week
we talked about this particular page and and there's actually a very
similar page here on the. Careers website. However, there are also some differences that we noted.
Some things might be shared, some things might not. So now obviously
this is going to be more of a a hard rock would need to decide are these
pictures truly supposed to be different on this page or would it make
sense for them to be a one-to-one match? So depending on that answer, that would actually depend on whether or
not this would be a good candidate for a content fragment or an
experience fragment. If these were obviously one to one match, say you
always want to be in this card format, you always have the image and
this text here that would make sense to be an experience fragment. You
would then. Use the experience fragment wherever you need to show this particular
card, and then you'd only change it in one location. However, because
I'm seeing that there are some slight differences, but some of it's
shared, what I would say if that was indeed intentional is that it might
make sense for this. To be actually a content fragment with a content fragment model. So let
me open up down here and I went down to the integration environment just
so that way people aren't accidentally using this and what I did was I
actually created a. New content fragment model called bio. I'm just gonna navigate to where
I have put my information. Was it careers? Oh, oops, sorry, I'm not in
the DM. Here it is. OK, so going to my CF folder and here I have a folder called
Biography because I created something called a biography content
fragment model. I'm going to have you guys just take a quick look at it
and then I'm going to show you how I actually created it. All right, so clicking edit. So you'll see here I was taking a look.
OK, what are some things that are relevant, you know, that are shared
across all these different pieces of of content on that other page? So I'd identified the name. I split it up in first name and last name,
but that could certainly have just been one field. I identified the
title, the bio, and then also the image. So you can see here exactly how
I split it up. This is the shared structure that I would imagine all
biographies. Would use and so all that information that's on here I have now
captured as a content fragment. So when I create when I created that
content fragment model, here I am in the content fragment model editor
and you can see the exact fields that I selected for this. So for my first name I have my text field and I believe this and correct
me if I'm wrong. I do believe you you all probably covered some of this
within the training in terms of how you can have different types of
fields and also different types of validation. So I'm not going to get too deep into like what each of these fields
mean. However, I just wanted to just show, for example, like you know,
using the different types of field and what makes sense in this case for
an image using a content reference, setting my root path to the dam so
that way whenever someone. Creates a new content fragment based off of this model, it will always
default to the DAM. If there's a specific location that you know these
images always are based off of Don's new structure, then it would make
sense to set it exactly where you need it, but just trying to show you
how. When creating these content fragment models, the important thing is
understanding that the structure needs to be shared across everything
that's going to use this, and you want to make sure that you know
you're putting the proper validation in place. For example, in this
case, I don't want someone to necessarily select like a content
fragment here. I want them to only be able to select images. So you can see I I've
like essentially put some guardrails in place as I was making this
fictitious content fragment model and as additional. If there's
additional fields that I need and maybe they they aren't necessarily
required, I can add those. In this case I only set the. First name to be a required field, but certainly it's possible that I
would imagine you might want to have first name, last name and title all
be required. So that of course is a decision that would be coming from
the, you know, the SHRSS team, probably the product team or so on
determining. When, when should something be required, what should these fields be,
etcetera, etcetera. But this is the way to essentially build it out and
to make sure that you're essentially guiding your users to be able to
fill this out properly with the specific validation and things in
place. So I'm actually going to pause here as we take a look at this editor to
see if there's any questions about how I essentially built this
fictitious model. All right. OK. All right. So let's jump back then to the actual content
fragment I built based off this model. All right. So if this were a a
real life scenario and say we this particular content fragment model has
been approved by everyone as in like these are the. Exact fields we want and the way we want them. Simply as a content
author, what I would be doing is I would be getting all that information
for each one of these, creating a new content fragment, filling out the
fields, etcetera, etcetera. And so then these would all be stored as
content fragments as opposed to right now. I believe these are probably
either card or. Text components. So moving forward, what I would need to do is instead
of editing anything on the page, I would be editing it from a content
fragment perspective. So right now on the hardrock.com corporate site, I
believe you have to edit directly in the page. But if you were to use a content fragment model, as you guys know, you
would be editing the information here, saving and publishing, and then
that is what would determine what content is being displayed on the
page. So looking at. This here we can see one of the reasons though why I chose a content
fragment model versus doing an experience fragment is because there's
things that are not exactly the same. So in this case here again, this
is a card. This is instead showing the shared fields. These two and the shared fields here you know is right here. The image
is different. There's a read bio button here so that none of that is
shared between these two. So within my let me show this here. How do I display these fields on the page though? All right, so I'm
going to navigate to just creating a test page where let me see if I can
find it. Uh, here we go. All right, so out-of-the-box there is a a content fragment component,
and its purpose is to essentially surface information from a content
fragment, a stored content fragment. So you'll see here I have a
content fragment component on. Here and what I've chosen to display is a the bio field from the
selected content fragment that I have. So you have the option of
choosing a single text element or multiple elements. This is an
out-of-the-box component, so there's been no customization to this. And so this is something that yes, you can use. However, there are
certain fields that are not going to work out-of-the-box and would
require some some some customization too, for example the image field. The image field is not going to display the actual image right now
without any customization. It displays the location of the image. A
typical use case though would be for a developer to essentially create a
custom component that is relying on that content fragment. So when we have our content fragment card, if you guys remember, this is
a custom component that our team made and surfaced and so it's calling
in content fragment models here. And what we're able to do is we're
able to pull in the same information that's stored in the content
fragment, but we've included a. Additional code to say, for example, display the image or style things a
certain way. So I want to be clear that just because you create a
content fragment model, it's not going to magically look like a card.
There's going to have to be some discussion amongst how you would want
that information to be displayed. But out-of-the-box, what you can do with the content fragment model
component is display different specific fields that are stored within
the content fragment. So I'm just going to call. This content fragment again and just show how if I were to want to
display say the title, I could do that here and it it displays my title.
If I display let's say a bio, I'll display my bio here. So I can. I also do have some control when it comes to paragraphs. Right
now I'm showing everything. Say I just want to show the first
paragraph. I should be able to do that. So this is the content. So the
content fragment component again is a way to display pieces of text from
your content fragment. However, if there's obviously like image fields or things that need to
be displayed, that does require some customization.

**Edwin Aquino** 23:13 Daniela, with this text that we're seeing here, will this at least
inherit the the stylings and everything that we have of the website?

**Daniela Tea** 23:17 Hmm. But inherit the style. So I believe this is. Let me check what that
field was one second. Let me go back 'cause there is actually a rich
text editor that can be used within the. Content fragment model, but let me check what I have that set to. It
should be I believe the body text, right? So like right now this this
font should be. Let's see what the font is. It should be whatever the
body font is saved within the in the style sheet. Yep, so font family,
font family. So Lato, I believe is what the font family is. So when you say inherit,
that's it is essentially inheriting whatever was in the style sheet.
Does that make sense? OK, Yep. But yeah, let's take a look at this
really quickly. I believe I just create. Yeah, so this here is a multi
multi line.

**Edwin Aquino** 24:00 OK. OK, yeah, yeah, I just wanted to make sure.

**Daniela Tea** 24:16 Text field. However, there is the ability to change it from plain text
to rich text, but in this case I didn't necessarily want like the
styles to be, you know, people putting whatever. So and again this is an
example, but also another decision. Um, or something to consider when you're planning out building out your
content fragment models. Right. Um, so with what we're seeing here, any questions about why I
would use a content fragment for this and and essentially the shared
pieces versus an experience fragment?

**Edwin Aquino** 25:00 I do have one question regarding the actual creation of the content
fragment. Now is there any way for us to include a default image for
that? Like let's say when we're creating the content fragment model,
are we allowed to create put in a default image that's going to be
there no matter what and we have the option to override that image?

**Daniela Tea** 25:03 Sure thing, Yep. Mhm. So we do have a default value that can be set. So I believe you should
be you should be able to select like a. In this case this is keeping in
mind this is a content reference which I'm using for image. I should be
able to set that default value and then as it as I'm creating new
content fragments that would be there. And then I would be able to replace it. But because again, there's no
custom component associated with this content drag model, you wouldn't
actually be able to see it right now. But yes, you are able to put
default values in place.

**Edwin Aquino** 25:51 But any specialized content that we have, any kind of a special
components that we have would be able to show that defaulted image.

**Daniela Tea** 25:59 Any special oh oh, so it's like, um, you're saying like if they're.

**Edwin Aquino** 26:03 Like if we're using a card component or something that references this
content fragment, it would show that default image.

**Daniela Tea** 26:09 There's a card to put. So the what would happen is that say this image
field would essentially inherit whatever was stored in the default
value. Does that make sense? Yeah, I think that answers your question,
right? OK, perfect. Yep.

**Edwin Aquino** 26:18 Yeah, yeah. It should be good.

**Daniela Tea** 26:25 OK. Uh, any other questions about the content fragment model? OK. All right. OK. So let's take a look now at another example that I had
identified as I was reviewing the sites. So I think it's probably the
same day when we were reviewing careers, we had noticed that. There are benefits on, of course, the benefits page, but then also on
the home page. However, you'll notice there's a slight difference.
While essentially the image and the title under each benefit is the
same, you know there's some text that's present here, but not present
on here. So what is the best way to handle something like this? Since the
presentation is essentially the same with just one thing removed, this
seems to be a good candidate for an experience fragment. So let me show
you guys how I would do something like this. Now I'm going to go up to the stage environment since I have some
examples there. Previously again, I was on int just because I didn't
want anyone to actually use this thinking it was real. So when you're
on stage or prod, you're not going to see this, so don't be alarmed.
It's just this is for training purposes. But now that I'm in stage, let's go to our Experience Fragment
section. OK, where's my training stuff? OK, here we go. So I started making just
one example, the annual bonus eligibility, and let's take a look at
what I have done. OK, so here you can see I have my image, I have my text, I have my my
other text which is essentially what we see here. So I've identified
all the all the parts to like what this benefit would require however. I also know that I don't necessarily want this piece to be on the
homepage, but I do know that if I were to change, say, the title or this
particular title portion for annual bonus eligibility, I want to make
sure that gets pulled out to both pages. So what I've done is I have created a variation as live copy. So what
that does is once I decided what I want the original to be, I then have
created a copy. We can do another one create variation as live copy.
Let's just call this test. And then it's going to be test and I've created. I've hit done. So
here's my copy of test. It's the exact same thing. So if I don't want
this portion here, but I want everything else to be the same, I'm going
to select this. And I see that there's a button called Cancel Inheritance. What this
means is now if I cancel this, I say yes, I don't want that. If I
cancel this, anytime I make an update to annual bonus eligibility, this
part will not be updated. The other parts will be, but this portion won't. So let's actually
test that and we're going to put this is not inherited and see what
happens. OK, going back to my original copy, the annual, I'm sorry, the
original experience fragment annual bonus eligibility. Make a change to this text. And I'm going to hit done and right now nothing's going to change
because I haven't rolled anything out. But if I select this, you'll
see that there's this button that says roll out. I have the option to
be able to roll it out to all the variations that are essentially
inheriting from this or. Hit roll out to and I can select exactly which ones I want to have
rolled rolled out to. So in this case I was messing around with my test
one, the homepage one. I think that's something I probably made
earlier, so I'm just going to uncheck that because I don't. I
personally don't want that to be updated right now, but I do want test
to be updated. O I'm selecting this. I'm going to hit roll out. I just happened now, so I'm just gonna hit now. I'm gonna hit
continue. Alright, so if we were to go to annual bonus eligibility, the
update I made for training is here and I go back to test, you'll see
the training has been updated and this text was not touched because I
canceled that inheritance. So what I'm trying to show is that for this particular section here,
right now everything that I believe is probably just on the page, so
you're editing it there. However, one thing to consider is this could
potentially be moved to an experience fragment. You would use the experience fragment that's that's here to be
displayed on this page and then on this page here the home page you
would likely want to use the experience fragment for test. Pretend this
is this part doesn't exist so that way it displays exactly the same and
then as as say on you know something changes like. The image here or say the title here, you only have to change it in one
location, that original experience fragment and then roll it out to
anything that's copying from it. I'm going to pause here to see if
there's any questions about this or any thoughts about, say, some other
use cases. I've identified some other use cases I think could be good
for this. I just want to hear any questions first.

**Edwin Aquino** 31:58 So regarding this component, is there any way we can break the entirety
of it being a variation? Let's say for example we have it as a
variation where you have one that doesn't have the text, one that does,
but we decide to change the order on one page. So we'll have annual
bonus eligibility on the 2nd row instead of the first, but we want to
keep.

**Daniela Tea** 32:05 Mhm. Mhm.

**Edwin Aquino** 32:18 Bit the same on the other page. Is there any way to undo that and break
that connection so that we can just use it as a regular component itself
or we would have to redo the component?

**Daniela Tea** 32:26 Let me let me confirm what you said, just to make sure. OK, so taking a
look at this, we're saying what if we actually want this to be
underneath? Is that correct? For like a variation of this to be underneath.

**Edwin Aquino** 32:40 Um. Let's say we wanna change the position on the page itself, right? So
we're not changing the component, but we're changing the position. Um.

**Daniela Tea** 32:46 Oh, the page itself.

**Edwin Aquino** 32:53 Is is there any way we can just maybe break the component itself or
there's no reason to break it? We're OK with the way it's set up.

**Daniela Tea** 33:02 When you say component, to be clear, the experience fragment is
containing right now it's containing 3 different components, right? So
I have my image, my text and my text. I can drag. I actually can drag
pretty much anything into here. I can even actually add an additional
experience fragment and we can talk about when this would be a good use
case for this. So I guess I I just wanna confirm what like what you're asking because
this is essentially like a mini page, right? Like you're adding your
components here, you're able to adjust it. And then what happens is on
the actual page that you're authoring, you would add your experience
fragment component.

**Edwin Aquino** 33:30 Yeah.

**Daniela Tea** 33:41 Let's do that right now. I'm gonna find a test page and just add the
experience fragment component. Experience fragment I just built. I think
it's.

**Edwin Aquino** 33:50 Basically, to clarify it, but if we just wanna break that connection
from the experience fragment and have it as its own component, would we
have to recreate the component?

**Daniela Tea** 33:52 Yeah. As its own component, as in like do I? If you want this stuff here
that's stored here to just appear on a page without being an experience
record, what would you need to do for that? I see. OK, one second. So
going back here.

**Edwin Aquino** 34:08 Correct. Yeah.

**Daniela Tea** 34:16 1st I'm just gonna add the experience fragment so you can see that
reference on a page and then we will address what you just asked. So I
added my experience fragment component. I'm going to then find the
specific variation that I built. Where is it? Uh, yes, here. OK. OK, so here's a variation I built. So you're saying, oh, but I
actually want this to be, you know, not with an experience for
everything. I want everything to be here. So I guess one way you could
do that is you could theoretically copy out the different parts and just
put them on the page, right? You would have to likely do some
formatting, but you can. And certainly because again, this is all actually for the ease of use,
I'm going to put everything within a container and then copy out my
container. So one second please. This one here. OK O for the ease of use, I'm going to copy out my container. I'm
going to put this here. Yeah, so you could see this. This is actually now. Here we go. Yeah, let me refresh the page just to make sure that I'm
able to access. Here we go. So now instead of me editing it within my
experience fragment, I just copied over the components, slapped it onto
a page. This now has no. Inheritance associated with the experience fragment. It's, you know,
like this could be anything, right? So any rollouts and anything that's
made to this, it's not going to affect us at all because now it's just
three independent components within a container. Is that what you were
you're asking?

**Edwin Aquino** 36:07 Yeah, that's exactly it. Just wanted to see if you can break the
association. That's all.

**Daniela Tea** 36:09 OK. Yeah, yeah. So two ways. Again, there's two ways. One is when you have
a variation, you can. If you do not, if you actually don't create
variations live copy, then there's actually no inheritance. It's
essentially like grouping things together of of. Like like experience targets, but variations live copy. There is that
ability to break the inheritance within the variation by cancelling it
or like I just showed, just copying out the components, slapping on the
page and now it's local on this specific page only with no inheritance.
OK.

**Edwin Aquino** 36:45 OK, perfect.

**Daniela Tea** 36:45 Yep. Any other questions about this specific experience fragment? And
for the purpose of this, I actually want to show. Sorry, I'm going to
add the other variation as well. So we can see how both of these, how this would essentially work. Where
is it? That is test, right? Yeah, OK, so you can see how like in this
case this would go on one page, this might go on another page, but
again. Anything that was marked as inherited will only have to be changed in
the original experience from it, OK. All right. OK, let's take a look at. Some other examples that I was noticing that could be potentially good
candidates. Sorry, trying to get my bearings straight on here. OK, so I
had mentioned earlier, hey, you might actually want to use an experience
fragment with an experience fragment, which sounds crazy, right? However, not always. As we know, footers and headers are all experience
fragments. I believe that the the authoring team, you guys have probably
had to edit the headers and footers on maybe the corporate page and
probably also when you review the careers page, there might be some. Updates and you would do that by going to the Experience Fragments
section. Now something that I was noticing as I was reviewing is that
sometimes the copyright here I notice it's not shared across all the
sites. There's some different variations of it, however it seems like
the. Lines of businesses all seem to have the shared copyright for it. So
like, for example, hotels might have a certain copyright, like it might
say like something about privacy in this statement here, but then I
noticed on cafes might be a little different. So when I saw that, that
to me seems like it would be a good case to make, say like. Different disclaimer experience fragments and then within your footer,
adding that experience fragments to the footer. Since right now the way
we have this structured is that every single every single cafe, every
single hotel, each one has their own. Header and footer, right? So as an example, but each one has their own
individual header and footer. So right now what you would have to do
with this not being an experience wagon is you or the property owner, I
suppose would have to make sure that the header and footer is updated. With the correct text. So anytime a year changes or anytime if something
ever changes here, you'd have to update that for every single property.
What can be done instead is say we had in our hotels, we had another
experience fragment that was just called disclaimer. That disclaimer would have one text field this and then what would
happen? This would require some updates, but it would only be one time
is within the footer. I'm just going to open this for an example
instead of having this text component here, adding that experience
fragment there and then pointing to that disclaimer and then. Moving forward from then on, you would only have to change it in one
place and then everything that's using experience framing would then be
updated. So that's something that I noticed. Again, it seems like you
know. You know that that obviously like right now the text, yeah, it's pretty
easy to change it, but if you're changing a bunch, that might take a
little bit of time. So just want to call up another example and a way
when you might want to consider using experience fragment within an
experience fragment, in this case the footer. So while we're taking a look at the footer right now, just out of
curiosity, is the team aware of like, you know, any other say any other
examples of places where you know, maybe it makes sense to make a
content fragment or maybe it makes sense for an experience fragment. Is
there anything that? Perhaps at the top of y'all's head that perhaps we can take a look at
right now.

**Edwin Aquino** 41:04 Experience fragment within an experience fragment. Same thing here, just
in general.

**Daniela Tea** 41:07 No, just I guess just in, yeah, just in general like I know for one of
the things that I believe will be handled in the future is like say say
these these cards. So here this is an example. I believe we identify as experience
fragment. I know there's additional logic. However, what would happen
is this carousel would be put in experience fragment and then replacing
the carousel that's on the page for the experience fragment. So this is
a perfect candidate for experience fragments. So I'm just curious. If there's any examples that you guys like to take a look at.

**Edwin Aquino** 41:54 Believe one experience fragment was wherever we have a specific card on
the cafe pages, it would be pointing toward a promotion.

**Daniela Tea** 42:00 And. Let's take a look at that. Are you talking? Oh, OK, sure. Does that land? Yeah. OK, Yep.

**Edwin Aquino** 42:05 So if we go to a specific property, like if we go to a specific property
page, sorry. Yep. So that third card that we see right there that says Captain Messy,
this is shared across multiple properties and it changes for some, but
not for all. So that's something that we definitely wanna consider as
maybe something along the lines of an experience fragment.

**Daniela Tea** 42:16 Mhm. Mm-hmm. Yeah.

**Edwin Aquino** 42:28 That we can customize dependent on the property.

**Daniela Tea** 42:28 Mm-hmm. Yes, yeah. So like you're like you're saying something that's shared.
You said something that's shared, but something that may change but not
for all. Is that correct? So like Atlanta might have this. However, the
fact of the matter is what can happen is you would replace this card
with the experience for.

**Edwin Aquino** 42:41 Correct.

**Daniela Tea** 42:50 You would reference the specific experience fragment variation that
contains this. And then if you're saying like, say, at least decides
they need to change that to something else, and at that point they
could, they could replace experience fragment with this instead of this
one pointing to something else. However, anything that's still
referencing Captain Messi would. Still have that and anything that gets changed in the text here would
also get rolled out to all the sites that still reference this. So yes,
this is definitely a good candidate for an experience fragment,
absolutely. Yeah. OK. All right. So let's take a look now at our. Let's take a look now at the remaining agenda. So we talked about
experience fragments when you want to use them, why you'd want to use
them. I didn't have that here, but the content fragment model we talked
about, you know, like an example of one that I created. And essentially how that could be used for say a custom component that
displays content fragment information. Or if you need to just display a
portion of text or something, how that would work with the
out-of-the-box content fragment component. Let's take a look at some of these other components that we have here,
starting with our content fragment card list. I'm going to navigate to my test page. And I believe we are using the content fragment card list. I don't know
if we're using non careers, but we can perhaps make up our own. OK, all right, so here is an example of a content fragment card list
component. Right now, since this is a custom component, right now we are
able to display news and events I believe we had mentioned. I think when we were going over promotions that one of the one of the
things that would be beneficial would be to have promotions to be added
here of course and also something to consider as you start to identify
additional candidates for content fragment models this particular
component. Component would likely have to be updated to take that into account. So
with the Contra Fab and Carlos component though right now it's just
news and events and this is saying OK, I can use a news model or an
event model. For my cards layout style, I can display it in 1-2 or three columns just
like we have for the card carousel. If you're doing events, you would
put your event page based path. This is something that I know you guys
are are aware of how it's just that one event page and then it passes
in the ID of the event. So this is just that field that says well where's your event page so I
know what to pass in and display when someone clicks on on learn more
which is the CTA in this case. So I have my learn more text here as a
placeholder, no results message I'm able to put. You know there are no news, there's no events, so something custom. So
it's this field is open to whatever you have decided to choose for the
type number of cards to show at a time. I know we have here. The column layout and so of course depending on what you choose here, 18
cards would make sense for say like a three card layout or a two card
layout, but you know perhaps something like like like. I'm just trying to think of like 99 would only probably make sense for
a three column versus 2. So just some flexibility in terms of cards that
you want to display in the list and then selecting the list type. We
have our fixed list, our root path and our tags. I believe typically what we've been using across the site is root path.
So when I select that, that just tells me where within the dam I can
pull in those content fragments. So as we remember from our structure in
the dam, currently things are set up for content fragments based off
of. Of the content fragment model and then the line of business and then the
location. I understand though that there could be instances where you
might want to show multiple locations. So if there was a certain certain
things that you knew you want to show, fixed list might be your best. Option you can select the individual content fragment you want to show
here, and so while that may be a little, you know there's like 200 or
so, this of course is not going to be something that you would want to
do. However, if there's a limited number that's crossing multiple
folders, this is certainly a viable option. And then finally, tags. With tags, of course, you're able to select
which tags you have applied to those content fragments. So that's
certainly another way to be able to show things across multiple folders,
as long as you select the root path to be something that's a little
higher than. Obviously the obviously higher than on the specific like location. Like
right now if I wanted to show Barcelona I could show it at this level.
But say I want to show Barcelona and say there was another thing that I
want to show that was within Spain. Then I would of course select a higher level. So as long as things are
tagged, choosing the tag list type should be able to pull as in.
Gonzalo, I see your hand up.

Gonzalo Calasich (SHRSS)** 48:33 So on um, I think on the first option that you have on the selected list
type you have the CTA.

**Daniela Tea** 48:38 This sorry on the select the list type we have fixed list, root path and
tags.

Gonzalo Calasich (SHRSS)** 48:44 I think was the first one.

**Daniela Tea** 48:47 this one here.

Gonzalo Calasich (SHRSS)** 48:48 No, there was one that you were you were talking about the root path.

**Daniela Tea** 48:55 Let's see root path.

Gonzalo Calasich (SHRSS)** 48:56 That one, that one is this can can the root path needs to be an internal
page in Adobe or it can be external?

**Daniela Tea** 49:05 So this keep in mind that this list is saying I'm building things based
off of content fragments, right? So the root path is since our content
fragments are stored in AEM, it would be you know a folder that's
within here with content fragments, right? So what I'm saying here is I'm building, pretend I'm building this
news content fragment card list. Now where are all those news located
within the dam? So I would select, yeah, so it's not so much like
something you it wouldn't make sense for this to be an external link in
this case because I'm just basically saying I want.

Gonzalo Calasich (SHRSS)** 49:32 Gotcha. OK.

**Daniela Tea** 49:42 To choose, say, all corporate news, or I want to choose all news across
all sites by choosing this folder. So what's the root path of content
fragments that you want to display? That's what that means. Yep, all right. News default image. This is essentially you know what
would display if you didn't have an image for your news. And then here
we have some check boxes and so these are gonna be kind of.

Gonzalo Calasich (SHRSS)** 49:53 Thank you.

**Daniela Tea** 50:09 Conditional. So for example, you can see here location is applicable for
events. So if you were to check this and you have me selected,
nothing's actually going to display. However, if you were to switch
just to events and reset up this component, that's when location would
appear. Categories again only applicable for news doesn't matter for
events, at least in this. Instance and then if you need a secondary CTA button to appear, that's
when this is checked and then we would check to see if there's any
information stored in the content fragment. So I know it's a lot, so we
can take a look at an example of a content fragment card list that has
already been set up with content fragments and such. So what I'm going to do is I'm just going to navigate to the live
usage. So if you're ever looking for examples of components and like
where they're being used across the site so you can see like how did
somebody else set this up? The way that I I do this and the way that you can find where this be
used is by clicking on the top left Adobe Experience Manager, clicking
on our little hammer and then clicking on components. So in this case I
want the content fragment card list. So I see that that is here. Click on that and I'm clicking on live
usage and this is not going to list every single page that it's being
used in because that would likely slow down this site. However, this is
going to give you a very good. Representation of pages that are using this. So let's take a look at
this cafe page. I'm just choosing one at random. Once I click on that,
it's going to navigate me to where this is and then I would select here
on the content tree to see exactly where is that content fragment card
list being referenced. So I can look at it and I see it right here. So in this case, with my
event calendar section, there's no events found. However, if I wanted
to find, say, another example of one that's using this, I could go back
to exactly where I was and just take a look, but we can see for Foxwoods
Cafe. In this example, the way that they have set up, we have our event page
based path. We have our CTA labeled more details which would be
displayed if there are events. We have set the route path of where those
events are all located and in this case all we have is a secondary CTA
to be displayed when there are events. I want to find an example where there's actually events. I'm curious
if anyone has any suggestions of a cafe and stage that would likely have
any events. Let's try Valley. That's the an Asian one. Let's try this. Just take a look. Uh, perfect. OK, so here's an example where everything has been set up.
So let's take a look. Here's our CTA label of more details. So you can
see this is what's populating this button here. So we have our news
default image. In this case, it looks like. Each of these specific content fragments had an image that was stored
within it. That's why this is not displaying. Actually, no, this is a
news default image. My bad. So this this has no effect on this here. But
then also you'll notice I do have my secondary CTA. Let's take a look
at. While it's all being displayed, if there's no secondary CTA info
stored with for this particular event, then that button's not going to
display, but we can look at that within the content fragment section. That's Cafe Valley and and let's check out February 19th. OK, I think this one is it. Alright, OK, so here's our event image and you can see a secondary CTA
link is indeed blank. That's why there is no button that actually
appeared here. Um, let's see. And so yeah, the image there's an image event placeholder image that's
being stored here and that's what's displaying. And if I were to click
on the more details, this operates just the same on my bent details page
which I had inputted or which was inputted in the configuration window
had been set and then it just passes in the ID. And so the information all displays here just as expected. OK, so this
is the content fragment list. The other places there you can see this in
action today I believe would be on the Hard Rock website when it comes
to news. That's also again another available model. Moving forward though, it
seems like as as the team is coming up with additional content fragment
models, it would make sense to enhance this component to be able to
reference those models and then display it as a list. Moving forward, I'm going to pause here to see if there's questions
about this content fragment cart list component.

**Edwin Aquino** 55:48 With this component, I've I've seen it before where if we only have
two cards, it's not really centered, it's it'll show the two cards to
the left. Is there any way to center those cards or have it like fit
configured to where if it's just two cards, it'll show centered or one
card?

**Daniela Tea** 55:53 Mhm. Currents. Right. I think that's something, right. I think that's something that we also
were talking about when it came to the careers website and I think that
was noted in Jira and that was identified as a gap. Definitely
understand that you know as there if there's. One or two having that centered. So we understand what the ask is
currently today that's not available, but that was something that was
captured in JIRA and we would bring up again during our gap analysis.

**Edwin Aquino** 56:29 Perfect. Thank you.

**Daniela Tea** 56:30 Yeah. Any other questions about the CF card list component? Alright. OK. Yeah.

**Edwin Aquino** 56:45 Actually, one more, one more. What if there is no CTA for the event? Is
there any kind of additional functionality that any settings that we
have to check off or change if there's no CPA for just a specific
event? Yeah.

**Daniela Tea** 56:55 If there's no CTA for the event, oh, I see. So to be clear though, the
CTA that's here for these events is specifically to take you to that
event details page. Are you saying that there might be an instance where
this page doesn't exist?

**Edwin Aquino** 57:12 Correct. So a lot of times we would host events where there's not any
additional information to share with the guest. It'll just be the the
act, the time, the date, that's it. So there's no reason for the Learn
More page. So we generally keep that CTA away because there's no reason
to have a guest click on something that's not going to show them.

**Daniela Tea** 57:22 Hmm. OK. I see. Let's see how trying to see where the model is and if we
actually have that as a required field. So I think, I think the way that
the component has actually been set up is that the expectation was that
all.

**Edwin Aquino** 57:32 Anymore.

**Daniela Tea** 57:52 Events would have additional details. I understand what you're saying
that not all events would have, but that's when we were creating it
that like whether it's the ability to say like share it or post, you
know, like this has the social media portion, right? Or if there was
some information that would be captured within this detail section,
that's why the. Default is that all of them would have an event details page. So I think
what you're saying though sounds like that would also be a gap where
the desire would be to not have this displayed at all. So right now that
functionality is not available, but that can certainly be identified as
one of the gaps.

**Edwin Aquino** 58:33 Thank you.

**Daniela Tea** 58:34 Yeah, OK, all right. OK, so that is the content fragment card list
component. I'm going to now go on over to the header and footer
specific components since those are related to shared content. So we are actually within a footer right now for San Diego. I see this
is an open tab, so let's take a look at this one. Um. OK. And actually, yeah, that's right. I remember, I remember we talked
about this when we were talking about, you know, experience fragments
and experience fragments. Gonzalo, I believe you and the team had wanted
when when you guys were putting in like the forms and such, correct me
if I'm wrong, but you guys had updated. Experience fragments in order for for this form to appear. Is that
correct? Yeah.

Gonzalo Calasich (SHRSS)** 59:27 Correct, correct. The goal was that we needed to have this form on every
page and that is why I think the experience fragment was the right
choice. And because what's on the bottom of the of the page would say
like why don't we reuse the footer to make it happen and it it came out
really nice.

**Daniela Tea** 59:33 Mhm. Yes. Uh huh. Yeah, so yeah, this is a absolute perfect example of experience
fragments within experience fragments. So now if if Gonzalo, if you and
the team, if you guys ever need to like change anything within here
instead of changing it within the footer experience fragment, it would
just be within this location. So glad to see. That we see in a live example in action. That's wonderful. All right.
So moving on to some of the different portions of our footer. Again, I
know we talked a little bit about this, but wanted to make sure that we
covered some of the footer specific items, for example. When actually creating a footer itself, there is a specific footer
template that needs to be used. So I'm I'm here at this root level.
I'm not actually going to create it, but if I were to create experience
fragment, typically when it comes to headers and any of those examples
that we talked about like this. This one here when I was making up that fake benefit card, you would use
the SHRSS blank variation. The reason why is because this is going to
this is the specific experience fragment template that we created which
has all the components that you guys are accustomed to seeing. However,
when it comes to footers and. Only you want to use the footer variation. The reason for that is
because the footer variation experience fragment template actually wraps
the content with the footer markup, so that's going to be visible
within the actual like markup code, so there's no real difference. Or change in what you would see when you're interacting with the
experience fragment, but it is specifically so that way there's that
footer markup available to you. Additionally, when it comes to the
footer, there was, I believe when we were discussing how the footer
should be set up, there was. An original requirement to essentially restrict some components from the
footer. So that's why when you add something within a footer experience
fragment using that template, you're not going to see the full list of
items because that was requested to restrict what was shown. So in this case here you'll notice there's there's, you know,
certainly less than the components that are available. However, if you
are creating a regular experience fragment. This here and I'll make sure I delete it. So this is my regular
experience fragment using that SHRSS variation. This is where you'll
see the full list of things because essentially this is this could be
placed anywhere on the page and not not just like a footer. So I want to make sure the team understood why this you see a smaller
list when you create footers and also what you would need to do if you
wanted to create something that had additional components in it. It
would just be a regular experience fragment. OK, so let's take a look then at some of these footer specific
components. I believe the only one here that would be footer specific is
the footer image list. This is something that is. Believe visible on our hotels, but not all of them. So can someone give
me an example of a hotel that has like the footer images at the bottom?
Does anyone have an example at the top of their head? It's like the, I guess, like the awards and such for a hotel.

Lyon, Rick (Director of Digital Experience)** 1:03:24 You can try Cancun. Can. Yeah, New York, Cancun or Madrid. Try one.

**Edwin Aquino** 1:03:25 New York. New York has one, I believe. New York has two.

**Daniela Tea** 1:03:28 New York. Let's take a look at. Yeah, cool. Let's let's take a look
at New York then, of course.

**Edwin Aquino** 1:03:35 And how? OK.

**Daniela Tea** 1:03:39 OK, well actually yes. So this is here we go. Here is an example. In
this case this only has looks like it only has two. We can take a look
at the others, but for this specific one we can see here this is. All right. Um. And actually yes. So you can see here are required fields, images, alt
text. However link is not and my understanding for that is because
sometimes they don't actually link to like a an external URL and it's
just simply to display the image. However with the image list as you can
see multi field can add as many as you want. We'll take a look at. Another hotel where we can see how that's in practice, depending on how
many images you do add. I believe the display of images. I think I
can't remember if it's restricted to three. Or if it's two, I can't remember exactly. Let's take a look at
another one. Then you guys said Cancun, Madrid, maybe, which would have
a ton of awards.

**Carlos Aldana** 1:04:43 I think that the brand page highrock.com and the hotel it it has a
bunch.

**Daniela Tea** 1:04:48 Uh. Which one? Sorry.

**Carlos Aldana** 1:04:50 The main page for the hotel.

**Daniela Tea** 1:04:51 Oh, OK, let's take a look at the main page then. Not header, footer.

**Carlos Aldana** 1:04:55 Yeah.

**Daniela Tea** 1:04:59 OK, let's take a look at this. All right, perfect. Yeah, great candidate. All right. OK, so for this
one here, we can see that I'm going to view this as published. So I
guess is there only five? Let's take a look. Let's find out. And this is in stage, guys. This is not, this is like not in. So if you
guys were really expecting this to look different, this is all like
stage content. So I have 12345, all right, Yep. So I don't think we had
put a limit within for this particular component. So of course as Hard
Rock continues to win more wars. And such. This could certainly grow with just like with all of our other
multi fields, the ability to change the location or the I'm sorry, the
position of where that image is. And we'll notice here this image Max
height. So this here is as you're having some images I guess. It depends on if you guys are pre-formatting your images or resize them
in advance and then uploading them to the DAM. But in this case here we
were trying to put some sort of height restrictions I believe to the the
carousel itself. So that's what that field is. We do have the image
position tab just like we have everywhere else. As we've talked about, you can see in this instance it's not being
used, but this particular component, I don't know if we're actually
using it outside of the footer, but this is one of those specific
components that we have allowed for use within the footer itself. So that's where you have it here, the footer image list. OK, let me see
what else is here. So we footer, footer image list, social media.
That's also something that is captured here within the footer, although
this can certainly be used in other locations. In this case, I think we are aware of of how you know this component
works since we had seen it before. The main thing though I think that
can differ and and what you'd see be different across properties is the
two column view or the inline view. Inline of course. This means it's just one line, and that would probably be something you
would want to consider if there's like, say, an odd number of social
media icons here. And so as you're reviewing the footer experience
fragments for some properties, you might see a different style variation
being selected. OK.

**Edwin Aquino** 1:07:33 And Daniella, for these, for those award images, 'cause I know we
currently have them set up a specific way, is there any specific specs
that you may recommend or anything that we can use for these images?

**Daniela Tea** 1:07:33 So those, yeah. Mhm. Mhm. Let me see if that's so that's as we're reviewing the component spec
list. Let's see if that's on there. I know we had put a logo on here.
Let me talk to the team about. Oh, here we go. Image list, awards,
carousel, Flutter, 96 pixels. So I it looks like we have provided that,
but again, we're reviewing. This page to confirm the information on here so you can see that's
already here, but we'll confirm that for you.

**Edwin Aquino** 1:08:12 Perfect.

**Daniela Tea** 1:08:13 Yep. All right. OK, going back to our confluence page. Any questions
though about the footer in in general that a lot of these components
with the exception of the ones I called out, you're you're using it
already across multiple pages on the site. Um, but anything you know about footer in general that that you guys
have any questions on?

**Edwin Aquino** 1:08:40 Nope.

**Daniela Tea** 1:08:41 All right. OK, let's move on to the top where the header is our other
main experience fragment that's been established. OK, I'm gonna go to actually, let's go to since we are reviewing
careers. Let's take a look at careers and see how what's being set up
there, OK? OK, so here is our careers header and we know that there are different
parts to the header. We have the header in general, which is this whole
entire component. So this is this encompasses the entire component which
is made-up of our crowd navigation. Our crown CTA and also the main navigation. So clicking on the crown
navigation as we can see here, in the case of the career site, we know
there's only one label and that's why this has been, excuse me,
that's why there's only one thing here. However, for say like the. Corporate page. I believe there's multiple labels that are being
displayed, so this that's why this particular component is using a
multi field. So if you need to ever change this and say link it to
something else, this is where you would go crowd navigation. Crown CTA, which is this ortion here on the right. We have our different labels, returning applicant login, team member
login and then the search for jobs button. And you'll notice here the
different experience selectors CTA with the color of this. You also see
CTA with color of this. And then this here is a CTA, but no color has been selected because by
default CTAS will display with this background. So what I'm trying to
highlight here is that the experience selector is all the same a CTA.
However, if you need to change the appearance, you do have some
flexibility with that by using this color selector field. OK, each of these within the Crown CTA we have the different link types,
so you have a link. So of course a link would link to whatever is
located here, but you also have modals, modal small, so depending on
what size you want the modal to be. These would be selected and then what would be put within the URL field
would be the specific experience fragment that you say would want to
display in the modal. So in this case here. And careers, we don't have that. I will look for an example where we do
have that since I don't want to mess this up, but just showing that
links are typically I believe what you guys are using across most of
your sites. However, when it comes to like hotels, I think that would be
the book your experience model. So we can take a look at like a hotel
navigation to see how. Modals being used with our experience selector. CTAs, as we all see, are
basically going to be buttons or links that take you to a location, but
you also have the sign in functionality. The sign in is actually what
calls the modal for Unity. As we know on the hardrock.com website, this particular button displays
this iframe of Unity within here that was set up by actually clicking on
the sign in. Experience selector. You also have your drop down which can be displayed
as a CTA, a map marker or a language selector. So these are the
different icons that would display and then you would be able to add
list items underneath that. Cycle. The map marker and then I can create a list that would appear after I
clicked on that map marker, I click on the language selector icon and
then I would put the different languages that I want along with the
URLs, etc etc. So these are being used across I believe some of the
other sites, not this particular one, but just wanted to make sure the
team was aware. Like when these would be used and how to access that. Then we also have
help which displays a help button and then the help button would link to
whatever is here and then finally an author unique ID. Which in this case we don't have that, but this would be a way to be
able to assign an ID that would then be added to the markup for this. OK, so let's take a look at. Actually, I want to. I want to show one
that has a modal. I want to show one that has a modal. So let's go to
hotel. I would assume this one has one. OK, this has a lot. All right, it's perfect. Alright, so as we saw exactly what I mentioned Unity. In order to
display the Unity modal, I'm sorry, iframe sign in is selected. Learn
more about our best rate guarantee. We've used the image. Oh yeah,
there's an image field here which you can see is clearly being used.
This best rate guarantee image. We're saying it's a CTA so that way when you click on it, it takes you
to this page. Our book now button also a CTA. It has the modal. You'll
see the modal is pointing to the book now experience fragment. Unity loyalty program. This looks like it's just a link to the Unity
website, so that's why CTA was selected. And yeah, so this essentially
is this is showing the majority of the items, you know, like a
combination of the different items that we just reviewed. And we can actually take a look also at this ground navigation. Just to show, I think there was a small change that we have made where
the pipe no longer shows that there's only one items that's now being
reflected in the careers websites. There's only one link, but of course
if there's additional items to the right of that, the pipe will appear
and then anything underneath the first item. We'll just display to the right of the pipe, right? Hey. All right, and finally for the header, main navigation is a big one.
This is essentially where you would put your everything that's in this
section, including the drop down menus that will appear under each
individual links. Of course on this logo tab, this is where you set your logo and also
what link you would point to. We know that location address and reverb
is reverb. This is something that we would see for the reverb headers,
so it's just using the same component but with with this checkbox
essentially in place. So it's styled that specific way. For the main navigation, this is where we are putting all of our links
here along with secondary navigation, also tertiary navigation. I'm
trying to remember which sites use that, but essentially as I hover over
destinations. This is where I'll see anything that's here in this portion, and if I
need to go a little bit deeper, I can. However, I believe in most cases
I think we're only using secondary navigation for most navigations. So
yes, a lot of multi fields in place in here since. There's a lot of links that need to go in the navigation, but
essentially you know this is I think where you would likely have to
spend the most time to update links when you're adding new pages or
removing pages, and also if you need to prioritize ordering. Of these different pages, finally the mobile slash tab. What this is
showing here is I believe when you're actually just in like a smaller
break point, there's going to be a. Let's actually take a look. So if I were to expand this. You can see that text. So if you want to put say like back or back to
main NAV or whatever, that's where that text is appearing for that
specific field. Alright, OK. Any questions about the header in general? Because I know
that you know this is the headers already header and footer are both
already being used on say the reverb site, the corporate site. Not sure
if the team has had to update anything as of yet, but just wondering if
there's. Any questions about the authoring portion of that? It. OK. OK, so let's see here. OK, so tabs.

**Lucas Nelson** 1:17:52 Did you did you cover everything, Daniella?

**Daniela Tea** 1:17:54 I think I did. I didn't put. So we talked about content fragment
models. That's not something that was listed here. It was more like
general, but we did go over content fragment card list as well. Frage
fragment, yeah. So these are all the items that are essentially within.

**Lucas Nelson** 1:17:58 OK.

**Daniela Tea** 1:18:14 Your header or footer. So I yeah, so I covered what I wanted to. So
turning it over to the team, anything in particular that you guys had
questions about. Carlos, I see your hand. Go ahead please.

**Carlos Aldana** 1:18:29 Yeah, Daniela, I have a question related to the content fragment events.
Is it possible to copy one event, one content fragment in order to
create a a new event?

**Daniela Tea** 1:18:35 Sure. Is it possible to create? Sorry, let me I'm gonna. I'm gonna just
navigate to our. OK, you're asking if I'm just gonna oops, didn't mean to click on
that. I'm just gonna change the view here back to column view. You're
asking if you can copy an event content fragment, is that correct?

**Carlos Aldana** 1:19:04 Yes, because what I understand is that we are going to create the
events, let's say for our content calendar events. And then if if I
have a similar or the same artist presenting the same show but in a
different date, can I copy and paste that?

**Daniela Tea** 1:19:08 So. Mhm.

**Carlos Aldana** 1:19:24 Enter.

**Daniela Tea** 1:19:24 Yeah, so you should be able to copy and paste and you'll notice that
now there's two versions. If you look at the name, wait, but one
second. OK, sorry, I zoomed in. If you look at the name, you'll see
that the name says day one, right? Whereas the original version does not
have.

**Carlos Aldana** 1:19:36 Ha. Yeah.

**Daniela Tea** 1:19:44 So this is indicating that this is a copy and then if I were to open
this up, so I'm going to click on this and I'm going to click on edit.
It's going to have the exact same information and then obviously you
know like say this is a new date then you would want to change whatever
you know you want to change.

**Carlos Aldana** 1:19:59 Mm-hmm.

**Daniela Tea** 1:20:02 And I would recommend though, you know, like for ease of use, you can
also don't forget you can also rename your content fragments, right? So
hang on, sorry, this isn't the way. Yeah, so you can rename your
content fragments by selecting it, clicking on move and then.

**Carlos Aldana** 1:20:10 Yeah.

**Daniela Tea** 1:20:21 Changing the title to whatever you need. You can also actually change,
you know, like we saw the one because that's a copy. You can also
change that too. You just need to make sure that this is, you know, not
the same as like a different content fragment, right? Or else that's
that's not going to, it's not going to work. But yes, you can
certainly copy things as like a starting point.

**Carlos Aldana** 1:20:35 Yeah.

**Daniela Tea** 1:20:41 or whatever and then changing the relevant information and also even
changing the title after you copy it.

**Carlos Aldana** 1:20:47 OK, awesome. Thanks.

**Daniela Tea** 1:20:48 Mm-hmm. Any other questions?

**Edwin Aquino** 1:20:53 I got a few questions here Daniela for the for the main navigation is is
there any? Can you explain like what the is reverb does exactly again?

**Daniela Tea** 1:20:56 Sure. Yes. Yeah, absolutely. Let's navigate to our experience fragments and I'm
actually going to open up reverb one. I think Atlanta might be a good
should have it. Alright, so. This has OK, so first to this field location address you can see how
that translates to reverb right? And with is reverb the navigation for
reverb is slightly different right? So like our navigation and keep in
mind this is the experience fragment so if. We actually view the site. I'm gonna pull the site over as well from
stage. So you can see how it actually looks. No, not that. I'm at Atlanta, I think. Yeah, I'm at Atlanta. OK. OK. All right, OK, so just to be clear, you may be like, wait, why is it
styled this way? This doesn't look the same. So the experience like the
theme has not been applied to the experience fragment because if you
guys recall, you set the theme at the level in sites. So that's why some things might look a little bit different, but as you
can see, like the font is pulling in what's correct for the reverb
theme, etcetera, etcetera. So don't be alarmed when it doesn't look
the same, it's because the theme is applied at the site page level. All right, so the is reverb, essentially what it's saying like the
navigation for reverb is obviously different from the navigations from
like the Hard Rock website, et cetera, right? So like this is just
saying when I have is reverb checked everything that I'm putting. You know, like in the main navigation and such is going to be structured
this way and like you know, like appear like as in the hamburger versus
like across the website, etcetera, etcetera, right. So that's why is
reverb was specifically made because while the reverb navigation, you
know it's it's a navigation just like every other site, there are some
different. Differences between reverb and like corporate or reverb and hotels,
etcetera. None of those need it because their navigation is pretty
pretty much the same and how the component you know like is technically
built, but reverb just had to be an exception. That's the only reason
why this checkbox is here specifically for the reverb sites. So you're not going to use this outside of anything that's not reverb.

**Edwin Aquino** 1:23:36 OK, cool. And then you just mentioned something about how the child, the
child pages inherit the the main theme for the site. Is there any way
you can change it to where we can have the child page have a different
hero, I mean, excuse me, main navigation or footer?

**Daniela Tea** 1:23:44 Yes, yes. Let me confirm what. Yeah, let's confirm what you're saying. So let's
take an example of like, say, actually the Hard Rock website, right? OK,
let's see. Is it set at this level? One second. OK, so at the Hard
Rock.

**Edwin Aquino** 1:23:54 Or is that just basically manage? Yeah, how how would you manage the? Mhm.

**Daniela Tea** 1:24:10 Level. I'm sorry, the Hard Rock EN meaning the language, the English
language website, the home for that. I have my theme set Hard Rock and
then also have my header experience fragment and my footer experience
fragment. So what this means right now is that anything underneath here,
all of these are going to have that same experience fragment you're
asking for like. Say our history to have something different. Is that correct? Like a
page like this?

**Edwin Aquino** 1:24:34 Oh yeah, or just the just for the header or footers to be different on a
child page versus the actual prior page itself. So let's say you'll
have a subpage cafe that'll have a different header or just an as an
example.

**Daniela Tea** 1:24:44 Hmm. So. So right now, so based off the structure of this, because this child
page is underneath this home page where the theme and the navigations
are set, it is going to inherit. This is using the open page template,
yeah. What it sounds like you're asking is instead of it inheriting, what
might make sense for like the future is to have a slightly different
template which doesn't necessarily inherit the information that was put
in the properties of this page. And so that template could be built to say, you know, have an experience
fragment built directly into that page templates. That way the user
would then select which header and footer to use. So right now, because
you're using, we're using page templates for all of our child pages,
you don't have to. What I'm saying is. The thing is you could theoretically create a new page template to
essentially have the requirements that you just described to me. We just
don't have that right now.

**Edwin Aquino** 1:25:53 OK, OK.

**Daniela Tea** 1:25:53 Yeah. So it sounds like what you're describing would be a could be a
new template in order to be able to to kind of break that inheritance,
but still live amongst the same level as the other topic. Does that
sound right?

**Edwin Aquino** 1:26:05 Yeah, that sounds about right.

**Daniela Tea** 1:26:06 OK. OK. Yeah, that's what my recommendation would be for that then. And
I think we are going to be going over page templates. So maybe what I
can show kind of similarly to what I was doing for that bio biography
contact factor model I was just demonstrating earlier. I can perhaps demonstrate like you know like a template and like some of
the decisions you would be making when creating a template and how that
could potentially be built out.

**Edwin Aquino** 1:26:38 OK.

**Daniela Tea** 1:26:38 Right. OK. Um. All right, so let's take a look now at. So we've covered this, so some other items we're talking about future
sessions I did have on the radar since I wanted to make sure we covered
as many of the content fragment model related components possible. I did
have on the radar news. I believe the team is probably already used to news, but can certainly
cover you know different the different components again as well as the
the specific templates. I also had locations which I think we were going
to try to cover sometime next week. This is for the location content fragment, menu content fragments. Since
those are currently existing in the system, we're going to go over how
these specific content fragment models relate to some of these
components and then also some components you guys are familiar with with
the hotel websites. Like booking widget offers destination search and filters. And then also
I think we've seen the Google map, the location list used on certain
other parts of the the corporate site as well as potentially using the
Google map on the careers website. So this is something these are the some of the topics that we'll be
covering in some future sessions tomorrow and I think hopefully early
next week. And then I think after that we'll move on to things such as
like page templates and then also take a look at the other components
that are not necessarily content fragment model related. But certainly want to make sure that they are covered. So yeah, this is
what I had for today. I do see the time. I think Luke, anything else
that you want to add?

**Lucas Nelson** 1:28:35 No, I don't think so. Thanks for flashing those future topics,
Daniella. I think that was helpful as well. I don't have anything else
to add. Andy Lambert, I don't know if you're active. Is there any, you
know, updates technically that you have?

**Andy Lambert** 1:28:51 No, I think I'm good.

**Lucas Nelson** 1:28:54 OK. Yeah, Danielle and I think we're good from our side.

**Daniela Tea** 1:28:56 OK, sounds good. Then I'm gonna flash the KT calendar again though,
just so the team is aware the location of it and what we have planned.
So typically we don't necessarily want sessions on Friday, but we are
making exceptions since we weren't able to have it last week. But you'll notice here we are scheduled to begin our technical
knowledge transfer sessions, not next week, but the week after. So
we'll be getting more into and this will be particularly relevant to
you, Gonzalo, if you're still on us, we'll be getting into more of
those technical topics starting the week after next.

**Lucas Nelson** 1:29:34 Yeah, and that's a good, that's a good call out, Daniella, Scott,
because those are morning times and the morning can be tough for both of
us. I'll work with you asynchronous. Maybe we can get the placeholders
on for technical enablement in the adoption sessions so we can get them
on the calendar sooner.

**Daniela Tea** 1:29:34 Right.

**Scott Sorel** 1:29:53 I would say send it out sooner instead of later, Luke. Exactly. Yeah,
yeah.

**Lucas Nelson** 1:29:54 Rather than later. Yeah. So I'll ping you what my thoughts are for those morning calls and
then we'll go from there. Yeah.

**Scott Sorel** 1:30:02 Yeah, yeah. I think people will make room for to be there. If Gonzalo is
here, I mean, you can ask him where we finish early. You know, he's
here. Yeah. So like the early ones, Gonzalo, the week of March 9th,
would that be a problem?

**Lucas Nelson** 1:30:03 OK, sounds good.

Gonzalo Calasich (SHRSS)** 1:30:11 I'm here.

**Scott Sorel** 1:30:18 If we did like 9 to 11.

Gonzalo Calasich (SHRSS)** 1:30:21 No, that's fine.

**Lucas Nelson** 1:30:23 OK, yeah.

**Scott Sorel** 1:30:24 OK, there we go. Team player. Told ya.

Gonzalo Calasich (SHRSS)** 1:30:26 Yeah.

**Lucas Nelson** 1:30:26 Yeah. So Andy and Vinay will be like co-leading those. That's the
reason we're doing them in the morning. So Vinay can participate. OK,
yeah, sounds good. So I'll work to get those on the calendar, Gonzalo,
and you guys can see those and you'll know it's kind of a blitz week,
the March 9th week. OK. So thank you for that.

**Scott Sorel** 1:30:46 Yeah.

Gonzalo Calasich (SHRSS)** 1:30:47 Thank you.

**Lucas Nelson** 1:30:48 Yep. Alright, cool. Yeah. Danielle, thanks for doing that. Yep, I I have
the next action for that stuff. Thanks.

**Daniela Tea** 1:30:50 Alright. Thank you very much. OK.

**Scott Sorel** 1:30:53 Cool. Beautiful.

**Edwin Aquino** 1:30:54 And Danielle, for for next week's session, for next next session we
have, would you be able to provide us some examples of possibly a footer
with a search query and a footer that uses the tag as a component as the
options?

**Lucas Nelson** 1:30:54 Alright, thanks.

**Daniela Tea** 1:30:55 Yes. Sure. We're talking about for the footer like what? Like, oh, are you talking
about like for the list of links?

**Edwin Aquino** 1:31:09 'Cause I I think. Like in the list component settings when we have, yeah. Is there any way
we can maybe explore that? I'm not too sure if you have one off hand
already.

**Daniela Tea** 1:31:20 Sure, yeah. So let me confirm. We say footer with list that shows tag
query and then also what was the other one?

**Edwin Aquino** 1:31:29 One was the search query and one was for tag.

**Daniela Tea** 1:31:32 Search query and text. Got it. Awesome. Yeah, no, I'll take note of
that and try to either find examples or create some new ones, certainly.

**Edwin Aquino** 1:31:40 All right, thank you.

**Daniela Tea** 1:31:41 Alright, awesome. Thank you guys very much. Hope you guys have a good
rest of your day then. Thank you everyone. Goodbye.

**Lucas Nelson** 1:31:46 Thank you, Daniella.

**Edwin Aquino** 1:31:46 Thanks. Thank you.

**Lucas Nelson** 1:31:49 Thanks.

Scott Sorel** stopped transcription



## Session: News — 2026-02-20

**SHRSS Adobe Knowledge Transfer-20260220_130127-Meeting Recording**

February 20, 2026, 6:01PM

1h 19m 41s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:08 All right, Daniella, I think we're we're off and running on the
recording. If you want to start by just sharing the agenda for today's
call, we can get started.

**Daniela Tea** 0:15 Yeah, sure thing. OK. All right. Good afternoon, everybody. Let's see
here. OK. So for today, since we are continuing to cover anything that
has a content fragment, I was moving on to the news content fragments. Related components. What I'm hoping to do today is actually show you
guys how you would go about creating a brand new news homepage. So this
is going to be relevant for say like for example if you guys had career
specific news that you wanted, you want to add a careers news page
specifically to the career site. We've seen how that works in the corporate website, but how do we start
that from scratch? So going to walk you guys through that and I also
want to spend a little bit of time at the very beginning though to
address some of the questions that came up yesterday. Starting with I think Edwin, you had asked a couple of questions,
especially at the very end with regards to showing a list that pulled in
tags and also a list that pulled in based off of the search in query. So
I wanted to go over that really quickly first. OK, so if I'm not mistaken, you had asked specifically for the footer,
but I did want to confirm we are talking about the list component. In
this case here the list component is in the footer, but of course the
list component can be used outside of the footer and so just wanted to
confirm that is like that's what you were.

**Edwin Aquino** 1:49 Correct.

**Daniela Tea** 1:49 You're asking about the list component in general, is that right?

**Edwin Aquino** 1:51 Yeah, that's correct.

**Daniela Tea** 1:53 OK, sure. OK, so this is my little fake footer that I have in my
training folder. So I made a copy of the an existing footer. What I'm
doing here is in my list component I have shown an option for tags. So I created two training tags, one called events and one called
calendars and you can see here that I have selected the parent page of
this location and I'm saying OK anything that has this these two tags
applied to it underneath this location I want you to just. Display it within my list. So I've selected match all tags and so right
now you'll see I have one page that's showing up and we can take a
look at that page and see what's actually applied to it and why it's
coming up. If I were to change this to any tag, now it's saying OK
underneath this section here, find anything that either has this. Events tag that I added or this calendar tag. So I'm going to click
done and so now you can see I have 3 pages so they either have one or
the other tag. So let's take a look at where I created the tags as a
refresher for the team. I'm going to click on Adobe Experience Manager and then the little
hammer and then tagging. I created a new namespace for training just so
that way it's not something that you guys would you would because you
guys won't be using these are just for training purposes. So I created
a new namespace for training and then I created these two tags. One called Events and one called Calendar. So now that those are
available here in tags, when I go back to the sites section where all
the pages are located, I'm just going to navigate to my training
pages. Under corporate and then under careers in English. So these of course
are the pages that we've kind of been going over. I'm going to open
up, I think it was calendar test and I'm just going to click on
properties and you'll notice here under tags in the basic tab, I had
added those two tags. One for events and one for calendar. I can, you know, add whatever I
want and I can also add multiple at a time to this page in this case. So
I've just selected these two. So that's why when you. Where's my page? Oh, here it is. When I selected this tag and this tag and I said match both tags,
that's why only this page calendar test is what we're expecting to see
will show up in this list. However, if I have selected any tag. That page will also still of course show up because it has one or the
other tag, but then these additional pages showing up because it has
either the event tag or has the calendar tag that I created applied to
it. So any questions about the tagging, how tagging works with the list
component?

**Edwin Aquino** 4:56 Yeah, so when it comes to tags, we occasionally have some pages or
events or any, you know, content in general sometimes has tags where we
want to exclude them from a list. Is there any any option that we can
maybe exclude certain tags from this list from appearing?

**Daniela Tea** 4:57 Mhm. Hmm, so let's see. So let's take this for example. Pretend that it has
another tag like I don't know, like something silly like do not use
right? But it still has events in calendar. So what you're saying is I
want to show anything with events in calendar but nothing with do not
use. Is that an accurate like?

**Edwin Aquino** 5:31 Correct, correct.

**Daniela Tea** 5:31 Um, useless. OK, OK, um, so hmm. I don't think out-of-the-box it works that way. What this is doing is
is like I just showed it's building it based off the tags. It's not.
It's not excluding, it's more matching. Let's see. I'm trying to
think of a. Can you give an example of um like like like what's a real example like
of A tag that might be something you want to exclude but it would still
have the other tags?

**Edwin Aquino** 6:05 So for an example, we would have a promotion pages set up where one
promotion page is specifically excluded from appearing on the landing
page just because it's something that maybe the property uses off off
site, so they don't want general public to be able to view it. So they won't show it on the website, but it'll still be up here in
the back end. Um, but it'll still be elicited as a promotion. So like,
that's one of the things, yeah.

**Daniela Tea** 6:31 So is it to confirm, is it a pub? Would it be a published page and and
something that would be indexed or is it OK, so it's it's published,
but just not something you necessarily want to feature on the home page,
but it would still have these appropriate text to it. OK, let me take
that use case back.

**Edwin Aquino** 6:39 Correct. Correct.

**Daniela Tea** 6:51 To the team right now, the way that this works as we just showed is
based off of matching the tags. But I I understand though what you're
trying to look for with regards to excluding. So I'll I'll see what we
can, what we can do if that's something that's possible currently with
this. All right, yeah, OK, so let's now go to search. OK, so with search,
what search query is doing is you are putting any text here and it's
actually going to match or look within.

**Edwin Aquino** 7:09 Awesome. Thank you, you know.

**Daniela Tea** 7:25 The title, the description, the page properties, but it's also going to
be looking on things that are actually on the page itself that might
match this query. So in this case here I'm saying OK, search it in this
specific folder, anything that has KT in it. And I hit done and so you'll see OK, it makes sense that these KT ones
are appearing. However, why is KT appearing on calendar, calendar, test
and test page if we were to take a look at these pages and we can do so
right now. The reason why is because somewhere on this page there is something
referencing KT on it because the query is looking for any sort of text
or any anything like a component or something that's referencing the
phrase KT. So that's why and if if you guys want to see actually. I realized it's because this folder path is pointing to my KT folder
path. That's the reason and it's also pointing the KT event this
particular page. That's the reason why this page is actually appearing
here. The search query is specifically looking again for properties and
anything on the actual page itself that is referencing this. Specific term. So if you need something that's again a little bit more
specific, tags is a good way to be able to make sure it's only things
that you have tagged. Of course, we're going to look into that other
use case Edwin you mentioned if you need only say like very, very, very
specific things to show like a list of five. You have that option of course for your fixed list and then for child
pages. This of course is you would select which page at what level. In
this case I'm going to show at my. English level is going to show a list of everything and it's going to
of course list every single page here, and it's not going to list the
child pages because I only said only take the first level. So there are
a couple of options where of course you know you're able to show
whether it's all the child pages in the location. A very, very specific list of pages that you want to show anything that
might match a certain term, but keeping in mind it could pull in things
that you might not intend if that particular text is on on the page
itself, and then tags in order to pull in anything that was tagged at
the page property level.

**Edwin Aquino** 9:51 No, Daniela, with the listing function, is there anything that dictates
how many elements up here before it splits into two columns? Or is this
is it just?

**Daniela Tea** 9:54 Mhm. Um, so let's. So yeah, so we have a number of columns for list items.
In this case we have two. Your question is if you were to have like say
like 6 or something, how would it display? Is that what you're trying
to?

**Edwin Aquino** 10:02 How was? How was that? Yeah. Yeah, how is it? How are you dictating whether you know what items are
appearing in what columns? Is it just a?

**Daniela Tea** 10:21 Oh, I see. OK, so this is actually going to be going. So you'll you'll
see this list calendar, test KT calendar, KT career. So this is in
alphabetical order. I am able to order it by the last modified date. So
it's looking at the title of the page. I have selected order by. Title or I could do by last modified date depending what your use case
is. So based off the column, if I were to do this as three columns, this
might look a little wonky. Yeah, you can see it's still it's still in
alphabetical order based off of the title, right? So 123 and then the
next one would be underneath here in alphabetical order. Does that make sense? Yeah, based off the columns.

**Edwin Aquino** 11:02 OK, got it. And then one final question, since we're on the footer
still, there's one thing regarding the image icon right there that we
saw it. There's an option for logo styling. Could you explain what that
is? If, if, what's the use case scenario for that?

**Daniela Tea** 11:06 Mhm. Oh, let's see. Oh, my bad. The oh for this right here. Yeah, so logo
image. If I'm not mistaken and I will check the ticket for this one. I
believe logo image was supposed to apply a specific.

**Edwin Aquino** 11:17 Uh, not for the social, not for the social media, but for the the logo.
Excuse me. Yeah, it.

**Daniela Tea** 11:35 Is there a specific height or specific padding? Let me see if I can find
that. Um, let's see here. And I think let's take a look though at when I'm pulling that up in,
let's take a look at what we have in corporate. I I can't remember if
that's actually set or not. Mm. Yeah. OK. So it's not set. I I think that this is something that's
actually not necessarily set for the footer. I think it's set on the
pages where you guys are displaying multiple logos. What is it? Maybe
the, is it the Heels Foundation page perhaps? Let me see if I can find that, but I believe that's supposed to make it
like a certain height and width. So that way if you have multiple logos
on a page it it displays in a certain way but showing a logos. I think
it's the heels foundation page. Oh, maybe not. Hmm. Hmm, let's see. I think I need to look into that one. I need to check
the JIRA ticket to see exactly what that does, but that's not
something. Just to be clear, it's not something that's specific to the
footer, it's for the image component in general. I will provide
additional information as to when you would want to use that. That and the reasoning for it, OK.

**Edwin Aquino** 13:17 Thank you, Danielle.

**Daniela Tea** 13:19 Yeah, sure. All right. OK. So this is the list. Let me get out of some
of these live pages. I don't want to touch anything in the corporate.
Go back to my training and let's see. I think you will. There was
another question, Edwin, that you had that I wanted to show really
quickly. Just about the transparent backgrounds for what was it? The content
fragment card list and I just wanted to show the content fragment card
list is actually inheriting all the actually no, I have something for
this already. It's inheriting all of the styles from the cards itself, so it's so
it's not something that's unique to the content fragment card list.
Just to be clear, it's um. It's one of the styles that's on the cards and the purpose for it. Uh,
here we go. OK, so if you have and excuse the crazy colors, but I was
trying to show it. If you have say a default card, I'm sorry if you do
not have like a specific card style. So like with tertiary, like you can see that the background can be set
to transparent. If I uncheck transparent background, you'll see that
it's white. If I set this to default and let's say transparent red. So
it's not it's not with default, it's with I believe primary button so
you can see a transparent background affect that. Hopefully you can see that. Sorry. Yeah, hopefully you can see that. And
then also with the tertiary tertiary style, if you need to have it be
transparent for whatever reason, you have that ability to do so. So I
think what if you were looking at a list, it might have had certain
things. It might have had say like the default overlay horizontal. To apply and transparent background is like it doesn't do anything. So
transparent background is specifically for like the primary button and
the tertiary link styling that's here. If you need to have say like a
different background color coming in and say you don't want that
default white, that's what the purpose is for. Yep. All right. OK. So I also know I saw the the list of questions for
the shared data page. I had only taken a look at a couple, so we'll
continue to review that and if there's a.

**Edwin Aquino** 15:24 OK, got it. Thank you.

**Daniela Tea** 15:40 Anything else we can show for that? I can certainly do that. But oh,
sorry, Edwin, there's one more thing I know that you asked. It was
about the redirect made URL. I did want to provide some documentation on
this that you'll be able to see so. The difference between a redirect vanity URL and just adding the vanity
URL entry is that the redirect vanity URL will cause the vanity URL to
behave as a 302 redirect. So this is something that like I I guess it's
dependent on what you're trying to do with the page like is this? You know, like a permanent redirect you're trying to do or is this like
a short-term redirect you're trying to do? So there there is
information on here. However, I realize this might be a more like
technical topic. So I don't know if Andy's on the call, but I believe
our plan is to talk more about the dispatcher and like redirect. Management and such in our technical enablement, but I did want to
provide, yeah, thank you, Andy. Yeah. So I did want to provide you some
information, Evan, from the direct documentation exactly what it does.
However, we can certainly get more into like redirects and such during
the technical enablement sessions.

**Andy Lambert** 16:38 Yep.

**Edwin Aquino** 16:53 Perfect.

**Daniela Tea** 16:54 Yeah. And I can, I can pass along this link to you in the chat. OK. All
right. OK, then. So now let's jump back over to our agenda for today,
which is news. So as mentioned earlier, we're going to go through all
the different news templates, the news content fragments. And the various news components. And just to confirm, the authoring team
right now is currently adding news to the corporate site, is that
correct?

**Edwin Aquino** 17:25 That is correct, yes.

**Daniela Tea** 17:26 OK, perfect. So in terms of like setting up any new news articles within
the dam, I I just wanted to confirm like the team, you know, like like I
don't think I saw anything for. So I didn't see a 2026 folder here, so
I wasn't sure if there was. Like anything new that had been added or like exactly how the team was
going to be handling news for the new year. So this isn't staged
though. I didn't want to go and prod mess anything around, but just
wondering, you know, like if the team has been adding anything new for
the year 2026?

**Edwin Aquino** 18:05 That is a good question. Carlos, would you be able to answer? Yeah.

**Carlos Aldana** 18:06 Yes, I think, sorry, I think that we added probably one, but we are that
is on prod.

**Daniela Tea** 18:15 Yes, that's on prod. Yeah, don't worry, this is stage. I just because
I couldn't, I didn't want to go into prod to look around and actually
do something. So I just wanted to. OK, perfect. So yeah, so you know as
the team has been practically doing it that we can we know what the set
structure is for news.

**Carlos Aldana** 18:16 Yeah. Yeah.

**Daniela Tea** 18:32 At least for corporate, I believe in pride you would see the similar
structure except for my KT folder which I only made on stage. So we set
up that same sort of structure also for the hotels based off of the
property name, course and language and then the year and then the month
and then the actual content. And so not certain if you guys are planning on changing that structure,
but this is again of course a way to organize your content to make sure
you're editing exactly what you want for the property that you want. In
my case here for my KT folder, you know I was also following a very
similar structure. I have my February item right here. So First things first, when we are
creating new news articles for say a new line of business like careers
or something, what you would need to do is in the dam, which we are here
under CF and under news, you just want to create your. Folder for your line of business and then just set up something very
similar to what I have here and then you can start creating your content
fragments under the specific month that you have. So I'm going to go
ahead and click create and click on content fragment. So as the team is familiar with, when I do that, I see the different
types of models available to me. We're going to select Muse, click next
and put my title, and I'm just going to hit create. All right, so here's my news content fragment model. You can see the
highlighted fields or anything that's required. There are certain
things that are not required but could still be useful. And as we had
mentioned yesterday when we were talking about content fragment models,
I did. I want to call out of course in the future as you guys are perhaps
identifying say other fields that you might want to add here or maybe
you're going to use some of the things that are previously not required
is required. That can certainly be done. Once you guys make that
decision, you can certainly. Certainly update the content fragment model. One thing to keep in mind
though is of course if you are say making like the author field required
suddenly and then there's content fragments that do not have that
value, that's the kinds of considerations you need to make. So
certainly a new field making a required that's not. Don't necessarily cause issues, but definitely want to plan and make
sure that before you create a content fragment model and before you edit
one that you have a clear understanding of of what field you want. Some
other things that you can do as we saw yesterday is say for your author,
say you know that right now it's a text field. And it's not required. However, say in the future you have a Bank of
authors that you might want to, you know, set as your own content
fragments with like their bio or something. This could potentially be
updated to say a content reference field to then be able to select an
author and all their information. Versus typing in the same name over and over again. So just trying to
give you guys some ideas of like what can you do to essentially create
additional models, like what are some considerations to take and how to
make it, you know, more like shared content, which is what we were
discussing yesterday. Carlos, I see. No, go ahead.

**Carlos Aldana** 22:05 Yeah, I I see that the image field there. So can can this content
fragment include the default image?

**Daniela Tea** 22:08 Mhm. And the content fragment create a default image. OK, so yeah, as we saw
yesterday, so I don't think a default image was set. However, let's
see here. So that can certainly this is what I mean. Like this is
certainly something that that can.

**Carlos Aldana** 22:19 Just. Yeah.

**Daniela Tea** 22:33 Be added in the future. Right now it's it's it's not a required
field, but what you're saying, Carlos, is that the expectations that
all articles would have an image. Is that accurate?

**Carlos Aldana** 22:44 Yeah basically because when when you publish A blog article then there
is the this feature that display that the new one on the website on the
landing page on the main page of the site. So it requires to have an
image if if we if we publish A blog without without image then.

**Daniela Tea** 22:49 Mhm. Uh. So are you talking? Yeah.

**Carlos Aldana** 23:03 And we have to do, we have to add something.

**Daniela Tea** 23:06 Just so Carlos, just to confirm, are you talking about this? Let's take
a look at the Hard Rock website and I just want to confirm which section
you guys are talking about. So I'm here on the news page, the blog
page. Are you talking about like these images here?

**Carlos Aldana** 23:19 Yeah, that one. Yes.

**Daniela Tea** 23:25 OK, so just to be clear that so this here, this here is a new search
result component and I'm going to jump back over to my page. That's
this this component. You can set a default image at this level.

**Carlos Aldana** 23:38 Yeah.

**Daniela Tea** 23:42 And so that would appear for any content fragment based off of what
I've what I've like configured here. Any content fragment that
doesn't have an image will automatically display this image within this
view. Is is that so is this what you're this is what you're referring
to correct cause like.

**Carlos Aldana** 23:57 Oh, OK. Yeah, that that would be a solution, yes.

**Daniela Tea** 24:01 OK, OK, cool. Because yeah, we can take a look. This is the test article
I had made earlier. So we can take a look at that test article. Let me
pull this up here. So my test article, I believe, was my was my training
article. I think it was this one. Oh, Nope, sorry, it was my. News article so that so you'll notice my title is is slightly different
from what my title of my actual article is. But yes, so this is the test
article and you'll notice here I left the image and the image alt text
blank, but I set the image at that component level so that way something
would. Appear here in the new search results. So hopefully Carlos, that answers
your question on how to have like a default image for anything that
doesn't. If you don't fill it out, as long as this is set with
something, then that would display within this page.

**Carlos Aldana** 24:53 Yeah. OK. Thank you.

**Daniela Tea** 24:55 Yeah, sure. OK.

**Edwin Aquino** 24:57 So Danielle, with the with the images, just to expand on Carlos,
sometimes we have it to where we have default images on categories. So
let's say we have A tag and the tag is, you know, it'll say casino,
it'll show an image, a default image of the casino, unless if we
override that with something else or if we have.

**Daniela Tea** 24:59 Yes. Mhm. Yes. I see.

**Edwin Aquino** 25:17 Have the A tag that says hotel will change the image just so that The
Newsroom is a little bit fresh. It's not constantly the same stale
image over and over again. Um, is there kind of any kind of
functionality we have here that can imitate that?

**Daniela Tea** 25:23 Mhm. Mhm. I don't think we have the default image set based off a category like
based off a tag. I do have a question though. So like is there ever any
use case where like for example say you had tagged Hard Rock News and
you had tagged like gaming? Are you saying that perhaps like there would
be a default image for gaming and a default image for Hard Rock News?

**Edwin Aquino** 25:44 Mm-hmm.

**Daniela Tea** 25:50 Is.

**Edwin Aquino** 25:51 There would be and in this situation where you would have multiple tags,
it would pull that first tag's default image rather than the second
one.

**Daniela Tea** 25:55 Uh. OK. So it always based off of the oh, oh, based off what you selected or
based off the outcome order. OK, OK, so like.

**Edwin Aquino** 26:03 Correct. Or we would override it to whatever we wanted if if there was a unique
image that we can use for that article.

**Daniela Tea** 26:11 OK, so yeah, so right now the default image is based off of what what's
set in here. So clearly you can see it's not based off of categories. I
I do understand what you're saying, but I think that this would one,
this is a gap, but I think we would also want to discuss like the
requirement that you're. Saying because like I can certainly see like you know if you have plenty
of categories selected, now the author has to make a choice as to which
specific default image should be prioritized to show for here. So
that's gonna, you know that that to me is like, OK, yeah, want to dig
deeper into that.

**Carlos Aldana** 26:45 Mm.

**Daniela Tea** 26:50 So want to make sure that we capture that as a gap and then also want to
make sure that you know there seems to be some sort of requirements and
logic that are that would be required for us to like jot down for that
one since yeah, the multiple of these articles probably would have
multiple default images selected. So want to understand how we would
want to make that work. Work. So no right now, but could be in the future, yes.

**Edwin Aquino** 27:10 Got it. Yeah, got it.

**Daniela Tea** 27:15 All right. OK, so let's go back to my news article that I did not fill
out, and let's go aptly to this category section here. So I'm clicking
on my little field. You can see it's showing a list of. Tags here. And so to be clear, this specific field, if we were to look
back in that tagging section, all of these tags are tags that are listed
as news categories, so. Let's see how this was mapped, going back to tagging and I'm clicking
on some of Hard Rock support. I'm gonna click on news categories, cafe,
news, casino, featured gaming, etcetera, etcetera. So this particular
field has been mapped to our actually is it this field? It's either this field or it's one of these fields. Actually, yeah,
no, I think it is this field. OK. No, hold up please. Uh, here we go. It's been mapped directly to the
Seminole Hard Rock support tagging section. So this namespace is showing
all of these. Of course, in the future, if that's something that you
want to change so that way it defaults to just news categories only,
that's of course something that that could be. Configured by editing the content fragment model. In this case though
there were some I think flexibility involved so that way I could choose
other tags, but in this case I'm just going to choose some specific
news categories and just hit select. All right, all right. So now I have three tags associated with this, of
course, my article's title. And then my ublish date. And my image I'm going to leave blank my excerpt this text excerpt.
This is my description. This is additional content, a different page. I'm going to fill in the
author field, but I don't think we're currently using that. And then
we also have here some additional tags which are different from
categories and then we also have the page path which is. When you create your new news article, all all this particular content
that we've stored here will be displayed on that. So I don't have the
page path yet, so I can't put anything. And again, the LD JSON field is
something that's on our content fragment models, I think all of them. This was a requirement, I believe, for SEO purposes, so I'm going to
leave it alone since we're just like training right now. But I do
believe that there are instances where you guys have filled this out, so
we could potentially take a look at that in a bit. All right, I'm just
going to go ahead and save since I filled out my required fields. And now I'm going to go back to my KT news page. Age. And see how it looks. So it's not going to appear in my new search
result yet. The reason why is because I have not published my content
fragment. So this is my previous test article that we had taken a look
at when we're looking at the default image. But it's not showing the other one that I had published or sorry that I
had just made. So let's go ahead and publish that right now. I'm going
to close this. And I'm going to select it and hit my quick publish close. And if I
refresh this I should now see two articles. Here we go. Test article.
This excerpt test. This is a test article. This excerpt. I know this is
the right one because I have the tags I selected. So in case like if you guys, as you guys are adding these articles and
since you guys are working on these, you know right now, hopefully you
guys have not like had that freak out moon where where did my news
article go? Make sure that you publish the content fragment and then you
should be able to see it on on this page and know this page. Not published, so no one else is seeing it. I'm just viewing it within
my author. OK, so I can see this here and when I click on read more. I shouldn't open this in new tab. Let me refresh. OK, when I click on view as published and then I'm going to click on
read more. Is it this one or is it this one? Uh, OK, I know what I did wrong. OK, so. So right now read more is not going to do anything yet. The reason why
is because if I were to look at my content fragment for either of these,
the page URL, the page path that has not been published, the page path
is not does not have any value. It's opening up my KT training article. There's no, there's no page path, so there's nothing for me to
actually go to. So that's why the read more button's not working. Sorry, I'm gonna close out. Let me close out a couple of these tabs
first. All right, so let's stay here. Yeah. OK, cool. Um, so how do we, how do
we get those read mores to actually go to a specific details page? Let's go back to our site's view O here, as the chart says Cororate
careers EN. Here's my news page. I am going to create a new page and I am going to
select news page. So here's all the available templates I have. I'm
going to select news page. I'm going to click on next my title. I'm
going to call it KT article. Oops. And I'm going to click create an open. And on this page I'm going to click edit the this particular news page
template. What it does is it's going to have a the header and footer
that gets automatically pulled in. You can see this experience fragment
which is pointing to a specific image so. By default it's going to show whatever is in this experience for me.
You can change it if you need to to something else, but this is I
believe this is what was established for the corporate site. Of course,
if you guys are trying to use this in other places, you can certainly
customize it to be a different image. We also have our breadcrumb functionality here. We have a news content
fragments component. Another experience fragment is just listed here in
case you guys need to show, say like specific texts that's shared
across articles. This is one place to put it. Then we also have our related posts
component which will be pulling in any articles that have similar
categories or tags. And then on the right we have this new search
component. We have this category listing component and then we have another
category listing component, but it's displaying different tags. So
let's break down everything that we see on this page. But first
starting with our news content fragment, I'm going to click here and I
am going to select which content fragment I want to display. Display. In this case I want to display my. Training article that I just made and you'll see here display mode
multiple elements being. I just want to show everything from here.
Variation. I'm not going to touch it. There's I don't have any
variation for this content fragment. I don't necessarily need to fill
out the ID field. The searcher page search result page though I do need to fill out since
it's a required field. Since I have not set up a search result page for
my little test site. Currently I'm just going to point it to the
existing one underneath corporate, but that's that's just for right
now because I don't have that set up. Up. And I believe that's located here on log and search. Here we go. So
this is just temporary, but we're going to also set one of these up for
my little training site. So select. And hit done. So now this is going to show everything that was stored in
my news content fragment. We can see here all those different categories
that I applied, the date, the social share also automatically gets added
and then here is the description portion that I had. And then the additional content, which is something that's only
displayed on this page. That's why I put that note to myself. So all
that is here. So this portion's configured. I'm going to ignore the
experience fragment for right now because there's nothing that I care
to display from the experience fragment on this page. For related posts, let's configure that. By default you're going to
have the placeholder of related posts as the title. This could certainly
be changed to say like related articles or other news or whatever it is
that you want. Right now we're going to be displaying up to three cards at a time. I
point to my content fragment path. I'm going to choose EN. And then I can have a default image if I want to, but for right now I'm
just going to hit done. Yes, Carlos, go ahead.

**Carlos Aldana** 37:24 Daniela, at some point, for example that path or the one for the search
option, those paths at some point are going to be set by default. So do
I I don't have to look for that?

**Daniela Tea** 37:25 Mhm. Mhm. So keep in mind that what I'm showing is if you were to set up a
completely brand new news page right for like a say like a hotel or say
a like for the career site. Since we don't know exactly what you guys want to do, like where this
is located, This is why it's required for you guys to configure this.
However, what you're asking though is as you're creating new news
pages underneath the same location, you're wondering, can that actually
be filled in in advance? So that way you don't have to worry about it. Is that correct? Yeah. So
right now it's it's not filled in because again, like we didn't have
any default values for this depending on where you're using this. But I
can understand what your use case is. I think I would capture that as a
gap.

**Carlos Aldana** 38:18 Yes, yes.

**Daniela Tea** 38:34 With the desire to have a search result like certain fields, identify
which fields would make sense to be essentially have a default value and
establish like you know. Obviously if you're like if you're setting
something up new for the first time, there can be no default value
because it doesn't know exactly where you're trying.

**Carlos Aldana** 38:43 Mhm.

**Daniela Tea** 38:54 Where the location is, right. So these are the kinds of requirements
that would we would want to understand and that's why we want to make
sure this is captured for the gap. OK, yeah, no, but that that's a I
agree though. I understand where you're coming from, so.

**Carlos Aldana** 39:04 OK. Thanks.

**Daniela Tea** 39:09 OK. Yeah. And so it sounds like also like like related posts, you know,
so this is like what I would capture as well. If you know that the CF
folder path would be the same for all the related posts and that you
would eventually want that to have a default value, that would totally
make sense. So we want to make sure that that's also captured. All right. So, yeah, go ahead. Sure.

**Edwin Aquino** 39:28 Yeah, Danielle, Danielle, sorry. I'm just thinking like if there's
maybe some kind of logic that could be applied since we're creating
this article underneath, you know, the Hard Rock page, it should note
that it's coming from that path directly. That's the kind of thing
that is that something that could possibly be addressed in the gap as
well?

**Daniela Tea** 39:38 No. Yeah, that's that's exactly what I mean. Like if you guys know anytime
you create this news page under like you're you say, OK, yeah, I know
it's going to be in this specific location. That could be the
established default value and then that's what you would want to be
stored, right? Yeah, that's exactly what I what we would want to
understand. Mm-hmm.

**Edwin Aquino** 39:58 Perfect. Yeah, cool.

**Daniela Tea** 40:03 Awesome. Yep. OK, so right now you can see I have no related posts and
the reason why is because the other section where I was sorry, this
particular folder path only has two articles and they don't have any
overlapping categories. I'm going to actually change this really quickly to cororate and see if
anything OS U. OK, Yep. So you can see now, yes, related posts is working because these
particular items match the categories I have associated with this
article. So that's, you know, just wanted to show that. So that way you
guys understand how related posts like the logic for that in this case
though because I'm pointing it to my little. Training folder, which has nothing in it. Basically that's why you're
not seeing anything. But of course if I add more articles and such and
had matching tags and this would surely be displaying things up to three
items, since that's what's been configured. All right. The other things that you would need to configure on this page would be
the search right now again, because this was specifically only for the
the corporate news. That's why this was the default, but this could
certainly be one of the things that would totally make sense. To change this instead to whatever the site that you are in to default
there. I kept it this to to this one right now just because I don't
have my search result page set up, but this is also something I would
envision you would want to capture in your gap. Then here we have our category listing. Open this up and see the titles
as categories. My search result page. Again, I'm pointing it right now
to an existing one, but this is something I would change depending on
where I created this specific page. My listing type. I have the option of either categories or archives. In
this case I'm choosing categories and then I'm saying OK, find
anything within this path that's been chosen and display all the
categories that are in there. So if I were to change this to my. Little training folder. This is this should be a lot smaller. Yeah, so now it's pulling in,
looking at all the content fragments in my little training folder and
extracting all the tags that were within there. And so if we recall I
used three tags in this one. The other one I had applied Caffe News and
Casino News. That's why these are appearing here. And finally with this archive section. Same component category listing. It's just that archives is the listing
type for my content fragment list path. I am again just going to change
to KT and we can see what gets here. So right now you can see it's
it's it's just showing EN like there's like I don't. I don't really, again, I don't really have anything associated with
that. So that's why it's it's not actually like showing much. If I
change it back to like say corporate, we're going to see where is it? Actually, I don't think it was at corporate level. I think it was at
the news level. Yeah, OK, so these specific you'll see here. This is showing Roxino, KT
Hotel and corporate. This is showing the folder structure that's listed
here. I think if we take a look at the hardrock.com site. And we look at blog, which I have over here and see what it's like
currently on production. So the archives are displaying the different
years. I don't have the years necessarily set up like that on mine. But let's see. Yeah, so on this particular page apparently is
configured a certain way, and then on some other pages it looks like it
might have been configured differently. I'm just pulling up some other
ones, but this is configured at both the. News article page level on the news on the news page template. This is
the news page template and then also on the news homepage which is when
you view the news website. So this is the news page. And then this is. This is the this is the news page template, but a lot of things are
shared between the two with the sidebar and then of course like the
header. So there's gonna be a lot of similarities between those two
templates, however. The news page is for one specific article, whereas the news homepage is
for when you were displaying all the news. OK, so that is the yes,
Edwin, go ahead.

**Edwin Aquino** 45:04 So I just wanted to go over a few things on since you know it looks like
we covered a bit with the new page template. So I'm just gonna back
back up a little bit. When we do the create title, is this impacting
anything like is this creating the impacting the metadata or anything
like that?

**Daniela Tea** 45:08 Yeah. Yes.

**Edwin Aquino** 45:20 What? What is this crew impacting?

**Daniela Tea** 45:20 When you say. Which title are you talking about? This is a test article or the the?

**Edwin Aquino** 45:23 Yeah. Let me first create the page, right? When we're creating this page,
right?

**Daniela Tea** 45:28 OK, I see. So if I were to take a look at my properties, so the title of
my page is KT article. So ideally what you would do in my case I
didn't, but ideally what you would do is this would likely this is
likely what you would want the title of the page to be. I would imagine
right?

**Edwin Aquino** 45:37 Yep. Mhm.

**Daniela Tea** 45:48 Visit as article. So when you're creating the page and I believe I saw
you guys were doing this essentially copying whatever you have in the
content fragment and then when you create the page with the page title
and such, that's where you just, you know, paste it here. So that way
everything is all matching for like SEO purposes, right? Like the title
of the page as well as like the each one that's on the page. So I think that's what you guys are doing right now. In my case here, I
was just putting something for knowledge transfer, but from a practical
standpoint, I think you guys are likely just going to copy whatever the
title of the content fragment is.

**Edwin Aquino** 46:23 OK, great. And I'm just trying to go through a few things here under
page properties. If we go back to that, the more titles and description,
what what is the page title used for and and like where what what is
this being used for?

**Daniela Tea** 46:24 Yeah. Yeah. Yes, sure. Yeah, yeah, sure. And actually I yeah, one second. I want to pull up the
documentation for that cause it does a pretty good job. I I hope it, I
hope you would think it does a pretty good job of how it breaks down.
But I think we saw, I believe I saw in some instances you guys are
using.

**Edwin Aquino** 46:41 Is this the meta?

**Daniela Tea** 46:59 Different values for here. To be clear, if you leave it blank, it will
always default to whatever like the title is. So you'll see here page
title is typically used by title components. So when you put a title
component on the page, it will take whatever's listed in here and it's
going to be the default value for your title component which you can. You can of course change later. However, in most cases, like I think
I've seen a lot of instances where this is usually left blanked and
then just defaults whatever you have in this section here here for
navigation title second. So it says here you can specify a separate
title for use in navigation. For example, we want something more
concise. If empty, the page title is used, this is empty again, so therefore
it's defaulted to KT article. So when we're talking navigation, like
if you're like trying to surface up like a list of a list of pages, or
perhaps I would say like in the navigation itself and you don't want to
have like that long article name. Or something. If you need something different, you could store that
value here. And so that way if this, you know if this has anything
there, it would it would default to this one versus just looking at the
title and displaying that instead. So if you leave this blank, yeah,
yes, exactly. That's exactly right.

**Edwin Aquino** 48:09 Basically like like like a breadcrumb or something like if you wanna use
it in a breadcrumb or yeah.

**Daniela Tea** 48:15 And then subtitle. So I think this here I know the subtitle for your sub
page is kind of vague, right? I believe we can actually put something
here. This is the subtitle and then let's take a look at the page and
see where it displays training, but we'll take a look at that in a
second. And then of course the description this I believe would. Would be what's displayed like in say like the like Google search
results or whatever if you have something here. If not, I believe it
takes like the first, you know, paragraph or however many characters
from whatever's on the page itself. So let's take a look at where
subtitle shows up. I'm going to view as published and I am going to actually inspect it. And I'm just going to type in subtitle and see what pops up. OK, so in here. Let's view source. Hmm. Well, I did save it here. All right, let me take that one back then.
Edwin, let me get back to you on that one. Let's save it. This is the
subtitle training. Yeah, let me get back to you on that one, because now
I don't think so to be to be. Perfectly candid with you. Typically like when when I see pages created,
most people might fill up page title or navigation title or just the
title itself in the description. I don't there's I, you know, I
haven't seen subtitle being used on like. A lot of sites, but I want to get back to you on exactly where that is,
pinpoint that and then show you that way. If you guys do use that field,
you understand what the purpose is, OK.

**Edwin Aquino** 50:14 OK, perfect.

**Daniela Tea** 50:15 Yeah, but alright.

**Edwin Aquino** 50:16 Alright. And then can we go over a few more things with the news content
fragment if you can? Um.

**Daniela Tea** 50:19 Go back to. Back U and we can take a look at the content fragment itself.

**Edwin Aquino** 50:28 Sure. I just didn't wanna interrupt your flow of, you know, going over
the content.

**Daniela Tea** 50:29 Um. No, no, please. This is great. I just wish I was better organized with
my tabs. OK, assets. Let's navigate back to our news. OK, go ahead.

**Edwin Aquino** 50:45 So with the content fragments, I see that we have a a published date for
that. Is that specifically related to when the article will go live on
the website or is that just when we want to display that information?

**Daniela Tea** 50:50 Huh. No, but yeah, that's just so you'll actually notice if I go back here,
if I go back to the home page of this. Oops, didn't do that right. OK, if I go back to the home page of this, you'll actually notice this
particular article's displaying, even though it says February 23rd,
today's February 20th. So it's for display purposes. However, you
know, keep in mind that there is that publishing functionality. So for
let's see here. Um. Oops. So when you manage publication. You can schedule that, but the actual published date that you are
selecting within the content fragment itself is for the like display
purpose. Like it's essentially the date of the article, right? So it
has nothing to do with scheduling within the content fragment itself,
OK.

**Edwin Aquino** 51:55 It's just for displaying and if we wanted to add the time, we can
always update the content fragment model to include the time as well.

**Daniela Tea** 51:57 Yeah, it's for display. Uh, yes. So right now I think we had defaulted the value to just be
date, but if I'm not mistaken, you should be able to set like you know,
date, date with time, that sort of stuff. Yep.

**Edwin Aquino** 52:15 Perfect. Alright. And then could we do a little bit deeper dive on the
new search functionality? Um, what exactly is triggering the results
here specifically when we use this component?

**Daniela Tea** 52:20 Yes, sure thing. Yeah, so this particular component and let's create a new search page
and then we can see and then I'm going to update this to instead of
pointing to this version, this corporate version will point to my new
one. Alright, so let's go back to. I'm going to close out of literally everything, if possible. OK, so this is here. All right, perfect. I'm going to create a new page
under my KT news home and I am going to select news search template. OK,
next this is my KT search. And OK, right create. All right, the page has been created. So on this
particular template. As I mentioned before, things are going to be, you know, shared. It
looks very similar to the news page template and also the news home page
that we were just looking at just now. In this case here though, what is
different is this news search result component. So if I were to take a look at that, I can see I can configure things
such as how many results do I want on the page before pagination shows
up, right? Older post label, newer posts, the no results found message,
the read more text. I'm pulling in the content fragment path where I want all my articles
to be. In this case I want it to all be within that KT folder. Yeah, let's do this all right. And then setting that default image
here. Um, let's just choose anything. Yeah, sure. OK. And then I'm gonna put 5 results per page. And this is
this seems weird, right? The search results page. It's like, wait, am I
going to be pointing to myself? And I actually need to check this one
here, but for the time being. I'm going to put where I have this page created which is. Select. All right, done. OK. All right, so now I can see that my articles from that specific folder
are displaying here and that you may think, OK, well, well like like
what is the purpose of that here? Like this seems to look exactly the
same as what is on our home page. Let me pull up the home page for
reference. This is the homepage for reference and it is using the exact same
component. However, as you're searching when you're searching on the
new search, instead of it taking you back to the homepage, you can see
there's some additional stuff on this homepage. There's. Like the featured news, which you can put here. And then there's also I
think, I believe there might be some additional components or text or
something that you guys might have present on the news homepage. So
instead of having, you know all this information here at the top. Before your users actually get to the news search results. That's why
there's a separate page which essentially like see it removed
everything else from there and it's literally just showing the new
search results. So now if I were to. Change my KT News home new search component and point to my. Age that I just created. Done. And if I were to view this as published. And if I were to try and search up the word. Wish I didn't use the exact same things search. This should take me to
the search page I just created and you can see I search for this and
it's showing my this is a test article and you can see it took me to A
to the search page itself and not like refreshing the home page. And also keep in mind I had selected a different default image. That's
why this is here, because this particular content fragment did not have
an image associated with it and I said it at the component level. So I
guess Edwin for your question about what's the purpose of the search,
just to make it clear. Page is slightly different from the whole page in the sense that it
doesn't have any of this other stuff on top and it's basically
bringing the search results to you like you know, like immediately
versus having like the featured news and anything else that might appear
on top of this component.

**Edwin Aquino** 57:31 Yeah, not not necessarily the purpose. I was referring to what is
pulling in the actual content. So is this similar to the search query we
were looking at earlier where it's checking everything on the content
fragment, whether it's the categories, tags, a title, everything? What
is it pulling in?

**Daniela Tea** 57:38 Yeah. I see. So search itself. Oh, like what is the actual this part here
looking for is what you're asking. OK, if I were to search an excerpt,
I do believe it is indeed showing or pulling in.

**Edwin Aquino** 57:50 Yes, correct. Yes.

**Daniela Tea** 57:59 Oops. One second. Oh, did I change it back? I change it back. I don't know if I changed it back or not. It should
be based off of the things within the content fragment, right? So like
whether it's in the title or whether this is the, this is the excerpt,
and then there's also a description field. See here. This is take one second. One second. Let me go back to my search page.
Oh, I didn't. OK, I didn't configure it on my search page. That's why
it's doing that. OK, all right. Alright, so now if I were to go back here and let's take a look at
searching for the word excerpt this time to show that it should pull in
this result because it's the search is looking also within that field
as well. OK, so it's not. So it's not pulling up. Sorry. Must then just be the
title. And the description, I believe let's pull in. Let's pull in the description. I want to see what the description is
and we can take a look at. We can put actually a specific term there to
confirm that that's showing up. Let's say property. I'm just putting. I'm just putting some of a term
here that we can reference and I'm going to hit close. All right, let's now publish this. And I am going to refresh this again and we're going to search for the
word property.

**Edwin Aquino** 1:00:02 Can we also see if this is pulling in possibly tags like reverb or or
something? I know we have tags that we could just click. I'm just
curious what else is being pulled in here.

**Daniela Tea** 1:00:05 Yeah. No, sure, we can. We can certainly let's let's. I think that's a
good, it's a good way to be able to confirm what you're expecting.

**Edwin Aquino** 1:00:17 And and how are we adjusting this exactly? Like what if we wanted to
change how the search is being populated? Is there any kind of is this
functionality being built in already into the component or is there any?
Yeah, how are we changing this?

**Daniela Tea** 1:00:30 Let me pull up the ticket really quick. I believe for this one this
would be something that's within the components functionality, so that
would be like a a a code change, but one second. I'm waiting the search component and we can take a look at what was
captured for that. But to your point though Edwin, I think like for this
here understanding exactly what should you know be tailored for the
search like. You mentioned tags and like I guess you know that that's certainly
something that could be added, but keeping in mind, you know like is
that something that you would want to see here? So like you might feel a
lot more than you're anticipating if something was tagged a certain
way. So I guess identifying you know like which parts of the content
fragment model would you want to?

**Edwin Aquino** 1:01:19 Yeah.

**Daniela Tea** 1:01:25 Want to surface up in the search, like perhaps just the title and the
description or the title and the actual article, the tags and the
excerpts. So taking a look at what you guys want, that can certainly be
adjusted, but that would that would have to be a code change.

**Edwin Aquino** 1:01:41 Yeah, and it's just, it's just because it's not very intuitive as to
what it's actually doing, right? It doesn't like any kind of like keep
a tool tip or anything that's telling us exactly what it's searching
for. So if anything, just things to make it more clearer for the end
user, that'd be perfect, honestly.

**Daniela Tea** 1:01:45 Yeah, understood. Mhm. I know, I agree. That totally makes sense. Um, so let's take a look
here. I'm just taking a look at at what was captured here. So it's based off of keywords is what it says against the title, the
excerpt and the full body. That's what the keyword search should be is
title, excerpt and full body. So if I were to. Type in and this is. So if we are seeing that the excerpt text is not appearing on here, Yep,
alright. So the fact that this is not appearing is something that I
would want to investigate a little bit more. It might be because of the
content I have in my content fragment. Because I kind of put, I kind of put like, you know, bare bones test
data. But the intention for this is supposed to be those three different
fields. So this, this and then also the body. But this is something
I'll have written out as a take away for us to investigate and confirm
since that is what the search bar is supposed to to. Work against and to your point about a like a tool tip or something,
depending on what you guys decide, like how you would want this search
to search against, maybe it's more than those 3 fields that can you
know within whenever that code change is made, a tool tip could
certainly be added with that information so that way the. End user knows what they're searching against too. Yeah, all right, so
I have this one as a take away. Anything else but the news search. I
also want to cover the news homepage template since that's also a
that's a different template and that's something you would need to do
to set up a news.

**Edwin Aquino** 1:03:26 Okay, perfect. Thank you.

**Daniela Tea** 1:03:42 section in any other site. Anything else about this search page?

**Edwin Aquino** 1:03:48 Um, finally, one last thing is where do we add the category? How do we
add additional categories that we can select from?

**Daniela Tea** 1:03:50 Yeah. OK, yeah, sure. So categories are going to be added in in the tag
section. So if we were to go back to our little hammer and tagging. And I'm choosing Semo Hard Rock support. As we saw, you know when
you're creating an article, you have the option to select from any of
the tags that are located within this namespace. If you're trying to
add a new tag to like say the news category, so that way this is
available like one of the options available. You'll click create, you'll create tag and then you would put whatever
the title of the tag is here and then that would eventually. When I say
eventually I mean like it will be available then to people who are
creating new content fragments, you would see that tags an option to
select. So anything that any article that has that tag would then appear in this
section.

**Edwin Aquino** 1:04:50 All right, perfect. Thank you. That's it for me.

**Daniela Tea** 1:04:51 Yep, yeah, sure thing. OK, OK, I'm going to now switch on over to my
homepage template. I'm going to create a completely brand new one so we
can see, you know, again, the process of if you have to do this for,
say, a new site. So here I'm going to just click create and click on page. So I see that
option for news homepage and I'm going to hit next. OK. I'm going to hit create. OK, so creating a completely new homepage, this is what's going to look
like. It's pretty empty and so it's basically the the portions of the
site that you need to configure like we saw earlier, setting the new
search categories and archives to point to where you need it to point to
setting. New search results to point to the content fragment folder path that you
need to when filling out this information. But the main difference
between the news homepage and the new search is that you have an area to
feature some news. So as we see on our homepage here on the Hard Rock blog homepage, we
have this section for the title News and Press Releases. Right now the
title is defaulting to what I need it. However, as an author, I have the
ability of course to configure that with whatever title I need. And then here in this section this year we had the featured news that
again title for you to put whatever you need, featured news or featured
articles, whatever it is. And then the ability to select exactly what
you want to feature. So in this case here this you can see. That this isn't necessarily going to be the most recent ones. It can be
things that you specifically select, or if you did want to be the most
recent ones, you could. You could do that too if you always wanted that
to show up here. Just keep in mind though that. Whatever. Like if you set it to be like, you know, show most recent,
then that of course will change without you intervening with it. So if
you really want to just say like pin a news article, then you would want
to select that like fixed list or something like that in order to make
sure it's showing exactly what you want versus changing out. Out without your own control. So just some options here to be able to
feature articles is really the main difference, but just this is one of
the parts of the news portion of your site that you need to take into
consideration if you're creating it for a new a new property. So any questions like what the purpose of this news homepage template
is? OK. OK. OK, um, let's take a quick look at our agenda. All right, so we have our news homepage template, news page template,
new search page template. Then we saw the news content fragment. We saw
our new search which is used on a couple of pages, the category listing,
the social share which is on the article page enabled by default. That can certainly be turned off if that's something you want to do
related posts and how it pulls in based off of the article's category
tag and then also the news search results component. So these this here
new search this was. Let's see this here is that new search here, whereas new search results
is this section here. So I know that might be a little confusing, but if
you look at the titles of the component you would see that's what this
this is referring to as new search and this here is new search results. OK, um, let's see. So any questions about news, anything that was covered today or any
questions about say, setting up a new section for a completely new
website or property?

**Edwin Aquino** 1:09:16 Just one thing regarding the social sharing. How does that information
get populated and what exactly? How do we edit this information?

**Daniela Tea** 1:09:19 Mhm. Alright, let's take a look at social share in one of these pages.
Alright, so I'm going to open up one of my knowledge transfer
articles. All right, so social share this as mentioned before, this particular
component is just part of this this news content fragment component. So
when you fill out the news content fragment component, this will also
appear. When I configure it, I can see I can enable Twitter, Facebook and
Pinterest. I realize maybe you guys might consider wanting to change it
from Twitter to X, but keep in mind this is only shown to the authors.
But if I were to say what the author can do is if I were to uncheck
these. And that would remove those options from displaying to the end user. So
if you guys decide, oh, I don't actually want this to be shared on
Pinterest for whatever reason, you have that flexibility of removing
that specific social media icon. But your question was like what? How
does it share? Is that is that correct? Correct.

**Edwin Aquino** 1:10:32 Yeah, So what is exactly pulling in from the article? Is it pulling the
article title? Like where is this information being pulled from?

**Daniela Tea** 1:10:36 Right. So I wish I could log in. I don't actually have. Yeah, I don't
have. OK, so this is supposed to be pulling in from some information
that's, you know, within our basic tab. Let me see if I can. For this one, Edwin, I might want to create because I don't. I I'll be
honest, I don't have X so I can't show you exactly how it works, but I
don't mind creating like a an account for the purpose of that. But I
can show you a screenshot of like how that's being shared and like
point that to. The specific properties that's coming from. So for example likely going
to be like the title and the description as well as on this images tab
you have the ability to set a specific image that's associated with
that. So like. These fields are not required because you don't you might not need it
for other pages. However, this is these tabs are available. So I want
you to keep in mind though that I am planning on going over page
templates a little bit more in depth. I'm trying to see if I can. Put that as to one of the sessions next week. I would like to go over,
you know like the the custom tabs that we had added as well as the
different page templates and then also like you know how do these come
into play when it's like shared across other sites and other
platforms. So we'll definitely get more of that. And by then I will make sure I
have my X account created so you can see what that looks like when
we're sharing these pages across social media. Does that sound good?
Yeah. OK, Yep, absolutely.

**Edwin Aquino** 1:12:19 Perfect. Yeah, that sounds great. Thank you.

**Daniela Tea** 1:12:24 OK, um. Anything else? Try to take a look here to see what like, since I know
you guys are already using news, it's like, yay, you guys, you guys are
probably already pros at this. Yeah, so like, you know, I can see this
news, new news article February 5th. Yep. So just to keep in mind, and this is what I meant about like, you
know, if you guys ever have content, going back to our discussion
yesterday, if you guys ever have content that's like potentially going
to be reused across multiple articles. That's when we would recommend, you know, using like an experience
fragment. Say this, say this here in particular. I know it's probably
not going to be shared across all these articles, but say this was
something that's a constant on every article. It might make sense to
put that within the experience fragment and then just reference that
experience fragment with. In the article page itself, and then if this ever changes, you only have
to change it in one place.

**Edwin Aquino** 1:13:26 Perfect. Good to know.

**Daniela Tea** 1:13:29 Yeah. All right. OK, guys. Anything else before we wrap up? I know it's Friday afternoon, so I
don't want to keep you guys too long, but happy to take a look at
anything else if you guys have any questions right now.

1:13:45 No.

**Lucas Nelson** 1:13:49 Hey Daniela, it's Luke. I scheduled the remaining sessions for next
week and the three days of the following week for content authoring, and
then I also scheduled the adoption sessions.

**Daniela Tea** 1:13:51 Hey. OK.

**Scott Sorel** 1:14:04 Mhm.

**Lucas Nelson** 1:14:06 Uh, starting the end of the week after next. Um, so those are on the
calendar. Um, we'll we'll.

**Daniela Tea** 1:14:10 OK. Let me let me flash up the calendar really quickly then. Luke, one
second. OK, I'll pull that up.

**Lucas Nelson** 1:14:16 Yeah, and we'll we'll owe agendas on the invites, Daniela. OK, OK.

**Daniela Tea** 1:14:22 Yup, understood. So yeah, let's let's take a quick look to see what we
have ahead. OK, Yep. So let's see. We are here. So next week's gonna be all
content authoring and then the week after, like you mentioned. OK, Yep.
So I see the first adoption session is going to be on Thursday, which
also coincides with the beginning of the.

**Lucas Nelson** 1:14:42 Yeah.

**Daniela Tea** 1:14:51 Um, technical knowledge transfer.

**Lucas Nelson** 1:14:51 Yeah, and and the other comment there is Scott and I are working in the
background. I'm gonna schedule those technical enablement sessions. So
Andy, perk your ears. It's gonna be from 9:00 to 11:00, the 5th,
Thursday the 5th through Thursday the Thursday the 12th. That's the two hour blocks that we're going to cover those technical
enablement sessions. So you Yep. So we'll see those on the calendar.
And then last but not least, we'll have the platform expansion
discussions on the calendar as well for the two weeks on the last part
of the schedule.

**Andy Lambert** 1:15:15 Sounds good.

**Daniela Tea** 1:15:28 OK. And to be clear, these are going to be in the afternoon as well as
the adoption ones. It's just strictly the technical knowledge transfer
ones will be in the morning.

**Lucas Nelson** 1:15:32 Yeah. Yeah, just because we want to include Vinay to to co-lead those with
Andy given the context he has. So Yep, I just wanted it was housekeeping
at the end of the call. That's all I yeah, I'm, I'm sorry to be the
guy to schedule a Friday afternoon call. So you know you can blame Luke
for that.

**Daniela Tea** 1:15:39 Yep. Yes. Yeah, that's good.

**Lucas Nelson** 1:15:54 Uh, but if there's no other questions, appreciate your time everybody
and have a great weekend.

**Daniela Tea** 1:16:00 Thank you, everybody. Goodbye. Thank you.

**Edwin Aquino** 1:16:00 Have a great weekend, everyone. Thank you, Daniel. Thank you, everyone.

**Shirley Madera** 1:16:03 Thank you.

**Scott Sorel** 1:16:03 Great. Thanks, Luke. Thanks, Danielle. Good job.

Lyon, Rick (Director of Digital Experience)** 1:16:05 Thanks everyone.

Scott Sorel** stopped transcription

---

## Session: Locations — 2026-02-23

**SHRSS Adobe Knowledge Transfer-20260223_130200-Meeting Recording -- PART 1**

February 23, 2026, 6:02PM

49m 15s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:07 (Part 1) All right, we're off and running, Daniela, whenever you want to get
started. Thank you.

**Daniela Tea** 0:12 (Part 1) OK, awesome. Thank you. Hey, everyone. Good afternoon. I don't see
Edwin on right now. I wanted to follow up with some of the questions
that he had from our Friday session, but perhaps we can cover that at
the end of the call if he's able to sign on then. And if not, then I can certainly post responses on Confluence later. All
right. So today let's go ahead and share my screen. We can take a look
at our agenda. OK, today we are going to cover locations, so location related
components as well as some of the content fragment models associated
with locations and see examples of how these components are being used
on. The Hard Rock websites specifically for the corporate site, cafes and
hotels. So as you can see here, we do have two content fragments to
cover 1st and then we'll take a look at some of these components. So let's go ahead and get started with the location content fragment.
So I'm gonna jump on over to AEM here and just navigate again to the
section where we're going to find our content fragments. So let's if I
were to click on the AEM logo in the top left. I'm going to my assets, going to my files and then SHRSS and CF and now
I can see here is the folder for locations and you're going to see a
breakdown of all the different regions. Four locations and as I click on them, I'll see the particular country
names and then I will see the particular content fragment itself. So to
be clear, hang on. Alright, so this is so I wanted to call out something
that I know that we have talked. About previously about the titles that we see here and you can see here
in Mexico this actually has a title that seems to make sense. So one of
the things that I wanted to let the team know is that when these are
coming in from DPLT. What's being stored here in the title field is the location ID. This
particular field though the title, I'm going to open this up, is
actually something that can be changed. You'll see here I actually
renamed this particular one. What the actual name of the location is. So I I put that there versus
location ID and so this is something that can be changed. And Don,
correct me if I'm wrong, do you have any experience with bulk metadata
updates? OK, awesome. So what I just wanted to show is that I understand that
this is not something that could be easily found by like the author
themselves. However, if we were to take a look at the properties, I'm
sorry, not the properties, if we were to take a look at the actual
content fragment.

**Don Middlebrook** 3:01 (Part 1) Yeah, I do. I do.

**Daniela Tea** 3:20 (Part 1) There are a couple fields here that could be appropriate to use instead,
whether it's a property, legal name, location, legal name, long name or
short name, you know, whatever that's decided upon, which would be a
better title for the content fragments. I would recommend that once that's decided, you could apply those
updates so that way the titles are renamed from instead of the location
ID number to whatever that specific field is. So again, this one looks
correct because I had manually titled it this way, but since there's so
many. Any locations that's being stored here. That's why we're recommending
doing a a bulk metadata update for it once you decide on the field.

**Don Middlebrook** 4:03 (Part 1) Right, so go back in and show me what we might be adding.

**Daniela Tea** 4:09 (Part 1) Yeah, sure thing. So I'm trying to find one where the the names aren't
all the same. Um, so let's see if I can find one of those.

**Don Middlebrook** 4:17 (Part 1) Right.

**Daniela Tea** 4:21 (Part 1) OK, this is a bad example 'cause all the names are the same, but maybe
this? No, these are all Hard Rock kind of.

**Don Middlebrook** 4:29 (Part 1) But even if yeah, where would how would I pull that property legal name?

**Daniela Tea** 4:33 (Part 1) So this is a stored value like right now it's read only because these.
So these fields are coming in from DPLT, right? So this value is being
stored as the property legal name like that's that's the name of the
metadata property or something to that extent.

**Don Middlebrook** 4:41 (Part 1) OK. OK.

**Daniela Tea** 4:50 (Part 1) So whether it's this field or this field, this field or this field,
that's really going to be up to to, you know, you guys, whatever it is
that needs to be updated to, you would take that value and then replace
the title with it. If that's and if that's something you know that you might you know
need some help from us, I you know like we can perhaps talk about that
more during like some of the technical knowledge transfer, but if
that's.

**Don Middlebrook** 5:03 (Part 1) OK. Sure. Yeah, let's, let's, let's spend a little time on that 'cause I
just wanna make sure I'm pulling the right and adding the right data.
But yeah.

**Daniela Tea** 5:18 (Part 1) Yeah, no, understood. Sure. OK, awesome. Yeah. So just wanted to make sure the team is aware there
is a way to do it. Of course there needs to be, you know, some thought
as to which field would be the most appropriate one to rename it, but it
doesn't have to be like this. And and certainly Don, once we enable you
on showing how to do the update, then that can be.

**Don Middlebrook** 5:35 (Part 1) Sure.

**Daniela Tea** 5:42 (Part 1) Updated moving forward. All right. OK. So, well, let's take a look at one of these content
fragments and break down some of the fields that we're seeing here. So
I am just right now, I just have this specific one open. I'm from DC
area, so I found one from Washington, DC as mentioned earlier. The fields that are all read only, those are going to be fields that of
course an author cannot change. It's coming in from DPLT, so these are
not something that's editable. However, there is a section of fields
that are going to be editable by the author. And it starts here with these this image field and we're going to be
seeing this image field be used on some of the components, not the. Some
of these content fragrates will not have them because there was nothing
to since it's not coming in from DPLT. And it wasn't something that was necessarily set for like this
particular location. That's why some of these fields are going to be
blank. So image is one of them that's being used for example in in a
component called destinations and venues. So we're going to see another
content fragment which has this filled out and how it will appear in a
component. Component in this section here we also have some dropdowns, type of
destination and type of vacation. These are also things that the author
is going to fill out as necessary since this is a cafe specific content
fragment. Is delivery is something that's only relevant to cafes and you can see
once this is checked it displays this multi field here to add the
delivery partners. In this case Doordash, Postmates, Uber Eats and
Grubhub are going to be associated with this Hard Rock Cafe, Washington
DC. Take a look at the delivery widget. We're going to see how these appear
on there. So Scroll down. There's also another editable field for is
venue and an opportunity to select a venue content fragment. This is
specific to hotels. And it's on the main hotel website I believe where you see a list of
locations and the associated venue with them, meeting space, that sort
of stuff. So if you have a hotel and you have a venue, you would select
the check box and then you would also add the venue content fragment. Reference here so that way it's linked to this location. So in terms of
the is delivery, let's take a look at how this translates to the web
page. I'm just going to go to this other tab here of a live usage of
this. I am on the delivery page on the Cafe Stage website and this is our
delivery widget and you can see here Washington DC is what I selected
and the preferred service here are the four items that were being stored
within that content fragment. DoorDash, Postmates, Uber Eats and Grubhub. So going back to the Hard
Rock Washington, Hard Rock Cafe, Washington DC, you can see if any of
these need to change, whether it's URL, whether it's the order or just
like the name of the service that would be done here within the location
content fragment. For that specific cafe. So this section again is specifically for
displaying it within this component that's on the delivery page and
you're able to see the options that you put here. And then of course
when you hit go, it would take you to that URL. Hey Rick, I see your
hand up. Right. Did you have a question?

Lyon, Rick (Director of Digital Experience)** 9:38 Sorry, I was still muted. I didn't see an option to open the links in a
new window, so I assume that they will all automatically open in new
windows.

**Daniela Tea** 9:39 (Part 1) No problem. Yeah, so these, so you'll see here Uber Eats, I'll click it, go, it
opens up in a new tab, yeah.

Lyon, Rick (Director of Digital Experience)** 9:52 OK, so even like the venue stuff, like anything on that I guess page or
card that you're adding links to. Is it the assumption every link here
just automatically opens in a new window?

**Daniela Tea** 9:56 (Part 1) So. So for this particular section, everything is going to open up a new
window. I I don't think these are ever going. These would never be like
an internal link, right? So I believe that's why it was just baked in.
These are always like 90. Like I can't imagine an instance where this
would be an internal link. So it's it's baked into the component to
automatically.

Lyon, Rick (Director of Digital Experience)** 10:08 Perfect. OK. Mhm. OK.

**Daniela Tea** 10:25 (Part 1) Open up to new tab. You mentioned the venue portion though, so now venue
is something that's different. In this case here I'm referencing a
content fragment and we can take a look at that. Yeah, yes, exactly.
Yep, we can take a look at that shortly.

Lyon, Rick (Director of Digital Experience)** 10:36 And that's that table, the meetings and event table, OK.

**Daniela Tea** 10:42 (Part 1) But before we do that though, any questions though about the is delivery
portion of this content fragment and how it translates to the cafe site?

**Lisa Cardia** 10:53 (Part 1) Just a question from me.

**Daniela Tea** 10:56 (Part 1) Sure.

**Lisa Cardia** 10:57 (Part 1) When a new location's added to the DPLT, this part is delivery only
would be checked if the author manually went in and did it right. Like
we wouldn't. OK, that was my first question and my second one was not
to derail from delivery, but we quickly glanced over the image.

**Daniela Tea** 11:01 (Part 1) Mhm. That is correct, yes.

**Lisa Cardia** 11:15 (Part 1) Section. So we said that that image you you don't have an example of
where that populates yet or we will get to that.

**Daniela Tea** 11:16 (Part 1) Image section, yes. Oh, we'll see that this is, um, we'll see that when we look at the Uh
hotels.

**Lisa Cardia** 11:27 (Part 1) OK, so image is specific to hotels. I just wanna make sure I'm like
writing my notes correctly. OK.

**Daniela Tea** 11:30 (Part 1) Yep, yeah, I will show you. Yeah, let's look at an example. I think, I
think Lisa, sorry, before I cut you off, was there any other questions
related to delivery before? Because I want to jump to hotels so you can
see this portion and then also we can talk about the venue portion too.

**Lisa Cardia** 11:43 (Part 1) Yeah, sorry, I missed that. That was hotel related, so I just wanted to
glance over that.

**Daniela Tea** 11:46 (Part 1) Oh, that's OK. Okay, yeah, perfect. Uh, okay, great.

Lyon, Rick (Director of Digital Experience)** 11:49 OK. I think I'm good. I don't know if anyone else has questions.

**Daniela Tea** 11:53 (Part 1) Yeah, we can always. We'll come back to our location content fragments
as we continue to review this. But since we were talking about some of
these other fields, let's take a look at venues as well as how this
maps to a venue. All right. So I'm going to now jump on over first to show you guys what where the
venue CF comes into play and I'm actually going to view this. OK, yeah,
oops. So I am in. Just to be clear, I'm an author. We can take a look
at this. Um. The ublisher side and I'm just going to put this in my tag here. I'm
going to do find a venue. OK. All right. OK. So here is our destination and venues component.
We'll look at it in author in a second, but so you guys can see what it
looks like on here. These are the different locations that have venues
associated with it. So Lisa, the image that we saw in that field, that's where these images
are coming from. So if we took a look at Hard Rock Hotel Cancun, let me
see if I can pull that up. You'll see this is it. Yeah, Hard Rock Hotel
Cancun. You'll see that this particular picture is associated with it
and that's the picture that's being displayed. Play here.

**Lisa Cardia** 13:19 (Part 1) OK. I think just obviously you're going to know our our question will
be what size for this, but we can move on from that. I'll I'll make
sure it gets written on the Confluence page.

**Daniela Tea** 13:24 (Part 1) Yeah. Yes, sure thing. All right. Um.

Lyon, Rick (Director of Digital Experience)** 13:30 But then you know, does that image also get displayed on the
destinations page?

**Daniela Tea** 13:33 (Part 1) I'm sorry, what was that?

Lyon, Rick (Director of Digital Experience)** 13:34 Does that image also get displayed on the destinations page or is that
strictly for the venues page?

**Daniela Tea** 13:40 (Part 1) So let's take a look at destinations. I believe it is also displaying
destinations. We're using the same component. So in this case here,
keep in mind we are on our stage website. I think this means. So what we
would need to do here is just republish the images. I don't think. I don't know if anyone is actively working on any hotel related things
on stage, but yes, right to your point, those images are also associated
when you view it on this particular page. This is actually the exact
same component as what we we just saw here. It's just a different. A different variation that's selected, but we'll take a look at how
that's being authored. But yes, these images are also being used on
that on that page as well. All right, yeah.

Lyon, Rick (Director of Digital Experience)** 14:24 OK. Thank you.

**Lisa Cardia** 14:28 (Part 1) And I think the reason why maybe the image specs is probably critical
for this is because it doesn't look like we'll have the same
flexibility to adjust like image position and you know height or what
what have you like it's pretty contained which.

**Daniela Tea** 14:43 (Part 1) Yeah.

**Lisa Cardia** 14:44 (Part 1) Honestly, I prefer just as long as we know what the image spec is.

**Daniela Tea** 14:46 (Part 1) OK. Yeah, understood. Let me refresh the author site here so we can take a
look at this component. So this component is called destination,
destination search and filters. As we saw, it's being used on our find
a venue page. It's also being used on that destinations page. But we can take a look at this configuration first, so pull this to the
side to show how this was authored. So one component but different
variations. In this case here you can see I've selected find a venue.
When we go to the destinations page we'll see this one being selected. We have our request for this is the RFP, sorry request for proposal like
here. Right now it's linking it to this request information page and
then we also have our sort by drop down. So you can see everything's
actually selected and it's it's within this. This particular order, so meeting room, Max capacity, total square feet
and number of guest rooms. So when I take a look at the actual page
itself and expand this meeting room, capacity, total square feet and
guest rooms, I think this is actually a better view, so I'm going to. Pull this off to the side. So I want I want you guys to see how this was
authored and how it corresponds to what the end user will see. So bear
with me one second. OK. All right. So let's open this back up. OK. All right. So then we also have our region section. So we have North
America and this is going to show everything that's under the North
America region. In this case, we can see like some of the Mexico ones
are here. We see Atlantic City, Indiana, etcetera, etcetera. This is all
information. Like when we just select region North America, this is like associated
with those specific location content fragments. So as I'm selecting the
different regions, Central America, South America, Caribbean, say OK,
pull in anything that has the venue. And pull anything that is from this specific region and then display it
in that section, right? So let's see here. Then we have Europe, Middle
East, Africa, and then we have Asia Pacific here at the bottom. All
right.

**Lisa Cardia** 17:14 (Part 1) And Daniella, for for those fields, for region and for when you checked
off, I believe it was, let me go back to my notes when you were sorting
by the different, yeah, when you were doing those categories, can we add
to those?

**Daniela Tea** 17:14 (Part 1) So yeah. Mm-hmm. Yes. So these categories are based off of what's being stored in our venue
content frame like these. Sorry. Oh, I'm sorry, I'm sorry, not sort
by. I apologize. You're talking about the regions.

**Lisa Cardia** 17:40 (Part 1) I guess it's two-part question because I would like to know what if we
decided to make a new category to sort by. So we'd like a new field
basically to say what these locations you know can have. Is that hard
coded right now? So I just want to know. If if tomorrow we need not just meeting rooms count, but meeting room
view view, I don't know whatever it ends up being. Can we add to those?
And then is I guess the regions just characterized by the folder
structure? Just trying to better.

**Daniela Tea** 18:00 (Part 1) A. OK. So let's take a look. Yeah, let's take a look at our venue content
fragment. So let's take a look at the content fragment. So in this case
here, I'm going to look at Hard Rock Hotel Cancun, which is associated.

**Lisa Cardia** 18:14 (Part 1) And if we have new.

**Daniela Tea** 18:28 (Part 1) With this specific location, so we have there's a corresponding venue
content fragment that has been associated with this location. Alright,
so let's let's look at it. I'm going to hit edit just to open it up.
So here is all the information that was displayed on here, right? So all
this information is being stored.

**Lisa Cardia** 18:34 (Part 1) Venue content fragment, OK.

**Daniela Tea** 18:48 (Part 1) In a content fragment that looks like this. So you can see here those
were those established fields that we had meeting rooms, Max capacity
area and guest rooms. And so your question about what if we needed an
extra field that would require an update to the content fragment model
since this was the defined data structure for.

**Lisa Cardia** 18:52 (Part 1) OK.

**Daniela Tea** 19:08 (Part 1) This particular content fragment, so you wouldn't be able to just add
it right now to this view. You would have to update the content fragment
model, determine what kind of field you want it to be. Is it a text
field, is it a number field, etc. And then once that's been enabled and
added and published to the model, then you would be able to. See that field here and start storing values for it, but right now.

**Lisa Cardia** 19:31 (Part 1) So if I I guess that would be like if our IT team or product team,
whoever's in charge of editing the fragment models adds it, do they
work in conjunction how that new field also looks on this? Like just so
I can understand like what's going to be our process for we need a new
field and if we can't add it as authors, we need another.

**Daniela Tea** 19:38 (Part 1) Mhm. So this. Mhm.

**Lisa Cardia** 19:50 (Part 1) I know that it might take us a week to get the fragment updated plus the
design of the new field.

**Daniela Tea** 19:56 (Part 1) Right. So um, let's take your example of if you needed to add, let me
see like you said like, I don't know, like view or.

**Lisa Cardia** 20:03 (Part 1) I said like meeting. Yeah, the view of the room, even though I'm just
couldn't think of.

**Daniela Tea** 20:06 (Part 1) Yeah, so say that's a field that you want to add. First step would be
OK is that a number of fields that determine the input field, which of
course like you mentioned, that would be added by whoever has admin
rights to those that content fragment model. The next step would.

**Lisa Cardia** 20:22 (Part 1) Group did take the content fragment model course, so I did see where it
gets added, but obviously I just want to know what that process looks
like for this.

**Daniela Tea** 20:24 (Part 1) Mhm. Yes. Yep, so that specific field needs to get added. This specific sort by
would also need to be sorry this this drop down would need to make sure
that that particular field is added here. However, keep in mind how
would you want it to be displayed here, right? Do you want it to be
displayed in the section in a different part of section? So that would be also a component update. So like there are like you're
saying there are different like decisions that would need to be made.
You add a new field, you need it to be accessible to the author within
the dialogue window, but then also determine where should it go to the
end user which would require a front end update to the component.

**Lisa Cardia** 20:50 (Part 1) Mhm. OK.

**Don Middlebrook** 20:59 (Part 1) OK.

**Lisa Cardia** 21:07 (Part 1) OK. Thank you. Rick can probably speak to how an author does it today, but I
just want to be sure that this group knows if we needed something new,
we're going to need to make it like a process to get that field.

**Daniela Tea** 21:09 (Part 1) Yeah.

**Mayte Eme** 21:20 (Part 1) Can we can we tag this as a as a as a gap please? Because it's way
overcomplicated on how to manage knowing that we're constantly changing
to at least those points. We will need to have a more optimized way of
doing this.

**Lucas Nelson** 21:36 (Part 1) Yeah, go ahead and mark it as a gap, guys. Yeah, it makes sense. If
y'all need this optimized market and document it accordingly. And
Gonzalo has his hand up, Daniel.

**Mayte Eme** 21:37 (Part 1) So we can add up. Thank you.

**Lisa Cardia** 21:45 (Part 1) Oh, yeah. I was gonna say cause but sorry before Gonzalo goes, the probably same
will go to the filter itself. Like I'm I'm assuming the filters also
now hard coded for grabbing these destinations. So it's like if we were
to to classify the type of destination by being a unity participating
hotel, we can't just add it so.

**Mayte Eme** 21:51 (Part 1) Yes.

**Lisa Cardia** 22:03 (Part 1) Same kind of concept, but sorry, Gonzalo, your hand's been up for a
while.

**Mayte Eme** 22:08 (Part 1) Yeah, one, sorry to consult. I'm sorry. One more thing. Luke, I just
want to make sure we're doing the right thing before we could move in.
I assume you guys were like marking the gaps. Are you saying we have to
annotate them? OK.

**Lucas Nelson** 22:18 (Part 1) No, no, Maite, no. We're providing the knowledge transfer and the
information you need to document those. Yep.

**Mayte Eme** 22:23 (Part 1) OK. OK. Thank you for clarifying. So for now on we'll we'll document them.
Thanks.

Gonzalo Calasich (SHRSS)** 22:32 Hey Tim, thank you. Quick question. You were in the component a moment
ago and that you were sharing the regions and this section. So it in
prod I don't see this working the when you select the regions.

**Mayte Eme** 22:32 (Part 1) OK, let's start.

**Daniela Tea** 22:42 (Part 1) Mhm.

Gonzalo Calasich (SHRSS)** 22:47 Uh, and and I'm talking about the hardroad.com one. The the Google Maps
component is.

**Daniela Tea** 22:51 (Part 1) Yes. Yeah, so that's a different. So to be clearer than the one that's a
different component than this one. I like you said, I think it's using
the Google map component which we are going to be going over today on
how that works. But this component here is destination search and
filter. So there are some different functionality and different fields
in the.

Gonzalo Calasich (SHRSS)** 22:59 OK. Got it.

**Daniela Tea** 23:13 (Part 1) Component dialog window.

Gonzalo Calasich (SHRSS)** 23:14 OK. So maybe we can go through those questions when we get that. Thank
you.

**Daniela Tea** 23:17 (Part 1) Yeah, when we go through Google Map, definitely we'll we'll make sure
you have some time to ask that. OK.

**Lisa Cardia** 23:24 (Part 1) Sorry, I am getting a little bit confused Luke, with that statement.
I'm gonna be honest, I was really under the impression that you guys
were also like building out the list and like ours was just more so like
the questions. But if I was under the wrong impression, I think this
team needs to know because we might not be document mean not be
documenting as much. Um.

**Lucas Nelson** 23:44 (Part 1) Yes, Scott, this is kind of what I talked to you offline about. I was
wondering how the process was going for you guys internally documenting
the the gaps that you would come to the platform expansion reviews on
the last two weeks on the calendar. So Scott, if you could take that offline with Lisa.

**Scott Sorel** 24:01 (Part 1) Yeah, I I thought our question, I thought the questions on confluence
were were feeding into that funnel. No.

**Lucas Nelson** 24:07 (Part 1) They're feed into a funnel for you guys to document what you're
finding as gaps and what we're showing in this knowledge transfer. Yep, but but we're we're not documenting your your your gaps. You guys
come prepared with use cases and functionality that's missing from the
framework that we're showing you how to.

**Scott Sorel** 24:15 (Part 1) Right, right.

**Daniela Tea** 24:16 (Part 1) But.

**Lisa Cardia** 24:16 (Part 1) But.

**Scott Sorel** 24:25 (Part 1) Right. And that's what yeah exactly in the in the landing zone for that
is is the questions in confluence like we did in previous sessions
right. Whether it you know what like like with Maite's ask or
anybody's ask them we need more of this or we need we need
clarification on this or you know this is not working for us. You know
like the the questions I think it's also it's questions slash needs. Maybe is a better terminology, Luke, on confluence, right? It's not
just questions, it's also what do we need, right?

**Mayte Eme** 24:46 (Part 1) To be, to be. OK. To be fair, Scott, just to the Adobe team, I don't think they can
easily understand the gaps from the questions because our questions were
more on like how do we do this and can you show us this or that because
these are pretty high level, so we don't get to see all the steps, but.

**Scott Sorel** 25:00 (Part 1) Mhm.

**Mayte Eme** 25:06 (Part 1) That's why I asked earlier if there was another list being done, but
now that I know it's not, I'll catch up, look on the rewatch stuff and
I'll start documenting gaps. That way when this ends, we should have a
list.

**Lucas Nelson** 25:18 (Part 1) OK, that sounds good, my team.

**Lisa Cardia** 25:19 (Part 1) Yeah, to add to that, because I think, remember when we met as like a
high-level group with Leandra and she was like, well, why are you asking
questions if they were asked in the video? So it's I hadn't been
documenting gaps necessarily on the confluence page, just questions. So
to me it feels like a lot.

**Scott Sorel** 25:19 (Part 1) It sounds great, Mikey.

**Lisa Cardia** 25:38 (Part 1) A lot of my gaps from those previous sessions might not be written
because I thought those were at least getting take away from the Adobe
side.

**Mayte Eme** 25:47 (Part 1) OK, so Lisa, once I have my listing, well, I'm going to start, but once
give me next week to catch up, I'll make sure that I'm not missing any
of your gaps and that we are aligned.

**Scott Sorel** 25:54 (Part 1) OK. Well, the good thing is things are recorded and Luke, you've been
posting the A I notes as well, right. So it should be pretty, yeah. So
we can distill from that too. It's not like we we we have missing time.

**Mayte Eme** 25:57 (Part 1) Yep.

**Lucas Nelson** 25:59 (Part 1) Yeah, that's that's correct. The the transcripts. Yep, Yep. Yeah, transcripts and videos, yeah.

**Mayte Eme** 26:06 (Part 1) Yeah, and to be fair, we know what we need, right? So it should be, it
shouldn't be that hard for me to accomplish because we know exactly
what we're missing in most of the cases. From what we're seeing, like
it's it's a lot. So I'll, I'll take on that.

**Scott Sorel** 26:11 (Part 1) OK.

**Lucas Nelson** 26:20 (Part 1) Thanks, Mike. Yeah, I'm glad we got this cleared up then. Thanks, guys.

**Scott Sorel** 26:23 (Part 1) Yeah, 100 S now instead of later. I gotta step away for a minute. I'll be right back.

**Daniela Tea** 26:31 (Part 1) Um, sorry guys. I'm trying to. I'm trying to remember where we were.
Uh, OK, OK, yeah, so.

**Lisa Cardia** 26:38 (Part 1) I I think it was Gonzalo had a question. I'm gonna. I don't know if he
still have a question, but.

**Daniela Tea** 26:42 (Part 1) I think, yeah. OK, yeah. No, thank you. That reminds. OK, yes. So
Gonzalo had asked specifically about the Google Map component, which is
being used on the hardrock.com website under locations. That's a
different component. We'll be covering that. That's in one of my one
of my tabs here. Yeah, here we go, Google Map. So we will take a look at that and any questions that you have, Gonzale,
you can certainly ask them while we're looking at the component. OK,
Yep. All right. So we have here. So, yeah, so this is the how the venue
content fragment is being used. Let's take a look at a live example
here.

**Lisa Cardia** 27:06 (Part 1) Thank you.

**Daniela Tea** 27:19 (Part 1) This venue for Hard Rock Hotel Cancun. Again, you'll see there's no
actual connection to the actual location for Hard Rock Hotel Cancun. The
connection is being made when you add it to the location content
fragment. Meaning, as we saw here, this is that location, content fragment, Harbor
Coast Hall, Cancun. We saw that there's an associated venue or there's
associate, there's venue information associated with this location. And it's being added by attaching a content fragment to this location. So going back to this is the venue content fragment and it has these
fields for meeting rooms, max capacity area and guest rooms which we saw
can be displayed in a certain order through the component configuration.
We also have the short description, additional information and the fact
sheet that information is being. Dislayed here. And then we have, let's see, yeah, so the fact sheet, no. So none of
these are necessarily required, feel like none of these have been made
required. So if like for example, there's no additional information or
if there's no fact sheet that will not, you know, that's not something
that an author needs to.

**Lisa Cardia** 28:26 (Part 1) And and those aren't required fields, all of these, so like if
someone's missing one.

**Daniela Tea** 28:41 (Part 1) To add in order to publish and save this. Yep, alright.

**Lisa Cardia** 28:45 (Part 1) OK. And I could be wrong, but maybe Rick, if you won't answer this, if
you go back to the like options right there on the cards, like so we can
see the additional information, do we ever have more than just two
buttons on the left?

**Daniela Tea** 28:54 (Part 1) Yeah. Do we ever have more than two? Oh, sorry. Is this the right question?
OK, yeah.

**Lisa Cardia** 29:00 (Part 1) I'm I'm I'm asking, yeah. So Rick, I'm I'm just, I'm trying to
understand he has a little bit more background with hotel do we is it
this card or am I confused something else where we've added more more
buttons than just the two?

Lyon, Rick (Director of Digital Experience)** 29:14 It's just the two on this. I don't know if you think about like the
rooms or the eats and drinks venue card on those. Yeah, you have like 5
or 6 menu buttons or something, but on this it's typically just these
two and then that view more link that links to the, I think they're
PDF.

**Lisa Cardia** 29:17 (Part 1) Yeah, that might be what I'm thinking. OK. OK.

**Daniela Tea** 29:29 (Part 1) Mhm.

Lyon, Rick (Director of Digital Experience)** 29:30 So this is kind of just like a high level quick view and if you want to
know everything else, just download the fact sheet.

**Lisa Cardia** 29:33 (Part 1) OK. Okay, thank you.

Lyon, Rick (Director of Digital Experience)** 29:38 Mhm.

**Daniela Tea** 29:42 (Part 1) OK, so this as we mentioned for the destinations and filters component,
this is using that venue find a venue variation, but let's take a look
now at the destination search. Um variation for this O I'm going to. Open UA new tab. Let's see here. Yeah, I'm going to find the example
of. Hotel stage. So under destinations. OK, so let's take a look at this
component here. I'm gonna open up this page and the author so we can
see how that's been configured.

Lyon, Rick (Director of Digital Experience)** 30:28 We can do something with all those countries listed on the left, right
underneath Central and South America.

**Daniela Tea** 30:29 (Part 1) To. Let's let's take a look how we can if we can get that. Sorry, I'm
sorting this out to get to the destinations page. Here we go. All right,
I'm going to click edit.

Lyon, Rick (Director of Digital Experience)** 30:37 Shouldn't that list, yeah.

**Daniela Tea** 30:47 (Part 1) OK, all right. So now as the component is loading, we're going to keep
this here on the left and take a look at this on the right. All right,
so same component, slightly different filters are being displayed due to
the variation that was selected here. Here we have again the regions. This portion here is of course the same
as what you saw for find a venue. However you see the sort by is missing
since that's venue specific and then also. I can't remember what else is on there, but this portion here where you
select regions is going to be exactly the same functionality. So in this
case we have North America specified and then we have the the
description listed. So the country names here is what's being surfaced
under the title. The description is what's being listed here and then the associated
countries are what's being listed here. So right to your point about
how do you clean up these countries, I believe that was an update that
we had made to the Google map component. But it sounds like, you know, of course if if you have specific
countries that you want to show versus anything that is in South America
and Caribbean, you would want that sort of functionality also being
added to this component. So that to me does sound like a gap, but we
will look at how it's done in Google Maps just to confirm that that's
what the expectation essentially like an open. Field I would imagine is what you're looking for to be able to select
certain countries to be listed here. Is that correct?

Lyon, Rick (Director of Digital Experience)** 32:25 Yeah, I think Envisogy is just a manual text field. So we could put, you
know, two countries, we could put 12 countries, but we could also remove
individual countries because like there were a couple of countries that
we were in, but we didn't want to list Russia, China, for example.

**Daniela Tea** 32:28 (Part 1) Mm. Yeah, OK. I see. Yeah. OK.

Lyon, Rick (Director of Digital Experience)** 32:43 I don't know what those locations are now, but so just having that
control was pretty important 'cause I know it came up a couple times.
Hey, can you remove this country?

**Daniela Tea** 32:50 (Part 1) Mhm. OK, Yep. So that that to me sounds like, uh, that's that would be,
yeah, that would be a gap for this specific component. But when we take
a look at Google Map, we'll confirm that that functionality is what
essentially the gap would need to.

Lyon, Rick (Director of Digital Experience)** 32:56 I don't know if that's a gap. All right, that's been. And that would be the same for wherever there's a locator, we want to
be able to control what shows. So if it's on hardrock.com, hotels,
cafes.

**Daniela Tea** 33:09 (Part 1) Um, a su. Mhm. Yeah. Got it. OK, all right. So taking a look now as we see this here. And
again, I can I can take a look at why these images are not displaying.
This is likely either there's no image associated with this or if
something's not necessarily published. But you can see here that the images that we saw previously associated
in this content fragment for the location is being surfaced up in the
destinations as well as the venues here. And I know Lisa, like you
mentioned having the dimensions. For the image that's being displayed is is information that the team
would be looking for. Where did I? Sorry, I was.

**Lisa Cardia** 34:03 (Part 1) Yeah, definitely because I I don't see the option to make this like. I
know like that was the solution with the image position at least, but
since I don't think that has that here, we'll definitely want
baseline.

**Daniela Tea** 34:11 (Part 1) Hello. Yeah. Yeah, understood. And yes, you are correct. The image position is not
available on here since I think like the images would, it wouldn't
really make sense to have that here at a component level in its
entirety. So yes, definitely want to make sure that we can identify what that is.
So the authors can add something appropriate to this field here. OK,
where did it go? Here it is. All right, so let's see. OK, so this component, so we can see what the author looks like. We can
see how it displays. We've identified a gap for the countries that are
listed underneath the the title for each section. Any other questions though about this specific component, the type of
destination and filter by region. This is information again that's
coming in from the content fragment. So type of destination, type of
vacation. In this case this is empty for this specific one for Hard Rock
Cafe if we're to go back to our. Cancun one. These should be filled out by an author to make sure that
it's filterable when if the user were to interact with this here.

**Lisa Cardia** 35:33 (Part 1) I do have a question. Given that cafes, you know, are going to need the
knowledge base to access their own fragment model if they have something
that they need on their page, what if they were to accidentally fill out
anything for like hotel because?

**Daniela Tea** 35:35 (Part 1) Mhm.

**Lisa Cardia** 35:49 (Part 1) You know some cafes are at those hotels, so what if someone just gets
confused? Are they going to now accidentally show show here? Like does
this get impacted by any author in their content fragment model if I
like am a cafe website manager, but then I put. You know, I don't know something one of the the fields that are for
hotel only.

**Daniela Tea** 36:15 (Part 1) Um, so your question, let's see here. So I know.

Lyon, Rick (Director of Digital Experience)** 36:17 I get the menu, they check yes, but it's a cafe.

**Lisa Cardia** 36:19 (Part 1) Yeah, exactly. So like what if they're like, oh, we're we are a venue
because they got confused and they also put their capacity for their
maybe their cafe can be used for meeting. I don't know. I just, I'm
saying worst case scenario, is it gonna impact our hotel pages, those
fields?

**Daniela Tea** 36:25 (Part 1) Mm. Um. Right. Understood. Yeah, no, understand, especially with all the fields.
So one thing that I do know is I believe we are looking at the line of
business, you know, as because that's not, this is not something like
you can't just say, oh, only get me cafes or only get me hotels here.
So my understanding. As we are looking at the line of business, I will check with our dev
team to ensure that these specific components you know like. So if I
were to add something here, this should you know this uneditable field
should prevent that. But I will check with the team just to confirm that
because I understand. Yeah, I definitely understand that. Like you wouldn't want this cafe to
appear on this page, but I will.

**Lisa Cardia** 37:17 (Part 1) I meant for like the editable, the editable fields, obviously.

**Daniela Tea** 37:20 (Part 1) Well that what I'm saying is that if the editable field here is saying
cafe, even if you fill out this information, I do believe that that
should not have an effect on this, but that's what I'm going to check
with the dev team to see how that was coded up.

**Lisa Cardia** 37:34 (Part 1) Because the reason I ask is we've we've seen not cafe locations under
the is delivery meaning someone went in to a hotel location and selected
is delivery so then they appear on cafe. So it's like we may run into
that.

**Daniela Tea** 37:49 (Part 1) Yeah, yeah, definitely. We'll want to check. I will be checking with
the team tomorrow just to get a better understanding of how these
components will display certain information that's not related to their
line of business. And so we'll check in on that one, Lisa. Hey. All right.

Lyon, Rick (Director of Digital Experience)** 38:08 Danielle, on this page that we're looking at the the HTML version, is
that just like a a test page that you made or is that like the actual?
OK, that is the actual page. Can we see what this looks like like a
preview, view preview, view of published, whatever it is?

**Daniela Tea** 38:10 (Part 1) Yes. Yes, you can view as published, but this is also something that's. So
if you were to go to the publisher, this is what it would look like.
Keep in mind, I think that these probably don't have images associated
with that, so that would be something that an author would have to add.

Lyon, Rick (Director of Digital Experience)** 38:33 Right. OK, the only reason I ask is you have the the accordions aren't the
same length or width, and then there's white underneath each accordion
instead of the Gray background. So I'm just looks like there's some
unfinished styling padding on the above purple section.

**Daniela Tea** 38:43 (Part 1) Yeah, yeah. Right. So I think, yeah, so you can see this page has not been touched
for quite some time. So I I don't think, I don't think that we have
made any changes to this, but obviously like to your point, Rick,
there's this would be something that would certainly want to be
reviewed prior to.

Lyon, Rick (Director of Digital Experience)** 38:51 Um.

**Daniela Tea** 39:09 (Part 1) Doing any actual publishing to an actual website, but no one has touched
this page in quite a few months, so just be clear on that.

Lyon, Rick (Director of Digital Experience)** 39:12 Um.

**Lisa Cardia** 39:18 (Part 1) I think we'll want to report it, Rick. Yeah, because, well, the reason
I think we need to report it is because hotels was technically already
handed off. So to our understanding, there's no no other work being
done from that handoff until until the gap.

Lyon, Rick (Director of Digital Experience)** 39:18 OK, so it's gonna be touched. Yeah, OK.

**Daniela Tea** 39:26 (Part 1) Mhm.

Lyon, Rick (Director of Digital Experience)** 39:28 Oh, fine. OK, who reviewed before that was handed off?

**Lisa Cardia** 39:34 (Part 1) No, I mean, we paused that. It didn't make it to the content team or
past Angelica. But what I'm saying is Adobe's not working on these
components, so it just needs to be documented.

Lyon, Rick (Director of Digital Experience)** 39:39 Oh. So we find issues with them.

**Lisa Cardia** 39:47 (Part 1) Yes.

Lyon, Rick (Director of Digital Experience)** 39:48 We're OK. There's no review process before they're handed off.

**Lisa Cardia** 39:54 (Part 1) This will be part part of our like gap analysis, part of our gap
analysis.

Lyon, Rick (Director of Digital Experience)** 39:58 Gotcha. OK. I'm surprised it wasn't reviewed by somebody, OK.

**Daniela Tea** 40:08 (Part 1) OK, let's see here. All right, so venues, the destination and
destination search and filters component. So we understand how this
works and how that's. Author and lives on this page. Let's take a look now at. Cafe stuff. OK, let me see what else I have open here. All right, let's
take a look now at some hotel specific items, starting with the booking
widgets. And I did want to mention that I believe before the pause there
was discussion about the. Different booking engines. However, of course, since we were paused,
changes had not been made to the component. So what I'm going to show
you today is what the component is in its current state, but I do
remember prior to the pause, I believe sometime last year. There was quite a few meetings about booking engines and and that sort
of things with the with the need to add certain other ones in addition
to say Synexus and I can't remember the name of the other ones, but
that is not in place right now, so just want to make sure that's
clear. OK, so with this booking widget component, what we're taking a look at
now is at the very top of our hotel pages, clicking on book now. And
because I am viewing and publish, this is actually, I'm sorry, I was
being in preview. Let's look at this view of publish. Look now. OK, so
this. Specific component booking widget is being used in two locations for
most hotels. You're going to see it here at the top in the Book Now
button and then also on the main page for the hotel. I will take a look
at this in. Alright, yeah, so taking a look at this on the publisher side, you'll
also see here's the book. Now the booking widget, except it's laid out
slightly differently to control that. It's a style variation between
pop-up and default. Default will have that horizontal view and pop-up
displays it. Like this, since the intention is to use it within a Moodle. So what's
being shown here when you click book now and you see this. Right now
this is being authored within an experience fragment. I'm taking a look
at the Riviera Maya. Experience fragment, Book now experience fragment. And so this has a one
booking widget component in it with some configuration. I see your hand
up, Rick. Go ahead and ask your question.

Lyon, Rick (Director of Digital Experience)** 42:52 No, I I didn't wanna wait or interrupt you as you're doing the
functionality. I just had a comment on the other view, but I don't
wanna stop your functionality.

**Daniela Tea** 43:00 (Part 1) OK. All right, sure thing. Um, Carrie, I think your hand's up.

Kerry Holyoak (SHRSS)** 43:10 Can you hear me now?

**Daniela Tea** 43:11 (Part 1) Yes, there we go.

Kerry Holyoak (SHRSS)** 43:13 Thank you. Um, this book now button today fires event 67. How do we
ensure that that continuity is maintained?

**Daniela Tea** 43:28 (Part 1) I, let's see.

Kerry Holyoak (SHRSS)** 43:32 Is that something that happens at the developer level or is that
something that happens in this configuration of the the module itself?

**Daniela Tea** 43:39 (Part 1) Someone, I believe it. Hey, Andy, are you?

**Lucas Nelson** 43:42 (Part 1) Andy might have to help with that. Andy, can you perk your ears? And
Kerry, you might have to restate it.

Kerry Holyoak (SHRSS)** 43:45 OK.

**Daniela Tea** 43:45 (Part 1) Yeah.

43:46 Yeah, what's the question?

Kerry Holyoak (SHRSS)** 43:47 Well, we can take it offline. We can take the analytics discussions
offline, but I just want to make sure that we're aware that this
specific component, wherever it's used, should be firing event 67 on
that book. Now for the first time it's clicked in a session, and if
it's clicked more than once in a session, every subsequent time it
fires events. 68 and that's the current implementation today. So we want to make sure
we maintain that that tracking.

**Andy Lambert** 44:14 (Part 1) Thanks, Carrie. Yeah, definitely track it and we'll take a look into it
and and circle back with it.

Kerry Holyoak (SHRSS)** 44:16 Sure. Excellent. Thank you.

**Andy Lambert** 44:21 (Part 1) Yeah.

**Daniela Tea** 44:23 (Part 1) Alright, OK, so looking at the configuration for the booking widget
component and I'm actually going to go to the Riviera. OK, yeah, let's go to this page so we can see the exact oops. OK, alright, so I'm clicking book now. Alright, so for starters you may
wonder, OK, why is the experience fragment showing the button in this
color but on the actual site is showing different color. This is because
when you are in experience fragments. It's not going to show the theme, the theme for your site because the
themes are being set at the site level. So when you see it like this and
you see it differently on this, the the only difference is just that the
theme colors have now been applied at the site level. All right, OK, so configuration wise for this one.

Kerry Holyoak (SHRSS)** 45:17 Sorry, real quick, one other question. So we have a target activity
running on the book now button on the sites where it's green and it
says check availability. How do we well this might be a separate
conversation for another time, but I just want to raise the issue that.

**Daniela Tea** 45:19 (Part 1) Sure.

Kerry Holyoak (SHRSS)** 45:36 If we were to make that change, if we're running an AB test on this
module, do we run it on this experience fragment or do we set it up some
other way?

**Daniela Tea** 45:50 (Part 1) So Kerry, correct me if I'm wrong. You're saying that this basically
you're running target to change this when the page loads. So instead of
saying book now it would say check availability.

Kerry Holyoak (SHRSS)** 46:01 And it's a color green, yes, that's correct.

**Daniela Tea** 46:03 (Part 1) It's color green. So I think in terms of the target activity you're
asking, would you be taking this experience fragment and setting the AB
test in the experience fragment versus page? OK.

Kerry Holyoak (SHRSS)** 46:15 Yes, versus the way we're doing it today on Sitecore, yeah.

**Daniela Tea** 46:20 (Part 1) And in site core is the the buttons on at the page level.

**Andy Lambert** 46:24 (Part 1) Yeah, that's OK.

**Mayte Eme** 46:25 (Part 1) Actually, visually, that's a visually.

**Daniela Tea** 46:25 (Part 1) Oh, um.

Kerry Holyoak (SHRSS)** 46:26 Oh, sorry, visorgy. Yeah. Uh. I mean, is it at the page level? I don't that's Rick, is it at the
page level? I mean, I feel like it's a module that that drops down.

**Mayte Eme** 46:40 (Part 1) It's a it's global on pages.

Kerry Holyoak (SHRSS)** 46:43 Yeah.

**Daniela Tea** 46:43 (Part 1) It's global across all pages. OK, so with hang on, I'm going to just
pull up. Oh, hang on. Oh, one second, guys. My computer seems to have frozen.

Kerry Holyoak (SHRSS)** 47:01 And I don't want to take us off track for the training of the module
itself. I just want to be aware of where do we go to run a B test. So
maybe we can do target activities as a separate training session just in
general.

**Daniela Tea** 47:14 (Part 1) Oh yeah, I think, yeah.

**Lucas Nelson** 47:15 (Part 1) We'll take that offline, Carrie. We we we don't have a target resource
as part of this KT. We had it explicitly out. You know, I hate to be the
scope guy, but I always am it. Yeah, so. So I'll take it offline that
there's some further target questions that you're having as a result
from these KT sessions that we can see.

Kerry Holyoak (SHRSS)** 47:18 OK. OK. No, that's fine.

**Lucas Nelson** 47:35 (Part 1) we can do, okay?

Kerry Holyoak (SHRSS)** 47:35 Yeah, and and I know how to set up the test. I just need to know if I'm
targeting an experience fragment or or some other component. That's
all. It's a basic question. Thank you.

**Lucas Nelson** 47:44 (Part 1) OK, got it. Yeah. And and Andy, take that down technically. I know, I
know you, you go through these as well for notes and then we can have an
internal follow up to see what we can do for Carrie. OK.

**Andy Lambert** 47:55 (Part 1) Got it.

**Lucas Nelson** 47:57 (Part 1) All right. Thanks, Carrie.

**Daniela Tea** 47:59 (Part 1) OK, OK, so my computer has frozen just this browser. So if you guys can
give me one second, I'm going to try to relaunch Google Chrome. Sorry
about that guys. One second please. OK, I am still having some issues with this. I might need to restart my
computer. Uh. Computer. Uh. Luke, can you if you want to pause the recording for right now because I
think I need I think I need a restart. I wouldn't want to have like 5
minutes of dead air on here so.

**Lucas Nelson** 49:07 (Part 1) OK, yeah, no problem. I'll stop the recording real quick. All right, no
problem.

**Daniela Tea** 49:08 (Part 1) Thanks. I'll be right back guys. Thank you.

**Lucas Nelson** stopped transcription

**SHRSS Adobe Knowledge Transfer-20260223_135724-Meeting Recording --PART 2**

February 23, 2026, 6:57PM

10m 37s

0:07 (Part 2) Alright, we're back up.

**Lucas Nelson** 0:10 (Part 2) And Daniella, if you have issues with whatever system updates happening,
you know, if you have to, if it drops you quickly, I'll, I'll screen
it and we'll have to pick these back up, OK.

**Daniela Tea** 0:21 (Part 2) Yeah. Yeah, yeah, got it. Hopefully my computer doesn't just restart. But
yeah, if so guys, just FYI, if I just disappear, it's because my
computer restarted. But well, hopefully that won't happen. OK, let's
resume. I'm going to go ahead and share my screen again.

**Lucas Nelson** 0:25 (Part 2) All right. Thank you. Yeah.

**Daniela Tea** 0:38 (Part 2) And let's pick back up. We were talking about the booking widgets.
Carrie had some questions about things that we will hopefully be able to
address with a target resource if possible. Um, but going back to our experience fragments.

Lyon, Rick (Director of Digital Experience)** 0:59 So, so before you get started, this is probably a good time to ask ask
my question or just speak. If you can go back a tab or two to the to the
main UI widget, no on the homepage.

**Daniela Tea** 1:00 (Part 2) Yeah. Check. Here. Uh, so the homepage like the hotel homepage?

Lyon, Rick (Director of Digital Experience)** 1:17 Yeah, you had it open in one of your tabs.

**Daniela Tea** 1:18 (Part 2) Yeah.

Lyon, Rick (Director of Digital Experience)** 1:21 So the the booking widget looks a little like not long enough or wide
enough and then then all the lines are like on different levels. So is
that something that we can get adjusted or are we going live with all
those lines and book now buttons all just everywhere?

**Daniela Tea** 1:39 (Part 2) So I think like I think this is the kind of things that we would want to
make sure is covered in the gap analysis. So just to be clear, Rick,
like you know things like this, you know or if there's like
functionality that we know should be added to the booking widget such as
the booking. Engines functionality I was mentioning that's stuff that needs to be
covered in the gap analysis. So as long as you write that down and we
can review it during the gap analysis portion.

Lyon, Rick (Director of Digital Experience)** 2:09 OK. Thank you.

**Daniela Tea** 2:10 (Part 2) Yep. K. Oh, yeah, I see. OK. I was like, I see your head back up. Another
question. OK, looks like we're OK.

**Lucas Nelson** 2:17 (Part 2) No, he was giving you a high five, Danielle. Are you good?

**Daniela Tea** 2:19 (Part 2) Oh, got it. Thank you. All right. OK, so let's go back to. I think I
had to. Yeah, I had to get out of that tab. I'm going to open back up
the experience fragment for Riviera Maya. So to be clear, these booking
widgets are added to. To the header. Um. The header of each individual website and the reason being is that they
each have individual URL links that they would go to. In this case here
for we were looking at Riviera Maya back up. I'm going to click on
Hotel Riviera Maya and then EN and you'll see here here's the header. And then here's the book now. So opening up book now, I'll see what it
looks like when you click on the book now button. Going back here, I'm
going to go to the header. I'm going to take a look at the header
experience fragments. We've seen these before. Um, but the way that this has been added. Here in the crown CTA location, I Scroll down and I see book now that's
so this is the actual button itself and then you'll see it's pointing
to that experience drive that I have open in this tab and it's going to
open it. Up in a modal, so that's how this is authored. So the book now modal is
separate, but separate from the header, but it's referenced in the
header by adding it to the Crown CTA component. Let's cancel this and I'm going to close all this tab. So now I'm
focusing on our book now widget. I'm going to click on edit. And take a look here. So this specific component as we saw, it's being
used on the main hotel site, but then also each individual property. So
you'll see group name here. It says North America. Reason why is
because again, this is the shared component. So that is listed in the dropdown. If we take a look at the main hotel
website and and and then. Now. OK, sorry, it's loading if we were to take a look at. If we were to take a look at the main main website, you'll see that the
book. Like I might be going through a restart right now.

**Andy Lambert** 5:06 (Part 2) Yeah, you cut out audio wise there for a second.

**Lucas Nelson** 5:07 (Part 2) Yeah, I noticed you cut out too. Do we need to? Do we need to postpone Daniela?

**Daniela Tea** 5:16 (Part 2) Um, can you hear me?

**Lucas Nelson** 5:18 (Part 2) Yeah, I hear you. Can you hear us?

**Andy Lambert** 5:18 (Part 2) Yeah.

**Daniela Tea** 5:19 (Part 2) OK, yeah, I hear you. I just. I don't know what's we might need to,
because I don't want this to persist. Um.

**Lucas Nelson** 5:26 (Part 2) Yeah, a lot of people on the call, right?

**Daniela Tea** 5:28 (Part 2) Yeah, understood. So I think what we can do is let's, let's, let's
pick this up tomorrow. What we'll cover is the booking widgets. I want
to make sure we cover the Google map. So that way Gonzalez has a chance
to ask his questions. And I unfortunately, I can't pull up the agenda right now, but anything
else that we have not talked about, we'll make sure that we cover
during the first half of the session tomorrow and then just kind of
continue with our next agenda, which I can connect with you, Luke. About so we can send it out to the team.

**Lucas Nelson** 6:03 (Part 2) And we can tailor the agenda from what you know you you you were
planning on tomorrow plus the remaining stuff we need here. Yeah, I
think it's it's probably better anyway because Lisa had the drop I see
and I she's key for these discussions. So yeah, all right, sounds good.
I'll send the recording and transcriptions out and then we'll send the
agendas out for the.

**Daniela Tea** 6:13 (Part 2) OK, OK.

**Lucas Nelson** 6:21 (Part 2) At least tomorrow's session with the tailored agenda. Alright, thanks
guys.

**Daniela Tea** 6:25 (Part 2) In. Sorry about that, everyone. Thank you, everyone. Goodbye.

**Lucas Nelson** 6:27 (Part 2) No, it's all it's all good. Alright, bye. You.

Gonzalo Calasich (SHRSS)** 6:32 Thank you. Bye.

**Lucas Nelson** 10:07 (Part 2) Angelica, are you on this call right now? Yeah, yeah, we we we had to end it. Yeah. Oh, no problem.

---

## Customer Follow Up Questions

| Session                       | Question                                                     | Date Asked | Asked By   | Answer | Answered On | Answered By | Status   |
| ----------------------------- | ------------------------------------------------------------ | ---------- | ---------- | ------ | ----------- | ----------- | -------- |
| Jobs                          | Are all job-related components  production-ready, or are any still considered MVP or interim solutions? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Are configuration options  role-based (author vs. admin)?    |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Are default search behaviors  configurable (e.g., location-first, keyword-first)? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Are filters driven dynamically  from Workday data or statically configured? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Based on demo, seems we can use  job components on other sites. is that correct? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Can category ordering and  visibility be controlled by content authors? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Can hot jobs be scheduled like  in sitecore (using promo cards) |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Can I choose which categories  are displayed in category cards? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Can the page template used to  build this site support additional content blocks below or between? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Can we default the Search Page  path to the existing search page so authors don’t have to select it every  time? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Has load testing been done at  scale?                        |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | How are image cropping, scaling,  and focal points controlled to prevent distortion? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | How does search behave with no  results or partial matches?  |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | How does the Job Listing Card  component handle incomplete or missing data? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | How is search relevance and  ranking determined?             |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | How will property/location data  and images be fully mapped and maintained in AEM for Careers? ETR? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Is the layout responsive and  optimized for all breakpoints (desktop, tablet, mobile)? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | What are the user roles created  for this website?           |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | What data is sent to the data  layer on job click?           |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | What happens if a  category/location/property/type has no jobs in filters? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | What image renditions are  generated, and are aspect ratios enforced |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | What is the element ID or  tracking event for job card clicks? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | What is the finalized DAM folder  structure for job-related images? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | When we create a page (any  template) does it inherit header/footer? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | When will image issues be  addressed and resolved?           |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | When will the style  inconsistencies compared to the current site be addressed? |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Who has access to configuration  pages for job components?   |            | @Mayte Eme |        |             |             | deferred |
| Jobs                          | Are filters interdependent?                                  |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Can Awards be scheduled (go live  on a specific date and automatically expire)? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Can Product configure sorting,  filtering, or query logic for Hiring Events (e.g., upcoming first, region  filter)? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Do hiring events and job fairs  automatically show and drop off based on start/end date/time? Is timezone  respected per property? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Do Hot Jobs automatically drop  off based on end date/time? Is timezone respected per property? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Does filter state persist across  navigation?                |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Does the Job Card support  personalization rules (e.g., geo-targeted jobs)? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | For Job Portal Url, Is this URL  automatically assigned as the default CTA link on job listing cards? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | How are dynamic queries built to  reuse components across pages? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | How are long job titles  truncated — CSS only or server-side logic? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | If “Is API Data” is unchecked  that’s the next sync checks it? Assume not but would like confirmation |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | If DPLT updates a property, does  it automatically update both Brand and Careers? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Is there a custom 404 for  expired jobs?                     |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Is there built-in logic to  maintain equal row heights across dynamic content? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Is there version history for job  overrides?                 |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Need to get a walk us through a  live authoring example of creating a Hiring Event from start to publish and  scheduled drop off. including feeds/queries on other pages/sites. |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | The address from API, where is  that used?                   |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | The Inclusion page uses shared  components—how are those configured? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | To help us provide accurate  feedback, can you please include direct links to each component reviewed  during these sessions so we can easily reference them afterward? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Told tags are internal metadata  to categorize content but can they be used to query content? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | We understand LD JSON is not  used but why is it there and what does it do if used? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | What does a Hiring Event detail  page template look like?    |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | What does type do?                                           |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | What happens if a job detail  page URL exists but job no longer exists in Workday? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | What templates are used for  returning applicants, team members? |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Where are the filters for hot  jobs listing page?            |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Where is Job Zip Code used?                                  |            | @Mayte Eme |        |             |             | Pending  |
| Jobs                          | Why are logos the same height as  navigation links? Is that intentional from a design system perspective? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | What fields in the card and detail page are managed by status values? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we schedule events to  automatically publish and unpublish based on start and end date/time without  manual intervention? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we ensure events  automatically drop off the Event Calendar after the end date/time without  requiring manual unpublishing? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we configure property-level  timezones so event times always display in the venue’s local timezone instead  of the user’s browser timezone? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we restrict Location Reference selections by user role or property  access to prevent cross-property publishing errors? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure custom tags (ex:  “Dinner & Show,” “21+,” “Free Event”) beyond predefined categories and  use them for filtering/display? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we dynamically query and  display events in other components (carousel, grid, homepage modules) outside  of the Event Calendar component? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we build event listings using  queries (tags/metadata) instead of a single folder path, especially for  cross-LOB “featured events” scenarios? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we exclude specific categories or tags when pulling events into a  listing component? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we control sorting behavior when two events share identical start  dates and times? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we manually reorder featured events within the same month beyond  the default “Featured” checkbox logic? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we temporarily hide an event without fully unpublishing the  Content Fragment? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we customize Event Detail Page layouts per property instead of  using one global template? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we add structured modules to  the Event Detail Page (ex: venue info, parking, FAQs, disclaimers) without  embedding everything in the Description field? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we preview Event Detail pages in author mode without publishing to  Stage or Production? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure ticket prices?                           |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we preview Event Listing page in author mode without publishing to  Stage or Production? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure recurring events (weekly, monthly) without creating  separate Content Fragments for each occurrence? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do I group events?                                       |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we conditionally display different CTAs (Buy Tickets, RSVP, Learn  More) based on event type or status? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we manage event-specific SEO fields (Meta Title, Meta Description,  Open Graph, Schema Event markup)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we display venue name separately from full address instead of  relying solely on the Location Reference field? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we add structured compliance disclaimers (ex: 21+, ID required) as  dedicated fields instead of manual RTE content? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we duplicate or clone events efficiently for repeat use cases? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we report on which Event Content Fragments are live, unpublished,  expired, or scheduled? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prioritize certain events globally (pinning logic) beyond  chronological sorting? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we integrate event status dynamically with ticketing systems? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure different event card layout variations (horizontal,  vertical, large hero, compact)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure default filters for specific properties (ex: default  to “Concerts” category)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure the filters: venues, categories, date presets and  custom date range, properties? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we query events to be displayed within site in other pages? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we query events from multiple sites or all sites to be displayed  in other site? (i.e. entertainment site) |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure event lifecycle  states (Announcement/Presale/On-Sale/Post-Event/Cancelled/Rescheduled) so the  badge, CTA, and messaging change automatically without manual republish? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we define the timing rules  for each state (announce time, presale window, on-sale time) so transitions  execute at the exact moment and are logged for audit? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we handle multi-date events  (one event with multiple showtimes) so cards/detail pages display correctly  and listings sort predictably? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we support multi-venue events (touring performer) without  duplicating content fragments or losing consistency? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we ensure cross-site event  reuse renders with the consuming site’s format while still showing the  correct timezone label? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we ensure scheduling works for reused content across sites  (schedule once, updates everywhere it is displayed)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent layout breakage  when scheduled items expire (collapse module or show fallback message, keep  row styling patterns intact)? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we standardize the tagging taxonomy so filtering logic works (and  isn’t ad-hoc per site/component)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we support “badge/bubble  text” on event cards (e.g., “21+”, “Free”, “Phone-free”), including cases  where properties intentionally leave it blank today (often using   )—without forcing awkward author workarounds? (aligns to lifecycle + UI  rules) | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we preview “future state” scheduled content (e.g., “what the page  will look like when presale starts”) ? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we guarantee event updates reflect within an acceptable caching  window on Stage/Prod (and what is the target SLA)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we ensure dynamic queries stay performant (e.g., 200ms server-side  target) as events scale across properties? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent expired events from appearing in search results,  filtered grids, and cross-promotional components? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we support soft-deactivation (temporarily hide from UI but retain  data and URL)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we restore an archived or expired event without rebuilding the  Content Fragment? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure dynamic filtering logic that adapts based on  available content (only show filters that apply)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we exclude certain categories from filters while still allowing  them to display in grids? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent filter pollution when incorrect Location References are  selected? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we support conditional display rules for badges?      |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we control display limits (e.g., show only 3 upcoming events)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we control fallback behavior if no events match the query? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure search indexing rules for events?        |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure canonical URLs for event detail pages?   |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do event cards adapt across breakpoints (mobile, tablet, desktop)?  (they looked weird in the demo) |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent layout shift when images are missing or delayed? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we enforce max character limits on titles to protect grid layout? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we implement friendly name display instead of numeric Location  IDs? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent authors from publishing events without required  governance fields? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we validate that required lifecycle dates are logically sequenced? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we implement role-based author permissions per property? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure the number of  event cards per row per breakpoint (desktop, tablet, mobile), and is this  configurable per page template? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do orphaned cards behave in the  final row (e.g., 1–2 cards when layout is set to 3 per row)? Can alignment be  configured (left, centered, stretched)? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | How do we control card height consistency when titles, statuses, or  metadata vary in length? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How does the Smart Event Grid determine priority when multiple events are  marked Featured? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we define maximum events displayed before pagination or load-more  is triggered? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure pagination vs. “Load More” vs. infinite scroll for  event listings? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How does pagination behave when filters are applied — does it reset,  persist, or re-query dynamically? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Are filtered results URL-driven (query parameters) to support sharable  filtered views? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure on-page search scope for events — title only,  description, venue, tags, status? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How does the Events Filter component support multi-select filters (e.g.,  Venue + Category + Date Range)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How are filter states handled in browser history (back button behavior)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent empty filter states (no results) from degrading UX? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How does filtering interact with event lifecycle (Announced, On Sale,  Sold Out)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Is there version history specific to Content Fragments for event  rollback? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we prevent properties from editing enterprise-managed events? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How are Event Detail Pages structured for SEO (schema markup: Event,  Venue, Offer)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Is sitemap updated instantly upon event publish/unpublish?   |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we aggregate events from multiple properties without duplicating  CFs? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Should Events remain a Content  Fragment model, or should they be modeled using Experience Fragments or a  hybrid architecture for cross-site rendering control? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | What is the recommended AEM pattern  for separating “event data” from “event presentation” to avoid template  duplication across properties? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | Does AEM support inheritance or  composition patterns for Content Fragments to allow enterprise-managed fields  and property-managed overrides? | @Mayte Eme |            |        |             | Pending     |          |
| Events                        | What is Adobe’s recommended modeling approach for multi-venue or touring  events to prevent duplication? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Can filtering logic be centrally managed or does each component require  independent configuration? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Can a single Content Fragment be rendered across multiple site themes  without duplication? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Does AEM automatically generate structured data for Event schema, or must  it be custom implemented? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Are any fields hardcoded in component logic but not exposed in the CF  model |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Which fields are display-only vs logic-driving (e.g., status, badges,  visibility)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Can fields be conditionally required based on event type?    |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Does a new property automatically inherit tag taxonomy?      |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | What breaks if a property is added but event configuration is incomplete? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Are renditions automatically generated per event component use? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | What happens if an asset is deleted or moved?                |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure the default fallback image per site per event type? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Which CF fields map to which component elements (card, detail, calendar)? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Does the card and detail page share the same image source?   |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How do we configure the mobile image?                        |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Where is the master event taxonomy managed?                  |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Are tags property-specific or global?                        |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | How are retired tags handled in existing events?             |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Does template enforce accessibility standards? (noticed a few issues) |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Does URL generation follow naming convention rules?          |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Can URL be edited after creation without breaking references? |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Is there version rollback at page level?                     |            | @Mayte Eme |        |             |             | Pending  |
| Events                        | Need to demonstrate cross-property/site reuse                |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Are accessibility controls (captions, ARIA labels) supported? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Are all fields translatable, or are some hard-coded?         |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Are field values dynamically inherited or copied per language? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Can alignment rules differ per breakpoint?                   |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Can location-based components fall back to manual text if DPLT record is  missing? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Can multiple templates render the same Promotion Fragment?   |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Can Promotion Content Fragments be  decoupled from Casino-specific fields (e.g., Loyalty, Slot) if reused for  non-casino use cases like Hiring Events? | @Mayte Eme |            |        |             | Pending     |          |
| Careers                       | Can promotions be syndicated across sites dynamically?       |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Do translations require full manual duplication of every field? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Does Hide remove components server-side or apply client-side CSS only? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Has load testing been performed?                             |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How are autoplay, mute, and looping governed at component level and  browser policy level? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How are Promotion Fragments translated?                      |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How are responsive renditions generated — Dynamic Media, Adaptive Image  Servlet, or static crops? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we allow authors to toggle between carousel and grid layouts at  component level? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we configure an SEO-safe, UX-optimized empty-state behavior when  no results match filters? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we configure compound Query Builder logic (path + tag + metadata)  for precise Promotion retrieval? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we configure fallback thumbnail behavior if video fails to load? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we configure site-specific filter sets while reusing a global  Promotions component? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we eliminate manual breakpoint resizing through template-level  grid policies? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we enable author-controlled filter display order without requiring  code changes? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we enable controlled extensibility of Promotion Detail pages  without breaking structure? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we exclude specific CFs from query results without restructuring  the DAM hierarchy? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we implement mobile-specific image overrides for Promotions? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we implement start/end lifecycle logic for Promotion visibility  beyond page activation? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we implement workflow-driven Promotion states (Active, Expired,  Archived)? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we improve author experience by enabling searchable CF references  instead of manual ID entry? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we leverage metadata-driven queries instead of hard-coded ID  references? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we structure taxonomy governance so new tags automatically surface  in filter UI across sites? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we support layout variation per Promotion while maintaining  template governance? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How do we suppress specific filter values in the UI while retaining  underlying metadata for governance? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How does AEM handle deduplication when querying overlapping CF paths? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How does AEM validate Promotion ID uniqueness at repository level? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How does Promotion status impact Query Builder results and direct ID  rendering? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How is focal point behavior managed across responsive breakpoints? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How is http://Schema.org structured data applied to Promotion Detail  pages for SEO compliance? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How is lazy loading implemented to support Core Web Vitals performance? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How is Promotion ID uniqueness scoped — globally across AEM or per site  root? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | How is responsive video behavior governed across breakpoints? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | If a CF Model is modified (field added/removed), What happens to existing  fragments? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | If cards wrap unevenly across breakpoints, how is visual balance handled? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | if DPLT updates, does that update cascade to all components referencing  it automatically? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Is there a global grid system policy that can enforce consistent column  behavior across components? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Is there a library of icons?                                 |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Is there a Promotion Detail Page  template planned, or are all promotion detail pages expected to be manually  created using the Open Page template? | @Mayte Eme |            |        |             | Pending     |          |
| Careers                       | Is there version control / rollback for CF Model edits?      |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Should Hiring Events truly be  modeled as Promotions long-term, or should Events CF be enhanced instead?  Seems promotions requires even more manual steps than events CF. | @Mayte Eme |            |        |             | Pending     |          |
| Careers                       | What architectural difference causes carousel cards to auto-adjust while  standalone cards do not? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What architecture prevents ongoing 1:1 maintenance overhead for Promotion  references? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What formats are accepted for icons?                         |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What global responsive grid policies exist at template level? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the architectural limitation of External URL mode versus  structured 3rd Party integration? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the architectural reason for  requiring a manually entered Promotion ID, and how do we eliminate manual  dependency? | @Mayte Eme |            |        |             | Pending     |          |
| Careers                       | What is the caching strategy (Dispatcher/CDN) for Promotion listing  queries? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the dependency impact if a referenced Promotion ID is modified? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the performance impact of broad path-based CF queries at  enterprise scale? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the recommended pattern for recurring Promotion visibility? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the scalable pattern for dynamically surfacing Promotions across  grids and carousels without manual ID references? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the standardized template architecture for Promotion Detail  Pages? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What is the underlying logic that drives filter values — dynamic  metadata/tag queries or hard-coded dialog configuration? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What lifecycle controls exist beyond basic publish/unpublish? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What performance thresholds should we consider for filter volume in Query  Builder–driven listings? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What provider constraints exist when using External URL configuration? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | What validation or fallback logic protects layout integrity when asset  specs are incorrect? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Where is layout behavior governed — Editable Template Policy or component  dialog? |            | @Mayte Eme |        |             |             | Pending  |
| Careers                       | Why do standalone card components Icon and video cards) not inherit  responsive grid policies automatically? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What is the current intended  taxonomy architecture under the SHRSS namespace (Categories, Category, Event  Categories, Properties, Property Names, etc.)? | @Mayte Eme |            |        |             | Pending     |          |
| Tagging_Taxonomy_Metadata_Gov | What are the functional differences between: Categories, Category, Event  Categories, etc? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Which components or services currently reference each of these tag  branches? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What is the safest approach to consolidating or renaming tag branches  without breaking? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What validation steps should be completed before restructuring the  taxonomy? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Which site components rely on ACS Commons Path/Tag mapping?  |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Where are Generic Lists currently configured and what functional  dependencies do they drive? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Are Generic Lists governing allowed tag values in specific components? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | s there documentation mapping each Generic List to its consuming  component? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Why are some Content Fragment Model fields driven by static enumerations  instead of Tag taxonomy? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Should Category fields inside CF Models be refactored to reference  centralized Tags instead of hard-coded options? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What is the difference in  implementation between CQ:tags field, Category dropdown field, Metadata  schema tag-driven dropdowns? | @Mayte Eme |            |        |             | Pending     |          |
| Tagging_Taxonomy_Metadata_Gov | Is Category a required field on Content Fragments?           |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What components currently query Content Fragments by Category tag? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | How does tag selection in a Content Fragment affect dynamic listings  (e.g., News card lists)? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | If taxonomy is consolidated, how will this impact existing Content  Fragments? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Which asset metadata fields are currently tag-driven?        |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Are asset metadata tag fields governed differently than page-level  tagging? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What is the process to audit tag  usage? What is the recommended process for exporting asset metadata for audit  (without selecting “All Properties”)? | @Mayte Eme |            |        |             | Pending     |          |
| Tagging_Taxonomy_Metadata_Gov | Is there a recommended naming convention for tag namespaces and branches? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What happens if a tag in use is deleted?                     |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Does AEM provide dependency warnings before tag deletion?    |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What functionality in SHRSS implementation is currently not supported in  Universal Editor? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | What is the roadmap for migrating back to Universal Editor (Experience  Cloud editor)? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | Are any tag-related features incompatible with Universal Editor? |            | @Mayte Eme |        |             |             | Pending  |
| Tagging_Taxonomy_Metadata_Gov | How do we validate that no dynamic components break after tag  consolidation? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | Why were Careers assets renamed incorrectly during migration? Was the  migration tool responsible for the naming changes? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | What metadata fields should be mandatory upon upload?        |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | Should we rely on metadata (not folder location) for identifying asset  languages (EN/ES/FR)? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | Can we adjust how asset filenames  display in the asset picker and in the Sites rail so authors can see more of  the filename (avoid truncation)? | @Mayte Eme |            |        |             | Pending     |          |
| DAM_Training_Usage_Admin      | How do static renditions get automatically chosen by out‑of‑the‑box  components? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | How can we prevent components from accidentally pulling old or duplicate  assets? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | What are the recommended image rendition sizes for SHRSS components  (cards, banners, hero, gallery, tiles, etc.)? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | When an author uploads a new asset, how do we ensure the correct  rendition is chosen automatically? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | Should static renditions be fully disabled once Dynamic Media is  launched? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | What is the plan for transitioning from static renditions → Dynamic Media  presets? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | When Dynamic Media is implemented, will image presets replace all static  renditions? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | Do we need dedicated language folders in DAM to support future  localization automation? |            | @Mayte Eme |        |             |             | Pending  |
| DAM_Training_Usage_Admin      | Can metadata alone be used to identify language-specific versions of  assets? |            | @Mayte Eme |        |             |             | Pending  |
| Shared_Data                   | How do we decouple the footer? mote very page needs the pre footer. |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How can we validate which components are allowed on which templates? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we enforce component‑level governance so property teams don’t  misuse components? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can we enable/disable components at the template level without making new  templates? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Are there any components that should never be used inside containers? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How can we force authors into structured content (CFs) instead of  free‑form page edits? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Which components support personalization (Target / ContextHub)? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Which components support responsive behavior automatically, and which  require specific authoring steps? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Is there a component audit available showing which components rely on  clientlibs, HTML templates, Sling models, etc.? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Which components support drag‑and‑drop DAM assets natively?  |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Which components support variants / styles, and how do we expose more  styles? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Which CF models support translation and which do not?        |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Do CF references break if CFs are moved into new folders?    |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can CF models be versioned, and how do we migrate existing CFs to a new  version? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | What is the recommended governance for creating new CF models? Who  approves them? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do validation rules in CF models affect existing fragments when rules  change? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do authors locate CFs when the number of fragments becomes very  large? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can CFs support conditional fields or business rules (e.g., show this  field only when…)? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do XF variations handle caching across sites?            |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | When should an XF NOT be used because of performance implications? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can XF inheritance be partial? (e.g., inherit CTA but not image?) |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we prevent authors from editing a variation that should be locked? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | What is the versioning strategy for XFs used on multiple sites with  different publish cycles? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How does AEM’s site search index XFs, CFs, and DAM assets?   |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can we exclude certain XF variations or CF fields from search indexing? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How are navigation links cached and invalidated globally (important for  corporate → property consistency)? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can we define navigation hierarchies outside the Experience Fragment  (e.g., via CFs)? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we properly use “policy inheritance” to avoid accidental template  override? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we create a template that allows flexible component-level  permissions but retains design rules? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can we restrict certain components on certain templates for governance? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can we create a template with two optional headers or footers |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | When authors choose an image from the DAM, can we warn them if the image  is too large (e.g., 12MB)? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can components auto‑select the correct rendition based on container  width? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Does the component detect WebP, AVIF, or DM renditions automatically? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | When Dynamic Media launches, do any current components need refactoring? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do CFs work with AEM translation frameworks?             |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Can XFs be translated automatically, or must they be duplicated per  language? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we ensure shared CF models work across EN/ES/FR without breaking? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Do localized assets need folder-level locale structure if we rely on  metadata only? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Which components automatically contain http://schema.org markup? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Should we add structured data fields to CF models for SEO?   |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we ensure canonical URLs work when XF content is shared across  pages? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | To what extent do CF‑ or XF‑driven pages get indexed differently? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How does AEM handle caching and invalidation when CFs are updated but  used on 30+ pages? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | What is the recommended publishing workflow when shared content exists  across multiple sites? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Do we need a “Content Freeze” rule when updating shared XFs or CFs? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | Is there an audit log showing which components are used on which pages  (to avoid accidental side effects)? |            | @Mayte Eme |        |             |             |          |
| Shared_Data                   | How do we troubleshoot page performance if components load large images  or too many CF references? |            | @Mayte Eme |        |             |             |          |
| Locations                     | Which fields are sourced from  DPLT, which are managed directly in the CMS? Is it just relation to location  ID? |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | If a location’s status is  changed, how does that impact its visibility or behavior in AEM? |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | When a location is added to  DPLT, does it automatically appear in AEM even if some values are blank? |            | @Mayte Eme |        |             |             | xq       |
| Locations                     | Is the display or availability  of locations in AEM driven by any specific DPLT status? |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | What are the steps to add  locations to another page in AEM? |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | How can we add locations without  using the accordions?      |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | How do we add decorations with  the map?                     |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | How can we add only the map and  locations, without including accordions? |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | Why are images not displayed for  some locations?            |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | How do we add a location not yet  in the DPLT?               |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | How do we set up criteria in AEM  to display specific locations? For example, based on one or multiple LOBs,  different DPLT criteria (geo, amenities, sub-locations, categories) |            | @Mayte Eme |        |             |             | Pending  |
| Locations                     | Which DPLT field should be used  to replace the Location ID as the Content Fragment Title (e.g., Legal Name,  Long Name, Short Name)? |            |            |        |             |             | Pending  |
| Locations                     | What is the correct process for  bulk updating Content Fragment titles using metadata values? |            |            |        |             |             | Pending  |
| Locations                     | Which fields in the Location  Content Fragment are read-only vs. author-editable? |            |            |        |             |             | Pending  |
| Locations                     | When a new location is added to  DPLT, does the author need to manually check “Is Delivery”? |            |            |        |             |             | Pending  |
| Locations                     | What image specifications  (size/dimensions) are required for the Location image field used in hotel  components? |            |            |        |             |             | Pending  |
| Locations                     | What happens if authors  mistakenly populate hotel-specific editable fields on a cafe location (or  vice versa)? |            |            |        |             |             | Pending  |
| Locations                     | Is component display logic  restricted by Line of Business (LOB) to prevent incorrect cross-display  (e.g., café appearing in hotel components)? |            |            |        |             |             | Pending  |
| Locations                     | If authors incorrectly check “Is  Delivery” for a hotel, will it surface in cafe delivery results? |            |            |        |             |             | Pending  |
| Locations                     | Are any fields in the Location  Content Fragment required for publishing? |            |            |        |             |             | Pending  |
| Locations                     | Are delivery links automatically  configured to open in a new tab? |            |            |        |             |             | Pending  |
| Locations                     | Is there any scenario where  delivery links would be internal instead of external? |            |            |        |             |             | Pending  |
| Locations                     | If delivery partners change, is  updating the URL in the Content Fragment sufficient? |            |            |        |             |             | Pending  |
| Locations                     | Does adding delivery partners  require republishing the Location fragment only? |            |            |        |             |             | Pending  |
| Locations                     | If a new field (e.g., Meeting  Room View) is needed, what is the process to update the Content Fragment  Model? |            |            |        |             |             | Pending  |
| Locations                     | Who has permission to modify  Content Fragment Models?       |            |            |        |             |             | Pending  |
| Locations                     | After adding a new field to the  model, what additional front-end updates are required for display? |            |            |        |             |             | Pending  |
| Locations                     | If a new venue data field is  added, does the Sort By dropdown also require component updates? |            |            |        |             |             | Pending  |
| Locations                     | Are venue fields (Meeting Rooms,  Max Capacity, Area, Guest Rooms) hard-coded in the component? |            |            |        |             |             | Pending  |
| Locations                     | Are venue fields required for  publishing?                   |            |            |        |             |             | Pending  |
| Locations                     | Can authors add additional  buttons beyond “Additional Information” and “Fact Sheet”? |            |            |        |             |             | Pending  |
| Locations                     | Is the “View More” link  automatically tied to the uploaded fact sheet PDF? |            |            |        |             |             | Pending  |
| Locations                     | Are filter categories (e.g.,  Type of Destination, Type of Vacation) configurable without development? |            |            |        |             |             | Pending  |
| Locations                     | If a new filter category is  needed, does that require Content Fragment Model changes? |            |            |        |             |             | Pending  |
| Locations                     | If a new sort option is needed,  does that require both model and component updates? |            |            |        |             |             | Pending  |
| Locations                     | Are regions (North America,  Europe, etc.) tied to folder structure or another data source? |            |            |        |             |             | Pending  |
| Locations                     | Can specific countries be  manually excluded from a region list? |            |            |        |             |             | Pending  |
| Locations                     | Can authors manually control  which countries display under each region? |            |            |        |             |             | Pending  |
| Locations                     | Is the inability to manually  control country listings considered a functional gap? |            |            |        |             |             | Pending  |
| Locations                     | Why are some images not  displaying on the Destinations page (missing image vs. unpublished)? |            |            |        |             |             | Pending  |
| Locations                     | Is there image position/focal  point control available in this component? |            |            |        |             |             | Pending  |
| Locations                     | Should styling inconsistencies  (accordion width, padding issues) be treated as gaps? |            |            |        |             |             | Pending  |
| Locations                     | Is there a formal review process  before components are considered “handed off”? |            |            |        |             |             | Pending  |
| Locations                     | Does the Google Map component  allow manual country selection (unlike Destination Search)? |            |            |        |             |             | Pending  |
| Locations                     | Should locator behavior (hotels,  cafes, corporate) allow granular country-level control? |            |            |        |             |             | Pending  |
| Locations                     | Is the Google Map component  functionally different from Destination Search & Filters? |            |            |        |             |             | Pending  |
| Locations                     | Will map functionality be  reviewed separately in KT?        |            |            |        |             |             | Pending  |
| Locations                     | Is the Booking Widget configured  via Experience Fragment?   |            |            |        |             |             | Pending  |
| Locations                     | Is the “Book Now” modal  referenced in the header via the Crown CTA component? |            |            |        |             |             | Pending  |
| Locations                     | How does the theme override  button styling in Experience Fragments? |            |            |        |             |             | Pending  |
| Locations                     | What is the difference between  “Default” and “Pop-up” style variations? |            |            |        |             |             | Pending  |
| Locations                     | Where is the booking URL  configured for each hotel?         |            |            |        |             |             | Pending  |
| Locations                     | Is booking engine logic  currently limited to specific engines (e.g., SynXis)? |            |            |        |             |             | Pending  |
| Locations                     | If additional booking engines  are required, does that require component enhancement? |            |            |        |             |             | Pending  |
| Locations                     | Should visual alignment issues  in the booking widget be logged as a gap? |            |            |        |             |             | Pending  |
| Locations                     | Where should A/B testing  (Target) be applied — at Experience Fragment level or elsewhere? |            |            |        |             |             | Pending  |
| Locations                     | Is analytics event firing  handled in the component or at developer/data layer level? |            |            |        |             |             | Pending  |

