import requests
from bs4 import BeautifulSoup

from server.core.engine import Scraper


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
                    "tag": str(self.url)
                }
                # print("object is ", obj)
                res.append(obj)

        except:
            return []

        return res


# jumia = JumiaEngine("https://www.jumia.com.gh/", "iphone 13", querytype="catalog/?q=").process()
# print("jumia ", jumia)
