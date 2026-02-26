**SHRSS Adobe Knowledge Transfer-20260224_130151-Meeting Recording**

February 24, 2026, 1:00PM

1h 50m 12s

Lucas Nelson** started transcription

**Lucas Nelson** 0:09
All right, Danielle, it\'s all yours. Thanks.

**Daniela Tea** 0:12
All right. Thank you everyone for joining. Apologies again for yesterday\'s computer technical issues. Hopefully we won\'t have that today, but what I wanted to cover today is first start off with some follow-up items from our new session. I I had planned on doing that yesterday.
But Edwin, I don\'t think you were here at the time at the beginning. So I just wanted to quickly cover at least one of your questions from that day. And then I also want to show some follow-ups from yesterday\'s session before it got cut short. And then we\'re going to continue the rest of the agenda to go over the remaining locations related components.
and leaving some time for questions and and seeing where we end up at the end of the call. So I\'m going to go ahead and share my screen so we can take a look at that news page here on the Confluence page. And Ed, when I saw this specific question here, um the other items I know
That we had also talked about on on our call and I am planning on going through the confluence pages and providing some answers, but for this one I think it\'ll be easier if I just show what we\'re talking about here. You asked what path do we choose for the CF list path? This was a bit confusing in the enablement session.
Can we maybe explore updating the info tools to be more informative as it isn\'t intuitive on on what the path should be? So I was a little confused when I saw that, but I looked down here and I saw that it was specifically for category listing, so I wanted to just show and confirm our understanding of this.
So here on our news pages we have these two category listing components. Depending on how you configure it, it can either be showing categories or it can show archives. Your question specifically was what should the content fragment list path?
And what we can see here is that I\'ve selected the path for showing all the years. So basically the EN is what I\'ve selected. So that\'s going to be showing all the content fragments that are news under corporate under EN.
And then immediately under that all these child items will be listed here on the side. And I saw an example of a page where that was not set. So this is just a page I I saw on stage. The category listing is listing something different.
And the reason why is because this specific content fragment list path stops at news and so if corporate, that\'s why the the child items immediately under news being displayed. But to show the years like we saw previously, you would have to just go down a little bit further in the DAM.
So if this were changed to EN, I\'m just actually going to do this because we\'re in stage, so it\'s OK and we hit done. You can see how it updates to that next child, that next child level, which happens to be the year folders.
So just wanted to confirm that that was what your question was, is you know, what would you ideally want to put in this path? And whatever you plan on showing, it\'s going to be the child, the child level immediately after the last item in your content fragment list path.

**Edwin Aquino** 3:33
Thank you, Daniela. That that covers it exactly. It was just a little bit confusing for the team and we wanted to make sure we had the right answer for that.

**Daniela Tea** 3:37
OK.
Yeah, perfect. Understood. So yeah, glad I could answer that. And again, I think it was a lot easier to do it by just showing it versus trying to write that out. So, OK, great. All right. So that was the one item from news. You had also asked about the news page template. We are going to be covering page templates hopefully this week, if not very.
Early next week, depending on how far we can get through the other items. So we\'ll talk about the name field since that\'s not exclusive to news page, it\'s for all pages. Alright, OK, I\'m gonna pull this over to the side now and I wanted to address another question that came up yesterday.
With regards to the dining, I\'m sorry, the delivery widget and I think Lisa, you\'re on and I just wanted to confirm when we take a look at this, I think your concern, you mentioned a hotel that was on here. I don\'t see it here, but maybe it was on the production or.

**Lisa Cardia** 4:35
Yeah, it\'s it\'s actually, it\'s a casino that\'s showing. So how it\'s Hard Rock Casino, Rockford. Obviously we wouldn\'t want that unless something\'s pulling like the wrong name for that location.

**Daniela Tea** 4:37
Something.
OK. Yeah. OK. OK. Yeah. So I.
Right.
Yeah, so let me show you. I did some digging as to why is this coming up? Um.

**Lisa Cardia** 4:52
Yeah, \'cause I think we reported this actually like way back when when we were, you know, looking at Cafe for validation. So something\'s not right at DLT.

**Daniela Tea** 4:59
Yeah, so.
Yeah, OK, Yep, Yep. So you can see here the property legal name is Hard Rock Casino Rockford. The location legal name is Hard Rock Cafe Rockford Casino. This this specific item has this delivery with the Uber Eats. So and if you look down here the sub, the line of business is.
Cafe.
So that\'s why this specific item is coming up in that list. I also did some tests just to take a look. You\'ll notice this here. What I\'m showing is Hard Rock Hotel, Daytona Beach and the line of businesses hotel. What I did was I added some test delivery partners for.
Delivery, however, and I published it too. You can see I had published it. However, it\'s not going to appear because it\'s not the line of business isn\'t Cafe.

**Lisa Cardia** 5:53
OK. That\'s good to know that the line of business is dictating this widget. I think the concern here is, I don\'t know Scott or IT if someone can take this to the right contact to say like like this casino is getting classified as a cafe, which I believe is wrong.

**Daniela Tea** 5:58
Yes.

**Lisa Cardia** 6:14
I don\'t know who the contact is for this though. This is my question to SHRSS.

**Daniela Tea** 6:17
Hmm.
Mhm.
I yeah, I.

**Lisa Cardia** 6:24
31.

**Kerry Holyoak (SHRSS)** 6:24
Is it? Is this being driven by the DPLT integration?

**Daniela Tea** 6:27
That\'s, yeah, that\'s correct. Any field that you see here is that\'s hard. I\'m sorry, that\'s disabled. That\'s coming in from DPLT.

**Kerry Holyoak (SHRSS)** 6:37
Then the DPLT team needs to all the classifications have to come through DPLT correctly, and that\'s Vipul Patel.

Lyon, Rick (Director of Digital Experience)** 6:38
So it\'ll be that team, yeah.

**Lisa Cardia** 6:46
OK, so.

**Kerry Holyoak (SHRSS)** 6:47
So if you see something misclassified here, then we need to take that up to Vipul\'s team.

**Lisa Cardia** 6:53
OK, that\'s fine. I was just curious because obviously this is the only one that this is happening for, right? The casinos. This is the only casino showing as a cafe compared to other locations that might be a casino, but their cafe specific location is showing. For example, Hollywood comma Florida is the Hollywood.

**Daniela Tea** 7:00
Mhm.

**Kerry Holyoak (SHRSS)** 7:00
Mhm.

**Lisa Cardia** 7:13
Cafe. Yet there is probably a different DPLT name and number associated for the casino for Hollywood. So does that make sense? So something\'s wrong with Rockford.
Rockford should just say Rockford in this list if Rockford has a cafe.

**Daniela Tea** 7:29
Mm.

**Lisa Cardia** 7:31
And I\'ll take this back then. I guess I\'ll, yeah, that\'s fine.

**Kerry Holyoak (SHRSS)** 7:35
Um.

**Daniela Tea** 7:37
Did did did you need the property ID number Lisa or?

**Lisa Cardia** 7:41
Um, if I can just like, actually zoom in and I\'ll screenshot this. Yeah, that\'s fine.

**Daniela Tea** 7:45
Yeah, that\'s helpful. Um.

**Lisa Cardia** 7:49
Thank you.

**Daniela Tea** 7:49
Yep. And so yeah, I just wanted to show though. Um, so yeah, I had done some tests.

**Lisa Cardia** 7:53
I just thought it had mistakenly said is delivery, but it\'s and that by mistake it was like selected for a casino property. But it\'s because this is classified as cafe and DPLT. So OK, let me reach out and I will get.

**Daniela Tea** 7:57
Hmm.
Yeah.
Correct. That\'s correct, yes.

**Lisa Cardia** 8:09
You can carry on, I\'m sorry.

**Daniela Tea** 8:10
Sure, no problem. Yeah. So I was testing, I did some tests, you know, with the hotels. So with this Hard Rock Hotel, Daytona Beach, the category was, I\'m sorry, the live business was hotel that did not appear in the list. And then I also tested with like for example, this one was sports book and it was categorized as a sports.
Book also not paired the list and then to make sure that things were actually being published, updating an existing one like Amsterdam and you can see here\'s my fake Google one. So this is basically pulling in the things that our line of business Cafe has is delivery checked.
And it\'s it\'s just showing those names. So Lisa will you know if they make that change in DPLT like changing the the line of business or something, this should be removed even if his delivery information is still stored there. But we can certainly you know look at that later once that changes is made.

**Lisa Cardia** 9:00
OK.

**Daniela Tea** 9:05
In DPLT. So Yep, no problem. All right, so that was a follow-up from yesterday that I wanted to make sure the team was aware of. Let me pull up the agenda so we can take a look at what else we are covering.

**Lisa Cardia** 9:07
Take care.

**Daniela Tea** 9:24
All right. So yesterday we talked about the location content fragment and we\'ll continue to reference that as we go through some additional components, the venue CF and how that works for hotels and how it\'s displayed within the destination search and filters component.
We started talking about the booking widget and then that\'s when my computer died. So we\'re going to pick up here and go over booking offers, find a location, Google map, and I know Gonzalo said he had some questions about this one and then also the location list component. So let me go ahead and pull up our booking widgets.
Booking widgets. OK, so I\'m just going to pull the publisher side to the right and the configuration side on the left. And right now I am in Cancun Hotels homepage and we\'re taking a look now at the booking widget from the.
Within the content page point of view. All right. OK, so let\'s let me select my booking widget and take a look at how this has been authored. So as we saw yesterday, if you guys remember the same widgets being used within this book now component.
We have our the ability to display it in two different ways, whether it\'s within a modal like we see here, or whether it\'s just on the page like we see here will be listed horizontally. The fields are exactly the same since the same component, just a style variation has been either default or pop up.
And you\'ll notice here under under my group name I have North America, but my destination is Cancun with the specific URL where the book now will lead to and the destination value and I\'ve enabled rooms, adults and children.
And so this here rooms, adults and children is displayed because I had that check mark there. You see North America, which was the group name Cancun, which was I I had configured for it to say Cancun.
And then the you know. So let\'s take a look at what gets passed. We need to hit book. Now we can see that this passes in the parameters I had selected from the previous page, including the one second.
Uh, geez.
Including the destination URL, so hotel.
Reservations are hardrock.com. The destination value of 59391 is getting passed in so that we were able to go specifically to our Cancun location and then all the parameters for rooms, adults and children are also getting passed in as you can see here with the URL.
And Rick, I see your hand up. Um, please go ahead.

Lyon, Rick (Director of Digital Experience)** 12:22
Sorry, I didn\'t want to interrupt your your flow. Can we see that the pop-up booking model again? There is like a black border thing around it.

**Daniela Tea** 12:28
Yeah, certainly.
Yeah, so I think this here is. So this is coming in from the modal, I believe if we were to, yeah, so this is coming in from the modal on the backgrounds. Try to remember if you can change that or not.

Lyon, Rick (Director of Digital Experience)** 12:50
What can we make the the booking widget the same size as the model, at least the background color or something?

**Daniela Tea** 12:54
Mm.
We can see.

Lyon, Rick (Director of Digital Experience)** 12:59
OK, that was it. I didn\'t mind it. Sorry, I check it. Sorry.

**Daniela Tea** 12:59
So I\'m gonna pull. No problem. Yeah, no problem. Let\'s take a look at this this experience fragment though, just to make sure we understand how it\'s used also with an experience fragment. Let\'s see, where\'s Cancun?

**Lisa Cardia** 13:16
And again, while you\'re looking for the location, we get the number from here. Where do we get that number from?

**Daniela Tea** 13:17
OK.
So the number was, I think, Rick, can you answer that question with regard? You\'re talking about the destination value, Lisa. Yeah, Rick, these are numbers I believe that were provided to us during like the migration like these were. Yeah, OK.

**Lisa Cardia** 13:30
Yeah.

