import requests
import pytest
import os
from routes.routes import Routes
from utils.DataProviders import read_json_data
from datamodels.Products import Product

test_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "product.json"))

class TestProductAPI:
    @pytest.fixture(autouse=True)
    def setup_class(self, set_up):
        self.base_url = set_up["base_url"]
        self.config_reader = set_up["config_reader"]
        self.category = "electronics"


    @pytest.mark.parametrize("data",read_json_data(test_data_path))
    def test_add_product(self, data):
        product_id = self.config_reader.get_property('productId')
        product_data = data[0]
        title = product_data["title"]
        price = float(product_data["price"])
        category = product_data["category"]
        description = product_data["description"]
        image = product_data["image"]
        payload = Product(title,price,description, category, image)
        res = requests.post(self.base_url+Routes.CREATE_PRODUCT,json = payload.__dict__)
        assert res.status_code == 201
        endpoint = self.base_url+Routes.DELETE_PRODUCT.format(id=product_id)
        res = requests.delete(endpoint)
        assert res.status_code == 200


