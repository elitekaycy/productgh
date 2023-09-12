import unittest
import json
from app import app


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def correct_process_text(self):
        pass

    def correct_rank_products(self):
        pass

    def correct_input_search(self):
        input = "iphone 12"
        # return all the items should have a template
        # status 200
        # cannot be empty
        # response should be json type

    def fail_input_search(self):
        pass
