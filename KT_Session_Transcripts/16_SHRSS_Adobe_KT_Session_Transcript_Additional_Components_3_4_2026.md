**SHRSS Adobe Knowledge Transfer-20260304_130309-Meeting Recording**

March 4, 2026, 6:03PM

1h 59m 56s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:09
All right, we\'re off and running on the recording, Danielle. Let\'s do it.

**Daniela Tea** 0:12
All right. Thanks, Luke. Hey, everyone. Good afternoon. Coming up with coming near the end, guys, for our content authoring sessions, I\'m going to go ahead and share my screen so we can take a look at what I hope to cover today.
I can\'t think of a fancy name for this topic. It\'s basically here are the other things that we want to make sure that we cover in this final session. However, to be clear, a lot of these items I do believe the team is familiar with. However, there are a couple of new things like the tabs cards filter that will take a closer look.
At as well as the card component. It\'s just looking at all the different variations, but I believe most of these will be familiar to the team, so let\'s go ahead and get started. All right, just switching over to the test page.
That I\'ve made, so I want to just start out here at the very top. Just going to make this a little bit bigger with our button components. So we\'ve seen buttons being used a lot across the site and of course with our button.
We have that ability to be able to of course put the text. You can see my link type here. In this case I have selected a modal which is linking to an experience fragment, but typically for most of the buttons that I\'ve seen on the site, you guys are just using it for the link functionality to link it to a.
External or internal link if we were to take a look at this button as it launches.
Put this you can see here it\'s displaying that parking information experience fragment. This was from one of the cafes I believe. Yeah, Amsterdam. So I was just referencing an experience fragment. So that\'s how you essentially tie a modal to a button by selecting the specific link type as modal.
You\'ll also notice that when it comes to buttons, right now you can see how this is full width. I can certainly set it to be center aligned or right aligned. Yes, the style change because I did not have my primary style selected.
But if I change the alignment, if I need to put it in a certain way, I can do this. However, what we also have underneath here is I have put three buttons into a container and within this container I have set the button group styling to be center for desktop.
Up in tablet. So looking at this right now in desktop, you can see it\'s all centered. Hard to view it in tablet. You can see it\'s stacked without me having to actually change anything. If I wanted to say put them all center across all viewports or left across all viewports, I also have those.
Options there. So by saying left it\'s essentially like this and then if I were to look at it in a similar window you can see it\'s all left aligned. However these will start to wrap depending on the length of the OR the width of the button.
So this is just a way to be able to say group the buttons if you need them to appear side by side. I think we ran into this use case for the first time on cafes and so some of these button group stylings were introduced to support how some of those buttons were handled, but you can certainly just use one.
Button if it\'s needed on the page or you can put multiple within a container and group them just like you can see here. There are some styles for our button. You see how it is with primary. I\'m actually gonna show you the XD file because it\'s going to.
Show exactly how this was handled for the different. Um.
Uh, the different themes. So let me pull that up really quickly.

**Lucas Nelson** 4:13
Why are you looking for that? Rick has his hand up, Danielle.

**Daniela Tea** 4:16
Oh, OK. Go ahead, Rick.

**Lyon, Rick (Director of Digital Experience)** 4:21
Can we see the button on Gray? I just said for whatever reason I just want to make sure I can see it on the right. And then is there any option to make the buttons a a percentage with so like if we wanted to have?

**Daniela Tea** 4:26
Yes.

**Lyon, Rick (Director of Digital Experience)** 4:37
You know, two buttons side by side that were 50% each so that it filled the width on mobile, for example. Are we able to do that or is it all a default with?

**Daniela Tea** 4:42
Um.
So right now, yeah. So right now there was a minimum width and a maximum width that had been established. But certainly, you know, I I believe like this is the kind of information that I think we would want to capture in terms of like how would you want your button to be handled and mobile. So I think what you were saying.
Even though Rick is like perhaps like this might be full width or essentially you know like display block or something within a mobile. So that that\'s certainly something that I would note down right now with the button grouping. What we were focusing on was allowing it to display in Center for desktop and tablet.

**Lyon, Rick (Director of Digital Experience)** 5:06
Yeah.

**Daniela Tea** 5:23
Because that\'s how it was, I believe for cafes and then having it essentially stacked. But for the full width version of this, that\'s something that would have to be noted down.

**Lyon, Rick (Director of Digital Experience)** 5:35
Thank you.

**Daniela Tea** 5:36
Uh, you mentioned something about seeing it on a Gray background. Is that OK?

**Lyon, Rick (Director of Digital Experience)** 5:40
Yeah, like if you could just put it in like turn your one of your containers full width with the Gray background just to.

**Daniela Tea** 5:45
Yeah, let me let me turn this. Let me turn this one. Let\'s see. OK, I would say, so let\'s put this in here. So this is how it look like in a Gray backgrounds. And keep in mind when you have. Where\'s my?

**Lyon, Rick (Director of Digital Experience)** 5:47
Just for the sake of seeing it, I guess.

**Daniela Tea** 6:05
When you have the other themes, certainly the like primary CTA button is going to be different across themes and you can see how like this specific class for the Hard Rock theme that you\'ll notice that the light color is the same as the default color.
Because there was not necessarily a primary light that was established for the Hard Rock theme. However, if I Scroll down specifically for cafes, there\'s a primary CTA button and the primary light, secondary light, secondary. So because these buttons, this button component.
Is going to have the exact same. This is the same button component that\'s used across all the themes. However, the styling of the buttons, specifically the the color of the background and the color of the text is going to change depending on if that button is on a cafe page or hotel page, et cetera.
But that\'s why these specific styles are all here, because they might apply to a theme or they might not. But if you do select something that isn\'t necessarily applicable in the theme you\'re in, in this case I\'m the corporate theme, so I\'ve selected primary and primary light looks the same. That is expected because.
The Hard Rock theme didn\'t necessarily have a rimary light established. If I were to move this button to cafes though, and I selected primary versus rimary light, that\'s where you\'ll actually see like a very clear difference between the two.
Um.

**Lisa Cardia** 7:37
And I have, I have a question with the colors, Daniela, I think we might have mentioned this in the past, but can we do, how would we have the option to change the color of the button if we were trying to like manipulate it for let\'s say a pinktober campaign where we would want to do pink buttons or pride where we do kind of like a rainbow of a sort?

**Daniela Tea** 7:40
Mhm.
Yep. So within the button right now, your options for that would be if you were to write a specific class and like say your developers had specific color classes for your buttons, you could call on that in here. That\'s one option.
So you would need to know what class, like say they had established a class that was called like button pink. If you knew those classes existed, you could call that here. So one option, the other option, and this is something I would advise with great caution.

**Lisa Cardia** 8:26
Sorry for that one though would be like in the style sheet someone would have to make changes.

**Daniela Tea** 8:31
So if say say your dev team you knew that you wanted all specific colors for buttons like say you know pink, red, green, whatever and so they established it within the style sheet. So it\'s then available for you to be able to call through here. So you yourself would not be writing the CSS.
A developer could write CSS and then you would just need to know what the class name is to access it by calling it here. So that would be done through code. The CSS would be written in code, but an author would be able to call the class if they knew what the class name is. That is one option.

**Lisa Cardia** 9:05
Would the code require a development, I mean a deployment?

**Daniela Tea** 9:09
Yes, because that would be entered into the style sheet that\'s applying to the site.

**Lisa Cardia** 9:14
OK.

**Daniela Tea** 9:15
So that\'s one option, second option and this is a component that we are. Um, I was planning going over today, so this is.
A decent time to do it is using the advanced embed component. This is highly I\'m. I\'m basically going to highlight this. We have this big warning on top because essentially what this is doing is you can insert.
Some CSS through here and I believe we might have that in the sign up form just going to the Hard Rock website. So these items here like the stay connected.
Form. This is using the advanced embed component, so you know you\'re able to embed like pieces of JavaScript and stuff in there to be able to display different things. On the other hand, you are able to use it.
We\'re putting some inline CSS for this specific page, but again, highly want to make sure that everyone is aware you can do this. However, I would make sure that if you do this, you know what you\'re doing. So if I were to say right, I could write that same class here.
Right, and I could put whatever I wanted for wrap it in a style tag. I could put whatever I wanted here.
Um, I\'m actually not sure what the color for pink is, but we\'re just gonna do this. We\'re gonna do this. I\'m gonna call it button red.
All right, so done this.

**Lyon, Rick (Director of Digital Experience)** 10:52
You you can probably just give it color pink, the word pink.

**Daniela Tea** 10:56
Well, I wanted to do a hex code, but all right, hang on. OK, one SEC. Yeah, if it doesn\'t work. Alright, so let me add this here.

**Lyon, Rick (Director of Digital Experience)** 11:01
This case if it doesn\'t work.

**Daniela Tea** 11:12
What I call button red?
So let me see. Try to remember if I have to put the period or not. Let\'s let\'s view this as published. Let me see if it actually got applied.
Was it this one or was it this one?
All right, OK, so I don\'t want my red.
I\'m gonna open up my advanced in bed.
Um.
Uh.

**Edwin Aquino** 11:49
You may you might have to also add the important modifier to the background color to override it.

**Daniela Tea** 11:56
We\'ll see. Yeah, you\'re probably right. But but one second, one second. I do want to to do make sure that this doesn\'t have that period in it, which I think it does. So you\'re gonna do this one second.
OK, I have this here and I\'m going to view this and I\'m going to see how it\'s being overwritten.
All right, Yep. So you can see my class is not as specific as this. So what I could do is in order to, I\'m going to avoid putting the important tag just because I don\'t want that necessarily floating around, but that was a good call out.
I think it\'s all at the same level.
Is it?
So, hey, Andy, are you uh?
And are you listening right now?

**Andy Lambert** 13:00
Yep, Yep, I\'m here. What\'s up?

**Daniela Tea** 13:00
I think let\'s take a look at this page. I believe there\'s cause it\'s hanging a little bit on here. It\'s probably the combination of me trying to mess around with the advanced embed while trying to test out some classes.

**Andy Lambert** 13:14
OK.
OK, can you speak the URL over in chat?

**Daniela Tea** 13:16
Alright.
Yes, I can. Here you go. I\'ll send it over. Thank you. All right.

**Andy Lambert** 13:22
All right. All right. Yep.

**Daniela Tea** 13:26
OK, so OK, there\'s a space between that and button.
OK, so we have that. Let me have button red.
Oh, do you not reply?
Um.
Mm.
Let\'s see. Oh, it was this one.
OK, so we have CMP, button and button read at the same level. So I just need to write that at the same level too. All right. OK, so yeah, the important tag would have been easier for this specific demo, but.
Let\'s do this.
OK, oh, there we go. All right, so you can see how I\'ve overwritten the the styling for my button text by having my advanced embed component on here and then.
Is that if I highlight this, you\'ll see my role CMP button in primary, CMP button dot button red has been applied with a specific background color. But as you can also see because I actually put say like you know I took away my space there when I was writing it up in the advance embed and then things didn\'t seem to work.
As planned. That\'s why I do advise caution with using that component. But that is the other option for those who I would recommend people who are more familiar with, say like JavaScript and HTML and CSS to use this component. But this is the way that you would essentially do it. Keep in mind though.
So that if you\'re not specific with your class name, what will happen is it might have some unintended effects. For example, if say another card on here has a class name of something that perhaps you were trying to target, that could also be affected as well if you wanted to change the.
Font on say these cards here, but not the cards everywhere else. You\'re going to have to make sure you\'re extremely specific by either setting additional IDs on the component or make like a very specific class name. So I I just want to strongly advise everyone before they just bust out advanced embeds to do everything there are.
You have to be very careful, but it is possible without a deployment. However, again, the other option is to do it by having the CSS established and then just simply referencing the class name without having to write it up yourself. So Lisa, hopefully that.

