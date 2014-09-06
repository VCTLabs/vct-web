gadgetfs regression workaround
##############################

:date: 2014-09-01
:author: Stephanie Lockwood-Childs
:tags: gadgetfs, linux, patch
:category: news
:slug: gadgetfs_workaround
:summary: Workaround for gadgetfs module refcount bug 

The *gadgetfs* driver has had a `module refcount bug <bug_>`_ in all recent kernels, from
v3.10 up through present (last tag from Linus currently being v3.17-rc3). 
Embedded developers interested in using gadgetfs module with kernels 3.10 through 3.16
may wish to try this `version of the patch <patch_>`_ rather than the one attached to the `bug report <bug_>`_ 
(the only difference being paths: before or after the gadgetfs driver got shuffled into a "legacy" subdirectory). 

.. _bug: https://bugzilla.kernel.org/show_bug.cgi?id=83721
.. _patch: /downloads/gadgetfs-fix-refcount.patch

