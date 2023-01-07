import tokopedia.constant as constant
import requests
import re
import functools

class Tokopedia:
    def __init__(self, keyword = "indomie goreng") -> None:
        keyword = keyword.strip()
        fkeyword = keyword.replace(' ', '%20')
        self.keyword = keyword
        self.fkeyword = fkeyword

    
    def grab(self):
        payload = [
            {
            "operationName": constant.OPERATIONNAME,
            "variables": {
            "params": f"{constant.PARAM1}{self.keyword}{constant.PARAM2}"
            },
            "query": constant.QUERY 
            }]
        req = requests.post(constant.URL, json=payload).json()
        rows = req[0]['data']['ace_search_product_v4']['data']['products']
        return rows

    def average(self):
        prices = []
        pattern = re.compile(r'\D')
        for row in self.grab():
            price = str(row['price']).strip()
            price = pattern.sub('',price)
            price = int(price)
            prices.append(price)
        average = functools.reduce(lambda x,y : ((x + y) / 2), prices)
        average = round(average)
        kformat = "{:,.2f}".format(average)
        rpformat = f'Rata-rata harga dari {len(prices)} produk {self.keyword} adalah Rp {kformat}'
        return rpformat

    def daftar_harga(self, title=None):
        if title is None:
            title = f"Daftar Harga {self.keyword}"
        file1 = open(f"{title}.txt", "a") 
        file1.write("Nama Produk\tHarga\tLink Produk \n")
        file1.close()
        rows = self.grab()

        for i in range(len(rows)):
            file1 = open(f"{title}.txt", "a")
            file1.write(f"{rows[i]['name']}\t{rows[i]['price']}\t{rows[i]['url']}\n")
            file1.close()