##############################################################
Run Gentoo or Ubuntu Linux On The New Acer Tegra K1 Chromebook
##############################################################

:date: 2015-01-22
:author: Stephen Arnold
:tags: Gentoo, low power, Ubuntu, chrubuntu, embedded, ARM, Tegra, Nvidia, Linux
:category: howto
:slug: tegra_chromebook_hack
:summary: Acer Tegra K1 Chromebook with Custom Kernel and Rootfs

Quick and easy script for making a bootable SDCard loaded with Ubuntu, already stocked with ChromeOS graphics blobs and kernel:

 * Quick install steps are documented in the `readme file here`_
 * More info on the `chrubuntu script arguments here`_
 * Reference for `custom kernel build here`_

.. _readme file here: https://github.com/VCTLabs/chrubuntu-tegra
.. _chrubuntu script arguments here: http://chromeos-cr48.blogspot.com/2013/05/chrubuntu-one-script-to-rule-them-all_31.html
.. _custom kernel build here: https://github.com/lgeek/gnu-linux-on-acer-chromebook-13

Follow the quick install steps in the readme above to make a bootable SDCard with xubuntu.

The Gentoo steps are essentially the same as those documented in the custom kernel reference above, where you can of course build natively on another ARM box, or use the cross-compile method documented above (which is suitably modified for gentoo below).

For Cross-Compiling
===================

First grab the latest crossdev-9999 and the required tools, then build a current armv7a hardfloat toolchain::

 # emerge uboot-tools vboot-utils dtc bc -v
 # emerge crossdev -v
 # crossdev -v -t armv7a-hardfloat-linux-gnueabi

You may need to add the following to your package.keywords file::

 sys-devel/crossdev **

Next grab the chromeos kernel sources and configure/build a kernel::

 # git clone https://chromium.googlesource.com/chromiumos/third_party/kernel linux-chromeos
 # cd linux-chromeos
 # git checkout chromeos-3.10

Get the USB firmware (from `this overlay`_) and prepare the config file::

 # wget http://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/xhci firmware-2014.11.06.00.00.tbz2
 # tar xf xhci-firmware-2014.11.06.00.00.tbz2
 # cp -R lib/firmware/ .
 # rm -R ./lib/firmware/
 # ./chromeos/scripts/prepareconfig chromeos-tegra
 # WIFIVERSION=-3.8 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- make menuconfig

According to the reference above, the WIFIVERSION variable is required to build the drivers in ``drivers/net/wireless-3.8``; the mwifiex driver in /drivers/net/wireless/ does not support the Chromebook's adapter.  CROSS_COMPILE should be set to the correct prefix for your toolchain.

In the kernel config, set ``Device Drivers > Generic Driver Options > External firmware blobs to build into the kernel binary`` to ``nvidia/tegra124/xusb.bin``.  Make any other desired changes, and build the kernel, modules, and dtb file::

 # WIFIVERSION=-3.8 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- make zImage
 # WIFIVERSION=-3.8 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- make modules
 # WIFIVERSION=-3.8 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- make tegra124-nyan-big.dtb

Build a Flattened Image Tree using the provided configuration file::

 # wget https://raw.githubusercontent.com/lgeek/gnu-linux-on-acer-chromebook-13/master/nyan-big-fit.cfg
 # mkimage -f nyan-big-fit.cfg nyan-big-kernel

Now create the kernel args and a bootable (signed) vboot image::

 # echo "noinitrd console=tty1 debug verbose root=/dev/mmcblk1p7 rootwait rw lsm.module_locking=0 net.ifnames=0 rootfstype=ext4" > ./cmdline
 # vbutil_kernel --arch arm --pack kernel.bin --keyblock /usr/share/vboot/devkeys/kernel.keyblock --signprivate /usr/share/vboot/devkeys/kernel_data_key.vbprivk --version 1 --config cmdline --vmlinuz nyan-big-kernel

Now insert your prepared SDCard (see below) and copy the signed kernel image to your kernel partition, install the kernel modules, and copy your rootfs; here we'll use a stage3 armv7 tarball::

 # dd if=./kernel.bin of=/dev/sdb6
 # mkfs.ext4 /dev/sdb7
 # export mount_point="/mnt/card/root/"
 # mkdir -p $mount_point
 # mount /dev/sdb7 $mount_point
 # INSTALL_MOD_PATH=$mount_point WIFIVERSION=-3.8 ARCH=arm CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- make modules_install
 # tar xpf /path/to/downloads/stage3-armv7a_hardfp-20141023.tar.bz2 -C $mount_point

.. admonition:: Note

   The above partion numbers match the SDCard section below; just use the matching values if yours are different (eg, use 1 and 2 instead of 6 and 7).

Now you can complete the normal Gentoo embedded install, ie, set the root password, configure and enable networking, etc.  Insert the card in your Chromebook (make sure it's in "developer" mode) and Ctrl-U at the warning screen.

.. _this overlay: https://chromium.googlesource.com/chromiumos/overlays/board-overlays/+/master/overlay-nyan/sys-kernel/xhci-firmware/xhci-firmware-2014.11.06.00.00.ebuild

For Native Builds
=================

Once you have a bootable SDCard, you're free to build more components on the card itself, or even better, use an external SSD or hard disk with a USB3 interface.  This works well on even the older ARM Chromebooks (velcro, as always, is your friend, along with a short right-angle USB3 cable).  For new kernels, simply omit the ARCH and CROSS_COMPILE variables and build/install as above.

Make an SDCard
==============

For either build method, you'll need an SDCard with the right partition format, which you can do by hand or with the chrubuntu script.  The one caveat is that the latest Chromeos on my own Acer 13 is missing some key tools compared to previous revisions, mainly parted and partprobe.  The workaround is that you must make a GPT partition table on the SDCard first, using another Linux machine (ie, not your shiny new Chromebook).  So first on another Linux machine, insert your (blank or unimportant) SDCard and run the following command, where "target_disk" is most likely either sdX for USB card readers or mmcblkX for built-in devices::

 # export target_disk="/dev/sdb"
 # parted --script ${target_disk} "mktable gpt"

The following can be done on the chromebook, which is what the chrubuntu script expects.  Since we're not running chrubuntu, we'll manually create some partitions, one for the kernel image, and one for the rootfs::

 # ext_size="`blockdev --getsz ${target_disk}`"
 # aroot_size=$((ext_size - 65600 - 33 - 4*1024*1024*1024/512))
 # cgpt create ${target_disk}
 # cgpt add -i 6 -b 64 -s 32768 -S 1 -P 5 -l KERN-A -t "kernel" ${target_disk}
 # cgpt add -i 7 -b 65600 -s $aroot_size -l ROOT-A -t "rootfs" ${target_disk}
 # sync
 # blockdev --rereadpt ${target_disk}


.. admonition:: Note

   The above assumes at least a 16 or 32 GB card.  4 GB is known not to work.

Now you can go back to installing Gentoo, or, if you must, run the chrubuntu script and wait...

