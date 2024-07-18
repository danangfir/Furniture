from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_product_info(url):
    # Set up the Selenium WebDriver dengan path absolut ke ChromeDriver
    chrome_driver_path = "C:\chromedriver-win64\chromedriver.exe"  # ganti "path/to/chromedriver" dengan path ke ChromeDriver yang sesuai
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        print(f"Mengakses URL: {url}")
        driver.get(url)
        
        print("Menunggu halaman dimuat sepenuhnya...")
        time.sleep(10)  # Anda dapat menyesuaikan waktu tunggu sesuai kebutuhan
        
        print("Scrolling halaman...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Tunggu 5 detik setelah scroll
        
        print("Mencoba mendapatkan elemen product name...")
        product_name = driver.find_element(By.CSS_SELECTOR, '#homepagePromoBrandProductName').text
        print(f"Nama Produk: {product_name}")
        
        original_price = driver.find_element(By.CSS_SELECTOR, '#homepagePromoBrandPrice > div.price__initial').text
        print(f"Harga Asli: {original_price}")
        
        discounted_price = driver.find_element(By.CSS_SELECTOR, '#homepagePromoBrandPrice > div.col-xs-12.price__real').text
        print(f"Harga Diskon: {discounted_price}")
        
        rating = driver.find_element(By.CSS_SELECTOR, '#productsProductCard > div > div.col-xs-12.items-center.product__review > span:nth-child(2)').text
        print(f"Rating: {rating}")
        
        reviews = driver.find_element(By.CSS_SELECTOR, '#productsProductCard > div > div.col-xs-12.items-center.product__review > span:nth-child(3)').text
        print(f"Ulasan: {reviews}")
        
    except Exception as e:
        print(f"Error saat scraping: {e}")
        return None
    finally:
        driver.quit()

    return {
        'Product Name': product_name,
        'Original Price': original_price,
        'Discounted Price': discounted_price,
        'Rating': rating,
        'Reviews': reviews
    }

def save_to_csv(data, filename):
    if data is None:
        print("Tidak ada data untuk disimpan.")
        return

    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)
    print(f"Data produk telah disimpan ke {filename}")

# URL of the product page
url = 'https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995'

# Scrape product information
product_data = scrape_product_info(url)

if product_data:
    # Save data to CSV
    save_to_csv(product_data, 'product_info.csv')
else:
    print("Gagal mendapatkan informasi produk.")