**Lisa Cardia** 16:05
I think like I said, it\'s gonna be like on occasion anyway that we would change the color for a campaign, but maybe that\'s a bigger discussion to say, can we limit the advanced embed to even be available just to like a certain group of users just so that no one does use it?

**Daniela Tea** 16:06
Answered.
Mhm.

**Lisa Cardia** 16:20
Um, and adds random code to their pages anyway, but.

**Daniela Tea** 16:23
Yeah, I would. Yes, definitely. I would say we wanna lock it down for sure. And I know you guys are using it right now for like its intended purposes of like, you know, displaying things like this, the form stack form and I think there\'s some other places where you guys are using it, but.
For your Pinktober example, I do believe that page is on the corporate site, right? And I think we were targeting things such as say the card background, right? So like for the overlay card, I believe you know it was like a light pink versus like a darker white and then also just the card colors.
Itself. I believe the way that we did that was with the advanced embed component.

**Lisa Cardia** 17:07
OK. And then I did have a quick other additional question for buttons. Is there a character limit and if there isn\'t, how many characters is it until it it decides to wrap? Because we did notice a lot of buttons with.
Like stacked text, which isn\'t like our yeah, that\'s not really our our standard, but it seems like there really is no way to enforce a limit anyway. So I guess understanding what that limit is before it\'s wrapping.

**Daniela Tea** 17:24
E.
Yep.
Yeah.
So I yeah, so you can see here that the Max width was established at 3:16. For whatever reason that was, I I can\'t answer to that. However, it\'s not so much a character limit, but it\'s more of is that is what is your text going to?
Exceed what the Max width is before it starts wrapping, right? So I\'m like, like I said, like I can\'t tell you exactly how many characters, but it is based off of the width of the button.

**Lisa Cardia** 18:00
Yeah.

**Daniela Tea** 18:18
OK.
I\'m gonna remove this class since it\'s no longer valid. Button, button, button. Trying to think what else we got here. OK, right. So we were talking about the button styles. We talked about two ways to potentially override the button style if you need something outside.
Of the established styles here we talked about the button alignment. So for the button state let me show we have like a disabled version that can be shown like so for secondary light buttons if it\'s disabled it should look like this.
If it\'s a primary button, it would look like this. So that I\'m not quite sure if you guys are necessarily using that, but it\'s just a way to be able to have the button not or visually look a specific way that is disabled.
Oh yeah, of course. There\'s the Aria label that is going to be added to the button, which you would see if you were to inspect it. But are you guys, is there any other questions about the button that we have here? I know you guys are using it a lot throughout the sites, so is there anything else?
On like what you were observing, Lisa, you might have questions on.

**Lisa Cardia** 19:41
I think that\'s my only questions for for oh, I did have one question. There\'s the option to display an icon inside the button and it says that the availability depends on the CMS configuration. So I guess my question is like what\'s an example of this icon and like what are?
What are our options? Can we use like?

**Daniela Tea** 20:00
Yeah, so this I believe is linked to the Font Awesome icon. If you recall, sorry, the Font Awesome icon library. Let me check. I\'m trying to remember some of the class names for this. Um, so this this.

**Lisa Cardia** 20:16
So if we use Font Awesome, it\'ll it\'ll just, uh, use the same code.

**Daniela Tea** 20:21
Yeah, so one second, let me show you how the icon would appear. So you can see here that the FA Chevron right here. So this here like you can see how what I passed in is appearing here, but I need to check to see you know like how this is hooked up.
Font Awesome. We know that we have Font Awesome already available in AEM because we\'re referencing it for like say the dining widget or so. So this one here would be basically putting like specific class names, but I need to get back to you in terms of the proper format for that.
I think though, in the future it sounded like I believe when we first talked about the button a while back, instead of like more like, you know, typing things out like this, I believe it sounded like, you know, perhaps determining what icon library you guys might want to use and then.

**Lisa Cardia** 21:00
Yeah.

**Daniela Tea** 21:18
Perhaps having like a drop down instead or something of available icons, but currently right now it is a text box and you would have to know the class name for it.

**Lisa Cardia** 21:30
Thank you.

**Daniela Tea** 21:30
Yeah.
OK, so that is buttons. I\'m gonna keep moving \'cause I know we we probably want to get the cards at some point. Yep.

**Mayte Eme** 21:41
11 question before you move. I was trying to see the model but it was too quickly and I it when you trigger the model it didn\'t seem finished, it looked weird. So I wanted to make sure if there\'s a yeah is that how it\'s supposed to look?

**Daniela Tea** 21:58
So the modal is simply taking in whatever\'s in the experience fragment. So this is the content that was in the experience fragment. If I can certainly reference another modal when you say it doesn\'t look finished, like if you\'re talking about like say I don\'t know like the padding around here or whatever.
This is going like if I were to change out the content, I have to do at the experience fragment level because I\'m referencing an experience fragment. I\'m not actually like creating a modal in here, I\'m just simply referencing it. So this is where the modal is.

**Mayte Eme** 22:32
OK, so we just you just took an unfinished model just to show us how it works, right? That\'s not how it works.

**Daniela Tea** 22:37
I\'m showing you. I\'m showing you that if I linked so it\'s I could link to. I don\'t know. I don\'t know what\'s in this reserve table. We could try this one.
So this is showing like open table. I can\'t tell you if this is how it looks the experience fragment, but it\'s simply taking whatever you have in the experience fragment and putting it within this modal.

**Mayte Eme** 23:03
And how do you how do you configure that to make it look better than that? Like is that a setting that we just apply?

**Daniela Tea** 23:12
So you would have to go to where the experience fragment is. If you\'re say trying to make it, I don\'t know like add additional space at the bottom or anything like that, then you would add you would edit the experience fragment itself. So right now if I were to go to this experience fragment for.
Uh, I think.

**Mayte Eme** 23:30
I mean, I wouldn\'t go to those widgets because that\'s that\'s another discussion for another day. But like if we wanted to do a regular model, we can\'t use how it looks now. So is there like a configuration for models so they can look decent?

**Daniela Tea** 23:43
The only configuration you have an option between modal and modal small. I was checking to see how that affects the modal and it\'s basically setting like a a Max width. So it\'s based off of the content that\'s in the experience fragment. So I changed it to modal and so you can see this content seems to be.

**Mayte Eme** 23:51
Oh.

**Daniela Tea** 24:03
Is exactly the content that is an experience fragment.

**Mayte Eme** 24:04
Yeah, but but that one was very specific, right? I\'m talking like other use cases. We wouldn\'t use this. So what I\'m, I guess what I\'m trying to ask is are we locked into that look and feel and that\'s it, right? We have to redo it so it can serve.
All our use cases or is there something we can do a checkbox or setting that would make it look decent that we can use it at now or we just got to wait until we redo the whole thing?

**Daniela Tea** 24:32
Um.
I think the only thing I could say is
Depending on your content, right? If your experience fragment, if there\'s things that you need to put in experience fragment, like say extra spacing, padding, anything like that, you would do at the experience fragment level. There is not a setting within the button component to be able to simply change the way the modal looks because it\'s simply taking.
This experience fragment and putting it within that container.

**Mayte Eme** 25:06
I\'ll just add my questions to conference so we don\'t keep going.

**Daniela Tea** 25:10
OK.
OK, moving on to the accordion component. This is another component that I think you guys are using on the corporate website. So I believe y\'all are familiar with it, but it\'s similar to the tab component in the sense that you add your items, meaning your accordion headers.
So I can add multiple multiple headers. In this case I I I know that you\'re able to insert a new component here. What I\'ve been doing is I would typically recommend putting a container component because then you are able to have some additional flexibility in terms of layout and such like that.
But let\'s do this. I\'m going to add another item, all right? And you can see here in my properties I\'ve set the expanded items to be one and two. I can make this a single expansion one and let\'s say I want.
I don\'t want to be open, so you can just see how you can control what you want to be open within the accordion upon load. If you don\'t want anything to be open at all, you can just simply do this so everything is closed at once. I did see a hand up, but I don\'t see any more.
So does somebody have a question?

**Mayte Eme** 26:32
It was Rick.

**Daniela Tea** 26:33
OK, great.

**Lyon, Rick (Director of Digital Experience)** 26:34
Yeah, sorry, that was me. I was just gonna say if you could also show us it on the the Gray background as well, that would be awesome.

**Daniela Tea** 26:39
Oh, sure thing. Yeah. And so something that we we do have two different variations for this. I\'m going to put this in the very background here. We do have different, two different variations for this. We have a basically a transparent variation.

**Lyon, Rick (Director of Digital Experience)** 26:42
Thank you.

**Daniela Tea** 26:59
Which would just make it inherent or or just remove the background color of the accordion. Or if you remove the transparent, it becomes white. So that\'s certainly a whatever preference is needed. I think we\'re using the transparent variation now on the careers.
Website, but for most of the accordions that are on on the Hard Rock, because the Hard Rock website, because it\'s within a white background, you can\'t really tell if it\'s using transparent or white. So this is what it looks like if you were to have the white background. This is what it looks like if you were to make it transparent.
OK.

**Lyon, Rick (Director of Digital Experience)** 27:37
Can you show that expanded with content?

**Daniela Tea** 27:39
Sure, let me see. So we want to add some content here. I\'m going to put title. Oh yeah, because I have the with the background on if I were to take this off.

**Lyon, Rick (Director of Digital Experience)** 27:42
Thank you.
OK, so stays quiet.

**Daniela Tea** 27:56
This is what it looks like. Everything is just essentially one color. Yep.

**Lyon, Rick (Director of Digital Experience)** 27:59
Great, OK.
OK, so in this view there\'s nothing to highlight the title with of the accordion that\'s expanded. So we\'ll have to do that I guess with styling on the title.

**Daniela Tea** 28:03
Alright.
Oh.
So you can let\'s see. So you could see it is a it is a some. There\'s some formatting that you are able to do for the specific title. So like I I highlighted this by bolding it right.
Excuse me, I don\'t think. I don\'t know if you would ever put like a title within the accordion. Maybe you would depending on what content you have. But so right now, if I were to remove this, I think it is a little bit clearer that this is the header just because it\'s bolder than the text that\'s within it.
Um, but yes, there is a little bit of, um, somebody to do.

**Lyon, Rick (Director of Digital Experience)** 28:48
So we can\'t change the size here or give it a heading or anything.

**Daniela Tea** 28:53
So for the size itself, not with the you could, we\'re able to do a subscript and superscript, yes.

**Lyon, Rick (Director of Digital Experience)** 28:58
OK, but we can do it with the visit.
OK, but we could do it with the source if we had to. OK, but no default way to change the size, OK.

**Daniela Tea** 29:05
Yes, you could do it with the source edit if you had to.

**Lyon, Rick (Director of Digital Experience)** 29:14
Oh, properties. OK.
OK.

**Daniela Tea** 29:15
Can be applied, but I don\'t think it\'s very obvious. It\'s more along the lines of like the heading has that structure, right? So now this is an H2. So this this is essentially adding the H3H4 markup or whatever that\'s being set.
In in the markup. So that way depending on accessibility, you know obviously this is never going to be an H1. That\'s why it\'s not allowed, but it could be H2 headers for here. So you can change the heading element markup here to make sure that\'s clear.
All right. Um, and.

**Lyon, Rick (Director of Digital Experience)** 29:52
And you can give it to the class or the ID so you can link to an opened accordion.

**Daniela Tea** 29:58
Yes. So in order to do that, what you do need to do is so you can see here at the very top there are generated IDs for the accordion that get added to each item. So when I click on item 2, you\'ll see this got changed.
I\'ll click on item three, you can see this got changed. So these would be the IDs that you would pass for like a anchor link or something in terms of like having something that\'s more custom than that. Right now the ID that would be applied here is for the entire accordion element.
And you aren\'t able to necessarily set it for the accordion item header, but you can get that generate ID when you view it as published and you can see what that ID is.

