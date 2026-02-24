---
title: SHRSS Adobe Knowledge Transfer - Jobs Session Transcript
source: KT Session (Microsoft Teams meeting recording)
date: 2026-02-10
duration: 1h 53m 23s
topic: Job-related components, job content fragment, Workday integration
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

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
