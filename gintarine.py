from requests import get
from lxml.etree import HTML
from queue import Queue
visited_pages = set()
visites_articles = set()

# turim dvi eiles
pages_queue = Queue()
articles_queue= Queue()

def query_to_url(query: str) -> str:
    return f"https://www.gintarine.lt/search?q={query}"


def process_page(page_url: str):
    #articles.add(page_url)
    if page_url in visited_pages:
        return
    else:
        visited_pages.add(page_url)
    try:
        response = get(page_url)
        tree = HTML(response.text)
        for page_link in tree.xpath("//a[contains([@class='paginator__pages')]/@href"):
            page_url = "https://www.gintarine.lt" + page_link
            if page_url not in  visited_pages:
                #visited_pages.add(page_url)
                pages_queue.put(page_url)
        for arcticle_link in tree.xpath("//a[contains(@class='paginator__pages')]/@href"):
            articale_url ="https://www.gintarine.lt" + article_link
            if articale_url not in visited_articles:
                 visited_articles.add(articale_url)
                 articles_queue.put(articale_url)
        visites_articles.add(page_url)
    except Exception:
        print("Error retrieving url")


if __name__ == "__main__":
    process_page(query_to_url("dantys"))
    while not pages_queue.empty():
        page = pages_queue.get()
        print(page)
        process_page(page)

    #print(pages_queue.qsize())
    #print(articles_queue.qsize())