**Lyon, Rick (Director of Digital Experience)** 30:53
Got you. OK. Thank you.

**Daniela Tea** 30:54
Yep. All right. OK, so that is the accordion. I\'m gonna keep moving. Yep.

**Lisa Cardia** 31:05
Oh wait, sorry, I I do have a few questions because we\'re we\'re really kind of rushing through these. The FAQ markup, we saw that, but we didn\'t explain if we check this box to show what what does this do exactly? What does that mean?

**Daniela Tea** 31:08
Mhm.
Yep, so checking FAQ markup if I were to view.
You can see how the item type oops Nope, not there. Sorry the item type here. I\'m I\'m looking at the accordion so this is the accordion component. The item type is has the schema.org slash answers and you can see how the accordion item.
Item here has schema.org question, so it\'s essentially applying this item type property within the markup in order to essentially say like this would be a question right? Your your accordion item would be a question or as the accordion item inside of it would typically be the answer.

**Lisa Cardia** 32:11
So this is the schema markup.

**Daniela Tea** 32:14
Yes.

**Lisa Cardia** 32:15
OK. And then my second question before we\'re able to move on to a just a different component is some issues that we\'ve experienced as a team was that when you do add a third item, the container for items one and two are always set to none for width and then adding a third you have to I think.
Set it to content area. Whatever it is that third item, they don\'t have the same settings to get the same alignment for your for your items 1-2 and three. So if you check what items one and two were set to and you added text boxes to both items one and two, and then you added a new item with another text box.
They don\'t all have the same alignments, but then when you try to set them to the same alignments, it doesn\'t work.

**Daniela Tea** 33:01
OK, is that AI guess? Lisa, do you have a Jira ticket that perhaps I can reference so I can understand like?

**Lisa Cardia** 33:10
I like I said, I haven\'t submitted a JIRA ticket since the project pause, but it might exist. I can track this in confluence, but I mean you probably could see it in real time with like once an accordion\'s added to a page just from the start you get items one and two.
And they\'re already set to have their certain container. So as soon as you add item 3 and you want to make item 3 also a text, whatever that container is, it just doesn\'t have the same adjustments. So when you do try to adjust it, it still doesn\'t align.

**Daniela Tea** 33:45
OK, yeah, no, I think.

**Lisa Cardia** 33:47
I I can track it in confluence, but like it\'s definitely a consistent thing we experience.

**Daniela Tea** 33:54
OK. And yeah, no, I would appreciate if that\'s in confluence. I can also take a look in in JERA to see if there are any associate tickets for accordion that\'s having what you\'re describing and if not, I can.

**Lisa Cardia** 34:06
Yeah, \'cause probably even if you just look at your items one, you can see what is that container set to.
Right there.

**Daniela Tea** 34:15
Yeah.

**Lisa Cardia** 34:17
So it\'s not set to anything and so item 2 is not set to anything. But as soon as you add text to item 3, if you can add text to that one instead, because I\'m assuming one and two have text, maybe I don\'t know what they have.

**Daniela Tea** 34:19
Mhm.
Mhm.

**Lisa Cardia** 34:33
Yeah, so add item 3.

**Daniela Tea** 34:34
Mhm.

**Lisa Cardia** 34:35
This way you can see it in real time.
So assuming that we have the container here, I don\'t know if you did that if I missed it, yeah.

**Daniela Tea** 34:43
I yeah, I do.

**Lisa Cardia** 34:45
So this container now if you want to, yeah, just type dummy text. See how it\'s slightly indented.

**Daniela Tea** 34:51
Mhm.

**Lisa Cardia** 34:52
Compared to items one and two.

**Daniela Tea** 34:54
Right. And that\'s just because the width content area or full width has not been uh set. So that is that\'s that\'s why I mean like.

**Lisa Cardia** 35:02
But but if you set content area, it still doesn\'t align. I believe like if you change one and two now.

**Daniela Tea** 35:10
So I\'m going to set everything to full width.

**Lisa Cardia** 35:15
But that.
OK, so.

**Daniela Tea** 35:18
Let\'s see if that works.

**Lisa Cardia** 35:22
So the issue is, or the resolution I guess, is having to change the alignment of one and two because they\'re not preset and then whatever comes after that.
Change it to be the same. I guess to me it was coming. It\'s.

**Mayte Eme** 35:37
No, no, I would say that\'s a bug, Lisa. We shouldn\'t have to be. If one and two are working fine, the rest should work like one and two. If you wanted to change it, that\'s a different story.

**Lisa Cardia** 35:46
Yeah, that\'s where I think as authors we were getting confused to add additional items and since one and two come automatically adding a third fourth doesn\'t add the same way.

**Mayte Eme** 35:51
OK.
Yeah.
Yeah, that that\'s a bug.

**Daniela Tea** 35:59
Mhm.
Yeah, that\'s why I I wanted to see if this was something I was tracked in JIRA, because I know I understand where you\'re coming from, Lisa. And yes, well, I can show you how you can kind of make it work as an author. So that way you\'re not like waiting for like some code deployment.

**Lisa Cardia** 36:14
Yeah.

**Daniela Tea** 36:21
Totally understand that you guys would want to have this track somewhere. So if it\'s not endure though, if you could just make a note on Confluence, I do understand the issue, but I just want to make sure that we have note of it somewhere.

**Lisa Cardia** 36:35
OK. Thank you.

**Daniela Tea** 36:35
Thank you.
OK, um, anything else before we move on to the container?

**Mayte Eme** 36:42
Did I miss how you changed the background? Because I think we had a bug that you couldn\'t even see when it was on a darker background.

**Daniela Tea** 36:52
So there is a background style called transparent that I had set. In terms of changing the background, I had changed the background on the container that this is in. So you can see this has the Gray background here. So it\'s not actually applied to the accordion itself, it\'s applied to the container holding the accordion.

**Mayte Eme** 36:56
OK.
2.
OK, and what about if the background is black? I assume automatically the text changes to white.

**Daniela Tea** 37:17
I don\'t think that is the case right now since this transparent class I believe was added specifically for when we were working with careers. So. So what was established then was just to make a transparent class where it would just have the background color.

**Mayte Eme** 37:37
OK, so we\'ll have to redo this one too. OK.

**Daniela Tea** 37:42
S.
OK, moving on to our container light box. So I\'m not sure if the team had has ever used this feature, but just to be clear as to what this feature is, let me see, is it here OK?
So on the container, there\'s those four tabs, which I know we\'ve been filling out the properties tab in order to set colors and background images. We use the Styles tab to essentially set a lot of, excuse me.
A lot of different styling properties for like widths or paddings. We had the parallax tab, which we reviewed yesterday in terms of identifying pieces of content where we might want to have specific animation associated with it. And then finally there\'s this fourth tab that says G light box.
The check box that says enable G light box and So what I\'m showing here is I just have a container full of some cards. I even have an image here and I have set the container to enable the G light box.
So what happens is when I view, when I click on anything within this container, it\'s going to open it up in a light box. As long as it has an image like you know, like that\'s why I was showing cards and images, it\'s going to open up in a light box. You can just view the images in a light box.
Just like what I showed right there. So I\'m not sure if the team is using this right now, but just want to make sure you all were aware of this feature. Again, it\'s just simply having your items in a container, but I notice I\'m having items that have images.
And then setting the glightbox checkbox to say enable.
I\'ll pause here, though, to see if there\'s any questions about that piece of functionality.

**Mayte Eme** 39:48
I mean, my screen was too small. Can you? And I\'m gonna make it bigger, I\'m sorry, but could you pop the light box again? We\'re trying to capture like all the steps and what everything means to ask the right questions, and sometimes it\'s hard.

**Daniela Tea** 39:55
Sure.
alright. So I clicked on one of the cards within the light box. Um, so oh,

**Mayte Eme** 40:03
Yeah.
No, I\'m sorry. Can you open the settings like the? Yeah. Thank you.

**Daniela Tea** 40:10
Yes, Yep.
So I am targeting my container which contains my three cards and my image. It\'s essentially this right here and within the container all I simply did was on the G light box tab. Excuse me, I just have the the button checked.
OK.
Alright.

**Edwin Aquino** 40:38
Any other? I have a question. I have two accessibility questions regarding the light box. Are users able to like tab to the little X \'cause I know that\'s sometimes an issue with the light boxes where you can\'t close it if you\'re using like tab or.

**Daniela Tea** 40:39
Yes.

**Edwin Aquino** 40:53
Some other option.

**Daniela Tea** 40:54
So I am able to get out of it by pressing my escape button. So I\'m actually not using my mouse, I\'m using my arrow key to go forward and then I\'m using my escape to get out of it.

**Edwin Aquino** 40:59
Escape, OK.
OK.
OK. And then the other question is, I know some users have like a dark mode on their web browser. Is the X visible in that mode? Do you know?

**Daniela Tea** 41:16
Um, that\'s a good question. Um.

**Mayte Eme** 41:19
Where is the X?

**Daniela Tea** 41:21
The X is here.

**Edwin Aquino** 41:23
On the top, top right? Yeah, it\'s kinda small.

**Mayte Eme** 41:24
Why is it so?

**Daniela Tea** 41:25
I do have just just to be clear, I do have a very large monitor, but the X is there.

**Edwin Aquino** 41:30
OK.

**Mayte Eme** 41:32
Yeah, it seems way too small.
Oh my God, there are rows on the bottom. The dust are super small too.
Let me just take a screenshot so we cannot do the list of things to.
OK.

**Edwin Aquino** 41:51
Thank you, Danielle.

**Daniela Tea** 41:52
Yeah. And so just to confirm on what you were asking about how it looked in dark mode, right?

**Edwin Aquino** 41:58
Yeah \'cause I know some web browsers use the dark mode and occasionally since the X is like a text letter, it\'ll convert the texts from white to black and I don\'t know if.

**Daniela Tea** 42:01
I.
Yeah.
I do think.
I think this is actually let me see. I think we\'re using. I believe we are using an icon for this one. So but well, I can certainly check just to confirm that one though. I believe it still should show up as white, but I can certainly check on that.

**Edwin Aquino** 42:27
I appreciate it. Thank you.

**Daniela Tea** 42:28
OK.

**Lisa Cardia** 42:29
And then Daniella, are you able to at least quickly run through just the regular properties of the container? Just because you know, I think most are set to responsive, but just if there\'s any use case of us selecting default and simple.
I think we understand the background color now, but there\'s still like options for like roll, hide container on page, minimum container height. So just understanding all of the different styling options would be helpful.

**Daniela Tea** 42:44
Yes.
Mhm.
Yes.
Yeah.
Yep. And I actually did want to go over. I was planning on going over the the styling options with regards to like cards in here, but we can let us Scroll down and just have another container. Excuse me. And so we can start, we can start from there. So I\'m just going to add a container here.

**Lisa Cardia** 43:14
OK.

