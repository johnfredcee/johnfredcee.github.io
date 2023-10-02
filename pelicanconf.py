AUTHOR = 'John Connors'
SITENAME = 'Bad Byte Bootstrap Blues'
SITEURL = 'https://johnfredcee.github.io'
SITELOGO = "images/logo.png"   
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True

PATH = 'content'
OUTPUT_PATH = 'docs/'
TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('Github', 'https://github.com/johnfredcee'),
         ('Twitter', 'https://twitter..com/johnfredcee'),
         ('Mastodon', 'https://mastodon.gamedev.place/@johnfredcee'),)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="themes/blue-penguin-dark" 