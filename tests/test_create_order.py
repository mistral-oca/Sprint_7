import requests
import pytest
from data import *

CREATE_ORDER_URL = BASE_URL + CREATE_ORDER_PATH


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order(self, color):
        order_data = ORDER_BODY.copy()

        if color is not None:
            order_data["color"] = color

        response = requests.post(CREATE_ORDER_URL, json=order_data)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)