**SHRSS Adobe Knowledge Transfer-20260302_130320-Meeting Recording 1**

March 2, 2026, 6:03PM

2h 13m 51s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:08
All right, the recording\'s live now. Um, Daniela, if you wanna get started, thank you.

**Daniela Tea** 0:16
Thanks, Luke. I am pulling up the agenda and I will go and share my screen once that\'s up.
OK. All right, here we go. Good afternoon, everybody. So we have actually three more content authoring meetings for this week. And so you can see here I do have some agendas and draft where I\'m essentially getting.
The remaining components that we have not discussed yet and then putting them into the agendas for today, tomorrow and Wednesday. For today we\'re going to be covering navigation and data displays. So you\'ll see this is what I plan to cover for today.
Tomorrow I wanted to cover things that are line of business specific. So think about things that are specifically on the cafe page, like for example the dining widget. So we\'ll go over things like that for tomorrow and then the final day is essentially going to be like a catch all.
Anything that was not covered in the other sessions, I want to make sure is within that final session, but also going more in depth into things like the container, which we did talk about in some other sessions, but going into some of the additional properties that we didn\'t have a chance to cover as well as the.
Card component will be on the last day since I know that\'s something that the team is familiar with in terms of using cards, but we can certainly explore more of the variations and some of those use cases on that final day. But for today though, we\'re going to cover these items and I think.
For the most part, most of these are things that the content authoring team is familiar with. I\'m not sure if we have ever discussed content carousels. I want to make sure there\'s enough time for that one. But as we go through, you know, I would love to hear if you guys are.
Currently using these or have any questions about these components since I believe the majority of these are probably used on the corporate or the reverb website. So I\'d love to hear any of the use cases you guys are using these for for the corporate site.
So I\'m going to jump on over to my test page over here and let me pull it U in author. So a little quick tip for anyone who is viewing a page as publish.
If you want to quickly get back to the author view, all you do is add slash editor dot HTML after the base URL and then remove the question mark WCM mode equals disabled at the end.
And so when I click on that, that takes me right to the page that I was just viewing as published, but now I\'m in the author mode. All right. OK, so this is my one of my test pages I was creating specifically for today.
As you can see here, I have the components listed out and so I wanted to start with our breadcrumb navigation. One second, I\'m going to pull this over here. Alright, OK, so the breadcrumb components as we were reviewing things such as the page properties.
There are some things that are being driven from the page properties that affect how the breadcrumb navigation works. So what I have here is I had just added a breadcrumb to the page and I\'ll do that again. I\'m going to add the breadcrumb component.
And you can see here this is what\'s being displayed by default. When I just add the breadcrumb to the page, it\'s showing the page hierarchy starting at Level 3. It\'s not showing any hidden navigation items when I just drag it to the page.
It\'s not hiding the current page. You can see my KT NAVS page that we\'re currently on is being displayed and with disable shadowing that is unchecked. But I do have an example down here to explain what that means. So by default you can see the start level is set where the base site is in this case.
In the careers website and then it shows all the child items underneath it and it\'s also going to show the current page that I\'m on so we can see how that is being displayed right now. Now this is the exact same version that I previously had on the page. You can see nothing has been selected.
However, for this next one, what I\'m showing is show hidden navigation items. So the navigation start level is still at 3:00, but now I\'m showing anything that\'s hidden and So what you can see here is this hidden page.
So if I were to view this particular page in the sites, you\'ll see Careers, KT Home, this hidden page and then KT Navs. So for my hidden page, what I did was if I clicked on properties, you\'ll see.
I had checked the box that said hide in navigation. So when we first dragged the breadcrumb component onto the page, this page was not listed in the navigation. However, because it is part of the structure, if I wanted to show that hidden page for whatever reason, I could do that.
Just by making sure this checkbox is checked. So again, you can see that my KT Navs page is actually not really directly underneath this level where it says Seminole Hard Rock Careers. It\'s actually under a hidden page and I was able to show that by checking this box.

**Lisa Cardia** 6:00
So that hidden page checkbox that impacts both our site map and this now component just so like I can understand OK.

**Daniela Tea** 6:04
1.
Yes, Yep, that\'s correct. So the hide and navigation check box here in the page properties affects the breadcrumb component and the site map.

**Lisa Cardia** 6:21
OK. And then for the navigational start level, I\'m, I\'m just a bit confused because we say that like obviously it\'s at three, that\'s what it starts with, but like the higher the number, the less it it displays. So I guess.

**Daniela Tea** 6:25
Yeah.
Yeah, so, so let\'s look here. I\'m gonna go back. I\'m gonna hit cancel on this so we can see this is 123. So say you didn\'t want careers to be listed. If you started at four, it would start at this level.

**Lisa Cardia** 6:51
OK. So the start is counting from left to right on the page that\'s going to start. So three starts you on the third level, 4 which would only show you the two. Got it. That was definitely a question of mine. Thank you.

**Daniela Tea** 6:54
That\'s correct.
Mhm.
Yep.
Yep, absolutely. And so I think what would be like for example when you guys are say setting like a cafe or something, if you put the breadcrumb and you know by default it would start at three, you might, you might need to adjust it just based off of the level, but you could see what level to start at based.
Off of what you see here in the sites page. So that is certainly something that can be configurable through the breadcrumb component. All right, so we see how this hidden page was listed. Now let\'s take a look at this one. You can see I\'m going to hit preview just so you can so it\'s a little bit clearer. You can see instead of it saying Seminole Hard Rock Careers.
It actually says KT home O let\'s see what I checked in order for that to display.
So I have selected disable shadowing and so the reason why this has changed is if I were to go back and look at this page, this KT homepage, I\'m gonna click here on EN. Let me navigate back to corporate careers. Here\'s the KT homepage.
If I select this and I click on Page Properties and I click on my Advanced tab, you can see I actually had set a redirect to go to the Careers homepage if I go back to my page here.
That\'s why this is listed, because this is the page that KT home redirects to. However, with disable shadowing checked, instead of showing the redirect, it\'s going to show you know like the the page, the page that\'s a higher level than what I\'m currently on. So like this KT home, which is actually a redirect to Seminole Hard Rock.
Careers with disable shadowing checked, it\'s going to show Katie Holmes instead.

**Lisa Cardia** 8:55
But we would be able to access the page. It wouldn\'t. It wouldn\'t just show the page title, but still redirect.

**Daniela Tea** 9:01
So if I click on KT home, you can see. So hang on, I\'m gonna show this as view as published so you can see what the behavior looks like. So KT home, it should redirect. If we publish this, I might need to publish a couple of things to actually show this. So one second, I\'m just gonna publish some pages.

**Lisa Cardia** 9:21
OK, just because I can\'t really think of a use case where we would want to show the page if it\'s ultimately redirecting.

**Daniela Tea** 9:25
Mhm.
Right. And so I I think for for you guys you would likely either want to hide it, which you could do that right? If you were say this is a redirect you don\'t want in the navigation, then you could simply use the hided navigation feature, but let\'s take a look.

**Lisa Cardia** 9:37
Yeah.

**Daniela Tea** 9:44
So what should happen though is it should redirect you to the thing. So I agree Lisa, it\'s likely not something. But if you guys do need it, you know to say something else, like say you don\'t want it to be like a like you don\'t want the redirected title, you want like what the actual title of the pages that you named it. That could be a reason for you guys to perhaps need to use.

**Lisa Cardia** 9:45
Yeah.

**Daniela Tea** 10:04
Is that right? So OK, I think I have published everything. This one\'s not published yet, so I\'ll publish this.

**Lisa Cardia** 10:11
And and just a question though, that doesn\'t impact the redirect in general, right? So like if I again can\'t think of why we would want to use disabled shadowing, but let\'s just say we did and the user clicks the page and then they get redirected. If someone just accessed the URL otherwise it would still redirect as normal, right? Like putting the disabled.

**Daniela Tea** 10:30
Yeah, a bit.

**Lisa Cardia** 10:31
This is only for the from.

**Daniela Tea** 10:32
Yeah, yeah. So that, yes. So this is strictly for the breadcrumb, right? Like, so KT home is actually not like there\'s nothing on the page. It\'s actually just a redirect page. I\'m not like using it. I simply put the in the properties that I want it to redirect to the Seminole Hard Rock careers page. So what it should do is it.

