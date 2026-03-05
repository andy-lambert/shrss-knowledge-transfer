**SHRSS Adobe Knowledge Transfer-20260226_130306-Meeting Recording**

February 26, 2026, 6:03PM

2h 17m 23s

**Lucas Nelson** started transcription

**Lucas Nelson** 0:09
All right, Danielle, it\'s all yours. Thank you.

**Daniela Tea** 0:11
All right. Thank you guys. Good afternoon, everyone. Let me go ahead and share my screen so we can go over some page template items today. So what we have identified here are the page.
Page templates that we currently have in the system. So we\'re going to go over the home page template, which I believe that the content authoring team should be familiar with already as well as the open page template. There are a couple of other templates that I think you know if we can explain what they are, you can understand how that might be.
Used and then these two templates. Here we have a messy burger page template as well as a microsite page template. I wanted to create an example of those so I might not be able to show them today, but essentially this is the template that\'s used.
For those very specific pages in cafes, we created a special template because there was a lot of custom functionality that was expected for that page, so it had its own template. And then also for these microsite page template, that\'s something that\'s specific to the microsites that are present.
In the hotel, we can take a look at a live example within the state environment if there\'s one available, but if not, my plan is to create one and then I can walk through that in our next session. But first, let\'s take a look at how to access existing templates.
So I am going to navigate to the template section which is available by clicking on the AEM in the top left. I\'m going to click on the tools icon and then general tab we can see.
Right here is a section that\' called Temlates.
And just changing my view so I can show Hardrock Seminole and then we can see here there\'s quite a few templates in here and you can see when the template is enabled, when it\'s last been modified, if it\'s published, etcetera.
And you know, I like this to be better. If we were to take a look at, say, our homepage template, this is a template that\'s already been created. It\'s already been in use. One thing that you can do if you\'re ever curious to see what pages are using your templates is by opening up the side rail.
I can see just the content, just the templates that are available, or I can click on references. When I select a specific template type, let\'s do the news homepage because there\'s not too many. I can see that there are 7 pages that are used in that template and when I expand on that I can see.
Exactly which pages are are using it. I can also have it take me back to the site section so I can see the exact page. In addition to that, if you\'re ever curious about what template is being used for a page.
When you select the page itself with the the sites, the sites who you\'ll see here underneath name where it says template and it tells you what template you\'re using. So just some things to keep in mind. If say you see a page and you want something maybe similar, you can understand what template they started from or.
If you want to understand, hey, is this template something that people are really using? Is it popular? You can come to this section and just simply select it and view what pages are referencing that template. All right, so let\'s take a look at our homepage template.
And what it consists of. I\'m going to go ahead and click on Edit.
And one thing that I wanted to point out is that when it comes to authoring templates and you know, creating new ones or editing the template, that sort of stuff, I believe this should have probably been covered in the authoring training that the team took.
From the Adobe Learning Services team, there are several different parts for this template to be able to be edited. There\'s of course the admins being able to like a certain admin group to be able to allow.
Adding the template, you know, depending on permissions. There\'s also the developers who would need to set up things like the template policy and some of the more technical details about it. And then for the content authoring team themselves, the ability to do things such as editing the structure or editing the initial content on the templates.
So that way when the template is live and you create a new page based off of it, it\'ll automatically have whatever set in the initial content. So there\'s different roles that are involved with creating a template for the content author themselves. So what will likely be the case is that the development team will identify.
The sections of each template, sections on the template for each layout container, identify which components are allowed, which policies are being applied, and then setting some of these additional details here so that way the content author themselves doesn\'t need to worry about that. So that\'s more of a development.
Task and there are going to be certain authoring groups in the permission side. There\'s a template authors group that I believe is is part of part of the Hard Rock environment right now, so not everyone is going to have access to be able to.
You know, create a new template or edit or anything like that. It would be based off of whoever\'s in that specific group. And from what I saw, I think like folks like Gonzalo and I believe Lisa and probably the rest of the team on Lisa\'s team, you guys would have access, but say somebody from like.
A random cafe or hotel. They wouldn\'t necessarily have access to create or edit the template or anything like that. Just want to make sure it\'s clear that before you just start creating new templates, there are some things that would need to be set up from the developer side and.
That\'s some documentation that I can certainly send out or put on the page from the link site. But taking a look at our homepage template, this is very similar to what you would expect like with the page layout. For example here I\'m clicking.
And I can see the content tree, so I understand what has been set up for the structure of the homepage. So for our homepage, what have been established for this template is the top portion has a component called the Alert Aggregator.
We have not reviewed alerts yet. That\'s something I do have on the schedule though, but essentially this is at the top of the header. You can see this portion here is experiments. Experience fragment is intended to be used for the header, but the alert aggregator is essentially on every single home page at the very top. So if it is.
Configured with actual alerts that it would always display. We also have, as I mentioned, the experience where I went to display a header. We have this container which contains 2 layout containers.
One which represents the hero, the hero banner, hero carousel. Essentially those are the only components that can come here in this portion of the page. And then here is essentially like the main container, like the main page content section, and you\'ll notice it has a list of all the allowed components.
So as additional components are created, that would just be that could be allowed based off of what\'s added in the policy. You can see here this is the allowed components tab. We can see that Hard Rock Seminole content.
Components have been all added. Everything that\'s within that group is available for you to use. This is essentially what you see whenever you are interacting with the page. When you\'re editing a page and you do insert new component. This is the list of components that you should see when you\'re editing the page.
Finally, at the very bottom we have our experience fragment which is intended for the footer.
And so this is this is the homepage template. The main difference between the homepage and say like the open page template is there is this section to be able to have like that hero carousel at the top. It\'s been defined already for you. I believe I saw a.
Either a JIRA ticket or a question or a comment or something about why the hero carousel isn\'t necessarily available on the open page. It just was defined this way where we had requirements that said that the homepage would always have that. However, the open page doesn\'t always have a hero carousel at the very top.
So when you are considering building out templates, typically you want to make sure that it\'s flexible enough to be used for, you know, your various use cases. But then there\'s also of course the need to have some specifics. So for homepage, since we knew everything, every homepage would always have a section.
Above the main content, that\'s why that was defined. However, for an open page template, we want it to be more flexible, so we didn\'t include that section since it seemed a lot of pages were not necessarily using that we didn\'t receive requirements.
For that to be captured. However, moving forward that can certainly be added and edited on on the open page template. So this is the structure. We can see what\'s here. We can see when we go to the initial content portion of this.
That certain things have already been set. For example, if I wanted to say I\'m not going to add it here, but if I wanted to to add a specific hero carousel here so that whenever you create the page off of this template you always.
Want that specific image or something there? That initial content can be present and set in advance on the template side, so that way it could potentially save your authoring team some time. But again, if these are supposed to be, say, flexible for.
Multiple lines of businesses or, you know, multiple sites. You need to just be aware of like what\'s going to make sense for your authors. What would make sense for for your initial content to be able to apply to several use cases, but just keep in mind that as you\'re planning your templates.
You are able to set things up so that way you can save your author team time. Just wanting to make sure that you are still keeping the templates a little bit flexible in case some use cases don\'t cover that. All right, when I click on layout, I think we\'re familiar with the layout mode.
You\'re able to essentially resize the structure the the contain, excuse me, the components that are on the page based off of your view port. So if you know that say you have like a the hero banner on here and perhaps you know that you.
Want it to appear in iPad? You can set that hidden button in advance on the template side. So that way when your authors start using this template, they don\'t have to worry about doing that themselves. It\'s already taken care of at the template level.
So all they have to do is just focus on essentially like adding the content versus setting up that layout. So this here though is the home page template. Let me take a look at showing you an example of a home page.
Right.
Yes, Edwin, go ahead.

**Edwin Aquino** 12:27
Just to just to confirm, any edits we make to the template don\'t impact existing pages that use the template. This is just for new pages that are created, correct?

**Daniela Tea** 12:34
So you\'ll see here editing the structure will affect all the pages referencing it. So right now, yeah, so like you do want to be careful. And so I\'m mainly talking about the pages that I know that are like the pages that I know that you guys, I\'m sorry, the templates I know you guys are likely going to want to create. Definitely want to.

**Edwin Aquino** 12:42
OK.

**Daniela Tea** 12:54
And make sure you kind of plan that out because of course right now there\'s as we saw, I think there\'s like I think 420 home pages right now. So if I were to edit this right now, that affects all those 420 pages that are using this template.

**Edwin Aquino** 13:08
Now, how exactly would that impact those pages? Would it change the content as well or just the the the components that we\'re adjusting here? I\'m just, yeah.

**Daniela Tea** 13:15
So if you\'re yeah, yeah, if you\'re adding say, I\'m going to make this a little bit bigger. If I were to say add like another container here or something like that and and perhaps add that initial content right there, then that should add that also to my page.
However, if I were to say like set some initial content for like sections that have been established, that\'s where you\'re going to potentially run into trouble, right? So I would strongly advise making sure that if you\'re making updates to templates of things that already exist.
You know, of course there\'s with the cloud services, I know backups being taken up, so you could potentially restore content, that sort of stuff. But I would certainly make sure to try things out down in say lower environments or or such, you know, just to make sure that you\'re not.
Essentially having to do a roll back if possible, but yeah, just want to be careful with anything that\'s that\'s already being used. But I believe when you guys start identifying things like I think there was a need for like a say like a cafe template, right? Make sure you\'re planning that out and you can certainly set up whatever you need in advance.

