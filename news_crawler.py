import scrapy
import re
from scrapy.crawler import CrawlerProcess
from news_entries import NewsEntry


class NewsSpider(scrapy.Spider):
    name = "hacker_news"
    start_urls = ["https://news.ycombinator.com/"]

    def parse(self, response):
        entries = response.xpath('//tr[@class="athing"]')
        for entry in entries:
            order_text = entry.xpath('.//span[@class="rank"]/text()').get()
            order = int(order_text.strip("."))
            title = entry.xpath('.//span[@class="titleline"]/a/text()').get()

            next_sibling = entry.xpath("./following-sibling::tr")[0]
            comments_text = next_sibling.xpath(
                './/a[contains(text(), "comments")]/text()'
            ).get()
            comments = (
                int(re.search(r"\d+", comments_text).group()) if comments_text else 0
            )

            points_text = next_sibling.xpath('.//span[@class="score"]/text()').get()
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