**Lisa Cardia** 10:38
OK.

**Daniela Tea** 10:52
Should take you to this particular page, but I\'m trying to publish everything like things work a little bit different in the author. Always keep that in mind. You know some things are are going to function differently, so you need to like if I\'m trying to just click around on here because it\'s like taking into account you know.
The how do you say like the interface on here and stuff. Not everything\'s going to work exactly the same as when you actually publish the pages. So it takes the properties that were that you\'ve applied when you view page properties and all that stuff. So that\'s why I\'m trying to publish the page so we can take a look at the exact behavior when I click on KT home.

**Lisa Cardia** 11:24
OK.

**Daniela Tea** 11:31
Should do though is it should redirect you to this page.

**Lisa Cardia** 11:31
But.
To be clear though, disable shadowing just means you\'re using the original page title. But other than that, it\'s still the same exact experience. If we didn\'t use disable, it would just show the redirect page title. OK, so it\'s just I just I\'m taking some notes, OK?

**Daniela Tea** 11:39
The.
That\'s correct. Yep. So if I were to put this, yeah, if I uncheck this and I hit done, you can see how it it puts back that Seminole Hard Rock careers page, which is what I had redirected to. Yep. All right. And then this one here, this was just showing all the combination of disabled shadowing.

**Lisa Cardia** 11:54
That right here, OK.

**Daniela Tea** 12:04
And show hidden navigations kind of the same as what we had above, but just wanted to show, you know, like depending on what you check, your breadcrumbs certainly could look different. And if I wanted to hide the page I was on for whatever reason, say because you have a very large title on the page that you would rather have that be.
The focal point you can see here I do not have the name KT Navs on here. Instead I just have the pages before KT Navs listed since I have hidden the current page from the breadcrumb navigation.
Hey.
All right, let\'s see. And one more thing to think about as I find my editor. This is.

**Lisa Cardia** 12:50
My my question was going to be more for the team and I don\'t know if this would be on the Adobe side or internal, but I did notice that this component, you know, comes with let\'s just say like the open page template, but we like currently don\'t use breadcrumbs on our sites. I mean, I know that there\'s some pages such as like The Newsroom, but not on our typical inner pages.
So I just wanted to know if there\'s a way to remove that just from all feature page templates or is that just something the internal team needs to do? Because I did notice it comes with it.

**Daniela Tea** 13:21
Yeah. So I think last week when we were talking about page and yeah, Lisa, sorry, I believe you probably missed that specific one. Yeah.

**Lisa Cardia** 13:31
Yes, I I know you were talking about which templates to use, but I I know my team did tell me open page over content page. But I\'m just curious if we could remove like the breadcrumb from that since we wouldn\'t have a breadcrumb on our inner pages.
Typically today.

**Daniela Tea** 13:47
Yes, yes. So we last week we were talking about how you can edit the templates in terms of like the structure, the initial content, that sort of stuff. So let\'s see here for our open page template.
When we talked about initial content, we do have this breadcrumb here editing templates. So you know, since it\'s not a draft, definitely need to be mindful of the changes that you made. However, there is, you know, I understand as you\'re creating it, the breadcrumb is automatically there.
While you can edit the templates in the future, you know like we\'re we\'re not trying to change anything right now, but if you\'re trying to remove things or add things as initial content to the template, you can certainly do that if you have the correct privileges to access templates and author them.
So that can that change can be made and as you guys are planning out your templates for future sites, anything and you know there could be a page that might have a breadcrumb, like you might determine that there are some pages that should have the breadcrumb on it. You can certainly add that there, but in order to delete it though, you need to be able to have author privilege.
To templates and I do believe Lisa, your team should, but not everyone would have access to be able to like mess around with the template.

**Lisa Cardia** 15:07
OK, I can connect with the internal team and it will probably be like my taste team that would do that, but I would just suggest it since we don\'t really use bread crumbs outside of a very few one off pages.

**Daniela Tea** 15:18
Got it. OK, yeah, one second. I\'m just refreshing my page. The last thing I want you guys to keep in mind when it comes to this breadcrumb component is that another page property that does affect it is that page page navigation title. One second, just closing out of a couple things.
So if I were to, I don\'t want to add any templates. If I were to go to my properties, although my page, my title for this AEM page was KT Navs and the navigation title you can see I put KT navigation title and so now when I look at the breadcrumb it is displaying that.
Title instead.

**Lisa Cardia** 16:00
But we don\'t need to use that, it\'s just overriding.

**Daniela Tea** 16:02
No, correct. So if I were to remove this here and justice hit save, it\'s going to default to whatever was in the title field.

**Lisa Cardia** 16:13
OK.

**Daniela Tea** 16:16
OK. Um, any questions about the breadcrumb? Um.
Whether it\'s like, you know, like what\'s being displayed here or like the level, any questions about the breadcrumb in general?

**Lisa Cardia** 16:30
Is it responsive? So what what do we see on?

**Daniela Tea** 16:35
So it\'s it\'s not necessarily responsive in the sense that it doesn\'t actually like collapse into say like a drop down or something, it just sort of wraps.

**Lisa Cardia** 16:44
OK.

**Daniela Tea** 16:47
Yeah, OK, it wraps. All right. OK, so breadcrumb navigation. Yeah, I think Lisa, I\'m not sure exactly where it\'s being used, but I believe, like you said, it was a few one off pages that we had noticed.
The sub nav though, this is something that we saw was used on the hotel pages, I believe like the meetings and weddings section. And so for the sub nav component, what this does is I\'m essentially able to take a subset of pages.
So instead of it, you know, taking everything from like a hierarchical structure, if I want to group pages together in some form of navigation, I can do so. So in this case you can see here I\'ve taken a homepage from my KT home section.
I\'ve taken my hidden page, I\'m sorry, my KT Navs page in my KT home section, a KT open page and my KT blank page. So these are all pages that if I clicked on here you can see where they are and all I did was just select what I wanted.
To appear in my sub NAV. With that being said, what happens is you\'ll notice here that the KT NAVs right now is actually highlighted because I am currently on this page. If I were to open up, say I think I added it on KT blank.
If I were to open up my KT Blank page and if I added the subnav, which I did on this page, you\'ll see that the KT Blank page is now highlighted because that\'s the active page within the subnav. So if I were to add this subnav to another page that isn\'t.
That isn\'t listed here. So like say there was another page called KT Media, nothing would be highlighted because it\'s not within the sub NAV, but you would be able to access it. So the highlight is based off of if it\'s in the sub NAV and if you\'re currently on that page.
So if I were to also change this to mobile, this does have slightly different mobile functionality. You\'ll see here I actually want to view this as published so that way I can interact with it.
Oops.
Second.
Hmm.
Let me stop sharing the reshare. One second guys. Sorry, my computer seems to be freaking out yet again.
go and try this here.
OK.
So I get this back up. I will share my screen.

**Lisa Cardia** 19:55
\'Cause I I do have a few questions, but I can wait until you your screen is back up.

**Daniela Tea** 19:58
Yeah, sorry guys. One second. Just trying to get my trying to close out of some stuff since my computer is running a little bit slowly.
Elise, if you do want to ask your questions, you can go ahead. I just won\'t be able to show it just yet, but you can go ahead with the questions.

**Lisa Cardia** 20:20
Yeah, I had said how do we and cause we had tested this in the stage environment and we actually struggled to get the the down state that you were showing where it was like showing just the page you were displaying on. But maybe we need to play with that a little bit more and make sure it\'s added to all of the pages to see it in.

**Daniela Tea** 20:26
M.

**Lisa Cardia** 20:39
To actually work, but we didn\'t know how to get the the tablet mobile mobile options to expand past the first navigation. It wasn\'t working for us and then there was like no hamburger menu or option to expand to like the next set of links. So that was one question of ours was seeing it on a different break point and it wasn\'t working.

**Daniela Tea** 20:45
Mm.
OK.
OK.

**Lisa Cardia** 20:59
If you want just all my questions that I have, I can go through them. My I was just wondering if we have the option to use a light background with a dark font. I know it\'s only right now showing the black with the white, so just wanted to see if that is something we can do as authors or is that?
Extra development. And then I was just curious if that first page like is considered I guess like the parent page because like it does show the arrow as if those are ending up to be like children of it. So I\'m just.