**Edwin Aquino** 14:12
OK.

**Daniela Tea** 14:27
To make a couple test pages to see if it covers what you need, make those edits, and then certainly, you know, start creating pages. So there\'s a way to edit it after it\'s been used, but you still want to be careful since that template\'s already live. Yep, Yep, Yep. All right, so.

**Edwin Aquino** 14:38
Got it. Thank you for clarifying.

**Daniela Tea** 14:45
Here\'s a look at my homepage template I\'ve used. I am using and I\'m just going to show this. So by KT homepage, if I check it, you\'ll see it\'s using the homepage template, which you\'ve established is it concludes an experience fragment.
The alert aggregator through the top, some containers, one that includes a hero carousel and then also a layout container which is manually for all page components and then a bottom experience fragment. Let\'s take a look at how that is.
Your no, this is not it here as we see same structure alert aggregator. Now the experience fragment you may wonder why am I not able to edit it here? This is something that is actually presets. We\'ll take a look at where I had set that.
So the experience environment is displaying. That\'s what the header and the footer are, right? But I\'m not. I don\'t edit it through this page. I edit it somewhere else, but we\'ll take a look at that in a second. Here\'s my earlier aggregator. Here is my container, my first container, and here is my second container, just as I have right here. So you guys can kind.
I see like I created a page. It\'s using this template. This is what it looks like when I first create it. It matches the structure that I\'m expecting since that\'s what was established here. Now if I were to create an open page template, I want us to take a look at that since that\'s what the majority.
Of your pages are. I\'m going to select this and I actually want you guys to see how many pages are referencing this template and I\'m going to go ahead and open up my open page template. I have Bing that I\'m using so we can see how this gets mapped.
All right, as you can see, it\'s thinking quite a bit because so many pages are using it. So I\'m going to go ahead and click edit and we can come back and check how many pages are actually using it. All right, so we\'re looking at the open page template. I take a look at my.
At my content tree, we can see exactly what\'s been established. For the most part, what you\'re going to be using is again the open page. The homepage template is going to be mainly for.
Setting up your site. So what I mean by that is in this homepage template there are certain properties that are going to be filled out that establish essentially any child pages underneath it. So when I mentioned the header and footer experience fragments, I had set that here.
At the homepage template level, the page I choose my homepage template and then underneath there where I\'m using my open page, it\'s going to inherit that experience fragment that was established within the properties I\'m gonna go.
More through properties and such, but just wanted to show why when I created the open page, why is it automatically look like this? Why is the theme color applied? All of that is established at the homepage level. At the open page level is where I believe the content authors.
Would be creating content ages in general.
So here in my open page we can see I have a hero banner here and I\'m going to go to initial content just so you guys can see in this section here where I previously had a layout container and it said what\'s components were allowed. Here it\'s establishing it\'s a hero banner.
That\'s why over here I see here banner. If I wanted something different to appear in this section here, what I would do is I would add whatever component I wanted. These are the allowed components as we saw from that previous page. It only allowed five different components in the section. That\'s why I\'m seeing 5 different components here.
If I wanted to say change out the hero banner to be a hero carousel to appear initially when creating a page, this is where you would do it.
You can see here a breadcrumb has been established in this container section, so that\'s why when I created my new page, a breadcrumb automatically appeared here and then this last container I think.
Let\'s see where it is. Yes, this last container is actually just the root container. Essentially you\'ll see the little icon here. This is an unlocked container. This is for the entire page itself. So creating an open page, my initial content includes.
A hero banner and a breadcrumb, just like what we can see here. Hero banner and breadcrumb. The alert aggregator is appearing. There\'s nothing set because it\'s it\'s just there, but nothing has been configured for this. You\'ll see it\'s blank, and that\'s because of course it\'ll be different based off what page you have.
But this hopefully this can you guys can kind of see as you\'re planning out your templates again as you understand like what components would make sense for like say a cafe template, you know having your your experience fragment set up so that way it\'s pointing to having a header and footer.
Having a section for bread crumbs, perhaps having like an event section, etcetera, etcetera. So that can be set up by both structure, identifying the different sections and then the initial content, actually selecting the components and even configuring the components with say.
You know, like like a specific hair banner that might be present on every single cafe. You could set that here. So with our open page template though, a couple things to keep in mind as we see here the.
Navigation at the top and the footer are the same as what was established in the homepage template. Now Edwin, I believe you had asked a question I think a couple of days ago with regards to how do you create a page that doesn\'t inherit from that homepage section, right? So like maybe you want something.

**Edwin Aquino** 20:57
Correct. Yeah.

**Daniela Tea** 20:58
At the same level, but you don\'t want say this here, right? OK, so we do have a blank page template and so I started thinking about I was like actually you could use this. So the way the blank page template works is it is literally what the name is. It\'s a blank page.
So what that means is there is no header and footer, right? So we\'re just going to put show you what this is. There\'s no header or footer associated with it. So if your intention is to say add a header and footer, you can can do it by adding your experience fragment.
And then you can reference whatever header or footer you know you want to use instead of the one that\'s that was established at the level up top. I\'m just going to choose a random one so you can you can kind of see that I\'m going to hit done. So let\'s see. Yeah, so you can see it says order now.
Reserve a table, menu, locations, catering, etcetera. If I were to go to my other page, my open page that I just had, you\'ll see this has different, this has a different navigation, right? Destinations, hotel and resorts, casinos.
But this one, my blank one has many locations catering right? So they\'re at the same level KT open page, test blank, but I\'m using different header navigations because I\'m using blank page template. So I just wanted to check if this is kind of like the use case that you were looking for.
Like to fulfill, you know, with the different header, header and footer for a specific page.

**Edwin Aquino** 22:40
Yeah, that that\'s correct. So sometimes we occasionally have footers that are a little bit different than other pages or you know, so, so yeah, this this would qualify to to there\'s a better issue.

**Daniela Tea** 22:44
OK.
OK, perfect. So yeah, so the process for that always keeping in mind is since it is an experience fragment, you would create an experience fragment and just point to the reference. And something else to keep in mind that I did want to point out is that it\'s still going to inherit the theme colors and.
I\'m not sure if that\'s part of your use case too, Edwin, but like you can see here, like the theme that I\'m using is actually the hotels theme. I know that because the buttons are purple and that\'s the that\'s one of the indicators. So even though I\'m pointing and using a different experience fragment, it\'s still going to inherit the same.
Themes, it\'s still going to look kind of similar to that. Does that make sense? Hoefully that is that is also in line with your use case that you were describing.

**Edwin Aquino** 23:29
OK.
Um, um, I\'ll have to bring that back to the team. But yeah, it sounds like we we can discuss that if that\'s needs to be adjusted.

