import requests
from bs4 import BeautifulSoup



class Scraper:
    def __init__(self, url, product, **kwargs):
        self.url = url
        self.product = product
        self.query = str(kwargs.get('querytype')) if kwargs.get('querytype') else f'search/?query='
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                         "Version/15.4 Safari/605.1.15"}

    def parseJiji(self):
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

    def parseTonaton(self):
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

    def parseJumia(self):
        url_builder = f'{self.url}{self.query}{self.product}'
        #print("url ", url_builder)

        if len(self.product) < 1:
            return []
        
        res = []
        try:
            page = requests.get(url_builder, headers=self.headers) 
            soup = BeautifulSoup(page.content, 'html.parser')
            items = soup.find_all("article", class_="prd")

            for item in items:
                get_a =  item.find('a')
                get_img = item.find('img')
                price = item.find('div', class_="prc")
                title = item.find('h3', class_="name")

                obj = {
                    "link": str(get_a.get('href')),
                    "img": str(get_img['src']),
                    "title": str(title.text).strip(),
                    "price": str(price.text).strip().split()[1],
                    "location ": "",
                    "tag": str(self.url)
                }
                print("object is ", obj)
                res.append(obj)
     
        except:
            return []
        
        return res

    def parseMelcom(self):
        url_builder = f'{self.url}{self.query}{self.product}'
        #print("url ", url_builder)

        if len(self.product) < 1:
            return []
        
        res = []
        try:
            page = requests.get(url_builder, headers=self.headers) 
            soup = BeautifulSoup(page.content, 'html.parser')
            items = soup.find_all("li", class_="product-item")
            print("soup ", soup)

            for item in items:
                get_a =  item.find('a')
                get_img = item.find('img')
                price = item.find('span', class_="price")
                title = item.find('a', class_="product-item-link")

                obj = {
                    "link": str(get_a.get('href')),
                    "img": str(get_img['src']),
                    "title": str(title.text).strip(),
                    "price": str(price.text).strip().split()[1],
                    "location ": "",
                    "tag": str(self.url)
                }
                print("object is ", obj)
                res.append(obj)
     
        except:
            return []
        
        return res
    
    def process(self):
        return []