**Daniela Tea** 21:18
Mhm.
Mhm.
Mhm.

**Lisa Cardia** 21:32
I\'m I\'m guessing like you\'d always want that to be a parent level the way it\'s designed with that arrow and and then we and then we just had some we just had some concern about like the the alignment of the text isn\'t actually the same for the additional links. So that just might be something we want to report that it\'s not really to the like.

**Daniela Tea** 21:39
Yeah. So, yeah.
OK.

**Lisa Cardia** 21:52
The correct pixels across all of them.

**Daniela Tea** 21:56
OK, yeah, so let\'s take a look at. I just restarted Chrome. So let\'s take a look at some of the things you said for for when you mentioned that you guys are messing around with this component. Out of curiosity, are you can we like maybe we can see?
How you guys set it up and perhaps we can understand you know what is like what\'s different from your version versus what I showed.

**Lisa Cardia** 22:20
I don\'t think I have the example for you ready today. A lot of times we\'ve just been testing the components like by themselves. So it it does make sense to see how you just said it like needed to be on several pages for you to see. So that could be why, you know, we just encountered the one issue that I questioned.

**Daniela Tea** 22:23
OK.
Yes.
OK, OK, so so.

**Lisa Cardia** 22:39
So I don\'t, I don\'t really want to share it right now just cause it\'s like the component on an empty page, but I think our our other questions if you were able to take those down are definitely warranted.

**Daniela Tea** 22:45
OK.
Yeah. So let\'s see the other question, one of them was about the arrow portion. So like you said that is intended to be kind of like say like the highest level, the parent if you will like you mentioned. So in the use case on hotels I believe.

**Lisa Cardia** 22:55
Yeah.

**Daniela Tea** 23:07
It\'s the the portion that\'s showing before the arrow is like meetings of events because that was like the top level navigation. And then it\'s like a subset of pages that essentially are related to meetings and events. So there\'s no like real like it\'s not like saying oh this.

**Lisa Cardia** 23:15
Right.
Yeah.

**Daniela Tea** 23:25
This is a parent and it\'s going to automatically bring in all the child pages. It\'s more this is an author set navigation, like you\'re determining like what you want within that group. So it\'s so like the intention is to be like, OK, this is more like a parent level page and these are the pages related to it. But as an author I have selected the pages.

**Lisa Cardia** 23:36
OK.

**Daniela Tea** 23:45
That I say are related to that parent page.

**Lisa Cardia** 23:48
OK, just because like the first one has the arrow, but the rest don\'t. So it to me it makes sense to say like the rest almost group in underneath that umbrella. Otherwise I feel like it would be a bit misleading to have the first one not be like a higher level, if that makes sense, just because of that arrow.

**Daniela Tea** 23:56
Mhm.
Yeah, so OK.

**Lisa Cardia** 24:08
Like at least the other children items kind of all seem like siblings versus higher than another.

**Daniela Tea** 24:12
Mhm.
Yeah. So, yeah, I think it.

**Lisa Cardia** 24:16
To at least, especially because like if you could test the tablet mobile and us not being able to see anything past that first navigation is what kind of makes it seem that way as well. So we definitely want to figure out why we can\'t get past the first level and if.

**Daniela Tea** 24:28
Yeah.

**Lisa Cardia** 24:32
Why there\'s no like hamburger?

**Daniela Tea** 24:35
Yeah, so let\'s view as published. OK. And I\'m about to share my screen. One second. Let\'s see. OK, let me share my screen. Sorry about that, guys. Hopefully this will work now.
OK, all right. So what we\'re seeing here with our sub NAV currently on that KT Navs page, I\'m viewing it as published and I\'m going to make this as a smaller breakpoint. So now we see it saying I\'m at KT Homes.
Our KGM is like the the the essentially the quote UN quote parent I have determined and with KG navs that\'s the page I\'m on. If I click on this it\'s going to show a drop down underneath of the other pages.

**Lisa Cardia** 25:17
What did you just click though? Because I guess like there was no like a user wouldn\'t know to click and maybe I\'m not as familiar. Rick, if you want to speak of what this looks like in present is there? I thought there would be like a hamburger to indicate that there like that this is a drop down.
So maybe I just misunderstood what it was supposed to look like.

**Lyon, Rick (Director of Digital Experience)** 25:38
It\'s been a minute. I\'d have to see what\'s live. I think it just goes turns to menu and then all the links are down below, but I\'d have to take a look.

**Lisa Cardia** 25:48
OK. I guess we could move on from that question and just circle back. I I had tested this and was wondering how I just kept clicking for example KT Nav so I could never get to the drop down. So you\'re clicking just is it?

**Daniela Tea** 25:59
Yeah.
Yeah, I\'m just clicking where I\'m.

**Lisa Cardia** 26:05
Is it because it\'s like disabled right now or I don\'t know why we were struggling to get or maybe it wasn\'t even showing?

**Daniela Tea** 26:13
O Let\'s go to KT Blank.

**Lisa Cardia** 26:15
More than just the parent is what we were saying.

**Daniela Tea** 26:16
Yes, so so you can see here I\'ve clicked on K So I clicked on KT Blank and open in a new tab. So now it\'s showing when it\'s in in mobile, it\'s showing again that that parent level that I\'ve determined and then the current active page I\'m on which is KT Blank. When I click on that I can see the other options as.
Down underneath.

**Lisa Cardia** 26:39
OK, I guess Rick did send a link I I guess I\'m not as familiar with.
The present one.
I\'m going to click it if you\'re not.
Just compare really quick.
So I think, yeah, the one present day has that drop down arrow and then they all kind of fall. So I guess the confusion here is that this is isn\'t the same functionality experience, like I guess to a degree because you\'re clicking on it, but there\'s no indicator to the user to click if you.
To click Rick\'s link and look at the production site.

**Daniela Tea** 27:26
Yeah, sorry, one second. Let me try and get up the link.
M.
Oh.

**Lucas Nelson** 27:54
Looks like your crumb\'s struggling, Daniela.

**Daniela Tea** 27:56
Yeah, what\'s going on?

**Lucas Nelson** 27:59
I don\'t know.

**Daniela Tea** 28:01
Yeah, one second. I won\'t let me. Sorry guys, about this. Let me get out of Chrome again. I might be able to do this. I could do it from Firefox, but one second.
Mhm.
Let\'s try again.
OK, I am going to share screen again and see if this works. Hopefully it works. All right. So taking a look here now at here we go. All right. So we have our overview page, which is the meetings and weddings page. And So what you\'re saying, Lisa, is when you come down here.

**Lisa Cardia** 28:46
Yes.
Yeah, so it\'s like indicating to drop down \'cause otherwise I\'m unless that was like just me not realizing you had to click. I I had no idea with the current implementation that a user should click since there was no arrow.

**Daniela Tea** 28:58
Here how it\'s shown.
Mhm.
Let me see. Yeah, I uh.

**Lisa Cardia** 29:17
Especially cause on mobile like you can\'t hover to see that state so.

**Daniela Tea** 29:21
Mhm.
Go back.
Yeah, so I think in terms of the functionality itself, it\'s uh wait, am I on the wrong page?
Oh.
OK, sorry, I just noticed it says old in here, so I\'m not sure if I was on the right page or not. But what you\'re saying is that the yeah, so the functionality is the same in the sense that yes, you can click on the area and it presents a drop down. However, what it\'s showing is not just the active page, it\'s also showing the.
The established like the author established quote UN quote parent level page and it\'s also having a drop down here versus essentially the carrot facing to the right.

**Lisa Cardia** 30:21
Yeah, so I would say for our team, I don\'t know if if like this would get reported as a defect, but or like missing for gap analysis. But to me it\'s not indicative of the to the user that there\'s gonna be a drop down since it doesn\'t.
Look the same.
Is my thought. We can take it and move on though, so we don\'t waste.

**Daniela Tea** 30:47
Yeah.
OK, Yep. So for sub NAV, I think another thing you asked was about in terms of the background. So I believe we had established it was black.
Yeah, so we had established that it was black, so it\'s not currently author configurable. So like it\'s always gonna be black, but it sounds like what could be added in the future, what a desire would be to essentially have a configurable background color.
As well as the ability to change the text color from white to a dark color in order to accommodate for whatever was selected for the sub NAV.

