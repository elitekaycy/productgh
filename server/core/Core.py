

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
        if len(product_name) < 1:
            return []
        if type(product_name) != type(""):
            return []
        try:
            jumia = JumiaEngine("https://www.jumia.com.gh/",
                                f'{str(product_name)}', querytype="catalog/?q=").process()
            jiji = JijiEngine('https://jiji.com.gh/', f'{str(product_name)}',
                              querytype=f'search/?search={product_name}&query=').process()
            tonaton = TonatonEngine(
                "https://tonaton.com/", f'{str(product_name)}').process()

            self.products = list(chain(jumia, jiji, tonaton))
        except:
            print("could not get product try again")
            return []

    def getProducts(self):
        return self.products

    def process(self):
        new_product = sorted(self.products, key=lambda k: k['title'])
        return new_product


# jumia = JumiaEngine("https://www.jumia.com.gh/", "iphone 13", querytype="catalog/?q=").process()
# jiji = JijiEngine('https://jiji.com.gh/', 'iphone 13').process()
# tonaton = TonatonEngine("https://tonaton.com/", "iphone 13").process()


# init = Core(jumia, jiji, tonaton).process()
# init = Core("laptop").process()
# print("running core process ************ ", init)
