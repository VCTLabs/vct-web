##################################################################
 Stock and Custom PiTFT Kernel Options with Your Choice of rootfs
##################################################################

:date: 2014-10-22
:author: Stephen Arnold
:tags: Gentoo, Debian, Linux kernel, Raspberrypi, PiTFT, LCD display
:category: howto
:slug: pitft_kernel
:summary: Understand and customize your PiTFT kernel config

This is primarily useful if you have one of the Adafruit (or similar) small TFT/LCD displays for Raspberrypi (one possible non-Adafruit vendor is SainSmart).  The Adafruit displays are available in several sizes and configurations, both touch and non-touch, some come in kit or assembled form, and some are available in both Capacitive and Resistive Touch (CT / RT) varieties. The particular display tested here is the Adafruit 2.8 inch PiTFT resistive touchscreen display.  It's just a bit smaller than the bezel on the Pibow acrylic case, with the button pads exposed along the "bottom" of the board (which needs a default 90 degree rotation argument passed to the kernel).

Since the upstream raspberrypi kernel and firmware does not yet have support for these devices, you'll need to do one of the following: download a new rootfs or kernel image, update your existing raspbian image using the Adafruit script, or build your own custom kernel using either the modified Adafruit kernel source or adding the fbtft device drivers to your own kernel source and rebuild.  The current support is still maintained in the `Adafruit forks`_ of the `raspberrypi.org repos`_ on Github.

.. _Adafruit forks: https://github.com/adafruit
.. _raspberrypi.org repos: https://github.com/raspberrypi

The best documentation I know of for assembling and testing the Adafruit displays are on the Adafruit site, specifically `Adafruit PiTFT 2.8 inch Touchscreen Display for Raspberry Pi`_ for the display described here.

.. _Adafruit PiTFT 2.8 inch Touchscreen Display for Raspberry Pi: https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/overview

Easy Raspbian Install/Upgrade
=============================

If you already have a recent Raspbian install, the easiest way is to use the upgrade script provided by Adafruit.  Since it's a Bash shell script, you can read through it fairly easily to see what it will do.  Download the script from the Easy Install section and follow the steps in the excellent Adafruit document linked above.

.. admonition:: Note

   If you don't have a current Raspbian image, then download the `Adafruit image here`_ and burn it to a card (no extra configuration should be required).

.. _Adafruit image here: http://adafruit-download.s3.amazonaws.com/PiTFT28R_raspbian140620_2014_08_25.zip


