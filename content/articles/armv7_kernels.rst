##############################################################
ARMv7 3.15.0 Kernel and U-Boot Images for Gentoo / Other Linux
##############################################################

:date: 2014-06-18
:author: Stephen Arnold
:tags: kernel, u-boot, rootfs, Gentoo, Debian, Wandboard, Udoo, BeagleBoneBlack
:category: news
:slug: armv7_kernels
:summary: 3.15.0 ARMv7 kernel and u-boot images now available

ARMv7 Linux kernel (3.15.0) and U-Boot (2014.07-rc3) images are available 
for use, built from the `github repos`_ of Robert C Nelson, the current 
upstream maintainer of several board-specifc kernel patch sets, u-boot 
patches, custom build scripts, and eewiki docs.

The primary (patch) sources used for these builds are:

 * https://github.com/RobertCNelson/Bootloader-Builder
 * https://github.com/RobertCNelson/armv7-multiplatform
 * https://github.com/RobertCNelson/bb-kernel

The primary tested hardware and deployment docs for these builds consisted of:

 * BeagleBoneBlack Rev A6A - http://eewiki.net/display/linuxonarm/BeagleBone+Black
 * WandBoard Quad - http://eewiki.net/display/linuxonarm/Wandboard
 * Udoo Quad -http://eewiki.net/display/linuxonarm/UDOO

The build output and a stage "4" Gentoo rootfs are available here:

  * http://www.gentoogeek.org/files/armv7-multiplatform/
  * http://www.gentoogeek.org/files/arm-u-boot-multi/
  * http://www.gentoogeek.org/files/arm-bb_kernel/

You can always build your own from the above github repos (which is the subject 
of a future article) and these are really provided just to get started, ie, boot 
up the hardware, do some test and checkout, maybe chroot using a SATA or USB disk. 
These choices are left as an exercise for the reader...

===========
Quick Start
===========

For Wandboard quad, download the following, similarly for Wandboard dual, Udoo, etc:

  * http://www.gentoogeek.org/files/armv7-multiplatform/

    - 3.15.0-rc8-armv7-x1.2.zImage

    - 3.15.0-rc8-armv7-x1.2-dtbs.tar.gz

    - 3.15.0-rc8-armv7-x1.2-firmware.tar.gz

    - 3.15.0-rc8-armv7-x1.2-modules.tar.gz

Download the latest u-boot image for your specific board from the appropriate subdir:

  * http://www.gentoogeek.org/files/armv-u-boot-multi/

    - u-boot-wandboard_quad-v2014.07-rc3-r8.imx

For BeagleBoneBlack, use the above BBB u-boot image, but substitute the following kernel:

  * http://www.gentoogeek.org/files/arm-bb_kernel/

    - 3.15.0-bone1.zImage

    - 3.15.0-bone1-dtbs.tar.gz

    - 3.15.0-bone1-firmware.tar.gz

    - 3.15.0-bone1-modules.tar.gz

Follow the eewiki doc (above) for the appropriate board to make an sdcard, and choose 
a rootfs.  For a basic Gentoo stage "4" rootfs with a portage tree and a few other tools, 
download the following tarball and edit the password file, hostname, and net 
config.  Otherwise try one of the distros recommended on the eewiki doc.

Gentoo armv7a-hardfloat stage 4:

  * http://www.gentoogeek.org/files/armv7-multiplatform/

    - stage4-armv7a_hardfp-rootfs-20140614.tar.bz2


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

You can choose a Gentoo Stage 3 tarball (or the stage 4 listed above) 
or any other appropriate rootfs (ie, Debian Wheezy armhf).  Substitute 
whatever rootfs tarball you like when you get to that step.  The stage 4 
provided here is essentially the latest Gentoo stage 3 for ARMv7 hardfloat, 
with some extra apps (distcc, ccache, gkrellm, nfs-utils, screen, ntp, 
zram-init, portage tree).

See the eewiki links for supported distros, or the Gentoo mirror list for 
ARM stage 3 tarballs and portage snapshots.  Download the stage 4 at the 
link above.


Prepare an SDCard
-----------------

Follow the steps for your board/device; the key difference lies mainly 
in which u-boot files are used and how they are installed.  It isn't 
strictly required to reformat the card each time, depending on what 
your needs are, ie, you can preserve an existing rootfs and manually 
update the bootloader and/or kernel as needed.

If the card seems slow when running, then check top and loof for a piggy 
process.  Some cards feel faster/slower depending on how they're formatted, 
so feel free to test some of the recommended formatting options (although 
the partition allignment should be fine with default fdisk, whether or not 
you want ext4 to use a journal and setting a specific stride option is up 
to personal choice).

Lastly, make sure your mount options include relatime/diratime or similar 
for decent card performance.  Also consider using a small zram swap device 
and/or tmpfs device for /tmp if you have enough physical RAM.  The latter 
options actually help quite a lot for general performance and on most compile 
jobs, but make sure your parallel make setting isn't too high when you compile 
things like binutils/gcc/glibc, and especially webkit-gtk and firefox...



.. _github repos: https://github.com/RobertCNelson?tab=repositories


