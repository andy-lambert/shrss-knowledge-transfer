**SHRSS Adobe Knowledge Transfer-20260303_130309-Meeting Recording**

March 3, 2026, 6:03PM

1h 37m 18s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:09
All right, Daniella, recording started whenever you\'re ready. Thank you.

**Daniela Tea** 0:13
Thank you, Luke. Hey, everyone. Good afternoon. Let me pull up today\'s agenda.
OK. All right. So today I wanted to cover some line of business specific components. This is for the cafe websites, which we have talked about some of these before, but we\'ll take a look at them and and see the configurations for each of these.
I also wanted to go over something that we know was specifically within hotels for the microsites. So that includes A microsite page template as well as a component called the microsite navigation. We can see how that works.
And then also as part of the cafe websites, there was also that special page for the messy burger. And so in order to create that page, the team had to create a special template as well as another special component that\'s used within that template.
So we can take a look to see how that works and how that\'s set up, and also what the page looks like when it\'s viewed as published. So we\'re going to go ahead though and start first with these three cafe components here, the cafe delivery widget, the dining reservation component, and the reserve table component.
So I am going to jump on over to my little test page called KTLOB and so let\'s take a quick look here. All right, so I believe the team should be familiar with this component. We talked about how it\'s pulling in those cafes.
That are within the locations content fragments and we had acknowledged why Hard Rock Casino Rockford was appearing. As we saw from within the content fragment itself, it had been marked as a cafe location.
And so that\'s why this is here. And of course when we were trying to add some additional locations without that line of business selected, we saw that that wasn\'t actually getting added. So this is coming in from the cafes listed in the content fragments.
And within those content fragments, as we remember, you\'re able to select whether that specific location allows for delivery service and including the specific URLs that are associated with them.
So as you can see here for me, because I live close to the DC area, by default it\'s showing DC for me and for the Washington DC Cafe, there were the four different preferred services, DoorDash, Postmates, Uber Eats and Grubhub.
If I go over to this tab here, this is the Hard Rock Cafe, Washington DC content fragment. And so we can see that\'s where the delivery partners are listed with the associated URLs. And so that\'s what\'s populating the drop down that\'s present.
In this component, there are of course some additional configuration items for this specific component. In addition to pulling in the locations here, what we see here, I know there\'s a field called radius and kilometers and I was looking into the specific field.
Trying to track down how this is controlled right here. You can see though I\'ve left it blank and so it\'s not having any bearing on the component itself at this moment. It\'s showing Washington DC for me because my location services is on and that is the closest to me.
But I was planning on talking to the team to understand this specific field, but it does not necessarily need to be filled out. It\'s not a required field by any means, and I can speak more to this once I discuss with the team on this field. We also have our title field for order delivery now, which you can see is displayed here to the right.
We have our image displayed to the left, the alt text associated with the image, the description which gets displayed right underneath the title, the button text of go which is displayed here and we also have a disclaimer field. So if I were to fill out.
My disclaimer text and hit done. It displays underneath here and typically what we saw with this component I believe on the live version of this, there\'s actually a background where this is placed on it. So like you may think, oh this is like some really weird padding and such.
But if you look at the actual delivery page, I believe there\'s like a background image and another white background. So this seems to line up with that, but I\'m going to remove the disclaimer text right now, but that\'s what it looks like when you do display it.
And Don, I see your hand is up.

**Don Middlebrook** 5:07
Yeah, I just wanted so make sure like I said, the alt text is coming from the description field in the dam, but the description field is custom.

**Daniela Tea** 5:18
So you can inherit it from the description of the asset, but for this particular asset, I do not believe there\'s anything associated with it. That\'s why I just put something here for right now.

**Don Middlebrook** 5:23
OK.
OK.

**Daniela Tea** 5:30
Mhm.

**Don Middlebrook** 5:32
But I guess the description field right there, that\'s custom, right?

**Daniela Tea** 5:36
Oh, you\'re asking if it\'s no. So this description field if we.

**Lisa Cardia** 5:41
That\'s the description, Don, on the card, not for the image.

**Don Middlebrook** 5:46
OK, that\'s what I\'m just trying to clarify.

**Daniela Tea** 5:49
So wait, I\'m sorry, what? What do you mean on the card?

**Lisa Cardia** 5:51
He he he thought that like the all image text and the description field were related to the image above. But the description field right there is, unless correct me if I\'m wrong, the description we see when we\'re viewing the page, not for the image. Yeah, yeah.

**Daniela Tea** 6:04
Oh, you\'re. I\'m sorry, you\'re talking about this field. I sorry, dot. Thank you, Lisa, for clarifying. Yes, this description field is specifically for this here, right?

**Don Middlebrook** 6:05
So our delicious menu, yeah.

**Lisa Cardia** 6:14
I think the only confusion is why that\'s not like a regular text area where we have all the other like instead of it\'s like a field instead of like a rich text.

**Daniela Tea** 6:26
I miss. So I suppose this could potentially be changed to a rich text. However, I guess the this particular component has a certain style to it. Like this was not intended to necessarily be able to like change the heading or change.
Like bolding or anything like that. So that\'s that\'s why this was a specific text field. But I think what you\'re saying though is because it\'s like just like one line, perhaps it\'s hard to understand that it maps to this particular field.

**Lisa Cardia** 6:56
Yeah, I think that was the confusion there.
Right.

**Daniela Tea** 6:59
OK, but yeah, so the description field is this here. The alt text is specifically for this image here, and you do have the ability to inherit if there\'s something in the dam, but this field is is mapped to the image over here.

**Don Middlebrook** 7:09
Turn it on again.
OK. Thank you.

**Daniela Tea** 7:15
Yep.
Oh.
OK, cancel. So since we saw how this works with locations in terms of how the drop down is populated, of course as new cafes are opened and such and if there\'s delivery, what the author would certainly need to do is make sure that the.
Is delivery check box is checked as well as adding the delivery partners and as long as the line of business is correct then it should appear within the drop down drop down scene here. But I will pause to see if there\'s any questions about this component.

**Don Middlebrook** 7:58
I do have one for the location that\'s coming. Is that coming from the DPLT?

**Daniela Tea** 8:00
Mhm.
Yes. So this, yes. So the list of locations here is coming in based off of what you see in deep like when we say DPLT to be clear, when we see DPLT, the content fragments that is getting information from DPLT.

**Don Middlebrook** 8:23
OK.

**Daniela Tea** 8:23
That\'s that\'s what I mean when I say that.

**Don Middlebrook** 8:25
OK, all right, \'cause I I I guess.
I want to kind of relate that to the tags that we have in the dam for locations. Right now that\'s a manual process. So I I think we need to on our side look in how to how to keep updating those tags.
For locations rather than me and go in and update every time we have a new property. So if that\'s just something we need to look into.

**Daniela Tea** 8:58
Makes sense. Yeah, no. But that certainly makes sense. So in terms of like trying to get the process a little bit more streamlined. Um, yeah, understood.

**Don Middlebrook** 8:58
Nothing you need to do.
Yeah.

**Lisa Cardia** 9:09
I think for me Daniella, I was trying to compare this one to the production site and because this was I think designed just slightly different in the in the visuals like the disclaimer which I don\'t think you have in your example in mobile like looks.

**Daniela Tea** 9:15
Mhm.

**Lisa Cardia** 9:28
Unrelated to the content because of the way it sits. Like usually there\'s like an outline I guess in the box for desktop tablet.

**Daniela Tea** 9:35
Mhm.

