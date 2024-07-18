import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RuparupaSpider(scrapy.Spider):
    name = 'ruparupa'
    start_urls = ['https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995']

    def __init__(self):
        chrome_driver_path = "C:\\chromedriver-win64\\chromedriver.exe"  # Sesuaikan dengan path ChromeDriver Anda
        service = Service(chrome_driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def parse(self, response):
        self.driver.get(response.url)
        
        # Tunggu halaman dimuat
        time.sleep(10)
        
        # Scroll halaman
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        # Gunakan Scrapy's Selector dengan konten halaman dari Selenium
        sel = Selector(text=self.driver.page_source)
        
        products = sel.xpath('//*[@id="productsProductCard"]')

        for product in products:
            yield {
                'Product Name': product.xpath('.//*[@id="homepagePromoBrandProductName"]/text()').get(),
                'Original Price': product.xpath('.//*[@id="homepagePromoBrandPrice"]/div[1]/text()').get(),
                'Discounted Price': product.xpath('.//*[@id="homepagePromoBrandPrice"]/div[3]/text()').get(),
                'Rating': product.xpath('.//*[@id="productsProductCard"]/div/div[6]/span[1]/text()').get(),
                'Reviews': product.xpath('.//*[@id="productsProductCard"]/div/div[6]/span[2]/text()').get()
            }

        self.driver.quit()

# Untuk menjalankan spider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    "FEEDS": {
        "product_info.csv": {"format": "csv"},
    },
})

process.crawl(RuparupaSpider)
process.start()
