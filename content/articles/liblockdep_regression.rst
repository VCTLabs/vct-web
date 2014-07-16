Fix for liblockdep regression in kernel 3.15
############################################

:date: 2014-07-15
:author: Stephanie Lockwood-Childs
:tags: liblockdep, linux, patch
:category: news
:slug: liblockdep_fix
:summary: patch for liblockdep regression in kernel 3.15

The *liblockdep* userspace lock debugging tool was merged to the mainline
kernel tree in version 3.14. Unfortunately, the very next official release, 
linux 3.15, had a lockdep change that happened to break *liblockdep*.
I have submitted a patch to fix the regression, but it is currently two steps
away from the mainline tree (first Ingo Molnar will need to `pull the fix
from Sasha Levin`_, then Linus will need to pull from Ingo). Thus 3.16 might
also get released without this fix. Here is a copy of the patch for those
who wish to apply it manually to an affected kernel (3.15, and possibly 3.16): liblockdep-fix-regression.patch_

.. _pull the fix from Sasha Levin: https://lkml.org/lkml/2014/7/7/465
.. _liblockdep-fix-regression.patch: ../downloads/liblockdep-fix-regression.patch
