Title: Do-It-Yourself Home Automation with the Belkin WeMo
Date: 2014-07-13 12:40
Tags: home automation, ha, scripting, belkin, wemo, automation, ifttt
Category: howto
Slug: home-automation
Author: Donald Burr
Summary: Information on how to set up a Home Automation system using Belkin's WeMo products

### By Donald Burr

---

For many years futurists and sci-fi authors have been promising us the "smart home" that senses and responds to our needs, automating many daily tasks and allowing us to monitor and control every aspect of the house's operation from anywhere.  This so-called ["Home Automation"][HOMEAUTO] (HA) has been a pipe dream until fairly recently, when the required technology became cheap enough to mass produce.  Unfortunately today's technology still cannot realize some of the more advanced "smart home" concepts -- for example, we don't yet have robots that can perform menial tasks such as cooking, dishes and laundry -- but the technology that we do have lets us do some pretty cool -- and useful -- things.

Commercial HA systems have existed for some time now that can do a wide variety of things.  (Some of these are so complex that they pretty closely approach the sci-fi portrayal of the automated home in terms of capabilities, minus robots of course.)  However they are proprietary, expensive, and require custom installation, so are out of reach for most hobbyists, newbies and the curious.  The good news is that, with HA's recent growth in popularity (it's become *the* topic *du jour* among the tech press these days) many companies are coming out with some very attractive and affordable HA options.  In fact, this sudden growth in HA has not gone unnoticed by the mobile industry, and now major players in the mobile space such as [Apple][HOMEKIT] and [Google][GOOGLE-HA] have announced some big HA initiatives.  This is a smart move, since the two technologies really go hand in hand -- smartphones and tablets serve as perfect control surfaces for interacting with and controlling HA peripherals.

For the longest time, [X-10][X10] was the dominant standard in consumer-grade HA, and is still a major player in the industry.  A wide variety of X-10 compatible controllers exist, giving users the ability to interface with a large selection of household appliances.  However the X-10 standard is quite old (almost 40 years now!) and its communications protocols are slow and inefficient.  Today, while X-10 devices are still quite popular, a number of companies have jumped on the HA bandwagon and have released a slew of really cool and innovative HA products.  Unfortunately this has created a bit of a "Tower of Babel" situation in that these various devices use different protocols and are (in general) not cross-compatible with each other.  Several companies (for example, [SmartThings][SMARTTHINGS] and [OpenHAB][OPENHAB]) have taken the interesting tack of releasing hardware- and/or software-based platforms that "speak" all of the various HA device protocols and therefore essentially act as hubs tying disparate HA devices together -- essentially a "Universal Translator" for HA systems.

One of the many companies entering the HA arena is Belkin, the venerable consumer networking giant.  Their [WeMo][WEMO-BELKIN-PAGE] devices, which connect to your home network via WiFi, are available in several flavors, including a remotely-controllable power outlet (WeMo Switch,) a remotely-controllable wall light switch (somewhat confusingly named the WeMo Light Switch,) a remotely-controllable power outlet with built-in energy usage meter (WeMo Insight Switch,) a remotely dimmable LED light bulb (WeMo LED,) and, oddly enough, a remotely-controllable Crock-Pot (Crock-Pot Smart Slow Cooker with WeMo) which, as silly as it may sound, actually makes sense since a Crock-Pot is a device you'd want to be able to remotely control and monitor.  In addition, Belkin's webcam has been enhanced with WeMo technology, plus they also make available a separate motion sensor; these devices can be used to trigger other WeMo devices, for example turning the lights on when you get home, or turning on floodlights if motion is detected in your yard.  WeMo devices are particularly attractive because they are readily available, reasonably priced and use a simple XML-based REST-like API, and thus can be easily manipulated using Open Source tools.

In this article I will be focusing on the [WeMo Switch][WEMO-SWITCH] since that is the one I have; also it is the cheapest of the WeMo devices.  I will take you through the procedure for setting up and configuring the device, and will end with a few use cases that should give you an idea of the many things you can do with these devices.