**Lisa Cardia** 9:39
I don\'t see your the outline for you right now though. Like if you go to view as published, maybe that\'s why I\'m not seeing it.

**Daniela Tea** 9:47
What are you? Sorry, what are you trying to? What do you mean by?

**Lisa Cardia** 9:48
I I had on my notes like mine was showing like a black border.

**Daniela Tea** 9:56
Uh oh.

**Lisa Cardia** 9:57
Is it no longer? That\'s interesting. Like I had a black border around this entire widget.

**Daniela Tea** 10:03
So if you had it within, I\'m not sure if you had it placed within a container or something, but what I did was I just placed the cafe delivery widget directly on the page. I think if we were to look at at the cafe delivery page that has this on there in AEM, it\'s likely going to be set in.

**Lisa Cardia** 10:03
Widget.
OK.

**Daniela Tea** 10:23
In a container with a background image or something like that, but I this is me just adding this directly on the page. So if I added it directly on the page, I guess I\'m this is what it looks like right now. You can see it\'s pretty empty because there\'s no image, there\'s no button text.

**Lisa Cardia** 10:30
OK.
Oh, no, no. Now I understand what I was. OK, I do understand my comment. Sorry again, I\'ve tested these so long ago. So if you add a disclaimer and I guess the same, it\'s so you see when you hover over the whole widget, you can see that where the border is.

**Daniela Tea** 10:43
OK.
Mhm.

**Lisa Cardia** 10:54
So the disclaimer like isn\'t aligned with the photo, it\'s more so aligned with like the container itself. So the disclaimer looks very disjointed to the content since it doesn\'t match production, which goes pretty much edge to edge photo with the disclaimer.
So if you added a disclaimer and you just put like a sentence, like a fake filler sentence, I guess this is where. Yeah, see how it goes. To me, that looks odd.

**Daniela Tea** 11:23
Yeah.

**Lisa Cardia** 11:25
Because you\'re not gonna have the cafe delivery widget title there. So to me, the disclaimer looks off or unrelated because we can\'t like align it with the content.

**Daniela Tea** 11:29
Right.
Mm-hmm. Um, let me see.

**Lisa Cardia** 11:38
Does that make sense? It\'s just and it\'s because this is a different visual than production. Like I think production\'s image has either a like a background to it or something. So this is just slightly different. But since it\'s different, I think it looks off or like unrelated to the content above it.

**Daniela Tea** 11:53
Mm-hmm. Yeah. So let\'s see. I\'m trying to take a look to see what what was what we did on the actual page and.

**Lisa Cardia** 12:04
It\'s just, yeah, because there was background images from our production site, but since the containers are empty, it doesn\'t look like it aligns.

**Daniela Tea** 12:09
Yeah.
Yeah, so yeah, Nope, I I agree. So in terms of of what I\'m seeing here on on the other AEM page, the delivery page, and I\'m gonna just pull that over here. So yeah, it looks like it was placed within a container and then also a container with the background.
I noticed the disclaimer isn\'t on here. Perhaps this was what where we moved the disclaimer to appear completely underneath. Of course, this is just a text component versus actual using the disclaimer field here. So I think this is one way to get the desired alignment, but I think as we\'re documenting.
And understanding how to like some of the things that could be needed for this component. You mentioned like the edge to edge for the image as well as the alignment for the disclaimer text.

**Lisa Cardia** 13:02
Yeah, just because if a if a background image isn\'t used, it just doesn\'t look correct.

**Daniela Tea** 13:07
Yep, understood.

**Lisa Cardia** 13:12
Minor, but yeah, you can continue. I don\'t think I had actual questions because we did answer the Casino Rockford question why that was displaying and I reached out to the to the the DPLT team, so.

**Daniela Tea** 13:13
OK.
Mhm.
OK, Yep. So that I guess it might take a while for it to appear, but once the that data is correct and it\'s updated and and pushed to AEM, then that it should disappear from the drop down.

**Lisa Cardia** 13:39
Yeah, and then I think it just goes without saying again, image will hope for the spec.

**Daniela Tea** 13:44
Yep.
Let me pull up for the reserve a table component. I wanted to also show how this is authored for an individual site, so I\'m going to pull up experience fragments here on the side.
OK, so for the reserve a table component, this is what\'s being used within both the the modal at the very top of our cafe page, but also something I believe you would see within the dining reservation component if it if there\'s say like a button.
Or something that would activate it. So let\'s take a look at how this one is handled. So with our reserve table configuration, there\'s two fields, one for the drop down placeholder and then one for the button that will appear.
After you select something O let me show you though how this is populated because if I click this you\'ll see a bunch of different locations O this dropdown is actually coming from.
I\'m going to change the view to column. This might be if you\'re more familiar with some of the experience fragments and I\'m going to cafe and you\'ll see all the different cafe locations. If I click on a location like let\'s say Pittsburgh and I click EN, you\'ll see there\'s an experience fragment called reserve table.
O I\'m going to open this U and I\'m going to hit edit.
And I can see that actually. So let\'s see one second or table. I want to get something that actually has like a button or something, so it\'s very clear. Let\'s see.
Nope, that\'s all I.

**Lyon, Rick (Director of Digital Experience)** 15:37
Hey Daniel, is that that one fragment you just showed? Is that in every cafe folder?

**Daniela Tea** 15:39
Yeah.
Yeah.
Yes. So there is a, so there is each of the cafes have their own separate section of experience fragments and that\'s to be able to say handle say like the header, the footer as well as this reserve table component.
So I\'m trying to find one that just has a button associated. So let me let me. OK, so like, let\'s look at this one here. Let\'s look at this one.

**Lyon, Rick (Director of Digital Experience)** 16:09
It\'s purple.

**Daniela Tea** 16:11
Yep, it\'s it\'s purple because I\'m within a I\'m in the hotel\'s theme. I\'ve set my page to be the hotel\'s theme. That\'s the reason why it\'s purple.

**Lyon, Rick (Director of Digital Experience)** 16:12
Why is it a purple button?

**Daniela Tea** 16:23
Um, one second. I\'m going to.

**Lyon, Rick (Director of Digital Experience)** 16:23
Oh.

**Daniela Tea** 16:27
Try to find this here.
We should.

**Lisa Cardia** 16:33
I know you\'re looking for an example, so would it? I know and you\'re going to show us that it gets configured on the fragment level too. So would you say that when you add the the actual component to the table that filling out those two fields isn\'t really necessary because it\'s going to get overridden by this or?

**Daniela Tea** 16:35
Mhm.
Mm-hmm.
Oh, so to be clear, what we\'re seeing here is this is a component that\'s going to be used within the header, the EN header. I\'m going to show you what that is and so I\'m just showing though.

**Lisa Cardia** 17:02
OK, so so we\'re not dropping it on a page. It\'s only. OK, that makes sense then. Got it.

