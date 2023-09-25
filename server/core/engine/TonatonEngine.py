import requests
from bs4 import BeautifulSoup
import re

from server.core.engine import Scraper
# import Scraper



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
                get_a = item.find('a')
                get_img = item.find('img')
                price = item.find('span', class_="product__title")
                title = item.find('p', class_="product__description")
                location_set = item.find('p', class_="product__location")

                obj = {
                    "link": str(self.url) + str(get_a.get('href')[1:]),
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
    
    def string_to_number_or_zero(s):
        try:
            number = float(s)  # Use float to handle both integers and floats
            return number
        except ValueError:
            return 0
    
    def getByLink(self, link):
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            detail = soup.find('div', class_='location')
            title = '',
            location = ""
            seller = ""
            get_img = soup.find('div', class_="details__images__item").find('img')
            price = soup.find("span", 'details__side-grid__price').getText()
            
            if(detail):
                title = detail.find("h1").getText()
                location = detail.find("div", "details__location").getText()


            seller_feedback = soup.find('div', 'details__feedback')
            if seller_feedback:
                seller = seller_feedback.find('p').getText()


            get_ratings = seller_feedback.find('a').getText().split()[-1]
            get_ratings_list = list(get_ratings)
            if get_ratings_list[0] != '(':
                get_rating_num = "0"
            else:
                get_ratings_list.pop(0)
                get_ratings_list.pop(-1)
                get_rating_num = "".join(get_ratings_list)

    
            prop_type = soup.find('div', class_='details__description').find_all('div')
            sample_prop = {}

            for items in prop_type:
                get_value = items.find('p', class_="details__description__attribute-value").getText()
                get_brand = items.find('p', class_="details__description__attribute-title").getText()
                sample_prop[str(get_brand).strip()] = str(get_value).strip()

            result = {
                "title": str(title).strip(),
                "img": get_img['src'],
                "price": str(price).strip(),
                "seller": str(seller).strip(),
                "views": str(get_rating_num).strip(),
                "location": str(location).strip(),
                "types": sample_prop,
                "get_ratings": str(get_rating_num).strip(),
                "description": str(title).strip(),
                "bookmarked": str(get_rating_num).strip(),
                "tag": "Tonaton"
                
            }

            print("results are ", result)
            return result
        except Exception as e:
            return f"Error getting link By ID , {e}"
        
        return result


# tonaton = TonatonEngine("https://tonaton.com/", "laptop bag")
# tonaton.getByLink("https://tonaton.com/a_a-week-used-magic-keyboard-for-2018-and-2020-ipad-pro-12-9-uuAPoCmd9J405JZBjceYeUfL.html")
# print("tonaton ", tonaton)