#### Getting Started

First you will need to buy a WeMo switch.  They are [available on Amazon][WEMO] which is extremely convenient.  Once your WeMo arrives, *resist the urge to plug it in right away*.  Instead, make a note of the device's MAC address, which is located on a sticker on the back (wall plug end) of the device.

You'll want to assign your WeMos static IP addresses, since you always want to be able to reach them, and with dynamic IP addresses there is a chance that the WeMo might get assigned a different IP address sometimes.  The problem is that WeMo devices *don't* support assigning static IP addresses - they always pick up their IP addresses using DHCP.  Fortunately, most home routers these days have the capability to assign static IP addresses to a given device based on its MAC address.  (Look for a menu option in your router labeled "Static DHCP" or "Reservation DHCP" or something similar.)  Then enter your WeMo's MAC address, and give it a static IP.  Once the router has updated its configuration, you can plug in the WeMo.

Next you will need an iOS or Android smartphone or tablet.  At this time the only way to perform initial setup on the WeMo (give it a name,  tell it how to connect to your WiFi network, etc.) is by using the WeMo app for [iOS][WEMO-IOS] or [Android][WEMO-ANDROID].  (The app is free.)  Once the initial setup is complete, you can control the WeMo from any Linux computer.  If you don't have a smartphone or tablet, you can just borrow a friend's to perform the initial setup.  You may want to consider getting one though; as I mentioned earlier, they make excellent HA controllers, plus they have many other uses as well.  Decent Android tablets can be had for $150-200 nowadays, and used iOS devices aren't that much more.  (If you are willing to set up a separate *unencrypted* network for use exclusively by your WeMo devices, [there is a way][WWS] to set up the WeMo without the aid of a smartphone or tablet.  This dedicated network need not be connected to the Internet or your home network, but any computers that you want to be able to control your WeMos must be able to connect to it.  I would wager that this is something most people won't want to do, so my advice to you is just borrow a smartphone/tablet or consider getting one.)

Access your mobile device's WiFi settings screen.  You should see a new WiFi access point named `"WeMo-*string of random alphanumeric characters*."` Connect to it, then launch the WeMo app.  It will guide you through the setup procedure, which includes assigning the WeMo a "friendly name" (a name to easily identify this particular WeMo) and connecting it to your WiFi network.  Once that's complete, go back to your mobile device's WiFi screen and reconnect to your usual WiFi network.  If all is well, then when you next run the WeMo app, your new WeMo should appear on screen.

(By the way, as you run the setup procedure, the app will probably inform you that a firmware update is available for your new WeMo.  It would be wise to install these whenever they come out, as they are always coming out with bug fixes and improvements.  This is another reason why you should have a smartphone/tablet and the WeMo app; it is the only way that you can run firmware updates.)

Now head on over to your Linux PC, and `ping` the WeMo to make sure it's alive.  Once you have confirmed its aliveness, go off and download, `gunzip` and install [this shell script][WEMO-SHELL-MINE].  (Installation is simple: just copy it to `/usr/local/bin` or `$HOME/bin` or wherever you keep random shell scripts.)  This script is based on one I found at the [Modern Toil blog][WEMO-SHELL] with some bugfixes and additional features.  You'll also need to have the `curl` utility installed; this utility is installed by default on most systems, but if not, it should be available in your distribution's package repository.

Usage is quite simple:

`wemo IP_ADDRESS[:PORT] ON/OFF/GETSTATE/GETSIGNALSTRENGTH/GETFRIENDLYNAME`

where `IP_ADDRESS` is the IP address of the WeMo you wish to control, and `:PORT` (optional) specifies the port to communicate on.  (If unspecified, the script will probe for the correct port.)  The final argument is the command you wish to give your WeMo.  Commands can be entered in uppercase or lowercase.  The following commands are available:  