If you'd rather do things by hand and/or leave things largely unmodified, then you can manually upgrade your kernel and firmware by cloning the Adafruit firmware repo on Github and manually update your running card as follows, after logging into your pi::

    $ cd ~/  
    $ sudo mount /boot  # make sure /boot is mounted
    $ git clone https://github.com/adafruit/rpi-firmware.git
    $ sudo cp /boot/kernel.img kernel.bak
    $ cd firmware
    $ sudo cp -v boot/* /boot/
    $ sudo cp -v extra/Module.symvers /boot/
    $ sudo cp -av modules/3.15.8+ /lib/modules/

Depending on your actual hardware, the above kernel config maybe missing the correct config to work with the modules and options documented in the Adafruit guide.  If the latest Adafruit kernel does not load the fbtft_device module correctly, then download and unpack the .deb packages in the script and manually install the 3.12.x kernel using the above process.

At some point later you can update your userland (vcgraphics) software as well, but for now we only need to test the kernel and display.  This may very well suffice for your needs, so feel free to stop here and finish the config manually (or maybe go back and run the install script).  The rest of this document is mainly for building your own custom kernel; if that's what you want to do keep reading...

Custom PiTFT Kernel and Rootfs
==============================

Currently the "upstream" for Adafruit hardware support are their repos on Github (of which there are many).  In this case, the important ones are their forks of the "official" raspberrypi kernel source and firmware, along with the fbtft framebuffer drivers (which get automatically included as a submodule in the kernel source repo).

 * https://github.com/adafruit/adafruit-raspberrypi-linux
 * https://github.com/adafruit/rpi-firmware
 * https://github.com/adafruit/adafruit-rpi-fbtft

If you're running Gentoo, you can add the following overlay and use the adafruit-raspberrypi-sources ebuild and ignore the manual clone steps for the kernel, et al, in the next subsection.  For Gentoo::

    $ cd /usr/local/
    $ git clone https://github.com/sarnold/arm.git

Add /usr/local/arm to your PORTDIR_OVERLAY in make.conf, then::

    $ echo "=sys-kernel/adafruit-raspberrypi-sources-3.15.9999 **" >> /etc/portage/package.accept_keywords
    $ sudo emerge adafruit-raspberrypi-sources

For other distros, continue with the manual steps below.

To build your own kernel and update your boot firmware, you'll need to clone the first two repos above (if you already have the firmware repo, you can omit the second one below).  You'll also need to either clone recursively or do the git submodule dance to actually bring the fbtft source files into the drivers/video/fbtft directory.  Note the following steps assume you're either building native on the Pi itself, or in an appropriate ARM chroot or virtual environment.  If you need to cross-comppile the kerrnel, then you can follow the usual `Raspberrypi`_ cross-compile process (you will of course need an appropriate cross toolchain and build environment).

.. _Raspberrypi: http://elinux.org/Raspberry_Pi_Kernel_Compilation

::

    $ sudo -i
    # git clone --recursive https://github.com/adafruit/adafruit-raspberrypi-linux.git
    # git clone https://github.com/adafruit/rpi-firmware.git
    # cd adafruit-raspberrypi-linux
    # git checkout rpi-3.15.y -b rpi-3.15-working   # create local branch
    # cp arch/arm/configs/adafruit_defconfig .config
    # sed -i -e "s/CONFIG_DMA_BCM2708=m/CONFIG_DMA_BCM2708=y/" .config
    # sed -i -e "s/CONFIG_DMA_VIRTUAL_CHANNELS=m/CONFIG_DMA_VIRTUAL_CHANNELS=y/" .config
    # make oldconfig

There are only two active branches in the adafruit-raspberrypi-linux repo, rpi-3.10.y and rpi-3.15.y so make sure you've checked out the branch you want (note 3.10 is default).

Now you can proceed with building the default kernel config, however, you may want to modify it further to suit your own needs (eg, to enable the zram block device or the latest nftables support).

.. admonition:: Note

   The adafruit-raspberrypi-sources ebuild takes care of the above two sed commands for you, otherwise you must do it manually.  This is very important or else the fbtft_device module will not load correctly when following the Adafruit instructions.

Once you're ready, proceed as you normally would to build/deploy a kernel::

    # make menuconfig
    # make -jN
    # make modules_install
    # mount /boot
    # cp /boot/kernel.img ~/kernel.bak
    # cp arch/arm/boot/zImage /boot/kernel.img
    # cp Module.symvers /boot/

If you didn't follow the above steps to update your boot files, you should do that now (be careful not to clobber your new kernel.img file).  Also, with newer u-boot, the above (compressed) kernel zImage file should work fine, but if it doesn't boot use the (uncompressed) Image file instead (note that you only need one, not both, just rename either one to "kernel.img" when you copy it to /boot).

Now is a good time to reboot and test the new kernel (however, the display won't really be usable until we finish the configuration).  Make sure all your normal services are working and everything looks nominal.  If not, copy your backup kernel from above back to /boot/kernel.img and try reverting any suspect config changes (you can always start from the defconfig again if necessary).

As mentioned, we still need to make the required config changes for the framebuffer modules, boot arguments, environment variables, etc.  The required changes are all documented in the Adafruit guide above, as welll as in the bash install script for raspbian.  You may or may not want all of the changes, depending on how you plan to use your display.  For example, if you want to display specific output or other data, simiilar to how you might use one of the 2-line character LED displays, then you probably don't want to use it as a login console.  It all depends on *your* requirements, so we'll walk through each major change below.

Although the following configuration snippets are strictly "optional", if you want your display to actually *do* anything besides light up with a white backlight, then you'll at least want to configure the module parameters for your display device, and (optionally) autoload the modules on boot.

Configure Modules
=================

Raspbian (and similar) will load the modules specified in /etc/modules, while Gentoo uses /etc/conf.d/modules::

    modules="i2c-dev bcm2708-rng snd-bcm2835 spi-bcm2708 i2c-bcm2708 fbtft_device"

The last three are required for the display device, with the following default parameters.  Feel free to experiment (within limits) with the clock speed and rotation.  Most distros use various conf files in /etc/modprobe.d to configure modules; in this case the `Adafruit Software Install section`_ asks you to create /etc/modprobe.d/adafruit.conf with the following contents:

::

    options fbtft_device name=adafruitrt28 rotate=90 frequency=3200000

Note the "name" parameter is specific to the 2.8 inch RT display, while the others are recommended defaults (90 degree rotation puts the button pads along the bottom of the display).  These values should take effect whether modules are loaded manually or at boot time.

.. _Adafruit Software Install section: https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/software-installation


Configure Kernel Command Line
=============================

Modifying the command line will switch the default console device to the small display on boot, so depends on how you want to use the display.  With the options below, the display will switch when the fbtft_device module loads (how much of the boot process you can see depends on the size of the kernel log buffer).  If you want the console display to switch, then you'll need to edit /boot/cmdline.txt (which is simply a single line of kernel parameters).  Add the last two parameters to whatever is currently there as shown::

    dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait fbcon=map:10 fbcon=font:VGA8x8

Be sure it stays all on one line of text.  In Gentoo you can change fonts in your consolefont config, otherwise use "dpkg-reconfigure console-setup" to change your console font.

Configure Xorg
==============

Xorg needs to know both which display to use and what the touchscreen calibration values are.  To get started, create a default set of "touch" input values in /etc/X11/xorg.conf.d/99-calibration.conf and use the following values::

    Section "InputClass"
    Identifier "calibration"
    MatchProduct "stmpe-ts"
    Option "Calibration" "3800 200 200 3800"
    Option "SwapAxes" "1"
    EndSection

You can recalibrate later for more accuracy.  Somewhere in your environment (either user or system) you also need to set FRAMEBUFFER=/dev/fb1 so X will know where to point the display output.  In Raspbian, you can set that in ~/.profile or /etc/profile and will also probably need to move the fbdev-turbo config out of /etc/X11/xorg.conf.d/.

Configure Udev
==============

The actual touchscreen driver for the 2.8 inch RT display will load on its own, however, the following udev rule is recommended.  Add the rule file /etc/udev/rules.d/95-stmpe.rules with the following contents::

    SUBSYSTEM=="input", ATTRS{name}=="stmpe-ts", ENV{DEVNAME}=="*event*", SYMLINK+="input/touchscreen" 

Once you reload the module, the output of "ls -l /dev/input/touchscreen" should be symlink to an eventN device.

Manual Calibration
==================

Follow the `Touchscreen Install and Calibration section`_ of the Adafruit documentation to install the tools and manually calibrate your touchscreen (they also have an "auto" calibration script).

.. _Touchscreen Install and Calibration section: https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/touchscreen-install-and-calibrate

Testing Video Playback
======================

Follow the `Playing Videos section`_ of the Adafruit documentation to test your display with a small animated video.  Since mplayer doesn't use the accelerated RPi graphics libs, it seems to be right on the edge of being able to play the test video correctly (ie, with audio and video in sync and without dropping too many frames).  It seems to play correctly in Raspbian, however, in Gentoo the audio was always several seconds delayed without additional configuration options in ~/.mplayer/config:

::

    lavdopts=lowres=1:fast=1:skiploopfilter=all
    vfm=ffmpeg
    
    # ao is the audio output and should be pulse if using pulseaudio
    ao=alsa
    
    # af is the audio filter, using re-sampling in this case, to provide audible sound
    #af=lavcresample=44100

    # Allow framedropping might reduce video quality, but allows video and audio to stay synced
    framedrop = yes

    fps=24.0

The key option in this case is fps=24 for smooth/synced playback.  The CPU utilization is just a little over 50%.  Use the above config options with the following command line::

    $ mplayer -vo fbdev2:/dev/fb1 -x 240 -y 320 bigbuckbunny320p.mp4

With the above parameters the test video would play with audio and video in sync and decent quality for both audio and video.  Note that audio quality can suffer if running from a noisy power source (such as a cheap battery).  If audio is noisy, try a decent quality power brick.

.. _Playing Videos section: https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/playing-videos
