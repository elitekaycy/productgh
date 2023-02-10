import requests
from bs4 import BeautifulSoup
import Scraper


class FrankoTrading(Scraper.Scraper):
    def __init__(self, url, product, **kwargs):
        super().__init__(url, product, **kwargs)
    
    def process(self):
        url_builder = f'{self.url}{self.query}{self.product}&post_type=product'
        print("url ", url_builder)

        if len(self.product) < 1:
            return []
        
        res = []
        try:
            page = requests.get(url_builder, headers=self.headers) 
            soup = BeautifulSoup(page.content, 'html.parser')
            items = soup.find_all("li", class_="product")
            # print(soup.prettify())
            for item in items:
                #print("item content is ", item)
                get_a =  item.find('a')
                get_img = item.find('img')
                title = item.find('h2').get_text()
                price = item.find('span', class_="amount").get_text()

                obj = {
                    "link": str(get_a.get('href')),
                    "img": str(get_img['src']),
                    "title": str(title),
                    "price": str(price).strip().split()[1],
                    "location ": "",
                    "tag": str(self.url)
                }
                # print("object is ", obj)
                res.append(obj)
     
        except:
            print("error occured while fetching from " + self.url)
            return []
        
        return res




franko = FrankoTrading('https://frankotrading.com/', 'iphone', querytype="?s=").process()
print("franko ", franko)
