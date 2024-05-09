import scrapy


class NewsEntry(scrapy.Item):
    order = scrapy.Field()
    title = scrapy.Field()
    total_comments = scrapy.Field()
    points = scrapy.Field()