**Lisa Cardia** 31:28
Yeah, I think just having like a light and dark version is something we should take back as a team.

**Daniela Tea** 31:33
Yep, and the final thing as we saw with the the sub NAV in mobile, how it looks it it if it\'s in desktop, it\'s going to display everything. However, for whatever reason you need to always display it like it\'s in mobile.
If that use case is there, then this would just simply be checked. So then even in desktop it would be displayed the same way as in mobile.
OK. All right.

**Lisa Cardia** 32:03
Could you? I I don\'t think unless you were gonna get there next, there\'s the accessibility tab, what we would typically label for that.

**Daniela Tea** 32:09
You.
Yes, so the accessibility tab there is just for an Aria labels. So you can see I put here sub NAV label and so when you view this as published and if we were to inspect this you can see here\'s where the Aria lab Aria label gets applied.
So it\'s, um, not something that like a user would see, but it\'s more for like, um, screen readers and such.

**Lisa Cardia** 32:36
Yeah, I think that we would want to cover it if it\'s a.

**Daniela Tea** 32:39
Yeah.

**Lisa Cardia** 32:41
um, field.

**Daniela Tea** 32:46
All right, so moving on now to our site map components. I\'m going to open this up. So for our site map you can see here I have for my route path just selected the KT home.
Which should include then everything underneath it except for things like hidden pages. So in this case I should see 123456 links which I can see. Actually I\'m going to try and open this in a new tab so we can compare.
Let\'s go back to the admin section, OK?
So here we have our homepage, we have my KT blank page, my KT media navigation title which is what I had named this here. Underneath it you can see test news is appearing so it\'s saying this is a child level page.
And then we have my KT open page here and then we have my test blank page. So what\'s not showing is my error page because I believe for this page let me check.
I don\'t think I actually. I think this page it\'s so I\'m using the an error page template and so that\'s not going to appear as part of the site map itself. So that\'s why this is hidden. And then for the hidden pages, we remember I had selected the hide and navigation field so the hidden page is not going to appear.
Ear here, nor will the items underneath my hidden page.
All right. Um, so questions about the site map and how it\'s bringing in the items.

**Lisa Cardia** 34:45
So just everything besides an error page template unless we have it selected as hidden.

**Daniela Tea** 34:50
Yes, that\'s correct, but also keeping in mind that the page pages underneath hidden pages are also not going to appear in the site map.

**Lisa Cardia** 35:00
Hey OK pages under hidden pages.

**Daniela Tea** 35:03
And also that the page title, the navigation title. Let me open this up. Yeah, so the navigation title is also what\'s going to be displayed within the site map. However, of course, if that\'s not filled out.
It\'s going to default to the title that\'s U here.

**Lisa Cardia** 35:25
OK, I don\'t know if the team can think of any pages where we hide the parent, but then we want the children to display, so we\'ll have to think on that if it\'s something we need in this section.

**Daniela Tea** 35:36
OK.
Yeah.
OK, so that is the site map. So now I wanted to show the content carousel, which I don\'t think you guys, you guys are not using this currently on the corporate site, but this is something that\'s pretty common on the hotel pages.
Let\'s take a look at the published view of this page over here.
We need to just drag this over here so we can have it in a separate window. All right, so the content carousel. The purpose of this is to essentially be able to display things within this image carousel here, and then there\'s content that appears underneath. Again, this is typically.
Something that\'s being used on the hotel websites. So we\'ll break this down in a second, but wanted to show you guys what it looks like when you view it as published, because when you work on it in the editor, what\'s happening is the content carousel.
There\'s multiple images being added and you\'re not going to see the information underneath. The information underneath is within this tab. So in order to be able to view it, just remember to just view as published and you can see that preview of how the content looks and what images you\'ve added, et cetera, et cetera.
So here it is in author. The content is there, it\'s just only within the the component itself, but you can view it by viewing it as published.
OK, so let\'s break down exactly what has been authored here in the content carousel. All right, so for starters, what we did is when I dragged on the page, I can only add images to here. It was restricted to just images.
Since the images is what\'s populating here, if that\'s something that needs to be, you know, if that needs to be expanded on, say. I\'m not sure if you guys would ever add a video or something here, but that can certainly be added in the future to allow additional components to be added here, however.
When this component was made, it was supposed to be strictly just for image carousels only, but that that\'s that\'s where you would add this here. So this carousel portion for the items is strictly just for the images and I\'ve added two images as you can see.
Then on my additional tab, what I\'ve done is I filled out some information. So we have a title and a subtitle and those are listed here on the card itself. Then I have a description.
Which is displayed underneath the subtitle if I am having a if I\'m having a two column style. So this is a two column, this is a three column. So this here is the description. It\'s going to be displayed underneath here if I\'m having a two column style and then my.
Details I\'ve left blank. I can add some details here so you guys can see.
The details we don\'t actually do this. We need to refresh this.
So you can see that the details field would display here if I added something there because this is in the two column field. However, I don\'t think typically two column the two column content carousels you would actually have anything in this field from what we saw on the hotel site.
I\'m going to Scroll down and we can see the CTA for book now. Let me refresh. Oops, let me hit done and then I\'m going to hit refresh here. So this updates. Yep, right. So we have our CTA for book now and I have my URL.
Listed here. So when I click on this it\'s going to open up in a new tab. I also can style the button whether I want it to be the primary style, which you can see here for these three, the secondary light style which is that outline version or the tertiary style which is we can show it right now essentially like the button.
Without the background and the the carrot on the right.
And then?
If I want to have a read more details section up here, I can select this box. If I uncheck it then this will go away. So there\'s you don\'t necessarily need to have it if this is all you really need for your card. But as you can see here I have my read more details label which is what populates in this.
For this specific button, then I put a section heading called Amenities. So when I select read more details, you can see my section heading amenities. I put whatever I want here and then for these features here, free Wi-Fi, 24 hour room service, etc. What I\'ve done is I\'ve selected from this list as to what I want to display.
In here and this list is coming from a generic list, which means that certain authoring groups based off of permissions. If you are, if you have the right permissions, you can add additional values to appear in this list. However, say.
Like a hotel author who likely wouldn\'t have that privilege, they can\'t just add additional features here. So this is managed at from a a specific user group. So if you know if you guys are seeing this, you\'re like wait, but there\'s a lot more amenities that should be there that can be added as long as it\'s in like a specific.
Admin person who is able to add additional options to this list. In this case I\'ve picked four and so that\'s displayed here. And then there\'s also another text box that\'s here if I need to put any other information that might need to appear on underneath my amenities sub header.
And before we go into the three column version, I\'ll pause here to see if there\'s any questions about how this portion has been authored.
And hit cancel. OK, so now let\'s take a look at this one. This one has some differences. You can see here there\'s actually 3 columns that are being displayed instead. Pretty much all of the details and such is here on the left. And then the middle we have this.
Section called Hours and then in the far right we have a menu of buttons. So if we take a look how that was authored.
So I had two images that were added to this carousel. On my additional tab you can see my title and my subtitle. We can see my description is populating this section here. The details is populating here in the middle and then I have my different CTA.
Days. In this case, the style has all been selected as primary, so that\'s why they look like this. But if I wanted one to look, you know, say slightly different, so I want these two to essentially be secondary links, can certainly do that. I hit done.
And I hit refresh. You can see how that has changed. And then for this particular one, it\'s kind of the same thing. Read more details. I\'m not using the features section because I don\'t necessarily. I\'m not actually showing any sort of amenities because this.
This is a restaurant. However, you can see how I\'m using that additional info box to put the dress code information here in this section and then finally for this one.
I click on styles, you can see here that three columns has been selected. That\'s why you see again 3 columns. If I were to change this to two columns and hit done, things are probably going to look a little strange. So the buttons are now appearing here on the bottom.
So, and so things are a little, you know, this is not intended to be a three, a two column card. So you want to make sure that when you\'re planning out your carousel, is it going to be 2 columns or is it going to be 3? That will determine how the items are displayed. So I\'m going to change it back to three.
Hit refresh and so now it\'s it\'s back to three columns and it\'s displaying as intended.
Um, so questions about this content carousel.

**Lyon, Rick (Director of Digital Experience)** 44:32
Hey Daniel, I\'m getting a door installed so it might get loud here. So as quickly, quickly as I can. I think we had briefly discussed this, you know what a year or two ago. Some hotels will have like four or five if not more menus and I think we had talked about maybe having a drop down or something.

