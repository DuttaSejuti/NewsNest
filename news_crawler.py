import scrapy
import re
from scrapy.crawler import CrawlerProcess
from news_entries import NewsEntry


class NewsSpider(scrapy.Spider):
    name = "hacker_news"
    start_urls = ["https://news.ycombinator.com/"]

    def parse(self, response):
        for entry in self.get_entry_elements(response):
            order = self.extract_order(entry)
            title = self.extract_title(entry)
            comments, points = self.extract_comments_and_points(entry)
            yield NewsEntry(
                order=order, title=title, total_comments=comments, points=points
            )

    def get_entry_elements(self, response):
        return response.xpath('//tr[@class="athing"]')

    def extract_order(self, entry):
        order_text = entry.xpath('.//span[@class="rank"]/text()').get()
        return int(order_text.strip("."))

    def extract_title(self, entry):
        return entry.xpath('.//span[@class="titleline"]/a/text()').get()

    def extract_comments_and_points(self, entry):
        next_sibling = entry.xpath("./following-sibling::tr")[0]
        comments_text = next_sibling.xpath(
            './/a[contains(text(), "comments")]/text()'
        ).get()
        comments = int(re.search(r"\d+", comments_text).group()) if comments_text else 0

        points_text = next_sibling.xpath('.//span[@class="score"]/text()').get()
        points = int(re.search(r"\d+", points_text).group()) if points_text else 0

        return comments, points


custom_settings = {
    "ITEM_PIPELINES": {"pipelines.JsonExportPipeline": 1},
}

process = CrawlerProcess(custom_settings)
process.crawl(NewsSpider)
process.start()
