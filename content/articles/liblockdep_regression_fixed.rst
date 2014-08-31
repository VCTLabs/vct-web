liblockdep fix was merged in kernel 3.16
##########################################

:date: 2014-08-30
:author: Stephanie Lockwood-Childs
:tags: liblockdep, linux, patch
:category: news
:slug: liblockdep_merge
:summary: Linus merged liblockdep fix in time for kernel 3.16 release

The *liblockdep* userspace lock debugging tool was merged to the mainline
kernel tree in version 3.14. Unfortunately, the very next official release, 
linux 3.15, had a lockdep change that happened to break *liblockdep*.  The
patch_ for this regression was submitted just after Linux tagged 3.16-rc4, and
being a fix for a regression (as opposed to a new feature) Linus was still
willing to merge_ it in time for the 3.16 release without any fuss. 
Users of liblockdep should thus upgrade to 3.16 or later.

.. _patch: /downloads/liblockdep-fix-regression.patch
.. _merge: https://github.com/torvalds/linux/commit/b10827814e9c81c5a14fb73c5a6e06bd85df3f94