* `ON` - turns on the device plugged into the WeMo
* `OFF` - turns off the device plugged into the WeMo
* `GETSTATE` - gets the current state of the WeMo (whether it is turned on or off.)  This status is printed to the terminal, and the shell script's exit code is also set based on this information (`0` if off, and `1` if on.)
* `GETSIGNALSTRENGTH` - prints out the signal strength of the WiFi it's connected to.  (Seems to be a percentage, in other words a value of `100` means full signal, `50` means ok signal, etc.)
* `GETFRIENDLYNAME` - prints out the WeMo's "friendly name."  This name can be set during initial setup and is a handy way of identifying your WeMo devices.

(By the way, for you language junkies, there are WeMo libraries for [Perl][WEMO-PERL] and [Python][OUIMEAUX] as well.  In fact, I'd wager that there is probably a WeMo library for whatever language floats your boat, I'm sure.  [Google is your friend.][WEMO-SEARCH])

There is one final tool you might want to take a look at, a free(!) and extremely useful Web service called [IFTTT][IFTTT] ("If This Then That.")  This web service allows you to connect many disparate web technologies together using the simple concept of "**If** *a certain trigger is detected/set off*, **then** *perform a certain action*."  So, for example, you can set up a "recipe" (as they call these formulae) along the lines of, **if** *you get a new email at your Gmail account*, **then** *turn on the flashing police light/siren plugged into your WeMo**.  (Hey, nobody said you couldn't have a little fun with this stuff!)  This service is extremely powerful and very useful for non-HA uses as well, so I recommend you check it out.

Now, armed with the tools you'll need, it's time to check out some use cases.  These are ones that I am actually using, and should give you some ideas as to the cool ways you can use these devices.

#### Use Case #1: The Lights Are On (But Nobody's Home)

We don't travel very often, but when we do we are always nervous about leaving the house unattended.  In general, thieves pass over houses that look like they have people in them (i.e. there is observable activity; lights turning on and off, etc.)  Conversely, they tend to zero in on those houses that always remain dark and look unoccupied.  So whenever we go away, we always set up some light timers to turn on and off lights and certain appliances (TV, radio, etc.) at various times throughout the day and evening.  The problem with these is that they are ridiculously hard to program.  Also, they operate on a fixed schedule - in other words, once you program them to turn on/off at a given time of day, they *always* turn on/off at that exact time.  A determined thief who cases the joint for several days on end could easily notice this pattern and deduce that timers are in use.

With the WeMo, you can easily write up a shell script (or Perl script, or Python script, or whatever) to turn various lights and other devices on or off at a given time.  And, since you have the full power of your Linux computer at your disposal, you can do cool things like randomize the times when things turn on or off, or vary the patterns of what devices to turn on or off to further throw off observant thieves (e.g. one day just turn on and off the lights, but the next day throw the TV and the radio into the mix.)  Finally, since this "not at home" functionality can be easily disabled when not needed (just stop running your shell script,) you can leave your WeMos plugged in all of the time; there's no need to go crawling behind furniture to plug/unplug those stupid timers whenever you go away and return home.

#### Use Case #2: Lazy Man's Christmas Lights of Doom!

Christmas has always been one of my favorite holidays.  Seeing friends and relatives whom I've lost touch with over the years, the wonderful foods traditionally associated with the season, and of course there's the giving (and more to the point, receiving) presents part.  But, being a geek, one of my favorite parts of Christmas is the lights.  Not surprising, since most geeks I know tend to like things with lots of lights on them, especially [blinking ones][BLINKENLIGHTS].  *Setting up* the lights, on the other hand, is *not* my favorite part of the holiday, and is quite frankly something that I would rather not have to deal with at all.  So we foisted this chore off onto someone else.  :)  (Delegation FTW.)  Once the holiday was over, we thought about taking down the lights, but we decided that having to go do it all over again when next Christmas rolled around was too repulsive to bear.  So we decided to just leave them up year-round, but obviously turned off during non-Christmas months.

