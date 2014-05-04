Yet another vim cheatsheet: vim basics
######################################

:date: 2005-02-24
:tags: vim, vi
:category: cheatsheets
:slug: vim_basics_cheatsheet
:author: Stephanie Lockwood-Childs
:summary: vim cheatsheet covering editing basics

vim cheatsheet that covers editing basics (and which mostly applies
to other vi implementations as well)

vim basics cheatsheet
=====================

This cheatsheet is intended to help those who "barely can get around"
in vi to become competent vim users. It is not intended for complete
beginners, since an understanding of vi editing modes is assumed.

Most of these commands come from original vi, and theoretically will work in
simple vi applications rather than just vim. "Theoretically" refers to a caveat
that many embedded systems run an extremely cut-down busybox vi, leaving
out a lot of supposedly standard vi features (sometimes explicitly warning 
that a feature is "not implemented", and sometimes just doing a weird edit
instead of the intended one).

Notable vim-specific commands included in this list for being incredibly
useful when available:

* visual selection commands, in particular, column-selection mode for convenient
  editing of text in fixed-width columns
* macro recording and playback, which can simplify repetitive editing tasks so easily
  that it has replaced many a throw-away perl/python/ruby/whatever script

MOVEMENT
--------

::

 absolute motion
    go to line number: <line number>G
    go to last line: G (without a number)
    show 
 relative motion
    by character: arrow keys or hjkl (mneumonic: video game controls)
    by word: w forwards and b backwards
    by page: <ctrl>f forwards and <ctrl>b backwards
    beginning of line: 0
    end of line: $
 search
    initial search: / forwards and ? backwards, followed by pattern
    find next: n forwards and N backwards
    find word under cursor: #
 markers
    go to marked line: '<marker letter> (normal single quote)
    go to marked character: \`<marker letter> (back tick)

ACTIONS
-------

::

 insert new text
    insert before letter under cursor: i
    insert at beginning of line: I
    append after letter under cursor: a
    append after end of line: A
    open new line after current line: o
    open new line before current line: O
 copy text (Yank)
    copy range: y (followed by motion to end of range)
    copy line: yy
 delete text
    delete character: x (mneumonic: like typewriter strikeout)
    backspace character: X
    delete range: d (followed by motion to end of range)
    delete line: dd
 paste text
    put after cursor: p
    put before cursor: P
 replace text
    replace single character: r 
    enter replace mode: R (text not typed over is unchanged)
 change text (like delete followed by insert)
    change range: c (followed by motion to end of range)
    change to end of line: C 
 undo/redo
    undo last action: u
    undo all actions on current line: U
    redo last action: <ctrl>r
 line formatting
    join lines: J
    reformat range to current textwidth: gq (followed by motion to end of range)
 macros
    define macro: q<letter for macro>
    replay macro: @<letter for macro>

DEFINING RANGES
---------------

::

 markers
    set marker: m<marker letter>
 visual select (type again to cancel)
    visual select: v (followed by motion to end of range)
    line-mode visual select: V (followed by motion to end of range)
    column-mode visual select: <ctrl>v (followed by motion to end of range)

IMPORTANT COLON COMMANDS
------------------------

::

 help :help
 write file :w (use :w! to force a write when you get a warning)
 quit :q (use :q! to force a quit when you get a warning)
 revert to saved :e!
 edit another file :e <filename>
 syntax highlighting :syntax on (or "off" to disable)
 set options :set <option> (use ":set all" to see list of available options)
 horizontally split window :sp 
 vertically split window :vsp 
 substitute :<range> s/<search pattern>/<replacement text>/

RANGE SYNTAX FOR COLON COMMANDS
-------------------------------

::

 'a,'z  = from marker a to marker z
 .,$ = from current line to last line 
 1,. = from first line to last line 
 %  = whole file (short for "1,$")

USEFUL SET OPTIONS
------------------

::

 enable paste mode (turn off default settings that make pasting act weird) :set paste
 show command being constructed :set showcmd
 show cursor line & column :set ruler
 number lines :set number
 ignore case on searches :set ignorecase (or "ic")
 automatically break long lines :set textwidth=80 (or "tw")
 convert from dos line-endings :set fileformat=unix (then save the file)
