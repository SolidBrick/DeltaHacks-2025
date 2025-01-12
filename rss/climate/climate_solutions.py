import feedparser

# URL of the RSS feed
rss_url = "https://www.climatesolutions.org/rss/climatesolutions"

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Iterate through the feed entries and print the required information
for entry in feed.entries:
    title = entry.title
    link = entry.link
    description = entry.description
    
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Link: {link}")
    print("-" * 80)
