Command-line Editing with Readline
##################################

:date: 2007-12-28
:author: Stephanie Lockwood-Childs
:tags: readline, bash
:category: cheatsheets
:slug: readline_cheatsheet
:summary: command-line editing with readline cheatsheet

Cheatsheet for readline command-line editing, aimed towards bash but
most functions are generally applicable to other shells and apps that
use readline

Readline usage
==============

Display configuration
---------------------

Use bash 'bind' builtin command:

::

bind -v  # show readline options
bind -p  # show readline functions and corresponding key mappings
bind -q yank  # show key combination for function yank

Details:

* bind -v shows current settings in native readline command format;
  each line is a valid readline command for setting an option, e.g.
  if the option 'bell-stype' currently has value 'visible', it will
  be displayed like this:
  
::

  set bell-style visible

* bind -p shows functions and key mappings in native readline command format;
  each line is a valid readline command for mapping a function to a
  key combination, e.g. if 'ctrl-y' key combination is bound to the function
  'yank', it will be displayed like this:

::

  "\C-b": history-search-backward

* bind -q <function> will show all the key combinations that will 
  trigger the given function (if any), e.g. if the function
  'yank' is bound to 'ctrl-y' key combination, it will be
  displayed like this:

::

  yank can be invoked via "\C-y"

Modify configuration
--------------------

Use bash 'bind' builtin command:

::

  bind 'set bell-style visible'             # select visual bell-style
  bind ' "\C-b": history-search-backward'   # map history-search-backward function to ctrl-b
  bind -r "\C-k"                            # ctrl-k is unmapped

Details:

* when setting an option or mapping a function to a key combination,
  the syntax matches the output of the corresponding display command, 
  but with a pair of single quotes surrounding the whole readline command 
  (so that it will be interpreted by bash as a single entity)
* when mapping a key combination, don't allow whitespace before ':' or 
  mapping may silently fail
* bind -r <key-combo> can be used to remove a default function mapping from 
  a key sequence that tends be accidentally triggered by a habitual typo

To make changes to settings or mappings persistent, either put commands as above 
in ~/.bashrc or edit ~/.inputrc (creating it if non-existent). The syntax in
.inputrc is the same as the arguments to 'bind' command, except in the case of
unmapping a key combination (the 'bind -r' syntax being just a shortcut):

::

  # select visual bell-style
  set bell-style visible
  
  # map history-search-backward function to ctrl-b
  "\C-b" : history-search-backward  
  
  # ctrl-k is unmapped
  "\C-k" : self-insert

The advantage to using .inputrc instead of .bashrc is that custom keybindings
should be re-usable in other applications that use readline, rather than just
bash

Reusing history
---------------

::

previous-history (up arrow, ctrl-p)
next-history (down arrow, ctrl-n)
history-search-backward (unbound by default)
history-search-forward (unbound by default)
reverse-search-history (ctrl-r)
forward-search-history (ctrl-s -- poorly chosen default)
yank-nth-arg (@<number> alt-ctrl-y)
shell-expand-line (alt-ctrl-e)
magic-space (unbound by default)

Details:

* previous-history

  * goes backwards through previous commands in historical order
  * one of the most commonly used readline functions, being conveniently 
    mapped to down arrow by default

* next-history

  * goes forwards through previous commands in historical order
  * only useful for reversing direction after going backwards in history 
    via another function (sorry, no time-traveling into future here)
  * one of the most commonly used readline functions, being conveniently 
    mapped to up arrow by default

* history-search-backward

  * searches backwards through commands **starting** with the sequence 
    of characters **already typed**
  * rarely used, due to being unbound by default

* history-search-forward

  * searches forwards through commands **starting** with the sequence 
    of characters **already typed**
  * only useful for reversing direction after searching backwards in history 
    via 'history-search-backword' (sorry, still no time-traveling)
  * rarely used, due to being unbound by default

* reverse-search-history 

  * searches backwards through commands **including** the sequence of
    characters **typed after calling function**
  * can alternate between calling reverse-search-history or
    forward-search-history and typing more letters to narrow down the search

* forward-search-history

  * searches backwards through commands **including** the sequence of
    characters **typed after calling function**
  * can alternate between calling reverse-search-history or
    forward-search-history and typing more letters to narrow down the search
  * only useful for reversing direction after going backwards in history 
    via another function (nope, no time-traveling)
  * has a positively **unusable** default binding of ctrl-s, which is
    interpreted by terminals as `XOFF flow-control signal <flow_>`_ and stops all input
    until crtl-q = XON is typed

.. _flow: http://en.wikipedia.org/wiki/Software_flow_control

* yank-nth-arg

  * without number arg, yanks 1st word from prev command 
  * with number arg, yanks that word from prev command (numbering starts with 0)

* shell-expand-line

  * expands current command-line using bash expansion rules, allowing further editing 

* magic-space

  * performs history expansion and inserts space after it


Completions
-----------

::

complete (tab)
menu-complete (unbound by default)
dynamic-complete-history (alt-tab)

Details:

* complete

  * attempts to complete current word, if enough has been typed to be unique
  * one of the most commonly used readline functions, being conveniently 
    mapped to tab by default

* menu-complete

  * rotates through possible completions on successive presses

* dynamic-complete-history

  * uses history words as possible completions for current word

Editing commands
----------------

::

transpose-chars (ctrl-t)
undo (ctrl-_)
revert-line (alt-r)

Details:

* transpose-chars

  * swaps current character with previous

* undo

  * undoes last change to line

* revert-line

  * undoes all changes to line
  * useful when going back to a line from history and accidentally mangling it
  * not as useful when starting from a fresh line (unless you just want to clear it...)

Movement Commands
-----------------

::

  beginning-of-line (ctrl-a)
  end-of-line (ctrl-e)
  backward-word (alt-b)
  forward-word (alt-f)

Readline w/ history expansion
-----------------------------

set bash histverify option

::

  shopt -s histverify

when using history substitution (e.g. "!!" and so forth), 
hit 'return' and see the command after the substitution, edit if desired using normal
readline features, and hit 'return' again to finally accept the command
