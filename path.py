coba dengan full xpath

Nama barang = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[1]/div/div/a/div/div[3]/span
sebelum diskon barang = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[1]/div/div/a/div/div[4]/div/div[1]/text()[2]
sesudah diskon barang = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[1]/div/div/a/div/div[4]/div/div[3]/text()[2]
rating = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[1]/div/div/a/div/div[6]/span[1]/text()[1]
ulasan = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[1]/div/div/a/div/div[6]/span[2]/text()[2]

https://www.ruparupa.com/p/kursi-lipat-hitam.html

#homepagePromoBrandProductName

coba dengan selector

nama barang = #homepagePromoBrandProductName
sebelum diskon barang = #homepagePromoBrandPrice > div.price__initial
sesudah diskon barang = #homepagePromoBrandPrice > div.col-xs-12.price__real
rating = #productsProductCard > div > div.col-xs-12.items-center.product__review > span:nth-child(2)
ulasan = #productsProductCard > div > div.col-xs-12.items-center.product__review > span:nth-child(3)

coba dengan xpath 

Nama barang = //*[@id="homepagePromoBrandProductName"]
sebelum diskon barang = //*[@id="homepagePromoBrandPrice"]/div[1]/text()[2]
sesudah diskon barang = //*[@id="homepagePromoBrandPrice"]/div[3]/text()[2]
rating = //*[@id="productsProductCard"]/div/div[6]/span[1]/text()[1]
ulasan = //*[@id="productsProductCard"]/div/div[6]/span[2]/text()[2]




coba ganti 

nama barang =  /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[2]/div/div/a/div/div[3]/span
rating = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[2]/div/div/a/div/div[6]/span[1]/text()[1]
ulasan = /html/body/div[1]/div[2]/div/section[3]/div/div[2]/div[3]/div[2]/div/div/a/div/div[6]/span[2]/text()[2]

coba kalau setelah mengscrape halaman yang itu coba pindah ke halaman lain dan pindah halaman lain itu tergantung berapa mau kita scrap(agar bisa di batasi berapa mau scrape pagenya)

contoh link nya ini dibuat seterusnya
https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995
https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995&from=50
https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995&from=100
https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995&from=150
https://www.ruparupa.com/c/furniture.html?itm_source=mini-category-category-furnitur&itm_campaign=first-level&itm_device=desktop&size=50&sort=matching&identifier=furniture.html&categoryId=2995&from=200