**Daniela Tea** 43:21
And I\'m going to change the background of the container so we can we can see what it looks like. So this is just for the purposes of seeing it on the page. All right, all right. So by default, whenever you add a container to the page.
It\'s going to be with the content area selected. The reason why is because and I\'m going to delete that one. The reason why is because within this everything\'s going to be within this root container and if you guys remember when we talked about page templates.
The page template for for example, this is the open page template. It\'s basically the experience fragment up top for the header, experience fragment at the bottom for footer, and then there\'s like this container on the page that essentially allows you to add all the components. So this container is like a full width container.
And so that\'s why whenever you add content in it or containers in it, it\'s going to default to content area. So if you need it to be a another full width container, say you\'re setting like a background image or some or or like a background color or something you want to extend full width, just simply change it there.
And then from here, likely you\'ll want your content to be set, set to be within the content width. So just want to make sure that that\'s like, you know, kind of like the practice is.
This one here is in my outer container that\'s red. This one is going to be set to full width because I want that background color to be full width. The container within it is set to content area and so to see what that looks like, let\'s just make it this color.
So this is likely what most of the content that you guys are doing when you, especially when you guys are alternating colors, you\'re going to want to have that outer container with the background color, the inner container for the content inside of it.
OK, let\'s see. So let\'s take a look at some of the other pieces of functionality. So when it comes to layout, the simple and response grid, so default is actually a responsive grid. To be clear, these two options.
One with response grid means, hey, I want to be able to like adjust columns and you know, do everything that we\'re doing in layout mode where simple is basically like not having all that functionality in it. So if you just need like a simple container around components without.
Say, like wanting to allow for like any layout adjustments, it\'s just going to be like, here\'s like a box full of things in it. That\'s why we had it defaulted to responsive grid, because more than likely you probably do want to make some adjustments to it.
But so by default layout grid is going to be selected. I\'m not clear if you guys have any use cases where you might use simple, but it is essentially to kind of have pieces of content that aren\'t necessarily going to be adjusted by columns and widths.
So that\'s what layout is. Background colors, we can see what it does. The background image. I\'m not sure if you guys are using this currently, but essentially it just sets the background of the container with whatever that image is. And something to keep in mind is that by default containers are not.
Not going to have any height.
It\'ll only have height as you put content in it. That is why there is a minimum content container height down here to be able to set a height so that way I can have the height of something on here without any content in it.
O That is what that specific field does.
OK, let\'s see ID. We know what ID is. That\'s essentially adding your HTML value and you can you can reference that label. This is going to be your Aria, yes.

**Mayte Eme** 47:31
Quick question, is the ID only for let\'s say an anchor or analytics or is that used somewhere else like other places where we had to copy paste IDs because there was no relation to components?

**Daniela Tea** 47:33
Hello.
Oh.
So the ID, let\'s put an ID value here at container. So basically this is just populating the ID for the. Yep, good, I got that. It\'s populating that ID field within.

**Mayte Eme** 47:50
OK.

**Daniela Tea** 48:06
The container. So here\'s my value. How you use it? You know it could be. It could be an anchor tag, right? You might put an ID on the container or say like the title or something. You might use this ID for say JavaScript if you need a target for whatever reason.
You mentioned analytics. Right now I\'m showing you on a container. I\'m not sure when you would be tracking a container itself in analytics, but the ID field should be on every component for you to be able to put a value on and you can see how it\'s getting populated when you inspect the element.

**Mayte Eme** 48:42
OK, so this is not like the other ones where we had to remember the ID because we had to paste it somewhere else.

**Kerry Holyoak (SHRSS)** 48:45
And.

**Mayte Eme** 48:50
And there\'s no validation either, right? Because ID should be unique, but it seems like you can enter whatever you want and you can repeat that idea across anywhere. So if we had two containers, we have to remember the IDs we gave them.
Across any bay.

**Daniela Tea** 49:05
That, yes. So in term, Yep. Sorry, who? Go ahead.

**Kerry Holyoak (SHRSS)** 49:07
Sorry, I have a question. Can those IDs be used in target to target an entire container for a personalized experience?

**Daniela Tea** 49:16
Yes, and it should. Yes, this this should be able to.

**Mayte Eme** 49:21
Remember the names? We\'re gonna have to keep track of them, otherwise you\'re gonna be targeting. Yep.

**Daniela Tea** 49:21
So.

**Kerry Holyoak (SHRSS)** 49:24
Well, yeah, no, I agree that. Well, that the reason I asked the question is because for that very reason what you\'re saying might is well, we\'re going to need a standardized process, right, or some constraints and can that field be, are there rules we can set on that field to force constraints for like a?

**Mayte Eme** 49:32
Mm-hmm. Yeah.

**Kerry Holyoak (SHRSS)** 49:41
A naming convention or something like that? Or is it just open?

**Daniela Tea** 49:45
Um.
So let\'s do this. So I\'ve added container and I just I\'ve added KT container to the other one. Let\'s add it again. So it\'s likely not going to allow me to save it. Yeah, so you can see this idea already exists on the page. Please enter a unique ID. So this is something that we saw also with our content.
And fragments. So I\'m not able to save this or get out of this because I\'m already using this on this page. Now if you guys are trying to have IDs that are unique like across the site, like you know outside of the page, I don\'t think it\'s doing. It\'s not going to do that validation, but it is going to do the validation.

**Mayte Eme** 50:13
Awesome.

**Daniela Tea** 50:26
Within the page itself, OK.

**Mayte Eme** 50:28
Is this the same case from the other one? And I don\'t even remember the component, but there was another one that was also validating that it was unique. But now I\'m wondering if was that only for the page or the whole site?

**Daniela Tea** 50:42
Uh, that\'s really hard to answer because I\'m not really sure what you\'re referring to. Um.

**Mayte Eme** 50:49
There was one. I\'ll go through the through the pages because I know we asked the question where we had to paste an ID, otherwise it wouldn\'t display what it was supposed to display. And now I\'m wondering if that\'s page only or site only because that\'s another fix we gotta log.

**Daniela Tea** 50:50
Uh.
We cancel this and let me go back to our container and I think, yeah, this is it. So let\'s add a label.
And let\'s add a role.
All right, and we can inspect and see how that comes up.
All right, so Aria label, KT label, role, KT roles. So these are just the values that you would put. And again, you yourself wouldn\'t see it unless you inspect it and then you can see how the values are populating and how it would work like for example with a screen reader perhaps.
So let me open this back up again. All right, so we\'ve talked about these fields here. So hide container on page. So you can see here it says check this checkbox to hide container and use page template based on keyword and selectors in the URL. So this one is is I think more of like a.
If you need to hide the container on the page but you don\'t necessarily want to delete it. So if I were to check this, this is not this is only. However this is only I believe on the news page template as it says here so.
I can open that up in a side window so we can see how that works. I don\'t think you guys are actually using this functionality currently. I can check on that but.

**Lisa Cardia** 52:40
So if if we use this on a page, this is different than that feature where we were like hiding on mobile. Like sometimes we actually add content to a page, take it down and then end up replacing that content down the road with something a little bit more refreshed. But the layout\'s already there so we don\'t have to worry about recreating it from scratch.

**Daniela Tea** 52:42
Mhm.

**Lisa Cardia** 52:59
So this would actually be very useful as long as the hidden content isn\'t crawled on the live page. Is that correct?

**Daniela Tea** 53:05
Yeah, So what? So let me confirm what you\'re saying. So you\'re you wanted to make sure like your use case when I was showing how you hide things on mobile, that\'s not necessarily something you would want because you want to essentially set up like the whole layout of everything.
And say mobile and desktop, but simply hide it from the page so that way it\'s not showing right now and it can show whenever you\'re ready, correct?

**Lisa Cardia** 53:29
Yeah, like we might add to a cafe or to like a spa page. It might be the Valentine\'s Day specials, which obviously only work for February. But then in March there might be, I don\'t know, Saint Patrick\'s Day specials. And instead of the author having to now figure out how he wants to lay that out from scratch, we could repurpose the same.

**Daniela Tea** 53:36
Mhm.

**Lisa Cardia** 53:49
One already on the page and unhide it. We like to store content a lot on the back end and reuse it later down the road or already configured. Not saying it\'s like an experience fragment per SE because it\'s not like reused across sites, but.

**Daniela Tea** 53:52
Mm.
OK.

**Lisa Cardia** 54:09
Like on that page level, so it just helps us make quicker updates by repurposing, but I wanna make sure that\'s not crawled if we were to hide it.

**Daniela Tea** 54:17
OK.
OK. So actually Lisa, like what you\'re describing and the reason why I\'m trying to like get clarification on the use cases and this is actually what the purpose of the platform expansion sessions will be. We want to hear these specific use cases like what you just said to understand, OK, is that like is that something that?
Perhaps you could do with an experience fragment, but like you know, hearing as you describe it and we\'re asking questions like, OK, no, is that something we can do by repurposing this checkbox that we have within the container, but we might have to tweak it so that way it\'s not actually displaying and being crawled, you know, so.
Right now, I believe what we have right here, based on what I\'m hearing you from the use case you just described, I don\'t think that this is going to provide everything you need in terms of hiding it from being crawled. I believe it\'s essentially I could display none, but the content would actually still be on the page.
It\'s just hidden, but this is the.

**Lisa Cardia** 55:21
What? What would be the purpose of it then, if it\'s getting crawled but you have it hidden?

**Daniela Tea** 55:23
So.
So this is where this is where I was saying this specific functionality is actually for the news page template. But what I\'m saying is based off of your use case, it could potentially be tweaked upon and repurposed.

**Mayte Eme** 55:41
I I wouldn\'t tweak it. This doesn\'t suffice with the the need because it\'s bigger than just one component. But I wanted to understand what\'s the use case for this. You said news, but what are we hiding the news that gets crawled?

**Daniela Tea** 55:52
Yeah.
Right, so if you I don\'t know if you guys can read this little tooltip, but it\'s say it\'s this is specifically for the news page template. Right now I\'m actually on an open page template, so that\'s why this is.

**Mayte Eme** 56:00
Yeah.
So why is he showing Akers not?
And then.

**Daniela Tea** 56:12
So yeah, I\'m so this. Keep in mind that these containers are going to be reusable across all components. Sorry, across all all templates. However, like we saw with the style variations, the style variations don\'t necessarily apply to all themes.
Some of the fields on some of these components aren\'t necessarily going to apply to all page templates. This specific field is not something that\'s necessarily applicable for the template that I\'m on. This is for the news page template, so I\'m showing.

**Mayte Eme** 56:45
What is he? OK, what is he doing? The new speech number?

**Daniela Tea** 56:49
Yeah, so that\'s what I was showing what the tooltip says. I would need to set up something so we could see that, but I do want to make sure that we\'re trying to cover as much as possible. We have about an hour left. So this one here though, what you\'re describing though Lisa, this is not going to cover your specific use case.

**Mayte Eme** 57:08
No, not at all.
OK.

**Daniela Tea** 57:11
All right, class field. We talked about applying a class and how it gets applied to the container. You could be on the markup. We saw how the minimum container height is set and it\'s essentially adding height to the container even though you don\'t have content in it.
As you continue to add content though, and as it grows, this too will of course grow. It\'s just simply a minimum height. All right, so that is the first tab. Moving on to our styles tab.
We have our width. We can see the full width which is applied to this one here. We see the content width which is applied here. We have borders left and right. Let me see if I can try and apply that somewhere.
Um.
Let\'s see. So you can see this black border has appeared left and right. This is typically actually used I believe down in the footer is where I think I\'ve seen this being used for a container. Essentially if you say have like 3 containers in a row and you want to add borders.
That\'s what the border left and right is. Hide border and mobile devices and mobile slash tablet devices. Keep in mind that the breakpoints that were established were mobile and essentially tablet and desktop were considered to be one. So that\'s why there\'s two options, one for mobile and then one.
For both. So when I shrink the screen down, if these are selected then these borders would disappear if these if these two options were selected the vertical spacing. Again this is being used for I believe we\'re using the.
And this experience fragment which I can actually open up and we can take a look at that. But the vertical spacing allows you to add some space for left up to 40 pixels and from right up to 40 pixels of these set values.
The card styling though is something that I think will be of most importance for you guys as you guys are using a lot of cards. So I\'m going to actually scroll up to this section here where I have these cards set up. I also have this image, but I\'m just going to delete it cause it\'s not a card.
All right, so on my container right now I have set cards list equal space. If I set it two column lists, it\'s going to change it so it\'s displayed as two columns. I can set it to three card list.
So it\'s set within three columns. There\'s also center line, which you can see here. If I hit preview, it\'s there\'s absolutely no space between the cards and then if I set.
End a line. I think you\'re going to see this with some of the other card variations. Keep in mind right now I have the default card set. I really want to get through all these card variations so we can see how that gets applied. But typically what I believe you guys are using when it comes to these default cards in here is.
The cards list this equal space. You\'ll see here though. One second.
You\'ll see here in my container I have my three cards. If I were to add another card, I\'m just going to add another card here. It\'s going to just appear underneath.

