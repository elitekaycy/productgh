# get the cheapest prices first
# rank the one with the most number of clicks
# rank the one with the most number of unique visits
# rank the ones with the most likes
# remove duplicate
class Algo():
    def __init__(self, products, products_db_data) -> None:
        # products - { link, image, title, price, tag }
        # products - { title, clicks }

        self.products = products
        self.products_db = products_db_data  # dictionary

    def rank_data(self):
        temp_products = self.products
        try:
            if not temp_products:
                return []
            for value in temp_products:
                if value.get('title') in self.products_db:
                    value['clicks'] = self.products_db.get(
                        str(value.get('title')))
                else:
                    value['clicks'] = 0
            return sorted(temp_products, key=lambda x: x['clicks'], reverse=True)

        except:
            raise Exception('error ranking data')

    def dictate(self):
        print("get products_metadata as dictionary ", self.products_db)
        print("get products", self.products)
