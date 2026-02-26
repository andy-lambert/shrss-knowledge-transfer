**SHRSS Adobe Knowledge Transfer-20260225_130204-Meeting Recording**

February 25, 2026, 1:00PM

1h 34m 37s

Daniela Tea** started transcription

**Daniela Tea** 0:07
Alright, good afternoon everybody. So today we are going to be covering some media related items, so some components such as the media gallery, the image gallery grid and then also reviewing some things that I know that the team is already familiar with like the hero band.
Or the Hear A Carousel. But before we get started with that, I did want to provide an update for an item from yesterday and Gonzale, I see her on the call and I was hoping perhaps if you could share your screen and if we can open up the prod environment, I would just like you to navigate.
To the Google Map component, just to confirm and see if you\'re able to view the dropdown options that you weren\'t able to see yesterday.

**Gonzalo Calasich (SHRSS)** 0:57
Hi, uh, sure. Let me give me a minute so I can go to Prague and I\'m gonna share.

**Daniela Tea** 1:04
Yeah, sure thing. Thank you. And yeah, and if Lisa, I don\'t see Lisa on right now, but I would also if when she\'s joined, I would also like to confirm that she can see it as well. And then if all is good, I can explain what\'s going on and and what the fix is.

**Gonzalo Calasich (SHRSS)** 1:24
Thank you. OK, let me share my screen.

**Daniela Tea** 1:28
Yes.

**Gonzalo Calasich (SHRSS)** 1:39
Can you guys see my screen now?

**Daniela Tea** 1:40
Yes, I can see it. I see you in the prod environment and you\'re navigating to. We need to go to the locations page.
And just to confirm, this is the island browser, is that correct?

**Gonzalo Calasich (SHRSS)** 1:56
Yeah, this is correct.

**Daniela Tea** 1:57
OK, cool.

**Gonzalo Calasich (SHRSS)** 2:00
So this is loading.
There you are.
OK, sweet. Now I can see them.

**Daniela Tea** 2:40
OK, perfect. Hang on, let me just admit some people are also still joining the room. Awesome. Just wanted to confirm you can see that. So thanks for showing that Gonzalo. I can check separately with with Lisa on that, but I\'m gonna go ahead and take over screen share to show how we resolve that, what the issue is.
OK, so I\'m sharing my screen and I\'m in the prod environment and the field that you\'re interacting with that locations drop down, that\'s actually something that\'s coming in from what\'s called a generic list.

**Gonzalo Calasich (SHRSS)** 3:00
OK.

**Daniela Tea** 3:16
And that generic list is we have one called regions and that\'s populating that specific drop down. I\'m just going to hit property so you can see. So these are the values. These values are the same ones that you saw within that drop down. Now the reason why you were not able to see it yesterday, but I was is because.
Yeah, the user groups that have been set for you, we took a look at user groups that you were in that did not have read access to this list. That\'s why you weren\'t able to see the values. So we specifically added you to. We saw you\'re part of this group called Template Authors.
So that group has been provided access for read privileges. We understand that there are probably some additional groups that need that, but this is all related to user groups, permissions, understanding who should view them versus who should write them, etcetera. That is a topic that we are covering within knowledge.
Transfer starting next week with the technical side of things with Andy running that. So that\'s the reason why you were having issues seeing it. Same thing with Lisa, but in order to make sure that the proper people are seeing it and the proper people are able to actually like edit this, say add an additional value.
Or change a value or a title on here. That\'s where we would need to understand what those user groups are that need privileges for this. So hopefully that\'s clear to the team. This was a permissions issues, but that\'s how it gets resolved is making sure that your groups, the groups that you\'re in, have access to this.

**Gonzalo Calasich (SHRSS)** 4:52
Thank you. But still I still have a question. I still see the North America being on the last on production is that we need to publish the page again or do something in order to show up on the top because of the components on the top.

**Daniela Tea** 4:56
Mhm.
Yes.
Right. So yeah, so this particular issue was specifically for the dropdown. I think you haven\'t published the page in like a month or so. Definitely if you were to view as published and you can confirm to see what the order is before you publish, then perhaps you know.

**Gonzalo Calasich (SHRSS)** 5:19
Got it.

**Daniela Tea** 5:28
Then you can go ahead and publish the page, but I would recommend you viewing the ages published, making sure it\'s in the right order, and then publishing it again.

**Gonzalo Calasich (SHRSS)** 5:37
OK, let me let me do that right away and you can continue. I will let you know if if.

**Daniela Tea** 5:40
OK.
Yeah, if you want to post in the chat too. And Andy, if you could just take a look at that and perhaps we can, we can discuss that after if that\'s good. Gonzalo, OK.

**Gonzalo Calasich (SHRSS)** 5:49
Yeah.
Yeah, we can discuss. Thank you.

**Andy Lambert** 5:52
Sounds good.

**Daniela Tea** 5:53
Alright, awesome. Thank you guys. OK, I\'m going to go ahead and close out on some of these tabs since I do not want to be messing around in the prod environment right now. So let me close out of a couple tabs and now we are going to.
Pull up the agenda so you can take a look at what we have covered or plan on covering today. So to be transparent with you all, there are a couple items I believe that we will not fully cover today just because there\'s quite a few pieces of functionality that I would like to break out into.
Different sessions, so that including the container component. So there\'s other elements with the container component I would like to cover on a different day, but we are going to cover some items within the container, things that relate to actual media, but when it comes to say like the container best practices.
Sizing using layout mode, that sort of stuff. I think that that would be best handled in a separate sessions, so I want to keep this kind of focused on specific media items. So let\'s go ahead and get started. I would like to focus on 2.
Components here that I know that the team hasn\'t necessarily used on the main Hard Rock website, and that\'s the media gallery and the image gallery grid. I believe that the team should have experience with the other components, so I would like to focus on these two first.
So let\'s get started with the media gallery. I\'m going to show an example of a page that has a media gallery, as well as how the functionality currently works, and then we\'ll break it down with the configuration of this.
So when we say media gallery, we\'re referring to this section right here. You can see that there are 4 images being displayed right now to the end user. When I select an image and I click on it, it opens up in this light box view. I\'m able to cycle through additional images.
And I\'m able to exit this out and get taken back to the page. So configuration wise this media gallery component. Yes, this is a global component as in every page can use it, but we haven\'t seen on hardrock.com. But right now I\'m pulling up an example from the hotel\'s website.
When I configure this specific component, I\'m able to add different types of media. So in this case this specific gallery was using images and so you can see images has been selected for everything that\'s here.
But you are able to also have videos be displayed here so we can take a look at actually authoring one and seeing how how that would be done. So when you add an image, you would select the image from the DAM. You would also include the alt text, a caption and a title.
On here, and that\'s the caption and the title are things that can be displayed on the image or visible on the light box view of the image. In this case here, there\'s no caption or title, so that\'s why we didn\'t see anything. But we\'re going to again, I\'m going to be authoring a new one on the KT on my KT Media page.
So just like any multi field, you\'re able to add multiple. You\'re also able to change the order of the items and how you want them to be displayed. So you can see right here there are four images showing, but I actually have one to.
345 S That\'s why there are some arrows indicating that I can go to extend and see the additional images that are not visible in this view.
When I click on others, this tab allows me to select the aspect ratio that I want for the images that I\'ve I\'ve included. So I have the ability for desktop, tablet and mobile. You can see here for number of desktop tiles it\'s been set to four. That\'s why any image past four is not going to be visible.
Table on the screen upon load. Tablet tiles has been set to three, number of mobile tiles set to two. So when it\'s viewed on the different devices, you\'re not going to see all four. You\'re going to see whatever\'s been configured here. You also have the ability to display the indicator dots.
To the end user or hide them. In this case this is not being displayed currently and then you also have the ability to loop the carousel so that way you can just cycle through without any without like an end point for the carousel itself.
So I\'m going to now go on to a new media gallery and we\'re going to author one and then play around with some of these options to see how that affects what it looks like to the end user. So let me get my page up here.
And I\'m going to just add a media gallery component.
All right. And just for just to put a separate spacer in between here so it\'s not butting up against the other element I have here. Now let\'s configure it. Yep.

**Andy Lambert** 11:09
Hey, Daniella, real quick, Gonzalo or Danielle, can you just paste the link to that page in production so I can take a look at it?

**Daniela Tea** 11:17
Which page?

**Andy Lambert** 11:18
The one that was having the the issue with North America showing up left.

**Daniela Tea** 11:20
Oh.
Yeah, Gonzalez, that\'s something you can send from the Hard Rock website, please.

**Gonzalo Calasich (SHRSS)** 11:27
Right away. Thank you.

**Daniela Tea** 11:28
Thank you. Thank you, Andy. Thank you, Andy. And thank you, Gonzalo. All right, so for my media gallery component, we\'ll also go over the vertical variation and how that works. Here\'s my media section where I\'m able to add specific items.

**Andy Lambert** 11:28
Thank you. Oh, he got it. He\'s on it. Thanks.

