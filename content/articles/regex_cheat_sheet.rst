Posix-style Regular Expressions
###############################

:date: 2009-09-24
:author: Stephanie Lockwood-Childs
:tags: regex
:category: cheatsheets
:slug: regex_cheatsheet
:summary: regular expression cheatsheet

Posix regular expressions cheatsheet, where "posix" refers to the syntax
supported by traditional unix utilities (grep, sed, awk) without the additions
of perl-style "extended" syntax

Regular expression syntax
=========================
  
============== ==================================  ========
    Pattern    Backslash needed (basic syntax)     Meaning
============== ==================================  ========
.              No                                  ANY character
[:class:]      No                                  Character inside pre-defined set named "class" [#]_
[abc]          No                                  Character inside given set
[a-m]          No                                  Character inside given range
[^abc]         No                                  Character NOT inside given set
(abc)          Yes                                 Cluster into pattern group
a|b            Yes                                 Alternative patterns/groups
a?             Yes                                 Repeat count: occurs zero or once
a*             No                                  Repeat count: occurs ANY number of times (including 0)
a+             Yes                                 Repeat count: occurs one or more times
a{2,5}         Yes                                 Repeat count: occurs some number within range
^abc           No                                  Anchor: beginning of line
abc$           No                                  Anchor: end of line
============== ==================================  ========
  
.. [#] there is no character class named "class", merely serving as placeholder for the real classes
       of which the most important are: alpha, digit, alnum, lower, upper, blank, and space

Basic syntax vs extended syntax
-------------------------------

The only difference between "basic syntax" and "extended syntax" [#]_ is
differing policies on backslash-ification.

Basic syntax requires certain characters to be backslashed to obtain the
special pattern-matching meaning ("Yes" in middle column of table above), while
other characters are assumed to have the special meaning *unless* they are
backslashed to be meant literally ("No" in middle column of table above).

Extended syntax is much more consistent: omit the backslash to use the
pattern-matching meaning for all special characters, or include a backslash to
take the literal meaning of a character.

.. [#] "extended" in this case refers to Posix-style extended syntax, not to perl-style extended syntax,
       which adds entirely new syntax elements not included in this cheatsheet
  
Expression grouping
-------------------

Reasons for grouping with parenthesis:

* Apply count to whole group *(abc)?*
* Use groups as alternative choices  *(abc)|(xyz)*
* When using regexes to do substitutions, groups can be recalled as part of replacement text
  
Tips
====

Convenient testing from the command-line
----------------------------------------

Use *--colour* option of *egrep* or *grep* to do testing with a candidate pattern

::

  # matches "2014-02-15"
  echo "2014-02-15: did stuff" | egrep --colour "^[^:]+"

Develop complicated patterns in extended syntax with *egrep*, then backslash-ify to basic
syntax and test with *grep* if needed

::

  # matches "product ID 4234A"
  echo "quantity 5: product ID 4234A-Z99" | egrep --colour "(product ID [0-9]+)+A"

  # matches "product ID 4234A"
  echo "quantity 5: product ID 4234A-Z99" | grep --colour "\(product ID [0-9]\+\)\+A"


Convenient testing from a browser
---------------------------------

A very friendly web app for interactive experiments with regular expressions:
small text box for the regex, large text box for the text to be matched,
and highlighting that shows all matches in real-time

http://regexr.com/

Watch out for "*" vs "+"
------------------------

Choose carefully between "any number" and "one or more"; it is a common mistake
to use "any" when the match should specify "at least one"

::

  # matches "A", but probably not intended
  echo "HUMMA" | egrep --colour "(product ID [0-9]*)*A"

  # no match
  echo "HUMMA" | egrep --colour "(product ID [0-9]+)+A"

Relevant man pages 
------------------

"man 7 regex", "man perlre"