**Mayte Eme** 1:00:46
Do you have to? Do you have to add the cards like that? Like one by one? Can we just do a query and just pull them? Does he have?

**Daniela Tea** 1:00:55
There is, there is a. So if you\'re doing a content fragment card list, meaning if your cards are coming from content fragments, there\'s a list list component that allows you to pull those in.
In terms of cards, those like I guess when you say a query, keep in mind these cards are being edited on this page. Like these cards are something I\'m just editing on the page.

**Mayte Eme** 1:01:21
We we don\'t do that. We really don\'t do that manage anything at local level like 1 by 1. So it\'s it seems everything has to be built as a fragment.

**Daniela Tea** 1:01:35
And Yep, so I mean if that\'s the case, like another option is if you\'re using say experience fragments, then you can use these add experience fragments to the page instead. But when it comes to the content fragments, that\'s why I think I\'m not sure might say if you\'re part of the.
We\'re going over the content fragment and the page templates and such, but understanding like what would make a good content fragment model. So you\'re saying that a lot of things are not necessarily local and you know that that\'s fine, but establishing what are the common elements?
For these items, that way you can build out the structure for that content fragment model. That\'s something you know that that certainly would be beneficial if you\'re if you know for a fact that like these cards can be used across multiple sites or multiple pages, but you just have to define what the model is.

**Mayte Eme** 1:02:32
Yeah, I was watching that the other day and I\'m still very confused about the whole thing, but we it\'s more than just repeating on pages.
That it shows on one or the other, it\'s.

**Lisa Cardia** 1:02:46
I was going to say to add a great example is that a cafe author should not even have to configure 1212 different checkboxes and settings to get the card to look how it should in the breakpoints that it should. This would have ideally been set up as just a content fragment feeding in so that they don\'t impact UX at all.

**Mayte Eme** 1:02:54
I know.

**Lisa Cardia** 1:03:06
So it\'s not necessarily reused, but still a fragment so that we don\'t break anything because there\'s a lot of room for error with how many settings can be adjusted, especially if certain settings need to be trained to say this is available to you, but actually not for your theme or not for this style card, because there\'s really no clear.

**Daniela Tea** 1:03:16
Mhm.

**Lisa Cardia** 1:03:26
Indicator as you pick styling efforts that like your first option for styling is only meant for a card that is horizontal and has a shadow. Like there\'s really no grouping of the stylings. You can check off as many or as little as you want.
Does that make sense? There\'s really no like construct constraints.

**Mayte Eme** 1:03:47
No, and the more I see this, we\'re gonna have to adapt because one like all these checks and settings that you have to like literally trial and error until you get it right. It\'s just too time consuming.

**Lisa Cardia** 1:04:01
Yeah, and it\'s not like based on logic, so that if you were to choose, let\'s say the horizontal card, that certain variations remove from the list because obviously you wouldn\'t want to use them, but instead they\'re all available.

**Mayte Eme** 1:04:04
No.
Yeah, I\'m just scared of the limitations of those fragments and if it\'s really gonna work, so.
I\'ll let the question so we get answers and and decide how we\'re going to use what has been built until we can redo the whole thing and and and use it for our business.

**Daniela Tea** 1:04:37
Um.
Well, let\'s see what else we have here for our container. Let me see. I\'m going to go back down here to my container I just made for the purpose of this, and I\'m going to actually open up the styles tab.
All right, we looked at card styling, which was above used with cards, footer, wrapper. So these items here are specifically for the footer. Keep in mind again, yes, containers are global.
But to your point, Lisa, understand that like since you\'re not having a footer necessarily being built within the main page, sounds like there would be a desire for some conditional logic to hide some of these things that shouldn\'t be on the page. But footer wrapper is available because this is something that would be applied to containers within the footer.
The messy burger style. This was something that was applied to a container that\'s that was specifically for that messy burger page. So again, sounds like this would be something that could also potentially be hidden for outside of that template.
Padding. It\'s either you have the built-in padding that was established or you have no padding depending on what you select. The border color. When we had selected borders up here, you\'re able to set it border black, border Gray.
Those are the two options, and I know that there\'s also a border here. I think this is something that should have been consolidated where it says red border. This was specifically, I believe, for the cafe sites, the ability to put a red border around some of those different divs.
Text alignment, setting the text either center, right or left. With this specific container we have content alignment, so not just text, but setting content that\'s within the container center horizontally or center vertically.
And then we have the button group styling that we saw up top where I had set the center desktop slash tablet for that group of buttons above. Let\'s see. So one second here I\'m going to put back my image.
We\'re actually, I\'m going to let\'s remove this card and I\'m going to make this card have a lot more text.
My X button\'s not working. All right, so I were to remove my card list. You can see now how things are not going to be evenly spaced. Things are not going to be the same height.
If I were to do, let\'s see.
My two column list, it pushes it down. If I were to add more to here, it\'s just going to keep it within two columns. If I continue to add more, it\'s just going to naturally keep going underneath and across. I can change this also to my three column list.
Um, which is?
Again, if I add more, it\'s just going to keep going in threes underneath. All right, so.

**Mayte Eme** 1:08:16
So so you have to do 1 by 1 to make sure they have that same high and if you add more text then you gotta go back and tweak all of them again.

**Daniela Tea** 1:08:25
Hang on, if I were to add more text here.
I hit done so right now you can see it.

**Mayte Eme** 1:08:33
So it\'s not like it\'s smart enough cycle to know and grow based on the highest.

**Daniela Tea** 1:08:39
So you can see right now this is truncated. So this this specific card has truncation applied to it by default. However, on the card itself you can turn off truncation if needed.

**Mayte Eme** 1:08:43
OK.

**Daniela Tea** 1:08:54
So that is at a card level. So if I were to turn this off right now, no truncate description. So it\'s you know, depending on like I believe for some of the cards you guys do have a truncate I think with like the news card if I\'m not mistaken.
So the truncation is added by default, but you can turn it off and you can see when I turned it off here it expanded the height of the other cards.

**Mayte Eme** 1:09:21
So because of Newsroom is default for all of them instead of just for Newsroom.

**Daniela Tea** 1:09:29
Since I think that was probably the first one we worked on, but I mean there\'s this is something again, like if it\'s OK, yeah, the card should always not be truncated and then have this essentially have this essentially be like the default.
That that\'s certainly something and you know during the platform expansion discussions that can be noted for sure.

**Lisa Cardia** 1:09:52
Well, what additional setting do you have to these cards right now? Because when we did the cafe content validation months ago, all of the cards were different heights. Was that because it was migrated without a container with the settings because?

**Daniela Tea** 1:10:02
Mhm.

**Lisa Cardia** 1:10:07
They were all all different heights.

**Daniela Tea** 1:10:10
I believe that these so right now I have it set to three column list. Um.

**Lisa Cardia** 1:10:15
Mhm.

**Daniela Tea** 1:10:16
As you can see under the card card styling, this is on the container. I believe that some of these were additional variations that were created as we were working on the cafes.

**Lisa Cardia** 1:10:31
Sorry, I\'m not understanding. So like, there\'s new cards now.

**Daniela Tea** 1:10:35
No, I\'m I\'m saying like when during that time, I don\'t remember when that was, maybe it was like October or so. Our team was also working on some additional style variations. So like they were added there, but when it was migrated, I don\'t think those variations were necessarily available.
Mobile.

**Mayte Eme** 1:10:55
So with these variations, we don\'t have to configure each one one by one to be the same height. We can just apply that to the cafe.

1:10:56
OK.

**Daniela Tea** 1:11:06
For at the container level, yes.

**Lisa Cardia** 1:11:09
If there\'s a container on the page from migration.

**Mayte Eme** 1:11:13
So we love it as a bug and then that can get fixed because it should have been migrated properly, right?

**Lisa Cardia** 1:11:22
OK.

**Daniela Tea** 1:11:27
All right, OK, let me see what else is in the container. Styles, border, border, parallax. We went over to like box. We went over. OK.
I wanted to get to something I think which is brand new to you guys 1st and that\'s this tabs cards filter and then we can go back to the actual card styles itself. But this is something I I don\'t know if the team has actually used before, so I just wanted to show that.
So the way that this works and I put this note view as published because if I were to interact with it right now in the preview mode, it\'s not it\'s. It doesn\'t work as as it will for the end user when you view it as published. So I\'m going to view it as published which is.
Right over here, just refresh this and so the tabs cards filter. I have my 6 cards here. You\'ll see I just put spring, summer, fall, winter, spring and fall and just description as to when I\'m expecting this to be shown.
And So what it does is it just displays the cards which is associated with the tab on top. So I\'ve clicked summer, so I\'m seeing summer. I\'m seeing my summer and winter card. When I click on winter, I see my winter card on my summer and winter card. Click on all, I see everything.
So this specific component I think is likely on the hotel pages and the way that this is authored is.
I have my tabs that I\'m able to establish. So you\'ll see here I have my all tab label all offers and then here I have specific category filters. So here I have the label for spring offers.
I have my summer offers, fall offers and winter offers. So those are all the labels that are on this button here and then here.

**Mayte Eme** 1:13:28
So one one quick question because to freaking out, is this the only cards that we can use with these tabs?

**Daniela Tea** 1:13:37
What?

**Mayte Eme** 1:13:37
Hey.
So you have the tabs, right? All offers and spring offers. I don\'t know what offers we would use like this, but fine. And then you have cards below 6 cards. Is that the only card variation that you can have below the tabs?

**Daniela Tea** 1:13:50
No, I have not. No, I have not gotten to that yet, might say. OK, all right.

**Mayte Eme** 1:13:54
OK, OK, that was very scary.

**Daniela Tea** 1:13:57
So here I\'m showing the button label or the tab label and I\'m showing a name. And so this name is essentially the category filter name. I\'ll show you where this is used in order to attach the cards to these filters. I\'m going to keep scrolling down.
I have my column layout set to three. I could set it to four. Don\'t think there\'s a limit, but I think there would be you would want there to probably you would probably do three or four I would imagine. But right now I have it set to three and I\'m going to click done.
So now within the tab card filter I have the ability to add cards. So I\'ve added 123456 cards here. I can add more if I want. Let\'s go ahead and do that right now.
So I have my a new card here and this card is the same as all my other cards. I am able to put an image, I am able to put my text.
I\'m able to put a a link to here, right? So this is the exact same part.

**Mayte Eme** 1:15:01
Does it only take? Sorry, does it only take manual cards again, or can we just query and pull a list from whatever criteria we need?

**Daniela Tea** 1:15:11
So keep in mind I just wanted to show this on each of these cards. What I have here is a specific category. So this category is associated essentially with those buttons there. So in terms of the list.
Thinking.
I I think right now this is hooked up to be individual cards to match with these tabs.

**Mayte Eme** 1:15:43
Does that mean we can\'t query like query experience recommends or does it have to be local at the page level and manually 1 by 1?
Because if we\'re gonna have offer like I\'m just using the use case that you have right offers, we can be recreating offers. We gotta pull the ones that we already have.

