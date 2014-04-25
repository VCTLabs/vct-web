================================
The Mercury Programming Language
================================

Infrequently Asked Question (IAQ): What is the Mercury programming language, and what is the point of it?
---------------------------------------------------------------------------------------------------------

The Mercury programming language was developed in Australia, by the computer science
department at the University of Melbourne.  It was funded by various grants.  The
code for the reference implementation, developed there, is all delivered under the GPL
license, i.e., entirely open-source.  There are other implementations.  The Mercury project
has left the University of Melbourne, and now may be accessed at the website www.mercurylang.org.

Programming languages and their features are classified by computer science in a number
of categories.  The ideas summarized here are well covered by Wikipedia and other net
sources, not to mention possibly an education in computer science.

Low-level versus high-level
---------------------------
A low-level language requires closer attention to the specific hardware features of the 
computer system running the program than a higher-level language would demand.  At the
lowest level is the binary command set for the cpu.  C and C++ are higher-level than 
that, and Fortran, Ruby and Ada are high level languages.  Although many higher-level
languages have special features allowing contact to specific hardware features, it is
easy in these languages to write programs that run properly with little or no attention
to the specific hardware it runs on.  
*Mercury is a high-level language.*

Practical versus research
-------------------------
A practical computer language is directed toward usage by those who are interested
in getting data processed at a reasonable time and cost.  They are interested in
answers, not arcane computer science questions.  They want their analysts and
programmers to write software with a minimal amount of bugs and which is not hard
to maintain. A research language supports scientific investigations, either 
computer science or any other investigations requiring something special not 
easily available using the usual languages (like Fortran, C, Visual Basic, Perl,
Python etc.).  In order to satisfy unique research requirements, investigators
will put up with a remarkable amount of inconvenience with respect to obtaining
an exotic language, building the compiler or other support software, struggling
with the documentation, and so on.  This is not what the commercial user wants
to deal with.
*Mercury aims to be a practical language.*

Compiled versus interpreted
---------------------------
This refers to the expected run-time environment for the language.  The same
program could be either compiled or interpreted, depending on what run-time
software is used.  When a language is compiled, it is transformed to a form 
which can be run as process under the operating environment of the computer
system.  When a language is interpreted, it is transformed to data which is
to be used by an additional program, the interpreter, which is running
on the target computer system.  The introduction of the interpreter as a 
middleman results in additional consumption of computer resources (time and/or 
space) when the program is run.
*Mercury is a compiled language.  This is in the interest of speed, as Mercury aims
to be used for large practical problems.*

Imperative versus declarative
-----------------------------
Computer languages started out all being imperative.  That means the main
emphasis is on the algorithms used to process the data.  There has been 
a movement among both computer scientists and actual software developers
in which some persons want the computer languages they use to more closely
reflect the problems they are solving.  This is in opposition to closely
reflecting the computer architecture they are using, and constitutes a shift
toward a higher level.  Some speak of "compilable requirements", meaning that
by the time you have an accurate requirements specification there is enough
exact information available that a computer could produce the acutual
runnable program.  Lisp is a good example of a declarative language, as
is Prolog, which is a logic language.
*Mercury is in the declarative camp.*

Iteration versus recursion
--------------------------
Iteration refers to repeating a process on some data by repeating an action on each
chunk of data.  In some languages, iteration is not available directly. Instead,
operation on a big structure is accomplished by finding that the big structure is made
up of a bunch of structures to the big structure, so that the routine after acting with
respect to the big structure calls itself to deal with the similar component structures.
(If this seems confusing, it is not surprising--most people not already familiar with
recursive methods need more than an introductory paragraph to get comfortable with it). 
*Mercury uses recursion, not iteration.  This goes with being a declarative logic 
language.*

Object-oriented programming
---------------------------
This is a technique in which the problem environment is modeled in terms
of "objects", which are entities each of which have data attributes and operations
upon them.  Some languages do not directly support this concept:  examples,
C or Fortran.  Some languages provide support for this style of programming,
but it is not exactly built into the language, and it is not necessary to
progam in an "object-oriented" way.  Examples:  Perl, ocaml.  Some languages
are defined from the ground up for object-oriented programming.  Examples:
C++,Python,Ruby,Java.
*Mercury is like Perl or ocaml, in that features are provided to aid programmers
who wish to adopt an object-oriented style.*

Functional programming
----------------------
This refers to languages which organize computations into functions
which have the property that the result of applying the function algorithm
to its inputs depends only on the inputs to the function.  This means
that a routine cannot have so-called "side effects", that is, do something
not implied just by the inputs.  Printing out results is a side effect,
and so are various other things you might want your computer to do.
The implication is that you can have the bulk of your code purely
functional, but you must also somewhere have a part that is not purely
functional.  For some languages this involves a few contortions, but
this is OK if they are minimal, and you gain the desired benefit of
the rest of your code (presumably the hard part) being especially
easy to understand and maintain.
*Mercury is a functional programming language like ML, Haskell or ocaml.
It has very precise tracking of the necessary "impure" code.*

Logic programming
-----------------
Logic programming languages address the problem of finding valid consequences
of given axioms and postulates.  These languages are based on mathematical 
logic, comparable to, for instance relational database being based on set
theory.  Logic programs have application in artificial intelligence.  They
also have been used to prove that certain programs are valid, i.e., are 
doing what they are supposed to.  An example would be showing an encryption
program is valid.  Program proving is so difficult it is not widely done.
"Research Continues"
*Mercury is a logic programming language.*

Backtracking versus other
-------------------------
Backtracking refers to the feature of a language which applies when at a certain
point the computation can proceed along alternative paths (each of which may
require extensive calculations) but it is not known which (if any) will provide
an acceptable result.  The backtracking feature allows a checkpoint to be taken
so that if this path does not work out, the computation revert to before the 
alternatives, and another alternative can be tried.  This could be all arranged
by the programmer, but it is immensely easier when the language supports it.
*Mercury provides backtracking, like Prolog or transaction rollback in SQL.*

Compile-time type-checking versus run-time type-checking
--------------------------------------------------------
In programs, data structures are assigned types, which determine what operations
may be performed on them.  It is easy to make mistakes, and write a programming
command which specifies an invalid operation.  There are three options for what 
happens next: 
1.  The error is not found except possibly by detection of bad output when the
program is used.  This is the worst outcome.
2.  The error is found when the program is run, because the program contains checks
which signal that an invalid operation was attempted, or that the result of an
operation was invalid.  Here at least we know that there was a problem.
3.  The error is found when the program is compiled.  The programmer can fix the
problem before delivering a bug.
Which option is desirable depends on how important is is for the program to be
reliable.  Option 2 means a lot of work by the programmer if reliability is to be
achieved.  However, it is not hard to get programs to compile, and compilers are
relatively cheap to develop and thus to buy.
Option 3 requires plenty of work to develop a compiler, and demands careful type
definition and use by the programmer.  All this is to detect bugs earlier and
make it less likely that a bug will be delivered.
*Mercury, like Ada or ocaml, performs extensive compile-time checking.*


Mercury is the result of adding functional programming (like Haskell) and full
compile-time type checking (like Ada or ocaml) to logic programming (like Prolog).
Some might look at this as having the both the desirablity and the likelyhood of
a successful effort to hybridize armadillos and hyenas.  Nonetheless, the project
has produced a running compiler and a full build environment.  It works on Linux
and Windows and some other places.  The compiler is fast and so are the resulting
programs (relatively speaking).  
