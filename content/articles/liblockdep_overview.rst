liblockdep: userspace lockdep
#############################

:date: 2014-07-09
:tags: linux, debugging, locks
:category: programming
:slug: liblockdep
:author: Stephanie Lockwood-Childs
:summary: debug your userspace locking with liblockdep

What is lockdep?
================

Lockdep is the kernel-lock validator. Core kernel developer Ingo Molnar
originally designed lockdep to help clean up deadlocks left over from 
the kernel's transition in SMP implementation strategy, from a single 
"Big Kernel Lock" in early days to increasingly fine-grained locking. 

Tracking locks necessarily adds some overhead to the code under observation,
and thus experienced developers might wonder whether running code with
lockdep enabled would tend to change timing enough that race conditions 
triggering deadlocks would disappear, the `"heisenbug" effect <heisenbug_>`_.

The good news is that the lockdep validation strategy is not at all dependent
on timing -- it tracks patterns of lock acquisition and determines whether
code *could* lock if one thread ran code block X while another thread happened
to be running code block Y, and generates a warning regardless of whether
that concurrency happened or not. Kernel developers can thus use lockdep to 
track down locking errors without attempting to reproduce an obscure race 
condition that only pops up on *other* people's systems to trigger deadlocks.

Lockdep was officially released in the mainline kernel back in 2006 with 
version 2.6.18, and it has helped kernel developers clean up many locking bugs 
since then:

    over the past 2-3 years the term "hard lockup" in regression reports has
    gone down by about an order of magnitude - and much of that can be
    attributed to the lockdep coverage we have in place -Ingo Molnar

http://lwn.net/Articles/321670/

A very nice overview on lockdep architecture can be found at LWN_,
and some practical implementation details can be found in the Linux source
code as linux/Documentation/lockdep-design.txt

.. _heisenbug: http://en.wikipedia.org/wiki/Heisenbug
.. _LWN: http://lwn.net/Articles/185666/

What is userspace lockdep aka liblockdep?
=========================================

Fast-forwarding from 2.6 kernel days to the 3.13 era, lockdep was still a
widely used tool among kernel developers; not only for fixing deadlocks, but
also proactively auditing locking sanity of proposed code. Lockdep is
lightweight enough to allow fairly normal use of a system while it is enabled,
quite a major feature for debugging complicated systems -- enough to inspire
some jealousy by developers on the other side of the kernel/userspace divide.
Free software developers dealing with complicated locking in pthread code
needed a lot of patience to run it under the valgrind lock checker.

Finally in early 2013, Sasha Levin decided that since the lockdep algorithm is
not really tied to any kernel concepts, the lockdep code could be
repurposed as a pthread lock validator. He did this by wrapping the core
lockdep code, adding redefinitions and stubs that converted the kernel 
implementation into a pthread implementation. Ingo Molnar approved of
Sasha's leveraging of lockdep code without uglifying the original kernel
implementation, and helped pave the way for the userspace lockdep wrapper
(or "liblockdep") to be merged into kernel version 3.14 as part of the
tools/ subdirectory alongside other kernel-related userspace tools such
as perf_.

Unfortunately liblockdep suffered a regression in the very next official 
release kernel 3.15. I have submitted a patch which Sasha Levin has included 
in his `latest git pull request<pull>_`, so hopefully the breakage will be
fixed by the upcoming 3.16 kernel release. As liblockdep matures, regressions
like this will become unlikely.

For further discussion on liblockdep try this `LWN article`_; there are no
official docs in the kernel source code yet.

.. _perf: https://perf.wiki.kernel.org
.. _pull: https://lkml.org/lkml/2014/7/7/465
.. _LWN article: https://lwn.net/Articles/536363/

When is Liblockdep useful
=========================

Valgrind helgrind and DRD modules are the main Free Software alternatives to
liblockdep for userspace lock debugging, so it is useful to consider what
conditions might favor use of liblockdep over valgrind:

* consider liblockdep to reduce runtime overhead
  If the application is complex and the system running it does not
  have plenty of spare resources (CPU and memory), valgrind may not be
  practical. For instance, performance is often important when trying to 
  debug an embedded Linux program, either in an emulator (which often adds
  plenty of overhead itself) or on the native hardware.

* consider liblockdep for cross-compile support in niche environments
  Valgrind has been ported to the most popular architectures and
  is included in most popular embedded linux build systems (yocto/OE,
  OpenWrt, buildroot) but that can't match liblockdep, which should
  build easily for anything that has a mainlined kernel port. 

There are also circumstances that rule out the use of liblockdep:

* can't use liblockdep if the application uses non-pthread locks
  According to its docs, Valgrind can do lock validation with custom locks, 
  as long as all locking code is suitably annotated.

* don't use liblockdep with recursive mutexes 
  If possible, clean up the code so that recursive mutexes are not needed,
  but otherwise use something else to debug the locking.

    The kernel hates recursive locks. They promote incorrect usage of locking
    semantics and are completely unsupported in the kernel.

    As you might guess from the above, this also means that lockdep doesn't
    work at all with recursive locks, and will just detect a trivial deadlock
    when an attempt to lock a lock twice is made.

    Therefore, liblockdep is completely useless in code which relies on
    recursive locks, and I doubt the situation will change at any point in the 
    future since I don't see the kernel adopting recursive locking.
    -Sasha Levin (quoted with permission from an email)

Making Use of Liblockdep
========================

Building liblockdep
-------------------

If using kernel 3.15 (and perhaps 3.16 which hasn't been released at the
time of writing), start by applying `this patch`_ 

From toplevel kernel source dir,
::

    patch -p1 < liblockdep-fix-regression.patch

.. _this patch: downloads/liblockdep-fix-regression.patch

After either applying the patch or determining it is not needed,
the build can be run from the toplevel kernel source dir
::

    make -C tools/lib/lockdep

or in new enough releases (> 3.14)
::

    make -C tools liblockdep

For a cross-compile build, just add ARCH and CROSS_COMPILE
variables like when building the corresponding kernel, e.g.
::

    make -C tools liblockdep ARCH=arm CROSS_COMPILE=arm-none-linux-gnueabi-

or 
::

    export ARCH=arm CROSS_COMPILE=arm-none-linux-gnueabi-
    make -C tools liblockdep 

output files will be found under tools/lib/lockdep/ --
liblockdep.a and liblockdep.so.<version> for static and shared libraries
respectively.

Testing liblockdep
------------------

liblockdep comes with a nice set of unit tests. It is a good idea to make sure
the tests pass before trying to use liblockdep to do real work. 

Running the tests natively on the build host is quite simple:
starting from the toplevel kernel source directory, 
::

    cd tools/lib/lockdep
    ./run_tests.sh

Every test will say "PASSED" if this is a good build of liblockdep.

Running liblockdep
------------------

liblockdep build creates both a static library and a shared library,
so type of linking can be decided based on needs of the project.

Static library

  * need to use the static version if application under test is statically linked

  * watch out for licensing issues -- can only ship apps with builtin liblockdep
    if all the source is GPLv2 compatible (fine to use liblockdep in local 
    test builds with any source though, just can't release to users if non-GPL)

  * run application normally, no changes to command line

Shared library

  * application under test must be dynamically linked to libpthread

  * use LD_PRELOAD to allow liblockdep to override pthread locking functions

    LD_PRELOAD=/usr/src/linux/tools/lib/lockdep/liblockdep.so some_thready_application

Tips common to both styles of linking

  * liblockdep traces currently go to stdout, so make sure stdout is not closed

  * stack traces in output are improved if application is built with -rdynamic
    (functions will be listed instead of just addresses)

  * like compiler errors, focus on fixing first complaint from the output, 
    since single error can cascade to generate multiple complaints
