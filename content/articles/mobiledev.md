Title: Mobile App Development
Date: 2014-04-25 23:40
Tags: ios, android, google, xcode, apple, iphone, ipad, ipod touch
Category: programming
Slug: mobiledev
Author: Donald Burr
Summary: Information on how to get started with mobile app development

# So You Wanna Write an App?
### Jumping feet first into the wild world of app development
#### by Donald Burr

---

It happens to all of us eventually.  Perhaps you're having a frustrating time using an app, and wish that the developer could have written it *this* way, or added *that* feature.  Maybe a brilliant idea for the Next Big Thing(TM) hit you while you were in the shower one day, but you are hesitant to hire a programmer to help realize your dream, lest they decide to run off and [steal your idea][STEAL] (or perhaps you just can't afford to hire anybody.)  Or maybe you're trying to get something done, but as it turns out, there just isn't "an app for that."  (It happens more often than you think!)

In cases like this, you might have wished that you could write your own app.  But the mere thought of doing so sends a chill of fear and dread up your spine.  *It's hard!*  *I have to learn how to code!*  *It costs a lot of money!*  *What if Apple rejects my app?!*  Well, fear not my friend: I am here to tell you that developing apps for iOS and the Mac is not as scary as it sounds, nor is it as costly as you might think.  In fact, most of the tools and information you'll need are *entirely free of charge*!

"Whoa there!  Wait a minute!" you might be saying to yourself right about now.  "I thought it costs money to get into the Mac and iOS developer programs!"  This is in fact correct: you must pay Apple $99 per year to join the [Mac][MACDEV] and [iOS][IOSDEV] developer programs.  (That's $99 per program folks; so if you want to develop for both Mac and iOS, you're talking $198/year.)  However, you only need to pay if you wish to do the following:

* sell your apps in the App Store
* sell your Mac apps outside of the App Store with a [registered developer ID][ID]
* test your iOS apps on actual iOS devices.  (Apple's developer tools come with a software-based iPhone and iPad emulator; if all you want to do is use this, then you need not pay anything.)

In other words, if you're just getting started, or just want to experiment (get your feet wet, so to speak,) *you don't have to pay anything at all*.  Only once you've decided that, yes, this developing apps thing is my kind of gig, do you have to pay up.

But paying up does have its perks.  For one thing, you get to test new versions of iOS and Mac OS long before the public sees them.  This is of course vital to ensure that your apps will work with the "next big thing"; but it's also fun.  You also get access to the full Apple Developer website, with its wealth of information, technical documents, and training videos.  (all session videos from Apple's [Worldwide Developers Conference][WWDC] (WWDC) are available for your perusal; it's the next best thing to being there!)  You also get access to the Developer Forums, an extremely useful place where you can chat with other developers, ask questions, and discuss the finer points of app development.  (Oftentimes you'll find Apple engineers monitoring the forums, so you can get your help from the experts!)

##### So What Do You Need?

First and foremost, you will need a Mac.  Odds are that, if you are reading this, you probably already have one.  If not, then go and get yourself one.  Fortunately it doesn't have to be a particularly powerful Mac; however it does need to run the current operating system of the day (which at the time of this writing is OS X 10.8 Mountain Lion.)  A Mac mini will do nicely, as will a MacBook Air.  Even a used Mac would work brilliantly, so long as it can run Mountain Lion.

You will also need [Xcode][XCODE], Apple's [integrated development environment][IDE].  This comprehensive set of tools comes with everything you need to write, test, debug and package your app for sale or distribution.  Xcode is available for free in the Mac App Store.

Finally, while not strictly speaking a requirement, a cadre of friends, acquaintances, coworkers, etc. who would be willing to help out by testing your apps on their precious iDevices is extremely helpful.  The more testing your app gets, and the more variations on hardware and software that it is tested with, the better.

##### Dipping Your Toe in the Shallow End

Psst!  Did you know that you can create iOS apps *without even writing a single line of code*?  It's true!  Using the [RedFoundry][REDFOUNDRY] web-based environment, you can quickly and easily create a basic iOS app by dragging and dropping "widgets."  You can choose from a wide variety of widgets, such as RSS feed viewers, audio players, Twitter stream viewers, Flickr viewers, and more.  As you build your app, you can quickly test it on your actual iDevice using [Red Foundry's free app][RFAPP].  When your app is all done, you can publish it to the App Store straight from the Red Foundry website.