**Daniela Tea** 1:15:55
Um, so.
Yeah, no understood. I think for this here you are able to add additional components like this one. This one you know you can say I can add an experience fragment. However, what this has been tested against is for the like specific individual cards I understand.
What your use case is where say you have a list of cards where it\'s things that were all say located in a specific area or based off of a specific keyword or perhaps even A A tag like say you want everything that was tagged as like from this specific hotel.
So right now though, what we had created against was on individual local cards, but that doesn\'t mean you know in the future that that cannot be enhanced to be able to pull in things based off of say like a content fragment card or something.
Right now though, with the card itself, we have that categories field here, which allows you to be able to associate the individual card with the tab that you created in the component.

**Mayte Eme** 1:17:12
OK, I I really don\'t see a use case for this. Um.
I don\'t know what we will use this for. If it\'s manually creating cards, seems like too much work.

**Lisa Cardia** 1:17:22
I also am just a bit confused on like the difference between this and tabs itself. Like is tabs not the same? Couldn\'t we have added cards to the tabs other other component we learned?

**Daniela Tea** 1:17:33
So yes, you could. You could do that. However, keep in mind that I mean I have one card and I\'m able to oh sorry because remember view is published. I have my I\'ve created all my all my cards on the all offers tab. However, I\'m able to display it on different tabs without.
Having to make copies of that card, right? So yes, well, you could do it. Like say you had a tab called Spring Offers using the tabs component. So you\'d put two cards here, right? Then if I go to fall, I\'ll put another two cards here.
But what I\'m saying is like I only have one of these cards. If you do it within tabs, you would have to create this card multiple times to appear on both of those tabs.

**Mayte Eme** 1:18:18
OK.

**Lisa Cardia** 1:18:21
Got it.

**Daniela Tea** 1:18:21
Yeah. So that\'s where the, that\'s where the, that\'s why there there\'s that categories field down here at the bottom. That\'s what this is used for. It\'s associated with the categories that you had established at this component level here. So these are all the categories.

**Mayte Eme** 1:18:40
What will what will be the difference between using actual filters right where we can filter by category and versus these tabs?

**Daniela Tea** 1:18:41
I am using.
What do you what do you mean? Like what are you referencing when you\'re saying filters?

**Mayte Eme** 1:18:55
Then we have filters when we have offers and promotions and we can filter by different categories.

**Daniela Tea** 1:19:01
So we do have the promotions component which is linked to the promotions content fragment.

**Mayte Eme** 1:19:02
OK.
Yeah.
Yeah. So what would be the difference of just?
The look because it is.

**Daniela Tea** 1:19:13
So this is the promotions, this is the promotions, the promotions component and then we also have the destination and.

**Mayte Eme** 1:19:25
And the events.

**Daniela Tea** 1:19:26
Search and filters. So keep in mind that these components are tied towards specific content fragment models. This here is saying if you need to make something where it\'s you know like it\'s not so much. This is not content fragment based, at least not at this moment. This is something if you need to create it, you don\'t have the content.
Fragment model, but you need things to be filterable like a card level. You would create all your cards in one area, just this container. As long as you tag it correctly in the category section, you\'re able to essentially quote UN quote filter it with the tabs above as long as the categories match.

**Mayte Eme** 1:20:04
It seems like it\'s the same. It accomplishes the same in a way functionality, just more complicated. Is there a way to hide components from users selecting them and using them? Like how do we do that to avoid people from using this?

**Daniela Tea** 1:20:20
So that\'s gonna have to be something established at the permissions and user group level. So like so I think you guys had mentioned for example the advanced embed component, you guys would probably want to, you know, lock something like that down.

**Mayte Eme** 1:20:36
Yeah, it should have never been that open. Yes, too risky for people to break things. OK, so that\'s good to know. Thank you, Daniela. We can restrict based on user access what components they see because it seems like we have, I don\'t know, 3-4 things that do the same. So if we can limit to the one that we actually know how to use and has.

**Daniela Tea** 1:20:41
Mhm.

**Mayte Eme** 1:20:55
The least amount of steps the better.

**Daniela Tea** 1:21:02
Gonna remove some of this here just so the page doesn\'t have to grow.
OK, all right. So tabs, card filter, card carousel, which is kind of linked to cards. I think I know you guys probably want to talk more about the card styling.
Just preview. OK, all right, so cards. We are using cards everywhere. Right now we have the call to actions here. I put two versions of this to kind of show when the text is.
You know, a certain width or whatever. It will be a full width button on the card itself. So this is just to show how that looks.

**Mayte Eme** 1:21:49
Is that automatic or is that a setting where you say one is stacked or side by side?

**Daniela Tea** 1:21:55
No, it\'s if I were to like put stuff like this here. Hang on.

**Mayte Eme** 1:21:59
Because we might have shorter words, but we want them as stacked versus side by side.

**Daniela Tea** 1:22:03
OK, well, so it\'s automatic in the sense that it\'s based off of if you have enough text to make it wide enough.

**Mayte Eme** 1:22:12
OK, that\'s not right. OK.

**Daniela Tea** 1:22:15
Alright, let me put this back.
So it\'s other.
OK. All right. So taking a look though at some of the card variations. So I was trying to also show just a couple of the variations, but we can certainly change them here right now on the fly.
I think we have seen the primary and secondary button default card on several sites right now. What I did want to highlight though is that this specific card again keep in mind that this is the buttons are theme driven. So if I use this card in say a.
A casino, A casino theme site or like the hotel or the cafe, the buttons will be whatever colors were established for that. Same thing with the tertiary link. We can see here how it\'s gold. Sorry, it\'s in the edit mode. There\'s that slight overlay.
But you can see how how it\'s gold. That\'s again based off of the theme. If I were to select the overlay card, this is how it looks. So for vertical, horizontal, because I\'m at this specific width, I don\'t think you\'re you\'re really going to see much, but I think this.
This is used on the news website, so full width overlay cards. I\'m going to Scroll down to where I have something that is full width.
Oops.
All right, so I have this is split card. I\'m going to select my full width overlay card so we can see when it\'s right content, how the content displays here with this specific.
Uh, slight overlay left content. It moves.
Full with right content. This is making it white and then this makes it white on the left. Switching to split card image on the left, image on the right.
List card variation. The content is wider and the image is smaller. And something I did want to note is you may be wondering, OK, well how come like the image is just, you know, looks a certain way. I have used the image position for this.
This specific card, so you know this is this is where the image position tab tends to be used. If you\'re using a specific variation and the image is like perhaps not showing the focus focus on on the subject, if I were to remove this.
I hit done.

**Lisa Cardia** 1:25:03
I think one one of our gaps with the image position we did notice is that since the tablet and desktop, if we can take this down on our end was grouped together, it it doesn\'t work well because tablet shows such a different.

**Daniela Tea** 1:25:09
Mhm.
Mhm.
Yeah, tablets should be split out is what I believe, yeah. Mm-hmm.

**Lisa Cardia** 1:25:19
Yeah, tablets should be split, yeah.

**Mayte Eme** 1:25:21
I think that\'s across every single component that has an image, right? We have to redo that part because it\'s not looking good. Even the websites that we have live, it looks really bad on some specific widths.

**Lisa Cardia** 1:25:29
Yeah.
Yeah, because like, I know that the thought behind that was that we use the same image from for desktop and tablet on the hero banners, but that\'s because on our production sites it never changes like their widths, but since it\'s actually manipulating it in AEM.
We do see the difference.

**Daniela Tea** 1:25:53
Mhm.

**Mayte Eme** 1:25:54
Yeah.

**Daniela Tea** 1:25:57
Let\'s keep going. Yep, go ahead.

**Mayte Eme** 1:25:57
Yeah, and.
No, I was going to say that\'s a big issue, especially with entertainment and cropping people faces and and it\'s we got a that\'s one of the high priorities if we want to launch any other site.

**Daniela Tea** 1:26:10
Mm.
Yep. OK, so I wanted just to point out that up to this point here before it says additional style group borders, so.
In terms of guidance that I\'m providing, um, typically you\'re going to only select one of these from like, so like one of these up until this point. But when you get to the additional style group here, these items can be applied. Um.
Can be applied to the card in addition to whatever you had selected on top. So like when I select default card or primary and secondary button and this looks kind of weird because I don\'t have in a container, I haven\'t set the width when I set this here and I\'m clicking somewhere else right now, yes.
It does essentially stack and I can certainly see that that can be very frustrating if you\'re trying to have a specific look and you\'re messing around with the style and you\'re saying, OK, I this looks OK, but that\'s not actually what you want. So some guidance for the team is that default card.
A card, et cetera, et cetera. All the way up until you get to this additional style group is typically supposed to be. You select one of these and that\'s the variation that you would want applied to your card.
So in some cases it\'s going to look fine if you have multiple applied. It\'s not really going to have too much of an effect, but you might notice some wonkiness though if like you have say this selected and like that selected. So some unintended behaviors may occur.
So just wanted to provide that kind of guidance. OK, but with that being said, so let\'s keep going down with the styles underneath. We also have some borders. I think by default you\'ll see like a a shadow.
Underneath the card so that that\'s like the base card. If you especially if you have, if you have one of the cards that\'s not an overlay card, you you would likely see a shadow and a border and so this specific style.
Where the border group just allows you to either show a border or remove a border, show the shadow or disable the shadow for background color, transparent background. You\'re not going to see this on here. I will need to find an example for you guys to see how this works.
For microsite variations, this is what we were looking at yesterday when we were reviewing the microsite template, the content lab, content right, etcetera. All of these were created specifically for that microsite template and the use of the cards on there.
The messy card variations, these were used specifically for the messy template. We have the image height variation for some of our cards. We can see that if I select no minimum height, it essentially is saying OK for the default card there is a minimum height that\'s established here.
There\'s like some height restrictions for some of these variations. If I don\'t want to have that applied, I can select this so that way it will essentially show the full image like we see here. So now it\'s very tall, which could cause problems if you\'re trying to have.
Multiple cards on a page and say your images aren\'t all the same. The default card is supposed to kind of standardize that by only having a specific height. But if you do need to show the full image for whatever reason, that\'s why that is there. The icon card variation. We see that for the.
Careers site. I\'m just going to Scroll down here. So these are using the icon card variation. It\'s going to be essentially like an icon, AKA an image of an icon or whatever, however your icons are stored SVGS or something.
And then with the text underneath, but this is a card component, so I\'m just going to go back to where I was. So right now this looks kind of silly because I\'m not actually using like an icon, I\'m using like a full-size image, but that is what this is for.
Uncheck that and then the no no truncate description. If I have a very long description which is not on any of these right now, let\'s take this for example and this is this is the same. This is this is the same thing in terms of the styles for the card carousel.
And the card are going to be very similar, if not the same, but you\'ll see here I have no truncate description on this. If I have it unchecked, you\'ll see that it\'s trying to essentially make the cards a little bit smaller by only showing 3 lines of text instead.
And I do realize I\'m, I am going quite speedily and that\'s simply because I know that you guys probably have a lot of questions about the cards and I want to make sure you guys have time for that. But in terms of what you guys are, how you guys are using cards right now?
I think Lacy, you had, you know some some good use cases with regards to improving the selection of the groups if something is essentially supposed to be applied once, kind of trying to see how that can be enforced versus.

1:31:39
Yeah.

**Daniela Tea** 1:31:46
Having multiple be selected, but just curious to hear of some other use cases or questions about the cards.

**Lisa Cardia** 1:31:55
I think along with just the, you know, the conditional styling of when an option is selected that other options go away of course, is that we find a lot of trouble with these because they will accept any image and even if you have the same styling selected, the image dictates what the card looks like.

**Daniela Tea** 1:32:08
Mhm.

**Lisa Cardia** 1:32:14
Rather than the opposite. Now I think that\'s that\'s a huge gap and a huge problem honestly for the UX of our sites. Because even if we had selected horizontal card, shadow, border, what have you, whatever image gets thrown in there dictates the card look so.