Lyon, Rick (Director of Digital Experience)** 13:31
Yeah.
Yeah, I\'m sorry. If it\'s a hotel, Lisa, these are the Senex societies.

**Lisa Cardia** 13:41
OK, so we would have these already somewhere for reference and or they\'re just like pre created once this is handed over. Oh like I just want to make sure that as authors.

Lyon, Rick (Director of Digital Experience)** 13:47
Yeah, yeah, you\'ll you\'ll see it in like the booking links. It\'ll be like hotel is 68 whatever, whatever and then I\'ll say or chain group or something and then hotel equals and then that\'s usually when you\'ll see this number. Now I can\'t speak to site core sites, so I don\'t know what.

**Lisa Cardia** 14:00
Yeah, no, we we don\'t use values. We just have a link. Um.

Lyon, Rick (Director of Digital Experience)** 14:04
Right. So I don\'t know what that what this would look like if this was, you know, a a casino if you\'re trying to book Hollywood. So I don\'t know if it would just link off here or.

**Lisa Cardia** 14:09
Or actually, yeah, you\'re right.
I\'ll speak to that. I mean, actually I\'ll let IT speak to that because I\'m sure there\'s other configurations that I don\'t want to jump to conclusions for Sitecore. I was just curious, as authors, do we need to know that number moving forward or like once this is configured, there\'s no need for us to really get that number?

Lyon, Rick (Director of Digital Experience)** 14:17
Yeah.

**Lisa Cardia** 14:29
Again.

Lyon, Rick (Director of Digital Experience)** 14:31
I would say yes and yes. I don\'t know if they\'re all gonna come in, so you shouldn\'t have to do anything, but those numbers will never change. So once they\'re set, you should be good. But Danielle, So what? How does this work with a casino?

**Lisa Cardia** 14:36
OK.
OK.

**Daniela Tea** 14:44
So I think for a casino, I don\'t, I would need to check to see what had been migrated. Keep in mind that I know that when we pause the project we keep, we were planning on discussing additional booking engines and stuff specifically for casinos.
For the booking widget and also the booking offers component. So I\'m not quite sure if those like those had been finalized, but there is there were still some gaps that we were discussing before the pause. So right now this here like the destination value like you were saying Rick, I believe this was specifically for your.

Lyon, Rick (Director of Digital Experience)** 15:13
OK.

**Daniela Tea** 15:20
The Vizirgy sites and anything that had been previously within like the Hard Rock Hotel like Destiny\'s Rock Zoo should have been carried over during the migration. So if you\'re saying they would never change for these locations, they will already be in the dialogue window with this like text like this.
So I think Lisa, if like someone were to like put something else here and hit done and messes that up, then yes, she would need to be able to restore the previous value. But anything that\'s been migrated over like it should still it should be there.

**Lisa Cardia** 15:50
Okay, thank you.

Lyon, Rick (Director of Digital Experience)** 15:51
Is there any way we can test a casino if you had one migrated over just to because the the value, the ID is for Synexes. I don\'t know how the wind surfer links. I don\'t know if there\'s an ID maybe Kerry can jump in.

**Daniela Tea** 16:04
Yeah. So I I think with our during the IB discussion having specifically for casinos, that\'s where that\'s like right around the time of the pause. So I don\'t think that that\'s been finalized yet. So yeah, for Visorgy though this should be fine, yeah.

Lyon, Rick (Director of Digital Experience)** 16:15
Mhm.
OK.
OK.

**Daniela Tea** 16:22
I\'m going to hit cancel so we can see how this was authored here within the page and we were taking a look at our experience fragments which I opened up the header of Cancun.
I open up the Crown CTA component and I\'m scrolling down and we\'re seeing that we are referencing our book now experience fragment to open up within a modal. So as you can see here this is there\'s.
The modal itself I believe does have a black background automatically, Rick. So if the desire would be say to have like this be like a configurable color or something, that\'s something I I would want you guys to note down as like a gap, right? If that\'s the desire to do this.

Lyon, Rick (Director of Digital Experience)** 17:13
Yeah, just edge-to-edge. Nothing special. Just the, you know, black border. It\'s just it\'s like thicker at the bottom, so it doesn\'t even look like a border, just like a smaller container inside of the pop-up container.

**Daniela Tea** 17:21
Mm.
So let\'s take a look at the experience fragment version of this. We can see how you would set up the book now button to point to it, but we can take a look now at the experience fragment itself. So Cancun EN book now. So let\'s open this up.
And as mentioned before, again, don\'t forget when you are looking at things in the experience fragment section, the theme\'s not going to be applied. So this is certainly going to look different when you actually view the site. I\'m going to open this up and you can see here this is the exact same configuration as I had for what\'s on the.
Actual page itself O this portion here has been configured the exact same way. The only difference is that the style has been changed to OU.
Right. OK.
All right, so any questions about the booking widget component?

**Lisa Cardia** 18:27
Just for the rooms, adults, children, I know that that\'s what we have today, but just so I can understand configuration wise if we ever had to add or I I know for a remove would just be unchecking, but I see that word add that what what does that?

**Daniela Tea** 18:30
Mhm.
Mhm.
Uh.
Yeah.
Oh, so this this adds. Let me show you the version on the actual on the hotel site. So when you have multiple locations, oops, this is not what I want. When you have multiple locations, you would have.
Different groups that they\'re under. And so in this case here we have North America and then you have all these hotels underneath, right? So as I\'m adding locations here, like if I so in North America, I could add additional ones, right? So like Atlanta or whatever and then it would just be in whatever order.

**Lisa Cardia** 19:02
Okay.

**Daniela Tea** 19:17
I specify here, I save it and then it would appear within that dropdown. That\'s what the ad does.

**Lisa Cardia** 19:21
OK, so there\'s add for the group name and then add for destinations. But for those categories, just in the case of the future that we need a different differentiator, label, field, whatever for what someone selects, like say it\'s like you know, balcony, I don\'t know.

**Daniela Tea** 19:23
Mm-hmm. Underneath that group name, yeah.

**Lisa Cardia** 19:38
Do we? I just want to know, does that field right there require the development to the to the component? I guess I just want to know how it works or I know we don\'t have any other options today besides those three, but just wanted to know for future reference.

**Daniela Tea** 19:50
Mhm.

**Lisa Cardia** 19:54
If someone were to request it.
Yeah, different field.
Uh huh.
Uh huh.

**Daniela Tea** 20:15
Enable balcony and then determine what those fields should be. Is it like a yes or no field? Is it like a one through 6 whatever? It would probably be yes or no and then also and then updating the UI. So that would be development for sure.

**Lisa Cardia** 20:31
OK, OK.

**Daniela Tea** 20:32
Yep, because there\'s also like, you know, things in place to make sure it gets passed to the correct parameter, that sort of stuff.

**Lisa Cardia** 20:37
Right. It\'s gotta be smart enough on the booking engine side too. OK, thank you.

**Daniela Tea** 20:40
Yes, correct. Yep. All right. Um, OK. Yeah. Any other questions though about the booking widget?
Right.
OK. If not, let\'s jump on over then to booking offers, which is pretty similar. However, there\'s just a couple of nuances. So First off and Rick, I know that we had talked about.
I think like I was trying to find, I was trying to find like a live version of this. I wasn\'t clear if there was a live version of of where booking offers is being used. So I found something that was like old, at least in our author environment. So if there is something that that\'s live today, I can certainly take a look at it, but.

Lyon, Rick (Director of Digital Experience)** 21:28
The only thing is the the footer of the hotel site. There\'s a travel corporate and a travel.

**Daniela Tea** 21:29
It\'s.
Mhm.

Lyon, Rick (Director of Digital Experience)** 21:40
I can\'t remember travel advisors or something, but it\'s in the footer. All the offers. What they do is they just they set up the offer for anybody participating on the booking engine side so we don\'t have to pass a parameter, but these here do pass a parameter, so if you wanted to see it.

**Daniela Tea** 21:43
OK.
Oh.
Mhm.
Yes, OK.

Lyon, Rick (Director of Digital Experience)** 21:57
Just, yeah. And then you\'ll see it up top. There\'s R coming, R coming.

**Daniela Tea** 22:01
Yeah, saw it. Yeah, yeah, I saw the archon. Yup, I see it here. OK, So what we had here for booking offers is we it\'s as mentioned before, it\'s pretty similar to booking widget. We\'re able to put the group name if you need to. You don\'t have to put it on default to select a destination.
Yes, I see that this is truncated, certainly something that you guys would want to note, but the functionality for this one is just the ability to put those selected places that have that offer going, the ability to put that booking URL. In this case here I know this says EN and that\'s because.
This this I believe is an older page. I don\'t know if this is still valid anymore, but and then in our stage environment these right now are just defaulting to to to put something here since this offer is no longer valid, but you would certainly put the booking URL here. If you need to enable arrival and departure dates, that\'s also something that can be selected.
And then here at the bottom you have the booking window start date and end date. Now this is just for display purposes only. This takes up this portion here and you can see there\'s no way for the end user to change this. This is essentially like a read only field. What they can select is the specific destination they want to go to and the.
Depending on whether or not arrival arrived date and depart date have been selected, that determines whether this is showing. So in the case of Bali, if we look at the configuration window, we\'ll see that this did not have enable arrival and departure date selected. However the other ones did, which is why those.
Up here then. So this is the booking offers. Again, Rick, I I do see the version here on this page. I I noticed that this doesn\'t necessarily have the arrival dates. I don\'t know if that\'s that was intentional. I think when we reviewed it initially it did have like a window.
Um, for the booking window, OK.

Lyon, Rick (Director of Digital Experience)** 23:56
Yeah, this is just open. It\'s as long as you, you know, either one\'s for a travel agent. So this is the one for agents, travel agencies or whatever. The other one is for for corporate staff, so they didn\'t need the date.

**Daniela Tea** 24:04
OK.
OK, OK. So yeah, yeah, I think, I think then for for here the start date and end date is is not actually mandatory. But yeah, we don\'t. This is an, I know this is an older page so just wanted to show though how this worked, what the intention was for and.
An example that\'s on the live site right now where this specific component is used. I\'ll pause though and see if there\'s questions about this.

**Lisa Cardia** 24:38
Yeah. Do you mind opening? Oh.

Lyon, Rick (Director of Digital Experience)** 24:39
Are we able to hide that booking window section? Sorry.

**Daniela Tea** 24:41
Oh, let\'s try it. I\'m going to make a copy of the component.
And.
OK.
So the booking window is still present, but just the field is blank. Obviously if if you guys are hiding the values I can understand if you guys want to also hide the label too, but as you can see this is how it would work today where it would be present.
On the component.
But the fields itself aren\'t necessary. Yeah, go ahead, Lisa.

**Lisa Cardia** 25:24
Um.
My question again, sorry if I like missed it, just figure out what overrides it. So when you click the configure again.

**Daniela Tea** 25:34
Mhm.

**Lisa Cardia** 25:36
And so we\'re looking at a destination. So we have Bali which doesn\'t have enable in departure dates. So what displays when it\'s not checked and then what displays and then what displays when it is checked and then what about?

**Daniela Tea** 25:44
When it\'s not checked, yeah, when it\'s not checked, it looks like this. You can see that those specific fields didn\'t show up. When I chose Cancun though, these two fields did show up.

**Lisa Cardia** 25:51
What?
OK, so when it\'s not checked, it\'s using the if you go back to configure.

**Daniela Tea** 26:01
Yep.

**Lisa Cardia** 26:06
So if it\'s left unchecked, it\'s using the dates at the very bottom, the booking window dates.

**Daniela Tea** 26:10
Oh, so, so where? Hang on. Yeah, one second. Oh, sorry, sorry. Let\'s take a look at this again.

**Lisa Cardia** 26:18
No, I think I thought that was where it was.