**Daniela Tea** 17:04
No, you\'re not dropping it on a page. That is correct, Lisa. So here what you\'ll see though within here within my experience fragment I have this is this is not that component. What this is showing is this is a container that has a black background with a title, some spacers and a button that has.
The information on there, right? And So what this component does is it pulls in the different experience fragments and displays it depending on the drop down. So let\'s go ahead and make a new one so you can see how that gets added here. I\'m going to go back.
To just create a new cafe, I\'m going to create a folder called KG.
And I\'m going to go to my KT folder, which should be here, and I\'m going to create my structure. I\'m just following the structure here because this is typically what you\'re going to have for your cafes, the different languages.
O In my case I\'m going to have en and then I\'m going to make something called reserve table.
Second. Yeah. OK.
Yeah.
And then where did it go? Oh, it\'s down here. And then I want to make a something called reserve tables. I\'m going to create experience fragment called reserve table. I\'m going to choose SHRSS blank variation.
I\'m going to call reserve table.
OK, all right, so now within my reserve table, let\'s. I\'m actually going to just copy this container, but change out the phone number so it\'s clear what we\'re showing.
OK.
So I\'m just going to put some random numbers.
That\'s too close. Alright, so I\'m just going to put this here just so we can see the number has changed. Alright, and if I were to refresh this.
We should be able to see my KT.
So let\'s see, reserve a table.
And my reserve table had a reserve table. So I yeah, one second.
Yep. OK, so let me go ahead and publish my experience fragments.
Excuse me.
K and let me see if I can get that to appear on the page.
Table.
Table.
Trying to think this was one second.
Trying to remember what I did earlier to get this to work.
So once I can get this U and running I will show you guys how I did it.
this one again.
Hmm.
Hmm.
All right, so I should be seeing that on here. I will actually work on this one off the side, but I did want to show if I change something how you guys can see it get changed. I\'m going to go ahead and change this one right here.
So instead of showing this, if we were to take a look at this specific location, let\'s take a look here.
So that displays our OpenTable advanced embed here. So if I click on this you can see we\'ve used an advanced embed, but the experience fragment is going to be.
Gathered within this specific component, but if I were to like if I were to say, I think you guys have things other than just open table, but those would be using again the advanced embed component. So whatever you put in here will be displayed within this component when that specific drop down is selected.
So let\'s try and add. I\'m going to change this. Hey Rick, I see your hands up.

**Lyon, Rick (Director of Digital Experience)** 22:05
Yeah, so one thing that I know that we\'ve ran into on the Vision GN doing this is sometimes the widgets are sometimes are just insanely large because you\'re just not coded very well. So are there any like adding safeguards or anything in the widget if you know the code is like accessible?

**Daniela Tea** 22:11
Mhm.
Mhm.

**Lyon, Rick (Director of Digital Experience)** 22:25
Simply wide or or you don\'t very tall or anything like that.

**Daniela Tea** 22:29
So when you say excessively wide, do you mean like I guess like do you have an example that I can see?

**Lyon, Rick (Director of Digital Experience)** 22:34
I mean it\'s gonna be franchise, it\'s not gonna be open table because they have the nice widget. But I\'ve seen other smaller I guess services that are similar and you know you could see like the the table coded in in the widget itself is just not very styled and stuff like that and there could be like 7 or 8 fields.

**Daniela Tea** 22:38
Oh, OK.
Hmm.
So keep in mind that. So this is where that reserve a table. So I\'m just on the stage version of the cafe site. This is where the reserve a table button is located. It\'s in the top and then it displays as a modal and then depending on what you select, I think you\'re looking at.

**Lyon, Rick (Director of Digital Experience)** 22:53
Um.
Me.

**Daniela Tea** 23:10
This one here, depending on what you select, it displays, you know, like within the modal. So that\'s what I was saying. If you have an example, we can certainly see what it looks like in here. Oh, here we go. We can see here\'s my KT location. This is the one that I had added.

**Lyon, Rick (Director of Digital Experience)** 23:17
Mhm.

**Daniela Tea** 23:28
So just to be clear, this was the KT location that I had added within my experience fragment and you can see how it\'s visible within the cafe website and it\'s invisible in this drop down. So it\'s based off of and I\'m actually going to write out the steps for you.
Guys and post it onto the Confluence page later tonight just to make sure it\'s clear. But as you can see how my experience fragment is now displayed when I was looking at the cafe website available here. But yeah, Rick, if you have an example, I can certainly take a look at that. But I think for what we saw, it was mainly like buttons for phone numbers as well as the open table.

**Lyon, Rick (Director of Digital Experience)** 24:02
OK.

**Daniela Tea** 24:08
For for the reservation, I\'m I think I just want to know like what what other options there were and I can report back to you on that.

**Lyon, Rick (Director of Digital Experience)** 24:17
OK, yeah, so like I don\'t know if if what you guys build works the same way as on Visergy, but if a cafe site has a particular third party widget that\'s not open table on their cafe site, that same widget is will be displayed here in the pop-up.

**Daniela Tea** 24:28
No.

**Lyon, Rick (Director of Digital Experience)** 24:32
So that\'s kind of where that came from. So I don\'t know if if the same widget will appear twice in AEM or if it\'s only on the cafe site, but I\'ll I\'ll click around and see if I can find any that I\'m talking about, but.

**Daniela Tea** 24:33
I I see so.
OK, sure. Yeah, yeah. So for the most part though, I think what I saw from the experience fragments was the use of a button. I think it\'s possible, you know, if you needed to to have the button just I guess either link to the page versus doing an embed.
You know, something like that. So there there are potentially some ways you could get around like a really ugly embed. But for the most part, what I saw with the open table one is going to be very similar to this. Right now it\'s kind of wonky, right? Because this is when the experience fragment, but when it\'s displayed within the reservations component, I believe there was.

**Lyon, Rick (Director of Digital Experience)** 25:14
Mm.

**Daniela Tea** 25:20
Some styling that was added in order to kind of make it fit within the modal itself. But yeah, Rick, if you have any examples, please provide them and I can take a look. Yeah, OK, so for this reserve a table component though, again, I\'m going to write out the exact instructions for what I did to get this.

**Lyon, Rick (Director of Digital Experience)** 25:28
OK. Thank you.

**Daniela Tea** 25:40
To work. However, it is a matter of creating an experience fragment on folder. We go back here. As you can see with my KT folder here I created this and this is going to be something you\'re going to need to do for additional cafe properties.
Your experience fragments are going to basically be things like the header, the footer, reserve a table. You can see here we had the parking information set up for the specific cafes as well. So just something to keep in mind as you add additional properties.
To the site.
I\'ll pause here to see if there\'s any questions about this.
OK. All right. Let\'s move on now to our dining reservation component. This is something that I think that the team is pretty familiar with for the cafe websites located at the very top of our cafe websites.

**Lisa Cardia** 26:39
Wait, sorry, sorry. I I do actually have one question. What is driving like the options in the list? Like could we make this a like a unique list if we wanted a landing page with just US location? Sometimes we have offers where they\'re just.

**Daniela Tea** 26:41
I\'m viewing it as published. Yeah, go ahead.
Yep.

**Lisa Cardia** 26:58
EU locations or just or just the franchise or what have you? So is there a way that we can control the list?

**Daniela Tea** 27:07
So this.

**Lisa Cardia** 27:07
Or isn\'t it all or nothing?

**Daniela Tea** 27:09
So this list is based off of all of the different experience fragments that are created here. So that\'s what\'s that\'s what\'s dictating this. So keep in mind like for example I made my and I\'m gonna view it as on on here.
Yeah, so you can see my KT option is available here. However, this is not necessarily something that\'s in like DPLT, right? So this list is specifically drawing in the different folders that are listed in here in the experience fragment section based off of if there\'s that reserve a table.
Experience fragment in it.

**Lisa Cardia** 27:47
OK, but we can\'t like include or exclude.

**Daniela Tea** 27:51
As of right now, no. It sounds like though what you\'re saying is like the different regions would might be what you\'re interested in, OK.

**Lisa Cardia** 27:58
Yeah, yeah. In case it\'s on a page at the header, well, is it only in this header? I guess because we can\'t actually have a unique header per page, can we?

**Daniela Tea** 28:10
So you. So there\'s actually unique headers per each each cafe. Mm-hmm.