**Daniela Tea** 11:46
So I\'m just going to add some images for right now. I actually had my little training folder set up, so I\'m just going to use that for the time being. So I\'m selecting which folder in the dam where I want my sidebar to focus on and filter.
So I\'m just going to do this and hit select and so now my you can see my sidebar only has assets that are from my little trading folder. So this is just for me to make it easy and ensure I\'m using images that I uploaded earlier. All right, so I\'m dragging my images. I\'m putting my alt text.
Is alt text. This is the image caption. This is the image title. All right, so putting this here so it\'s very clear when it\'s displayed where those values are being displayed. Just gonna add a couple more images in this case.
Alright, just doing this and I\'m going to add two more.
Right.
OK, so that\'s been set for the images itself. By default, if I click on others, I can see that the aspect ratios are automatically set to 3/4. I also have the ability to do one for one, which makes it more of a square or 9:16 so.
We can certainly mess around with these and see what that looks like to the end user. For my number of desktop tiles, I\'m just going to set it say to four for tablet tiles, maybe three and then maybe two. And let\'s turn on carousel dots and carousel loop and I\'m going to hit done.
OK, all right, so preview. OK, so here we can see how the image caption is displayed on on top of the image. Let\'s view this as published.
OK, and let\'s take a look at what happens when I click on the image itself. You can see that the title is is what\'s being displayed when you view it within the light box. The other ones and I didn\'t put a title, nothing is displayed there. So just something to consider. Image title maps to this portion here and the image captions.
Is what\'s being displayed underneath the image. So since I only put one underneath, that\'s why this does look a little wonky. If I were to add captions for all, I\'m just going to do this.
So we can see now that everything is aligned because it\'s taking into consideration the image caption underneath the image. All right, so let\'s go back here and now that we see how it looks, let\'s change the aspect ratio.
Of say the to one to one. See how that affects it. So you can see how when I did that it changes what the ratio is. It\'s more of a a square instead of what it was before. And then the last option of course is the 916. I\'m gonna hit done.
And so this one is taller and a little skinnier. So depending on how you need the media gallery to display your images, couple of options with regards to changing the aspect ratio which is present on the others tab you might consider you know you might need separate aspect ratios for each one, so certainly have.
The ability to do that here. Let\'s take a look in tablet.
And mobile. So I had set. Actually I think I would have to do it as view as published and let\'s do this.
OK, so you can see how it went from 4:00 to 3:00. This is the tablet mode and then from 3:00 to 2:00 because I\'d set 2 for mobile. So this is just my way of being able to control how much I want.
The images, how many images I want to be displayed to the user as well as what aspect ratio I want for the for the user. Let me go back here.
OK, all right. So with the media gallery though, there is also a another variation. It\'s called the vertical variation. I\'m going to just check that and hit done and we can see what happens.
Um, so right now, one second.
Changes the view. Sorry, I\'m just viewing as published. It changes the view. This is a little I typically these are going to be, I believe we see them with a background container. So let me go ahead and set that up very quickly.
I\'m going to just add a container here.
With a background color, so it\'s not necessarily white.
Mhm.
Yeah.
OK.
It\'s fine.
All right, and I\'m going to cut this and then paste it here in the container.
Alright, and then I am preview it.
OK, alright, so I just wanted to show it so it\'s on a white background so you understood like the borders. I can see this looks a little off. Let me do a quick check.
I do have another version which doesn\'t seem to have it look like that, but let\'s take a quick look here. I\'m gonna add one more image.
You guys can see as I\'m adding images what happens. There\'s some indicators here that wasn\'t necessarily visible on the white background. So I think that\'s something you just want to call out. As I\'m cycling through, you can see that this is the main image and it shows.
The image to the right. It also displays the caption on top of the image when you have the vertical variation set. So it\'s basically it\'s the exact same media gallery component, but just determining which view that you want it to be, whether it\'s in vertical.
View or whether it\'s in horizontal view, you would just configure it once and then just select how you want the images to be displayed.
And as I click on the style variations, I also have a couple of ways to be able to say I want to have the media gallery. Yeah, so I want the media gallery with caption on image top. So previously I had it with the captions underneath. If I don\'t have that style variation set like you saw.
Before it would be underneath the image. I do have the ability to display it on top of the image if I wanted that. Let\'s see primary without indicator. I also have the ability to just not have the carousel indicators appearing underneath.
And then so the default. This is what the default looks like, where you have the arrows to the left and the right and the carousel indicators underneath. No caption unless you actually display that on here.
OK.
I will pause and yes, Rick, I see your head up.

Lyon, Rick (Director of Digital Experience)** 19:32
Sorry, I thought I had to unmute. It\'s more of like a a visual kind of notice of something that the two dots don\'t appear to be centered underneath the images. It\'s like they\'re on the left side of the center.

**Daniela Tea** 19:43
Mm.
I see. Uh, yeah, one second. Let\'s see.

Lyon, Rick (Director of Digital Experience)** 19:48
This must be like a third or fourth shot. Maybe that\'s just not rendering or just.

**Daniela Tea** 19:52
Let\'s jump.
So first I\'m going to set this to full width and then if I don\'t want this to be full width, I\'m just going to add another container in here. This container is being set to content area I\'m just seeing.
Happens when we put it with a content area. OK, yeah, no, I understand what you\'re saying. The believe how many images are here. OK, so there\'s five images total. So it\'s showing two. OK, all right.
Yeah, no, I noted on that one, Rick. Looks like that might be something checking, just checking the.
Aspect ratios as well. Wondering if that\'s.
OK.
OK, yeah, no noted on this one. This is something that would likely have to be updated to center a line on those specific carousel dots. So that would be something we would of course want to make sure is captured.

21:03
OK.

**Daniela Tea** 21:04
Um, any questions? Yeah.

Lyon, Rick (Director of Digital Experience)** 21:06
And then the how many images were there \'cause you got two dots, but.

**Daniela Tea** 21:10
Yes, I have 5 images total, so when I click next and it shifts over.

Lyon, Rick (Director of Digital Experience)** 21:13
So it just goes to like the other section versus the other thumbnail, I guess. OK.

**Daniela Tea** 21:19
Yes.
Yeah, mm-hmm.

Lyon, Rick (Director of Digital Experience)** 21:24
Thank you.

