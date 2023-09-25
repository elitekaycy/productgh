import requests
from bs4 import BeautifulSoup

from server.core.engine import Scraper
# import Scraper

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
    
    def getByLink(self, link):
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find('div', 'b-advert-title-inner').getText()
            detail = soup.find_all('div', class_='b-advert-info-statistics')
            price = soup.find('span', "qa-advert-price-view-title").getText()
            prop_type = soup.find_all('div', class_='b-advert-attribute h-pb-5')
            seller = soup.find('div', 'b-seller-block__name').getText()
            sample_prop = {}

            for items in prop_type:
                get_value = items.find('div', class_="b-advert-attribute__value").getText()
                get_brand = items.find('div', class_="b-advert-attribute__key").getText()
                sample_prop[str(get_brand).strip()] = str(get_value).strip()

            get_ratings = soup.find('span', class_="b-feedback-count h-flex").getText()
            get_description = soup.find('span', 'qa-description-text').getText()
            get_img = soup.find('img', class_="b-slider-image")
            get_bookmarked = soup.find('div', class_="b-fav-button-advert__text").getText()

            result = {
                "title": str(title).strip(),
                "img": get_img['src'],
                "price": str(price).strip(),
                "seller": str(seller).strip(),
                "views": str(detail[2].getText()).strip(),
                "location": str(detail[1].getText()).strip(),
                "types": sample_prop,
                "get_ratings": str(get_ratings).split()[0],
                "description": str(get_description).strip(),
                "bookmarked": str(get_bookmarked).strip(),
                "tag": "jiji"
                
            }

            print("results are ", result)
            return result
        except Exception as e:
            return f"Error getting link By ID , {e}"
        
        return result
        


# jiji = JijiEngine('https://jiji.com.gh/', 'tripod')
# jiji.getByLink("https://jiji.com.gh/kokomlemle/accessories-and-supplies-for-electronics/yuntung-vct-5208-phone-tripod-xgIRVrjESICUVX6UeGFWHOOw.html?page=1&pos=1&cur_pos=1&ads_per_page=22&ads_count=1333&lid=UFSLyU8Vl-Av4LCq&indexPosition=0")
# print("jiji ", jiji)
