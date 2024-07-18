import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess

class RuparupaSpider(CrawlSpider):
    name = 'ruparupa'
    allowed_domains = ['ruparupa.com']
    start_urls = ['https://www.ruparupa.com/c/furniture.html']

    rules = (
        Rule(LinkExtractor(allow=r'c/furniture\.html\?page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for product in response.css('#productsProductCard'):
            yield {
                'Product Name': product.css('#homepagePromoBrandProductName::text').get(),
                'Original Price': product.css('#homepagePromoBrandPrice > div.price__initial::text').get(),
                'Discounted Price': product.css('#homepagePromoBrandPrice > div.col-xs-12.price__real::text').get(),
                'Rating': product.css('#productsProductCard > div > div.col-xs-12.items-center.product__review > span:nth-child(2)::text').get(),
                'Reviews': product.css('#productsProductCard > div > div.col-xs-12.items-center.product__review > span:nth-child(3)::text').get(),
            }

# Jalankan spider
if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "product_info.csv": {"format": "csv"},
        },
        "TWISTED_REACTOR": 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
    })

    process.crawl(RuparupaSpider)
    process.start()
