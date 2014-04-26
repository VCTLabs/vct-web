=======================================================
The GNU autotools approach to source code configuration
=======================================================

by Stephanie Lockwood-Childs

User's view of source configuration
------------------------------------

./configure ; make ; make install
./configure --enable-ssl --prefix=/opt/newstuff ; make ; make install

the configure script:

* accepts arguments to allow user to customize software
* runs tests to characterize build environment and locate
  build dependencies 

assuming all tests were successful,

* creates Makefiles that are adapted to:
  * available build tools and locations of libraries 
  * customization choices made by the user

* (optional) creates config.h which has platform-dependent
  information that allows source code to adapt itself to:
  * properties of the host platform
  * customization choices made by the user

Package developer's view of source configuration
------------------------------------------------

* responsible for providing configure script that:
  * offers appropriate options for customizing package
  * locates any external build dependencies (utilities, libraries, headers)
  * runs tests to detect platform characteristics
  * uses collected information to turn Makefile templates into actual Makefiles
  * (optional) uses collected information create config.h from a template
* responsible for providing Makefile templates 
* (optional) responsible for providing config.h template

The autotools suite is a framework for generating each of these pieces, 
so each new project does not have write code from scratch to handle each aspect
of customization (command-line parsing, system characterization, and applying 
the resulting configuration to build files and source code)

Input files maintained by developer:
* toplevel
  * configure.in OR (deprecated) configure.ac 
    - m4 macro calls with shell script fragments as needed
    - lists user-configurable options, system characterization tests,
      and files to be generated from templates by variable substitution
  * (optional) acinclude.m4
    - custom m4 macro definitions
    - can define system tests not distributed with autotools
* per directory
  * Makefile.am
    - file lists and variable definitions 
    - use @NAME@ placeholders for variables to be substituted by configure

Autotools utilities:
* autoscan - generate a preliminary configure.in by scanning source code
             for common portability issues
* aclocal - collect all m4 macros needed by configure.in into aclocal.m4
* autoconf - create configure script based on configure.in (with required 
             macros in aclocal.m4) 
* automake - create Makefile.in files based on configure.in (with required 
             macros in aclocal.m4) and the corresponding Makefile.am
* autoheader - (optional) create config.h.in from which configure
               script can generate config.h
* libtoolize - install helper files used by libtool to abstract away
               platform-dependent details of building libraries 
* autoreconf - calls the various autotools in appropriate order


Overview of tools and files
---------------------------

Prepare for configuration

aclocal(configure.in + acinclude.m4 + autotool files) = aclocal.m4
autoconf(aclocal.m4 + configure.in) = configure
automake(aclocal.m4 + configure.in + Makefile.am) = Makefile.in
autoheader(configure.in) = config.h.in
libtoolize [installs some libtool files into toplevel dir]

Perform configuration

configure(config.h.in) = config.h
configure(Makefile.in) = Makefile

Perform build

make(Makefile + libtool files + source files) = build products


Resources
---------

Autotool book
http://sourceware.org/autobook/autobook/autobook_toc.html
Autoconf macros archive
https://www.gnu.org/software/autoconf-archive/
