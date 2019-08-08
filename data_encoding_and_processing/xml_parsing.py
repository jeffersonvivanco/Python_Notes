# parse and make summary of RSS feed on Planet Python

from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
# doc represents the top of the document
doc = parse(u)

# Extract and output tags of interest
# looks for all item items under channel
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print('title: {t}, date: {d}, link: {l}'.format(t=title, d=date, l=link))