**Lisa Cardia** 28:16
Property page but but like if we made like a a landing page for like a promotion that just so happens to be only available at specific cafes.

**Daniela Tea** 28:28
Um, maybe about specific cafes, I see.

**Lisa Cardia** 28:31
So if we made, yeah, so like so a lot of times we have these limited time offer menus that we make and we have a landing page dedicated to them. So like currently there is a landing page for International Women\'s Month. So if that\'s only available though at specific locations, my question was could we just limit?

**Daniela Tea** 28:36
Mhm.
Uh huh.

**Lisa Cardia** 28:47
The reserve to show just the locations that it\'s.

**Daniela Tea** 28:50
I see. So right now, no. But what I\'m wondering is for your use case, if perhaps you could do that using the drop down component we looked at yesterday. I know that\'s not like exactly the same. I\'m just trying to think about.
How what you\'re trying to show is essentially this drop down, but with specific locations listed.

**Lisa Cardia** 29:13
Yeah, but then it wouldn\'t trigger the, it wouldn\'t trigger the open table from there like that would be more so just like a work around to get you to the property page.

**Daniela Tea** 29:19
Well.
So something I wanted to show is that you can see how I\'m what I\'m showing right now is I\'m looking at this specific cafe, right? And I\'m looking at their specific header. The way that this is authored is it\'s showing the experience fragment.
Showing the experience fragment to be launched when clicking reserve a table. So it\'s not actually using this component at all, it\'s using the experience. It\'s going to show the experience fragment in a modal. So what I\'m saying is there\'s potential to be able to show these experience fragments in a different way, perhaps using that drop down.

**Lisa Cardia** 30:03
OK.
As as the URL. OK, OK.
OK, OK.

**Daniela Tea** 30:15
Yeah, so something something I need to think about since I I know like right now this specific component I believe is only used presently on on the cafe homepage. But for your use case, I think there could be ways to achieve what you\'re saying with that other component.
Yeah. All right. Yes.

**Lisa Cardia** 30:34
OK. Thank you.

**Lyon, Rick (Director of Digital Experience)** 30:36
Um, Port Porto is one of the cafes.

**Daniela Tea** 30:39
I\'m sorry, what was it?

**Lyon, Rick (Director of Digital Experience)** 30:40
Orto.

**Daniela Tea** 30:42
Let\'s take a look. OK, so I think here you can see it has that book now link and then it takes you to. It looks like it it what was added was the actual link to it versus showing an embed within the modal.

**Lyon, Rick (Director of Digital Experience)** 30:59
I don\'t know if it was Porto or I think it\'s just Porto.

**Daniela Tea** 31:01
Oh, was it? Oh, I\'m sorry.

**Lyon, Rick (Director of Digital Experience)** 31:03
That\'s fine.

**Daniela Tea** 31:04
Uh, I don\'t. Is that? Can you spell that word?

**Lyon, Rick (Director of Digital Experience)** 31:11
I mean, it\'s porto PORTO. Maybe go to the live cafe site.

**Daniela Tea** 31:14
Uh, OK.

**Lyon, Rick (Director of Digital Experience)** 31:21
Just forward slash portal. Oh OK yeah, I wanted to show the the website first cause it\'s the same.

**Daniela Tea** 31:29
Oh.
OK, so this is what you were saying. Um.

**Lyon, Rick (Director of Digital Experience)** 31:35
Yeah, so probably not the best case, but you can see how they\'re not as clean as the open table, which it.

**Daniela Tea** 31:43
Yeah, I\'m sorry, I\'m a little confused \'cause so on the live site it looks like it is. Does the embed normally display here?

**Lyon, Rick (Director of Digital Experience)** 31:52
It should. It\'s not now and I just saw that as I found Porto, but I just wanted to show you the non open table widget that could be a little bit taller than the open table widget, if not wider.

**Daniela Tea** 31:54
OK.
Bye, bye.
Yeah, no, understood.
Yep. OK, So what I am thinking, I\'m like if this were placed within because the way that this would be authored would likely be the advanced embed component with that embed code that would be placed within the experience fragment. I think we would. I can\'t tell you exactly how it will look in the modal.

**Lyon, Rick (Director of Digital Experience)** 32:16
Right.

**Daniela Tea** 32:24
I saw the code, but the experience from. Yeah.

**Lyon, Rick (Director of Digital Experience)** 32:26
What is that? Is that the procedure? We would put it in the advanced bed on the cafe site and then for that pop-up motor we would we would put it there as well.

**Daniela Tea** 32:32
So, so the procedure would be for the let me get back to our experience fragment. So in our experience fragments for your specific cafe, you would have created a reserved table experience fragment.
And on here you would have you know you would you would put whatever you need here. In this case I have my button for this specific for Porto. Where is it?
OK, one second. Proporto this code would then go within this experience fragment. So that way when you click reserve a table, it would pop up in a modal. So pretend it popped up here so you would see it here. It would pull in whatever\'s in the experience fragment.

**Lyon, Rick (Director of Digital Experience)** 33:08
Mm.

**Daniela Tea** 33:18
And then what you have here on the actual Porto page, this is part of the dining widget, which we can break down how this is authored and how you might be able to, you know, like add some of these features here.
So let\'s take a look at the dining widget to see how that would work. But for this to appear in the modal though, Rick, it would go within the experience fragment.

**Lyon, Rick (Director of Digital Experience)** 33:42
OK.
OK.

**Daniela Tea** 33:44
All right. Let me pull in the page we\'re just looking at, which has my dining reservation. OK. All right. So as you guys have probably seen on several of the cafe pages, of course, you know, there\'s.
Different options for every cafe. Not everything\'s gonna use OpenTable, not everything\'s gonna use Grubhub, etc. I believe when we reviewed this, I think a couple months ago, there had been an ask about other integrations other than just Grubhub.
And so I know that we had added another delivery services button in order to to provide some flexibility for you know things are the Grubhub. Of course we understand though that if there\'s additional integrations that\'s certainly something you know I would imagine you would want to capture in the gap while this.
Provides a button to be able to add other delivery services. If you\'re looking for something that\'s more styled for the specific delivery service, that would of course be additional enhancements for this, but let\'s take a look and break this down.
And see how is this specific component authored. All right, so let me maximize this.
OK, so starting with our title here, Baltimore in this case, we can see how it\'s presented on the image. The banner image of course is selected and then displayed here on the page.
Alt text whether you want to get it in from the dam itself or if you want to apply your own that those fields are there. We have our phone number which is displayed here. We have our e-mail CTA label.
General inquiries and you can notice that the icons that are present here, these are things that are paired with the specific label. As of right now, you\'re not able to necessarily change out the icons, but whatever is put in this label here or this label field is going to appear next to the appropriate icon.
So telephone for phone number and then this letter icon for the e-mail CTA label. The e-mail CTA link is then added and applied to be the HREF for whatever the label is for here and as we Scroll down we have the address.
601 E Pratt with the address link. So when I hover over this, if I hit preview, I\'ll be able to see this be underlined and then it\'s next to the address icon. I feel like someone\'s hand might have gone up, but I don\'t see it anymore, so I\'m not sure.
Does somebody have a question?

**Lisa Cardia** 36:33
I have a question. I didn\'t put my hand up. Yeah, my question is for the phone number. I know we had gotten this issue in the past to so that it like we don\'t have the special characters showing, but we still have it where if you click it, you still have the like TEL colon.

**Daniela Tea** 36:35
Oh, OK. Go ahead, Lisa.
Mm.
OK.