**Daniela Tea** 23:34
OK.
OK.
OK, awesome. All right, so let\'s take a look then. As I mentioned before, the blank page is literally a blank page, but we can always take a look at what has been established here. I\'m going to just click on edit.
So you can see initial content, everything\'s literally blank. There\'s a container on here and that\'s for you to be able to add what you need, all the components, you know, like literally the experience fragment all the way to the card to everything. So it\'s just a blank page. And so it sounds like there are already some existing use cases for that.
O hoefully the team will be able to use this as you guys see fit.
Alright, OK. Some other pages that you guys are also currently using. We talked about like the news homepage and the news page and the new search template and I I think we might have taken a look at them. We can look at them right now in terms of the structure and such.
But yeah, so at one point you you guys had seen that there was an experience fragment at the top of all the news pages. You\'ll see that was set in initial content. So this is where it\'s coming from that image. It was set here on the template side. So when you create a new page, it\'s always gonna have this banner.
Of course, you know in the future if you guys realize that\'s not necessarily something that you want, that that is something to consider potentially changing. But again, keep in mind not a draft anymore. Pages are using it, so.
Use some caution, but as you can see here like we\'ve this specific template for news home page has quite a lot of different components on here versus the open page since this was specifically for news with the and with the news search results component.
Category listing, etcetera. So from the initial content point of view, you can see that some things are already preset. So in this case here, initially when you first create your page, your news homepage, it\'s going to point to the CF list path. However, of course the author themselves.
Can change that. So this means like in the future if you guys have different news pages that you might want for different sites, it might make more sense to have a news homepage template with the initial content set to point somewhere else. So that that\'s going to be decisions you know that your team can make.
Keeping in mind that initial content is just to help the author be able to have essentially like placeholder values, which they can change as they\'re creating their page.
Right.
So with our structure, you can see the structure portion like we mentioned before. It\'s more I\'m establishing what needs to be on this page, but the initial content is I\'m establishing exactly what I hope a user will see when they first create the page.
Based off this template and then layout is again was I go look at different viewports, I can establish how I want that to be laid out. So that way the content author doesn\'t necessarily need to do it, but they do have the ability to change it.
As they\'re working with the page. OK, so we had our news homepage template, which was created for the corporate website. We have our news page template, which is for those specific articles.
Structure is going to look pretty similar to what we had for experience fragment for the header container for every component in there. Experience fragment for the footer. Initial content is where we establish what belongs on a news page.
You\'ll see the different ieces added here.
And then finally, um, the last uh news related template was the new search template.
And initial content. The main difference I believe is the new search results here, which is the main difference between the other two. So this is how I know you guys are already creating news pages in general, so these are where those templates are coming from.
And you guys can can see how they were initially set up. We also have a an experience fragment template which I believe the team is also familiar with called the SHRSS blank variation. This is essentially the same or very similar.
To that blank page. However, it\'s it\'s special because it\'s for an experience fragment. There\'s some things behind the scenes that makes it use for the experience fragment itself. So that\'s why you would want to use this when you create. When you create an experience fragment, you would want to make sure you\'re selecting this template, however.
The same premise is as an author. You know, you just add whatever component you need after you\'re using this template. That\'s the purpose of this is for experience fragments exclusively. All right, you can see that here. OK, let\'s see what else we have.
Uh, so the footer variation is specifically for footers.
In this case, I believe we were to take a look at.
Go to structure.
So you\'ll see that the footer variation only allows specific components since this is what was established. So when you are creating footer, if you wanted to, if you wanted to add something crazy like I don\'t know, like a media gallery, you cannot do that. You are restricted from doing that.
And if you were to take a look at the template policy for this, this was again when I mentioned things about policies, that\'s something that more than likely like the developers would have set up for the content authoring team. But the policy that has been selected is specifically for XF footer, you can see that what.
Variations are using that and you\'ll see that these are the list of allowed components. So it was the policy is to essentially restrict a content author from being able to add basically the world to a footer, so it\'s just restricted to these specific items.
So we have been using this when whenever you see your your footer at the very bottom, it\'s using that footer variation template and experience fragment. And let\'s see here, what else do we have? The event page is also.
Is also a custom template that was built. Um.
And we talked about events in general structure is going to look exactly like you expect pretty bare bones because we\'re just saying we need a section that has all this has all these components available for an author to select from.
However, the initial content itself has the specific component that should be present when a an author creates a page based off of this. In this case it\'s the event detail. You\'ll see there are some values that have been preset. Hard Rock live event calendar event details, no special error message.
Has been set here, but these are the same exact fields that you\'re going to see as an author when you create a page based off of this template. But this is this is where those placeholders come from.
Let\'s see. So for the messy burger, again for the messy burger and the microsite, I would like to make some pages based off of those and show them to you guys at a later date. But again, therefore both the cafe page as well as the hotel page.
I\'m going to pause here though, and see if there\'s questions about the template set up, you know, editing it or adding a new one. And then we\'re going to go to page properties. Hey Edwin, I see your hand up.

**Edwin Aquino** 32:00
So is there any way we can organize templates by like folders? So let\'s say we have templates specifically for casino sites. We can have templates listed there or templates for cafe. We can have a specific folder for that. Or is this just all in one general location?

**Daniela Tea** 32:15
So I\'m in my templates. So this is there\'s templates. So right now this established structure have been having Hard Rock Seminole, which is essentially you know like all the custom ones that have been created specifically for Hard Rock Seminole. What you\'re saying is you might want like say this error page and event page to be specifically.
For casinos, like essentially organization, is that correct?

**Edwin Aquino** 32:39
Yeah, right, correct.

**Daniela Tea** 32:39
Like you might want these at. OK, let me think. I think that has to be set up by an admin to essentially have a section like a lot for that. Like this is what I was talking about with like there\'s three different roles when it comes to creating templates. So that would have to be established I believe at like the admin level and then.
Also.
Also identifying which user groups would have permissions to that specific folder. So we don\'t have that set up necessarily because these are all intended to be used globally. But yes, you should be able to have additional organization as needed and then also be able to set up who should have access.
Access to the to those to those specific folders.

**Edwin Aquino** 33:24
OK. All right. Thank you.

**Daniela Tea** 33:25
Mm-hmm. All right.
OK. So yeah, so that\'s definitely something to think about. Like what do you guys necessarily want that might be global or what might you want that\'s specific for your like your line of business. So yeah, definitely things to plan as you\'re coming up with what templates are needed for your properties.
All right. OK, so now let\'s take a look at our page properties for some of our templates and get an understanding of, you know, what\'s custom, what\'s not, what\'s out-of-the-box. And I\'m just going to navigate back to my admin.
Now we\'re going to take a look at our homepage template first. All right, so I\'m selecting this. I\'m going to click on properties.
And um, all right, one second.
Actually, was it media? I\'m just checking something really quickly. OK, yeah, so media is the one where I filled out everything so we could take a look at how that translates when we resource. OK, so with our homepage template.
As I mentioned before, the most important thing to set at the homepage, one of the reasons why this is extremely important is as I mentioned, the child pages underneath will inherit the theme and will inherit the.
Header and footer. So if I go to our SHRSS themes tab here, this is this is where you establish that I have said I want my specific site to have the Hard Rock theme and for my sub theme it\'s going to be the hotel theme, which is why we\'re seeing those purple buttons everywhere.
And for every page that\'s created underneath this homepage, I want to make sure that it has this header experience fragment and this footer experience fragment. So as we saw, yes, you could add a blank page underneath there and kind of establish your own on the page itself.
But if you\'re using the open page template, which is heavily what most of the sites are using, this is where it\'s inheriting the information underneath the home page that\'s established for that site. So this is very important to set if I were to move to our custom common tab.
Again, these these three tabs. So sorry, you guys might be wondering why am I focusing on these three tabs? Everything before these three tabs are have are out-of-the-box page properties. So AEM provides, you know, specific page properties that are applicable.
For pages for different things such as SEO purposes or you know like special configurations that you could set. However, again, all of these are out-of-the-box. We do have some documentation on that which kind of go a little bit more in depth as to like what is the title, what is the page title, navigation title where?
What are these going to use, etc. But the only thing that has been customized for the basic tab I would say is when we discussed vanity URLs, I explained the process for creating a vanity URL due to the shortening rules that we had established as we saw with the International Women\'s.
Month page. So that was the one consideration I want to make sure the team was aware of is you have to put the full content path versus just like a slash women so that that this is still out-of-the-box, but there was a special consideration because of the shortening rules we had in place.
But all these properties that you see here are out-of-the-box and I can certainly try to answer some questions with regards to how they might be applicable to the team, but we do have the documentation experience link that we could take a look at.
For for some of these properties, all right, so going back to our custom tab. So here with our custom common tab you can see some options, one for hiding the breadcrumb. This means that the breadcrumb component can stay on the page, but if you just don\'t want it to be visible.
You can, you know, check it. So it\'s possible that you know you can also delete the breadcrumb component from the page itself. But if you want it there, but you say you want to temporarily hide it or you don\'t want an actual user to see it, that\'s what this checkbox is for. There\'s also the hide scroll to top button.
I think you should be able to see it on hardrock.com and I think Reverb is using that as well. That\'s the button that appears in the bottom right and let\'s see, where did it go?
Going back here, we have the LD JSON field, so that\'s gonna be something that\'s visible when you view. When you view page source, there\'s a value right here, so this this here.
Anything that needs to be displayed within this section of the page, I believe that\'s for. As I mentioned, I believe that\'s for SEO purposes would be put into this section here under custom common and then we have the OneTrust cookie configuration.
I believe if we were to take a look at the home page, we could see exactly what value was here as well as the domain script key that was entered here. And again this is set up for at the home page level and then the child page is underneath.
Should inherit this. So you should. If you view a homepage template, you should see these values filled out. And then finally there was an analytics tab established. It had these four specific fields. Now there are certainly additional values that.
You know, are being captured from the analytics side. However, my understanding of this was that there were four specific values that would need to be added at the homepage level. So that\'s what you see here. I think this is also available.
If we were to take a look at our open page template, you should be able to. Actually no, you you should not be able to set it at any child page, but you would set it at the home page and then all the child pages essentially would inherit that value.
So these three tabs, the SHRSS themes and the analytics are actually specific to home, but the custom common is another custom tab. These are three custom tabs that were created for every SHRSS template.
And that\'s what you\'ll see here. Here\'s the custom common, but it\'s missing the themes because this is not a homepage. It\'s missing the analytics because this is not a homepage, right?
Uh, I\'ll pause here to see if there\'s questions about these three tabs.
Hmm.
Yeah.
Mhm.
Yeah.
Yeah.

**Edwin Aquino** 40:41
That just because that\'s something that\'s definitely used a lot by the team.

**Daniela Tea** 40:44
Yeah, sure. So let me pull up the test page that I made and we can take a look at how it translates to the source. All right. So for starters, you may notice that this particular page has a thumbnail associated with it and the author.
And let me show you. I know that\'s not actually what you asked, but I am using the images tab here. So the intention for the featured image is this is what actually populates the OG image field. Edwin this here and then the thumbnail that I established is what\'s going to be displayed within the.
The AEM sites console like we just saw. So that\'s why you see this here. But this is what populates the OG image field. You are not able to set the image until after you create the page, so I wanna make sure that\'s clear. So you\'re thinking, wait, I\'d never seen that before.
If I were to try and create a page right now and I\'m just going to select open page, you\'ll see. Oh actually yeah, you\'ll see here on the images tab. I can\'t interact with this and that\'s because you need to have the page created first, but then once you open the page back up again, you\'re going to be able to interact with it.
So that\'s one field I think would be relevant to the team. So here we go. Here\'s my KT Media page. I\'m going to open up the publish side of this so we can see the source.
This was the page that we were messing around with yesterday and I published it. So it is not pretty by any means, but we\'re not actually looking at the page content. We want to see the source. OK, so take a look here. As we can see, title is a required property.
And it\'s not present here because this page has already been established, but there is the name field. I believe Ed, when you had a question about what the name field is, the name field is the URL. So like right now the name that I had was KT Dash Media.
When I was creating the page, if I want it to be something else like knowledge transfer instead within that field, I would have put, you know, something like this. Yeah, Carlos, go ahead.

