Tracing Cheatsheet
##################

:date: 2011-11-26
:tags: debugging, shell, python, ruby, perl, tcl, make, ant, cmake, scons
:category: cheatsheets
:slug: tracing_cheatsheet
:author: Stephanie Lockwood-Childs
:summary: cheatsheet for enabling tracing with various languages / build tools

List of simple methods to enable tracing in various scripting languages (shell, python, ruby, perl, tcl)
and build tools (make, ant, cmake, scons). Basic tracing is normally possible without editing the code or 
installing additional debugging software.

Script Tracing
==============

Tracing shell scripts
---------------------

Trace every line, showing literally when read and after shell expansion whenever executed:

::

  $ export PS4='+(${BASH_SOURCE[0]}:${LINENO}): ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'
  $ bash -v -x <script>

Tracing goes to stderr, so can be saved to a file separate from normal program output 
on stdout, e.g. replace second line with

::

  $ bash -v -x <script> 1>/tmp/OUT 2>/tmp/TRACE

Within the trace output, lines prefixed with '+' are post-shell-expansion and
the others are pre-shell-expansion.

In order to trace all the way down into scripts called from a toplevel script,
the toplevel script will need to be edited to run them with '-v -x' options.

:NOTE: 
  When using zsh rather than bash, you should be able to use the same commands 
  except for replacing '${BASH_SOURCE[0]' with '${(%):-%N}' in the 'export' command.

Tracing python scripts
----------------------

Trace everything:

::

  $ python -m trace --trace <script>

Trace except for standard library modules:

::

  $ python -m trace --trace --ignore-dir=/usr/lib/python<py-version> <script> 

where <py-version> is python version from 'python --version' minus the
trailing patch level, e.g. 2.7 or 3.2 rather than 2.7.4 or 3.2.2

Trace except for specific modules:

::

  $ python -m trace --trace --ignore-module=<module 1> --ignore-module=<module 2> <script> 

Tracing ruby scripts
--------------------

Trace every line:

::

  ruby -rtracer <script>

Tracing perl scripts
--------------------

Trace every line:

::

  $ export PERLDB_OPTS="NonStop AutoTrace"
  $ perl -d <script>

Trace subroutine entry and exit points, displaying arg list:

::

  $ export PERLDB_OPTS="NonStop frame=14" 
  $ perl -d <script>

Same, but copy trace to a file (can't just redirect stdout/stderr):

::

  $ export PERLDB_OPTS="NonStop frame=14 LineInfo=TRACE.out" 
  $ perl -d <script>

Tracing tcl scripts
-------------------

Trace everything:

::

  $ tclsh 
  % <paste excerpt below>
  % source <script>

using this as the paste contents:

::

  rename proc _proc
  _proc proc {name arglist body} {
      uplevel 1 [list _proc $name $arglist $body]
      uplevel 1 [list trace add execution $name enterstep [list ::proc_start $name]]
  }
  _proc proc_start {name command op} {
      puts "$name >> $command"
  }

Recipe taken from "Trace" section of the `debug page of the Tcler's Wiki <tclwiki_>`_, 
which is a page worth exploring further if needing to do much tcl debugging.

.. _tclwiki: http://wiki.tcl.tk/473

Build Tracing
=============

Tracing make builds
-------------------

Normal tracing:

::

  $ make --debug -n <target>

Note that '-n' is a simulation mode so commands are not actually run,
but it shows _all_ commands that would have been run (even commands that 
would otherwise be quieted by '@' prefix).

Much improved tracing:

::

  $ make SHELL='$(warning [$@ ($^) ($?)])bash'

This is essentially a suggestion from an excellent `Dr. Dobbs article on 
Make debugging <dobbs_>`_ with the additional observation that often it 
can be passed in on the command line without editing the Makefile
(unless some or all of the Makefiles are overriding SHELL already).

.. _dobbs: http://www.drdobbs.com/tools/debugging-makefiles/197003338

Tracing ant builds
------------------

Normal tracing:

::

  $ ant -v <target>

Tracing cmake builds
--------------------

Normal tracing:
 
::

  $ cmake --trace <target>

Tracing with extra debug info:

::

  $ cmake --trace --debug-output <target>

Tracing scons builds
--------------------

Normal tracing:
 
::

  $ scons --taskmastertrace=<logfile> <target>

where logfile can be a '-' to print dependency trace to stdout
