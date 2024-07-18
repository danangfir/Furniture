Ikuti langkah-langkah ini untuk membuat project Scrapy dan menjalankan spider Anda:

Buat Project Scrapy:
Buka terminal atau command prompt, arahkan ke direktori dimana Anda ingin membuat project, dan jalankan perintah berikut:

Bash
scrapy startproject ruparupa_scraper
Gunakan kode dengan hati-hati.

Ini akan membuat direktori baru bernama ruparupa_scraper dengan struktur project Scrapy di dalamnya.

Pindahkan Spider:
Salin kode spider RuparupaSpider yang sudah Anda buat ke dalam file spiders/ruparupa_spider.py di dalam direktori project Scrapy Anda.

Masuk ke Direktori Project:
Arahkan terminal atau command prompt ke direktori project Scrapy:

Bash
cd ruparupa_scraper
Gunakan kode dengan hati-hati.

Jalankan Spider:
Sekarang Anda dapat menjalankan spider dari dalam direktori project:

Bash
scrapy crawl ruparupa -o product_info.csv
Gunakan kode dengan hati-hati.

Perintah ini akan menjalankan spider ruparupa dan menyimpan hasil scraping ke dalam file CSV "product_info.csv" di dalam direktori project.

Struktur Project Scrapy:

Setelah Anda membuat project, struktur direktori akan terlihat seperti ini:

ruparupa_scraper/
├── scrapy.cfg            # file konfigurasi project
└── ruparupa_scraper/     # modul project Anda
    ├── __init__.py
    ├── items.py          # definisi item
    ├── middlewares.py    # middleware kustom (jika ada)
    ├── pipelines.py      # pipeline kustom (jika ada)
    ├── settings.py       # pengaturan project
    └── spiders/          # spider Anda
        ├── __init__.py
        └── ruparupa_spider.py
Catatan:

Pastikan Anda berada di direktori project Scrapy saat menjalankan perintah scrapy crawl.
Jika Anda masih mengalami masalah, pastikan semua dependensi yang diperlukan terinstal dengan benar (misalnya, Selenium, webdriver Chrome).
