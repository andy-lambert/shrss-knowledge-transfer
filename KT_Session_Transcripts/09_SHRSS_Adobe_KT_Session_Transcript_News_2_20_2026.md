---
title: SHRSS Adobe Knowledge Transfer - News Session Transcript
source: KT Session (Microsoft Teams meeting recording)
date: 2026-02-20
topic: News
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

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