**Daniela Tea** 26:20
Yeah, yeah, yeah. So yeah, the keep in mind the booking window this and correct me if I\'m wrong, like you could theoretically still bypass this by selecting dates outside of it. Is that accurate?

**Lisa Cardia** 26:40
Rick, you\'re on mute if you\'re.

Lyon, Rick (Director of Digital Experience)** 26:43
That was, yeah. If this is, this is for the offer space. We\'ve we\'ve kind of modified this since the version you have. So we do have a booking window and that kind of sets the calendars. So those calendars will still pop. I don\'t know if.

**Daniela Tea** 26:53
OK.
OK.

Lyon, Rick (Director of Digital Experience)** 27:03
This functionality is in the component, so I\'m explaining it. So like it says February 15th to August 31st. So the arrive is going to start at February 15th and then the depart would somewhere end, you know August 31st. So you have to pick dates between those.
Success since that\'s the booking window.

**Daniela Tea** 27:18
OK, but got it. So to confirm though, because I I feel like when the component you said that that\'s been like that\'s a a newer change, is that correct?

Lyon, Rick (Director of Digital Experience)** 27:30
Yeah, like I said, because they don\'t have to do the rates anymore. So they kind of try to simplify it and do it on the side. So once you\'re at the booking engine, you\'ll see all the rates. But the point is, I guess once you\'re there, you\'re gonna book regardless, so.

**Daniela Tea** 27:31
OK.
I see.
OK, got it. OK.

Lyon, Rick (Director of Digital Experience)** 27:46
That\'s what the the decision was.

**Daniela Tea** 27:47
OK, OK, so so that logic is likely not in here since that sounds like it\'s it\'s newer. So right now if you have the booking window set again, I think this is going to be just for like the display purposes, right? So you can see a changes 2026 this one.
The bottom um and.

**Lisa Cardia** 28:09
So it\'s if you have the booking window set and you leave it unchecked, you\'ll see it. If you have the booking window set but you check it off, you\'ll see it, but you also can choose your dates.

**Daniela Tea** 28:18
You will always see the booking window. Yeah, you\'ll always see that regardless. It\'s just that if you don\'t have arrival date and end date checked, that\'s not going to pass in. It\'s not going to pass in like any like user fed dates because there\'s no option for them to add that.

**Lisa Cardia** 28:21
Always will see the booking window.
OK, but there\'s no option to hide it completely.

**Daniela Tea** 28:38
Correct. There\'s no option to hide it completely as of right now, yes.
OK.
All right, I\'m gonna remove this since this does not belong to that page. All right, so let\'s move on now to finding a location. So this one is something I think you guys are familiar with on the home page.
Of the Hardrockcom website. Let\'s take a look at that here.
Yep, so find find a hard rock. Let\'s configure this.
All right, so author authorable fields, our location label, find a Hard Rock, our placeholder text. What appears here in the search bar, our search text. This is for the button itself, the view all text for the view all button.
If something\'s empty and someone tries to hit search then the message will appear and then also we have the page path. So essentially what the search and view all take you to. This will take you to the locations page. So that\'s the configuration for here and as we know the way it works.
If I were to put in a zip code and hit search, that gets passed as a parameter here. If I were to click view all, this just takes me to the locations page as specified in my configuration.
And if I were to say put some junk and I hit search, it\'s going to pass in the junk. But if I were to put in.

**Lisa Cardia** 30:20
And I\'m sorry, what where did we determine the path that of search or that\'s just like this is configured?

**Daniela Tea** 30:24
The path of search and and view all is determined by this page path right here.

**Lisa Cardia** 30:29
So both view all and search is to locations.

**Daniela Tea** 30:33
That\'s correct, yes. The locations page. Yep. OK, so since I didn\'t put anything in, here\'s that text that appears that was authored under empty input text.

**Lisa Cardia** 30:34
OK.

**Daniela Tea** 30:47
OK.
All right. And to my knowledge, I don\'t think you guys are using this. You guys are probably not using this currently on any other site, is that correct?

**Lisa Cardia** 31:04
I think that was going to just be my question. I don\'t think we are, but I was just wondering if we could change the color of the find a location like background if necessary.

**Daniela Tea** 31:12
Right now I believe that is established as black or whatever exact hex code this is. So if if a color change is required like if you wanted to use it on.
I don\'t know which theme or whatever, but that would have to be something that is updated through code to just allow for like this background to be changed by an author. OK, all right.

**Lisa Cardia** 31:38
OK.

**Daniela Tea** 31:42
OK, so that is the Find a location component. I\'m going to move on to the Google map component and I\'m going to show.
How it is currently right now and I\'m in stage. Just to be clear, I am in stage. I\'m not messing around anything on production, but I\'m in stage on the locations page. But I am going to go to the corresponding page here on the.
Published version. All right. OK, so here on our locations page you\'ll notice that there is something that says placeholder for Google Map component and this component here called Google Map is present. However, if I were to click on view as published.
You\'ll see it says oops, something went wrong. It didn\'t load. The reason why you\'re seeing this message is because essentially when I was talking to the devs about this, the the authoring side and the anything that\'s not in prod like the those URLs.
Would need to be whitelisted. So that\'s why you\'re seeing this issue. It\'s not really an issue, but it\'s that\'s why you\'re seeing this message because this particular domain has not been whitelisted. So anything in the author side has not been whitelisted. So I believe that would be something that the SHRSS IT team.
Would be managing. We would just need to make sure that anything an author is whitelisted. So that way when an author views is published, they would be able to actually see the map on here. As you can see here on the publisher side, the map is displaying because that\'s because this particular domain has been whitelisted.
So just want to make sure the team is aware you will see this message down in author, but the map does work and it is due to whitelisting domains.
All right, so let\'s go back to this component and let\'s break it down and see how we\'re getting this map to populate.
Wanted to be clear that this specific information, this was the API key was provided by the Hard Rock team and some some items here that you\'ll notice like C region for the element ID, you know things like that. This was all things that were migrated over. So I believe this was associated.
With the map on the original site, when it got migrated over to AEM, we retain those values here. So if the API key changes or anything like that, that is something that someone from the tech team would be able to handle. The authors don\'t have the ability to change out the API key.
I believe that is a smart move. You wouldn\'t want someone to be able to remove it or replace it or anything like that. The API key is handled outside of the configuration window and that would be managed by anyone who has access to.
Environment variables which would which would typically be like the dev team. OK so for our Google map component the element ID field. This is specifically for if you\'re say doing any JavaScript and you need to like you know have call this ID and and add some additional.
Functions or something. So that\'s that\'s what this specific field is for. An author typically wouldn\'t use this. Again, we retain the value previously from here, so this value is here. Radius and kilometers, default central latitude and longitude. All this information again was provided to us, so that\'s.
That\'s why it was captured here in the component. The zoom sets the zoom level. We can see some examples outside of this map though, where something might be zoomed in more or zoomed out more. That is controlled by the zoom level on load and of course the user themselves would be able to change that.
By interacting with the controls as necessary. Um.

**Lisa Cardia** 35:40
And that\'s just like 1 digit values.

**Daniela Tea** 35:43
Yeah, go ahead.
So this can go up to 15.

**Lisa Cardia** 35:49
OK, so it\'s just like playing around to see what each one kind of means.

**Daniela Tea** 35:52
Yeah, mm-hmm.
Yeah, I think and so I think Lisa, the maps that we migrated over, they were set to what like very like it should look similar to like whatever was already existing. If I\'m not mistaken, I believe like we tried to.
Get the values migrated over correctly.

**Lisa Cardia** 36:12
OK.

**Daniela Tea** 36:13
Here we have the style JSON. So this is gonna change the way that the map looks. I believe we have. So this is kind of like the, you know, a certain style of the map. But if I\'m not mistaken for like the franchise map, that\'s like grayscale.
So you\'re able to essentially like use like Google development styles as you can see here to kind of like tailor the map to how you need. Keep in mind this is like this is from like Google, not necessarily like us. So this would be something that I guess would be established like what the different maps should look like and then you can update.
The style Jason. So again, I don\'t think anyone would expect an author to just type this up. This would be more of OK, this is what map style we\'re applying based off of like the Google dev styles and then that information can be populated here. You can also leave it blank.
And then this the map might look a little bit different. We can I can make a copy of this. We can see how that looks, but the reason why the map looks like this specifically is because of information that you can see here.
All right, map type. There are three different selections that you can make. In this case here, this is the default map. We also have the ability to view the map as the area guide, which is what hotels is using.
And the franchise map is what\'s used in the cafe franchise opportunities page, I believe where I would mention the whole grayscale map. So this this also has different criteria, interested, not interested. Area guide has points of interest and the defaults.
Of course has something slightly different from those as well. So we can we\'ll we\'re going to take a look at the different types of maps in some of these other tabs, enable map type control. That\'s where we have this on here, right? The zooming in, zooming out. So that determines whether or not you want to do that.
In some instances you you might not want them to zoom in and just see what\'s there without them, you know, being able to play around. So you might have a need to check that off. And then also side panel. This is going to be seen I think with the area guide specifically if you want to hide the side panel, the area guide.
You have the ability to. You can see right here it\'s checked and this is or is it?
Right now it\'s checked, but the side panel, the side panel from the area guide is is not visible here. Find your location is a different sort of side panel and we\'ll take a look how that is authored, but these specific fields here are going to be present on all the maps you would need to.
At the bare minimum, I think it would be important to have the latitude and longitude. You can see here though nothing is actually required. So like if you don\'t have the style JSON, doesn\'t matter. You\'ll still have a map displayed, it just won\'t be styled.
The zoom will probably default to a specific value. I believe 3 is the smallest that you can go, so adjust that as needed. But recommendation of course having the center latitude and longitude is probably a good idea to have as well as just making sure that you have the appropriate map type selected.
So this here default map and a quick peek at the area guide map. Here\'s an example on here. So this is an example of the area guide map which has the side panel here and the franchise map. I know that we have that down in the integral.
Environment. I want to be clear about this. The franchise map is specifically for cafes. However, in DPLT there is some information that\'s not being supplied that we would need to get from.
Hard Rock for I think it\'s interested. We need to get the interested information in order to be able to accurately display the map on the franchise map. Well, so we can see the map, but you won\'t see points on it until that information is provided to us.
So let\'s focus right now though on the default map and how we got it to look like this and then we\'ll switch back to the others.
So for our map data here, just going to go down, explore our locations, I clicked on the map data tab. So that\'s the section heading at the top. We also have our description. So here\'s our description from Boston to Brussels, etcetera.
Area guide header. This is actually specific to the area guide. You\'ll see sample area guide header is not actually listed here.
And that\'s because we are displaying the default map. So this value, even though it\'s being it\'s stored in this component, it\'s not actually being displayed since the default map was selected, not the area map. Here as I Scroll down to regions, we have our group title.
Of North America, let\'s see. And so we have our featured countries and our. So we have, sorry, we have a group title, the region that selected associate that group title and then featured countries. And Rick, this is what I wanted to call out because I think yesterday when we were talking about destination search and.
Filters the ability to be able to kind of show, you know, just specific countries. And so in this component here you\'ll see there is that featured countries text box where you\'re able to put whatever text that you need, United States, Mexico, Canada, and that\'s why that\'s displaying.
Versus all the countries within North America.
Alright, yeah. So you\'ll see other regions that were added here and the regions that were selected to appear underneath that group and then the future countries are going to be listed underneath that region. So all that is configured by the author.
You\'ll see this check box for hide other locations. So I believe there are instances where some locations are actually I I saw a folder in the content fragments for other. So it\'s just kind of hiding anything that\'s outside of whatever\'s here. So that way there\'s not like a second section.
Section that says other displaying here you\'re able to hide anything that\'s not from what you specifically called out. That\'s why this is checked. The location addresses here. This is related to the area guide. It\'s filled out in this case, but it\'s not going to display because area guide has.
This has not been selected, so if you were trying to find this on here, you won\'t see it, but we\'ll see how it is authored for area guide. So let\'s go now to markers.