**Daniela Tea** 21:25
Yeah. Anybody else on the call? Any questions about this media gallery component?
We can go ahead and add a video. Actually, let\'s do that.
And.
So for Vimeo, let me get I was working with another Vimeo video that had an ID and I can actually copy that over one second.
No, not that.
Yeah, I was just going to get this one.
All right.
And then because of course the video is since this is is going to show images, that\'s why you would choose a specific thumbnail versus just the video itself. I am going to hit done.
Pull up my folder again, but we can actually take a look to see how that is. Right now you can see this is not going to show anything because I didn\'t put my video thumbnail, but this is the square that\'s representing it. So I\'m going to add the image now for my video thumbnail.
Let\'s just choose this.
Done.
Right, so I can see this and if I were to click on it.
One second \'cause it sorry I was blaring out of my ears. If I were to, as you can see, I click on it just like the same with the images. It does open it up in that light box. You notice I\'m in the author though, so let me show you really quickly the.
View if you were viewing it as published.
So it\'s again, it\'s just the same as the images, but the video is just within this middle window.
All right.
OK, um, anything else for this media gallery component?
All right. OK.
OK, let\'s move on then to the image gallery grid. I believe this is something also I don\'t think is currently being used on the hardrock.com website. It\'s typically right now from what I saw in AEM, it\'s being used on the hotel pages.
But let\'s take a look at how this is set up and what you might want to use this for. So the image gallery grid. You can see I set up something here just to show some items from my little trading path and.
Configuring this, what I did was I selected what image folder I wanted my gallery to contain, so I\'m pointing it to one image folder here and then I\'m also selecting what tags that are on these images do I want to pull into this component and display.
Finally, I\'m also selecting how many images do I want to display within this component. Because keep in mind you know if you have say a folder that has like 200 images and if those 200 images are all tagged.
You can certainly display all 200 or you can say OK after maybe like 20. I don\'t want to display those because the page is going to get too long with those. So that\'s this is a configurable field, but by default and I\'ll hover over this by default the.
Number of images is 50 when you first configure the component. I\'m just going to put 50 back because this is what it was before. So when it comes to the tags, what this is saying is OK, I want everything that has all photos like A tag called all photos applied to it or I want everything that has recreational.
Activities applied to it. The tags that I select here are going to be displayed on top of the image gallery grid to serve as essentially like tabs. So if I were to.
View this and I\'m just refreshing my section here. All photos currently is selected. If I click on recreational activities, it\'s only going to show me anything that has recreational activities tagged to this specific folder.
So how do we, you know, make sure that we\'re showing everything that we need in here? What if we choose tags that don\'t have any any photos associated with it? Let\'s go ahead and show how that works and what would happen. What\'s the behavior?
So clicking on my tags, it defaults to where those SHRSS tags are located. In this case, I\'m just going to go to the location where I knew most of these tags were being used. So for me it was hotel and gallery. Of course, if they\'re the tags are located somewhere else, whatever.
Images that you were using, you would go there, but I know for a fact I did not tag anything in my folder with rooms and suites. I\'m going to select that, hit select and I\'m going to hit done. So you\'ll notice that still appears as a tab.
I hit preview, I hit it and there\'s nothing that appears underneath because while I\'ve selected the tag to serve as part of the navigation, it doesn\'t actually have any specific images. As I start adding images with that tag, then it would automatically appear here. However, if you do not have images that are.
Are tagged with what you selected. You will not see anything, but you will see it in the navigation. So what I\'m going to do right now is I\'m going to add a couple more images to my grid in the dam by tagging them with certain tags and then we\'re going to see how they would appear.
Within this grid, so let\'s navigate on over to the dam. Let\'s go view an admin, just navigate to assets and files.
HR My little folder is called training. My little images folder is here.
Now say I want things to appear under my rooms and suites tag. So what I can do if I know exactly what images I\'m going to use, I\'m just going to select a couple and I am going to click on properties.
And I\'m going to see my asset metadata view. I\'m just going to go to tags.
And I\'m going to select that specific. Oops, sorry, I\'m going to select that specific tag of rooms and suites.
And then I am going to hit save and close and you\'re going to see this little drop down that says append mode. What that means is that if you when you select append mode, it\'s going to add this tag to these four images.
In addition to whatever tags are already there, it\'s going to keep. If say this image had four tags already associated with it by clicking the pen mode, that means OK, I\'m just going to add this tag in addition to those four for this image. If you do not select that, what it will do is it will replace the tags that are associated.
With these images. So if news one had four tags on there and I did not select the pen mode, this will now replace whatever tags were previously on news one. So something to keep in mind and be very aware of if you want to just simply add the tags to the images in addition to whatever tags are either, you want to make sure pen mode is.
Selected. All right, going to hit submit.
And I am going to come back here and hit refresh and hit preview. When we check rooms and suites, we can see that there are now 4 images that were there that were not previously there because these are the ones that I applied the tag to.
However, keeping in mind and I think let\'s see if this was there, the all photos tag is something that you if you want, if you want this specific view where you\'re seeing every single photo, I want to be clear that this is not the total of all the photos.
That are present on these other tabs. This is itself A tag and in order to be able to see all your photos, you\'d want to make sure that the tags that you\'re adding include all photos to it. So when I was adding my, I\'m just going to select some random ones.
Ones when I was adding my tag for rooms and suites. What I should have done is also added the all photos tag as well. OK, one second. All right, let me select that again.
Properties. All right, so we\'re going to add, do that again.
I\'m adding my rooms and suites and then also you\'ll see there\'s A tag called all photos. So by selecting this, this will mean that it would appear in that all photos tab at the beginning. Select it.
Same close, append mode, submit.
Ulling back refresh.
I should now see more photos. Yeah, so like I had added, I think I added. I added some more here. So all photos now contains the other ones that are in rooms and suites here because each of these individual photos.
Should have two tags, essentially rooms and suites and all photos added to it if you want it to appear on this tab and this tab.
Alright, um, something to keep in mind as well is as I\'m viewing as published.
Here\'s a view of me viewing. This is published. I can see everything looks as I as I intend. If I click on this, you know it\'s going to display the title at the bottom. Since I have no title, there\'s no title being displayed.
Let\'s take a look at the configuration for that. So in terms of how this works, I believe that the image gallery for the image gallery grid dam assets, you\'d want to ensure that a title is added since that is being displayed.
Right now at the bottom, but that\'s only visible when you do view as published, just to be clear. So I would recommend as you\'re doing your configurations items, always make sure you have like that second tab open. View as published as a.
Way more accurate view as to what your end user will see versus just the preview mode. Because sometimes as you\'re working with things like modals or light boxes, it\'s not necessarily going to be completely accurate since it\'s not taking, say, like the header into consideration when displaying it back to you. So just a quick tip making sure you just.
Simply have at least two tabs open. But yeah, so to be clear where it says no titles is because a specific asset did not have a title in the metadata stored. Don, I don\'t know if you\'re on right now, but I guess I my question for you and the team would be.
If the team is is planning on adding you know all metadata fields with like say titles and captions and descriptions or or is that if that\'s something that you know is not typically added for your assets?

**Don Middlebrook** 33:29
Sorry, sorry, I was doing something else. Yeah, we\'re planning on adding as much metadata as possible. So titles.

**Daniela Tea** 33:39
Description and OK.

**Don Middlebrook** 33:40
Uh, description and all that kind of stuff. So yeah.

**Daniela Tea** 33:43
OK. Yes, OK, got it. So I think, I think that\'s just something that the team should consider. And the reason I\'m highlighting this is because you know, say if if if you guys decide, well, we don\'t necessarily always want the tile displayed here currently with the configuration it is displaying.

**Don Middlebrook** 33:44
Um.
Sorry.

**Daniela Tea** 34:02
So if that\'s something you know in the future that you guys decide, well, titles might not always make sense because maybe we don\'t have titles for every asset or you guys are still working towards that, then that would be something I would recommend capturing as something you would want to to be configured to not always display a title or whatever or if there\'s like a.
Description you want to display that would be considered an enhancement that I would recommend you guys capture for this.

**Edwin Aquino** 34:29
Question Daniela for that title text, is that an option that we can uncheck or check like where it inherits the information from the asset or \'cause I know we have an option to inherit like a alt text.

**Daniela Tea** 34:30
Um.
Yes.
Yes.
Alt text typically, right? So no, I don\'t. That\'s not currently for this specific component and I\'m going to actually go back to preview and I\'m going to refresh the page so I can get out that Moodle. So taking a look at the specific configuration for this.
It\'s more since I\'m simply selecting the image folder from the component itself, I\'m just setting where the location is and what images I want. And in terms of what metadata properties it\'s pulling in, it\'s based off of whatever was stored in the DM. But since I up uploaded these, I don\'t actually have anything associated with it.
But if I were to update this image, let me see if I can find it. Let\'s take a look at where\'s that image.
Um.
OK.

**Edwin Aquino** 35:32
So, so basically there\'s no option to select specific images. Um.
Oh.
It it would only pull it via via tag like we.

**Daniela Tea** 35:42
It would pull it in via tag. That is correct. Yes, it would pull it in based off of whatever is stored here for each specific image and if you selected these tags within that that component.

**Edwin Aquino** 35:55
Is there a way we can select variations of an image? That way it has a different title \'cause let\'s say we don\'t use the same title across different property sites.

**Daniela Tea** 36:04
Is there a way to select variations? And when you say variations, do you mean I guess can you give me like a like would would they still have the tags associated with it?

**Edwin Aquino** 36:14
Same tags, except it would just be different titles for the images, yeah.

**Daniela Tea** 36:18
Different titles. OK, so I don\'t think that would be something that\'s in place right now. What we are doing for this currently, just going to refresh this and I\'m going to it was publish.
Is whatever I have associated with that specific image. It\'s going to display that title that was based off the image that was tagged. That\'s in the location that I have, if that makes sense. So yeah, OK.

**Edwin Aquino** 36:39
OK.
Yeah, that\'s.

