import requests
from bs4 import BeautifulSoup

from server.core.engine import Scraper
# import Scraper


class JumiaEngine(Scraper.Scraper):
    def __init__(self, url, product, **kwargs):
        super().__init__(url, product, **kwargs)

    def process(self):
        url_builder = f'{self.url}{self.query}{self.product}'

        if len(self.product) < 1:
            return []

        res = []
        try:
            page = requests.get(url_builder, headers=self.headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            items = soup.find_all("article", class_="prd")

            for item in items:
                get_a = item.find('a')
                get_img = item.find('img')
                price = item.find('div', class_="prc")
                title = item.find('h3', class_="name")

                obj = {
                    "link": str(self.url + get_a.get('href')),
                    "img": str(get_img['data-src']),
                    "title": str(title.text).strip(),
                    "price": str(price.text).strip().split()[1],
                    "location ": "",
                    "tag": str(self.url),
                    "tagName":"jumia"
                }
                # print("object is ", obj)
                res.append(obj)

        except:
            return []

        return res
    
    def getByLink(self, link):
        print("get by link....")
        try:
            page = requests.get(link, headers=self.headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find('h1', '-fs20 -pts -pbxs').getText()
            get_img = soup.find('img', '-fw -fh')
            price = soup.find('span', "-b -ltr -tal -fs24 -prxs").getText()
            get_views = soup.find('a', '-plxs _more').getText()
            get_ratings = soup.find('div',"-fs29 -yl5 -pvxs")
            default_ratings = get_ratings.find('span').getText() if get_ratings else "0"
            get_description = soup.find('div', "markup -mhm -pvl -oxa -sc").getText()


            prop_type = soup.find('article', class_='-pvs')
            sample_prop = {}

            for items in prop_type:
                get_value = ''
            
                for li in items.find_all('li'):
                    get_value += li.getText() 
                    get_value + '/n'

                get_brand = items.find('h2').getText()
                sample_prop[str(get_brand)] = str(get_value)



            result = {
                "title": str(title),
                "img": get_img['data-src'],
                "price": str(price).strip(),
                "seller": "jumia",
                "views": str(get_views).split()[0][1:],
                "location": "jumia ghana",
                "types": sample_prop,
                "get_ratings": str(default_ratings).strip(),
                "description": str(get_description).strip(),
                "bookmarked": str(get_views).split()[0][1:],
                "tag": "jumia",
                
            }

            # print("results are ", result)
            return result
        except Exception as e:
            return f"Error getting link By ID , {e}"

# complete tonaton first ...
# jumia = JumiaEngine("https://www.jumia.com.gh/", "iphone 13", querytype="catalog/?q=")
# jumia.getByLink("https://www.jumia.com.gh/samsung-galaxy-a14-6.6-128gb-hdd-4gb-ram-50mp13mp-camera-light-green-12-months-warranty-138952778.html")
# print("jumia ", jumia)
