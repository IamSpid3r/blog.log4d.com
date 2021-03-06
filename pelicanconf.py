#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'alswl'
SITENAME = u'Log4D'

SITEURL = 'http://lo:8000'

PATH = 'content'

THEME = '/Users/alswl/dev/myproject/python/pelican-bootstrap3/'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATHS = ['/Users/alswl/dev/project/python/pelican-plugins']
PLUGINS = ['summary', 'footer_insert', 'feed_footer_insert']

# Blogroll
LINKS =  (
)

# Social widget
SOCIAL = (
    ('RSS', 'https://blog.log4d.com/atom.xml'),
    ('Twitter', 'https://twitter.com/alswl'),
    ('Github', 'https://github.com/alswl'),
    ('Weibo', 'http://weibo.com/alswlx'),
)

MENUITEMS = (
    ('Tags', '/tags/'),
    ('Links', '/links/'),
    ('About', '/about/'),
    #('Board', '/board/'),
)

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
FEED_MAX_ITEMS = 20

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False

STATIC_PATHS = ['image', 'CNAME', 'favicon.ico']

#AUTHOR_BIO = 'Computers can change your life for the better.'
DISQUS_SITENAME = 'log4d'
GOOGLE_ANALYTICS = 'UA-8822123-3'

# Plugins

SUMMARY_END_MARKER = '<!-- more -->'

FOOTER_INSERT_HTML = u"""
<hr>
<div class="panel">
<div class="panel-body">
   <small>原文链接: <a href="https://blog.log4d.com/%(url)s">https://blog.log4d.com/%(url)s</a></small><br>
   <small>欢迎关注我的微信号：窥豹</small><br>
   <small><img src="http://upload-log4d.qiniudn.com/upload_dropbox/201605/qrcode_for_gh_17e2f9c2caa4_258.jpg"/></small><br>
   <small>3a1ff193cee606bd1e2ea554a16353ee</small>
</div>
</div>
"""

FEED_FOOTER_INSERT_HTML = u"""
<hr>
<div class="panel">
<div class="panel-body">
   <small>原文链接: <a href="https://blog.log4d.com/%(url)s">https://blog.log4d.com/%(url)s</a></small><br>
   <small>欢迎关注我的微信号：窥豹</small><br>
   <small><img src="http://upload-log4d.qiniudn.com/upload_dropbox/201605/qrcode_for_gh_17e2f9c2caa4_258.jpg"/></small><br>
   <small>3a1ff193cee606bd1e2ea554a16353ee</small>
</div>
</div>
"""

JIATHIS_PROFILE = '1604940'
