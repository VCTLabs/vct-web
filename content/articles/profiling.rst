=========================================================
Dos and Don'ts for profiling and performance optimization
=========================================================

:date: 2014-04-17
:author: Stephen Arnold
:tags: profiling, software testing, software performance, gprof, gcc
:category: programming
:slug: profiling-with-grof
:summary: Overview of using gprof to collect profiling data


Tips
====

.. admonition:: Note

    1) **Do** profile your code to look for performance bottlenecks, but **don't** worry about hand-optimizing your code right away.  Readable and obvious is much better from a maintenance standpoint than obtuse or cryptic.  Also, if you put too much into one line of code, you may actually be defeating the code coverage analysis.

    2) **Do** think about Big "O" when making algorithm selections, but **don't** worry about trying to out-think the compiler optimizations.  Trust in gcc/g++ at least up to the -O2 optimization level, but don't use -O3 (which is known to break certain constructs).

Using gprof
===========

Compiling for profiling
-----------------------

Before you can profile your program, you must first recompile it specifically for profiling.  To do so, add the -pg argument to the compiler's command line::

    $ g++ -g -pg -o dummy dummy.cc

This creates an executable called dummy from the source file dummy.cc with debugging and profiling turned on.  Another way to do this is to add -pg to the ``CFLAGS`` line in your ``Makefile``.

Creating gmon.out
-----------------

Once your program has been compiled with profiling turned on, running the program to completion causes a file named ``gmon.out`` to be created in the current directory.  gprof works by analyzing data collected during the execution of your program after your program has finished running.  ``gmon.out`` holds this data in a gprof-readable format.

Things to keep in mind:

* If ``gmon.out`` already exists, it will be overwritten.
* The program must exit normally.  Pressing control-c or killing the process is **not** a normal exit.
* Since you are trying to analyze your program in a real-world situation, you should run the program exactly the same way as you normally would (same inputs, command line arguments, etc.).

Running gprof
-------------

Run gprof like this::

    $ gprof program-name [ data-file ] [ > output-file ]

If you don't specify the name of a data file, ``gmon.out`` is assumed.  Following the gprof command with "``> output-file``" causes the output of gprof to be saved to ``output-file`` so you can examine it later.

For this example, the program name is dummy and we will save the output into a file called dummy.output::

    $ gprof dummy > dummy.output

Analyzing gprof's output
------------------------

After completing the last step, the gprof's analysis has been saved into the ``dummy.output file``.  You can use your favorite text editor to examine this file.  By default, two kinds of analysis are performed: the flat profile and the call graph. Both types are explained in the following sections.

Interpreting the flat profile
-----------------------------

The flat profile shows the total amount of time your program spent executing each function. At the end of the profile, you will see a legend describing what each of the columns of numbers means. Here is some of the output from the flat profile::

      Flat profile:

      Each sample counts as 0.01 seconds.
        %   cumulative   self              self     total
       time   seconds   seconds    calls  us/call  us/call  name
       37.50      0.15     0.15    48000     3.12     3.12  Life::neighbor_count(int, int)
       17.50      0.22     0.07                             _IO_do_write
       10.00      0.26     0.04                             __overflow
        7.50      0.29     0.03                             _IO_file_overflow
        7.50      0.32     0.03                             _IO_putc
        5.00      0.34     0.02       12  1666.67 14166.67  Life::update(void)
        5.00      0.36     0.02                             stdiobuf::overflow(int)
        5.00      0.38     0.02                             stdiobuf::sys_write(char const *, int)
        2.50      0.39     0.01                             ostream::operator<<(char)
        2.50      0.40     0.01                             internal_mcount
        0.00      0.40     0.00       12     0.00     0.00  Life::print(void)
        0.00      0.40     0.00       12     0.00     0.00  to_continue(void)
        0.00      0.40     0.00        1     0.00     0.00  Life::initialize(void)
        0.00      0.40     0.00        1     0.00     0.00  instructions(void)
        0.00      0.40     0.00        1     0.00 170000.00  main

Note that the functions ``mcount`` and ``profil`` (profil does not appear in this listing) are part of the profiling aparatus; their time gives a measure of the amount of overhead due to profiling.  Also note that functions like ``stdiobuf::sys_write`` and ``_IO_do_write`` are part of the system libraries and not directly part of your code.

In this output, we can see that 37.5% of dummy's execution time is spent in ``Life::neighbor_count``.  This is the highest percentage for any function in the program.  It is also worthwhile to note that it gets called 48,000 times.  This is your first hint that ``Life::neighbor_count`` might be the biggest bottleneck in the code.

Interpreting the call graph
---------------------------

The call graph shows how much time was spent in each function and its children. From this information, you can find functions that, while they themselves may not have used much time, called other functions that did use unusual amounts of time. Like for the flat profile, a legend appears after the call graph describing what each of the columns of numbers means.

Here is some of the output from the call graph::

                             Call graph (explanation follows)
    
    granularity: each sample hit covers 4 byte(s) for 2.50% of 0.40 seconds
    
    index % time    self  children    called     name
                    0.02    0.15      12/12      main [2]
    [1]     42.5    0.02    0.15      12         Life::update(void) [1]
                    0.15    0.00   48000/48000   Life::neighbor_count(int, int) [4]
    ---------------------------------------------------------------------------
                    0.00    0.17       1/1       _start [3]
    [2]     42.5    0.00    0.17       1         main [2]
                    0.02    0.15      12/12      Life::update(void) [1]
                    0.00    0.00      12/12      Life::print(void) [13]
                    0.00    0.00      12/12      to_continue(void) [14]
                    0.00    0.00       1/1       instructions(void) [16]
                    0.00    0.00       1/1       Life::initialize(void) [15]
    ---------------------------------------------------------------------------
    
    [3]     42.5    0.00    0.17                 _start [3]
                    0.00    0.17       1/1       main [2]
    ---------------------------------------------------------------------------
                    0.15    0.00   48000/48000   Life::update(void) [1]
    [4]     37.5    0.15    0.00   48000         Life::neighbor_count(int, int) [4]
    ---------------------------------------------------------------------------

The lines full of dashes divide this table into *entries*, one for each function. Each entry has one or more lines.

In each entry, the primary line is the one that starts with an index number in square brackets. The end of this line says which function the entry is for.

The preceding lines in the entry describe the callers of this function and the following lines describe its subroutines (also called *children* when we speak of the call graph). If the caller of a function cannot be determined, ``<spontaneous>`` is printed instead.

The entries are sorted by time spent in the function and its subroutines.

In this example, we see that the first entry is for ``Life::update``, the second entry is for ``main``, and so on.  42.5% of the program's execution time is spent in ``Life::update`` and its children.  ``Life::update`` only has one child, ``Life::neighbor_count``.  In the fourth entry, we see that ``Life::neighbor_count`` consumes 37.5% of the program's execution time and has no children.  As in the flat profile, the call graph shows that ``Life::neighbor_count`` was called 48,000 times.

Based on this information and what we observed in the flat profile, we can conclude that ``Life::neighbor_count`` is the main bottleneck in dummy.

For more detailed information on gprof, check out `the gprof Manual`_.

.. _the gprof Manual: http://www.gnu.org/manual/gprof-2.9.1/