**Lisa Cardia** 36:52
Format because the numbers they weren\'t. You couldn\'t make a phone call all the way through while the way it was configured because the display name needed to be the same as the actual phone number.

**Daniela Tea** 37:00
OK.
Yes.
Right. So I don\'t. I just might be super tiny, but you can see that I\'m maybe you can see I\'m hovering over if you look at the very bottom left. OK, OK.

**Lisa Cardia** 37:15
Yeah, I can see the tell. So does that mean if a user just puts in the right digits with no special characters? Like what was it on the the back end so that we know it?

**Daniela Tea** 37:24
Yeah, so let\'s take a look at what was put there. So you can see here this says 1410-347-7625 and what that equated to was when I hover over this again tell and then the plus and then 14103477625 without the dashes.

**Lisa Cardia** 37:44
OK, it\'s stripped it of the dashes and the spaces. OK, And then my second question was that if we don\'t have the e-mail, the phone number or anything, we can\'t hide the icons. They still show when it\'s blank.

**Daniela Tea** 37:45
That\'s correct.
Yeah, let\'s let\'s take those away. Yeah, so these are required fields, I believe. The e-mail at least was a required field, but let\'s take away the phone number.

**Lisa Cardia** 38:10
When you when we like, yeah, when we removed the optional, it didn\'t remove the icon.

**Daniela Tea** 38:16
OK, so I\'ve removed the phone number. The icon is hidden.

**Lisa Cardia** 38:21
OK, so maybe this is this was just something that we experienced in the past. Maybe that got fixed.

**Daniela Tea** 38:26
Well, so the for the phone number, phone number is optional.

**Lisa Cardia** 38:29
Or or or or is it the required ones that maybe that\'s what I\'m confusing this with. There was there was just something where we could not remove. So possibly it\'s the e-mail. Yeah some something like that where it\'s always displaying. But there are there are case like scenarios where a cafe might not have.

**Daniela Tea** 38:40
Maybe could be the. All right, one second. Let\'s do this.

**Lisa Cardia** 38:49
Of the the phone number or e-mail, so like we wouldn\'t have anything to put there.

**Daniela Tea** 38:54
OK, so one second, just putting something here. So the phone number can be blank and if you I\'m going to remove the phone number. So if you don\'t have the phone number, you can also see it\'s not technically a required field. e-mail was deemed a required field though.
But for the phone number, I\'ve removed the phone number and you can see that the icon doesn\'t show. So I\'m I\'m not sure if perhaps that was. I\'m imagining when you were doing the testing for this probably a couple months ago, perhaps that was something that got addressed during that time. But phone number since it\'s not required if you do remove it.
It\'s not displaying the icon.

**Lisa Cardia** 39:36
OK, we\'ll we\'ll take down that the other ones still display when left blank.

**Daniela Tea** 39:41
Yeah. OK. All right. I\'m gonna hit done again just so we can see the phone number that was there previously.

**Lisa Cardia** 39:46
Oh, I and I did have one more, but you didn\'t. I\'m probably jumping ahead myself. You didn\'t. Did you show us where you link the menus with the PDFs?

**Daniela Tea** 39:53
Oh, no, we\'re we\'re we\'re up top here. I\'m working my way down. No problem. No problem. Yep. All right. I\'m going to Scroll down and we can take a look at our social media icons. Excuse me. So in this case here, I\'m going to open this up and we can notice what\'s there.

**Lisa Cardia** 39:57
OK. Yeah. Sorry, I\'m, I\'m jumping around on my notes at the same time. Thank you.
Yes.

**Daniela Tea** 40:26
Icon is being phased out so that\'s being that was added here. I believe though I think we maybe it was last week we were talking about generic lists and adding you know like icons and stuff to to appear in this drop down list.
That that is something that\'s like kind of like permissioned group who would be able to add additional icons. This is the set of icons that we were provided with for the cafes. However, when it comes to adding additional ones, there is a way to do it, but only if you.
Who are within a specific user group. I\'m going to bring up the generic list which should not be accessed by like say a random site author. I\'m just going to head over to our little tools icon here and then ACS AEM Commons and click on generic lists.
So there is the social media types. Believe this is it. I\'m going to hit properties and you can see here this is where those icons are coming from. Facebook, Twitter, AKAX.
Instagram, et cetera, et cetera. And so someone who has the proper permission, so it\'s likely going to be like a site admin or something, can add additional options available to the authors.
And you\'ll notice here we are currently using Font Awesome for these. So these are the Font Awesome classes and so that\'s what would be displayed once that\'s enabled by the admin user. So I think Lisa, you were out last week, but when you were having that issue.
I think it was with the locations component, you and Gonzalo were having that issue.

**Lisa Cardia** 42:18
Oh yeah, yes, we couldn\'t see the drop down.

**Daniela Tea** 42:21
Correct. So yeah, we, I think last week, I don\'t know if Gonzalez is on the call right now, but we were able to confirm that Gonzalez can now see it. You should also be able to see it. The reason why you weren\'t able to see it is because there was the the list of drop down options again is a generic generic list.
And so that is something that just needs to be applied at like a read-only level for the users. So I believe we addressed that. So you can also actually confirm that on the locations component, but that was the reason why you weren\'t able to see it. So for the authors though, they should be able to see these values. However, they\'re not necessarily going to.

**Lisa Cardia** 42:49
OK.

**Daniela Tea** 43:01
Be able to add these values unless they belong to a certain user group. OK, so I\'m going to go back to our page.
Where\'s it? I\'m gonna go back to our page. So that is how these specific icons.
That\'s where these values are coming from, so everyone understands that. And as you can see here, you can add multiple, reorder them, et cetera. And I do believe these should open up in a new tab by default. Let\'s try that. Yep. So I didn\'t have the option to set it to open in a new tab in here because.
By default all of these are going to open U in a new tab.
All right. OK. I am going to keep moving down. So now we\'ve covered the top portion of this. Let\'s go down here to this make a reservation section. So we see where that label\'s coming from. Make a reservation. It\'s coming right here.
We have a reservation platform. We either have open table or you have the option to choose others. Others means that I let\'s. I\'m actually going to make a copy of this. One second. I\'m going to make a copy of this.
So I can kind of mess around with this one and we can see what that looks like.
OK.
Rush.
OK.
OK, so let\'s change this to others. I think there are quite a few that do have OpenTable, but if I were to keep, you know, if I have other selected, I can keep the OpenTable ID, but it\'s not going to do anything. I\'m going to hit done.
All right, so now we see that that the open table, the open table embed has now disappeared.
Right. And what I can do instead is I\'m able to enable my other delivery services button and I\'m going to hit done and so that\'s going to allow me to edit this component. There\'s going, there\'s supposed to be a button on here.
That appears I\'m going to refresh there. I don\'t think there\'s ever going to be an instance where there\'s going to be two of the same component on the page, so I think I might need to just bring this to a different window, but what this is going to show is.
The ability to instead of adding OpenTable, if you need to add, say something else, you should be able to add it within the component itself. Instead of having Grubhub, say you want to add DoorDash. Right now we only have Grubhub and that\'s why you have that style button.
However, if you don\'t want that, let\'s do done. If you don\'t want that, why is that button not appearing?
I think I am doing all sorts of things to complicate this just because I was trying to put things on the same page, but I\'m going to check on where that button is. So there\'s going to be an embedded button for you to be able to add another delivery link if it\'s not Grubhub.
But I\'ll show you that in a second and another page where I wasn\'t messing around with two at the same time. But let\'s move down to this menu section. So here we see I have my View menus button. I also have the additional menus underneath.
So cafe, drink, gluten-free, happy hour, banquet, etcetera, etcetera. I can add more if I want to, but if there\'s, I believe it\'s a there\'s only there\'s more than three, then it presents itself as a drop-down instead of listing out the menus if I were to go at.
Go ahead and just remove say like and remove about. Let\'s do these two here. So if I have two on the page, it\'ll display directly onto the page, but anything more than two then changes to a drop down and displays as a button.
Based off of whatever the label that you have here. In this case, view menus was the label.
I\'m just going to put this here. You can see that operates. So here\'s our view menus button with the three different options underneath. And then finally at the very bottom there is an ability to do enable languages.
What that does is that embeds our language selector component. This is the one we saw yesterday. So you guys should hopefully be guys remember from yesterday. This was the ability to essentially add additional drop downs as needed. So like you know English.
And then whatever the link is for that, French, etcetera, etcetera. And then it would just appear underneath the view menu section after you author the component. So I do want to get a working example for the delivery.
Portion of this component, which I\'m trying to work on on the side, but looking at the time, I also want to make sure we cover some of the other options. So for right now, were there any questions about the other portions of the dining reservation component?
Like for the menus, the language selector, the social media or the fields above as well as the image and the the title of the component.

