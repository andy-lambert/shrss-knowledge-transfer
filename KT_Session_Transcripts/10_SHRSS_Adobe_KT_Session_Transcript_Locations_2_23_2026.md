---
title: SHRSS Adobe Knowledge Transfer - Locations Session Transcript
source: KT Session (Microsoft Teams meeting recording)
date: 2026-02-23
topic: Locations
parts: "Part 1 (49m 15s); Part 2 (10m 37s) — recording restarted due to technical glitch"
format: Markdown transcript (no images). Optimized for AI ingestion and analysis.
---

**SHRSS Adobe Knowledge Transfer-20260223_130200-Meeting Recording --
PART 1**

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

**SHRSS Adobe Knowledge Transfer-20260223_135724-Meeting Recording --

PART 2**

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