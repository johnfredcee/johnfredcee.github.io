AUTHOR = 'John Connors'
SITENAME = 'Bad Byte Bootstrap Blues'
SITEURL = 'https://johnfredcee.github.io'
SITELOGO = "images/logo.png"   
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True

PATH = 'content'
OUTPUT_PATH = 'docs/'
DEFAULT_DATE='fs'
TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS="feeds/all.rss.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"
RSS_FEED_SUMMARY_ONLY = False

# Social widget
SOCIAL = (('Github', 'https://github.com/johnfredcee'),
         ('Twitter', 'https://twitter..com/johnfredcee'),
         ('Mastodon', 'https://mastodon.gamedev.place/@johnfredcee'),)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS=['images']

THEME="themes/blue-penguin-dark" 
PLUGINS = [ "pelican_gist" ] 