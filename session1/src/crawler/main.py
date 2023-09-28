import feedparser

def parse_feed(url, show_content=False):
    feed = feedparser.parse(url)

    for entry in feed.entries:
        print('Title:', entry.title)
        print('Link:', entry.link)
        print('Published:', entry.published)

        if show_content:
            if hasattr(entry, 'content'):
                print('Content:', entry.content[0].value)
            elif hasattr(entry, 'summary'):
                print('Summary:', entry.summary)
            else:
                print('No content or summary found.')

    print('------------------------\n')

if __name__ == '__main__':
    parse_feed('http://feeds.arstechnica.com/arstechnica/index')