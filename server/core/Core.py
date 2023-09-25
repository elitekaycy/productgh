

# from engine.TonatonEngine import TonatonEngine
# from engine.JumiaEngine import JumiaEngine
# from engine.Scraper import Scraper
from itertools import chain

import operator

from server.core.engine.JijiEngine import JijiEngine
from server.core.engine.JumiaEngine import JumiaEngine
from server.core.engine.TonatonEngine import TonatonEngine
from server.core.engine.Scraper import Scraper


class Core():
    def __init__(self, product_name):
        self.jumia = JumiaEngine("https://www.jumia.com.gh/", f'{str(product_name)}', querytype="catalog/?q=")
        self.jiji = JijiEngine('https://jiji.com.gh/', f'{str(product_name)}', querytype=f'search/?search={product_name}&query=')
        self.tonaton = TonatonEngine("https://tonaton.com/", f'{str(product_name)}')
        self.product_name = product_name
        self.products = []
        self.tags = ['jumia', 'jiji', 'tonaton']

        
    def initialize(self):
        if len(self.product_name) < 1:
            return []
        if type(self.product_name) != type(""):
            return []
        try:
            jumia = self.jumia.process()
            jiji = self.jiji.process()
            tonaton = self.tonaton.process()

            products = list(chain(jumia, jiji, tonaton))
            return products
        except:
            print("could not get product try again")
            return []
        

    def getProducts(self):
        return self.products

    def process(self):
        new_product = sorted(self.products, key=lambda k: k['title'])
        return new_product
    
    def fetchByLink(self, obj_arr):
        tag_dict = { 
            'jumia': self.jumia,
            'jiji': self.jiji,
            'tonaton': self.tonaton
        }

        items = list()
        
        for tag_obj in obj_arr:
            get_tag = str(tag_obj.get('tag')).lower()
            get_link = tag_obj.get('link')

            try:
                get_item = tag_dict[str(get_tag)].getByLink(get_link)
                items.append(get_item)

            
            except Exception as e:
                print(f"Exception error getting the items from products {e}")
        
        print("items are ", items)
        return items
        # tag, link
    
# jumia = JumiaEngine("https://www.jumia.com.gh/", "iphone 13", querytype="catalog/?q=").process()
# jiji = JijiEngine('https://jiji.com.gh/', 'iphone 13').process()
# tonaton = TonatonEngine("https://tonaton.com/", "iphone 13").process()


# init = Core(jumia, jiji, tonaton).process()
# init = Core("laptop").process()
# print("running core process ************ ", init)
