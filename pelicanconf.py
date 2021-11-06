AUTHOR = 'Equipe Duc'
SITENAME = 'Duc Athlé Sombernon'
SITEURL = ''

THEME = 'themes/brutalist'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOGO = 'logo-duc.gif'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

MENUITEMS = [('Présentation', '/pages/presentation.html'),
             ('Entrainements', '/pages/entrainements.html'),
             ('Association', '/pages/association.html')]

             #('Événements', '/pages/evenements.html'),
             #('Infos pratiques', '/pages/informations-pratiques.html')]