**Daniela Tea** 44:42
Mhm.
Yes.

**Lyon, Rick (Director of Digital Experience)** 44:51
Um, like a menu drop down and then you could select which menu. I\'m sorry Sir.

**Daniela Tea** 44:52
Uh, yeah, let\'s try. Let\'s try and do that.
Go ahead, Rich.
Press menu. Just gonna add some stuff here. Uh, let\'s see here.
Trying to remember if there was a limit. I do believe we talked about that. Let\'s add some more.
Um, this menu. Oh, I think I know. Um.
I believe that had been implemented when it came to the dining widget. If there were multiple menus there, I I do remember that discussion and that had been implemented. I would need to check our notes when it came to this specific component.
Because when we were talking about, I think what the intention is, is for this to be a drop down that then just shows the additional menus. So I\'ll check my notes to see if that was implemented for here. I know that we definitely did that for the dining widget, so I\'ll just need to check how we handle it for the content carousel.
So I don\'t know if Rick was able to hear that because yeah, no problem. OK, yeah. So what I was saying was that I do remember we talked about having the drop down appear. I know that that is in place for the dining widget for cafes.

**Lyon, Rick (Director of Digital Experience)** 46:05
Sorry, I just got back. Um.

**Daniela Tea** 46:17
I need to check to see what we implemented when it came to this specific component. I think it\'s probably like similar functionality maybe you\'re looking for, but I just need to check to see if we implemented that and how it was implemented and I can get back to you on that one. OK.

**Lyon, Rick (Director of Digital Experience)** 46:17
Hmm.
Go.
Yeah, that\'s fine. I mean, like, you know, I don\'t think we went into like too much detail on the hotel side, but I do think that we did discuss at least that part and during like a walkthrough. I just don\'t know if it got captured or anything soon. Cool. Thank you.

**Daniela Tea** 46:33
Yeah.
Yeah.
Yeah.
OK.
Yeah, that\'s what I\'ll definitely go and check on that one, right? Yep.

**Lisa Cardia** 46:48
And I\'d say for this one, just, you know, the same thing we\'ve been saying that knowing the baseline dimensions for the asset here going to be definitely critical for us since it\'s such a wide image. I don\'t want, you know, a very tall image impacting this or selecting the wrong image. It\'s.
Going to break this component essentially.

**Daniela Tea** 47:09
Yep, noted.
OK. And then let\'s take a look at this in mobile really quickly. So just shrunk the screen so you can see how things are stacking. So essentially those three columns are just in a row and then the read more details is underneath that and then just displays underneath the.
The buttons for both both the three column and the two column.
OK.
All right.
OK. All right. So if there\'s no other questions about the content carousel, we can move on, excuse me, to our drop down language selector. I think we have covered this one before just because I this is this should be on the corporate privacy policy.
Pages. Essentially this can be used for a drop down or it can be used for a language selector. The use case that I know that you guys are using again is for the privacy policy where you\'re able to put the label on the button.
The icon by default right now is the globe icons, since that\'s what I believe was used on those pages. And then you can see how I\'ve populated the different links, one for English, one for French, and then when I click on that I\'m just able to display whatever I want. However, the reason why I\'m saying.
Drop down slash languages because of course if you just need this to be more like a like a drop down menu essentially, then you can simply disable the icon, just you know, put whatever the label needs to be. And so then instead of it being more with a language selector, it\'s more just like a a page menu.
Menu that you can have if you need to use it within the pages. So the icon I think is just typically what you guys are using for your language selectors, but by disabling it then you can just kind of use it as a normal drop down menu.

**Lisa Cardia** 49:13
I just had a couple things on it, Daniela, and this may have gotten corrected, but we noticed this a lot on the cafe sites that if you kept the drop down open, it like overlaps the content beneath it. Like there was like a point where like multiple drop downs were.

**Daniela Tea** 49:15
Yep.
Mhm.
Mhm.

**Lisa Cardia** 49:31
I I don\'t know, creating some sort of like overlay on the content that you wanted to click under it. Had you kept one open or another? I think that got reported.

**Daniela Tea** 49:38
Yeah, I think I yes, I do. I do recall that one. It was specifically when the language selector was used in the dining widget component, like at the top portion of all the cafe pages. So yes, I do remember that issue being reported. I would have to check the status on if it was fixed, but I yes.

**Lisa Cardia** 49:49
Yeah.

**Daniela Tea** 49:58
Yes, you guys did report that one. So yeah, it\'s it should have been captured in JIRA.

**Lisa Cardia** 50:00
OK.
And then the I have just two questions on this component. I think you kind of answered it with one, but if we did want to change the icon, is that a development ask or is there just a possibility to like insert it somewhere on the back end as a content author but with someone with permissions?

**Daniela Tea** 50:21
So right now this is is is only showing 1 icon and the disable icons essentially show this or show not or don\'t show it. Sounds like what you\'re asking Lisa is like say like the ability to have like a library of icons to select from perhaps.
Ups um.

**Lisa Cardia** 50:37
Yeah, or a lot. A lot of times we use like, I don\'t know if we\'ll get away from this, but currently we use like font awesome for certain things to pull it in. So wasn\'t sure just the flexibility that we had here.

**Daniela Tea** 50:44
Mhm.
Yes.
Yeah.
Yeah so right now that is not present in here but what I what I could see you guys doing in the future like what if this if this were to get expanded on is having the library like save guys just want awesome or whatever icon library having that put as.
So like a generic list and then being able like a developer would need to enhance the component to allow the author to be able to select from the list of icons so that way it would display here instead. So like instead of like say like display disable icon, it seems like you guys might want to enhance this to essentially be like a.
Drop down select from a list and then it would display to the left and maybe there\'s an option on there that\'s like none and then it would just display as if it was disabled as in like the icons not there. So that would be a code enhancement. Yeah that that would that would be a development item, but definitely something that I would recommend you note down.

**Lisa Cardia** 51:41
Yeah, just so we know our options code, OK.

**Daniela Tea** 51:50
Or like gap, like the gap portion. Yeah, I can totally see how that could be used in the future.

**Lisa Cardia** 51:51
Yeah.
And and my other question was this seems to always left align. Is there a way that if we ever needed this drop down to be center on a page, I can\'t think of a use case really for right right alignment, but there\'s no way to change the alignment like we can with like buttons.

**Daniela Tea** 52:11
Yeah.

**Lisa Cardia** 52:13
So just I I was hoping we would have similar functionality if the three buttons you have below you know are are can use styling to do something like that so.

**Daniela Tea** 52:14
It\'s.
Yeah, I I see what you\'re saying. So for this itself, the only available options for styling is just changing the primary or secondary. What you\'re asking for is like say you want it to be center aligned or right aligned, so that\'s not presently in the component itself.
I\'m wondering, let me try something.

**Lisa Cardia** 52:43
I thought I tried with a container and I don\'t know if it was possible, but.

**Daniela Tea** 52:46
Yeah, I was just about to say I wonder what I I don\'t think it actually would work because I believe the language selector is essentially full width. I don\'t think this is able to necessarily be like resize the way that you\'re looking for. So what you\'re what you\'re asking is is something that I would also recommend putting within the.
The gap analysis portion, because while you probably could kind of fiddle around with it, I think what you\'re looking for is mainly like something where you\'re able to have like a center alignment or right alignment specifically on this component. Yep.

**Lisa Cardia** 53:19
Yeah, because it\'s like a button, so I would assume it would have had those same.
Uh functions or say my styling options.

**Daniela Tea** 53:25
It.
Yeah, Nope, understood. But yes, so currently not present on here because I believe it was always left aligned. However, totally understand how if you guys want to use this for other use cases, it would make sense to have an alignment built into that.

**Lisa Cardia** 53:41
Okay, thank you.