**Lisa Cardia** 43:18
I\'m sorry, what was the filter map? That was nothing.

**Daniela Tea** 43:21
Yeah, so the filter map is not being used on this here. Let me check if it\'s being used in our area guide.
So it\'s not being used there too. So if you were to, I\'m just gonna show this here. If you needed to add like I think like you know like a additional hotel, cafe, casino, social gaming, sports book, online gaming, if you need to add specific filters that appear within.
Here you have that ability to do that. In the case of what we\'re seeing right now, I don\'t think this is, you know, I think these are just the locations that are showing. Let me actually go to the prod environment and see if that map has been configured slightly differently.

**Lisa Cardia** 44:08
OK, \'cause I\'m I\'m a bit confused if it\'s showing the three categories, but it\'s not in the filter.

**Daniela Tea** 44:14
Yeah, let\'s pull that up.
So I\'m going to oops.
Alright, so I am in prod right now. I\'m going to just increase this to desktop.
So the filter map is in prod. It\'s also not being used. We can make a copy of the map though, at least on a separate page and add the filter map functionality. I believe what it does though is it will add the specific filters.
To show up on the actual map, but we can take a look at that on the like outside of prod. I don\'t want to mess around with this prod map, yeah.

**Lisa Cardia** 45:07
Yeah, no, I don\'t wanna mess up prod. I\'m just still confused why filters are showing if we didn\'t, if they\'re not like listed there.

**Daniela Tea** 45:12
Yeah, I\'ll make a copy of the page in a moment and then we can we can start adding something to that so we can see how that works. All right. For markers, you can see here these are the different markers for the different lines of businesses, cafe, casino, hotels.
Live we have first section marker image which I believe is something that will be used in area guide default marker image and then the interested and open markers are used for franchising. If we take a look here we can see how that corresponds.
With what we had authored and then finally for search, filter and results we have our text search which is the Finder location portion here.
Alright, so find your location. Hang on one second.
Alright, find your location is here. Search placeholder, city, state or zip postal code. Search result count is 10. So if I were to say let\'s say Washington.
Alright, OK. Um.
So if I were to have, if I were to change this to say like one or something, then obviously this would be this will only show one location at a time. In this case I think the default was set to 10, so you should see 10. I don\'t know if there\'s maybe a specific keyword we can.
Try that might have multiple results. I don\'t know if cafe. OK, so that\'s not something. Baltimore. Yeah, I\'m not clear exactly what would be something that could show a ton of results so we can see how that works.
But by default I do believe it\'s set to 10. So for our button text search has been configured here. No results found for. So let me put some junk. No results found for is is the text.
Right here and then messages for no locations. OK, I think. Hang on. All right, all right. I believe Lisa, I can explain what the filter map does. So this portion here explore locations. This is connected to our map above.
So we saw how like some of these parts are being configured based on what was put in map data. Again, we saw these sections here is what\'s configured. We also saw that the regions are being added in this portion and that affects this stuff down here.
However, if you are, let\'s see.
Trying to see if I can show this.
Hmm, I need to find. I need to, yeah, let\'s go ahead and create that that image. I\'m sorry, that copy of this specific map to show. So what happens is you are actually able to filter some like if you filter things you can have it so it\'s connected to this portion.
So as you are searching for things, then this table should update to only show things that match your results. But let me take a copy of this right now. We can do that.

**Lisa Cardia** 48:37
Sorry, did we finish the I I feel like we\'re just jumping around a bit. Did we finish all of the fields like did OK, so message for no locations was just the I just I guess I don\'t understand the difference between no results and no location.

**Daniela Tea** 48:43
We did finish all the fields, yes.
Yeah, that\'s what I\'m trying to show you, because right now this is not how the map is set up. So I\'m making a copy so we can make some adjustments. OK, alright, so I\'ve made a copy of the page, yeah.

**Lucas Nelson** 49:02
Hey, did did Daniella Gonzalo\'s hands up? Just wanted to call it a.

**Daniela Tea** 49:05
OK, go ahead, Gonzal.
That\'s all. You wanna go ahead?

**Gonzalo Calasich (SHRSS)** 49:11
Hey, so hey Daniela. So something that we noticed in prod is that and you were showing the the the publishing page on prod, you see that the Central America is on top first and we tried to kind of reorganise that we needed to be North America region to be on top.
But when we we notice that when you go into the component, it shows the sorry, go ahead.
Yeah, you see how Central America, right?

**Daniela Tea** 49:39
Yeah, I see that. Mhm.
So I\'m in, yeah.

**Gonzalo Calasich (SHRSS)** 49:44
So, so we noticed that there is a missing part there. So I wonder if there is something we can.

**Daniela Tea** 49:52
One second.

**Gonzalo Calasich (SHRSS)** 49:53
Sure.

**Daniela Tea** 49:55
I\'m trying to find the location page here on prod alright.

**Gonzalo Calasich (SHRSS)** 50:05
Awesome.

**Daniela Tea** 50:07
All right.

**Gonzalo Calasich (SHRSS)** 50:08
So if you go to map map data you will see that you have this group titles and in the stage you will have the region selected and here when you click in one of those regions or drop down box nothing shows up. So I think that oh now it\'s showing up.

**Daniela Tea** 50:13
Mhm.

**Gonzalo Calasich (SHRSS)** 50:24
OK, cool. Let me try it. OK, my question is that then how you can sort this up? What\'s is is the order that you\'re seeing here or is is taking a different order because North America is first, but in the page is Central America.

**Daniela Tea** 50:37
Mhm.
Hmm, let\'s see. So I\'m not going to touch the prom page, so I made a copy. Yeah, yeah, let\'s let\'s go back to the local copy that I have. Let\'s see. OK, so this is my KT locations. And so let\'s, yeah, let\'s mess around with this one and I\'ll first I\'m going to.

**Gonzalo Calasich (SHRSS)** 50:46
That\'s fine.
Yeah.

**Daniela Tea** 50:59
Publish this page so I can actually see the map. So yeah, let\'s take a look at that.

**Gonzalo Calasich (SHRSS)** 51:03
Correct.
And my question will be how how you manipulate the order. That\'s my question, right?

**Daniela Tea** 51:09
Yeah, let\'s see if that dot the hard rock dot no. Oh yeah, it is dot stage.hardrock.com and then I\'m just going to go to slash KT locations.
So I can see my published age. OK, perfect. All right, let\'s see here.
OK, so I think.
I think, I think Gonzalo, when I took a when we took a look at what you had. So you said that regions was blank for you.
Is that like \'cause in your?

**Gonzalo Calasich (SHRSS)** 51:53
Correct. It was it was blank. I just saw in production there was nothing selected and now that you\'re in stage you see those North America, South America and the drop down was was not showing anything. Now that you went it\'s showing up. So maybe maybe whatever you deploy.
This last Monday maybe that have that I could have fixed it, so I will take a look on that.

**Daniela Tea** 52:16
I guess in terms of deployment, I think you\'re probably talking about the ACS Commons deployment. I my understanding is I don\'t think that is on production as of yet. Luke, correct me if I\'m it is, it is OK. Thank you. Sorry, I was mistaken.

**Gonzalo Calasich (SHRSS)** 52:24
Right.

**Lucas Nelson** 52:28
It is on production, Daniella.

**Daniela Tea** 52:33
I think Gonzalo, we would want to just make sure that the Google map component on that page you\'re saying now regions should like. I think we saw that there is a drop down making sure that that is authored properly. At least here we can see here in stage North America was the first one.
And then central and South, etc. So this is ordered as expected here down in the stage environment like this is matching what you would expect, correct?

**Gonzalo Calasich (SHRSS)** 52:59
Correct. So how, how, for example, I make Asia or like Europe be on top?

**Daniela Tea** 53:06
So if we were to grab, let\'s see, where is Europe? So Europe is this one right here. If we were to drag this up to the top and hit done and hit publish because again, remember we\'ve mentioned that the Google map.
You would not be able to see until that\'s like whitelisted. So this might need to have a cache broken because of the.
OK, so yeah, you can see I I broke the cache here and the Europe is at the top based off my configuration where I drag that group to the top on the map data tab.

**Gonzalo Calasich (SHRSS)** 54:06
OK, so in production, North America is on top, but it\'s showing up showing up at last. Should I wish? Should I just publish the pitch again?

**Daniela Tea** 54:11
Right, so.
I would say also I guess like the for regions though, let\'s take a look at your at what\'s on here. OK, so I I thought I saw that the regions thing is is blank. I mean you can certainly publish the page again with what you have, but I guess I would.
Want to make sure that you have all the authoring updates that you needed for the region section first.

**Gonzalo Calasich (SHRSS)** 54:39
And something interesting in production. When you select the region dropdowns, it worked for you, but I tested again and it does not work for me. Maybe maybe it could be something else.

**Daniela Tea** 54:47
OK, let\'s take a look at that.
So I\'m in, I\'m in prod and I\'m gonna go to sites and SHRSS, corporate, Hardrock, English and location. All right, edit.

**Gonzalo Calasich (SHRSS)** 54:53
Uh.

**Daniela Tea** 55:06
And opening up the map component, opening up map data and clicking on region and you\'re saying that this is not working for you.

**Gonzalo Calasich (SHRSS)** 55:14
Yeah, it does not work for me. It\'s it shows up empty.

**Daniela Tea** 55:19
Hmm.

**Gonzalo Calasich (SHRSS)** 55:22
And I can I can share my screen if you want to.

**Daniela Tea** 55:22
Um.
I think, yeah, we\'ll do that really quickly and then we can, I can extract this portion of the recording to show our dev team just to take a look at that. And I think Gonzalo, what browser are you using? Chrome.

**Gonzalo Calasich (SHRSS)** 55:37
It\'s a it\'s a Chromium based browser. It\'s the one that we use in the company. So we have a prod for example, right? And this is the locations page and this is the Google map and we are in the map data and if I click region it\'s just submit.
Which I found interesting and that\'s why you know if you if you see a stage you will have like a region selected you know multi multi list as options here below because they have been selected but here none of this must work and the order you know I thought there was something else because this is this is not.

**Daniela Tea** 55:56
OK.
Uh huh.

**Gonzalo Calasich (SHRSS)** 56:15
Checking in place, uh, automatically, right?

**Daniela Tea** 56:19
So sorry, you said.

**Gonzalo Calasich (SHRSS)** 56:21
So for example, as you I just saw there, North America is is on top, but when you come here.

**Daniela Tea** 56:31
OK, yeah, so I I just, I checked when this page was last published. When did you make that change to put North America on top?

**Gonzalo Calasich (SHRSS)** 56:32
Essential America, I am.
No, no, that no, we we don\'t. We no, actually what happens is that North America was on top at some moment and then somebody came say, hey, somebody moved this thing to to the bottom. So we came here and we saw that no, it\'s on the top.

**Daniela Tea** 56:42
Was that like?

**Gonzalo Calasich (SHRSS)** 56:58
But we and then we haven\'t touched it because we we noticed that, you know, nothing we we do it, it will make a change, right. So we didn\'t know how to use this. That\'s why we didn\'t touch it.

**Daniela Tea** 57:12
OK, so I think we\'ve seen regards to spread. I guess my question is, are you able to use this in Chrome or something? I\'m just curious.

**Gonzalo Calasich (SHRSS)** 57:24
I will have to ask somebody else that doesn\'t have a Windows, but I yeah.

**Daniela Tea** 57:27
Oh, OK.

**Lisa Cardia** 57:28
You you can ask. You can ask me, Gonzalo, if you want on the side and I can try it on my Mac.

**Gonzalo Calasich (SHRSS)** 57:33
Sure.
OK. Thank you, Lisa. Yeah. And that was that\'s that was pretty much my question. Thank you. Let me stop sharing.