**Lisa Cardia** 48:46
I just wanted to comment on an issue we had uncovered when we were linking the menus for the PDFs that it it it. I think this might be an easy fix on Adobe side, but we can\'t link to the PDFs without having like a path already because it starts with sites and not.

**Daniela Tea** 48:53
Mm-hmm. OK.

**Lisa Cardia** 49:06
Not the assets, so.
That\'s what we\'ve encountered. I have that written down as a take away.

**Daniela Tea** 49:13
OK, I see what you\'re saying. Yeah, so that one second. Yep. So I can see what you mean here. This works because this was probably already inputted and you have access to the dam. But what you\'re seeing is that this is starting at this SHRSS level versus starting.

**Lisa Cardia** 49:28
Yeah.

**Daniela Tea** 49:33
At the content level, is that correct? OK, got it. Yep. Yeah, understood about that. I guess, Lisa, was there an existing GR ticket for that or is that something you\'re just noting down for the platform expansion gap analysis?

**Lisa Cardia** 49:34
Correct.
I\'ll I\'ll probably note it in the confluence, but like I haven\'t put tickets in quite some time.

**Daniela Tea** 49:53
OK.
OK, yeah, no problem. I just wanna make sure that if it\'s at least captured for the platform expansion, then we can we can make sure that it\'s good.

**Lisa Cardia** 50:02
Yeah, well, if if you guys can definitely take that on your end, just because I think it\'s just a matter of like setting the the starting point on the back.
I feel like we\'ve encountered this somewhere else and it got fixed.

**Lucas Nelson** 50:20
Lisa, what do you mean take it on our end?

**Lisa Cardia** 50:23
Like, like, I think like it was just like a setting. I don\'t know if this was during like Matt Ross\'s time or something, but it was like we just needed the starting path for the links to just start from the asset folder versus from the sites. Yeah, so where Danielle is showing us.
We can\'t get to that from how it\'s set up currently.

**Lucas Nelson** 50:48
Daniella, do you have a handle on what Lisa\'s asking us to look at?

**Daniela Tea** 50:54
Uh, yes, I I understand. Um, I think.

**Lisa Cardia** 50:56
It\'s linking to sites instead of assets.

**Daniela Tea** 50:59
Yeah, no, I I understand what the ask is. I just wanna make sure that, yeah, we we wanna make sure that\'s captured because I it is something that that would be. That\'s what the authors need. Yep.

**Lisa Cardia** 51:09
We can\'t as authors, yeah, like we we wouldn\'t be able to complete this.

**Lucas Nelson** 51:14
Yeah, Daniella, just articulate that when Danae\'s back on Thursday, just so I have a better understanding during our stand up. That\'s all. Yeah.

**Daniela Tea** 51:19
Mhm.
yep yeah sure thing sure thing um
OK, so for the menus, it\'s, uh, getting the starting point for the dam versus the sites.

**Lisa Cardia** 51:37
I\'ll put it on the confluence page, but yeah.

**Daniela Tea** 51:40
Yeah, no, sure thing. Thank you, Lisa. Any other questions about the other fields and I\'ll be posting a link to an example of with the other delivery options later in Confluence as well.
But any other questions about the component before we move on?
All right.
OK, so now I wanted to take a look at the Messy Burger page and what that entails. So there were two things that were created for this. I\'m going to.
First show in the template section that there is a page template for this and I\'m going to take us there, right? So clicking on tools, clicking on templates, Hard Rock Seminole.
And you\'ll notice there\'s a page called Messy Burger Page and it\'s based off of the open page template and we can actually take a look to see what it includes this page. To be clear, this page was specifically made. This template was specifically made for this page because that page had a lot of.
Custom functionality that was added to it and what this page has so everyone understands if I were to take a look at our page policy.
There is a specific class that\'s associated with the entire page. Now this allowed us to create very specific CSS that would only affect this page. What this does is if I were to view the messy page right now, I would see this at the page level, so it\'s essentially wrapping.
The entire page content within this class. So that way then we can target it with some specific CSS and not have to worry about it affecting the other templates. So if we were to look at the actual template itself, you may say OK, well this is pretty much this is very similar.
To what we saw the other day when we were viewing templates, how we had the experience fragment at the top, the experience fragment at the bottom, and then those two layout containers, one for the hero banner and then one that essentially is allowing every component to be added.
And so that\'s why I wanted to make sure it was clear. The messy burger page was created specifically for the messy page and it needed to be wrapped with a special class in order for us to target the CSS. So in practice though when you create a page with this template.
Which I\'m going to do right now.
And create a page and you will see that here.
I\'m going to hit next and I\'m going to call this test messy.
And I\'m going to hit open. So this is what it looks like to to an author. Again, looks just like the open page template. However, everything that is needed for this page to work is is dealing with that class that was added within the template level.
So a finished version of this page and we can break down all the components on it. This was what we had migrated over. I\'m going to refresh the page so you guys can see so we can see some of the parallax effects that were added to it.
And if we were to breakdown this page here.
This is using that specific template. It\'s also using some of the components you all are familiar with. The hero banner for example. This is the video.
This is the Messy Experience component, which I\'ll breakdown.
This is an image. You can see containers and other containers with images on it.
But with the special class that\'s added to it, that\'s why there\'s some additional CSS that\'s only affecting this specific template. So the main template, I\'m sorry, the main component here that\'s unique is this messy experience.
Component and it includes things such as. I\'m going to scroll this up a little bit so you guys can see how the fields are mapping. So we have our title field, elevate your experience.
With a description that appears underneath. We have a specific image background which shows this burger on mobile. It\'s going to show something slightly different. We have a title field here which is available at a Hard Rock Cafe near you.
And then the additional information section which is this description underneath. And then we have a couple buttons, find a cafe, reserve a table. These two open in a new tab if you select it and then it also opens reserve a table opens in a modal.
Which we can see in a second. So the messy experience component was specifically to be able to display this section here and have it work the same way as it did on the live site where the mobile version is showing something different, slightly different from the desktop.
And also allow for things to have that parallax effect in this section here. O again if we were to take a look at it.
So as we saw how how things were moving around, that is based off of that specific component we took a look at. That\'s why it\'s this portion here is all grouped together and not built with separate components since it needed to function a certain way for both desktop and for mobile.
It\'s coming in from below. It\'s showing that slightly different image.
However, as I Scroll down to this section, so like let\'s take a look here. We saw that there is a parallax effect also for these these two containers as well as these two containers. Let\'s take a look at that parallax effect again.
Scroll down here. So we saw this is coming in from the left and this is coming in from the right. Now that is something that is actually built into the container component. So when we were reviewing the container previously, we only talked about a couple of elements and I.
Said I want to talk more about that in the G light box later. So now let\'s take this opportunity to talk about the parallax tab that\'s within the container component. So I\'m going to select this outer container.
And this outer container contains this specific image and it also contains this container with the title and the text and the button.
So if I click on here and I click on the parallax tab, again this is the container that is surrounding both of these here. In the parallax section you\'ll notice I have a component class name targeting CMP image which is this image here that has that class.
And I said I want the animation class to fade in from right. I also have the option you fade in from left or fade in bottom. And then I\'m also selecting messy right. So this container has a class called messy right applied to it.
And I selected the animation class of fade in left. So what this is saying is OK this container target this element that\'s within this container and have it fade in from right. Target this specific element with this class name.
Within this container and then fade in from left. We took a look at this container here and I Scroll down. You\'ll see in this class messy rate has been applied. That\'s why I\'m able to target it with the parallax tab since I applied this class here and for this image.
I don\'t actually have a class on it. By default the class for all images is CMP image, but if you need it to be more specific, you can certainly change that out and apply a different class name for that, but again for the parallax tab.
I\'m targeting items within the container, the parent container, and I\'m just dictating which animation I want to apply to it. So fade in right and fade in left. The same was done for this section. Here we have our container. I think this is probably called.
Messy left and then here is my image for the parent container. What we did was on the parallax tab. I targeted messy left which is this container and I targeted the image to fade in left. I will pause here and see if there\'s questions on the parallax tab.
Tab in general for the container.
OK.
All right, so I am not sure if the team would be using this, sorry, this template as well as this specific component for additional pages. However, the parallax functionality that I showed within the container here, this is.
Something that is available for all containers, so you can certainly keep that in mind if you\'re trying to introduce any sort of parallax effects within your page and we can certainly we\'ll be going over the container a little bit more tomorrow to go over that final tab.
Of G lightbox. So if you have questions about the parallax you know between now and then, please put in the confluence. We will be taking a look at containers one last time tomorrow.