**Daniela Tea** 53:42
Yep.
OK, all right, so that is the drop down language selector. Moving on to tabs. I know you guys are also familiar with tabs, but just as a refresher, taking a look at how these tabs are.
Builds 2 variations. As we know I\'m going to click on properties, we have our horizontal style variation or we have the vertical style variation. So I have those on the page itself. Horizontal just means of course the buttons are going to be horizontally aligned.
However, when it\'s vertically aligned, you can see here instead of it appearing on top, it\'s going to appear on the side. Additionally, you also have a title that can show on when you\'re doing a vertical aligned tab.
I\'m gonna show this here. So I\'ve used in my properties the title field and you can actually put a description as well if you need to, but I don\'t. I don\'t know how often you guys are using that right now in the tabs that are currently live.
But the title field is what you\'re going to want to use when you have a vertical style for my items on the first tab, memorabilia, rock wall and in-house clinic. This is what populates the actual tab names on top and you will notice here. I\'m just going to cancel.
When you\'re viewing it in author, the vertical variation on author is is not going to display as you\'re expecting, so it\'s only it\'s only going to display when you are viewing it as published.
So just to be clear, like if you\'re seeing this here like this, you\'re like, oh man, this looks doesn\'t look like what I expect. If you view as published, it should look like this version.
OK, and of course with the tabs, essentially what the tabs is doing is kind of like how you have your other like just carousel components and such. As you\'re clicking on the tab itself, there\'s a container underneath for you to be able to add.
Your content underneath it, so that\'s you edit it within the container. So if I were to edit this here, I\'ll see here\'s a container specifically for my tab. I can put any component I want under the Rockwall tab. You do have to hit preview and then click on the next tab to be able to.
Edit that specific tab, but you\'re able to. Again, you\'re able to add any component within here. It\'s not. I do not believe there\'s any restrictions. Yep.

**Lisa Cardia** 56:26
And Daniela did. I don\'t know if I\'m because I\'m going back and forth between my notes and you said you needed to view as published. You don\'t have a spacer in there, right? The spacer just doesn\'t show in the authoring environment. That was one of my that there wasn\'t any really great spacing below the tab buttons.

**Daniela Tea** 56:33
Mhm.
Oh, oh, so I.

**Lisa Cardia** 56:42
But I wasn\'t sure if that\'s just in. Did you add a spacer?

**Daniela Tea** 56:48
Yeah, so I added a spacer to each of these. So I think, yeah, by default right now the container is just there. And so as you\'re adding your content, yes, there is a spacer that you would likely want to add within the container if.
And so like for example for your gap analysis. So if you know that you\'ll always want the spacer, that can certainly be added, but that would be a change with the component to build in a spacer to every container that\'s within the tab.

**Lisa Cardia** 57:07
Yeah.
OK, I think that\'s a really big take away for a lot of the components that we\'ve seen just over the course of the last few weeks is that it\'s really difficult that as content authors that that kind of attention to detail is needed just for adding one component to a page like it. It leaves a lot of room for error if not everyone\'s using.
Adding the spacer, they forgot it, or they\'re using a different pixel of a spacer. So just for consistency purposes, that\'s a big one I think that we need to add to the gap analysis.

**Daniela Tea** 57:42
Mm-hmm. OK, Yep, that makes sense.

**Lisa Cardia** 57:45
And then something I\'ve also just noticed in general, and I don\'t know if it\'s just my own authoring environment, but every time I use the preview mode, not view as published, but preview. If there\'s no like spacer added to the bottom of your content, you cannot Scroll down to see it.

**Daniela Tea** 57:55
Uhhuh.

**Lisa Cardia** 58:02
Which I find very defective. So if you if you had added a component to the very bottom of your page, most times than not, I can\'t scroll and view the entire component unless I had added a spacer or two and then clicked preview. Not talking view as published, but preview.

**Daniela Tea** 58:05
Mhm.
Hmm.

**Lisa Cardia** 58:20
And I experienced that like a a a lot of the practice pages that I built.

**Daniela Tea** 58:26
OK, so I think I would want to see that simply because I would want to understand first like what templates you might be using to see that. Second thing, what components? OK.

**Lisa Cardia** 58:37
Yeah, I\'ve I\'ve only been using open page templates myself.

**Daniela Tea** 58:41
All right, OK, so there\'s that. I think I\'d also wanna understand like for example, do you have like a navigation set up with like the footer? Has that been applied or is it like these are this isn\'t like the experience fragments are like you\'re not pointing experience fragments for these or?

**Lisa Cardia** 58:57
No, I the only thing I\'m doing is clicking open page and then testing out the component with whatever components already come with that open page. I didn\'t like add the header or the footer, so if it didn\'t have those, it was just me testing on the page. Does that impact it?

**Daniela Tea** 59:12
Well, so like I guess because you mentioned when you put a component at the very end you\'re not able to access. So I\'m just trying to envision and understand like like for example how might it look for you? So like right here this is my last component on the page, right?

**Lisa Cardia** 59:19
Mhm.

**Daniela Tea** 59:28
So that\'s why I\'m trying to understand like where is that being placed? Like I have my container here, right? So this is my my my container for all my content that\'s within it. And then there\'s the root container, which is, you know, essentially everything that\'s on the page outside of the experience fragments are being.

**Lisa Cardia** 59:29
Yeah.

**Daniela Tea** 59:48
Within this root container. So that\'s why I\'m just trying to understand like where you\'re placing the last component so I can I can understand like how to replicate that.

**Lisa Cardia** 59:58
Does that matter though if it was in root container versus the container you had above it? So if you were to add to the like, I don\'t think you\'re personally going to see it with the stay connected and everything on this page. If you were to build a brand new page from scratch using open and all you did was say let\'s test out this tabs and we add.
Add a tabs component to a blank open page. You would notice it.
So I don\'t know if that\'s just like a limitation of the fact that I\'m building on a page that\'s not exactly replicated to be header, footer and everything you see here.

**Daniela Tea** 1:00:36
Mm.

**Lisa Cardia** 1:00:38
Hopefully. Did I lose everyone? Oh.

**Daniela Tea** 1:00:40
I\'m processing what you\'re what you said. I think that, um, yeah, so.

**Lisa Cardia** 1:00:40
Oh.
If you just went into like the sites right now click to open page because that\'s I pretty much would do that with every component and that\'s why I\'m I\'m ready to go with questions is because I\'ve tested these. So if I just went from here and hit create and I used open.

**Daniela Tea** 1:00:54
Mhm.

**Lisa Cardia** 1:01:06
Yeah, and just if you call it tabs or whatever you\'re going to do.

**Daniela Tea** 1:01:11
That\'s fine.

**Lisa Cardia** 1:01:14
From this page is where I would just simply add to the container or to the page, whether that\'s you know at the very bottom there and I would click tabs.
And I would have it populated with like probably just the bare minimum just to see it in action.
I would click preview and I would not be able to scroll.

**Daniela Tea** 1:01:49
So this is what I mean like I would need to see the page so I can understand like how it\'s been set up and also you know like potentially like like what your container, what your page structure is. So I think Lisa you do have like an example. I\'m happy to take a look at that.
You know it under.

**Lisa Cardia** 1:02:06
Yeah, it it would be though like since there\'s nothing on the bottom, is that the reason why I\'m I\'m experiencing that is my question I guess because all of my test pages, I\'ve never gone the additional step to put a header and a footer because of time. I\'m not just trying to do that. So maybe that is the reason I don\'t want to like.

**Daniela Tea** 1:02:23
So.

**Lisa Cardia** 1:02:26
Come up with my own solution, but like I found it really hard to preview a lot of the components I wanted to test on a regular open page because it would cut off, but I never added a footer.

**Daniela Tea** 1:02:38
So keep in mind that the header and footer are actually being set. Excuse me, are actually being set at the homepage level, right? So like you would set it here once and then any child page that you create underneath it will automatically inherit that.
So I guess if you\'re like, So what the fact that I created it at this level? Sorry, excuse me.

**Lisa Cardia** 1:03:02
You could actually you\'re you\'re in the stage environment. You could find all of my test pages, which is fine for this. I would hope it would still show it on your end. I\'m not. I don\'t have stage open, so I don\'t know if this won\'t replicate, but if you went to.

**Daniela Tea** 1:03:06
It.

**Lisa Cardia** 1:03:17
US at the bottom US.

**Daniela Tea** 1:03:21
Mhm.

**Lisa Cardia** 1:03:22
English. I think this is where it\'s always um Hard Rock second one down Lisa component test pages and then scroll to tabs I guess if I if I have it marked on my.

**Daniela Tea** 1:03:39
Mhm.