**Carlos Aldana** 42:55
Sorry Daniela, the the feature image, where can I see it? Where is the is it displayed?

**Daniela Tea** 43:02
Oh, so the featured image one you can see. Yeah, so when you can see this is the image value right in the meta property OG image. You can see this is the image value right in terms of the display. The intention for the featured image is that for some.

**Carlos Aldana** 43:17
Mhm.

**Daniela Tea** 43:22
Components like yesterday we had used the image component and by default it was displaying this image. That\'s because I had set it here. So if I were to.
Um, let\'s see. I\'m gonna cancel this. I wanna open my KT media page.
You\'re trying to actually see the image and if I were to add a new image here.
It\'s going to automatically display that featured image because that\'s what I had said right? So from the AEM standpoint, the featured image is being used whenever you have like an image component. This is checked in here featured image. However, it\'s also intended to populate this the OG image meta property.

**Carlos Aldana** 44:08
But for example this morning I I built the a blog history story and and and I added the on the feature image a logo because I wanted to see if maybe that would be displayed as a priority.
On the home page because the story had like a an image with text and it was inappropriate if I wanted to display it on the home page on the blog widget.
So in that case the the the feature image doesn\'t work.

**Daniela Tea** 44:48
Are you talking about this here? So this is he, yeah.

**Carlos Aldana** 44:49
Yeah, yeah, so that that\'s that\'s the image I associated to the story, but it but I added on the on the component. I added a different image as a feature image, but I didn\'t see it anywhere.

**Daniela Tea** 45:06
So we\'ll take a quick look at this. So just to be clear, so the featured image for the page property is not necessarily associated with this component. I believe this is a content fragment list component, but I will take a look.

**Carlos Aldana** 45:13
Oh.

**Daniela Tea** 45:25
Um, so I think we\'re talking about two different use cases, but can certainly check to see what our homepage is using.

**Edwin Aquino** 45:34
Just for clarification, Daniel, like the featured images used whenever we\'re sharing it like on Twitter, like a a little the preview image, correct? OK.

**Daniela Tea** 45:39
That\'s the intention of it. Yeah, that\'s the intention of the OG image. So that\'s what I was saying, Carlos. I think you know what you were expecting from that feature image tab is not actually how the component is used, but I\'ll just take a quick look. So yeah, the content fragment card list.

**Carlos Aldana** 45:41
See. Um.

**Daniela Tea** 45:58
So this is the default image. So obviously if you had not had any image associated with this, it would display this instead. And what you\'re saying is that you\'re trying to change this image, is that correct?

**Carlos Aldana** 46:09
The the the story had a different image with some text and we don\'t want to display that. So we decided to go when we had those stories we we used this one. This is like the default image for us, but I wanted to try to use.

**Daniela Tea** 46:26
Hmm.

**Carlos Aldana** 46:29
Use the the image that they provided with the text and to be displayed on the story. But then I wanted to add the feature image on the on the place that you just show us in order to probably see it displayed on the on the homepage.

**Daniela Tea** 46:43
Mhm.

**Carlos Aldana** 46:49
Because it said feature image, so I assume that maybe it will be working like that, but it\'s not the case probably.

**Daniela Tea** 46:56
Right. So I\'m going to take a look here. So the image that you set is this, right? This image field is being used for like at the very top. Like I think, yeah, the intention of this image is to be at the very top of the article as well.

**Carlos Aldana** 47:02
Yeah.
That that one, yes.

**Daniela Tea** 47:16
well as what\'s being used for this content fragment card list. So I think if you were trying to say add some additional images, you would likely want to, yeah, go ahead.

**Carlos Aldana** 47:24
Yeah, on the properties on the properties section probably.

**Daniela Tea** 47:29
If you wanted to use additional images within the story, you would want to add it, say within the RTE, right? Or you know like on the actual page itself. You could also say like you wanted something at the bottom of of this use content fragment. You could add a new component.
Own it for an image, et cetera, et cetera, right? So I guess to to be clear though, this image that\'s here is the image that\'s being set in this section here, and this image is currently being used also for the content fragment card list.

**Carlos Aldana** 47:51
Oh no.
Yes, but can you check the feature this this section that you use to show that is does it?

**Daniela Tea** 48:15
Yeah.
So if we were to take a look at this here, this feature, yeah, so this featured image property is not being used in relation to the article image or this like. So as I mentioned, if we were to let me see here.

**Carlos Aldana** 48:19
See that? That\'s what I added, yes.
OK.

**Daniela Tea** 48:34
Going to click on edit just so I can see what this is called logo if we were to.
I think this is this is the live page. Is that right, Carlos? OK, let me let\'s find that.

**Carlos Aldana** 48:46
Yep.

**Daniela Tea** 48:56
OK, so looking at the OG image value, you can see how it\'s taking in the image that you had set Hard Rock News logo, right? Corporate logo is Hard Rock News logo. You can see how the value is taking what you had set in the featured image property field.

**Carlos Aldana** 49:13
Yeah.

**Daniela Tea** 49:14
So that that\'s that\'s what this is used as well as if you were to add an image right now to this page, it would also, you know, show that specific image that you set within that field. But if your intention was to try and you know, change this right now, this is going to be pulling in from whatever was the established image in the content fragment.

**Carlos Aldana** 49:33
Yeah. OK. OK. I get it. Thank you.

**Daniela Tea** 49:36
So yeah, hopefully, hopefully that makes sense. I think you know, like I mentioned, hopefully you can. If you need to add that image here though, you can certainly do that by adding say like another component or trying to use the description field. But yeah, keeping in mind though the featured image for the page is.
Going to map to the OG field, OG image field and then the thumbnail that I saw you had also set that maps to the thumbnail that\'s displayed here, right? So like if we were to look at your page now in AEM, you would see that that thumbnail image that you would set within the page properties.

**Carlos Aldana** 50:02
Mm-hmm.
Yeah.
Yeah.
Hey, saw that.

**Daniela Tea** 50:17
Yeah, OK, cool. So that you guys, you guys can also that can be helpful to add a thumbnail. You know, if you guys need to quickly find something like I was like, where\'s my page? Oh, it\'s right here. This thumbnail I know is set, but that\'s something that the team can certainly start using now. It\'ll certainly help the authors, you know, versus seeing.
It\'s just like a kind of, you know, generic image. So if you guys need to see something, you can classify it quicker, maybe having something different for like a homepage or an open page. That way you guys can just quickly see it by looking at the thumbnail. So some options for the team.
Let\'s take a look though back at our page properties. I\'m going to go back here.
OK. So Edwin, I think you were asking about, I was talking about the name field and I know that was a question that you had had when I create my new page is when I set the name field and I believe your question was with regards to what exactly is the purpose of the name field.
So this is going.

**Edwin Aquino** 51:21
Oh, not sorry, not necessarily. It was basically with the the news page titles like the news page name, because normally if we leave that blank, I think it auto populates the full URL based on the title. So I\'m not too sure if if the name is what we would use to override whatever gets populated there for the news articles.

**Daniela Tea** 51:24
Oh, go ahead.
Oh, I see.
Yeah, if you wanted to change it. So like, say the news article name was like, I don\'t know, like Hard Rock. I\'m just writing it like this intelligent Hard Rock news, right? And say you\'re like, Nope, it should be just like SHRSS news or something. The name field is where you would put this and then that would be what is sent in the URL.
Like it would look something like that, right? But the title itself would still be whatever\'s established here. That\'s what\'s listed on the page that would be listed, you know, within the tab name, that kind of stuff. So this is essentially a field to be able to change like, you know, like you mentioned with the Neos at the auto populates to be able to.
Change it to maybe something that\'s shorter because I have a feeling the use names are probably pretty long, so that\'s certainly an option. Keeping in mind though that the name does have, I\'m gonna try to show that again one second. Here we go. Those have some.
Validation in place. So you\'ll see here what I did was I typed a letter and I put a space and that is not allowed. So it\'s going to tell you what is allowed, which is lowercase alphabets, numbers, underscores, hyphens. So that way you know you guys are not making a page that could potentially break something.
So there is some validation in place here and I think you guys are probably aware of this, but just in case, if you say you have a name and you kind of messed up and you misspelled it and you\'re recreating your page, the way to fix that is selecting your page.
Clicking on move.
And then page name after the move. You know, make your correction. We\'re going to do this. Hit next. Select where you want it to move to. In this case, I have my page under KT home. I want to stay there. I\'m going to click next.
You can see it tells me, oh, hey, you know you actually have something that\'s that\'s going to be adjusted and or has like a reference. And so I\'m saying, Yep, republish that. I want that to happen. Click on move. I want to do it right now. Hit continue.
That\'s OK. And so now if I were to refresh, you can see this page no longer exists, right? Because I moved it. I go back.
To where I was before.
Oops, Nope, it\'s not there. It goes here. Yeah, you\'ll see my name is here and it\'s been updated. I published it from that previous screen that we saw. Anything that is referencing this page should still work because the references for for it should have gotten updated as well.
So um, yeah, and out of curiosity is as a team had um have had to like move any sort of pages or rename any of the names or anything like that as of yet.

