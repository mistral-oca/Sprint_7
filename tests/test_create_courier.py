import requests
from data import *
from helpers import generate_random_string, delete_courier

CREATE_URL = BASE_URL + CREATE_COURIER_PATH


class TestCreateCourier:

    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(CREATE_URL, json=payload)

        assert response.status_code == 201
        assert response.json() == CREATE_COURIER_SUCCESS

        # удаляем созданного курьера
        delete_courier(payload["login"], payload["password"])


    def test_cannot_create_duplicate_courier(self, registered_courier):
        login, password, first_name = registered_courier

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(CREATE_URL, json=payload)

        assert response.status_code == 409
        assert response.json()["message"] == LOGIN_ALREADY_EXISTS


    def test_create_courier_without_login(self):
        response = requests.post(CREATE_URL, json={"password": "1234"})

        assert response.status_code == 400
        assert response.json()["message"] == NOT_ENOUGH_DATA_CREATE


    def test_create_courier_without_password(self):
        response = requests.post(CREATE_URL, json={"login": "test"})

        assert response.status_code == 400
        assert response.json()["message"] == NOT_ENOUGH_DATA_CREATE