**Lisa Cardia** 1:02:01
I just have some questions on the messy experience component itself.

**Daniela Tea** 1:02:06
Yep.

**Lisa Cardia** 1:02:08
Um, for the title, can we change the color of the title or we\'re always?

**Daniela Tea** 1:02:15
I think we were doing this literally based off of what the existing page was, and so with the black background, I believe all the text that is on this page was intended to be white.

**Lisa Cardia** 1:02:31
OK, and that\'s because of the template of the page, \'cause I guess I tried this component on a different theme, so that\'s why.

**Daniela Tea** 1:02:37
So so to be clear, this specific component can be used on different templates, but yes, this is on the the template itself. I believe the color the background color was set to black.

**Lisa Cardia** 1:02:50
OK, what else do I have written down there for? There\'s two different options for buttons, like button one and button two, and it\'s just why is button two have the option to open in a modal but button one doesn\'t?

**Daniela Tea** 1:03:06
So I think that was because probably for the live for the live site, it was only the second button that was opening in a modal. I\'m not sure if that was the case for the first button or not, but I believe that was probably the reason why was when this was migrated over it was just.
Ensure that this reserve a table button, which is this actually the same exact one that we\'ve seen on the other pages, was just to allow it to open in a modal. So I think that was the reason why that was just made because this was just to support the reserve a table button.

**Lisa Cardia** 1:03:43
OK, and then for the text in the title on mobile, it looks like it\'s it\'s center aligned but left aligned. I\'m not sure. Was this intentional?

**Daniela Tea** 1:03:55
Let\'s see here we\'re talking about the elevate your experience or?

**Lisa Cardia** 1:04:02
I have just in my notes, so this could have just been from my example, but it went title and text on mobile is not. I\'m sorry, it\'s not center aligned, it\'s left aligned in the center is what mine came to be. So see how they\'re like all left aligned but in the center. Is there a reason that they\'re not? I guess.

**Daniela Tea** 1:04:14
Just left the wood in the center.

**Lisa Cardia** 1:04:21
Center all the contents just left aligned but centered not \'cause see how the buttons are centered but then.

**Daniela Tea** 1:04:25
Um.

**Lisa Cardia** 1:04:30
Everything else is left aligned.

**Daniela Tea** 1:04:33
Yeah, so I would have to reference what the original page requirements were for this. I\'m trying to remember that, so I can\'t answer about what the alignment was. However, excuse me, I think.
I think for this, keeping in mind that like you know these specific components here, at least down here, anything that\'s outside of the messy component, these are just like your standard title, text and container. So you know theoretically that the alignment for that could be set if we\'re talking about the.

**Lisa Cardia** 1:05:01
OK.

**Daniela Tea** 1:05:09
Information that\'s here. This is a specific component, so you wouldn\'t have the same kind of classes that you would for the container classes down here.

**Lisa Cardia** 1:05:16
OK. OK. Thanks.

**Daniela Tea** 1:05:21
OK, so.
Let\'s move on then to the microsite. I\'m going to close out of a couple of these tabs, all right.
OK, alright and a quick note, I\'m working on the microsite currently in the Int environment. We actually were doing a Sage deployment earlier today for the Careers website.
And so some things were were still like loading in the environment while I was trying to set this up. So in the in environment though I did set up the page and so I\'m just showing you guys right now an int. But I just want to make sure that was clear that right now we\'re looking at the integration environment, not on stage. So if you try to find this page.
Page in the stage environment. It\'s not going to be there, but you will see it in the in environment. All right. So when we\'re talking about microsite, this is specifically for so there are some very specific pages that are within the hotel\'s website.
That\'s essentially have like a sidebar navigation and then there\'s like some, you know, cards here on the right and then there\'s like the different things based off of like different locations which we can kind of see here.
This specific template, excuse me, has if we were to take a look at what gets added to this template.
When I create a new page.
Using this template so I click create page and I\'m going to click microsite page.
I.
I click create.
What I\'ll see on the page is something that looks like this where I\'m going to see the microsite navigation.
And I\'m going to see some containers which have some baseline components in here like microsite, banner, space or text. So some items that kind of sets it up. I realize that.
You know, there could be certain pieces of initial content that you guys might want to add to this. Like when we when we were talking about templates and planning out your templates, how the structure, how that gets set up and how if there\'s initial content that you identify that you might want all sites to kind of start out with, that\'s certainly something to plan out.
So right now this is the initial content, but if there\'s specific things that you know should belong, whenever someone creates a new microsite, that\'s an opportunity to identify that and make sure that that gets added to the page. So that way when someone clicks on create new, they\'ll see certain things like say a specific title that you might want to be on all.
Microsite pages or perhaps like specific links that you know belong within the sidebar navigation. So this is it from complete scratch. I want you guys to take a look at one that has been kind of authored. I did not author everything on here, but there are some items here that I want you guys to.
Take a look at. We\'re going to start with the microsite navigation, which is a component that is specific to this template.
I\'m just going to click on Configure.
And we can see that this component has our logo image which gets displayed at the very top on the side. It can also be linked out to a specific page, whether it\'s internal or external, alt text associated with it.
We have a a label for a button that appears above. Essentially it\'s supposed to be how you get back to the page if you want. However, this specific button, if you need to link it to something, it can certainly be linked to something else. However, the intention was supposed to be to link it back to the hotels.
Page. Then we have our NAV items, which is of course our multi fields, home, roots, mottos, etc. You\'ll notice here I\'m actually linking to specific things on the page, so just using anchor tags for these.
And then as I continue to Scroll down, I have my view destinations label which is actually a drop down. Underneath the drop down, the intention for this was to have different regions and then the different locations and then you\'ll notice again I\'m linking to specific.
Anchor tags, since these are things that are on this actual page itself. So the microsite navigation is like a sidebar navigation to literally navigate through your microsite. That\'s the intention for this.
I\'m going to hit cancel and if we were to take a look at this as published, which I have in this tab here, this is what it looks like. I\'m going to click on roots because I had tagged. I had the anchor tag for roots. This specific card here has an ID.
ID of roots, that\'s how it\'s linking to that, anything with like mottos, et cetera. So this is essentially like a slightly differently styled template with a sidebar navigation versus that header and footer experience fragment that we see on like the open page template.
So that\'s why we needed to have a new template for this. You\'ll notice that the cards do look a bit different, and that\'s because if we were to view the card component, this is the same card component that we\'ve been using across.
All of our sites, however, we\'ve just applied a specific style under the microsite variation. In this case we have content left, but there\'s also content right, title right, title black, title gold that can be applied. But these specific styles were intended for use on microsite pages.
When applied. So the styles are essentially making the titles this large gold color. It\'s also allowing for. Let\'s see here.
So essentially like that content left, content right, kind of like our. I think we have split cards that allow you to do that too. However, this is preserving the style that was specifically intended for the micro site. So that\'s why you would select these to be applied to these cards.
See what this one is. So here you\'ll notice it says title small that\'s been applied. So these titles that are here, this title here, that\'s very tiny in comparison to this. So it has a title small class.
So see it with this one title black. By default the titles I believe were intended to be gold, but just allowing some flexibility in terms of how you want to style the cards within the micro site.
So to be clear, the micro-site variations section is actually. I think you would be able to see that on any page if you\'re using a card, but the intention for it is for micro-sites or I suppose if you\'re trying to get that look and feel on other pages, but the styling was created specifically.
For our microsites.
So just trying to show you guys how some of these variations are being applied to the cards, but the main component that is specific to our microsite page is this microsite navigation component up here. Hey Don, I see your hand up.