**Daniela Tea** 36:48
But as as you guys can see here, this was that test title I just added within the metadata properties and that\'s what\'s being displayed here. That\'s how you would control what\'s for each image was to update the metadata. OK, any other questions?
About what we\'re seeing here.
So you can also see there there\'s a slightly different view when it comes to mobile. It changes to a drop down versus tabs and then you would just select which you would want to display. Same, you know, same kind of functionality of only showing whatever specific view you selected, but instead of it.
Tabs as a drop down.
OK. All right.
Hi. All right. So those two specific items I don\'t think we had covered before since they are not on the current Hard Rock website. So hopefully that is something. Perhaps if there\'s instances where you might be able to use it, you\'ll be able to do.
That however, moving on now to some items I do believe the team should be pretty familiar with, including our hero banner as well as our hero carousel. So with our hero banner, we do have.
The ability to either select an image or a video. I don\'t think on the Hard Rock website right now there\'s there were ever any videos that were appearing in the carousel, however, for the careers website.
We are using a video, so there is a video that is going to be displayed within the hero banner so we can take a look at how that is configured. This is going to be very similar to what we saw with the video player with regards to the third party and external URL options.
For this case here we use the Vimeo third party, just plugged in the ID and then we had some items selected here, in this case enabling mute so that way it\'s not blurring out at you when you first go to it, enabling auto play so that way it\'s playing when you first load it, enabling loop so.
Never stops. We also had background mode.
Which hides the controls and then this one enable transparency. It checks this chat box to enable transparency. I was looking into this one a little bit more just to understand when I unchecked it or checked it. I believe it\'s probably not visible now because there\'s no like container it\'s full width.
But in this case here this was selected. We also have the ability to have enabled the display of unmute button. So if you want the ability for the author to unmute it, that can be added and then we have inline playback. So it says here it controls where the videos play inline or full screen.
In an HTML player on iOS. This is an iOS specific toggle, but in this case you can see this is the video we had selected the ID. We selected the aspect ratio too because if we were to remove this there are black bars that appear.
And I can show an example on a different page. I\'m going to go on over to my original page, my KT Media page.
And then just add this video here.
Here.
So let\'s see, let\'s do this.
Yeah, I didn\'t want to. I don\'t want to mess around with this on this page because I know people are using it. But if I were to put the aspect ratio, I could leave it blank, or I could, you know, change that to whatever I needed. But if I were to do that, we\'re going to see how those black lines appear.
Just going to do video and I\'m going to hit done so you can see when I did that a video component appears for the hero banner for me to then configure and I\'m going to click on 3rd party and I\'m going to choose Vimeo.
And for the video ID, I\'m just going to see what this is. I can just add it.
OK, and I\'m going to do some of these. I believe these are all the ones that were selected. Click that. So I\'m going to hit done and you\'ll see this is a video with no aspect ratio selected. There are bars on top and below and so that\'s why you are.
Able to essentially change that when I put it to around 35, that\'s when the black bars for the video are gone. So there\'s some control that you have depending on how the video is rendering to change this.
And puts back to 35. So this again, I don\'t think I\'ve seen video being used anywhere else outside of careers, but certainly it\'s an available option, including within the carousel itself.
So what I saw on the Hard Rock website was that you guys are using all hero banners. However, there is that ability to add a video if that\'s needed as one of the slides. All right, so moving on though to the hero banner when using an image.
OK, so in this case, in most use cases that I\'ve seen on the site, we\'ve been using images and I think most of the team probably is aware of how these are set up. We\'ll do a quick refresher though on our text tab. Of course we have the eyebrow.
That\'s stored here. We have our title which maps to this, and we have our description which is then displayed underneath here.
We add our CTA\'s. You can see I\'ve added three different ones and just so you can see how they would be displayed, we have our one primary one and then everything else will take that secondary style.
For the asset, I selected something from the DAM. You do have the ability to inherit that description of the asset, which is whatever would be from the DAM. Or if there\'s something specific that you need to put for alt text instead, you can do it directly on the component here.
If the image that you\'re using is just decorative, that would make sense then to not provide one and then this would be selected and here this is for lazy loading. It\'s it\'s enabled unless you check this. So if you can read this little tool tip here, when checked image will be loaded eagerly.
Regardless of if the image is currently visible by the user. So I think typically these have been marked as unchecked from what I saw on the site. And then finally our image position tab for this and when you cancel Ramon, I saw your hand up, but really quickly let me just show this in mobile.
Here in mobile, I do have the ability to hide the description as part of my style variation, so you can see hide it. I could show it if I wanted to, but since the likelihood is you probably just want to focus on the title and the buttons, that\'s something that you can adjust.
You can also adjust the text style, so if the image is very light and text be dark, you can select this header height. What that does is it takes into consideration the height that\'s coming in from the header.
Or you can toggle that off and you can see how it\'s say OK, I\'m just going to show it from the very top without respecting the sticky header.
And then also gradient on or gradient off. See how that works for size, large, medium and small. These were sizes, preset sizes that were established. Oh sorry, I I did that too fast. So you can see how this one is super large.
As I get to medium and then finally I think small is actually I can check the exact size, but typically I believe you guys have been using I think either medium or large, but changing the size is accessible here and then changing the alignment of the content.
On the actual manner itself is selected through here, whether it\'s right, center or left. But I believe most of these have been on the left-hand side. So yeah, Ramona, please go ahead.

**Ramona Harris** 45:40
I\'m just curious to know, um, for the image size, how did you know what size dimensions to choose? If we don\'t really know, we don\'t really have any standard as far as what sizes work for cards, what sizes work for banners, and so forth.

**Daniela Tea** 45:55
So in this case here I had selected. I believe this was copied over. I think I copied over this hero banner from one of the home pages. So I had selected an asset that was just from the dam. If we were to, we can certainly change this out and see, but I believe this was one of the.
Assets that you guys had uploaded at one point, like right before go live. So it was more of me just selecting a random asset.

**Ramona Harris** 46:26
So it doesn\'t have to be any specific size dimensions like any. Should any image be able to be responsive to fit in that banner area or what are our parameters as far as the sizes we would know to select from images? Like if you did not know that if you didn\'t already have that knowledge, how would you know what size image?

**Don Middlebrook** 46:27
So it.

**Daniela Tea** 46:43
Mhm.

**Ramona Harris** 46:46
To put in there for it to work.

**Daniela Tea** 46:47
Yeah, so let\'s take another random image and see what happens. So I\'m just going to take this one here and hit done so we can take a look at how that is being displayed. So this is let\'s look at desktop. Actually this page is published.
OK, so.
Hang on. Yeah, so let\'s. I\'m trying to find something that\'s like not 1600. Let\'s see. Let\'s do this 11200.
So with regards to the hero banner, um, in terms of like the style variations where we have like the large and medium, you can see as I\'m like selecting large and I\'m selecting medium, it\'s essentially like kind of.
Scaling the image down. I think we are still working on getting getting like exact specs, but as you can see like I\'m using random images and you can kind of see just how it looks on there. But I understand Ramona about the overall ask about.
Understanding exactly what specific dimensions are needed. But yeah, as as we play around with this, we can see how it looks and if it\'s something that\'s necessarily appropriate, right. So, Carlos, go ahead. Oh, sorry, go ahead, Don.

**Don Middlebrook** 48:08
Yeah, Danielle.
No, go ahead Carlos. OK, with regards to this, so last week we we talked about the if if I were to set up you know static renditions and I had multiple sizes though.

**Daniela Tea** 48:23
Mhm.

**Don Middlebrook** 48:26
And it was told to me that if whatever I create it would this would automatically know what to put there in different placements and I want to make sure that that\'s accurate that if I were to set up you know.
Let\'s say it\'s a 4K image, but we don\'t want it to be, you know, 4K on the site. We want to use a static rendition to adjust it, whatever the site, whatever these dimensions are going to be. Is that accurate that it would automatically know what to put?
In a placement, depending I guess on if it\'s desktop, mobile.
So I\'m not sure if if that makes sense what I\'m saying, but.

**Daniela Tea** 49:09
Yeah, it\'s yeah, Don, let me let me repeat what you said to make sure I understand the question. You\'re asking about if you be based off of your conversation, it sounds like I think probably during like the DM enablement sessions.

**Don Middlebrook** 49:24
Mm-hmm. Yes.

**Daniela Tea** 49:26
Oh, it was probably discussed about renditions, correct?

**Don Middlebrook** 49:29
Yes.

**Daniela Tea** 49:30
OK. And so you\'re asking if you were to set up renditions including like say a hero banner rendition, so that way an image that\'s being used in the hero banner would match whatever rendition is applied to it. You want to confirm that that is an accurate statement, is that correct?

**Don Middlebrook** 49:37
Thank you.
Right.
Yes. So if I set it up, this would automatically be up. That image would automatically be applied to this placement or this type of placement or one that\'s that.

**Andy Lambert** 49:51
Yeah.

**Daniela Tea** 50:01
Hmm.

**Andy Lambert** 50:01
Yeah, it can be configured so that it will. It will, um, use the correct condition. Yep.

**Don Middlebrook** 50:06
But it has to be configured.

**Andy Lambert** 50:10
So.

**Don Middlebrook** 50:10
So we.

**Andy Lambert** 50:11
I yeah, I think it has to be configured in the template policy, but or somewhere. But let me check. You know what? We\'ll let\'s put a pin on that. We\'ll come back to you. Let me look into it.

**Don Middlebrook** 50:21
OK. All right. Thanks.

**Andy Lambert** 50:22
I\'ll check with uh, Chris to see if I need to talk to her about that.

**Don Middlebrook** 50:27
I just want to make sure that that\'s accurate or if there\'s other work that we have to do to make it work right until we get dynamic, you know, media. If if we ever get that in place, then we\'ll scrap all of that.

**Daniela Tea** 50:32
Mhm.

**Andy Lambert** 50:36
Yeah, exactly. Yeah. Then that all that changes it because yeah, it\'ll be automatic. But for now, yes, you can definitely set it up so that renditions of the correct rendition applies to the component on the page. I just need to let me get the exact status for you.

**Don Middlebrook** 50:43
Yeah.
Yeah.
Okay. All right. Thank you.

**Daniela Tea** 50:55
And and Don, yeah, well, while Andy is getting that info and we\'ll certainly send that over to you when it\'s available. Just I just wanted to quickly understand though, are you trying to set up renditions right now for every single component? Is that is that what you\'re working on?

**Don Middlebrook** 51:01
OK.
I I\'m not trying to. I\'m just want to know what the options are for me right now to start doing this to start looking into. Once we get the right dimensions for these different placements, I can set up the renditions for those so that they\'re automatically.

**Daniela Tea** 51:11
OK.
Um.

**Don Middlebrook** 51:21
Resized and for those placements and you know.

**Daniela Tea** 51:25
Yeah, no, that that makes, that makes a lot of sense. Understood. So yeah, we\'ll wait to hear back from Andy and Chris and hopefully be able to provide a response soon. Carlos, I see your hands up. Please go ahead.

**Don Middlebrook** 51:27
S.
It.

**Carlos Aldana** 51:38
Thanks. No, I just wanted to say that I would like to see you fixing the mobile option here and also what template are you using here? Because I think that I tried to build a page using the.
Template. No the content template and I couldn\'t find the option to size the image. You know the it\'s as large, medium and small. I couldn\'t find that under that that template.

**Daniela Tea** 51:59
Mhm.
Mm.
OK, so let\'s let\'s sorry, your first question was about mobile. Let\'s let me see if I can address that one. What? Sorry, what exactly did you want to ask about mobile?