![Red Foundry lets you easily build an iOS app by dragging and dropping widgets][RFIMG]

*Red Foundry lets you easily build an iOS app by dragging and dropping widgets.*

There are many similar tools out there; for example [GameSalad][GAMESALAD] is specially geared toward writing games, and includes such features as physics engines, graphics sprites, collision detection, and so on.  Services such as RedFoundry and GameSalad are a great place to start, and are perfect if all you want to do is write a fairly simple app.

![The beginnings of the Next Big Game.  I'm calling it "Belligerent Avians."][GS1]

*The beginnings of the Next Big Game.  I'm calling it "Belligerent Avians."*

![In GameSalad, you can easily assign attributes and set up behaviors for your game's objects.][GS2]

*In GameSalad, you can easily assign attributes and set up behaviors for your game's objects.*

##### Time to Swim Out to the Deep End

Although tools such as Red Foundry and GameSalad are quite capable, there will come a time when what you want to accomplish is beyond their capabilities.  It's time to leave the shallow end and swim out to the deep end of the pool, and learn how to code.  But, as I said earlier, it really isn't as hard as it sounds.

A good place to start is the excellent book *[Objective-C Programming: The Big Nerd Ranch Guide][BNRBOOK]*, written by the fine folks over at the [Big Nerd Ranch][BNR].  Big Nerd Ranch is a company that, among other things, teaches seminars on Mac and iOS programming; they also write apps on a contract basis.  So they know their stuff.  This book assumes you know nothing about programming at all, and teaches you the fundamentals of programming in Objective-C, the language Mac and iOS apps are written in.  It also teaches you the basics of Mac and iOS programming.  After this, you might want to check out their other books for more in-depth coverage of the particular platform you are interested in developing for: [Cocoa Programming for Mac OS X: The Big Nerd Ranch Guide][MACBOOK] (for Mac development) and [iOS Programming: The Big Nerd Ranch Guide][IOSBOOK] (for iOS development.)

![No, you're not looking at the Matrix.  This is Xcode's code editor.  It has many features that help make entering code a lot easier.][XCODECODE]

*No, you're not looking at [the Matrix][MATRIX].  This is Xcode's code editor.  It has many features that help make entering code a lot easier.*

Your local community college or Adult-Ed center might have courses on computer programming and app development that might help as well.  With the growing popularity of iOS devices and Macs, many institutions of higher education are jumping on the bandwagon and offering such courses.

![Using Xcode's Interface Builder, you can construct your app's User Interface by dragging and dropping from a palette of buttons, text fields and other common controls.][XCODEIB]

*Using Xcode's Interface Builder, you can construct your app's User Interface by dragging and dropping from a palette of buttons, text fields and other common controls.*

Or, if you are interested in iOS development, you might just want to stay at home and study online.  One of the best courses on iOS app development, [CS193P][CS193P] is available *for free* on Apple's [iTunes U][ITUNESU] service (one of the most under-appreciated parts of iTunes in my opinion.)  This college-level course is taught at Stanford by instructors who really know their stuff; and since Stanford is practically in Apple HQ's backyard, you can often find Apple employees appearing as special guest lecturers.  Using the free [iTunes U app][ITUNESUAPP] you can watch the lecture videos, view the lecture notes and slides, take notes and view the homework assignments.  (You can also download all the code you see the instructor working on in class, but you'll need to do that from your computer.)  It's all the benefit of a college education without the hassles (being graded, quizzes, finals, having to get up at the crack of dawn to make it to class on time, etc.)

![iTunes U: All the benefit of a college education, without the hassle.][ITUNESUIMG]

*iTunes U: All the benefit of a college education, without the hassle.*


##### Tips for Success (and Avoiding App Rejection)

You've probably heard the horror stories of developers toiliing long and hard on their masterpieces only to get flatly rejected by Apple.  It's true that Apple does reject a fair number of apps; however for each app rejection, there are also thousands of apps that "made the cut."  You only hear about the rejections because they complain about it vociferously on Twitter and blogs.  (In other words, they are a *very* vocal minority.)

But you would certainly want your app to be as good as it could be, and to really shine when viewed by the Apple review personnel; and to help with that I have the following suggestions.

* **Beauty is more than skin deep.**  Apple products are known for their beauty, elegance, simplicity and ease of use.  The same applies to the apps that run on them.  Apps should pick a design aesthetic and adhere to it.  User interfaces should be as simple as possible and convey only the most necessary information.  Navigation should be intuitive and fluid.  Every year at WWDC, Apple hands out its [Apple Design Awards][ADA] to apps that they feel exemplify the design and usability aesthetics of Apple.  You would do wisely to study these apps and learn from their success.  There is also a corollary to this tip, which is:
* **If you want to create the best apps, use Apple's tools.**  Tools such as Red Foundry, GameSalad, etc. make pretty decent looking user interfaces; but when compared to apps written using Apple's tools, they look a bit "off."  The user interface is "kinda, sorta, almost" Mac- or iOS-like.  But it's *just* different enough that someone would notice.  For the most "Mac-like" or "iOS-like" experience, you really need to roll up your sleeves and dive into the Apple development environment.
* **Keep your ear to the ground...** Wayne Gretzky once said, "A good hockey player plays where the puck is. A great hockey player plays where the puck is going to be."  Great apps come not from responding to the desires of users today (although that is certainly a good thing to do too,) but from anticipating what a user's needs will be in the future.  Keep an eye out on the various social networks.  Find out what the "next big thing" is ? the next big social network phenomenon that is starting to gain traction; trends in the types of games people like to play; etc.  When the "Next Big Thing" hits, you'll be ready with "an app for that."
* **...but be prepared to jump out of the way if a train comes rushing by.**  Apple has been known to radically (and without much warning) change things in its software or its developer policies.  Don't be surprised if a feature or programming trick that you are relying on suddenly changes its function or stops working entirely.  Be ready with a workaround.  Joining the paid developer program really helps in this regard, since you get early access to new iOS and Mac OS releases before the public does; you can test your apps, change your code or create workarounds to counter Apple's changes, and be ready with an app update when the public gets their next OS update.
* **Play by the rules.**  Heed Apple's developer agreements.  Most importantly, only use public APIs (the programmatic interfaces that Apple vends out.)  A good rule of thumb is: if it's documented in official Apple documentation, then it's fair game.  If, on the other hand, you heard of this really cool trick from a buddy, or saw an interesting function call while digging through Apple's code, then I would stay very far away.  Using private or undocumented APIs or coding tricks is the quickest way to get your app rejected.  And Apple, given its fickle nature, has been known to change their developer rules suddenly and without much notice (if any at all); so stay alert!
* **Respect your users' privacy and security.**  Apple has made some tremendous strides in respecting a user's privacy, and so should you.  If you don't need a particular type of information (a user's [location][LOCPRIVACY], access to his/her [contacts][PATH] or calendars, etc.,) then don't ask for it.  If you do, provide a good reason ? Apple gives developers a way to inform the user as to why your app is requesting that information from him.  If you transfer any sensitive data online, encrypt it.  If you need to store any sensitive data on a user's phone (usernames and passwords, etc.) do so securely.  Apple's Keychain is an excellent and very secure method of safely storing usernames and passwords, and there are many code libraries (both from Apple as well as third parties or Open Source) suitable for use in encrypting data for transmission over the Internet.  And if a user decides not to trust your app with access to his/her information, please respect their decision.
* **Apple gives you a lot of toys to play with.  Use them.**  Apple gives us developers a bevy of toys to play with, and users will expect you to take advantage of them.  Got an app that deals with significant amounts of data (databases, note taking apps, etc.)?  Use [iCloud][ICLOUD]; many people have multiple iDevices nowadays, and expect their data to be available ubiquitously.  Are you writing a game?  Then by all means use [GameCenter][GAMECENTER]!  Not only is it a great way to give users value (people *love* challenging each other and boasting about their high scores,) but it is also a great way to promote your game.  Are you writing an app with regularly updating content (blog, magazine, newspaper, etc.)?  Then you should definitely be in [Newsstand][NEWSSTAND].  And so on.  And finally:
* **Don't be disappointed if you don't make millions overnight.**  (OK, this doesn't really have any bearing on your app's chance at approval.  I just didn't have anywhere better to put this.)  The fact of the matter is that for every *Angry Birds* and *Tweetbot*, there are thousands of unsung heroes ? otherwise good (perhaps even great) apps that just didn't manage to grab peoples' attention and interest.  It's all a [numbers game][NUMBERS], and with [over 700,000 apps][MANYAPPS] currently in the app store, getting noticed is pretty difficult.  Sadly the App Store is not as fertile a ground for making money as it was in the past.  That's not to say that you don't have any shot at all; it's just going to take some effort (and some good luck) on your part.  Talk about your app as much as you can on Twitter and Facebook without being annoying; show it off to friends, relatives, colleagues, guys off the street, anyone really; perhaps even call in to [a certain nationally syndicated radio talk show host][TECHGUY].  But if you go into this whole app-making thing with the sole desire to [strike it rich][MONEY], then [you have lost the game][YHLTG].  Rather, the attitude I like to take is similar to the attitude I take toward podcasting: "Do it because it's fun and/or interesting.  Do it as a pasttime or a hobby.  And if you happen to make some money, more power to ya."

##### A Note about Accessibility

Finally, let me talk a little about [accessibility][ACC].  (Besides, [a certain podcaster][NC] and "technology for the disabled" advocate would have me drawn and quartered if I didn't!)

There are 314 million people worldwide who have some form of visual disability (partially sighted or totally blind)  278 million have moderate to severe hearing loss.  That's a *lot* of users ? *more users than are on Facebook!* ? and shutting yourself out of that sizable user base is sheer insanity.  Especially when adding accessibility to your app is [a lot easier to do than you think][AA]  (In fact, in most cases Apple has already done most of the work for you!)  The iPhone is the world's most accessible smartphone.  Period.  Same goes for the Mac.  Apple has put a ton of effort into making their platforms accessible, and they are definitely the industry leader.  These devices have literally opened up a whole new world for the disabled, and you would be foolish not to enable them to use your app.

##### That's it!  No, really, that's it!

Don't get me wrong.  There will certainly be a fair amount of head-scratching and "WTF" moments as you dive in and learn the intricacies of coding.  But it's certainly not an insurmountable challenge, and definitely isn't something that you should run away from in fear.  Aside from the resources I have mentioned already, there are a ton of places where you can get help and more information online.  (Besides the Apple Developer Forums, [Stack Overflow][SO] is an excellent place where you can ask programming-related questions and get really good answers.)  Programming is sort of like learning to ride a bicycle: you'll probably be quite a bit wobbly at first, you'll fall a lot and suffer many scrapes and bruises; but pretty soon you'll get the hang of it and will be zooming through code like nobody's business.

Now go forth and realize your dreams!  Who knows?  Maybe you'll end up writing the next *Angry Birds*... er, I mean *Belligerent Avians*!

---

*[Donald Burr][DBURRBLOG] has been using -- and abusing -- computers and gadgets practically since the day he was born.  (Rumor has it he was born with a keyboard in one hand and a mouse in the other.)  He is an [avid amateur app developer][DBURRAPPS] and is [available for hire][CONTACT] if you need a little help getting started in app writing.  When he's not geeking around with tech, he can be found blogging and podcasting about Japanese animation and culture at [Otaku no Podcast][OTAKU].  He can be found on the Twitters as [@dburr][DBURRTWITTER].*

[SO]: http://stackoverflow.com "Stack Overflow"
[YHLTG]: http://www.losethegame.com "You Lose The Game"
[MONEY]: http://bjango.com/articles/golddigging/ "Money"
[STEAL]: http://www.aljazeerah.info/News/2011/April/11%20n/Did%20Mark%20Zuckerberg%20Steal%20the%20Facebook%20Idea%20from%20the%20Winklevoss%20Twin%20Brothers.htm "Steal"
[ID]: https://developer.apple.com/resources/developer-id/ "Developer ID"
[MACDEV]: https://developer.apple.com/programs/mac/ "Mac Developer Program"
[IOSDEV]: https://developer.apple.com/programs/ios/ "iOS Developer Program"
[XCODE]: http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12 "XCode"
[REDFOUNDRY]: http://www.redfoundry.com "Red Foundry"
[GAMESALAD]: http://gamesalad.com/ "GameSalad"
[IDE]: http://en.wikipedia.org/wiki/Integrated_development_environment "IDE"
[WWDC]: https://developer.apple.com/wwdc/about/ "WWDC"
[RFIMG]: https://dl.dropbox.com/u/169813/DevArticleImages/RedFoundry.png "Red Foundry screenshot"
[RFAPP]: http://itunes.apple.com/us/app/fusion-mobile/id536032952?mt=8 "Red Foundry app"
[CS193P]: http://itunes.apple.com/itunes-u/ipad-iphone-application-development/id473757255?mt=10 "CS193P"
[ITUNESU]: http://www.apple.com/education/itunes-u/ "iTunes U"
[BNR]: http://bignerdranch.com/ "Big Nerd Ranch"
[BNRBOOK]: http://www.amazon.com/dp/0321706285/?tag=otakunocast-20 "Objective-C Programming: The Big Nerd Ranch Guide"
[NC]: http://podfeet.com/ "NosillaCast"
[AA]: http://www.podfeet.com/wordpress/tutorials/build-accessible-ios-apps/ "How to build accessible apps"
[C]: http://en.wikipedia.org/wiki/C_(programming_language) "C"
[OOP]: http://en.wikipedia.org/wiki/Object-oriented_programming "Object Oriented Programming"
[OBJC]: http://en.wikipedia.org/wiki/Objective_c "Objective-C"
[ACC]: http://en.wikipedia.org/wiki/Accessibility "Accessibility"
[MACBOOK]: http://www.amazon.com/dp/0321774086/?tag=otakunocast-20 "Cocoa Programming for Mac OS X: The Big Nerd Ranch Guide"
[IOSBOOK]: http://www.amazon.com/dp/0321821521/?tag=otakunocast-20 "iOS Programming: The Big Nerd Ranch Guide"
[GS1]: https://dl.dropbox.com/u/169813/DevArticleImages/GameSalad1.png "GameSalad 1"
[GS2]: https://dl.dropbox.com/u/169813/DevArticleImages/GameSalad2.png "GameSalad 2"
[UDID]: http://itunes.apple.com/us/app/udid/id458358726?mt=8 "UDID"
[MATRIX]: http://boscosgrindhouse.com/2012/07/30/boscos-franchise-collection-the-matrix-trilogy/ "The Matrix"
[ADA]: https://developer.apple.com/wwdc/awards/ "Apple Design Awards"
[OTAKU]: http://otakunopodcast.com/ "Otaku no Podcast"
[DBURRAPPS]: http://DonaldBurr.com/apps/ "Donald Burr's Apps"
[DBURRBLOG]: http://DonaldBurr.com/ "Donald Burr's Blog"
[DBURRTWITTER]: http://twitter.com/dburr/ "Donald Burr on Twitter"
[ITUNESUAPP]: http://itunes.apple.com/us/app/itunes-u/id490217893?mt=8 "iTunes U App"
[PATH]: http://www.pcmag.com/article2/0,2817,2400016,00.asp "Path Debacle"
[GAMECENTER]: http://www.apple.com/game-center/ "GameCenter"
[NEWSSTAND]: http://www.apple.com/ipad/from-the-app-store/newsstand.html "Newsstand"
[ICLOUD]: http://www.apple.com/icloud/ "iCloud"
[MANYAPPS]: http://ipod.about.com/od/iphonesoftwareterms/qt/apps-in-app-store.htm "Many apps"
[NUMBERS]: http://arstechnica.com/apple/2012/05/ios-app-success-is-a-lottery-and-60-of-developers-dont-break-even/ "Numbers Game"
[TECHGUY]: http://techguylabs.com "The Tech Guy"
[XCODECODE]: https://dl.dropbox.com/u/169813/DevArticleImages/XcodeCode.png "Xcode Code"
[XCODEIB]: https://dl.dropbox.com/u/169813/DevArticleImages/XcodeIB.png "Xcode Interface Builder"
[ITUNESUIMG]: https://dl.dropbox.com/u/169813/DevArticleImages/iTunesU.PNG "iTunes U image"
[LOCPRIVACY]: http://phys.org/news/2012-01-location-based-geo-fencing-apps-privacy.html "Location privacy"
[CONTACT]: http://donaldburr.com/contact-me/ "Contact Me"