**Lisa Cardia** 57:35
No problem.

**Daniela Tea** 57:41
Yeah, no, thanks, Gonzalo. Yeah, no, we\'ll we\'ll if I think, Lisa, if you can get back to us on if you\'re able to see the same functionality that I was showing where the drop down works and you\'re able to select things, that sort of stuff, that would be helpful for our team to understand what\'s going on.
Um.

**Lisa Cardia** 57:58
Yeah, I would say we truthfully haven\'t touched the component and that\'s the way it was migrated over. So it\'s like it\'s correct on the back end, but not displaying correctly on the front end. And it was just brought to our attention. Why was it at the bottom? So when they looked into it, they\'re like, well, we can\'t fix it because it looks fixed.
Besides it not displaying correctly, so no one went in and like changed the area of it.

**Daniela Tea** 58:18
I think.
Right, but I think what what I\'m concerned with is the fact that Gonzalez I have been able to access the region drop down. That is, I\'m not really clear as to why that would be the case when I\'m able to demonstrate it in my Chrome browser that reordering things will show when it\'s published as well as being able to.

**Gonzalo Calasich (SHRSS)** 58:29
Yes.

**Daniela Tea** 58:40
Select things from the drop down. So since I don\'t, I think you said Gonzal, that\'s like the browser that you guys use over at Hard Rock, is that right? So like I wouldn\'t be able to replicate that issue.

**Gonzalo Calasich (SHRSS)** 58:52
Correct. It\'s an Iceland, but it\'s it\'s it\'s chromium based, so it\'s kind of like very similar to Chrome.
Right. And no, and The thing is that it works on stage, correct. And if I go to a stage, I can see the drop down working finally correctly. So in stage it works fine, but in production does not work and that that was what I was trying to bring it up.

**Lisa Cardia** 59:01
I mean this is the location, correct?

**Daniela Tea** 59:09
OK, so so.
Uh, OK. Thank you for that. So stage everything works as expected. Sorry.

**Lisa Cardia** 59:17
And that\'s, so I\'m going to go into it now.
I\'m gonna try right right now for Gonzalo just so that we can say so I\'m on prod and I\'m on the locations page and then I need to go to the the future locations. Is that the?
How do I get to that exact component?

**Gonzalo Calasich (SHRSS)** 59:42
Just locations. Locations. Hard Rock Corporate. Hard Rock. No, sorry, Hard Rock Corp.

**Lisa Cardia** 59:51
Yeah, I\'m on corporate Hard Rock locations English page, but which part am I opening up right now?

**Gonzalo Calasich (SHRSS)** 59:51
Corporate.
Decides and select the.

**Lisa Cardia** 59:58
Am I opening the the Google map or this is the?

**Gonzalo Calasich (SHRSS)** 1:00:00
Let me share.
Let me share.
So when you are in this page and locations right and you select this one and you can click in this one.

**Lisa Cardia** 1:00:14
You\'re on the Google map. Yep.

**Gonzalo Calasich (SHRSS)** 1:00:16
Yep, enable map and click here and just you know.

**Lisa Cardia** 1:00:22
Yes. So North North America is the first region showing in prod. I\'m on my Mac and I\'m on regular Chrome.

**Gonzalo Calasich (SHRSS)** 1:00:22
Selected.
And and does this region drop down box works with you that does it shows multiple values?

**Lisa Cardia** 1:00:40
No, I can\'t see anything.

**Gonzalo Calasich (SHRSS)** 1:00:42
OK, maybe you can share really quick so.

**Lisa Cardia** 1:00:45
Yeah, I I have the same. I have the same experience as you. I can\'t. I can\'t view it. I\'ll share my screen, but.

**Gonzalo Calasich (SHRSS)** 1:00:45
Because for.

**Lisa Cardia** 1:00:54
It\'s blank.
And I\'m in prod, and I\'m in Chrome.

**Gonzalo Calasich (SHRSS)** 1:00:57
Thank you.

**Daniela Tea** 1:01:01
OK. All right. Yeah. So this is exactly what we wanted to confirm because I\'m in prod, I\'m in Chrome. The drop down does display for me. So trying to isolate if this is so since Lisa is also in prod, I\'m sorry, since Lisa is also in Chrome.

**Lisa Cardia** 1:01:03
OK.

**Daniela Tea** 1:01:19
No, it clearly is not a browser issue. So this is, yeah, I was gonna say we\'ll we\'ll ask, we\'ll ask our tech team to take a look at how this is. We\'ll see if we can try to replicate it, but.

**Lucas Nelson** 1:01:22
We\'ll get Vinay to look at it, Daniella.

**Gonzalo Calasich (SHRSS)** 1:01:33
Thank you.

**Lisa Cardia** 1:01:34
And my question too with this component in general, if we want to use it somewhere else, who configures all of those initial metrics? Because like any content author could want a map on their page since it\'s available, but we don\'t have all of the JSON JavaScript.

**Daniela Tea** 1:01:34
The fact that.

**Lisa Cardia** 1:01:52
Details, latitude, longitude, all of that. So that\'s not pre-populated. So who configures this for us then? IT like if we\'re like we need a map, they do it. We can\'t do it as authors.

**Daniela Tea** 1:01:59
No, it\'s not.
I think who would have, who would typically have that information right now was my question.

**Kerry Holyoak (SHRSS)** 1:02:09
So longitude latitude for locations comes from the DPLT.

**Daniela Tea** 1:02:16
So Carrie, to be clear, for this specific map, like you know it\'s not necessarily I I think we\'s are you asking like showing a point on a map or are you asking for showing like a location on a map or?

**Lisa Cardia** 1:02:28
I\'m sorry, my my connection must be poor, so it\'s cutting out, but basically every single field on that map component required some sort of knowledge base that we would not have.

**Daniela Tea** 1:02:32
OK.
Right. So I guess my question is currently right now how are you guys authoring the maps? So like this like where would this like who we got this information from migrating over the page? Who would typically provide this information?

Lyon, Rick (Director of Digital Experience)** 1:02:58
Well, I used to do it, but now everything\'s from the DPLT.

**Mayte Eme** 1:03:03
Oh, to Kerry\'s point.

Lyon, Rick (Director of Digital Experience)** 1:03:04
So whoever said no, I think Finance Finance usually sets it up in DPLT.

**Mayte Eme** 1:03:09
So yes, and to Kerry\'s point, if we have that in the DPLT, we expect all those values to come from the DPLT.

**Daniela Tea** 1:03:16
So this is the default center latitude and longitude. This is saying this is what I want the map to show. This is not saying show me the specific location right? So like in this case here we\'re showing like when I refresh the page it\'s showing the center of the map is these two points.
Right. So this is just say, oh, I want the map to be focused on this area. I want the zoom to be at this level. All these locations here, like you guys are saying all of this is stored in DPLT, right? These locations are coming up for DPLT.

**Lisa Cardia** 1:03:46
I think my my confusion is, my confusion is if you add this Google map to a page right now, every single field of this element ID, kilometers, all of that is blank. So even if we\'re getting the right locations getting pulled in, I don\'t even know how to configure the map from start to finish who.

**Mayte Eme** 1:03:46
OK.

**Daniela Tea** 1:03:52
Mhm.
Yes.

**Lisa Cardia** 1:04:05
Do I lean on for that?

**Mayte Eme** 1:04:11
I would say, Lisa, at this point, and I\'m sorry, Kerry, I\'m just saying since we see the gap, it\'s a gap. We\'ll just have to put a ticket, right? And then we\'ll rely on it to set it up correctly.

**Kerry Holyoak (SHRSS)** 1:04:11
OK, but let me let me just see. Hold on.
Well, hold on. I think it\'s a different. I think it\'s a different answer though, because if if what you\'re trying to do is set a view. So my apologies, I misunderstood. I thought we were mapping a location, but if we\'re trying to set a viewpoint, then why don\'t you just reference Google in maps.google.com where you\'re trying to get to? You can get your longitude and latitude from there.

**Lisa Cardia** 1:04:43
That that\'s two fields though this is.

**Mayte Eme** 1:04:43
Right, but you gotta remember the type of content authors that we have, Carrie. We\'re not gonna be asking content authors to do all these settings and setups. They shouldn\'t have to.

Lyon, Rick (Director of Digital Experience)** 1:04:52
And I don\'t think that counts for the Uh JSOM.

**Lisa Cardia** 1:04:55
Yeah, exactly. Every field is blank when you add this to a page.

**Kerry Holyoak (SHRSS)** 1:04:56
Oh, OK.

**Mayte Eme** 1:04:57
Yeah.

Lyon, Rick (Director of Digital Experience)** 1:04:58
Yeah.

**Kerry Holyoak (SHRSS)** 1:05:00
Hmm, it\'s there\'s. But Rick, you were doing it before you were the one adding the content or the the parameters before.

Lyon, Rick (Director of Digital Experience)** 1:05:07
Yeah, I didn\'t do the JSON though, but that was all back and it was just the map was already set up. I went out of location and I know it appeared on the map.

**Kerry Holyoak (SHRSS)** 1:05:10
Oh, I see. OK.
Oh, I see. OK.

**Lisa Cardia** 1:05:16
Yeah, so that\'s what I\'m saying is how do we get this in a place where I can just add the map and all I need to do is determine the locations that need to filter in, not actually configure the entire map.

**Kerry Holyoak (SHRSS)** 1:05:18
Yeah.
Gotcha.

**Mayte Eme** 1:05:27
We are going to have to redo this component and or enhance it, I should say, and until then we\'ll rely it on our IT support to set it up whenever we add a new one.

**Lisa Cardia** 1:05:39
OK.
Thank you.

**Daniela Tea** 1:05:41
So yeah, I do want to also call out and this is not, this is not saying oh this will cover a gap or anything, but one thing to keep in mind is you know the ability to copy like a component from an existing page.
To your new page. So like I made a copy of this specific component, it has all the values already in place and I can even see it when I published my page to the stage server. So like if you\'re trying the what I\'m saying is if you\'re trying to make a map that looks very similar to what you already have, you can do that and have all those.
values in place and then you can change like your map data fields here for the sections that are configurable, right? If you need to only, yeah.

**Lisa Cardia** 1:06:27
And Daniella, I\'ve had trouble doing that, copying components across pages. It like doesn\'t recognize my copy from one page to the next. It\'ll just remember the copy from that page I\'m on. So how how what\'s the solution?

**Edwin Aquino** 1:06:40
I\'ve noticed that as well, but I noticed it as well. In order to fix it, I had to refresh the page in order to get it to register it correctly. I don\'t know why it keeps doing that.

**Lisa Cardia** 1:06:42
Yeah.
Yeah, it doesn\'t remember your last copy, but rather the page you\'re on\'s last copy.
So if you copied it from this location page and decided to put it on the home page, if I\'m working on the home page and click paste, it\'s just gonna copy and paste something else from the actual home page, not this page, but to Edwin\'s page, it\'s a refresh.

**Daniela Tea** 1:07:08
So I.

**Edwin Aquino** 1:07:11
Yeah, I\'ve noticed that I had to refresh the page that I was on in order for it to actually like register that I copied something from a different page. Um.
That\'s something that I\'ve noticed I had to do for like a workaround, but shouldn\'t really be happening.

**Lisa Cardia** 1:07:34
Is that something we should like call out as like maybe a possible defect if it\'s not recognizing it without a refresh? Or is it something your team can look into? It just it\'s it was happening a lot when I was working on the campaign page. I really wanted to just add a convenience copy from other pages.
So.
And they wouldn\'t copy from page to page, but just on the same page level.

**Daniela Tea** 1:07:56
Yeah, so um.
That sounds to me more that would be more like a product issue or defect or something. So that would not necessarily be our team. So Ed, when you\'re saying though it does work, however, you have to refresh the page so we can we can certainly look into if that\'s something that\'s worth having a support ticket open.
And I guess, I guess I would want to understand like exactly what you guys are doing to see it. You\'re saying you have another page open, you\'re trying to copy this from there to there. And when you\'re saying it would work if you were to refresh the page in the other browser and then try to paste it again, is that correct?