**Carlos Aldana** 52:21
Yeah.
How? How would you adjust the images? Because I I I had many different many problems just trying to to adjust different images you know.

**Daniela Tea** 52:34
OK, so I think my first question for you would be are like are you like having some difficulties with using the image position for OK?

**Carlos Aldana** 52:43
Yeah, I for example you say I was working on this one and and tried to adjust the the mobile image and and even though I tried to set up the percentage in several different ways, I I couldn\'t.
Find the the right position for the image. So I finally I I changed the image.

**Daniela Tea** 53:07
OK, I think So what I would recommend is actually let\'s let\'s see. Actually, do you have the page? I actually want to take a look at what you were working with just to make sure I understand and then I can actually adjust whatever you were doing.

**Carlos Aldana** 53:20
I.
I was working on the landing page, the the main page of the hardrock.com.

**Daniela Tea** 53:31
OK, got it. OK, I\'m gonna go to stage then.

**Carlos Aldana** 53:36
I\'m Brad, yeah.

**Daniela Tea** 53:37
I\'m proud. I\'m not gonna mess with pro right now, but I\'ll go to the stage, the stage here, make sure I understand. And to answer your second question before I get too far, you asked about.
Why weren\'t you seeing it on the specific template? So I\'m going to show you what my template was. So when you view the page here and you click on an item like this, you can see it tells you what template was used to create that page. So in the case of the page we\'re currently on, I\'m using.

**Carlos Aldana** 54:09
Yeah.

**Daniela Tea** 54:12
The open page template. So just to confirm, Carlos, when you said you created a page, did you do you know? Do you remember which one you selected?

**Carlos Aldana** 54:15
Yeah.
Yeah, it was the content template.

**Daniela Tea** 54:24
OK, it was this. OK, yeah. So this is I think something that we will be going over more in the page templates session that I have. But a quick tip for you guys is that typically what you\'re going to be creating are probably homepages, which is of course.
You know the page like the main landing page for the site that you\'re working on, the open pages, which is going to be the child pages underneath that landing page. You\'ll also likely use the events page for any events like in cafes and such.
Those news pages, just like we saw, I think on Friday when we were going over creating news articles as well as the search results page and the news homepage. And then there are a couple other items like the blank page, which might be something that you would use for say like a modal or something where.
You don\'t want the header and footer to be included and microsite page is something that was specifically created for certain hotel pages and the messy burger page is of course for that those messy burger pages that were on the cafe website.

**Carlos Aldana** 55:35
Yeah.

**Daniela Tea** 55:35
Error pages is what you would use when you create an error page and the content page. I don\'t think you guys are using this right now, so this is something I understand. If you guys don\'t want it, this could essentially be removed from the view since I believe right now all the other pages are typically going to be your open page templates, but.
We can talk a little bit more about how can you guys create new page templates in the future or modify existing templates. Like when does it make sense to do that? When does it make sense for a brand new template? When do we set initial content, the structure, etcetera?
But certainly want to make sure all that\'s covered in I think the session that we are planning to have on Monday. So again, open page template I think is probably what you\'re going to want to be using moving forward, Carlos, based off of what I understood you were saying.

**Carlos Aldana** 56:24
OK.
Thank you.

**Daniela Tea** 56:27
Yes. OK. So now going back to the homepage for the site, I know you said prod, but I\'m just going to do this here in stage. Let\'s take a look if you could describe the situation please.

**Carlos Aldana** 56:36
Yes.
It is the oh you\'re you\'re on the stage sorry. OK no it was it was it was the the image on the when you look down the mobile side I I I had that hard time just trying to.

**Daniela Tea** 56:43
So if.
Yeah, I\'m on stage. I didn\'t want to go on prom.

**Carlos Aldana** 57:02
To set up the image for that. So I ended up changing the image and I\'m playing with the different positions, but it was super difficult. That\'s why I wanted to see you. How do you solve those issues? So maybe I did.

**Daniela Tea** 57:15
OK.

**Carlos Aldana** 57:22
I didn\'t do something that maybe you do.

**Daniela Tea** 57:25
OK, so I\'m navigating to prod. I\'ll just take a quick look at the page. Hopefully I can see your changes there, but OK, Yep, always log this and hit edit. You said you changed out the image. Was was it this specific image?

**Carlos Aldana** 57:38
Yeah, I\'m talking about this first slide.

**Daniela Tea** 57:42
OK, so let\'s see here how it looks in Google.
OK, so it sounds like if I\'m.
I guess I would need to understand like what placement yeah.

**Carlos Aldana** 57:57
Yeah now now you see it now you see it right. But I I I just struggle. So my my my question because I remember that you last probably last week or the previous week you you mentioned that you you adjusted the the.

**Daniela Tea** 58:11
Mhm.

**Carlos Aldana** 58:16
Only the mobile image and I I didn\'t know how to do it.
You know, you just did a specific slide for the mobile. It\'s light. Yeah, option.

**Daniela Tea** 58:35
Let\'s see. So I\'m going to, let\'s, yeah, let\'s take a look here and I\'m just gonna take a quick look at your image position. So what you\'re saying though, is that you had to kind of figure out like what\'s the best way to do this, you know, in order to set it so it\'s showing what I want.

**Carlos Aldana** 58:47
Mhm.

**Daniela Tea** 58:52
And honestly like this, I guess this is what the image position tab is for. Like what is the focal point that you want? Like for example when like this I\'m assuming in mobile you probably want you might just want it to be, you know, you might want it to be focusing on this section, you might want to be focusing on this session.

**Carlos Aldana** 59:10
Yeah.

**Daniela Tea** 59:10
It\'s a matter of just positioning, you know, like choosing the right position for that. Like I guess if you\'re if you\'re asking like how would I personally do that, what I\'m describing to you is exactly what I would do. Figure out oh is it in on the left or the right of the image. I want to show this person or I want to show this portion of the image and I would.
Just change the numbers accordingly. So yeah.

**Carlos Aldana** 59:32
And and but how? How? How does it work? If you want to display only the left side of the image, what would you do?

**Daniela Tea** 59:39
If you only want it to display the left side of the image for mobile.

**Carlos Aldana** 59:44
Yes.

**Daniela Tea** 59:47
Yeah. OK. One second. All right. So let\'s see.
I am going to go back to my thing. It\'s the exact same stuff, but just let\'s let\'s work on this one right here. So I\'m on stage and let\'s say we want, let\'s see. So if I were to do like say 10%.

**Carlos Aldana** 59:59
Yeah.

**Daniela Tea** 1:00:07
And if I were to view this here, let\'s see here.
Okay, um\...

**Carlos Aldana** 1:00:16
On on that note, if you you just you\'re you\'re putting 10% because it starts from the left to the right 10% and increases on from the left to the right side.

**Daniela Tea** 1:00:26
So, so just keep in mind that 5050% and 50% means centered, right? So we\'re like, yeah, 50 and 50, right? So 5050, that\'s why the focal point is centered. But let\'s see here.
Let\'s see what we can do and see how we can affect this. I think you\'re going to have to set a height for this as well, but let\'s check. I set four to pixels and see what happens. We can see how this is shifting up and down.
Oh, it\'s 200 pixels, 10%. Yeah. So you you can see just like how I\'m plugging in numbers. I\'m not saying that this is not exactly the intention I\'m doing, but I\'m just trying to show as I\'m shifting the numbers, you can see how it affects it. The reason why I think you guys, one of the issues that you guys have is that.

**Carlos Aldana** 1:01:12
No.

**Daniela Tea** 1:01:22
My sizing for this is a fixed size. I want to make sure that\'s clear. So I was going to pull up. I wanted to pull up the just so you guys could see really quickly what those sizes are.
Second, pulling up the JIRA requirements that describe the exact sizes for our hero banner.
Yeah. So for the hero banner, we can see that there are three different sizes, small, medium and large. So what was established was that small is always going to be 540, medium is always going to be 600 and large is always going to be 814.
So when you are using the hero banner component, this kind of goes back to, I believe Lisa was mentioning having to use the image component. These specific heights variations is not something that\'s for the image component, it\'s specifically for the hero banner and that\'s why there\'s kind of like a fixed size that\'s being put into place.
It\'s the fixed height for these images are always going to be this when these variations are selected. So that was something that was established a while back as what was necessary for the hero banners. However, as you can see, I am kind of changing.
Oh, where is it? I\'m kind of changing my heights here for my image. So instead of whatever the big size was that was selected for that variation, I\'m changing it to something different on mobile. So if I were to probably do this.
Maybe something like this 800. You can see how now it\'s changing. It changed the height of the image, but still only displaying a certain portion. It\'s also changing the position of where the image is. So my 10% and 80% is being respected if I were to remove that.
Should default to 5050 and you can see now it\'s everything is centered, but it\'s centered as if the image was 800 pixels. So if you wanted to say only have like say like the view of.
I would say like this sky area, right? You\'d probably need to do something like this.
And then now I\'m only focusing on the sky portion, and I\'m focusing on the sky portion because I\'ve increased the height of the image in the image position section, right? So I\'m not actually like modifying the image itself, just modifying how the image is displayed on here because I just want to show.
Clouds and mobile. But then of course if I were to go back to desktop, I can see the full image as it was before because I didn\'t set a specific height for desktop. Does that kind of make sense? I can go over that again, but hopefully you can see how me setting that height.
For the exact same image, an image position is forcing it, you know to say OK, I want it to be 1200 by leaving this blank, it\'s automatically 5050. If I wanted to like play around and only show certain parts of this image, say I do this.

