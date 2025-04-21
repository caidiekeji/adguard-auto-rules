import scrapy
import json
from urllib.parse import urlparse
from scrapy_project.items import ScrapyProjectItem

class StreamingSpider(scrapy.Spider):
    name = "streaming_platforms"
    
    def start_requests(self):
        with open('config/target_sites.json') as f:
            sites = json.load(f)
        for url in sites['streaming_platforms']:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = ScrapyProjectItem()
        item['url'] = response.url
        item['domain'] = urlparse(response.url).netloc
        item['type'] = 'streaming'
        yield item
        
        for link in response.css('a::attr(href)').getall():
            if link.startswith('http'):
                sub_item = ScrapyProjectItem()
                sub_item['url'] = link
                sub_item['domain'] = urlparse(link).netloc
                sub_item['type'] = 'streaming_sub'
                yield sub_item
