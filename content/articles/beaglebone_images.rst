###########################################################
Maintaining Your Stock BeagleBone Angstrom Images and Demos
###########################################################

:date: 2014-09-14
:author: Stephen Arnold
:tags: kernel, u-boot, Gentoo, Angstrom, BeagleBone, bonescript
:category: howto
:slug: beaglebone_images
:summary: Update or fix your BeagleBone Angstrom install

In a previous news article, we described building and deploying the latest U-boot
and Linux kernels on several armv7 machines, `including a BeagleBoneBlack`_.

.. _including a BeagleBoneBlack: armv7_kernels.rst

In this "HOWTO" we'll talk about restoring/upgrading/maintaining your stock
Angstrom install on both BeagleBone White and Black.  Why would we do this?
Several reasons, but typically to restore the default install or upgrade to
the latest build.  The nice thing about BeagleBoneBlack is that Angstrom lives
on the eMMC and you can always boot whatever you need off the SDCard.  Since
BeagleBoneWhite only has an SDCard, you simply swap your default 4 GB card
with Angstrom for another (possibly larger) card running your OS/Distro of
choice.  The two models have slightly different bleeding-edge patch sets
and hardware interfaces, but otherwise are very similar:

 * BeagleBoneBlack Rev A6A - http://eewiki.net/display/linuxonarm/BeagleBone+Black
 * BeagleBoneWhite Rev A6 - https://eewiki.net/display/linuxonarm/BeagleBone
 * BeagleBoargd.org info - http://beagleboard.org/static/beaglebone/latest/README.htm
 * Bonescript and documentation repos - https://github.com/jadonk

Out of the Box
==============

Depending on when it was produced/packaged, your BeagleBone will most likely
come with one of the Angstrom builds for SDCard and/or eMMC install.  There
are some builds which are supposed to support both White and Black, as well
as an SDCard image for "flashing" the eMMC on the Black.  There are changes
in both the Bone101/Cloud9 IDE and Gnome desktop config in the various builds
so it's probably worth it to try a couple of them (some seem to have a less
optimal Cloud9 bonescript environment than others).

The recommended builds are given below, "latest" for Black, and a slightly
older one for White (recommended for a good new user experience).  Simply
download the desired image, either from the archive or the latest link, and
use the standard tools (dd or WinDiskImager) to uncomnpress and write the
image to your SDCard device (be sure and select the .img file unless you
want to manually create your card and deploy the rootfs, etc).  Use the
links above for the manual method, otherwise download one or more of the
following images:

 * `Latest eMMC flasher for Black`_
 * `Recommended SDCard image for White`_
 * `Archive of OS, u-boot, and kernel images`_
 * `Latest OS images for all Beagle boards, both Angstrom and Debian`_

.. _Latest eMMC flasher for Black: http://downloads.angstrom-distribution.org/demo/beaglebone/archive/BBB-eMMC-flasher-2013.09.07.img.xz
.. _Recommended SDCard image for White: http://downloads.angstrom-distribution.org/demo/beaglebone/archive/Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.05-beaglebone-2012.11.22.img.xz
.. _Archive of OS, u-boot, and kernel images: http://downloads.angstrom-distribution.org/demo/beaglebone/archive/
.. _Latest OS images for all Beagle boards, both Angstrom and Debian: http://beagleboard.org/latest-images/

.. admonition:: Note

   The BeagleBoneWhite Rev A6 I received came with the above 2012.11.22 image on a 4 GB SDCard.  The
   Bone101 slideshow is highly recommended for new users.

Although these kernels are fairly recent, they are several versions
behind the latest kernel source (typically 3.10.x rather than 3.16.x)
and do not yet support HDMI out.  A future HOWTO will discuss building
your own OS images with custom kernels, etc.

BeagleBoneWhite Cloud9 IDE and Bone101 Web Tutorial
===================================================

One of the hardware differences on the White is a built-in USB serial
converter on the mini-USB port, so as long as your desktop kernel (or
other OS drivers) is configured properly, you should have a serial
console as soon as you plug in the USB cable (use minicom or putty
to connect at 115200,8N1, no flow control).  However, even more
interesting is the web server and Cloud9 IDE running on the network
interface, which should configure itself if you have DHCP (if not
you'll need to configure it manually via the serial console (login
as root with no password).