**Carlos Aldana** 1:04:25
Yeah.

**Daniela Tea** 1:04:41
You can see now we\'re focusing on on this portion, but if you leave it blank, it\'s always going to be essentially like centered.

**Carlos Aldana** 1:04:49
Yeah, and if I wanna display all the all the left side of the image, what would it be?

**Daniela Tea** 1:04:55
If you only want to display the left side, oh, so let\'s remove the height. Then make sure I understand this and we want to display the left side of the image, meaning like, I don\'t know like.
Sorry, this is.

**Ramona Harris** 1:05:10
Like for instance, that hero that you were just on with the two people at the at the the registration counter, the people are all the way to the left. Like if he just wanted to show those two people, would you just have to manipulate the mobile vertical position?

**Daniela Tea** 1:05:17
Uh.

**Carlos Aldana** 1:05:24
Mm-hmm.

**Daniela Tea** 1:05:29
Hang on, let me find a How about this? Let\'s add this these guys here.
OK, let\'s let\'s see how we can do that for this one too.

**Carlos Aldana** 1:05:38
Yeah.

**Daniela Tea** 1:05:39
Uh, OK hmm.
Uh, so we\'re saying we want these people to be shifted over to the left. Is that correct?

**Ramona Harris** 1:05:48
Like if we wanted them to be centered.

**Daniela Tea** 1:05:50
want them to be centered. Okay.

**Carlos Aldana** 1:05:52
In in this case, you will be looking to to go to the right, right?

**Daniela Tea** 1:05:56
I would want to focus to the right. That\'s correct. So let\'s try and see what we would need to do for that.

**Carlos Aldana** 1:05:59
Yeah.

**Daniela Tea** 1:06:05
60%. This is still 50%. Let\'s see. So we\'re slowly shifting. So I\'m going to change this to 70.
So if I want it to be centered, this is me centering. I know it\'s not exact guys, but this is me having them more centered on by changing that horizontal position specifically for mobile.

**Ramona Harris** 1:06:20
Yeah.

**Carlos Aldana** 1:06:27
No, but this this is very helpful looking look into you doing this.

**Daniela Tea** 1:06:32
OK. So yeah, so Carlos, just to confirm, is this like are you kind of seeing like how that would work in relation to like the image that you had for the prod site?

**Carlos Aldana** 1:06:44
What? What was that?

**Daniela Tea** 1:06:46
I said is is what we were just reviewing here. Is that is that helpful for you as you were working on the? OK, perfect. Glad to hear that. Awesome. Thank you, Carlos. Rick, I think I saw your hand up.

**Carlos Aldana** 1:06:50
Yes, yes, definitely. Thank you.

Lyon, Rick (Director of Digital Experience)** 1:06:59
No, I I I answered. The image looks like it was starting to like you\'d reach the end of it because of that white line, but you could see you moved it a little bit more. Now you can see there\'s a gradient and something in the foreground. So I I thought maybe the image had been reached the edge, but no.

**Daniela Tea** 1:07:06
Oh yeah, it\'s it\'s \'cause.
Oh yeah, yeah, no, understood. Yeah, the image I was chosen just happened to have like a white wall or something.

Lyon, Rick (Director of Digital Experience)** 1:07:15
Yep.
Yeah, yeah. So I\'m good. That\'s why I put my hand up. Thanks.

**Daniela Tea** 1:07:21
OK, awesome. Awesome. OK. So thanks Carlos for that for that question. Actually really happy that we were able to go over that and happy to hear that you\'re able to use that. Hopefully as you\'re updating the pod site, you know if you have a question, please post it in the Confluence page and perhaps I can take a look at it and.
Try to see if we can address it in tomorrow\'s session if you have any other issues, OK?

**Carlos Aldana** 1:07:44
OK. Thank you.

**Daniela Tea** 1:07:45
All right, so that was the hero banner. I\'m just going to Scroll down to the hero carousel, which of course is basically a carousel to be able to add specific components. I think there was a question previously as to why is the hero carousel only limiting us to show these three items to be.
Clear checking the requirements since this is supposed to only really have hero banner or in some cases just like a blank or plain image with no text or anything like that or a video. That\'s the reason why this was restricted to only three different.
Components. Certainly if there\'s additional components that you guys need to add that can be configured in the future, but we specifically restricted it based off of what we understood was needed for this component, so adding.
Adding a a new hero banner here. It\'s the same process as we had for. I think some of the other carousel components that you guys are familiar with the different slides displayed here. You would just add your title for the slide, see each.
And my properties tab.
I\'m able to select the active item. I think typically you guys are showing whatever\'s first. That\'s what the default is. But if for whatever reason you need it to start from a certain point, say you\'re adding more items, but a specific slide is something that should still be, you know, important even though it\'s not the first item place.
You have the ability to select whatever you want to be active on load. You can see here automatically transition slides is on. I think that\'s what you all are typically using, but you can change the delay if you need it to be longer than just sliding through at the speed that we see here. This can be increased.
Or decrease depending on what you think is best. We have disable automatic pause on hover. So depending on if you turn this on or off right now, if you were to pause on top of the slide it will stop. So that way the user can read the information on there versus it still automatically sliding.
And then also this final check box of always display carousel slide indicator, which we see is what\'s displayed here on the banner. Hey Carlos, I see your hand up.

**Carlos Aldana** 1:10:12
Yeah, regarding that the the transition delay, I I\'m not sure if that\'s working properly because when when I was trying that I had to increase the delay probably to 10,000.

**Daniela Tea** 1:10:14
Mhm.
Mhm.

**Carlos Aldana** 1:10:29
Because I I I\'m I\'m not sure if once once you go to you reach to the next slide it\'s supposed to start from zero again or it it it continues counting from the one the from the time that you start watching the the slides.

**Daniela Tea** 1:10:36
Mm.

**Carlos Aldana** 1:10:46
And I think that they should start again from zero once you are watching a particular slide.

**Daniela Tea** 1:10:55
Let me.

**Carlos Aldana** 1:10:55
I\'m not. I\'m not sure if I you get. Yeah, yeah.

**Daniela Tea** 1:10:57
Yeah, let me make sure I understand what you\'re saying. So we\'re gonna view this as published and if you could just describe what you what your understanding of it was. So right now you can see it\'s automatically transitioning, so it should be transitioning in like one second, yeah.

**Carlos Aldana** 1:11:05
OK.
This.

**Daniela Tea** 1:11:12
So now it\'s cycling through.

**Carlos Aldana** 1:11:12
Yeah, and that\'s too. Yeah, super fast.

**Daniela Tea** 1:11:16
OK, so if we were doing, yeah.

**Carlos Aldana** 1:11:17
OK so but if you use your arrows and if you use and OK then if you are here it it is supposed to start again counting you know the the the the frequency.

**Daniela Tea** 1:11:31
Oh, you\'re saying if I if I use the arrows, does it start at 0 when I interact with this? OK, I see what you\'re saying.

**Carlos Aldana** 1:11:35
Yeah, it it it\'s supposed to start at 0 because otherwise you you just use your your arrow and you don\'t have time to read the next one because it is gonna change.

**Daniela Tea** 1:11:46
OK, um, so let\'s see what we have configured here. So.

**Carlos Aldana** 1:11:54
To fix that, I I increased it to 10,000.

**Daniela Tea** 1:11:58
Right. Uh.

**Carlos Aldana** 1:11:59
At least to for the experience to be better.

Lyon, Rick (Director of Digital Experience)** 1:12:02
What? What\'s the equivalent to 7 seconds in milliseconds? Is that 7000 or or 70,000? OK.

**Daniela Tea** 1:12:02
Oh my God.
7000, right? I think. No, it should be 7070 thousand, right? Oh man, someone who\'s better at math than me. Please answer.

Lyon, Rick (Director of Digital Experience)** 1:12:20
Because that\'s what we I usually put is I think 7 seconds just so you have time to read.

**Daniela Tea** 1:12:24
OK, let\'s pretend.

Lyon, Rick (Director of Digital Experience)** 1:12:25
So if it\'s on 5000, then that would be like, yeah, very fast compared, compared to.

**Daniela Tea** 1:12:30
So I have changed it now to 770. Although yeah, I need somebody to check my math. I don\'t feel like 70,000 is correct, but that\'s why I changed it too. So as it\'s cycling through. So I think Carlos, what you\'re saying though is no matter.
If you were to, if you were to click on this, that should kind of your expectation is that it would retrigger the countdown from here. OK, all right, got it. So I\'m gonna change it back from 70. Yeah, let\'s change it to 7000 and so.

Lyon, Rick (Director of Digital Experience)** 1:12:51
Should be 7.

**Carlos Aldana** 1:12:56
Yes.

Lyon, Rick (Director of Digital Experience)** 1:13:00
7000.
I just looked it up.

**Daniela Tea** 1:13:05
OK. Thank you, Rick. Like we might be sitting here for a while, alright.