**Edwin Aquino** 1:08:34
Yeah, that\'s what I\'ve noticed happening. I I I believe you had the same issue during one of our enablements as well when you were trying to copy something and it wasn\'t working for you.

**Daniela Tea** 1:08:42
OK, and did I probably automatically refresh the page without even thinking twice \'cause that\'s \'cause that\'s.

**Edwin Aquino** 1:08:47
No, no, actually I I don\'t think we figured it out at the end, but I I was able to test it on my own and that\'s what caused the resolution.

**Daniela Tea** 1:08:56
OK, well I would say so here\'s here\'s some options. You should be able to copy from page to page. If there are issues with that, yes, we can certainly see about getting the product team to identify what could be the cause for that.
The second thing is making a copy of the page where the configuration is set up already, right? The point is though, I understand this is not going to cover entirely the gap of what you guys need, where certain fields maybe should be pre-populated already, however.
If copying the component, if you\'re able to do that, then that should have all the fields that you need with the ability to change the fields that might need to change, right? So I just want to make sure that that\'s also something that the team is aware of that if you guys have identified this is how all the maps should be default.
Yes, ideally there will be default values in place and that could be handled through a code deployment with some development updates to the component. But for the time being you are supposed to be able to copy a component from one page to another and it should retain the values that have been set here in the configuration window.

**Lisa Cardia** 1:10:10
I would say 99 percent, 99 times out of 100 it doesn\'t work without a refresh. So I don\'t know if that\'s like a platform defect or I I don\'t. I just don\'t think it\'s like user error at that point.

**Edwin Aquino** 1:10:16
Agreed.

**Lisa Cardia** 1:10:26
Because if you copy something so much and then it just doesn\'t.

**Daniela Tea** 1:10:27
Right.

**Lisa Cardia** 1:10:31
So I don\'t.

**Daniela Tea** 1:10:31
Yeah, so oh, I was just gonna say, um, hey, Andy, are you on the line?

**Edwin Aquino** 1:10:37
Yep, I\'m here.

**Andy Lambert** 1:10:47
Yep.

**Daniela Tea** 1:10:47
Just wanna make sure that I had your ears perked up. That\'s all.

**Andy Lambert** 1:10:51
Oh, I\'m I\'m dragging.

**Daniela Tea** 1:10:52
Thank you. Appreciate it. All right. Um, OK.
All right, so I want to take a look at some other map types, in particular the area guide to see how that is being configured. I\'m moving on to the hotel page for San Diego, since this is typically where I believe area guides are are mostly used.

1:10:58
No.

**Daniela Tea** 1:11:15
We see we have the Google map component on the San Diego page and I\'m going to open up what that looks like on stage so you can see how that\'s configured. If I can find it, where is it?
There it is. OK, alright.
OK, OK, so for our Google map component displaying the area guide, you can see the values that were in place here and how it looks like on the right.
And instead of having default checked, area guide has been checked instead and so that displays the map a little differently with the sidebar in place. You\'ll also notice the style Jason field is blank and this map does look a little bit different from what we had on the Hard Rock website with the style.
In place and so again style JSON that is like Google development standards and such. Leaving it blank is perfectly fine. However, keeping in mind that the map will look more something like this versus whatever was established for the Hard Rock website.
Clicking on map data, we\'ll see our area guide. This is the section heading portion. No description has been set. Our sorry the our area guide section heading is actually what would be displayed if this map was default. You\'ll see that there\'s no location list.
Underneath like we saw on the Hard Rock site. So this title here maps to the section heading here, but the area guide heading here is what gets displayed.
Right here OI know that seems a little confusing. There\'s a value here, but it\'s not actually being used even though the value\'s exactly the same. If I were to remove this and hit done.
And I published this page.
Then this should look exactly the same because that value is not actually being displayed when this area guide is being used.
So I\'m going to break the cache so we can make sure it is there and we\'ll continue to make changes as we configure this to see what happens. All right, filter map. I made a copy of that map. We\'re going to mess around that in a second. And regions. We saw how regions works when reviewing the map as the default.
Fault map like we saw on the Hard Rock website. This is not needed for the area guide, but what is needed is the location addresses. So as I\'m scrolling down here you\'ll see there are several fields. We have a section.
Called attractions. This is called attractions, right? And we\'re saying section ID is section two. You have 5 different sections that you can add to your area map. And so I\'m saying I want this to be with the second attract. Sorry, the second section is going to contain these items.
So you have the location name as well as the latitude and longitude of each of those locations and the full address. So you can see that gets displayed here within these little tool tips. And then if there is a specific URL that needs to be added for like view with this visit site that me added.
Added here within the URL section, so I\'m going to Scroll down, but you can see the attractions here, how they are mapping to what we have configured. If I keep going we see museums is Section 3. So we have our museums here.
OK. And then we have universities, which universities and we have arenas and stadiums.
Arenas and stadiums. So this here locations. All these locations are what populates the map for the locations of interest as well as the sidebar, specifically when the area guide map has been selected under map controls.

**Lisa Cardia** 1:15:28
Sorry, where did the visit site and get directions get pulled from?

**Daniela Tea** 1:15:31
So visit site and get directions are let\'s see here. OK, so visit site is supposed to be like whatever you\'ve put in the URL, right? So this is San Diego. San Diego. Oh, the text.

**Lisa Cardia** 1:15:45
So we can\'t change that first call to action, yeah.

**Daniela Tea** 1:15:48
That you\'re talking about the text here. Yeah, so the text doesn\'t do that. That\'s not configurable, I don\'t believe, but the values like the hrefs for these are determined based off of what you put in the URL and get directions I believe takes the latitude and longitude and then launches Google Maps.

**Lisa Cardia** 1:15:54
OK.

**Daniela Tea** 1:16:12
Second.
Yeah, so.
Let\'s see here.

**Lisa Cardia** 1:16:19
And what about the get directions? That\'s like in the full address description.

**Daniela Tea** 1:16:24
In the full after this, you\'re talking about where?

**Lisa Cardia** 1:16:27
In all of the descriptions for those locations it says get directions like hyperlinked.

**Daniela Tea** 1:16:32
Oh, I see that. Yeah, so looks like in the actual full address someone had put this here, so that\'s why that\'s appearing in in this. Like it is actually a hyperlink. You can see that, but this should be removed. This would likely be removed and then migrate that URL over to the URL section.

**Lisa Cardia** 1:16:43
Well.
Yeah.
OK.

**Daniela Tea** 1:16:53
1.
All right, let\'s see. We have our markers here. In this case, the marker that\'s being used is this. This is the first section marker, the all these locations.
While they I know that we had set the casino marker to this color, I believe that this is defaulting to that because we are on the hotel theme. Essentially that\'s why this color is being used so.
That the markers are typically that\'s that\'s something that you\'re really going to to utilize on the default location map, but the points of interest are all going to essentially be the same marker. And then finally the search filter and results. Again, while this is this is filled out, this is only something that\'s.
Used with the Google map that\'s on the this portion, this specific map, not the area guide. So we can certainly, you know, disable this. I\'m going to actually do that right now. I\'m showing that we can disable some of these items when you\'re viewing things in an area guide it and.
It doesn\'t affect it, like you could fill it out, but you it doesn\'t actually affect the map. The important part for an area guide map is filling out the area guide header and the location addresses and then also making sure that the area guide map type has been.
And selected.
Alright, um, let me close up this.
OK, so that\'s a lot for the map. I want to go back though to our copy of the page.
So my KT locations page and let\'s go ahead and.

**Lisa Cardia** 1:18:50
I guess like this is the reason why I have so many questions is that we actually have a very relevant request from the hotel teams to get an area guide map on both the reverb websites, Hamburg and Atlanta to to create that there is no existing so I don\'t know what values.

**Daniela Tea** 1:18:58
Mhm.
Mhm.
Mm.

**Lisa Cardia** 1:19:10
Input to get the map right. And also I guess we want to confirm 100% that this can be reused on that reverb theme, of course, knowing that we\'re going to make something very similar to that area guide we just saw with all of those locations.

**Daniela Tea** 1:19:17
Mhm.
Right. So I think what you\'re describing though, but so to confirm, you\'re saying like for example for you said for hotels, like would it be kind of like this, but like you would want to just.

**Lisa Cardia** 1:19:35
No, we\'re we\'re we\'re gonna do the area area guide map. Yeah. So we\'re trying to replicate this for Atlanta reverb and Hamburg reverb, but we don\'t have an existing. So it\'s like, what\'s the starting point to get this map configured?

**Daniela Tea** 1:19:38
Oh, the area guide. OK, I see. I see.
Mhm.
And a rebirth.

**Lisa Cardia** 1:19:52
And then add the locations that we need that are relevant to those areas.

**Daniela Tea** 1:19:55
Mhm.
OK, let\'s try to do that right now actually. All right, let\'s see. So I know I made my page and I know that I made a copy. But before we actually, before we get into that, Lisa, I know you wanted to you had some questions about what filter map does.

**Lisa Cardia** 1:20:14
Yes.

**Daniela Tea** 1:20:14
Um, so let\'s let\'s actually do that really quickly first, OK?
My cafes test and then also let\'s say hotels singing. All right, I\'m going to hit done. So I\'ve added two filters and I\'m going to publish this page and then we\'re going to refresh our KT locations page.
And then I will break cache if needed.
OK, so do you see how this got updated?
It.

**Lisa Cardia** 1:20:51
Yes.

**Daniela Tea** 1:20:51
Cafes test. OK, yeah. So previously nothing was set. So it\'s going to show, I think, you know, everything that you want if if you. That\'s correct, yes. So that\'s why it was.

**Lisa Cardia** 1:21:00
So this overrides it. I guess my question is though, if you\'re making your own filters, how? OK, because the types are hard coded. I was going to say how is it smart enough? OK, so this is the only filtering you\'d use to override to not just show the three LOBS, otherwise we\'d.

**Daniela Tea** 1:21:10
Yes, the type. That\'s correct, yes.

**Lisa Cardia** 1:21:19
Have to use this if we wanted it to be more or less.

**Daniela Tea** 1:21:23
And also because keep in mind if I don\'t have anything, it\'s going to default to certain values. So if you want the values to say like instead of cafes, maybe you want to say something else. I don\'t know what you might need, but like keep in mind that value also changes, right? So like by default when we did not have this present and I and so now it\'s empty.

**Lisa Cardia** 1:21:24
OK.

**Daniela Tea** 1:21:43
Right, and I\'m going to publish the.
And let\'s refresh it. It might take a second.
Strike the cache.
OK, yeah, so by default the all fragments in DPLT and such as cafe, hotel and casino, these are the default label names as well. So if you wanted to still show cafe, hotel and casino, you could do that. But if you wanted different labels, you could certainly put whatever label it is you want here and over.
Write it in this filter map section.

**Lisa Cardia** 1:22:20
OK. So I think just the important call out is that that\'s being that\'s needed to override is really the the answer.

**Daniela Tea** 1:22:26
Yes.
While we\'re here because we\'re this is our copy of our map, I\'m going to remove this style Jason and we can see what happens.
I\'m going to publish the page.
And.
OK, so cache is still not broken. You can see what that looks like though.
Uh, actually let\'s make another update and push that through. Um, so.

**Lisa Cardia** 1:23:03
So to be clear, the the whitelist issue is in the authoring environment, but if we view as published, we should be able to see it or that\'s still gonna give us an issue.

**Daniela Tea** 1:23:06
Mhm.
No, that\'s that\'s still the whitelist issue is for the authoring environment entirely, whether it\'s view as published or not. So you can see here you will not be able to see the map until this is whitelisted.

