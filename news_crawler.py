import scrapy
import re
from scrapy.crawler import CrawlerProcess
from news_entries import NewsEntry


def get_entry_elements(response):
    return response.xpath('//tr[@class="athing"]')


def extract_order(entry):
    order_text = entry.xpath('.//span[@class="rank"]/text()').get()
    return int(order_text.strip("."))


def extract_title(entry):
    return entry.xpath('.//span[@class="titleline"]/a/text()').get()


def get_int_value_from_text(text):
    return int(re.search(r"\d+", text).group()) if text else 0


def extract_comments_and_points(entry):
    next_sibling = entry.xpath("./following-sibling::tr")[0]
    comments_text = next_sibling.xpath(
        './/a[contains(text(), "comments")]/text()'
    ).get()
    comments = get_int_value_from_text(comments_text)

    points_text = next_sibling.xpath('.//span[@class="score"]/text()').get()
    points = get_int_value_from_text(points_text)

    return comments, points


class NewsSpider(scrapy.Spider):
    name = "hacker_news"
    start_urls = ["https://news.ycombinator.com/"]

    def parse(self, response):
        for entry in get_entry_elements(response):
            order = extract_order(entry)
            title = extract_title(entry)
            comments, points = extract_comments_and_points(entry)
            yield NewsEntry(
                order=order, title=title, total_comments=comments, points=points
            )


custom_settings = {
    "ITEM_PIPELINES": {"pipelines.JsonExportPipeline": 1},
}

process = CrawlerProcess(custom_settings)
process.crawl(NewsSpider)
process.start()