**Daniela Tea** 1:32:19
Mhm.
Mhm.

**Lisa Cardia** 1:32:33
I don\'t know how we fix that and set better constraints that way, but that all stems from the fact of of course us needing the image dimensions per card style variation, which I know you were working on the confluence page for, but it seems that even with that.

**Daniela Tea** 1:32:47
Mhm.

**Lisa Cardia** 1:32:49
It\'s still not a perfect science because the image is dictating the card rather than the opposite is what we\'ve noticed.

**Daniela Tea** 1:32:58
Right. And out of curiosity, like I guess I would if you guys can send me like just like a page or two, like I understand what you\'re saying, but I do also want to like kind of see the use cases that you guys have and this can be something that we can talk about during the platform expansion because like I know like you know what I\'m.
It\'s like, yeah, I have an image and it just happens to work. Yes, while I did set the image position for this one to make the focal point, you know, more like this. I\'m just, I just want to kind of see like the kind of content, you know, like how many lines of text are you guys using? What kind of images are you guys using? I just want to kind of see that.
Maybe play around with that a bit, but definitely noting, you know, like it\'s noted what you said about the image height dictating the card versus having some restrictions on the card itself for the for the image.

**Mayte Eme** 1:33:49
And to be honest, I think Daniela, this, this card is a whole refactor. It\'s just I don\'t think it was.
I think it\'s a lot of settings that contradict each other and it was not built for content authors, right? It was if you click this, this is your outcome. If you click this, this is your outcome, this and this, this is your outcome. But it wasn\'t. It wasn\'t built with our content authors in mind. So that experience is very poor right now and we\'re going to have to.
Refactor a lot of components that I would say this is one of the biggest ones.
So I get understanding the use cases, which obviously helps, but it\'s it\'s a redo in my opinion.

**Daniela Tea** 1:34:23
Yes.
Yep.
All right.
Let\'s see here.
OK, so yes, lots of styles that were added in order to essentially try and support some of the styles that we knew we had to migrate over. I am going to go to the card carousel which is linked to the cards.
And I think so right now what I\'m showing, I\'m actually using the example that was, I think that\'s currently on the careers website with our card carousel. I think you guys are fairly familiar with it, but.
What I just wanted to highlight was that the styles here as you selected here it does apply to all of the cards within it like we saw. So right now default card primary and secondary button is selected if I select the tertiary link.
That gets applied, so all the cards are now updated and I think let\'s see like we saw with the truncating description, having some control of the cards all within a group. Essentially for the card carousel though, it\'s it\'s pretty similar to I think the carousel you guys have.
I\'ve used. Keeping in mind though, this is restricted to only cards. This is called a card carousel. That\'s why it\'s only cards. So you can add as many cards. I believe there\'s no restriction in terms of how many cards you you can add to your.
Deleting them, of course, reordering them, et cetera. Setting the active item, essentially what should be the first card that actually gets displayed. This is similar to what we saw with our accordion component.
The ability to transition the cards. So we wanted to. I\'m going to make this really short just for the purpose of showing it. If we wanted to have the cards kind of move on their own, that\'s something else that that can also be done.
So you can see I was just moving without me interacting with it, but I think that is not checked by default and you guys are not currently using that right now. So I\'m just going to uncheck this and then I have my carousel slide indicators underneath displayed.
And we talked about how right now I don\'t think the tablet slide counts field is currently something that was taken into consideration because of the fact that the begin the project, the whole breakpoint established desktop and tablet were the same.
So right now this field is is there, but it\'s not necessarily something that I think we mentioned we we wanted to clean that up. However, the understanding that there is a desire to have separate breakpoints, one for desktop, one for tablet, one for mobile.
It seems like it would make sense, you know, for this as well as other components to have it tablet split out to be able to have more control with this new established break point. So while this is not necessarily something that is currently being used today, it sounds like this is something that is desired and needed for the future.
ID and class just like we saw on every other component, how this gets appears in the markup. We have our accessibility tab which also again in terms of screen readers and you would see it in the markup when you put values here.
And then the styles tab we kind of already reviewed questions about the card carousel component.

**Mayte Eme** 1:38:14
I just want to confirm that we can pull content right when we move, because this all has to be moved to fragments, so we can pull lists. It doesn\'t have to be manual, right? There was that setting where you were hiding where you said you can add unlimited cards. That\'s just an option, right?
We can add them manually or we can just pull and say this list based on this criteria.

**Daniela Tea** 1:38:34
Oh.
OK, so something I wanted to make sure you were aware of currently right now these specific cards, at least in the career site, while they are, these are manual quote UN quote localized cards. However, these have been stored in an experience fragment and so they are essentially being reused.
Used on multiple pages within the careers website. You would update it once in the experience fragment. When you make the update, say you have to add another card to that, you can do that there and then all those pages would be able to reference it and have that new additional card. So that\'s the current use case for today.

**Lisa Cardia** 1:39:11
But to be clear though, we we couldn\'t use different variations for that same experience fragment, correct? The experience fragment would have to be designed as a carousel and not as a list. Like we like to use the same source of. If there\'s 10 cards in this carousel, these 10 cards might be listed on another page, but as.

**Mayte Eme** 1:39:12
Thanks.
And so that.

**Daniela Tea** 1:39:23
The list.
Mhm.

**Lisa Cardia** 1:39:31
A a list. We weren\'t able to use the same experience fragment for that.

**Daniela Tea** 1:39:33
Oh, right.
So, yes.

**Mayte Eme** 1:39:36
Oh, so we can we need that to just one variation? Well, OK.

**Lisa Cardia** 1:39:42
Unless I\'m I I I\'ve learned that recently. So if I\'m if I was miss misspoken, please correct me. But I believe that we wanted to have these same sources just displayed differently, but same content.

**Mayte Eme** 1:39:48
Mm.

**Daniela Tea** 1:39:57
Yeah.
So.

**Mayte Eme** 1:40:01
So we still end up managing more than one in one plan.

**Daniela Tea** 1:40:01
So.
So this is so when we were talking about content fragment models. So this is where again like yes, I understand you know wanting to reuse this content elsewhere like the reusability shared content etcetera.

**Lisa Cardia** 1:40:17
Yes.

**Daniela Tea** 1:40:20
So like for example this could be this would be something where perhaps a content fragment model might be appropriate for say this is I\'m not sure like Hard Rock brands or or lines of business or something right? I\'m not sure what the exact term would be for that.
But then of course identifying what you would want to be stored for that right? Like an image, title, description, the apply now CTA link, the learn more CTA link, right? So understanding what that structure is.
And then from there, that\'s where this would eventually be able to be reused across multiple pages from the content fragment being the data source. So right now that content.

**Mayte Eme** 1:41:02
But to Lisa\'s to Lisa\'s questions, it can only be used as a carousel if you apply it as a so you set it up as a carousel. That\'s it. You\'re you\'re set to only use it as a carousel. If I wanted it in a list view or or a grid, I can\'t. I will have to.
Have another set of fragments that have exactly the same content, yes, so I can have the two different looks.

**Daniela Tea** 1:41:23
So.
Right, right now. OK, so right now like this specific card carousel component has individual cards within them. Currently we are using an experience fragment to reuse the card carousel on multiple pages, but only edit it once. Now what you guys are talking about is the shared content.
Aspect of having this be displayed in different ways. While there are different variations you can apply to the cards in here, right? It\'s like there\'s a list card variation. However, I don\'t think this is necessarily going to accomplish what you need because in this case here I\'m going to change this to one.
And then I\'m going to change this to here, right? So I don\'t think it\'s necessarily going to accomplish what you need, but what you guys are describing though would be creating or establishing what a new content fragment model would be for this, having this content then be added as as content fragments based off that new model.
And then you would be able to reuse that in multiple ways and display it in different ways. Right now there\'s no content fragment model for this specific type of data that we see here.

**Mayte Eme** 1:42:31
OK.
Yeah, I don\'t think if I follow all that. So can we just go through that example maybe on the next session and see how it applies? And my other question, if you want to take it on the next session, that\'s fine. But even though this and if I had it correctly, these courts are experience programs, you were still selecting them one by one. Can we just?
Query and say give me all the cards that have this tag or whatever. Is that not how AO works and we have to still manually click, click, click, click, click and add 1 by 1 every single time.

**Daniela Tea** 1:43:07
So so for I\'m gonna change this back to three so I can see at once alright and then I\'m going to change this to my default card. Alright, so for this component I am adding an individual card to the component.
So I\'m adding one at a time, one card, right?

**Mayte Eme** 1:43:30
Is that how it has to be done?

**Daniela Tea** 1:43:31
For this specific component, that is how this is this works for this specific component.

**Mayte Eme** 1:43:35
So all carousels are one by one. Other ones we can just do a query and like set up a criteria.

**Daniela Tea** 1:43:43
The way that this comonent works right now that is how you would set it U is adding an individual card.

**Mayte Eme** 1:43:48
And what happens when one drops? Because this is scheduled. Oh wait, we don\'t have a schedule.

**Daniela Tea** 1:43:58
So I will say though, like I said, it sounds like I understand the use case for the shared content. And so right now currently this these are quote UN quote localized cards. They were created and they were added to the card carousel component.
Card carousel component was then put into an experience fragment, so that way multiple pages would be able to display this and then only have to change it in one place. So if additional cards were to be added, it wouldn\'t be added at a page level, it would be added at the experience experience fragment level.
So again, not exactly the same thing. I understand the use case is separate, but I am explaining that while you are adding one card at a time to the card carousel, you are able to not just card carousel but with other components.
You are able to reuse them in multiple places as experience fragments and only have to change them in one location.

**Lisa Cardia** 1:45:04
I have another question, Danielle. Could you please use the select panel feature? We\'ve noticed on a lot of components it doesn\'t work as expected.

**Daniela Tea** 1:45:06
Yes.
Let\'s see. You\'re talking about this here.

**Lisa Cardia** 1:45:18
Yeah, so if you were to click one of those, it it\'s not working on this one, but it happens on more than you think.

**Daniela Tea** 1:45:20
Yeah, so I was I I saw that.
Yeah, no, no, no, I I understand what you\'re saying. And actually, let me stop. Let me stop with the transitions.

**Lisa Cardia** 1:45:31
Yeah, I\'m glad it\'s happening on your screen too, because we\'ve experienced that quite a bit and it\'s like we\'d have to go into preview mode and scroll, which is like obviously not the correct way to do it.

**Daniela Tea** 1:45:39
No.
Yeah, no, I yes. No, I understand that. So the yeah, so.

**Lisa Cardia** 1:45:47
Is that just like a bug with the platform or?

**Daniela Tea** 1:45:51
So this theoretically like the way this this should work, like this is also a way to be able to reorder the cards, which I think yeah, but I know you\'re what you\'re asking for is I want to have essentially like number six card be the active card and I want to be able to see it and be able to edit it here without me having to hit preview.

**Lisa Cardia** 1:45:59
Right.
Yes.

**Daniela Tea** 1:46:12
So that I am, I can\'t answer as to why that is not working, which you mentioned in terms of of preview mode and then having to edit. Yes, I understand you know that\'s not necessarily ideal so.

**Lisa Cardia** 1:46:24
Yeah, it seems broken on a lot of the components. That\'s why I wanted to flag it.

**Daniela Tea** 1:46:28
Mm.
Yep. So yeah, that\'s this is something that I can certainly take a look into for this one in terms of like if I select it, I I believe the same thing with I think like the accordion and also the hero carousel.

**Lisa Cardia** 1:46:45
Yeah, it works on some and it works on and it doesn\'t work on others, so.

**Daniela Tea** 1:46:51
Yep. So that\'s Yep, that\'s something I can certainly take a look at. Let me see. Let me see what else we got for card carousel.

