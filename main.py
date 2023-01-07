from tokopedia.tokopedia import Tokopedia

def main():
    scrapper = Tokopedia(keyword='ayam goreng')
    avg_price = scrapper.average()
    print(avg_price)
    scrapper.daftar_harga(title='Daftar Harga') 
    

if __name__ == '__main__':
    main()