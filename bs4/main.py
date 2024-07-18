from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

class RuparupaScraper:
    def __init__(self):
        chrome_driver_path = "C:\\chromedriver-win64\\chromedriver.exe"  # Sesuaikan dengan path ChromeDriver Anda
        service = Service(chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.url = 'https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995'

    def scrape(self):
        print("Memulai proses scraping...")
        self.driver.get(self.url)
        
        print("Menunggu halaman dimuat...")
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="homepagePromoBrandProductName"]'))
            )
        except Exception as e:
            print(f"Error saat menunggu halaman dimuat: {e}")
            print("Mencoba melanjutkan scraping...")
        
        print("Scrolling halaman...")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

        print("Mengambil konten halaman...")
        product_data = []
        products = self.driver.find_elements(By.XPATH, '//*[@id="productsProductCard"]')
        print(f"Jumlah produk yang ditemukan: {len(products)}")
        
        for product in products:
            try:
                name = product.find_element(By.XPATH, './/*[@id="homepagePromoBrandProductName"]').text
                original_price = product.find_element(By.XPATH, './/*[@id="homepagePromoBrandPrice"]/div[1]').text.split('\n')[-1]
                discounted_price = product.find_element(By.XPATH, './/*[@id="homepagePromoBrandPrice"]/div[3]').text.split('\n')[-1]
                rating = product.find_element(By.XPATH, './/div[6]/span[1]').text.split()[0]
                reviews = product.find_element(By.XPATH, './/div[6]/span[2]').text.split()[-1]

                product_info = {
                    'Product Name': name,
                    'Original Price': original_price,
                    'Discounted Price': discounted_price,
                    'Rating': rating,
                    'Reviews': reviews
                }
                product_data.append(product_info)
                print(f"Produk ditemukan: {name}")
            except Exception as e:
                print(f"Error saat mengekstrak data produk: {e}")

        self.driver.quit()
        return product_data

    def save_to_csv(self, data, filename):
        if not data:
            print("Tidak ada data untuk disimpan.")
            return
        
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print(f"Data telah disimpan ke {filename}")

if __name__ == "__main__":
    scraper = RuparupaScraper()
    product_data = scraper.scrape()
    if product_data:
        scraper.save_to_csv(product_data, 'product_info.csv')
    else:
        print("Tidak ada data yang berhasil di-scrape.")