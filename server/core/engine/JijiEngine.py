import requests
from bs4 import BeautifulSoup

from server.core.engine import Scraper



class JijiEngine(Scraper.Scraper):
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
            items = soup.find_all("div", class_="b-list-advert__item")
            for item in items:
                #print("item content is ", item)
                get_a =  item.find('a')
                get_img = item.find('img')
                price = item.find('p', class_="b-list-advert__item-price")
                title = item.find('h4')
                location_set = item.find('div', class_ = "b-list-advert__item-info").get_text()

                obj = {
                    "link": str(get_a.get('href')),
                    "img": str(get_img['src']),
                    "title": str(title.text).strip(),
                    "price": str(price.text).strip().split()[1],
                    "location ": str(location_set).strip(),
                    "tag": str(self.url)
                }
                # print("object is ", obj)
                res.append(obj)
     
        except:
            print("error occured while fetching from jiji")
            return []
        
        return res




# jiji = JijiEngine('https://jiji.com.gh/', 'tripod').process()
# print("jiji ", jiji)