Lyon, Rick (Director of Digital Experience)** 1:13:06
No, I wanted to know.

**Carlos Aldana** 1:13:08
It.

Lyon, Rick (Director of Digital Experience)** 1:13:09
Yeah. So I guess five was like 5 seconds. So that\'s still kind of quick.

**Daniela Tea** 1:13:12
Yeah. So five was 5 seconds, correct. OK. So yeah, OK. So I am going to, I think I\'ll Carl\'s off to investigate that a little bit more. What you\'re saying though is that the expectation or what you were wanting to confirm is if the arrow indicators resets the.
Timer if you have automatic transition set on and if not right now it sounds like what you\'re doing is you are you increase the time for the transition delay. But let me get back to you on on that. I\'m going to check with the dev team to see what our expected behavior was.

**Carlos Aldana** 1:13:37
Yeah.
Mhm.

**Daniela Tea** 1:13:52
I can report back on that tomorrow, OK?

**Carlos Aldana** 1:13:54
Awesome. Thanks.

**Daniela Tea** 1:13:56
No, thank you. OK, so properties, we talked about this. We talked how the carousel slide indicator is being displayed here and then there\'s some accessibility items with regards to labels, previous, next.
So this is items that you would be able to see if you were to view source. You would see these Aria labels within the markup. And for this you\'ll notice there\'s that empty slide. That\'s because what I did.
Was I had added my my beach slide, but I didn\'t actually edit it. So I don\'t know if like the team has run into any issues like that where you know you you\'re like, where\'s this coming from? Of course it\'s because I did not actually edit this one. All right, so.
Here I can see the different items. I am actually able to kind of interact with this if I wanted to, like so say I want to change the order from here. But truthfully, typically what I personally do is I I usually just like configuring it so that way I can also make changes.
Within the dialogue window or delete something from this specific view. So all right, so as we know from our hero banner, exact same items, you know, because it\'s just essentially a banner that\'s within the carousel. So I think you know you guys already know how to use this.
But I will certainly look into the automatic transition delay versus when you click on the arrow and I will report back on that item. Any questions though about the hero banner or hero carousel that you guys have? Anything else that you guys are doing currently on your site that you guys maybe want some more?
Yeah, Carlos, please go ahead.

**Carlos Aldana** 1:15:41
I think that that can can you open the the the carousel again the to see it?

**Daniela Tea** 1:15:46
The actual carousel, certainly, Yep.

**Carlos Aldana** 1:15:48
Yeah.
OK, I can you check if those names for each slide are named equally on the left side of the drop down menu? Yeah, that one.

**Daniela Tea** 1:16:06
You\'re talking about in here. OK, let\'s take a look. OK, so we have Harold Collard\'s Hard Rock sale. OK, so this is still seeing Hard Rock. Oh, wait, no, am I looking? I\'m looking at the right thing. OK, Yeah. OK.

**Carlos Aldana** 1:16:06
Yeah, yeah.
Because because what I what I I I think that my experience was that it was registering only the title assigned to the slide instead of these.

**Daniela Tea** 1:16:30
OK, I see. So your question is why is this showing items that are not actually associated with the hero carousel? So why are these not being replicated here? So for example we see.

**Carlos Aldana** 1:16:37
But I probably I\'m mistaken.

**Daniela Tea** 1:16:48
Hard Rock Live, whereas this one here is saying Mike Tyson presents return of the mic tour. So let\'s see Uni by Hard Rock. Now I\'m gonna assume this last one says Hard Rock Cafes, OK?

**Carlos Aldana** 1:17:04
And sometimes it\'s confusing, you know.

**Daniela Tea** 1:17:05
OK, so yeah, I think what\'s going on is what this is displaying is it\'s actually looking at the eyebrow portion of the hero banner. That\'s why this is blank because there\'s nothing there. If I were to put testing right here in eyebrow text.

**Carlos Aldana** 1:17:21
Yeah.

**Daniela Tea** 1:17:21
That\'s what should be displayed here. So this is actually taking the eyebrow text. It is not taking the name of the slide here, which I understand could certainly be confusing because from here I think from this aspect.

**Carlos Aldana** 1:17:36
Yeah.

**Daniela Tea** 1:17:39
You know, this is more for if you want, if you know you want to quickly reorder something or whatever, you know that this specific one is what you want. But yes, from this view it is showing the first element of the hero banner, which is the eyebrow. So that is what it is right now. But definitely understand that why you why that could be confusing and also something I would.
Mention this would be a perfect candidate to add as a gap if that\'s something that you would be looking to changing in the future.

**Carlos Aldana** 1:18:06
OK.
Thank you.

**Daniela Tea** 1:18:09
Yeah. All right. OK, let\'s see here. I\'m gonna go back to our agenda. Hero banner, Hero carousel, Media gallery, image gallery, grid. OK, so we\'ve covered those four. I\'ll be getting back with some.
Answers on some of the questions we had today with regards to the video player component. So as we had seen when I was adding the hero banner and using the video, we\'ve kind of we\'ve noticed you know with the video card and the and the like this video component.
Inside the Hero banner, you\'re going to see like those same settings. So this is more just, you know, it\'s you guys should be familiar with this based off what we saw. You know, selecting that third party is going to list those different options. Again, I think there are some follow-ups I\'m planning on providing. There were some questions.
Regards to the layout, fixed and responsive that I believe I saw on the jobs page, so I do need to get back to that. But the video card like we saw previously is very much similar to the video component. You\'ll see a lot of the same fields.
However, they are separate because the video card of course has some additional fields that need to be filled out with regards to like the title, the description, and also the fact that it opens up into a separate modal window.
So I want to make sure there was, you know, there\'s some clarity as to these two different components, but there are a lot of similarities with regards to the authoring dialogue. So in addition to, I guess, is there anything else other than the questions that I know have already been asked with regards to Video Guard?
Is there any other questions about like video in general with these components?

**Carlos Aldana** 1:20:07
No.

**Daniela Tea** 1:20:08
All right. OK. So going back here, we also have images. I think you guys, you guys are pretty familiar with the image component, I would imagine. I\'m just going to add one on here.
Alright, so this by default you may wonder, hey I added I just added an image component. Why is it just showing an image? You\'ll see here inherit featured image from page is typically checked automatically.
And my featured image was set when I was creating my KT Media page. I\'m going to open up the properties. You\'ll see that there\'s an images tab. I set my featured image here and so if there is an image associated with your page, in this case this one here when you add the.
Image component with that box being checked by defaults. That\'s why this image looks like it came out of nowhere, but no, it\'s because I had set it as the featured image for my page. I\'m going to uncheck this cell. I\'m also going to uncheck this and we\'re just going to add a different image.
Garrett from description of asset. We\'re all familiar with this or if I need to add something specifically here on the page itself, I can do that. We talked about that we saw these also on our hero banner, I believe these specific fields.
We have metadata fields on the image component caption which should be coming in from the DAM or of course if you want to add your own you can do that as well. The ability to make the image a clickable link, so selecting either from within a EM.
Or putting an external link and then opening in the new tab. We have our image position tab and then we have the styles tab. I know there\'s an open question about the purpose of logo image. I\'ve reached out to the dev team and they are looking for some instances where that\'s applied so that we.
Guys can see like the specific use case, so I will get back to you on that one. But typically I think you guys are not, you know you guys aren\'t using that on here. It\'s more I want to show an image on the page. I might want to make it clickable and so that\'s that\'s how you would do it. Add the image component at the link and it should become a clickable.
Image to a destination, but any questions I guess or any use cases where you guys are using images and maybe you know there\'s there\'s there\'s something you might want to know more about it.
Right.
OK. So then I also want to talk a little bit about the container and keep in mind we are going to go more about the container and layout mode and that sort of stuff. Yep. Oh, hey, Carlos, go ahead.

**Andy Lambert** 1:23:04
Daniella, we\'ve got a question. Henry.

**Carlos Aldana** 1:23:06
It\'s a it\'s like a comment. It would be great, really, really great if we are working on a component and we can upload the image from the component itself and not have to go through the tree to the assets.

**Daniela Tea** 1:23:11
Mhm.
Uh.

**Carlos Aldana** 1:23:26
8.

**Daniela Tea** 1:23:28
I see. So what you\'re saying is and like for example instead of having you\'re saying instead of the damn uploading an image.

**Carlos Aldana** 1:23:37
Yeah.

**Daniela Tea** 1:23:38
Um.

**Andy Lambert** 1:23:38
They\'d require a the way that it\'s set up is that you, I mean you have to use the the asset has to exist in the dam and there\'s not really a way to do that right now. It could be done as a if you really, really wanted it and it was really high value, it could be done through a custom.
Uh, extension of the um out-of-the-box interface. But yeah, I hear you Carlos. It would be nice.

**Carlos Aldana** 1:24:02
Yeah. Thank you.

**Daniela Tea** 1:24:02
So, yeah, definitely that that\'s that Carlos would be platform expansion for sure. I think, I think Donna still came off of you. I don\'t know if you had any comments that you perhaps wanted to add about. Yeah, go ahead.

**Andy Lambert** 1:24:03
M.