**Lucas Nelson** 1:47:00
Hey Daniella, one thing I just I there\'s like 10 minutes left. Might take you mentioned next session that this is our last content authoring dedicated session. Maybe maybe you meant like during platform expansion that I don\'t, I don\'t, I don\'t know what you meant.

**Daniela Tea** 1:47:02
Uh.
Oh, OK.

**Mayte Eme** 1:47:12
OK.
I miss that.
No, I missed the look. Thank you for reminding me. I\'ll just add because now I have so many more questions about the other components, so I\'ll just add them all to this page then.

**Lucas Nelson** 1:47:26
OK, sounds good. Thanks.
Sorry, Daniella.

**Daniela Tea** 1:47:30
No, that\'s OK. Oh.
Wait, one second. Look at my bearings. Oh, OK.
I I try sorry, I try to remember all saying.
Uh.
OK. Well, yeah. So I think, Lisa, what I was saying to you though was that, yes, I I can take a look at the select panel. Um.

**Lisa Cardia** 1:47:57
I\'ll add it to the confluence page, but I think it\'s worth noting that maybe we should check on all of the components that have that feature because we\'ve noticed it on more than not.

**Daniela Tea** 1:48:08
Mhm. OK.

**Lisa Cardia** 1:48:10
But we are aware of the workaround.

**Daniela Tea** 1:48:11
Yep, Yep, Yep. OK, I\'m taking a look to see what else we had here. Buttons, accordions, containers.
Questions about I know that this is a lot like even just with the cards it\'s a lot, but any questions right now cause like again I do see the time 251. Any questions that you guys have that perhaps I can try and answer right now or have as a take away?

**Lisa Cardia** 1:48:46
I think I asked all the ones top of mine in real time, but we\'ll we\'ll definitely be adding to the confluence page, but I I\'ll defer everyone else.

**Daniela Tea** 1:48:53
Sure. Yep. Understood. Oh, I just realized we didn\'t really go over the spacer component. Sorry about that, guys. I know you guys are using it. I know we\'ve talked about the established spacing. I understand you.

**Mayte Eme** 1:49:06
I do. I do have one question just because we have a few minutes. I noticed that sometimes you add 2 spacers like 4040, right? That it would equal 80. But when you publish you don\'t see 80, you see 40 and I\'ve seen that a lot.

**Daniela Tea** 1:49:08
Yep, go ahead.
Yep.

**Mayte Eme** 1:49:22
Is there a reason why we have to duplicate and just to see one? Like is is it a known bug or issue?

**Daniela Tea** 1:49:28
Are you talking about the ones that are perhaps up at the very top?

**Mayte Eme** 1:49:32
Not at the top. I mean, I remember at the cafe sites and the bits that I was shown about the hotel, it was like, why do we have 3 spacers in there? And they\'re like, oh, you gotta do that so you can see one. So is there a something weird about spacers we should know?

**Daniela Tea** 1:49:44
So yeah, so one thing, one thing to keep in mind and I so I can\'t speak to exactly the use case you\'re talking about, but since it\'s since this is a sticky header and.

**Mayte Eme** 1:49:56
No, but not at the top. These were like not at the head and not at the footer like within components or carousels or cards within cards I kept saying and I remember in one session you had to add 2 just to see one.

**Lyon, Rick (Director of Digital Experience)** 1:50:13
Is that maybe the visual placeholder for spacers that kind of go up and down the page everywhere?

**Mayte Eme** 1:50:17
Alright, but.
I don\'t know. I just think they\'re weird.

**Lyon, Rick (Director of Digital Experience)** 1:50:20
In the AEM mode.

**Daniela Tea** 1:50:22
Oh.

**Lyon, Rick (Director of Digital Experience)** 1:50:23
Could put back to edit mode, Daniela.

**Daniela Tea** 1:50:25
Yep.
So I I guess, sorry, I guess I\'m not, I\'m not fully following. I guess like I would need to understand what component you\'re talking about and then we can kind of take a look at that, but.

**Lyon, Rick (Director of Digital Experience)** 1:50:30
Or let\'s drag component.

**Mayte Eme** 1:50:37
I don\'t think it\'s related component, it was just that we had to put spacers back-to-back so you could see one of the two because they were not rendering. Maybe it\'s a bug that got fixed. That just got stuck in my head, so hopefully it got fixed.

**Daniela Tea** 1:50:52
Hmm.
Well, I will say you\'ll notice that at least like whenever I do like test pages and such, I do put multiple at the top. Reason being because this specific template has a hero banner and I typically don\'t put hero banners at the top when I\'m just like trying to work on my pages. So I just put spacers to kind of take up the space at a hero banner.
Would so that is.

**Mayte Eme** 1:51:15
No, this was an actual page, not like a test page, yeah.

**Daniela Tea** 1:51:17
OK. OK. Yeah, sorry, I I guess I would just need to see the page or or understand. Um.

**Mayte Eme** 1:51:26
That\'s fine. If we see it again, we\'ll just log the bug again.

**Daniela Tea** 1:51:27
Uh.
Bye, sure thing.
Um.
OK. Other questions about any of these components. Oh yeah, really quickly. First baser, I think we are familiar with it in terms of the established sizes that are here, certainly if additional sizes or if there\'s some sort of.
If it\'s supposed to be locked out or something, that would be during the. That\'s something we\'d want to understand during the platform expansion as well as the use cases for these. But right now these were the established sizes that were specified for the spacer component. Let me see.
Oh, I don\'t think we talked about title either. Sorry guys. Again, this is also something that I know you guys are already using on several of your pages for the title with our title field, our eyebrow field, the ability to put the eyebrow above or below like we saw for my title that\'s down here.
Here the the size H ones through H sixes. Let\'s see there is that link field if you need this to be a link for whatever reason, but typically I don\'t think you guys are using that ID in class.
And then for the styles, the text color, dark or light can be selected depending on say your background and then alignment left, center or right can be applied depending on how you want the title to display.
Can\'t believe I almost wrapped on that one. But yeah, I know you guys are already using this like everywhere, so not too much. Nothing. I imagine probably nothing new from there, but anything else guys?

**Edwin Aquino** 1:53:12
Hey Daniela, probably would have to address this next time, but whenever we have carousels, a lot of times we reuse the same carousel, but we\'ll exclude a specific card, whether it\'s maybe the current page that we\'re on. So we\'ll exclude a dining page, but we\'ll show all the other dining pages that are associated with it.

**Daniela Tea** 1:53:13
Yes.
OK.
OK.
Yeah.

**Edwin Aquino** 1:53:30
Um, is that something we would use a constant fragment model for or can we? Is there an option with the card carousel that we have right here to do that? How would we go about that?

**Daniela Tea** 1:53:37
Yes. So that specific use case I think is also that\'s something we also saw on the careers website. And so for right now that functionality is not there like that conditional check of am I on this page, if so then remove it. So we are aware of that specific use case once we were talking about careers.
But that functionality has not been built in yet. So what we did, at least for careers for the time being, is that all those cards will be displayed. We\'re using the same experience fragment, but it sounds like for during the platform expansion discussion, that\'s the kind of functionality that would need to be built into, say, the card care.
So and and perhaps other carousels if if you guys are using, you know referencing perhaps the page that you\'re on in a in a different way. So not available today, but certainly something that we want to make sure is captured during platform expansion.

**Edwin Aquino** 1:54:32
OK, cool. Thank you, Daniel.

**Daniela Tea** 1:54:34
No, thank you for that question. Anything else guys? I know we have 3 minutes, so just wanna. I understand though that you guys will probably want to, you know, capture things on the Confluence page and I I do have to add a couple of links to some of the previous pages I am planning on.
Sending an e-mail out when I have added those links there. I want to provide some of the experience leak documentation relevant to some of these components, specifically like the page properties. I know it\'s a pretty common one for for easy reference for you guys.
And then I\'ll also be taking a look at the questions and and try to provide answers as I can. And then also we\'ll be continuing discussions on the use cases that Hard Rock needs for platform expansion. I\'m going to pull up the KT calendar so we can take a look at.
What the schedule is for this? So let\'s see. Here we go. All right. So today is Wednesday. This is what this is where we are today. Tomorrow we are beginning our.
Technical knowledge transfers with Andy and Vinay leading those that will be the morning. We also have an our first adoption session starting I believe Thursday afternoon and so throughout all of next week as you can see here additional technical knowledge transfers our adoption session.
Sessions will continue on Thursdays and then on March 16th, the week of March 16th, that\'s when we\'re going to begin the platform expansion. This will be the time, of course, for you know, Hard Rock, you guys will be providing us with the use cases, yeah.

**Mayte Eme** 1:56:21
Daniela, one thing, can we put a checkpoint before the 16th to make sure that we are ready for the platform expansion? Because we still have a lot of questions and depending on the answers, we don\'t know what we can use or not or if things will work.
And also I\'m still trying to rewatch previous ones that confuse me even more when I watch them to identify all the gaps. So we\'re going to need a checkpoint to make sure if we are good to start on the 16th.

**Lucas Nelson** 1:56:51
Mayte, this is the schedule we\'re maintaining. So I would advise you to take an internal checkpoint to see what you have. Follow up with us with with whatever feedback you have ahead of those weeks. But we really have to maintain this schedule because this is what we committed to and what\'s in our scope of work.

**Mayte Eme** 1:57:11
OK, I\'m going to have them to let me talk internally because without having actual requirements, there\'s no point on having expansion meetings. I mean, it\'s going to be a waste of time for everybody.

**Lucas Nelson** 1:57:17
Yeah.
Definitely have those discussions internally for sure. That\'s why we flash this calendar so often.

**Mayte Eme** 1:57:26
And can you remind me what the adoption calls are for? Because I\'m still not 100% clear on those.

**Lucas Nelson** 1:57:28
OK.
Yeah, we brought on Jacob White, if you remember him way back when, two years ago, my day, he he\'s coming in to to kind of have like an adoption coaching with, you know, Penny\'s involved with those two. But you and Lisa are like the key participants in that because as you guys are getting into.
You know, we obviously we need to enhance the platform from whatever we agreed to from platform expansion, but but the further adoption of this across your broader authoring groups, that was the intention with those.

**Mayte Eme** 1:58:06
Yeah, I still don\'t know what the outcome of those are gonna be. Um.

**Lucas Nelson** 1:58:10
Let let let\'s let Jacob kick it off with you on Thursday and then definitely ask your questions with him and maybe we can get to a shared understanding of where we want want it to go. OK.

**Mayte Eme** 1:58:22
Sure, I might be late for the first one because there\'s a conflict, so just FYI.

**Lucas Nelson** 1:58:28
OK, Gonzalo, what\'s up? We\'re at time. What\'s up?

**Gonzalo Calasich (SHRSS)** 1:58:33
Yeah, the take.
Sessions. They start tomorrow.

1:58:37
Yes.

**Lucas Nelson** 1:58:38
Yes.

**Gonzalo Calasich (SHRSS)** 1:58:39
Sweet. Thank you.

**Lucas Nelson** 1:58:41
Yeah. Andy\'s looking forward to it for sure. Yeah, he\'s on the call right now. Yeah.

**Andy Lambert** 1:58:47
Yep, I\'m going to bed early, eating my Wheaties. I\'ll be, uh, ready to go.

**Lucas Nelson** 1:58:52
Going to bed early. That\'s the first time you and last time you\'ll ever hear Andy say that on the call. So, all right, guys, we we got to drop though. I got a hard stop. Thanks for your time, guys. I\'ll try to send that recording as soon as I can. Thanks. All right, bye.

**Daniela Tea** 1:58:56
Yes, absolutely.
Thank you, everyone. Goodbye.

**Gonzalo Calasich (SHRSS)** 1:59:03
Thank you. Thank you. Bye.

**Andy Lambert** 1:59:03
7.

Lucas Nelson** stopped transcription