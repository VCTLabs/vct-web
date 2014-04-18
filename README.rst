======================================
What is this and what do I do with it?
======================================

This is the repo of VCT web content (both new and old) and must be used to 
generate all (static) content for the new site.  The output is essentially a 
bunch of html files and a theme dir for style data, while the input defaults 
to ReStructuredText source files, along with config, plugin, and theme data.

See the following upstream URLs for documentation and source:

* http://docs.getpelican.com/en/3.3.0/getting_started.html
* https://gist.github.com/josefjezek/6053301  (secondary)
* https://github.com/getpelican/pelican-themes
* https://github.com/DandyDev/pelican-bootstrap3  (current theme)
* https://github.com/getpelican/pelican-blog
* https://github.com/VCTLabs/vct-web

The first link above describes the install process for pelican; don't run 
the pelican-quickstart tool, since we already have our own repo (clone the 
vct-web repo instead).  To run the pelican build tools, however, you'll need 
to install pelican, which should pull in all the required dependencies.  The 
current rub is that not all deps are packaged in debian wheezy; I didn't 
check anything else, but at least three or four will probably be missing. 
I may look at packaging them as debs and/or ebuilds, but for now I did it 
the documented way above (more or less).

It's up to you if you want to use the python virtualenv thing to install 
into; since mine is already a debian VM I didn't bother (see below).

First things first
------------------

For debian/Ubuntu, follow the above guide, simplifying as follows::

 $ sudo apt-get install git-core build-essential python-dev python-setuptools
 $ sudo easy_install pip
 $ sudo pip install pelican markdown ghp-import shovel

Setup your git config as documented in the secondary doc link above.  Clone 
the vct web repo::

 $ git clone git@github.com:VCTLabs/vct-web.git  (needs ssh pub key on github)

or::

 $ git clone https://github.com/VCTLabs/vct-web.git

Then cd into your fresh clone and clone the themes repo; we can trim it 
down later::

 $ cd vct-web
 $ git clone --recursive https://github.com/getpelican/pelican-themes themes

We'll probably want some plugins too, but for now just the themes repo.  The 
layout of the source is fairly obvious::

 $ ls
 content            Makefile     pelicanconf.py   publishconf.py  themes
 develop_server.sh  old_content  pelicanconf.pyc  README.rst
 fabfile.py         output       pelican.pid      srv.pid

The content folder is both for static pages (content/pages) and time-ordered 
posts, eg, blog/news articles (note the use of the term "article" in the docs). 
The output folder (not tracked by git due to .gitignore) will contain the 
static files, images, themes, etc, that will be uploaded to the web server 
document root.

The old_content folder contains everything that was reachable via wget in the 
current VCT web site.

The current theme that I like so far is pelican-bootstrap3 - see the theme 
readme file from DandyDev above for config options, features, etc (also the 
primary pelican docs).  Clone it to get the latest updates::

 $ git clone https://github.com/DandyDev/pelican-bootstrap3.git

The current pelicanconf.py points directly to the pelican-bootstrap3 dir.

Lastly, I haven't tried markdown (and I haven't read anything about mixing 
the two together in the same site files) but the above install should 
support both Markdown and rSt syntax.  All I've used so far is the latter, 
and it works pretty well.  That said, there are a few HTML-specific hacks 
in the index.rst file for tweaking the layout and/or text formatting.  The 
alternative is tweaking the theme itself (templates, static css) which I'll 
leave as an exercise for the reader...

ReStructuredText references
---------------------------

* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* http://docutils.sourceforge.net/rst.html
* http://docutils.sourceforge.net/docs/ref/rst/roles.html

