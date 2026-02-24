---
title: SHRSS Adobe Knowledge Transfer - DAM Session Transcript
source: KT Session (Microsoft Teams meeting recording)
date: 2026-02-18
topic: DAM
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

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