**Carlos Aldana** 54:33
Yes, images, yeah.

**Daniela Tea** 54:35
OK.

**Edwin Aquino** 54:35
I believe we, yeah.

**Daniela Tea** 54:37
Perfect. OK. Yep. Just making sure. Sounds like you guys are using it just great. So that\'s perfect. All right. Yeah. Yes.

**Edwin Aquino** 54:43
Uh, Daniela, with the move, however, so we did notice that the page broke, right? The previous link. Um, what if?

**Daniela Tea** 54:48
Yes, the. Yeah, because, yeah, yeah, yeah. Sorry, go ahead.

**Edwin Aquino** 54:52
So no, I\'m just saying in cases that where we still need people like if they have the old link to redirect to the new one, is that what we would use the vanity URL for to have that old link as well?

**Daniela Tea** 55:03
So, OK, so the purpose of the VAD URL is I\'m actually gonna let\'s, you know, like for let\'s take the International Women\'s Month page as an example. That\'s an established page. It\'s not getting moved, but you want people to access it by having like a more user-friendly URL.
Vid URL essentially. So that\'s the purpose of Vid URL. The page is there. The Vid URL is just going to take that user to the page that you have established in AEM, but through a different URL. What you\'re asking for though is like previously we saw I had KT Media. I have now changed the name to KT Media SKFJH.

**Edwin Aquino** 55:22
Yeah.

**Daniela Tea** 55:41
You, however, have a link to KT Dash Media, correct? So that would be like an actual redirect that that needs to be set up. So I think there\'s a couple of ways you could go about doing that. I think I I mentioned previously that there have been some redirect rules that were.

**Edwin Aquino** 55:45
Yes.

**Daniela Tea** 56:01
Established in the dispatcher, we\'re gonna be covering more about that. Those are like including the ones that have been added from Visergy and migrated over. So one of the URLs, for example, for the International Women\'s Month that was established I believe in Visergy maybe last year, the year before or something that got migrated over that\'s in the dispatcher.
You guys don\'t have to worry about that. What you guys would do here though for a redirect oops, I\'m gonna click properties.
So under the advanced tab there is a there\'s a redirect feature. However the way what this is saying though is that my specific page that I had for not the one I just did, my specific page can be redirected to someplace else and this is considered a permanent redirect.
So what I did with the naming portion, that changes all the references within AEM and stuff. However, if you were to have like KT Media, you can establish the KT Media page, then redirect to my new KT Media page by setting it up here, having a KT Media page point to the new one.
If it\'s permanent, set it there. So that\'s that\'s one way to do it. Again, the other way would be to do the redirect through dispatcher, like creating a rule for there for a vanity URL. I think if you\'re saying that the page no longer exists.
There is a rule for media URLs where you are not able to add an existing page here. So I think what you\'re describing is if it was actually well it would just be like slash media or something like if what we would have before would go here and that should work because the page.
No longer exist in AEM, but I just want to make sure you\'re aware of like some options. Dispatcher for redirect rules. If you had an existing AEM page that needs to redirect to another AEM page, you would do that here and then the VADI URL needs to be a page that doesn\'t actually exist in AEM.

**Edwin Aquino** 58:03
OK. That clarifies that. Thank you.

**Daniela Tea** 58:04
Hi.
Yeah, all right. OK, so we\'re taking a look at our KT Media page so we can see where these titles are all populating.
OK, so title again, very important. It\'s a required field. You need a title for your page that gets populated in the title field because I\'ve appended a a brand slug. You\'ll see I had override KTM brand slug that is also part of the title.
So we\'ll see how that displays here in the title tags. I think you guys are familiar. This is you adding any associated tags that you might want for the page. This might affect things such as we\'re looking at lists for example. Edwin, we were looking at like say we want a list that has this tag on it.
Then it would surface up whatever you applied here. So that\'s what this is is used for. The hiding navigation checkbox is used for things like the main navigation or the OR like the breadcrumb. There are components that specifically will pull in pages if you don\'t want.
That this page to appear in those components because say it\'s it\'s on a page you just want surface to user. You can select this and it would hide it from those components so it doesn\'t appear in like say a site map or something. Scrolling down our HTML ID field. Now this is something that would be applied like you know into the markup so that way you would be.
Be able to essentially attach it. I think it\'s at the. Let\'s see if I can find it. KTIT. So I don\'t think it was added because I put some spaces in it, but essentially this is what\'s going to be.
Added as like a a HTMLID so it you know the page can have like a unique identifier. For more titles and descriptions we can see how that gets inherited. Let\'s see.
YouTube Media.
T Media navigation title. I think the page title itself check this. Yeah, so this is actually the page title is an AEM. It\'s related to AEM. So when I drag the title component onto a page, it\'s going to take whatever\'s here versus what\'s here. If I leave this blank, it just.
It\'s going to take what\'s in this field, so none of these are actually necessary. As you can see, they\'re not required. But if you do want to establish, say like you know the title should be using this versus this when it\'s on a page, that\'s what you would put here. The navigation title, as we can see, populates.
Here in the OG field, OG title field here. I think there\'s a couple other places too. So we see Twitter title, data page title. Yeah, so you can see where this is coming in.
In.
OK, the subtitle. I think Edwin, you had that question about what is subtitle field documentation wasn\'t extremely helpful for certain. It basically says this is a subtitle for the page. This can be used as when you\'re referencing.
In components you might want to use this property so that way say your author has supplied something here and they want it to be displayed on a page without them having to edit it on the page. So right now we are not using the subtitle field, however I think.
If you guys say we\'re using the eyebrow text field within the title component, instead of having it editable on the page, it could theoretically point instead to the subtitle and you guys can manage it here. So that way the title and say the subtitle are both coming from the page properties versus having to edit it on the page.
So that\'s something that could, you know, potentially be an enhancement. But right now this specific field is not something that\'s necessarily used because we have the eyebrow field and the title component as essentially open text, but something that could be used in the future if desired.

1:02:16
Got it.

**Daniela Tea** 1:02:17
The the description field KT media description, we can see where that\'s coming in, how that populates in these areas. So this these these specific values as mentioned I think for SEO purposes hopefully.
Edwin, if there\'s like specific questions about like open graph or you know like how like how these affect SEOI would, you know, I could certainly take those questions back to the team so you know and provide more information. But was there something specific SEO wise that you\'re curious about?
You know from the page properties.

**Edwin Aquino** 1:02:55
No, I believe it was just mostly those specific categories. And then I know on some of our CMSS we can indicate a specific Twitter handle whenever we\'re associating with Twitter. Is that something that\'s on here as well?

**Daniela Tea** 1:03:06
Hmm, an associated Twitter handle. As in, I\'m sorry, can you like, can you like explain like like does it?

**Edwin Aquino** 1:03:13
It.
So it\'s whenever we share, whenever we share this, it\'ll automatically on Twitter, uh, attach that, um, handle to the link.

**Daniela Tea** 1:03:21
I.
OK, I I see.

**Edwin Aquino** 1:03:26
To the ship, yeah.

**Mayte Eme** 1:03:27
We have a section that I\'ve called out before that is a gap where we can set per site certain settings right their time zone. How do they prefer that day and time format? There\'s social handles for like a few things.
On other metadata fields and that\'s per site and that way when we have those sharing widgets, it gets associated.

**Daniela Tea** 1:03:52
So let\'s let me go back to the homepage template then. And again, you guys realize the reason why it\'s saying no page found is because this was the page that we had renamed and moved. But I\'m going to go to the homepage and make sure I again understand what you\'re just saying. Maite, you\'re saying per site meaning.
Say like the Hard Rock website or a specific hotel site, is that what you\'re referring to?

**Mayte Eme** 1:04:15
Every single website in Cycord.

**Daniela Tea** 1:04:20
Right. So, so like that\'s what I mean like, so like the Hard Rock site, a specific hotel site, a specific cafe site, et cetera, et cetera, like all of them at that site level, meaning not all these pages, you wouldn\'t set it there, but you would set it at like the Hard Rock site level or the Atlantic City site level or the San Diego site level, is that right?

**Mayte Eme** 1:04:25
What?
Yeah, those are site level for like languages, formats, associated content, like bunch of settings that we have per site.

**Daniela Tea** 1:04:39
OK.
Mhm.
Yep. So what I\'m hearing then is that it sounds like as we had talked about with the home page template. So each site we know would have a a essentially like a home page. That\'s where we\'re setting things like the theme and then the child pages inherited.
It sounds like what what would be needed in the future is to expand a little bit on on the tabs that we have. So it sounds like perhaps the custom common tab which is present you know on the homepage template but can is also present on a child page.
We might need some additional fields to be able to set some of those site wide variables that you\'re mentioning. Maite. It sounds like you mentioned social media. I\'m sorry, I don\'t remember what else you said, but if it\'s site wide and you want the child pages to inherit it, it would certainly make sense to expand upon these custom fields that are added.
Um uh to the page template.