**Lisa Cardia** 1:23:23
OK, I\'d say that\'s critical then for SHRSS since we need to use this component this week to be able to to view this.

**Daniela Tea** 1:23:27
Mhm.
Hmm.

**Lisa Cardia** 1:23:39
Is anyone taking away?

**Daniela Tea** 1:23:43
I guess Lisa, is there anyone on the call who would be able to take that as an action item or?
Is that?

**Mayte Eme** 1:23:56
Hey, I\'m sorry if I missed the Lisa. I\'m I\'m in two calls with the Ottawa stuff going on. Are you planning to use this component for the landing pages because?

1:23:56
Well, no one\'s.

**Lisa Cardia** 1:23:56
If someone could just, yeah.
Yes, so.
We.
Yes, we would. We would at least hope that it could be utilized for reverb. But the problem is we can\'t, we can\'t even test it and put in the locations because we can\'t view it and author it.

**Mayte Eme** 1:24:09
It doesn\'t seem like it\'s working.
I wouldn\'t use it. Yeah, I I wouldn\'t use it. Let\'s go with a plan that we had and maybe when we figured out how this works so it gets fixed, we can, you know, enhance the page.

**Daniela Tea** 1:24:22
It.

**Lisa Cardia** 1:24:30
OK.

**Daniela Tea** 1:24:32
So to be clear, and I think my team probably misses at the beginning, the reason why you\'re seeing oops, something went wrong is because the author environments are not whitelisted. So that\'s A and that\'s managed by SHRSITI believe, right?

**Lisa Cardia** 1:24:32
Understood.

**Mayte Eme** 1:24:40
Oh.
OK.
Not the first time I\'ve seen issues because I\'m hoping I\'m going to take a note to remind Scott when you guys send your e-mail, I\'ll probably you\'ll see my reply just following up on him to help us get this going. So just to make sure I get it right, why listing which environment?

**Daniela Tea** 1:24:58
OK, OK.

**Mayte Eme** 1:25:03
Why?

**Daniela Tea** 1:25:03
Oh, for for actually all the author environments.

**Mayte Eme** 1:25:06
I\'m listening. Really. OK.

**Daniela Tea** 1:25:09
Yeah, the only the published on the publisher side is that those domains were whitelisted, but the author says that\'s a different domain that was not whitelisted. Yep.

**Mayte Eme** 1:25:20
Thank you.

**Daniela Tea** 1:25:22
Yeah. OK. So I think, Lisa, you said you wanted to. I just want to understand what you\'re trying to set up in reverb really quickly. We can take a look at that, how that works with the Google map, OK.

**Lisa Cardia** 1:25:35
Yeah, it\'s not. It seems like we we probably won\'t use it for this week, but the intention is to add a Google map with different locations that are relevant to Atlanta, different locations that are relevant to Hamburg. But again, just to add the component to the page will mean all of the fields are blank.

**Daniela Tea** 1:25:48
Um.

**Lisa Cardia** 1:25:53
So there\'s not really like a starting point for us to get to us to just have to add, you know, the Coca-Cola Museum for Atlanta or whatever location, Piedmont Park. We can\'t just add those locations because the the map first needs.
You know, configuring.

**Daniela Tea** 1:26:12
So I have a couple suggestions for that. So let\'s see here. So for example, when we were taking a look at San Diego, yeah. So like you would want it to look something like this, yes. Yeah.

**Lisa Cardia** 1:26:28
Yes, just to the reverb theme, it\'s just to make sure that the property is, you know, reverb Atlanta and then and then the nearby attractions are new ones. So like this is a brand new content but using existing functionality.

**Daniela Tea** 1:26:36
Great. Okay.
Yeah. So I guess my question is in terms of adding this for reverb, you know, so you can take a look and see how this one was configured. The default center latitude and the longitude would be whatever you need, like where those locations are for reverb on Atlanta and Hamburg.
The map data is all the information that you said you needed to show here in the sidebar. So like anything that\'s relevant to reverb, Atlanta and Hamburg. So that you know those are be all fields that you would be wanting to fill out anyway. The markers, I believe they should already be added. If not, this is.

**Lisa Cardia** 1:27:18
Mhm.

**Daniela Tea** 1:27:24
Something that is just chosen from the dam and then for the search filter results as as I mentioned earlier, this is not needed for the area guide, so this one could certainly be left blank. This is not needed. It\'s really just the map data here.
As the areas of interest and then.

**Lisa Cardia** 1:27:40
So is that theme though configured for like the markers? Like I don\'t think I saw anything reverb colors.

**Daniela Tea** 1:27:48
So we can. Let\'s see here. So the first section marker image is what was displayed here. Yeah, so this here I would imagine you\'d probably want to put like the reverb icon or something, right?

**Lisa Cardia** 1:28:06
Yes.

**Daniela Tea** 1:28:06
Yeah, so I think you should like you should be able to replace this in this field.

**Lisa Cardia** 1:28:10
Is there certain certain dimension? Like where did these icons come from? Like how would we add a new one? Would we need to get an actual like icon designed and then make sure it\'s the right aspects or?

**Daniela Tea** 1:28:22
So.
So looking here, sorry, something just popped up from teams. Looking here we thank you, thank you. We can see this is located. There\'s a section called marker on and within the dam and that\'s where the specific image is.

**Mayte Eme** 1:28:30
I got him, Daniella.

**Lisa Cardia** 1:28:42
Mhm.

**Daniela Tea** 1:28:42
So you know, in terms of having something similarly, like I guess I would take a look at what this folder was. So these are where all those markers were located 50 by 50 or something. So these I think were probably, I don\'t know if these were necessarily provided to us perhaps or if these were carried.
Over and migrated from the original site. I can\'t remember an answer for that one, but this is a specific folder that was within assets and that\'s just what we\'re referencing. But if you have something else, you can certainly upload it either to here or whatever. I guess Don has specified it within the DM would be appropriate for icons like these.

**Lisa Cardia** 1:29:12
King.

**Daniela Tea** 1:29:21
And then you would just configure the component to be able to replace like what we see here with what you need, right? So.

**Lisa Cardia** 1:29:30
OK. So so we would say like currently not one. Go ahead, Don.

**Don Middlebrook** 1:29:30
Yeah, I think those were.
I think those were migrated over, but we can set up another directory for website elements.

**Daniela Tea** 1:29:36
OK, OK, got it.

**Don Middlebrook** 1:29:43
For these type things.

**Lisa Cardia** 1:29:45
OK. I\'m just, you know, trying to think ahead of we would need one specific to reverb that can\'t use the Hard Rock Hotels logo and then all of the markers we would want to be the reverb theme colors. So not sure how we go about getting that marker and then also just making sure this map.

**Don Middlebrook** 1:29:53
Right.

**Lisa Cardia** 1:30:04
I don\'t know, does the map have like a dark version so that it\'s not, you know, huge contrast against that it I do that.

**Daniela Tea** 1:30:09
So that would, yeah, that would be controlled by the style JSON, which again would be coming from like like Google, like the Google develop map development site, right? So like what we had here, this is not something.
That like our team wrote. I believe this was something that was provided to us for like what the exact style of the map should be. So and I understand like like you\'re saying an author wouldn\'t know. Oh, I need to add, yeah.

**Lisa Cardia** 1:30:32
OK.
Exactly. That\'s why it\'s like I I\'m finding it difficult to like place a map on there where we just don\'t add the the locations instead of having to configure the entire thing. So we\'ll have to meet internally.

**Daniela Tea** 1:30:50
OK.

**Lisa Cardia** 1:30:51
Thank you.

**Daniela Tea** 1:30:52
Yeah. Um, all right.

**Lisa Cardia** 1:30:52
Thank you.
So I don\'t think you need to go into reverb then, knowing we don\'t have the right markers or anything of that nature. We\'re gonna have to figure out how it looks and works.

**Daniela Tea** 1:31:06
Yeah, and just just just to confirm though, making sure that the area guides specifically since it seems like that\'s the type of map that you want. Those fields again are the area guide header and the regions field and setting the map controls map type to area guide is what\'s needed to display it.
Like this?

**Lisa Cardia** 1:31:27
Yes.

**Daniela Tea** 1:31:27
Yep. OK. All right, let\'s see here. I\'m taking a look at time.
And I also want to make sure that I have the agenda up so I see what other components we are taking a look at today. I believe the other one I did want to show is location list. Um.
So as we saw previously with the Google map on this view, there\'s our Google map component on this view. We have this explore our location section that is a list of the locations from above. However, I think that there was.
And ask at some point to be able to separate out the map from that.
So if I were to open up this location list page that is here down in stage on this, there\'s a component called location list and so it\'s essentially like the bottom portion of this map. However, it is a different component and I did want to call out that.
This specific component does not have the featured countries section, I think. So that means for the destination filters and the location list, it sounds like that\'s something that is desired to be able to have that override.
Text field to be able to say what country should display. So you\'ll see here this is that\'s why it\'s listing everything based off of the region I selected. So if that\'s desired, that would certainly be something I would recommend noting down to have the similar functionality to what\'s captured here within the Google map.
Map component, but the purpose of the location list was to essentially separate out the map from the bottom portion of this component in case this is needed to be displayed on a page without needing a map at the top.
OK, so configuration wise again looks pretty similar to what we saw for the regions, but the.
Um, the biggest thing is just that there\'s no map at the very top. That\'s all.
Alright, OK.
OK, so.
I know that there was a lot that was covered today and I know that there\'s going to be a lot of questions, particularly with probably the map component, but I did want to go back to our locations content fragment and just make sure that we had an understanding.
As to what these fields were and particularly the ones that were authorable versus the ones that are on disabled and coming in from DPLTI think I saw a question yesterday.
Asking about the ability to, if I\'m not mistaken, was the ability to ask to add a location that\'s not from DPLT. Let me check if that was. I feel like I read that question so to to be clear.
Since these are required fields and these are expected to be coming from DPLT, you would not be able to do what\'s being described. Our understanding was that DPLT was supposed to be a source of truth, and so that\'s why essentially these were made read only and these were required since it\'s needed to.
You know, make sure that there\'s some uniqueness to this. So I\'m confirming about that question though on the page.
Yeah, um.
Yeah, so.

**Mayte Eme** 1:35:14
So they are supposed to come from the yes, they are supposed to and they are coming from the DPLT. We just didn\'t know what was implemented. So common questions was like can we override them? I mean did they get out of sync, right? And I or do they get override? The override gets overridden after the sync.

**Daniela Tea** 1:35:30
So for so for any of the fields that are not this read-only, those should be retained. This information here though, if in DPLT say this gets changed to a different web page or something that will be, you know, added to the content fragment and essentially republished during the.

**Mayte Eme** 1:35:30
Um, I think there\'s several questions about that.

**Daniela Tea** 1:35:49
Sync, but the information that\'s here, this should not change because these are supposed to be authorable with an AEM.

**Mayte Eme** 1:35:58
OK.

**Daniela Tea** 1:36:01
Let\'s take a look to see what else is on here.

**Kerry Holyoak (SHRSS)** 1:36:03
Sorry, just for clarification, are you saying that a content author can change a field that comes from DPLT? No, they cannot. OK, good. In particular, the page location ID, the actual DPLT ID.

**Daniela Tea** 1:36:05
Mhm.
No, they cannot.
Yeah.
Page. Oh, you\'re talking about?

**Kerry Holyoak (SHRSS)** 1:36:21
In the data layer we call it a page location ID, but it\'s the property ID. Then sometimes it\'s yeah, I think it\'s one of those. Those we use to classify the data in Adobe Analytics, so it\'s really critical that those are not editable.

**Daniela Tea** 1:36:27
See there. It\'s probably one of these, right? Yeah, it\'s probably.
Right. And and yes, and none of this here is going to be editable. So content author cannot edit this, but there are certainly fields that a content author would need to add, such as the delivery options for say a cafe and like you know if there\'s an associate venue and images.