**Lisa Cardia** 1:03:41
Mm-hmm. Yeah, so maybe it\'s gonna show if you click preview.

**Daniela Tea** 1:03:46
Yep.

**Lisa Cardia** 1:03:47
Yeah, you\'re on preview. See how you can\'t see it.

**Daniela Tea** 1:03:49
I see that.

**Lisa Cardia** 1:03:51
I\'ve experienced this a lot of times, no matter the component, so I\'m just wondering why I can\'t see it. If I can see it in the edit mode, click preview quickly, can\'t scroll on my content and it happens more times than not without me adding a spacer beneath it.

**Daniela Tea** 1:04:00
Mhm.
Mhm.
Yeah, so I would need to take a little bit of time to take a look at what\'s going on on the page, like what\'s going on with these containers. Are these just, you know, I can see it.

**Lisa Cardia** 1:04:19
It would be me adding things more like I\'ve been playing around with these pages so I can\'t tell you why I have an extra container or two now, but just know that if I started from scratch, put this on the page, you would not be able to scroll.
And it\'s with like a lot of the components. But again, maybe that\'s a limitation of it not in having the header and the footer. I don\'t know, but these were just my random test pages.

**Daniela Tea** 1:04:38
So.
So I I think in terms of this, so yeah, I totally understand when you create a test page or like I just need to see what the component looks like, how it works when you preview it. Because I I can\'t answer you right now as to why this is happening for your test page. What I would recommend though is.
For the for future tests, I would set it up similarly to like however you guys would be using the pages. So kind of like how I have my little training folder here and careers like you could set up a section to be able to essentially establish what would that.
Excuse me, what would that header and footer experience fragment be and just set it once, then create all your child pages underneath there. So then you\'re also able to see it with the theme, like whatever theme applied that you need. So if you\'re working in hotels, I\'ve also keep in mind I\'ve also set the theme be hotels so I can see the correct color for the CT.
I can also see like if it\'s in the cafe section, if this was changed to the cafe, I mean we\'ll see that that correct color for there too. So I would recommend doing that if you guys are testing so that we can understand exactly how it\'s going to look for your theme.
But I will. I can certainly take a look at this to kind of understand like what\'s going on, because I do understand the frustration of not being able to see everything that you need as you\'re testing a component. But I would say though I think it it would be best practice though to try and test it with the correct theme applied, meaning having that parent level.
With the theme applied because like right now this is the corporate theme. However, if you were trying to understand, you know, like for hotels or whatever, like I I personally, when I test things, I like understanding how it\'s going to be for the site that I\'m testing it with, meaning the theme is applied. So that\'s personally how I\'ve done things is just making sure I\'m at a specific level.

**Lisa Cardia** 1:06:36
Yeah.

**Daniela Tea** 1:06:39
That has a homepage that has the theme established and the header experience fragments added.

**Lisa Cardia** 1:06:44
Which are you guys able to confidently confirm that this works across themes? Because I do have in my notes that it was not working for Cafe on mobile and I must have that written down for something with the theme. So I just want to is there any way we can get confirmation that this has been tested on all of them?

**Daniela Tea** 1:07:03
Are you talking for the are you talking about the for for tabs?

**Lisa Cardia** 1:07:06
For tabs.
Yeah, and and I do want to also call out that like the tabs accordions are gold on desktop, but they turn to black on mobile. So I do want to call that out. I\'m not sure if that was like a miss or intentional.

**Daniela Tea** 1:07:19
Let\'s take a look here.
So we are saying.
Actually, I\'m going to view this as published. Let\'s do this.
We\'re talking about these.

**Lisa Cardia** 1:07:42
Yeah, so you see how they\'re all now black, but they were just gold.

**Daniela Tea** 1:07:48
I don\'t think they would have been gold because this is using the hotels theme.

**Lisa Cardia** 1:07:55
Can you go to the one though that we just or the LC tabs?

**Daniela Tea** 1:07:59
So keep in mind though LC tabs though has no feeding like.

**Lisa Cardia** 1:08:02
It.
OK, so that I just assumed this is the the gold is showing me the Hard Rock theme.

**Daniela Tea** 1:08:10
So what are we trying to do here? So we\'re saying.

**Lisa Cardia** 1:08:13
To see how it was gold originally experiencing that on on desktop, but now they\'re like we lost that gold the highlight.

**Daniela Tea** 1:08:23
So see. So when it\'s expanded, it is gold. Is is that?
You\'re saying, you\'re saying, I guess you\'re saying because it\'s not expanded and it\'s not showing.

**Lisa Cardia** 1:08:38
I guess maybe that\'s why I\'m sorry, my note is from. I probably tested this a little while back so I can look back into this so I don\'t waste the time of the group.

**Daniela Tea** 1:08:47
OK.

**Lisa Cardia** 1:08:47
Thanks.

**Daniela Tea** 1:08:48
Yeah, let me close out that and let me close out of this one as well. Let\'s see. OK. Um.
All right, so tabs, we talked about the different variations. I\'ll take a look at your page, Lisa, afterwards and see if there\'s a can get back to you. As you mentioned, the tabs is accordion and mobile is a selection that can be checked. If it\'s not checked, of course.
Then it would look a little bit differently. I\'m going to uncheck this version, hit done.
Do it over here to see what happens. If we were to look at this in mobile, what happens?
Oops.
I actually think it affects the one on the top, not the one. One second guys, one second.
O for here.
For my tabs U here I\'m going to set this one. This is a horizontal version. I\'m going to set this to not be accordion and mobile.
And I\'m going to refresh here and so we can see the tabs instead of being an accordion is going to instead display as three buttons on top, right? So this is this is this is the default because by by default if I were to add a tabs component here.
Add it right on top here tabs component. I do not believe. OK, so actually I\'m sorry, this is checked as tabs accordion mobile. So by default it\'s going to have the accordion, but if you don\'t want it and you want it to be like this instead where you have the three tabs as buttons on top of the content.
You would just need to uncheck this um check box here for it to function like this instead.
OK.
All right. Um, OK, scrolling on. The last thing I had on my agenda was the table component. I know that you guys are also using this currently on the Um.
Corporate website. This is actually. I took this example from the corporate website. I believe it\'s on the Heals Foundation page if I\'m not mistaken. I also saw examples where you guys have tables on some of the hotels pages. It doesn\'t have necessarily the zebra striping or or anything like that, but it\'s.
Or just like a table to display information. So some use cases that can certainly be across different different lines of businesses. But of course with our table component you can establish how many rows you want, how many columns you want. Do you want a table header?
Do you need a section header within the table? With percentage allows you to say, hey for this column I want it to be X amount, say like by default what it\'s going to do is try and do things, you know, like just kind of resort itself to to make sure that everything fits within the table.
So you can see I didn\'t set anything for the width percentage. However, this is just, you know, based off whatever I have. However, if I were to say, let\'s do oops, so this is actually 10.
OK, so you can see now it\'s taking 10% of the table, whereas now charity partner is taking 90.
If I want something to be a little bit more even, maybe try 30 so that it it\'s going to redraw itself so it can take up however much I want, but if you don\'t put anything there, so I\'m just going to remove the width percentage.
And then you can see by default how it will display. It\'s essentially going to say, OK, there\'s two. It\'s basically going to be 5050 if I don\'t put anything there.
Yeah, so the parallax and G lightbox stuff. These are things I\'m going to cover when we go over the container. To be honest with you, I don\'t think this is actually really used in the table component, but I\'ll show you guys how it works when we cover a container on Wednesday.
But the main things for the table component is the table tab, the section tab, and then there are a couple of style variations such As for the borders with colors, the full border or striped, the sub header row color, the table row color.
Header row color. And then there\'s also the ability to select a piece of text within here and determine what color you want that cell to be. So let\'s say I want it to be yellow here and say I want this to be red here. So essentially some highlights are available for the table cell.
So this is your like your text component. To be clear, this is like a standard text component. So if I were to add a text field here like outside of the table, I do believe that the table cell color is something that\'s available. So the reason why is because the text component.
The component is comprised of several different text. The table component is comprised of several different text components, so that\'s where you\'re going to see the style variations that are for all the text components available in here, but mainly you\'re going to be using the table cell ones.
And I think that\'s that\'s that\'s really what you\'re going to be focusing on when you\'re interacting with these cells.