**Mayte Eme** 1:05:39
OK. And just because you\'re showing this, if you can, is there a place where it\'s enterprise wide? We have both site level and enterprise level where it goes through every single website. We we call it like master site and whatever we put there, it gets pushed to every website.

**Daniela Tea** 1:05:49
Enterprise level.
Oh.
I see. So I think right now, so the home pages are being set underneath the line of business, right? So like, but what you\'re saying is even like above here, right? It\'s like above like at this level is what you would be wanting to set like some global properties that would then be inherited by every.

**Mayte Eme** 1:06:10
Mm.

**Daniela Tea** 1:06:17
Anything that\'s underneath it, is that what you mean Maite? OK, got it. So that to me, yeah. So right now we do not have it at that like at the very top level that you see here because it was all done within the homepage level which would be per site. So sounds like you know that could be an opportunity for.

**Mayte Eme** 1:06:19
Yes.

**Daniela Tea** 1:06:37
Or perhaps say like a specific new template that\'s created or something that should be handled at a more global level and then more specific fields for the site level etcetera. So I think this is the kind of information that would certainly need to be captured for the gap. Currently it is not part of what was done.
The implementation.

**Mayte Eme** 1:06:58
And I\'m sorry I bought it in. Edwin, I don\'t know if your question but answer.

**Edwin Aquino** 1:07:04
No, no, my question is answered. Thank you.

**Daniela Tea** 1:07:07
All right.

**Edwin Aquino** 1:07:07
I think it, yeah.

**Daniela Tea** 1:07:09
OK, alright, so let\'s see here. We talked about the so as mentioned before these these specific tabs are essentially out-of-the-box. We we covered how the for the basic tab that one slight change of any URLs and and how to.
The proper way to set up a fan URL due to the shortening roles. We talked about the custom tabs that are present on the page properties, as well as how the content author would interact with setting up a new template, how it requires.
You know some development as well as an admin to essentially say set up the folders like you were discussing Edwin for a specific line of business. We also discussed how there\'s a template author group, so not everybody would have access to that section to be able to create new templates or edit templates so that can be restricted.
Let\'s see, what other questions do you guys do you guys have with regards to templates?

**Mayte Eme** 1:08:13
Maybe this was asked, but if we create a template, can we use it on any site like at a master level or is it per site too?

**Daniela Tea** 1:08:22
Yeah, so yeah, no problem. Um.

**Mayte Eme** 1:08:24
If you ask that, I can rewatch it so you don\'t have to waste that.

**Daniela Tea** 1:08:26
No, no, might say it\'s OK. Yeah, let\'s just show that right now because at the templates right now, currently all these templates that we see here can be used by every site. There was a question that came up like.

**Mayte Eme** 1:08:40
And your first three templates because we might not want to use some on some sites.

**Daniela Tea** 1:08:45
So there was a question that came up about how could things be say restricted for like say casinos, like could there might be some casino specific templates or cafe specific templates. So that can be set up by an admin right now. Currently these are all global, but you know if if it\'s determined that certain.

**Mayte Eme** 1:08:47
Oh.
Yeah.

**Daniela Tea** 1:09:06
things should not be at a global level. That can certainly be set up by a site admin. I\'m sorry, an AEM admin.

**Mayte Eme** 1:09:13
OK, I was gonna ask, is that an admin as in power user or like a developer admin?

**Daniela Tea** 1:09:18
So there, so there\'s a couple different levels and it depends on what group you\'re in. I believe there is an admin group. We would need to check to see who\'s part of that. There\'s also a template authoring group. So that means someone who can actually create a template. I think typically that\'s going to be like your your developer and then there\'s going to be.
I think the Super users might have their own group. I\'m not sure if they would be considered template authors or not, but say people who might need to create templates based off of policies a developer had created, etc. So there are different groups and there could be different permissions that are set up for that. So depending on you know who should have access to what.
That can certainly be adjusted. Right now though, all of these templates are global and they can be edited and new ones can be created by the template authoring group.

**Mayte Eme** 1:10:09
Can you restrict sections of the template?

**Daniela Tea** 1:10:13
Can you restrict? Um, so let\'s open up a template and take a look. I\'m going to open up.

**Mayte Eme** 1:10:18
I think you don\'t want you you know we have and this happened with cafe right sections that we don\'t want people to touch that are managed by corporate. So some sections that are like shared or pushed by corporate to properties we don\'t want the content others to.

**Daniela Tea** 1:10:34
Right. So yeah, so you\'ll see here you can lock a structure component. What that means like right now it\'s it\'s open, right? You can see that the lock is unlocked. But yes, there are features to be able to lock certain parts of the page. I think some might say just really quick because I we I would recommend.

**Mayte Eme** 1:10:35
Touch.
Oh.

**Daniela Tea** 1:10:53
Watching the earlier part when you do get a chance because we talked about initial content, but the initial content is set to be able to allow a content author to change things that are on there. As in when they create a page based off of this template, this is what they\'ll see, like they\'ll see this image, etcetera. However, at a structure level.

**Mayte Eme** 1:10:54
OK.

**Daniela Tea** 1:11:12
Level. We\'ve established exactly what is allowed on the page, and if I need to lock some things down, yes, that can be locked down at the structure level.

**Mayte Eme** 1:11:16
Mhm.
OK, that\'s good. And last question I can think of just from you know what we have on on or issues that we have had another on inside court. If you edit the template and you push it, does that update the pages using that existing template or do they need a a refresh?

**Daniela Tea** 1:11:30
Mhm.
Yes, so Eddie. So yeah, there\'s a message here that mentions how this specific template is being used by one or more pages. So this is live. I think there\'s pages using it. If you edit it, your question is if I were to add, say like a new component or a section here, what happens to the pages that are already referencing it, right?

**Mayte Eme** 1:11:48
Mhm. Yeah.

**Daniela Tea** 1:12:00
So you would have to publish the template and you can actually do it from this view like you can see published template. It should essentially tell you. I don\'t want to do it here just because I know things are using it, but it should tell you like the ones that are using it are going to be updated like kind of.

**Mayte Eme** 1:12:01
Yeah.

**Daniela Tea** 1:12:20
You a warning, but you would publish the template to make sure that those pages get those updates.

**Mayte Eme** 1:12:26
So let\'s say that you added a row, you publish and that gets added and it\'s live before you had a chance to edit those pages. Or is there like a draft state where you can validate that you got added, add the content?
Or update the content and then publish live.

**Daniela Tea** 1:12:46
Let me repeat what you said. Make sure I understand. You\'re saying I\'m on my news page, my news home template. You want to add. I\'m gonna go to the initial content section. You\'re saying you want to add like something here, something.

**Mayte Eme** 1:12:52
Uh huh.
OK.
Yeah, let\'s say we got a Yeah, what we add a new component there.

**Daniela Tea** 1:13:05
You add a new component there. Your question is, does any news homepage template now have that component in place or do you need to republish the page? Is that correct?

**Mayte Eme** 1:13:16
So when you when you add the component you publish it, does it automatically get live in every single page that is using the template? Or is there a chance to actually go to those pages and update the content before it goes live? Because each page might need different content.
It\'s a placeholder for each different property to update in.

**Daniela Tea** 1:13:36
I see. So there\'s a difference between initial content and structure, right? So with my structure I\'m adding, you know, I can add, you know, different parts of the page, whereas the initial content.

**Mayte Eme** 1:13:42
OK.

**Daniela Tea** 1:13:52
Is adding like actual content to the page, right? So like in this here you can see this experience fragment has been filled out. Any pages that use this specific template when they first create a page based off this template will always see this. They have the opportunity to change it, right? So it sounds like what you\'re asking is you want to add say like a.
On the page, but you want the page to be able to like the page author to be able to select what content goes in that section. Is that correct?

**Mayte Eme** 1:14:20
Yeah, mm-hmm.

**Daniela Tea** 1:14:21
OK, so yeah, so adding the structure doesn\'t actually add like like content. When I say content, I mean like if you have like a title, like it wouldn\'t have like like specific text in that title. If you had a title component on there, the title component will will be available to the author, but you know they would have to.

**Mayte Eme** 1:14:36
Mhm.
Mm.

**Daniela Tea** 1:14:41
Still, like, configure it, right? So it sounds like that\'s what you\'re asking for, right? OK, yeah. So structure is where you would be like essentially setting up the structure of the template, like what should go there. You know, if I add a container, I\'m determining exactly what components I want a.

**Mayte Eme** 1:14:46
Yes, uh-huh.

**Daniela Tea** 1:15:00
An author to be able to add. In some instances I might not want them to add everything as we saw with like the footer. We don\'t necessarily want like a huge media gallery being added by mistake, so we\'ve restricted what can be added within the footer. So you can see here allow components because this is like the main container of the page, we\'re allowing every component.
But if we wanted to remove something the that can be that can be determined by selecting one second. This was checked. I thought this one this was checked. I\'m going to hit cancel. I\'m not going to say this, but this can be, you know, determined like if I just wanted three components to be allowed in that section we can.
Do that at the structure level.

