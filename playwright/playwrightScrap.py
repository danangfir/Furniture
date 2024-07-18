from playwright.sync_api import sync_playwright
import csv

def scrape_data():
    with sync_playwright() as p:
        # Buka browser dan halaman
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995')

        # Array untuk menyimpan data produk
        products = []

        # Pilih elemen produk
        product_elements = page.query_selector_all('.container-card_product')

        for product_element in product_elements:
            # Ambil data produk
            product_name = product_element.query_selector('.product_name').inner_text().strip()
            price_initial = product_element.query_selector('.price_initial').inner_text().strip().replace('Rp', '').replace('.', '').replace(',', '.')
            price_real = product_element.query_selector('.price_real').inner_text().strip().replace('Rp', '').replace('.', '').replace(',', '.')
            rating = product_element.query_selector('.ui-text-4').inner_text().strip()
            reviews = product_element.query_selector('.text_grey50').inner_text().strip().replace('(', '').replace(')', '').replace('ulasan', '').strip()

            # Simpan data produk dalam array
            products.append({
                'Nama Barang': product_name,
                'Harga Sebelum Diskon': price_initial,
                'Harga Sesudah Diskon': price_real,
                'Rating': rating,
                'Ulasan': reviews
            })

        # Tutup browser
        browser.close()

        # Simpan data dalam format CSV
        with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Nama Barang', 'Harga Sebelum Diskon', 'Harga Sesudah Diskon', 'Rating', 'Ulasan'])
            writer.writeheader()
            writer.writerows(products)

        print('Data produk telah disimpan dalam products.csv')

# Ganti 'URL_HERE' dengan URL halaman yang ingin di-scrape
scrape_data()
