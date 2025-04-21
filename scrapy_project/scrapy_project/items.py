import scrapy

class ScrapyProjectItem(scrapy.Item):
    url = scrapy.Field()
    domain = scrapy.Field()
    type = scrapy.Field()
