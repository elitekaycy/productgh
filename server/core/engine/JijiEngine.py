import requests
from bs4 import BeautifulSoup

from server.core.engine import Scraper


class JijiEngine(Scraper.Scraper):
    def __init__(self, url, product, **kwargs):
        super().__init__(url, product, **kwargs)

    def process(self):
        query = f'search/?search={self.product}&query='
        url_builder = f'{self.url}{query}{self.product}'

        if len(self.product) < 1:
            return []

        res = []
        try:
            page = requests.get(url_builder)
            soup = BeautifulSoup(page.content, 'html.parser')
            items = soup.find_all(
                "div", class_="b-list-advert__item-wrapper")
            for item in items:
                get_a = item.find('a')
                get_img = item.find('img')
                price = item.find('div', class_="b-list-advert__price")
                title = item.find('div', class_="b-advert-title-inner")
                location_set = item.find(
                    'span', class_="b-list-advert__region__text").get_text()

                obj = {
                    "link": str(self.url) + str(get_a.get('href'))[1:],
                    "img": str(get_img['src']),
                    "title": str(title.text).strip(),
                    "price": str(price.text).strip().split()[1],
                    "location ": str(location_set).strip(),
                    "tag": str(self.url)
                }
                res.append(obj)

        except:
            print("error occured while fetching from jiji")
            return []

        return res


jiji = JijiEngine('https://jiji.com.gh/', 'tripod').process()
# print("jiji ", jiji)
