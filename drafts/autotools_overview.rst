Overview of the GNU autotools approach to source code configuration
###################################################################

:date: 2006-03-30
:author: Stephanie Lockwood-Childs
:tags: autotools, autoconf, automake, aclocal, configure
:category: programming
:slug: gnu_autotools_overview
:summary: GNU autotools overview 

Overview of GNU autotools from two different perspectives: software builder
and software developer (specifically, one maintaining a project's build system)


GNU Autotools from two perspectives
===================================

GNU autotools, or commonly referred to as plain "autotools", provides
source code configuration, allowing code to be customized in certain
ways as part of the build process. GNU autotools build-time customization 
is an important part of the toolset for many Free Software projects,
who use it to

* implement compile-time optional features
* account for differences in build environments

Let's look at autotools from two different perspectives, the "software builder" and
the "software developer". 

The software builder might be an end-user who is daring enough to try out some
software that has not yet been packaged up by the distro of their choice. Or,
it might be someone on the packaging-team of a distro, working to turn the
latest source code release into convenient packages for end-users. It could
even be a developer for another project, who needs a really fresh version of
some dependency used by their own code.

The software developer perspective in this case covers anyone on the software
project team who helps maintains the build process, in particular one that
allows source code to be built across a wide variety of hosts. This goal of
allowing source code to be built on hundreds or thousands of different hosts
across the world rather than just needing to build on a small number of
tightly-controlled corporate build servers has been a strong factor behind the
spread of autotools among Free Software projects rather than simpler, but
less-flexible, solutions such as hand-written Makefiles.

Software Builder's view of autotools
====================================

Autotools is rather friendly and convenient from the software builder's perspective,
with a basic invocation that has been memorized by many a power-user of Linux:

  ./configure ; make ; make install

and additional customization power available when it is needed:

  ./configure --enable-ssl --prefix=/opt/newstuff ; make ; make install

The configure script:

* accepts arguments to allow user to customize software
* runs tests to characterize build environment and locate
  build dependencies 

assuming all tests were successful,

* creates Makefiles that are adapted to

  * available build tools and locations of libraries 
  * customization choices made by the user

* (optional) creates config.h which has platform-dependent
  information that allows source code to adapt itself to

  * properties of the host platform
  * customization choices made by the user

Software developer's view of autotools
======================================

Autotools from this perspective is significantly more complex than what the
software builder typically experiences. A source code release supporting the
convenience of "./configure ; make ; make install" typically has

* a configure script that

  * offers appropriate options for customizing package
  * locates any external build dependencies (utilities, libraries, headers)
  * runs tests to detect platform characteristics
  * uses collected information to turn Makefile templates into actual Makefiles
  * (optional) uses collected information create config.h from a template

* corresponding Makefile templates 
* (optional) corresponding config.h template

The autotools suite is a framework for generating each of these pieces, 
so each new project does not have write code from scratch to handle each aspect
of customization (command-line parsing, system characterization, and applying 
the resulting configuration to build files and source code)

Input files maintained by developer

* toplevel

  * configure.in OR (deprecated) configure.ac 

    * m4 macro calls with shell script fragments as needed
    * lists user-configurable options, system characterization tests,
      and files to be generated from templates by variable substitution

  * (optional) acinclude.m4

    * custom m4 macro definitions
    * can define system tests not distributed with autotools

* per directory

  * Makefile.am

    * file lists and variable definitions 
    * use @NAME@ placeholders for variables to be substituted by configure

Autotools utilities

:autoscan:  
  generate a preliminary configure.in by scanning source code for common portability issues

:aclocal:  
  collect all m4 macros needed by configure.in into aclocal.m4

:autoconf:  
  create configure script based on configure.in (with required macros in aclocal.m4) 

:automake:  
  create Makefile.in files based on configure.in (with required macros in aclocal.m4) and the corresponding Makefile.am

:autoheader:  
  (optional) create config.h.in from which configure script can generate config.h

:libtoolize:  
  install helper files used by libtool to abstract away platform-dependent details of building libraries 

:autoreconf:  
  calls the various autotools in appropriate order


Relationship between tools and files
------------------------------------

Prepare for configuration

* aclocal(configure.in + acinclude.m4 + autotool files) = aclocal.m4
* autoconf(aclocal.m4 + configure.in) = configure
* automake(aclocal.m4 + configure.in + Makefile.am) = Makefile.in
* autoheader(configure.in) = config.h.in
* libtoolize [installs some libtool files into toplevel dir]

Perform configuration

* configure(config.h.in) = config.h
* configure(Makefile.in) = Makefile

Perform build

* make(Makefile + libtool files + source files) = build products


Resources
---------

:Autotools basics:  
  http://sourceware.org/autobook/autobook/autobook_toc.html

:Autotools Mythbuster: 
  https://www.flameeyes.eu/autotools-mythbuster/

:Autoconf macros archive: 
  https://www.gnu.org/software/autoconf-archive/
