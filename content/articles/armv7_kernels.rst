##############################################################
ARMv7 3.15.0 Kernel and U-Boot Images for Gentoo / Other Linux
##############################################################

:date: 2014-06-12
:author: Stephen L Arnold
:tags: kernel, u-boot, rootfs, Gentoo, Debian, Wandboard, Udoo, BeagleBoneBlack
:category: news
:slug: armv7_kernels
:summary: 3.15.0 ARMv7 kernel and u-boot images now available

ARMv7 Linux kernel (3.15.0) and U-Boot (2014.07-rc3) images available 
for use, built from the 'github repos'_ of Robert C Nelson, the current 
upstream maintainer of several board-specifc kernel patch sets, u-boot 
patches, custom build scripts, and eewiki docs.

The primary (patch) sources used for these builds are:

 * https://github.com/RobertCNelson/Bootloader-Builder
 * https://github.com/RobertCNelson/armv7-multiplatform
 * https://github.com/RobertCNelson/bb-kernel

The primary tested hardware and deployment docs for these builds consist of:

 * BeagleBoneBlack Rev A6A - http://eewiki.net/display/linuxonarm/BeagleBone+Black
 * WandBoard Quad - http://eewiki.net/display/linuxonarm/Wandboard
 * Udoo Quad -http://eewiki.net/display/linuxonarm/UDOO

You can always build your own from the above repos (which is the subject of a 
future article) and these are really provided just to get started, ie, boot up 
the hardware, do some test and checkout, maybe chroot using a SATA or USB disk. 
These choices are left as an exercise for the reader...

===========
Quick Start
===========

=============
Extra Details
=============

Download the kernel and u-boot
------------------------------

Download all of the kernel and u-boot files for your board; each board 
has a separate directory for u-boot images (choose the version you want) 
whereas the armv7-multiplatform kernels support multiple boards (again, 
choose the version you want).  If you have a BeagleBoneBlack, you can 
try the multiplatform kernel, but the bb_kernel repository patches 
seem to be more current.

Download a rootfs
-----------------

You can choose a Gentoo Stage 3 tarball (or the stage 4 listed below) 
or any other appropriate rootfs (ie, Debian Wheezy armhf).  Substitute 
whatever rootfs tarball you like when you get to that step.  The stage 4 
provided here is essentially the latest Gentoo stage 3 for ARMv7 hardfloat, 
with some extra apps (distcc, ccache, gkrellm, nfs-utils, screen, ntp, 
zram-init, portage tree).

See the eewiki links for supported distros, or the Gentoo mirror list for 
ARM stage 3 tarballs and portage snapshots.  Download the stage 4 here:



Prepare an SDCard
-----------------

Follow the steps for your board/device; the key difference lies mainly 
in which u-boot files are used and how they are installed.  It isn't 
strictly required to reformat the card each time, depending on what 
your needs are, ie, you can preserve an existing rootfs and manually 
update the bootloader and/or kernel as needed.

.. _github repos: https://github.com/RobertCNelson?tab=repositories


