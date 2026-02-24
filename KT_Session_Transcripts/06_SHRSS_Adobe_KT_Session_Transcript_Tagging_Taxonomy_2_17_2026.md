---
title: SHRSS Adobe Knowledge Transfer - Tagging & Taxonomy Session Transcript
source: KT Session (Microsoft Teams meeting recording)
date: 2026-02-17
topic: Tagging & Taxonomy
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

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