**Mayte Eme** 1:15:40
M.

**Edwin Aquino** 1:15:44
So basically like you can add that component to the page and it I think the the big part of of my taste question was rather than pushing it all live all at once, we can go in and check which pages, how the pages were updated before it gets published. Is that is that like a a step in the process or as soon as we make the change to the template it\'s all live where?

**Mayte Eme** 1:15:45
OK.

**Edwin Aquino** 1:16:03
There\'s not really anything we can do about that. It\'s it\'s there and we just have to go and check it and change it manually, even though it\'s not.

**Daniela Tea** 1:16:08
So I think, I think what I what I want to understand though is like if you\'re adding like I can add any component to in the structure side of things and it\'ll be empty, right? So even if I were to, if I were to publish it like that page in the authoring side.
Let\'s see, let\'s take an example of my KT media page. Yes. All right, so my page might have like a empty container component or whatever have been established in the structure. Say it had, I don\'t know, like a.

**Mayte Eme** 1:16:42
Mm.

**Daniela Tea** 1:16:44
Like a I\'m trying to think like a text component. Oops. So you added a text component for a reason. It\'s there, but it\'s empty because in the structure you\'re not setting initial content. Does that make sense?

**Edwin Aquino** 1:16:55
Got it. So it\'ll the the the structure will be there and then you can always change it and add whatever you need to afterward. It\'s it\'s just adding that portion there for you. But if you wanted the actual content, that\'s when you would do the initial content.

**Daniela Tea** 1:17:04
Yes, so.
You you would do the initial content so that if if you wanted every page that creates a template to have that right. So like as we as we saw for what\'s it called the news page template, it will always display that banner because that was set the initial content level. However when I create a news page.
I\'m going to do that here. Let\'s see that in practice. I think it\'s news page.
Oops, let\'s do this. So my initial content that appears, this appears, right? I didn\'t set it, but that\'s because initial content was set. However, I still have the opportunity to change it out, right? So what I what I heard you say, Maite, is say you wanted to add.
If you had a a like you know, say a title field or a text field. I\'m just using random components. You would set that structure level that would still that would appear on my page, but it\'s empty. You didn\'t set any content on it. So at a page level you would then have to configure it per page.

**Mayte Eme** 1:18:11
OK, OK, so it\'s not gonna show the page life is not gonna have this blank gap or OK.

**Daniela Tea** 1:18:17
Oh, right. So it it shouldn\'t take up like space if it\'s empty, right? Yeah.

**Mayte Eme** 1:18:23
OK, OK.

**Edwin Aquino** 1:18:24
OK, and Danielle, a question. This may sound a little confusing. Are we allowed to have a template of a template? So for example, you\'ll have a template that pulls in the structure. You have one template for the structure and then you have sub templates.

**Daniela Tea** 1:18:27
Yes.
Somewhere with some movements.

**Edwin Aquino** 1:18:39
Based on the initial content. So let\'s go back to like the news example. We have that, we have that initial structure set up for the news, but we have, you know, six different casino properties that have different things pointing to different experience fragments as their initial content. Is there some kind of like?

**Daniela Tea** 1:18:42
OK.
OK.

**Edwin Aquino** 1:18:56
Where we can have that set up.

**Daniela Tea** 1:18:57
OK, so one when you create. So when you create a new template you can see here I\'m able to see what templates I can build against, right? So like open page which was that open page template that we saw was created specifically for this project.

**Edwin Aquino** 1:19:10
OK.

**Daniela Tea** 1:19:15
What you\'re asking is if I were to click this and I were to. By the way, I\'m going to delete these from the stage environment later, don\'t worry.

**Edwin Aquino** 1:19:16
OK.

**Daniela Tea** 1:19:25
You\'re asking if you could set initial content separately on here, so that way it you can reuse it over and over again. OK.

**Edwin Aquino** 1:19:38
Yeah, basically.

**Daniela Tea** 1:19:39
I think I would want to get I would want to get back to you on like the precise answer because I think what you\'re what you\'re basically asking for is like kind of like how it\'s like shared content and then also if you were to like I\'m assuming and correct me if I\'m wrong if you were like to update the structure in one would it update the structure in.

**Edwin Aquino** 1:19:57
In all the other templates, correct?

**Daniela Tea** 1:19:57
Yeah, that\'s what. OK, yeah, I want to make sure I understood why you\'re asking that. Yeah, let me get back to you on a more exact answer for that, because I understand what you\'re. I understand what your use case is. I could totally see why you would want initial content for different sites that may use a similar structure. OK.

**Andy Lambert** 1:20:04
Yes.
Hey Danielle, I would say that the the short answer is yes, there\'s definitely a path to do it. What we what I would want to do is go and figure out like what the happiest slash best practice path is. There\'s several, well, there\'s several ways to go about it, so.

**Daniela Tea** 1:20:15
Yeah.
Yeah.
Yeah, that that\'s exactly what I\'m I\'m. I want to make sure I can explain it. But yeah, the short answer is yes, but I want to make sure I explained it properly to you, Edwin. So let me get back to you on that one.

**Andy Lambert** 1:20:31
Yeah.

**Edwin Aquino** 1:20:40
Yeah, \'cause that\'s a that\'s a important thing. Like if we have so many different newsrooms, which each of them have their own specific experience fragment, we definitely wanna make sure that\'s easier on the author to easily just pull in that template and be ready to go with whatever content they need rather than having to.

**Daniela Tea** 1:20:48
Mhm.

**Edwin Aquino** 1:20:56
You know, switch each and next every experience fragment, yeah.

**Daniela Tea** 1:20:57
Yeah.
Yeah, understood. Yeah, no, great question. So we\'ll work on getting back to you on that one. Let\'s see. So I\'m gonna pull back up the agenda again.
OK, so oh error page, let me show you guys. So we we kind of talked, you know we talked about like the custom templates, what blank page would be used for. This is another quote UN quote custom template. You can see 2 pages, right? 2 pages right now on stage are using it. Right now we have.
We have the Hard Rock page for careers I believe is using this. So if I were to take a look at what it is, my errors section, my 404 page in the error section is using this template.
So you can see what the page looks like.
There\'s really not, you know, too much difference from like the open page that we saw. However, if we were to take a look at the structure, one thing it does have that we saw other sites like the open page did not have is a site map template is is here in this specific template.
Right so the site map component is here. If I were to click on initial content right now the site map is not actually pointing anything because I think this page is actually this page is is still in progress since it\'s.
For the career site, but that\'s the reason why there isn\'t our template to make sure that the site map was available as part of the structure. So if I were to create a new page right now using that errors template.
We could see I have in my sections.
No, it didn\'t show up. We can see I have in my sections, my containers, my site map is not here because I believe the site map. OK, yeah, so root path of site map. So this here I think we\'re still this one must still be working.
This here the expectation is if initial content had been set for the site map, like say we had set the site map to use to point to a specific section, then that would display here within my KT errors page. I\'m going to take a look at this 404 one.
Mhm.
So here we\'ve added quite a bit of content for this page. Believe the site map is something that you guys are using on the hardrock.com site.
Yeah, so this is essentially the section that appears within error pages. I\'m going to go actually to prod so we can take a better look at this.
I\'m going to go to the prod error templates.
So error page. So I\'m selecting this. Actually we\'re going to see how many pages are referencing it.
OK, so no pages right now are referencing it. However, OK, this must be a new template that we created and we can we can use it moving forward. But let\'s see here. So yeah, no pages currently are using it. What we probably did for this page is use an open page template.
But the intention of the error page though is as you saw before, there\'s a section for site map which is not present on the open page template. So that way anytime you create an open, create a site map, create an error page.
For a new site, it would always have that site map component. So here\'s our open template. You\'ll see it had the hero banner established as initial content, the breadcrumb as initial content within those within this section of the page.
So I think hopefully you guys can kind of see how the page templates right now are pretty broad, pretty global. But like to your point, Edwin, we understand though that you guys are probably going to need to set up some specifics for like say a line of business or even specific sites.
Within those lines of businesses. So while we have established some, you know, quite quite open templates for you guys to start with understanding like what exact fields you guys need to display to the author, what initial content needs to be displayed based off of the site that you\'re on, that\'s going to certainly be things that I would.
Imagine that that the team would need to really kind of map out. So that way again, this is all for the ease of authoring and making sure that things are uniform and gives the author the right guardrails for them to be creating pages moving forward.
So hopefully you guys now understand more about like the different templates that have been available. We\'re going to go over the messy burger and the microsite template. I think Monday is our next session, yeah.
So we\'re going to go over that because I want to show like actual examples, including the initial content, how it is when I create the page, but then also a finished example of it and my plan for next week is also to go over.
Just gonna click here some additional navigation and data displays. So we talked about the alert aggregator component that\'s present as part of the structure on the templates. We haven\'t actually seen the example, so we\'ll go over how that works.
As well as things like breadcrumb, the list, the site map, the drop down, language selector, sub NAV, micro site navigation and page template like I mentioned before, content carousel. So there\'s some additional components that I think I might add to the section, so I\'m going to take a look.
But we have three more sessions next week and ideally we\'ll be able to have covered all the ticket items that were identified and listed in the SOW. And then on Thursday we are beginning the technical knowledge transfer.
With Andy, who will be going over things such as release management and development processes, best practices when it comes to AM development, that sort of stuff. So wanted to see though if there\'s questions about what we\'re going to be covering.
Or anything else you guys wanted to share about today?

