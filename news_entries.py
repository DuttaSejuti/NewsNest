import scrapy

class NewsEntry(scrapy.Item):
    title = scrapy.Field()
    order = scrapy.Field()
    total_comments = scrapy.Field()
    points = scrapy.Field()