**Kerry Holyoak (SHRSS)** 1:36:37
From a content author.
OK.
Sure, yeah.

**Daniela Tea** 1:36:56
Everything else that you see here should be coming in from DPLT if it\'s read only and disabled, so the author cannot interact with this or change it in EM.

**Kerry Holyoak (SHRSS)** 1:37:04
Great, thank you.

**Daniela Tea** 1:37:06
Yep. Um, let\'s see here.
OK, so on occasion I just designed the parent AM even if some values are blank. I think the answer, hopefully I understand the question, but the answer is yes, like we can see at least in this case, you know there are certainly some values that are blank. However of course since the required fields are filled out.
That\'s that\'s why the content fragment is able to be stored within a EM. So hopefully that answers the question. Yes, blank fields are possible, but the required fields do need to be filled out from DPLT.
Driven by any displayability of location need room.

**Mayte Eme** 1:37:48
What if the DPLT has a blank field when you call required because it could?

**Daniela Tea** 1:37:54
So I guess you\'re saying that there\'s no property ID, location ID or location code?

**Mayte Eme** 1:37:58
Well, I think property ID has to happen, but legal name could be blank, right?

**Kerry Holyoak (SHRSS)** 1:38:00
Uh.
They have. I just actually did a new I.

**Mayte Eme** 1:38:08
I can\'t see your wait, I\'m got to submit because I can\'t see. So you mean Daniela, that the only ones that cannot be blank are the ones with the asterisk.

**Daniela Tea** 1:38:19
These are considered required in a yes like this needs to be filled out in order to be stored.

**Mayte Eme** 1:38:23
OK, So what happens if the name is blank? It shows that blank.

**Daniela Tea** 1:38:30
If the if like a property legal name is blank.

**Mayte Eme** 1:38:34
Yeah.

**Daniela Tea** 1:38:35
Yeah, so if it\'s a property legal name is blank, then this is like this content fragment will be stored in A EM because that\'s not designated. That was not told to us to be a required field if that\'s something that needs to be changed in the future.

**Mayte Eme** 1:38:47
OK, so when, yeah.

**Kerry Holyoak (SHRSS)** 1:38:49
Well, and most likely it will come through as null, so it wouldn\'t actually be blank, it would say null.

**Mayte Eme** 1:38:56
No, it comes as blank. We\'ve seen the API that they use the same. So yeah, we\'ll load it as a up and then we\'ll have to enhance this.

**Kerry Holyoak (SHRSS)** 1:38:59
Hmm.

**Daniela Tea** 1:39:06
But.

**Mayte Eme** 1:39:06
3.

**Daniela Tea** 1:39:10
All right, let\'s see here.

**Kerry Holyoak (SHRSS)** 1:39:10
Mm.

**Daniela Tea** 1:39:16
OK, how do we add decorations with the map? I say. Can you clarify what this question? Oh, go ahead here.

**Kerry Holyoak (SHRSS)** 1:39:22
Real quick Mike, I just want to mention it\'s possible that that the gap that you just identified is already resolved. The DPLT team did a reconciliation on the data set and we just ingested a clean data set to Adobe Analytics and.
We didn\'t see any legal name or or look or long name or short name that was blank.
When we ingested the new list.

**Mayte Eme** 1:39:49
That is that that is good news. But we keep seeing wrong names, black names here and there, right? So I\'m just trying to understand what would happen. I\'m sorry my voice. What would happen if if it happens, right? So we know what to fix as we are logging bugs and and identifying ups.

**Kerry Holyoak (SHRSS)** 1:39:53
OK, OK.
Yeah.
OK.
Good to know. Thank you.

**Mayte Eme** 1:40:11
Mhm.

**Daniela Tea** 1:40:13
Yeah, so might take quick clarification is needed for this place. You said. How do we add decorations with the map? Can you explain what you mean by decorations?

**Mayte Eme** 1:40:22
Um.
I was trying to combine many questions into one, so let me think what that was. I think that was we have the ability in Cycor to change the map, you know, the color of the water, the lines, the details, all those things.
At that time I hadn\'t seen any from what you show. It seems like we can\'t configure any of that, right? It it it is what it is.
But that\'s not a friendly way for content authors, right?
I.

**Daniela Tea** 1:41:02
AEM specific, it would have to be generated from like Google, right? Whatever you need, like the colors or whatever you would want to be applied to that. So you mentioned something like changing like the watercolor, right? So yeah, as we had seen previously with our Google map component here.
The one that\'s on this specific page has all these different, you know, changes in place. But again, this is not something that like an author typically would write, but this is something that is would be from like Google\'s.

**Mayte Eme** 1:41:34
Yeah, we\'ll, yeah, that that\'s fine. We\'ll we\'ll notice the gap and we\'ll we\'ll fix it later so they can actually have a friendly UI where they can customize maps because we have campaigns, right? Not everything is going to look the same. And just being honest, if we start putting tickets to 80 for that, that the queue is going to be long.

**Daniela Tea** 1:41:47
Mhm.

**Mayte Eme** 1:41:53
And it\'s the the turn around is not as fast, so we can enhance it.

**Daniela Tea** 1:41:57
Mm-hmm.
OK, so let\'s see here. So I\'m just trying to take a look to see like what we can quickly answer. So OK, so this is this is the question I think that I was trying to remember how do we add a location not yet in the DPLT? So the answer.
To that would be as of right now you can\'t because those that information is supposed to be coming from DPLT. Those required fields are read only and supposed to be coming from DPLT so.

**Mayte Eme** 1:42:21
Oh.
OK, we have the ability to allocations that are not yet added because finance has to make the decision to add them when a lot of checks, checks and balances have you know, like passed the testing or whatever criteria they need to add. So we have the ability to.
Allocations.

**Daniela Tea** 1:42:47
So I guess my question is, I know that there is a field for what is it status like I guess is that something that\'s like?

**Mayte Eme** 1:42:56
No, they don\'t. Before we didn\'t get into that, like think of, I don\'t know, trying to come up with a good example for you, Athens, right? Athens is not in the DPLT yet, but we\'re going to start showing it in a couple of weeks as an upcoming location. It\'s not going to be in the DPLT until let\'s say 4 weeks from now and we need a life two weeks from now. So that\'s when we.

**Daniela Tea** 1:42:59
OK.
Mm.
Mm.
Mm.

**Mayte Eme** 1:43:16
Can actually go and add a cycle item and just type whatever we need to type and when it comes in the DLT, it\'ll override it and that\'s fine, but it lets us display the content that we need to.

**Daniela Tea** 1:43:27
So when you say display the content you need to like what are you like for your Athens example? I just kind of. I want to understand are you displaying it like on a map or displaying like all the information that would typically be in deep?

**Mayte Eme** 1:43:35
So we\'re listing.
Anywhere we want to, right? It could be a listing, it could be a listing, it could be a map, whatever we need to display it. It could be a coming soon section and all of that comes from the DPLT because we can dice whatever criteria we need with the queries that we can say give me only the coming soon locations, give me only the whatever locations.
And if it\'s not in the difficulty, we can just insert a new item.

**Daniela Tea** 1:44:04
OK, right. OK.
Uh, it\'s not. Locations based on one different like criteria. How do you say a criteria displays specific locations?
Um, let me see here.
I think we\'re kind of covering that, but we\'re saying very specific locations. That might be something I can work on. I don\'t think I can. I can work on this one. How do we ensure the canal fires vent 67?
OK, Yep. So Carrie, this is a question that you have with regards to tele. I\'m sorry, team was tracking that one running on the book. Now how can we get the AB test? OK, Yep, we talked about this one yesterday. This is also something we\'re tracking.
OK.
OK. All right. And Don, I see your question about bulk editing metadata. This is with regards to renaming the content fragments. That way they have the title instead. So I think we can, we\'d said that we would, we could walk you through the step.
So we can make sure this question is addressed when we get to the technical knowledge transfer section and and and help you help walk you through that one.

**Don Middlebrook** 1:45:20
Yeah.

**Daniela Tea** 1:45:22
OK, you filter category and you may for the development others should be used for place location. OK and I think Don, is this the same question?

**Don Middlebrook** 1:45:40
Um.
I can\'t see it. Um, hold on a second.

**Daniela Tea** 1:45:43
Sorry, this here.

**Don Middlebrook** 1:45:47
Let me pull this of the right screen so I can see it. Um, which CL should be used to replace? That\'s not me. I didn\'t have that. Um.

**Daniela Tea** 1:45:56
Right. But I guess this is that the same question though for?

**Don Middlebrook** 1:45:59
It might be, which I think so. I I added mine and someone else added more questions, so I don\'t know. It might be the same. Yeah, I think it\'s the same. Yeah, and it\'s.

**Daniela Tea** 1:46:02
OK.
OK, OK, no problem. I just want to make sure that that this we would we would make sure this is addressed, yes.

**Don Middlebrook** 1:46:14
Yeah, as far as the bolt, you know, updating metadata, I know how to do that. I just need to know what those fields are, the names. So if you go back to mine.

**Daniela Tea** 1:46:20
OK, OK.
Yeah.
Yeah. OK. I see. OK. Yeah.

**Don Middlebrook** 1:46:25
I just don\'t know what the fields are. I just because I\'m pulling metadata and I don\'t see anything that would align with those that data.

**Daniela Tea** 1:46:39
OK. Yeah, let\'s, let\'s make sure that we\'ll add that as a topic. Yeah, yes, got it. OK. Yeah. So don\'t want to go through all these questions over on the call right now. So what I\'m planning on doing though and I know that there\'s been a.

**Don Middlebrook** 1:46:40
So.
But yeah, just add that to the what we need to cover.

**Daniela Tea** 1:46:58
A lot of questions added to the pages and our team is we are trying to go through them. I want to make sure that I can identify ones that I can show during calls. So that\'s still what my priority is going to be, just like we did today by reviewing something with the news and then also with the location for.
The casino that was appearing in the dining widget, so definitely want to make sure that I\'m allocating time for that. So I\'ll try to identify some items here that I can show tomorrow, but the plan moving forward is we are hoping to cover.
As well as media items like I was trying to think of like a a category for this, but this is essentially things that are going to be using like say images or like videos or images. So the container is here because you can put an image or a video in there.
And then finally I have this other category called navigation and data display. So things like the breadcrumb, the site map and subnav and microsite navigation. That\'s what I mean by navigation, but data display things like the list and the content carousel, so.
Hoping to also cover this either today or tomorrow, but I\'ll be sharing some new agendas for some of the remaining components and we will be covering those next week. And then a quick reminder that if we take a look at the KT calendar.
We will begin our technical enablement sessions starting next Thursday. I think we\'ll be sending out some agendas for those and so Don will make sure that we we have the bulk metadata export topic in one of these sessions.
But keep in mind though with these sessions, we are also going to be bringing our offshore TA as one of the subject matter experts to each of those. So we\'ll send out the agendas and we\'ll be covering some of the more technical topics. So Gonzalo, I know if you have any questions and certainly please make sure that.
These are that you bring those questions to these sessions. That way we can get as many answered as possible. So with that being said, I am going to propose that we end the session so I can continue to review our locations page and.
Start to provide some answer to these and also identify some ones that we can cover tomorrow at the 1st 10 minutes of our next session. But before we close, is there anything else, anything, anything else that the team wants to cover for the next 5 minutes or so?
All right. OK, then. OK, guys. Thank you. Thank you so much, everyone. Hope you all have a good rest of your afternoon. All right. Thank you. Goodbye.

**Don Middlebrook** 1:49:49
Thanks, Daniella.

1:49:54
Thank you.

**Lucas Nelson** 1:49:55
You too. Bye.

**Mayte Eme** 1:49:56
Thank you.

**Don Middlebrook** 1:49:57
Thank you. Bye.

Scott Sorel** stopped transcription