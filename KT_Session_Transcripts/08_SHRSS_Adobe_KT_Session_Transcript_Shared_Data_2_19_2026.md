---
title: SHRSS Adobe Knowledge Transfer - Shared Data Session Transcript
source: KT Session (Microsoft Teams meeting recording)
date: 2026-02-19
topic: Shared Data
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

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