**Don Middlebrook** 1:13:17
Yeah, um, for those images, um, if we Scroll down.

**Daniela Tea** 1:13:22
Mhm.

**Don Middlebrook** 1:13:24
Do we have uh?
Like the dimensions like to like most of these are vertical and what I\'m looking at because I\'m looking at the side too. Do we have specific like what works best in these placements? This is.

**Daniela Tea** 1:13:37
Mhm.
Yeah. So for this specific page, like this microsite page in general, I believe we were using with the assets that were previously used on the live site. Yeah. And so these were like the assets that were migrated over.

**Don Middlebrook** 1:13:55
Already OK.

**Daniela Tea** 1:14:01
And I think, yeah, so they were just placed here in terms of if we wanted to, you know, increase like the height of the image in order for it to show more or essentially move it around like say you only want to show like this top portion and this portion and not show the bottom portion. That\'s where you would kind of fiddle around with it, which in which position, but we.

**Don Middlebrook** 1:14:01
OK.
OK.
Alright, so it\'s.

**Daniela Tea** 1:14:21
Have migrated over the existing content.

**Don Middlebrook** 1:14:23
OK. I wasn\'t sure about that. OK.

**Daniela Tea** 1:14:25
Mm-hmm. Um.

**Don Middlebrook** 1:14:27
Alright.

**Daniela Tea** 1:14:29
So as we take a look at the microsite page, we understand how it\'s created by using the template. We see that there\'s this microsite navigation component and then as we see here, literally these are components that are.
Kind of global, right? Like the card text component, image component. However, the card component of course has specific styles that are intended for use on the micro site.
So I\'ll pause here to see if there\'s questions about what we\'re looking at.
Actually, let\'s take a look at this in mobile too.
All right.
OK.
All right, so taking a look at our line of business specific agenda here, I will be posting a link for my dining reservation page and sharing that here.
I think Rick, for the Rick, if you\'re still on, I\'ll also see if there\'s any examples of locations that have that different embed. If you have anything that you could think of, you can certainly, you know, send that to me and I can take a look at that.
And in terms of the microsite page, keep in mind again my page is down in the integration environment. If you want to take a look at that I can post it. But again this is this one currently is not on stage right now since I was working in the in environment for this.
Are there any other questions though about these five components and page templates?
OK.
OK. So tomorrow what we will be covering essentially anything that was not covered in our previous sessions, these a lot of these are things that I know that the team is familiar with. So hopefully we\'ll be able to, you know, get through these these.
Those ones up top fairly quickly. We\'ll spend more time though on the card components since there are plenty of variations. I also hope to go over the last tab in the container as well as kind of see some like nesting containers, containers, backgrounds, etcetera. So we\'ll take.
A deeper look at containers tomorrow as well. The tabs cards filter might be new to the content authoring team. I don\'t think this is used on the corporate website, but we\'ll see how that\'s being used on other sites alongside the cards.
The alert and alert aggregator or something that is in our templates but currently is not being used, but I\'ll set up some alerts so we can see how that\'s going to be displayed and how that\'s being used across sites. And I added the list component here because I know we did cover it.
We were talking about how to build lists, say based off of tags or a fixed list or child pages, but I just want to make sure that we examine the rest of the fields if there\'s anything missing. Just want to have an opportunity to be able to go over lists one more time in case.
There was anything else with that specific component, but this is what we plan to cover tomorrow. Any questions about tomorrow\'s session, anything that we were expecting to see that\'s not on here?
All right. Um, I yes.

**Mayte Eme** 1:18:19
Question, but just wanted to let you know that I\'ve been out sick. I\'ve been trying to join these things, so I need to catch up on adding all the questions from the previous sessions. So I\'ll I\'ll try to do that tonight.

**Daniela Tea** 1:18:31
OK. Thank you, Mait. And I hope you feel better soon. OK, so I will put a title on this. I\'m still debating what I want to call it, but I\'ll put a title on this and I will be publishing the link. And when Luke sends out the transcripts and the recording later, he\'ll also.

**Mayte Eme** 1:18:35
No thanks.

**Daniela Tea** 1:18:51
Include the links that I am providing for some of the examples that I mentioned earlier, so please keep a lookout for that later tonight.

**Lisa Cardia** 1:19:01
Is it possible that Luke sends out a little earlier?

**Daniela Tea** 1:19:02
3.

**Lucas Nelson** 1:19:04
Yeah, let me see what I can do, Lisa. Yeah, sorry about that.

**Lisa Cardia** 1:19:09
No, it\'s OK. I just thought they were like automatic and sometimes I forget the questions I\'ve asked if it\'s not sent right away. So appreciate it.

**Lucas Nelson** 1:19:15
Yeah, let me see what I let me see what I can do here.

**Lisa Cardia** 1:19:19
Thank you.

**Daniela Tea** 1:19:19
Mm-hmm. Alright. OK, everyone. Um, well, that is it for today then. Uh, hope everyone has a good rest of their afternoon.

**Lucas Nelson** 1:19:29
Thanks, Daniel.

**Daniela Tea** 1:19:30
Thank you. Goodbye.

**Lucas Nelson** 1:19:31
Bye.

**Lyon, Rick (Director of Digital Experience)** 1:19:33
Thanks all.

Scott Sorel** stopped transcription