**Don Middlebrook** 1:24:13
Yeah, I yeah, no, I I think that we might want to avoid that because people might upload it and they might actually put it in the wrong directory. And then yeah, I I just see where the need might be, but maybe if you clicked on it and then you.

**Andy Lambert** 1:24:24
Yep, there\'s a reason for it. Yeah, it\'s.

**Don Middlebrook** 1:24:33
Found the directory you wanted to put it in and then you dropped it in there. But it\'s like which way do you do it? Do you do it through here or you just do it the normal way? It\'s not that much additional work I think to do it so.

**Mayte Eme** 1:24:47
It does. It does bring value to our content authors, and we have it built in a way that if you\'re working, it goes directly to the folder that you\'re supposed to upload it. So when?

**Carlos Aldana** 1:24:48
I hear you.

**Andy Lambert** 1:25:00
It\'s a governance issue though. Also sorry to cut you off my table and I\'ll let I definitely want to hear what you you have to say. But even to to hammer home the governance point from Don also is in terms of proper dam hygiene and governance.

**Mayte Eme** 1:25:03
Pleasure.

**Andy Lambert** 1:25:17
You you know there\'s you really don\'t want the average author to have, but they had an asset that they wanted to include on a page. There should be a process by which it gets put in then.

**Mayte Eme** 1:25:28
Oh, this is not for the average author. This is not for your regular author. This is more for like the like Lisa\'s team that need to do things really, really fast. So yeah, so we load it as a gap and then we\'ll do discovery. We\'re done.

**Andy Lambert** 1:25:33
Yeah.
Yeah.
So there could be a governance.
Yeah, there could be a path that makes sense. And as part of that, my dad would say look at a path where like you and Don where you have a space in the dam where you know like that is.
For that where things might you might have a workflow that lets Don know or that the an asset\'s been put in to a specific authoring like like real time space and then gets approved and then moved into you know what I mean like or or have like I said you could do a.

**Don Middlebrook** 1:26:10
OK.

**Andy Lambert** 1:26:19
Custom interface where you you\'re limited to putting assets into a certain place from there. So there\'s definite ways to go about it, but I hear both sides like it. It would be much more convenient. That used to be there by the way, but what would happen is you the asset wouldn\'t go into the dam, it would actually just go right into the JCR.

**Don Middlebrook** 1:26:30
Isn\'t.

**Andy Lambert** 1:26:39
Under the page. And so then you had all these like orphan ghost assets like floating around, so it took it away.

**Daniela Tea** 1:26:41
Um.

**Don Middlebrook** 1:26:47
Yeah, and I think part of that, even if we do go a route to implement something like that, we need to put certain parameters in place, especially around metadata. I don\'t want an asset to go in. Even if we\'re hurrying, it still need to do it the proper way to get the asset in, make sure the metadata is applied to it.
Make sure it\'s, you know, properly published and that sort of thing. So definitely discussion that we need to have about the right way to do this.

**Lucas Nelson** 1:27:16
Yeah, feels like an internal discussion, Don, Maite and team that you guys can have. And if that\'s something that\'s a priority for you guys to add, you know, for your platform expansion, bring it to the table. Yeah, yeah, OK, sounds good.

**Don Middlebrook** 1:27:20
Yeah.
Yeah.
Sure. Yeah.
Thanks.

**Daniela Tea** 1:27:33
Yeah.

**Andy Lambert** 1:27:35
Thank you.

**Daniela Tea** 1:27:36
Yeah, no, thank you guys for that. OK. So yeah, just going to cover the two portions of the container right now.
I I believe. I\'m not sure if you guys are using the background image functionality for the container, but of course there is there the ability to set a container, put a background image, and then of course you would put all your components on top of that, so.
I\'m not, I\'m not sure if you guys are using that feature right now. Let\'s we can do it really quickly. So you can see here my my contents, I\'m sorry, my container going to set this to full width. Again, we\'ll go over all this more in greater detail in our next session.
But my image is here and you\'re thinking, well why is it not showing anything? Like it\'s just showing this top portion. So currently what I\'m doing is as I add additional components, like say I add this image here, it\'s going to then grow the container.
So that way the and all the components that are within it are going to be adding height to the specific container. Oops, I accidentally resized both. Just want to resize the image so you guys can see it. So if I were to.
Say add like a lot of content within here, then I would likely see the full image. All right, yeah, so you can see the height of the image now is dictating the height of the container. However, there is the ability to set a minimum container height.
So I\'m just going to put, I don\'t know, like 600.
And hit done. So you can see how now this is this is growing because of what I had set without having to worry about the content that\'s in here. So if you want the container to be dictated based off the content that\'s in it, so that way the height will grow as you add more content, you have the ability to do that, however.
If you want to set a fixed or a minimum height for it, so it\'s always displaying say like the top of the firework like we see here, then you can use this specific field down here to do that. I think though what the.
Most of you guys are likely using the background color. I said that so the since the background image is in here that\'s taking precedence over the background color. I\'ll clear this, hit done so I can see here. Here\'s the background color that I selected for this. Same thing though if I removed.
The height for this, it\'s only going to be as tall as the content within it. Since there is the spacer component, that\'s also an option. Say you\'re like, well, I don\'t really necessarily want like a height, but I know that I I might want you know this to have.
Just to just row like this, certainly some components to be able to show more of that background color or image. But yes, we will certainly be going more in depth on the container. I can potentially tomorrow I need to check to see what the schedule is.
And I think there were some asks about, you know, things like alignment, resizing, the parallax feature we would also talk about and then this light box tab, how does this work? I\'ll be providing some examples where we can see the use cases for why you would use this tab.
Use this tab how it works today as well as seeing how Parallax works today and how to set that up. So more to come on the container, but wanted to make sure that the team was aware about how the background image field works and also how to show more of the background.
Depending on if you have a certain certain height in mind for the specific container to show. Alright, so with that I see the time is around 2:30 and I just wanted to make sure that the team had some time to.
Ask any additional questions about any of the components that we\'ve reviewed today, keeping in mind that this one we will go way more in-depth on, but any any questions, you know the image gallery grid, the media gallery, the hero banner, the hero carousel, or the image component itself.
And if there aren\'t any, just out of curiosity, is Lisa on the call right now?

**Lucas Nelson** 1:32:12
She\'s not.

**Daniela Tea** 1:32:13
OK. All right. No problem. So Gonzalo, we confirmed earlier that you are now able to see the drop downs that you and Lisa weren\'t able to see. And then your second question was about.
The order of the content that was displayed on the page. Out of curiosity, did you end up publishing the page or anything like that you know from from the earlier discussion?

**Gonzalo Calasich (SHRSS)** 1:32:40
Yes, I did publish and uh, this is still showing up uh at the bottom.

**Daniela Tea** 1:32:45
OK, sure. I think Andy, I believe you were planning on looking into that. I don\'t know if like we we need to just follow up with Gonzalo during perhaps tomorrow\'s session or so or if you were looking at that in the background.

**Gonzalo Calasich (SHRSS)** 1:33:01
Awesome. Let me know. Thank you.

**Daniela Tea** 1:33:03
Yeah, we can do that for sure. OK, um, all right. So

**Andy Lambert** 1:33:07
Sorry, I was on mute. Yeah, sorry. I was looking into it and didn\'t find a resolution and then was looking into other stuff based on the call. But but yeah, we\'ll we\'ll come back to you. It\'s so it\'s. So basically I updated it on author in the component configuration and North America\'s up top.

**Daniela Tea** 1:33:13
Yeah, no problem.

**Andy Lambert** 1:33:24
But it\'s not making any difference on display. It\'s so we got. There\'s something up with that. I\'m not sure. I also wondered if it might be driven by like the order in generic lists or some other magic. It doesn\'t seem to be, so we\'ll have to check with Vanana Marine.

**Daniela Tea** 1:33:35
Mm-hmm.
Yeah, sure thing. Then we will take a little. Yeah, we\'ll get, we\'ll get back to you with at least a status on that on tomorrow, Gonzalo.

**Gonzalo Calasich (SHRSS)** 1:33:40
Thank you.

**Andy Lambert** 1:33:42
Yes.

**Gonzalo Calasich (SHRSS)** 1:33:47
Awesome.

**Daniela Tea** 1:33:47
OK. All right. OK, guys, as always, please make sure to update the Confluence page with any questions. I\'ll try to take a look at it and see what we can answer for tomorrow. My plan again is to I need still need to go and follow up on some items on on some of the other pages.
I really appreciate everyone\'s patience with this and also your participation in today\'s session. But if there\'s no further questions, I think we can conclude for today and resume tomorrow.

**Lucas Nelson** 1:34:18
Great job, Daniella. Thank you.

**Edwin Aquino** 1:34:19
Thank you, Danielle.

**Daniela Tea** 1:34:20
Okay, thank you everybody. Bye.

**Don Middlebrook** 1:34:21
All right. Thank you.

**Edwin Aquino** 1:34:21
Thank you.

**Gonzalo Calasich (SHRSS)** 1:34:23
Thank you. Thank you. Bye.

**Kerry Holyoak (SHRSS)** 1:34:25
Yes, Sir.

**Angelika Akopyan (SHRSS)** 1:34:25
OK.

Lyon, Rick (Director of Digital Experience)** 1:34:27
Thank you.

Scott Sorel** stopped transcription