import scrapy
import re
from scrapy.crawler import CrawlerProcess
from news_entries import NewsEntry


class NewsSpider(scrapy.Spider):
    name = "hacker_news"
    start_urls = ["https://news.ycombinator.com/"]

    def parse(self, response):
        ENTRY_SELECTOR = '//tr[@class="athing"]'
        ORDER_SELECTOR = './/span[@class="rank"]/text()'
        TITLE_SELECTOR = './/span[@class="titleline"]/a/text()'
        COMMENTS_SELECTOR = './/a[contains(text(), "comments")]/text()'
        POINTS_SELECTOR = './/span[@class="score"]/text()'

        for entry in response.xpath(ENTRY_SELECTOR):
            order_text = entry.xpath(ORDER_SELECTOR).get()
            order = int(order_text.strip("."))
            title = entry.xpath(TITLE_SELECTOR).get()

            next_sibling = entry.xpath("./following-sibling::tr")[0]
            comments_text = next_sibling.xpath(COMMENTS_SELECTOR).get()
            comments = (
                int(re.search(r"\d+", comments_text).group()) if comments_text else 0
            )

            points_text = next_sibling.xpath(POINTS_SELECTOR).get()
            points = int(re.search(r"\d+", points_text).group()) if points_text else 0

            yield NewsEntry(
                order=order, title=title, total_comments=comments, points=points
            )


process = CrawlerProcess(
    settings={
        "FEEDS": {
            "output.json": {
                "format": "json",
            },
        },
    }
)

process.crawl(NewsSpider)
process.start()