**Edwin Aquino** 1:27:47
Yeah, Daniela, I have one more question. When it comes to the templates, is there any way we can limit specific templates based on the location in the tree in the in the structure? So let\'s say if we\'re under cafe, it\'ll only show these specific templates. Is this something an admin can also set up?

**Daniela Tea** 1:28:02
Hmm, I do believe you should be able to restrict it, Andy. I don\'t know if you\'re listening or not, but I believe that would that would have to that would be set up by the admin as well as like some like permission and user groups that et cetera, et cetera.

**Andy Lambert** 1:28:15
What happened? What\'s the question? I\'m sorry, I was not paying attention.

**Daniela Tea** 1:28:17
No problem. That\'s why I said your name. Question is about how how do you restrict a template? And correct me if I\'m wrong, Aaron, how to restrict a template to only be used in certain parts of the site? Is that correct?

**Edwin Aquino** 1:28:30
Correct. Yeah.

**Andy Lambert** 1:28:31
Yeah, absolutely. Yeah, absolutely. Yeah, you can definitely do that.

**Daniela Tea** 1:28:34
But that yes, so that\'s. But again, Edward, that\'s not gonna be like you as a content author wouldn\'t be able to establish that. Wanna make sure it\'s clear.

**Edwin Aquino** 1:28:35
OK.

**Andy Lambert** 1:28:39
No.
Yeah, it\'s a policy setting. So I would be like a super author that has privileges, you know, basically a a permissioned user and would be able to do it.

**Edwin Aquino** 1:28:42
OK. Yeah.

**Daniela Tea** 1:28:51
Mhm.

**Edwin Aquino** 1:28:51
And it\'s, it\'s sort of ties in with my question earlier about like the templates of a template. That way we have, you know, we have let\'s say a property specific templates for Bristol, right? We would have their templates under their. So whenever we get a quick land page under their section of the site, it\'ll only show those templates for them rather than all of these other templates that we have.

**Daniela Tea** 1:29:02
Mhm.

**Edwin Aquino** 1:29:12
Here, that\'s the idea behind that.

**Daniela Tea** 1:29:12
Yeah, I think, yeah, understood. So like anything that is established as global as well as anything specific to Bristol is what you\'re looking for when you are in the Bristol section. OK, yeah, yeah, I think I do know that one of Andy\'s topics is gonna be about things like permissions and user groups and things and.

**Edwin Aquino** 1:29:20
Exactly.
Exactly.

**Daniela Tea** 1:29:31
So hopefully we\'ll be able to dive a little bit a little bit deeper into that. But my plan is also everyone for the question you had previously about template within a template. I do want to try to gather some information and get back to you on that and then also maybe some other details about how to accomplish what you just asked as well.
O hoefully we can cover some of that next week and then additional actual technical details within the technical knowledge transfer.

**Edwin Aquino** 1:29:49
Alright, probably.
Perfect. Thank you, Daniela.

**Daniela Tea** 1:29:58
Thank you. Yeah, go ahead, Magic.

**Mayte Eme** 1:29:59
One question, I don\'t know if this was asked. Can we change templates? Like if page A is using template one, can we just change it to template 2 and apply it?

**Daniela Tea** 1:30:12
You\'re talking about like an existing page that\'s like published. So I I do not think you\'re able to do that. Like you\'re basically saying I want this page to be converted into another page.

**Mayte Eme** 1:30:16
Yeah.

**Daniela Tea** 1:30:28
Maybe it has a similar structure, but I think the The thing is it wouldn\'t. You are not able to do that as an author. You\'re not able to do that at all.

**Mayte Eme** 1:30:36
Oh, OK. We\'ll just write it down. Thank you.

**Daniela Tea** 1:30:41
However, I guess my question though might say is if you can give me an example like a like I guess like an example of like what you are expecting or hoping for. I can perhaps give a slightly better answer like a more detailed answer.

**Mayte Eme** 1:30:55
We have come up with new templates based on whatever needs, right? And then we see, oh, this template can actually fit this existing page or we do a whole revamp, not just an enhancement of existing template because we want to leave it like that. We need another variation. So a new page that gets created and we want to apply it to existing pages.
Without replacing. So it\'s not like replacing the existing, it\'s an additional temper that gets created.

**Daniela Tea** 1:31:20
OK.

**Mayte Eme** 1:31:26
Yeah.
Yeah.
Yeah.

**Daniela Tea** 1:31:41
OK, um, yeah, I.
Andy, if you\'re listening, we might need to take this one offline. Right now there would be no way to do that from like a content authoring point of view. I\'m not sure if like programmatically from the back end side of things, perhaps that could be done, but yeah.

**Andy Lambert** 1:31:57
Do you? Do you what, Danielle? You busted me again.

**Daniela Tea** 1:32:00
I know converting a page from 1 template to another.

**Andy Lambert** 1:32:06
No, it\'s not not a not a happy path for sure.

**Daniela Tea** 1:32:10
Yeah, that\'s that\'s exactly it. But but my day, let me, let me do a little bit of thought, try to gather some information. I\'ll write that down and and see if I can provide a better answer to you on Monday, OK.

**Mayte Eme** 1:32:21
OK, and another last last thing that that made me think about is can we have different template versions for different languages?

**Daniela Tea** 1:32:26
Mhm.
Different as in like this open page like would would the structure be different or just the content or?

**Mayte Eme** 1:32:35
So but then one let\'s say.
The structure. So content is easy because I know we can localize per language, but we\'re actually looking at the Japan site right now and we\'ve been in discussions under the templates that we have. It\'s the same content, but in a different way because it\'s a completely different culture. They read differently, not to mention right to left or up and down, whatever that is.

**Daniela Tea** 1:32:45
Mhm.

**Mayte Eme** 1:32:59
So it\'s kind of like the same content, but in a different template structure, if that makes sense.

**Daniela Tea** 1:32:59
Mhm.
Oh.
Yeah, I\'m.

**Andy Lambert** 1:33:07
I\'m saying similar with with other projects and customers. Um, so don\'t quote me on this, but I believe that there there there is a.

**Mayte Eme** 1:33:15
OK.

**Andy Lambert** 1:33:21
I don\'t know if it\'s happy, but it\'s not unhappy path. There is a way to do it with. Yeah, yeah.

**Daniela Tea** 1:33:24
Neutral path.

**Mayte Eme** 1:33:29
OK.

**Daniela Tea** 1:33:30
OK, it.

**Andy Lambert** 1:33:30
But I\'ve seen so I\'d like I said I\'ve seen something that I remember seeing something that smelled a lot like that and I so that\'s something we could definitely look into and talk about like like look at the what you\'re describing like probably during gap analysis and then and be like OK hone in on.

**Daniela Tea** 1:33:43
Yeah.

**Mayte Eme** 1:33:43
Mm.

**Andy Lambert** 1:33:47
Yeah. Is that exactly the right solution for that? Like different templates or is there another way to go about it that would be a happier, you know, I don\'t know, but but yeah.

**Mayte Eme** 1:33:53
Mm.

**Daniela Tea** 1:33:59
Yeah, I was, I was about to say, might say like from like the initial like what you just described, I think I would definitely want to learn a little bit more because you know to Andy\'s point, can you do it versus should you do it like you know, like is that the best way to handle what you\'re describing? I think we we would.

**Mayte Eme** 1:34:06
Mhm.

**Daniela Tea** 1:34:17
Want to make sure we understood fully before we prescribe something, but we can certainly do a little bit of research offline based off what we did hear you say. And if we, you know, can provide more information, we\'ll certainly do that sometime next week when we reconvene.

**Mayte Eme** 1:34:32
Yeah, no, I agree. I don\'t. I don\'t know what\'s the right way to do it. It just, you know, trigger something in my mind. So I\'ll add it to the list and when we get to it, you guys can advise what\'s the, you know, best, best approach for that.

**Daniela Tea** 1:34:36
Right.
Yeah, that sounds, that sounds good. My team will certainly ask additional follow-up questions to really pinpoint exactly like what you\'re looking for. OK. All right guys, well, if you guys have any other questions about templates, we I will try to.

**Mayte Eme** 1:34:50
Mhm.

**Daniela Tea** 1:35:01
Get up some follow up information on Monday based off of what we discussed today. But yeah, look forward to look forward to covering navigations data displays I think next Monday and then I will be also posting some additional agendas for Tuesday and Wednesday to essentially cover the remaining items.
Cards is a huge topic, so one of the sessions is probably going to be dedicated all to cards, so look forward to that one as well. But if there\'s nothing else, guys, I think we can end the session for today and I hope everyone has a great afternoon.

**Edwin Aquino** 1:35:39
Thank you, Daniela.

**Lucas Nelson** 1:35:40
Thanks, Daniella. Thank you. Thank you. Bye.

**Daniela Tea** 1:35:40
Great. Thank you guys very much. Bye everyone.

1:35:41
Thank you.

**Carlos Aldana** 1:35:42
Thank you, Sonia. Thank you.

Scott Sorel** stopped transcription