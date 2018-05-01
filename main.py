import maya
import requests
import PyRSS2Gen

URL = "https://scrape.pastebin.com/api_scraping.php"
N = '5'

print(maya.now())
r = requests.get(URL + '?limit=' + N)
j = r.json()

RSSitems = []

for i in j:
    m = maya.when(i.get('date'), timezone='Europe/Zurich')
    r = requests.get(i.get('scrape_url'))
    RSSitems.append(
       PyRSS2Gen.RSSItem(
         title = i.get('title'),
         link = i.get('url'),
         description = r.text,
         guid = PyRSS2Gen.Guid(i.get('key')),
         pubDate = m.datetime()
       )
    )

rss = PyRSS2Gen.RSS2(
    title = "Cutbin",
    link = "http://www.pastebin.com",
    description = "Cutbin",

    lastBuildDate = maya.now().datetime(),

    items = RSSitems
    )

rss.write_xml(open("cutbin.xml", "w"))
