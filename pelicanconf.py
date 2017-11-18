#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Ormandy'
SITENAME = 'Infinite n'+u"\u267E"+'rm'
SITEURL = 'http://chrisorm.github.io'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TWITTER_USERNAME = 'ClOrmandy'
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ClOrmandy'),
         ('LinkedIn', 'https://www.linkedin.com/in/cormandy/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
THEME = 'themes/pelican-elegant'

STATIC_PATHS = ['theme/images', 'images']
IGNORE_FILES = ['.ipynb_checkpoints']

LANDING_PAGE_ABOUT = {'title': 'Infinite Norm - Machine Learning and Related Topics', 'details':"My name is Chris. I'm a machine learning researcher based in London. I've been pursuing and studying Machine Learning for several years, and worked on more general quantitative problems before that. I'm interested in a range of ML topics, and this blog is predominantly to document things I find interesting.\n\n All views are my own, all jokes probably stolen."}
