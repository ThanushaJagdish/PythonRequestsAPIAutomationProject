import requests
import pytest
from routes.routes import Routes
from payloads.Payloads import Payload

class TestProductAPI:
    @pytest.fixture(autouse=True)
    def setup_class(self, set_up):
        self.base_url = set_up["base_url"]
        self.config_reader = set_up["config_reader"]
        self.category = "electronics"

    @pytest.mark.order(1)
    def test_get_all_products(self):
        response = requests.get(self.base_url+Routes.GET_ALL_PRODUCTS)
        assert response.status_code == 200
        data = response.json()
        #print(json.dumps(data, indent=4))
        assert len(data) > 0

    @pytest.mark.order(2)
    def test_get_single_product_by_id(self):
        prod_id = self.config_reader.get_property("productId")
        endpoint = self.base_url + Routes.GET_PRODUCT_BY_ID.format(id=prod_id)
        response = requests.get(endpoint)
        assert response.status_code == 200
        data = response.json()
        #print(json.dumps(data, indent=4))
        assert len(data) > 0
        assert data['id']==int(prod_id)

    @pytest.mark.order(3)
    def test_get_limited_products(self):
        limit = self.config_reader.get_property("limit")
        endpoint = self.base_url + Routes.GET_PRODUCTS_WITH_LIMIT.format(limit=limit)
        response = requests.get(endpoint)
        assert response.status_code == 200
        data = response.json()
        #print(json.dumps(data, indent=4))
        assert len(data) == int(limit)

    @pytest.mark.order(4)
    def test_get_sorted_products_desc(self):
        endpoint = self.base_url + Routes.GET_PRODUCTS_SORTED.format(order='desc')
        response = requests.get(endpoint)
        assert response.status_code == 200
        data = response.json()
        #print(json.dumps(data, indent=4))
        assert len(data) > 0
        ids = [item["id"] for item in data]
        assert ids == sorted(ids,reverse=True)

    @pytest.mark.order(5)
    def test_get_sorted_products_asc(self):
        endpoint = self.base_url + Routes.GET_PRODUCTS_SORTED.format(order='asc')
        response = requests.get(endpoint)
        assert response.status_code == 200
        data = response.json()
        #print(json.dumps(data, indent=4))
        assert len(data) > 0
        ids = [item["id"] for item in data]
        assert ids == sorted(ids)

    @pytest.mark.order(6)
    def test_all_categories(self):
        response = requests.get(self.base_url+Routes.GET_ALL_CATEGORIES)
        assert response.status_code == 200
        data = response.json()
        #print(json.dumps(data, indent=4))
        expected_categories = set(["electronics","jewelery","men's clothing","women's clothing"])
        assert set(data)== expected_categories

    @pytest.mark.order(7)
    def test_get_product_by_category(self):
        endpoint = self.base_url+Routes.GET_PRODUCTS_BY_CATEGORY.format(category=self.category)
        res = requests.get(endpoint)
        assert res.status_code == 200
        data = res.json()
        #print(json.dumps(data, indent=4))
        prod_category_received = set([item['category'] for item in data])
        assert all(category == "electronics" for category in prod_category_received)

    @pytest.mark.order(8)
    @pytest.mark.dependency(name="add product")
    def test_add_product(self):
        product_payload = Payload().product_payload()
        res = requests.post(self.base_url+Routes.CREATE_PRODUCT,json = product_payload.__dict__)
        assert res.status_code == 201
        data = res.json()
        #print(json.dumps(data, indent=4))
        assert data['title'] == product_payload.title
        assert data['price'] == product_payload.price
        assert data['description'] == product_payload.description
        assert data['category'] == product_payload.category

    @pytest.mark.order(9)
    @pytest.mark.dependency(depends=["add product"])
    def test_update_product(self):
        product_id = self.config_reader.get_property("productId")
        endpoint = self.base_url+Routes.UPDATE_PRODUCT.format(id=product_id)
        payload = Payload().product_payload().__dict__
        res = requests.put(endpoint,json=payload)
        assert res.status_code == 200
        data = res.json()
        #print(json.dumps(data,indent=4))
        assert data['title'] == payload['title']

    @pytest.mark.order(10)
    @pytest.mark.dependency(depends=["add product"])
    def test_delete_product(self):
        product_id = self.config_reader.get_property("productId")
        endpoint = self.base_url+Routes.DELETE_PRODUCT.format(id=product_id)
        res = requests.delete(endpoint)
        assert res.status_code == 200



