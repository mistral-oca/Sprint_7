import requests
from data import *

GET_ORDERS_URL = BASE_URL + GET_ORDERS_PATH


class TestGetOrders:

    def test_get_orders_returns_list(self):
        response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

    def test_get_orders_with_non_existing_courier(self):
        response = requests.get(GET_ORDERS_URL, params={"courierId": 999999})

        assert response.status_code == 404
        assert "не найден" in response.json()["message"]