Anyway our exterior Christmas lights plug in to an outlet located inside our garage, by way of a super long extension cord.  Going out to the garage in the bitter cold to plug them in at dusk and unplug them before going to bed was a real pain.  Sometimes, on especially cold nights, I would conveniently "forget" to unplug them before going to bed.  I thought about setting up a timer to automate this chore, but those things are a real pain.  (See my timer rant in Use Case #1.)  Fortunately we ditched our ancient incandescent light string and replaced it with LED Christmas lights a while ago, so if we did accidentally leave them on, it wasn't a huge energy waste.  Still, it is using energy, if only a small amount.  Plus it looks kinda weird.  Likewise, I was always forgetting to turn off our interior Christmas tree.

Of course, a WeMo would make this task ridiculously easy.  This can be accomplished either with a shell script or IFTTT; IFTTT recipes can use the time of day as a trigger, so you can say, "**If** *it's 5:30 PM*, **then** *turn on the Christmas lights*."  IFTTT can even determine the time that the sun rises and sets for you if you give it your location (not your exact location, just your ZIP code;) so you can say, "**If** *it's sunset*, **then** *turn on the Christmas lights*."

#### Use Case #3: New Email Indicator Light (or alarm, or whatever) of Doom!

If you never want to miss an incoming email, it is pretty trivial to set things up so that a WeMo turns on and off when a new email arrives.  Perhaps you can flash your desk lamp when an email comes in, or briefly turn on a police siren, or something.  If you have the equipment, you can even set up multiple levels of alerts; for example, flash a red lamp if the email is important (comes from your boss or wife) or a white lamp for all other emails.  If you have control over your mailserver, then you can easily set up a `procmail` rule to run the `wemo` shell script to perform these tasks whenever the desired type of email comes in.  If not, then IFTTT can handle that task.

Granted, for most of us this function is perhaps of more value as a novelty than an actual productivity tool.  However, for a deaf or hard of hearing individual, this type of visual alert is an absolute necessity.

#### Use Case #4: Automated "On the Air" Light of Doom!

In my spare time I [podcast][OTAKU] about Japanese animation, food, travel and culture.  A while ago I got myself an ["On the Air" sign][ON-AIR] just like the ones you see in radio and TV studios.  I'll admit it, I did this mostly because it looked cool.  But it actually serves as a useful indication to others that I need things quiet, so that people know not to make loud noises or barge into my room unannounced and mess up my recording.  Of course, it is something that I needed to manually switch on and off, so I was always either forgetting to turn it on, or forgetting to turn it off once I was done recording.

With the WeMo, I set up a [`udev` rule][UDEV-RULE] so that, whenever I plug in my USB microphone, the `wemo` script runs to turn on the "On the Air" sign; likewise, when I am finished recording and unplug my USB microphone, the `wemo` script runs again, this time turning off power to the "On the Air" sign.  Automation FTW!

#### Use Case #5: Automatic Cable Modem Resetter of Doom!

Our home Internet connection is generally fast and reliable... except when it's not.  Every now and then, for whatever reason my cable modem decides to go catatonic and suddenly stops communicating with the outside world.  Power cycling the cable modem usually brings it back from the dead.  This requires me to stop whatever it is I'm doing, wander over to the NOC (my name for the part of my office where all the networking gear is,) and power cycle the cable modem.  Annoying, yes, but not overly so.  (Honestly, I find the hue and cry of "The Internet is down!!!" from housemates and visitors much more annoying.)  But when I'm away from home, this problem turns from being a minor annoyance, to being a critical showstopper.  I frequently need to access my home computers while I'm on the road.  For one thing, my VPN server, which I use whenever I am traveling and am using a potentially unsafe network, is located on a machine at home.  I also often need to log in to and remotely control one of my machines at home, or to fetch a file that I need from my NAS, and so on.

I struggled at trying to find a solution to this problem for quite a while.  Detecting a net outage was the easy part: I just set up a script that ran periodically from `cron` that tries to `ping` a "reliable" Internet server (one that is known to be up most, if not all of the time; Google's DNS server at `8.8.8.8` is a good candidate.)  If the `ping` fails, then the script assumes that the net connection is down.  The problem then became how to remotely power cycle the modem?  Since we don't yet have the full-on HA with robots, a robotic solution was right out.  I thought about acquiring an [IP power controller][IP-POWER].  These devices are often installed in remote locations such as radio and TV broadcast towers and allow engineers to monitor power usage and remotely power cycle problematic equipment.  However these devices are extremely pricy and way too fancy for my simple needs.  Then, one day, I was ranting and raving about my predicament to a friend, and he was like "Dude, just get a WeMo."  (This is, in fact, how I first encountered the WeMo.)  With the WeMo in the equation, my script was complete: when it detects a network outage, it commands the WeMo attached to my cable modem to power cycle itself.  This setup works like a charm and I have never had an unrecoverable network outage since.  Feel free to [download][NET-TESTER] and use it yourself.  Simply edit the script to suit your particular needs (it is liberally commented) run this script periodically out of `cron` and you're all set.

#### Use Case #6: Automated Pool Reinflater of Doom!

A while ago I picked up a small above-ground swimming pool during a super closeout sale.  It's a popular attraction when our friends with kids come over for a visit, plus it's nice to float around in when the weather turns uncomfortably warm (which has been happening more often as of late.)  This particular type of above-ground pool consists of a vinyl floor and walls, and an inflatable ring at the top of the side walls which helps to hold the walls up and prevents water from spilling over.  Unfortunately, this inflatable ring recently developed a slow leak that has proven impossible to locate, even using the old "spray it with soapy water and watch for bubbles" trick.  So every other day or so I have to reinflate the ring in order to maintain the pool's structural integrity, or else risk a flood of Biblical proportions.  After a couple weeks of doing this (or, more to the point, *forgetting* to do this) I cobbled together an automated solution using mostly parts I had lying about.  I took the [air pump][PUMP] that I already had and attached its hose to the pool ring's air inlet valve, plugged the pump into a WeMo, and wrote up a quick `cron` job that turns the pump on for about 10 seconds every other day (just long enough to reinflate the ring to full capacity.)  Unfortunately there was nothing in the system to prevent air from leaking back out through the valve when the pump wasn't powered on.  So I devised a one-way air valve (allowing air to flow only into the pool ring) using a [PVC check valve][VALVE] combined with some [PVC tubing][PVC], all put together and sealed using liberal amounts of [duct tape][DUCTTAPE].  [This setup][INFLATER-PIC-1] is admittedly [a bit ugly][INFLATER-PIC-2], but it works amazingly well, and is in fact airtight.  Thanks to this solution, we haven't found the need to construct an ark in our backyard and gather up as many animals as we could find.

### Conclusion

Home Automation is not only useful, it's just plain *fun*.  And, thanks to a plethora of available devices and falling prices, it is within reach of everybody.  Now go forth and automate!

---

*[Donald Burr][DBURRBLOG] has been using -- and abusing -- computers and gadgets practically since the day he was born.  (Rumor has it he was born with a keyboard in one hand and a mouse in the other.)  He is an [avid amateur app developer][DBURRAPPS] and is [available for hire][CONTACT] if you need a little help getting started in app writing.  When he's not geeking around with tech, he can be found blogging and podcasting about Japanese animation and culture at [Otaku no Podcast][OTAKU].  He can be found on the Twitters as [@dburr][DBURRTWITTER].*

[HOMEAUTO]: http://en.wikipedia.org/wiki/Home_automation "HA"
[X10]: http://en.wikipedia.org/wiki/X10_(industry_standard) "X-10"
[HOMEKIT]: https://developer.apple.com/homekit/ "HomeKit"
[GOOGLE-HA]: http://www.forbes.com/sites/brucerogers/2014/07/08/apple-and-google-dominate-internet-of-things-influence-with-home-automation-efforts/ "Google HA"
[OPENHAB]: http://www.openhab.org "OpenHAB"
[SMARTTHINGS]: http://www.smartthings.com "SmartThings"
[UT]: http://en.memory-alpha.org/wiki/Universal_translator "Universal translator"
[WEMO-BELKIN-PAGE]: http://www.belkin.com/us/Products/home-automation/c/wemo-home-automation/ "Belkin's WeMo page"
[WEMO-SWITCH]: http://www.belkin.com/us/p/P-F7C027/ "WeMo Switch"
[WEMO]: http://www.amazon.com/dp/B00BB2MMNE/?tag=otakunocast-20 "WeMo device"
[WEMO-IOS]: https://itunes.apple.com/us/app/wemo/id511376996?mt=8&at=10lrq4 "WeMo App for iOS"
[WEMO-ANDROID]: https://play.google.com/store/apps/details?id=com.belkin.wemoandroid&hl=en "WeMo App for Android"
[WEMO-PERL]: https://github.com/ericblue/Perl-Belkin-WeMo-API "Perl-Belkin-WeMo-API"
[OUIMEAUX]: https://github.com/iancmcc/ouimeaux "Ouimeaux"
[WEMO-SHELL]: http://moderntoil.com/?p=839 "WeMo shell script"
[WEMO-SHELL-MINE]: https://dl.dropboxusercontent.com/u/169813/wemo.gz "WeMo shell script (my version)"
[WEMO-SEARCH]: http://lmgtfy.com/?q=wemo+scripting+language+support "WeMo search"
[IFTTT]: http://ifttt.com/ "If This Then That"
[UDEV-RULE]: http://unix.stackexchange.com/questions/28548/how-to-run-custom-scripts-upon-usb-device-plug-in "Udev rules"
[ON-AIR]: http://www.amazon.com/dp/B009CF5VUS/?tag=otakunocast-20 "On the Air sign"
[NET-TESTER]: https://dl.dropboxusercontent.com/u/169813/net_tester.gz "Net Tester script"
[WWS]: http://hackaday.com/2013/02/23/wemo-without-a-smartphone/ "WeMo Without a Smartphone"
[BLINKENLIGHTS]: http://en.wikipedia.org/wiki/Blinkenlights "Blinkenlights"
[PUMP]: http://www.amazon.com/dp/B000FE7J0A/?tag=otakunocast-20 "Air Pump"
[VALVE]: http://www.amazon.com/dp/B00B95U5NW/?tag=otakunocast-20 "PVC check valve"
[PVC]: http://www.amazon.com/dp/B0046ECKZ4/?tag=otakunocast-20 "PVC tubing"
[DUCTTAPE]: http://www.amazon.com/dp/B001HT720O/?tag=otakunocast-20 "Duct tape"
[DBURRBLOG]: http://DonaldBurr.com/ "Donald Burr's Blog"
[DBURRAPPS]: http://DonaldBurr.com/apps/ "Donald Burr's Apps"
[CONTACT]: http://donaldburr.com/contact-me/ "Contact Me"
[OTAKU]: http://otakunopodcast.com/ "Otaku no Podcast"
[DBURRTWITTER]: http://twitter.com/dburr/ "Donald Burr on Twitter"
[IP-POWER]: http://www.aviosys.com/9258st.html "IP Power"
[INFLATER-PIC-1]: https://www.dropbox.com/s/0dqw1i57fw0thyb/inflater_1.JPG "Inflater pic #1"
[INFLATER-PIC-2]: https://www.dropbox.com/s/hqg2fcshzva5sr9/inflater_2.JPG "Inflater pic #2"
