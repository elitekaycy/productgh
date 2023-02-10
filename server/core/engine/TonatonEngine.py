import requests
from bs4 import BeautifulSoup

from server.core.engine import Scraper



class TonatonEngine(Scraper.Scraper):
    def __init__(self, url, product, **kwargs):
        super().__init__(url, product, **kwargs)
    
    def process(self):
        url_builder = f'{self.url}{self.query}{self.product}'

        if len(self.product) < 1:
            return []
        
        res = []
        try:
            page = requests.get(url_builder) 
            soup = BeautifulSoup(page.content, 'html.parser')
            items = soup.find_all("div", class_="product__container")
            for item in items:
                #print("item content is ", item)
                get_a =  item.find('a')
                get_img = item.find('img')
                price = item.find('span', class_="product__title")
                title = item.find('p', class_="product__description")
                location_set = item.find('p', class_ = "product__location")

                obj = {
                    "link": str(get_a.get('href')),
                    "img": str(get_img['src']),
                    "title": str(title.text).strip(),
                    "price": str(price.text).strip().split()[1],
                    "location ": str(location_set.text).strip(),
                    "tag": str(self.url)
                }
                # print("object is ", obj)
                res.append(obj)
     
        except:
            print("error occured while fetching from tonaton")
            return []
        
        return res



# tonaton = TonatonEngine("https://tonaton.com/", "laptop bag").process()
# print("tonaton ", tonaton)
