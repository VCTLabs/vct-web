################################################################
Third Early Adopter Release of SailfishOS (1.0.7.16) for Nexus 4
################################################################

:date: 2014-06-30
:author: Stephen Arnold
:tags: android, cyanogenmod, jolla, sailfishOS, Nexus 4
:category: news
:slug: sailfish_prerelease
:summary: third early adopter release of SailfishOS (1.0.7.16) for Nexus 4

As the title and the announcement below says, this is now available for 
Nexus4 and other devices (see the upstream site for details).  Follow the 
steps below to flash your device and you should see a nice sailing ship 
on the next boot.

Although it runs on top of an "android" ROM the gesture-based interface 
is altogether different, and sweet once you get used to it.  Try it and see...


Email Announcement
++++++++++++++++++

Dear early adopter of SailfishOS for Android devices. This is important - 
read this whole mail through and follow all steps exactly as written.

IMPORTANT: If you choose to publish this mail through blogs, news sites, 
forums, or others, quote it as-is and in complete form ONLY, or people's 
devices may be at risk.

We're happy to publish the third Early Adopter Release of SailfishOS 
(1.0.7.16) for Nexus 4 (mako) to you.

We are still working on the SailfishOS Hardware Adaptation Development 
Kit, which describes how to port SailfishOS to existing devices based on 
CyanogenMod 10.1. Newer versions of CM will be supported eventually. 
We'll publish the HADK in the very near future.

This installation image is for early adopters only, meaning we know that 
some things are not functional or perhaps even broken -- please see the 
release notes below. We are excited to get all of you properly included 
in the early stages of the project. Do note that this SailfishOS image 
is strictly for personal and non-commercial usage only.

We've prepared a 'demo' version of the image which contains the kind of 
preinstalled 'marketing' content and the core apps used for 
demonstrations - this helps you quickly get a feel for all the 
interactions that are avalable on a device that has been used for a 
while but isn't really what you want for personal use. You can however 
cleanly remove the demo content.

