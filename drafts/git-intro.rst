==========================================================================
Using the Git repository - a basic introduction with command-line examples
==========================================================================

Getting Started
===============

Installing git
--------------

Fedora 7, Ubuntu 8, and later: The git-core package is available through the standard package repositories.  Other Linux and BSD environments should be similar, eg, *emerge git* on Gentoo will install the needed commands and dependencies.  If your platform does not package git, you may download the latest stable release from "http://www.kernel.org/pub/software/scm/git/".  Windows users are recommended to install either TortiseGit or Cygwin (the latter includes a bash shell and many other Linux programs).

Basic Tasks
-----------

First, note that you can get documentation for a command such as git log --graph with::

	$ man git-log

or::

	$ git help log

With the latter command, you can use the manual viewer of your choice; see the git-help(1) man page for more information.

You should also configure git with your name and preferred email address before doing any operation. The easiest way to do so is::

	$ git config --global user.name "Your Name Here"
	$ git config --global user.email you@domain.example.com

Download a new package from the repository::

	$ git clone https://username@github.com/VCTLabs/vct-web.git

To avoid the username part of the above URL, use a .netrc file to store your login ID, or use an ssh public key on github and the ssh URL::

    $ git clone git@github.com:VCTLabs/vct-web.git

Update a package to the latest upstream version ("fast-forward merge")::

	$ cd package-name
	$ git pull origin <branch-name>

or more simply, to pull from the default branch/location from which you cloned::

	$ cd package-name
	$ git pull
	
will pull from the origin repository and default branch defined in the package-name/.git/config file.

One way to undo all local modifications::

	$ git checkout -f

To check in your own local modifications (e.g. do some refactoring, fix a bug, or apply a patch)::

	$ cd package-name
	$ vi file1.c file2.c file1.h

.. admonition:: Note

   Don't forget to run 'git add' and 'git rm' if adding or removing files.

To check in all local modifications to your local repository::

	$ git commit -a -m "fix for ticket 345"

Undo recent commits
-------------------

Sometimes you have made a few commits, or just pulled a change, and simply want those commits to go away::

	$ cd package-name
	$ git reset --hard HEAD~2	# make last 2 commits disappear

This will "disappear" the top two commits. **DO NOT** do this, if you've already pushed said commits (at least not without coordination with others who may have pulled those commis).  Note that this is quite different from *git revert*, which applies a reversed patch as an additional commit.

Listing changes in your working dir, in diff format
---------------------------------------------------

Display changes since last 'git add' or 'git rm'::

	$ git diff

Display changes since last commit::

	$ git diff HEAD

Obtain summary of all changes in working dir::

	$ git status

List all commits on the current branch, with descriptions::

	$ git log

The 'git log' option "-p" shows diffs in addition to commit messages. The option "--stat" shows the diffstat.

List all commits to a specific file::

	$ git log net/file3.c

Branches
========

List all local branches (add -a to remote branches too)::

	$ git branch

Make desired branch current in working directory::

	$ git checkout $branch

Create a new branch from master, and make it current::

	$ git checkout -b my-new-branch-name master

Examine which branch is current::

	$ git status

('git branch' also shows you the current branch, using a "*" to indicate this)

Obtain a diff between current branch, and master branch
-------------------------------------------------------

In most trees with branches, .git/refs/heads/master contains the current 'vanilla' upstream tree, for easy diffing and merging. (in trees without branches, 'master' simply contains your latest changes).  The following is equivalent to git diff HEAD, when used with HEAD branch::

	$ git diff master..HEAD

Obtain a list of changes between current branch, and master branch::

	$ git log master..HEAD

(this is equivalent to git log, when used with HEAD)

Rather than full changeset descriptions, obtain a one-line summary of each changes::

	$ git shortlog master..HEAD

Merging changes from one branch to another
------------------------------------------

Suppose that you do work on branch A and branch B, and after work on those two branches is complete, you merge the work into mainline branch M::

	$ git checkout master	# switch to branch master
	$ git merge drafts		# merge drafts into master
	$ git merge new-theme	# merge new-theme into master

Misc. Topics
============

Optimize your repository
------------------------

git is heavily optimized for fast storage and retrieval on a per-command basis. However, over a long period of time, it can be useful to perform further optimizations, including packing all git objects into single "packfile" for fast retrieval and less wasted disk space.  The following::

	$ cd package-name
	$ git gc

will optimize your repository.  You don't need to run this frequently — git is quite fast even without it.  See the 'git gc' man page for more details.

Don't forget to download tags from time to time
-----------------------------------------------

git pull only downloads SHA1-indexed object data, and the requested remote head.  This misses updates to the .git/refs/tags/ and .git/refs/heads/ directories.  For tags, run git fetch --tags in your local repo.

Tagging a particular commit
---------------------------

In many cases, you will want to give interesting or significant commits a name, known as a tag.  The Linux kernel uses tags for each kernel version: "v2.6.21", "v2.6.22", etc.  For example, to create a new tag after a particular commit::

	$ cd package-name
	$ git tag my-tag

This creates a new tag named "my-tag", based on the current commit. You will probably do a lot more with tagging, including GPG-signing, so read the man page for more details.

Further reading
---------------

Another good introduction is the `Git tutorial`_

.. _Git tutorial: http://schacon.github.com/git/gittutorial.html

More complete documentation is available in the `Git community book`_, as well as the `Git Reference`_ and git man page documentation.

.. _Git community book: http://gitref.org/

.. _Git Reference: http://gitref.org/

And for even more detailed information on Git, check out `the Pro Git book`_.

.. _the Pro Git book: http://progit.org/book/