Download one of the Cloud9-IDE build images and write it to a card::

 $ wget http://downloads.angstrom-distribution.org/demo/beaglebone/archive/Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.05-beaglebone-2012.11.22.img.xz
 $ xz -d Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.05-beaglebone-2012.11.22.img.xz
 $ sudo dd if=Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.05-beaglebone-2012.11.22.img of=/dev/sdX bs=4M

(where sdX is your SDCard device)

Once your BeagleBoneWhite is on the network, use Avahi/Zeroconf or
the serial console to discover the IP address, then point your browser
at the IP address of your White (anything modern except IE should work).
You should see the Bone101 introduction, which will introduce you to,
and allow you to interact with, your new BBW.  There are bonescript
demos and hardware diagrams, including details on the board itself and
all the pinouts.  Click on the Cloud9 IDE link and try some of the
demo scripts (note the BlinkLED demo calls out an external LED, but
should also trigger the onboard USR3 LED).

BeagleBoneBlack eMMC Flashing Tool w/ Latest Cloud9 IDE and Documentation
=========================================================================

In addition to the bootable micro-SDCard slot, the Black also has onboard
eMMC flash (not technically true flash, but consider it like a faster and
built-in SDCard).  The Black should come out of the box with one of the
recent builds listed above; if yours is older or corrupted and you'd like
to update to the latest "official" build (including the latest Cloud9 IDE
and documentation) then perform the following steps.  

Download the latest Cloud9-IDE build image and write it to a card::

 $ wget http://downloads.angstrom-distribution.org/demo/beaglebone/archive/BBB-eMMC-flasher-2013.09.07.img.xz
 $ xz -d BBB-eMMC-flasher-2013.09.07.img.xz
 $ sudo dd if=BBB-eMMC-flasher-2013.09.07.img.xz of=/dev/sdX bs=4M

(where sdX is your SDCard device)

.. admonition:: Note

   If your BeagleBoneBlack is a Rev C, it should have a 4 GB eMMC,
   and you can use one of the larger flash images.

Boot the Black with the new card and wait (you can connect a network
cable if you like; this will allow you to login and check the status).
Once the kernel loads, the LEDs will blink in their default config:

 * USR0 - blink in a heartbeat pattern
 * USR1 - light during microSD card accesses
 * USR2 - light during CPU activity
 * USR3 - light during eMMC accesses

The USR3 LED will (for the most part) stay lit while the flashing
script does the formatting, unpacking, and configuration of the
rootfs.  When this process is finished, all 4 USR LEDs will light
up solid.  You can then power down and remove the card, then boot
your new Angstrom install.

BeagleBone USB/Ethernet Network Configuration and Automation
============================================================

Both Black and White BeagleBones default to DHCP for the ethernet
interface, so the IP address will depend on your own local network
setup.  While the White has the serial console on the mini USB
interface, the Black has the same port configured as a USB gadget
interface.  IF your kernel is properly configured, it should appear
as 3 devices: an ethernet interface (either usb0 or ethX), an ACM
tty device (/dev/ttyACM0), and a USB storage device.  Check dmesg
or the kernel log for something similar to this:

::

 kernel: usb 2-6: new high-speed USB device number 5 using ehci-pci
 kernel: usb 2-6: New USB device found, idVendor=1d6b, idProduct=0104
 kernel: usb 2-6: New USB device strings: Mfr=2, Product=3, SerialNumber=4
 kernel: usb 2-6: Product: BeagleBoneBlack
 kernel: usb 2-6: Manufacturer: Circuitco
 kernel: usb 2-6: SerialNumber: 6A-0314BBBK4860
 kernel: usb-storage 2-6:1.4: USB Mass Storage device detected
 kernel: scsi12 : usb-storage 2-6:1.4
 mtp-probe: checking bus 2, device 5: "/sys/devices/pci0000:00/0000:00:13.2/usb2/2-6"
 mtp-probe: bus: 2, device: 5 was not an MTP device
 kernel: cfg80211: Calling CRDA to update world regulatory domain
 kernel: usbcore: registered new interface driver cdc_ether
 kernel: rndis_host 2-6:1.0 eth1: register 'rndis_host' at usb-0000:00:13.2-6, RNDIS device, 90:59:af:68:74:cf
 kernel: usbcore: registered new interface driver rndis_host
 kernel: usbcore: registered new interface driver rndis_wlan
 kernel: cdc_acm 2-6:1.2: This device cannot do calls on its own. It is not a modem.
 kernel: cdc_acm 2-6:1.2: ttyACM0: USB ACM device
 kernel: usbcore: registered new interface driver cdc_acm
 kernel: cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
 kernel: cfg80211: World regulatory domain updated:
 kernel: cfg80211:   (start_freq - end_freq @ bandwidth), (max_antenna_gain, max_eirp)
 kernel: cfg80211:   (2402000 KHz - 2472000 KHz @ 40000 KHz), (N/A, 2000 mBm)
 kernel: cfg80211:   (2457000 KHz - 2482000 KHz @ 40000 KHz), (N/A, 2000 mBm)
 kernel: cfg80211:   (2474000 KHz - 2494000 KHz @ 20000 KHz), (N/A, 2000 mBm)
 kernel: cfg80211:   (5170000 KHz - 5250000 KHz @ 80000 KHz), (N/A, 2000 mBm)
 kernel: cfg80211:   (5735000 KHz - 5835000 KHz @ 80000 KHz), (N/A, 2000 mBm)
 kernel: cfg80211:   (57240000 KHz - 63720000 KHz @ 2160000 KHz), (N/A, 0 mBm)
 kernel: ip_tables: (C) 2000-2006 Netfilter Core Team
 kernel: nf_conntrack version 0.5.0 (16384 buckets, 65536 max)
 kernel: scsi 12:0:0:0: Direct-Access     Linux    File-CD Gadget   0308 PQ: 0 ANSI: 2
 kernel: sd 12:0:0:0: [sdb] 144522 512-byte logical blocks: (73.9 MB/70.5 MiB)
 kernel: sd 12:0:0:0: [sdb] Write Protect is off
 kernel: sd 12:0:0:0: [sdb] Mode Sense: 0f 00 00 00
 kernel: sd 12:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA

The gadget ethernet device can be configured just like any other,
whether manually, with a script, or your distro's config tools.
The latter is recommended; for example on Gentoo you can add a
new config file in /etc/conf.d for the ethernet interface (eth1
in this example).  You must also allow network hotplugging in
rc.conf (or /etc/conf.d/rc if your system is old).  The default
IP address on the Black side of gadget ethernet is 192.168.7.2,
and will assign 192.168.7.1 to the desktop side if left to DHCP
(here we hard-code a static address since this is a local subnet).

From /etc/rc.conf::

 # This allows all services to be hotplugged
 rc_hotplug="*"

And /etc/conf.d/net.eth1:

::

 config_eth1="192.168.7.1 netmask 255.255.255.0 brd 192.168.7.255"
 routes_eth1="default via 192.168.7.1"
 
 preup() {
 iptables -A POSTROUTING -t nat -j MASQUERADE -s 192.168.7.0/24
 echo 1 > /proc/sys/net/ipv4/ip_forward
 iptables -P FORWARD ACCEPT
 return 0
 }
 
 postdown() {
 echo 0 > /proc/sys/net/ipv4/ip_forward
 iptables -t nat -F
 return 0
 }

It's also possible to use a udev rule or manual script instead, but
I prefer the network-config approach best.  The above configuration
should configure everything automatically on the host side when the
Black USB cable is plugged in.  Now you can browse the web interface
over the BeagleBone gadget ethernet (just point your browser to
192.168.7.2).

Default BeagleBone USBNet Config Missing DNS Servers and Default Route
======================================================================

If you're logged in remotely to your BeagleBone over the USB ethernet
connection, you might notice there's only a host route and the default
DNS server is the loopback address.  If you want your BeagleBone to see
outside the local subnet, then you'll need to add a default route::

 # route add default gw 192.168.7.1

You can do this permanently by editing the default dhcp udev rule. You'll 
need to edit /etc/udev/rules.d/udhcpd.rules and change this::

 SUBSYSTEM=="net",ACTION=="add",KERNEL=="usb0",RUN+="/sbin/ifconfig usb0 192.168.7.2 netmask 255.255.255.252",RUN+="/bin/systemctl start udhcpd.service"

to this::

 SUBSYSTEM=="net",ACTION=="add",KERNEL=="usb0",RUN+="/sbin/ifconfig usb0 192.168.7.2 netmask 255.255.255.252",RUN+="/sbin/route add default gw 192.168.7.1",RUN+="/bin/systemctl start udhcpd.service"

and then add your preferred DNS servers to /etc/resolv.conf.

