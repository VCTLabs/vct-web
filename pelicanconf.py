#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'VCT Labs'
SITENAME = u'VCT Labs'
HIDE_SITENAME = True
SITEURL = 'http://www.vctlabs.com'
SITELOGO = 'images/logo.png'
SITELOGO_SIZE = '60'

TIMEZONE = 'PST8PDT'

DEFAULT_LANG = u'en'
DATE_FORMAT = {
    'en': ('en_US','%a, %d %b %Y'),
}

WEBASSETS = (True)
TYPOGRIFY = (True)

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = False

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Gentoo Linux', 'http://www.gentoo.org'),
          ('Yocto Project', 'https://www.yoctoproject.org/'),
          ('SELinux', 'http://selinuxproject.org/page/Main_Page'),
          ('Python.org', 'http://python.org/'),
          ('Pelican', 'http://getpelican.com/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('reStructuredText', 'http://docutils.sourceforge.net/rst.html'),)

# Social widget
#SOCIAL = (('github: Donald', 'https://github.com/dburr'),
#          ('github: Steve', 'https://github.com/sarnold'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/pelican-bootstrap3'
OUTPUT_PATH = 'output'
PATH = 'content'

# Tell Pelican to add 'powerpc' to the output dir
STATIC_PATHS = ['images', 'powerpc']

# theme settings for pelican-bootstrap3
CC_LICENSE_DERIVATIVES = "ShareAlike"
CC_LICENSE_COMMERCIAL = "No"

GITHUB_USER = 'VCTLabs'
GITHUB_SHOW_USER_LINK = True
GITHUB_REPO_COUNT = "1"

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
#RECENT_POST_COUNT

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