**Lisa Cardia** 1:14:26
And Daniela, I guess my question, unless this is answering it just for something like this unique feature, but I guess just like why wouldn\'t we just use the table feature that exists in the like rich text editor to build this?

**Daniela Tea** 1:14:39
Yeah, so you could certainly do that too. In terms of, I guess in this case here, I think it\'s it\'s really dependent on if you prefer. So I\'m gonna put this here. So in case people aren\'t aware, there is this table feature that allows you to do this.
There\'s a couple of I think additional pieces of functionality that are present in within the table component itself, but you could also, yes, you could also use the table within here. So I think it\'s really up to you guys what you guys wanted in terms of the table component that\'s being used on the.
Yields Foundation, all the variations and stuff that\'s present here. That\'s why we were using the table component, but you can also use the text component if you want.
Mm.
OK, I\'m going to delete the front page. All right, so breadcrumb, sub NAV, site map, content, carousel, the drop down language selector, the tabs component.
And our table components. Any other questions about these specific components?

**Lisa Cardia** 1:16:02
Unless I unless I missed it, did you go over the features of the table component where it allows you? It says like animation class and.

**Daniela Tea** 1:16:12
Oh yeah, so I was saying that this stuff here is. I believe that this is actually not going to be used in the table component. I\'m going to check with our dev team. This is typically going to be used in the container, which I am going to show on Wednesday.

**Lisa Cardia** 1:16:27
Oh.

**Daniela Tea** 1:16:28
So I\'m going to talk to the team about these two tabs, but you guys will see how it works, at least with the container component on Wednesday.

**Lisa Cardia** 1:16:34
Is there a reason that these were built that way? Like I guess it\'s it\'s just a little bit confusing to an author to see the options, but then to have to say that wasn\'t meant for this component. Like why would they just be options? Like could we not remove them so there\'s no room for error?

**Daniela Tea** 1:16:49
Yeah, so that\'s why I want to talk to the dev team to understand because I think the table component is. I believe it has some inheritance coming in from the container. I do want to confirm and check that. My understanding though is that this would there isn\'t necessarily use case for the table, but I want to talk to the devs to see.
If there was and and how the parallax or G light box functionality would affect that. So that\'s all I\'ll get back to you. And if there if it is something that can be used on a table, I will also show that on Wednesday, but you\'ll at the bare minimum see the functionality and how it\'s presented when it\'s being used within a container component.

**Lisa Cardia** 1:17:25
OK. And then the only other question I had was actually related to all of the colors. I noticed like between like border, the sub header table, header row, we get like a medium Gray and a light Gray as options for border but nowhere else.

**Daniela Tea** 1:17:30
Mhm.

**Lisa Cardia** 1:17:42
I just, I\'m just curious, I guess, like why it\'s not consistent of all of the options for every every section.

**Daniela Tea** 1:17:48
Yeah, so I would have to check the actual ticket for it. I think when we had established what was needed for each of these different sections, although it was like specifically called out for the color. So I\'m not, I can\'t answer right now exactly like why is there like right up here but not downs here.

**Lisa Cardia** 1:18:06
Yeah, or like a medium. We have us. OK, yeah, if you don\'t mind checking, I just found it a bit confusing that they weren\'t consistent with their options.

**Daniela Tea** 1:18:07
Like the header row, I would have to check the ticket for that one.

**Lucas Nelson** 1:18:17
But Daniela, either way, if we need additional options there, that can just be marked under gap analysis, right?

**Daniela Tea** 1:18:24
Yeah, certainly.

**Lucas Nelson** 1:18:25
OK. Yeah.

**Daniela Tea** 1:18:26
That\'s certainly.

**Lisa Cardia** 1:18:27
OK.

**Daniela Tea** 1:18:28
And.
All right, OK, so let me go back now to our wanna go back to the our Confluent page here.

**Lisa Cardia** 1:18:30
Thank you.

**Daniela Tea** 1:18:44
OK, excuse me. All right. So tomorrow and Wednesday, as I mentioned, we are going to be covering things such as the line of business specific components. So I\'m gathering together those. I will be publishing that draft hopefully this afternoon.
And then we\'ll be attaching it to the calendar invite. And then my last one, which is currently called Untitled, it\'s because it\'s essentially the rest of the components. So things like the button, the separator, which I know you guys are familiar with. So things that I know you all are also familiar with is also why I was keeping it for the end.
But definitely want to make sure there\'s time to discuss cards. So that\'s going to be covered here in Untitled. But I will be publishing these either this afternoon or very early tomorrow morning once I can gather the remainder of what\'s in the list. And then starting on Thursday, we will have our tech.
Technical knowledge transfer sessions. These are going to be morning sessions so that our GCTA will also be able to attend and then the adoption sessions will be beginning on Thursday afternoon and then as we continue the week after with additional technical knowledge transfer.
And then starting March 16th is when we\'ll actually go over the platform expansion sessions. This is where we\'ll discuss what\'s been documented, the use cases that the SHRSS team has come up with over the course of the.
Past few weeks. So we have 6 sessions scheduled for those taking us into the week of March 23rd. So I am going to pause though and see if there\'s any questions about the calendar or what\'s ahead for the next couple of sessions or if there\'s any other questions or comments.

**Lisa Cardia** 1:20:38
Are we gonna get those invites this week, you think? Just or at least placeholder if Scott, could it do something like that just so we don\'t lose the time? I don\'t know.

**Lucas Nelson** 1:20:45
The platform expansion ones, Lisa.

**Daniela Tea** 1:20:45
Look to me.

**Lisa Cardia** 1:20:47
Um, I I was just checking like my weekly calendar and I think I had for this week the adoption strategy, but not those morning ones, so that we were just referencing.

**Lucas Nelson** 1:20:57
Scott gave me the attendee list. I would ask him if he can forward those on.

**Lisa Cardia** 1:21:02
Is it not just like everyone?

**Lucas Nelson** 1:21:04
At least you\'ll have to ask Scott that.

**Lisa Cardia** 1:21:08
OK, he\'s not on the call.

**Lucas Nelson** 1:21:09
Yeah.

**Daniela Tea** 1:21:10
And and just to confirm, Lisa and Luke, do we these are sent out already, is that correct? Well, or at least placeholders, they wouldn\'t have the agenda yet, but I just want to confirm.

**Lisa Cardia** 1:21:11
OK.

**Lucas Nelson** 1:21:19
Yeah, tech. So technical enablements have placeholders. Andy\'s going to be sending in the agendas by at the latest Wednesday morning.

**Daniela Tea** 1:21:26
Oh, no, I I\'m sorry. Look, I meant the the two remaining clots.

**Lucas Nelson** 1:21:28
No, we haven\'t sent the agendas yet, but the placeholders are on the calendar for the content authoring, yeah.

**Daniela Tea** 1:21:33
OK. Yeah, that\'s what I was. I was want to confirm Lisa that those were on your calendar and so you will see an update to that once the agenda link is added.

**Lisa Cardia** 1:21:42
OK. I think I was confusing it with the the early morning ones that we were talking about. So those are the ones I didn\'t see.

**Daniela Tea** 1:21:48
OK, yeah. So yeah, that would be a definitely a a Scott questions. I think he\'s managing the attendee list for that, but are we sending out the platform expansion ones as well, Luke, this week?

**Lucas Nelson** 1:22:01
Yeah, I can put the placeholders on those for sure. Yeah. And and state state intention. It it\'s it\'s basically what\'s on this page here. I\'ll just restate it in the invite. Yeah, right. Yep. That\'s a good idea. Yeah.

**Daniela Tea** 1:22:04
OK, OK, sure.
Yeah, we can. Sounds good. OK, perfect. Thank you.
Alright.
Alright guys, um, there\'s no further questions then. Thank you guys for joining and I will be sending out the remaining agendas shortly.

**Lucas Nelson** 1:22:29
Thanks, Danielle.

**Daniela Tea** 1:22:29
Thank you guys. All right, goodbye.

**Charles Baugh (SHRSS)** 1:22:31
All right. Thank you.

**Lucas Nelson** 1:22:32
Have a good afternoon.

**Lyon, Rick (Director of Digital Experience)** 1:22:33
Thanks everyone.

**Lucas Nelson** 2:13:37
Hey Angelica, can can can you drop from the call so the recording can stop?

Lucas Nelson** stopped transcription