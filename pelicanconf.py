#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Ormandy'
SITENAME = 'Infinite n'+u"\u267E"+'rm'
SITEURL = 'https://chrisorm.github.io:'

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
         ('linkedin', 'https://www.linkedin.com/in/cormandy/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['pelican-ipynb.markup']
THEME = './pelican-themes/blue-penguin-dark'

STATIC_PATHS = ['theme/images', 'images']
IGNORE_FILES = ['.ipynb_checkpoints']

LANDING_PAGE_ABOUT = {'title': 'Infinite Norm - Machine Learning and Related Topics', 'details':"My name is Chris. I'm a machine learning researcher based in London. I've been pursuing and studying Machine Learning for several years, and worked on more general quantitative problems before that. I'm interested in a range of ML topics, and this blog is predominantly to document things I find interesting.\n\n All views are my own, all jokes probably stolen."}

CUSTOM_MENUITEMS = (('About Me', 'about.html'),)


PAGE_PATHS = ["", "pages"]
#INDEX_URL = ''
#INDEX_SAVE_AS = INDEX_URL+'/index.html'

#ARTICLE_URL = INDEX_URL+'/{slug}'
#ARTICLE_SAVE_AS = ARTICLE_URL+'/index.html'

page_dir = 'pages'
PAGE_URL = page_dir+'/{slug}'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

DEFAULT_PAGINATION = 10


USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Home', 'index.html'),('About Me', 'about.html'),)
