import scrapy
import json
from urllib.parse import urlparse
from scrapy_project.items import ScrapyProjectItem

class TVBrandsSpider(scrapy.Spider):
    name = "tv_brands"
    
    def start_requests(self):
        with open('config/target_sites.json') as f:
            sites = json.load(f)
        for url in sites['tv_brands']:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = ScrapyProjectItem()
        item['url'] = response.url
        item['domain'] = urlparse(response.url).netloc
        item['type'] = 'tv_brand'
        yield item
        
        for link in response.css('a::attr(href)').getall():
            if link.startswith('http'):
                sub_item = ScrapyProjectItem()
                sub_item['url'] = link
                sub_item['domain'] = urlparse(link).netloc
                sub_item['type'] = 'tv_brand_sub'
                yield sub_item