We want to build a community around SailfishOS for Android devices that 
is based on mutual trust and respect for what we are all doing. Hence -- 
we ask that whenever you do screenshots, videos, forum or blog posts 
(and we're happy if you do!) or the like, you emphasise that this is an 
under-development snapshot and not a final product release.

It is important for Jolla that the correct expectations are set for 
those who might be users of the final product -- and that they 
understand what they see is not a released product. If you do demo 
videos, you can take advantage of our new 'demo content' image that has 
pre-set contacts/imagery/messages/etc to show full functionality of 
SailfishOS.

WARNING: Modifying or replacing your device’s software may void your 
device’s warranty, lead to data loss, hearing loss, hair loss, financial 
loss, privacy loss, security breaches, or other damage, and therefore 
must be done entirely at your own risk. No one affiliated with this 
project is responsible for your actions but yourself. Good luck.

NOTE: You will lose your on-device data (including /sdcard), so make a 
proper backup and make sure to copy that backup to your PC.

NOTE: Make sure to read all the release notes below. Please DO NOT 
contact Jolla Care for any issues encountered with this Early Adopters 
build, instead use communication channels listed below.

To install this release of SailfishOS on a Nexus 4 device:

1. Install adb and fastboot

  a. Debian/Ubuntu: apt-get install android-tools-adb android-tools-fastboot
  b. Fedora: yum install android-tools
  c. Mac OS X: Install Homebrew from http://brew.sh/, then: brew install android-platform-tools
  d. Windows: See http://wiki.cyanogenmod.org/w/Doc:_fastboot_intro for instructions

2. Install Android 4.2.2 (JDQ39) to your Nexus 4

  a. Instructions here: https://developers.google.com/android/nexus/images#instructions
  b. Download links can be found here: https://developers.google.com/android/nexus/images#occamjdq39

3. Download CyanogenMod 10.1.3 for your Nexus 4

  a. Perform Factory Reset and wipe contents of the /data/ partition in case of leftovers from previous ROMs
  b. The file you want to download is cm-10.1.3-mako.zip
  c. Download links can be found here: http://wiki.cyanogenmod.org/w/Install_CM_for_mako

4. Download the SailfishOS for Android image for "mako"

  a. The file you want to download is http://releases.sailfishos.org/sfa-ea/sailfishos-mako-release-1.0.7.16-EA3.zip
  b. Another flavour filled with demo content: http://releases.sailfishos.org/sfa-ea/sailfishos-mako-release-1.0.7.16-EA3-demo-content.zip

5. Install CyanogenMod 10.1.3 on your Nexus 4 

  a. Follow the instructions at: http://wiki.cyanogenmod.org/w/Install_CM_for_mako

6. After flashing the "cm-10.1.3-mako.zip" file, flash the SailfishOS .zip file in the same way ("on top of it")

7. Reboot bootloader, SailfishOS should boot and be visible

We recommend reading through http://jolla.com/guide/ -- some parts may not apply to Nexus 4

If you want to go back to normal CyanogenMod:

a. Boot into recovery mode
b. Choose "Wipe data / factory reset"
c. Flash cm-10.1.3-mako.zip
d. (to go back to SailfishOS, flash the SailfishOS .zip on top of it)

If you want to go back to stock Android:

a. Download the stock image from https://developers.google.com/android/nexus/images#occam
b. Extract the package and follow the instructions for reflashing/re-locking

To SSH into your device via USB (Linux)

1. Enable remote connection in Settings->System->Developer mode
2. Set your USB interface on host machine to IP 192.168.2.2
3. ssh nemo@192.168.2.1
4. Use the password from developer mode to log in
5. Use the 'devel-su' command with the same password in order to gain root
6. To SSH over WLAN, use IP listed in developer mode under "WLAN IP address"

Read Sailfish OS release notes: https://together.jolla.com/question/45064/release-notes-software-version-10716-saapunki/

Release notes/Known issues in EA3:

* EXPERIMENTAL: Jolla Store is now available, you'll need to register with your Jolla Account

  - NOTE: Booting Nexus 4 with SIM first, and then removing SIM (or vice versa) may cause Jolla Store to see it as two different devices and cause potential breakage. Please stick to either SIM available or not when running SailfishOS on Nexus 4.

    + There may be a bug with oFono RIL support that makes it not report IMEI value causing this and will be sorted out in a later update.

  - DISCLAIMER: Using Jolla Store with Jolla Account might break applications on your other devices, use it at your own risk!
  - Android support is not available from the Store, even if you can see Android apps listed (those will be removed eventually from store view)
  - This functionality means that image comes with only minimal set of pre-installed apps. Use Store to download the ones you need.

* The backlight is dark during first launch, but can be fix by switching the currently-not-working ambient light sensor off (uncheck Settings->System->Display->Adjust automatically)
* When display is blanked, power management sets WLAN to the lowest speed state

  - Can be noticed in a SSH-over-WLAN session
  - Chat notifications may arrive with a slight delay

Fixes after EA2:

* Watermark removed
* Phone-call audio volume can now be changed with the help of volume buttons
* Improved responsiveness when waking phone up with the power button
* Settings->System->Developer Mode or About Product do not freeze anymore
* Reverted to the original (non-Silica) Fingerterm

Fixes after EA1:

* Phone-calls with audio work
* Timers and alarms (with device powered on) work
* HTML5 video+audio works in Browser (tested splash on http://jolla.com )
* Update is based on SailfishOS version 1.0.5.16

Release notes/Known issues in EA2:

* To securely power off the device, during its boot-up keep Volume Down pressed to enter bootloader mode. Using volume keys, select "Power off" option, then press the Power key
* If not auto-detected from SIM, set-up mobile internet data settings via Settings->System->Mobile network->(long tap on the first toggle-item under "Mobile data" section)->(enter settings given by your operator)

Nexus4-specific known issues reported by the adopters (in EA2):

* Chinese text input not working
* Localhost name is shown as Jolla
* Switching between the online and offline status in the status information setting takes very long and often doesn’t switch properly
* Google contacts which are put together with different information, are now split up into several contacts in Sailfish
* The battery display seems to be a bit buggy because it loses about 15% from one second to another
* The calendar overview when filled with events seems to be a bit laggy
* The email push is not working correctly, I do not receive any emails until I push the refresh button
* Splitting words in the German translation: e.g. in the open apps on the home screen it says: "Kurzzeitmesse" and in the next line the missing "r"
* NOTE: all other Sailfish OS issues have already been reported on TJC - http://together.jolla.com - and many of them were fixed in this 1.0.5.16 release

Release notes/Known Issues in EA1:

* Developer mode is activated at all times
* There has been no throughout testing of telephony related functionality (roaming, airplane mode, etc) and any use of this functionality is at your own risk
* Sensors, Device lock, Reset device, Bluetooth, USB control + MTP, Bluetooth, WLAN hotspot, Camera(photography, video recording), and video playback is not supported in this release
* The image SW is not currently upgradeable, nor is any typically licensed multimedia codecs (MP3, etc), HERE maps, Android application compatibility layer, or word prediction for virtual keyboard preinstalled

* This image does not include any typically licensed multimedia codecs (MP3, etc), HERE maps, Android application compatibility layer, Microsoft Exchange support, or word prediction for virtual keyboard preinstalled
* It is not possible to double-tap to wake up the device
* Powering off device puts it into a state of deep slumber; possible to get out of by holding power button and volume down key with a bit of persistence
* Fingerterm keyboard is not at its best due to the portrait-only mode
* FPS drop while scrolling in homescreen due to non-batching when rendering of application icon grid
* Icons/graphics appear unproportionally small in browser toolbar, time select widget, and Settings favourite icons
* Multiboot/Multirom is not supported yet but we're happy if you would like to teach/help us

We will all meet in #sailfishos-porters (note, new location) on irc.freenode.net and please use us (thp, alterego, Stskeeps, lbt, sledges) to work together, report any bugs, graphical glitches or missing functionality that you find, which are not included in the release notes above. You can also find the hardware adaptation source code at http://github.com/mer-hybris .

You are also welcome to participate in threads at http://forum.xda-developers.com/nexus-4/general about Nexus 4 and SailfishOS as well as for more general SailfishOS topics at http://forum.xda-developers.com/jolla-sailfish/general

::

 Best regards,
 Carsten Munk (Stskeeps) on behalf of the SailfishOS for Everyone team.
 Chief Research Engineer @ Jolla


