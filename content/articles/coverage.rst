====================================================================================
Dos and Don'ts for generating code/test coverage data (for C, C++, Java, and Python)
====================================================================================

:date: 2014-04-03
:author: Steve Arnold
:tags: code coverage, test coverage, software testing, gcov, gcc
:category: programming
:slug: coverage-with-gcov
:summary: Overview of using gcov to collect coverage data


Tips
====

.. admonition:: Note

    1) **Do** generate coverage data for your code; it should be especially helpful for pointing out where test drivers are exercising code (and where they aren't).  **Don't** rely on just line or branch counts and shoot for higher numbers.  For exmple, use  the branch count information to make sure you're executing all the appropriate decision paths, etc.

    2) **Do** try it under "normal" or ad-hoc execution conditions to look at the main flow(s) through your code. **Don't** restrict your use of coverage data to testing only.

The current tools described here include the following:

* gcov/lcov (for C, C++, and pretty much anything compiled with gcc)
* coverage.py (for Python)
* cobertura (for Java)

Using gcov
==========

Once your code is at least running local unit tests, and *if* you see any
performance issues, then you can add the profiling targets to your makefile
or python code.  For non-kernel code, you should add a make target by following
this simple example::

     $ gcc -fprofile-arcs -ftest-coverage tmp.c
     $ a.out
     $ gcov tmp.c
     90.00% of 10 source lines executed in file tmp.c
     Creating tmp.c.gcov.

Please try some of the available gcov options, such as:

-a
--all-blocks

    Write individual execution counts for every basic block. Normally gcov outputs
    execution counts only for the main blocks of a line. With this option you can
    determine if blocks within a single line are not being executed.

-b
--branch-probabilities

    Write branch frequencies to the output file, and write branch summary info to
    the standard output. This option allows you to see how often each branch in your
    program was taken. Unconditional branches will not be shown, unless the -u option
    is given.

-c
--branch-counts

    Write branch frequencies as the number of branches taken, rather than the
    percentage of branches taken.

-f
--function-summaries

    Output summaries for each function in addition to the file level summary.

Generating coverage data for the kernel
=======================================

To generate coverage data for the Linux kernel, it's as easy as rebuilding the
kernel with the following options enabled::

  CONFIG_GCOV_KERNEL=y
  CONFIG_GCOV_PROFILE_ALL=y

and mounting the debugfs file system under /sys/kernel like so::

  # mount -t debugfs none /sys/kernel/debug

Then change to the kernel source tree::

  # cd /tmp/linux

and run the coverge tool on one or more source files::

  # gcov kernel/gcov/base.c -o /sys/kernel/debug/gcov/tmp/linux/kernel/gcov/
  File 'kernel/gcov/base.c'
  Lines executed:52.17% of 46
  kernel/gcov/base.c:creating 'base.c.gcov'

Code coverage information for the specified source file(s) can be found in the
files created by gcov. Alternatively, use LCOV to obtain the information
automatically.

Quick start using coverage.py
=============================

Install coverage.py from the `coverage page on the Python Package Index`_, or by
using “easy_install coverage”.  For a few more details, see Installation_.

Use coverage run to run your program and gather data::

    $ coverage run my_program.py arg1 arg2
    blah blah ...your program's output... blah blah

Use coverage report to report on the results::

    $ coverage report -m
    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    my_program                   20      4    80%   33-35, 39
    my_other_module              56      6    89%   17-23
    -------------------------------------------------------
    TOTAL                        76     10    87%

For a nicer presentation, use coverage html to get annotated HTML listings detailing
missed lines::

    $ coverage html

Then visit htmlcov/index.html in your browser, to see a nicely formatted report.

.. _coverage page on the Python Package Index: http://pypi.python.org/pypi/coverage
.. _Installation: http://nedbatchelder.com/code/coverage/install.html

