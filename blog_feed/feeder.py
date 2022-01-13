import feedparser

rss = feedparser.parse("https://cat-minzzi.tistory.com/rss")
entries = rss["entries"]
for entry in entries:
    print(entry["title"])
