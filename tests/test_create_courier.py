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

        # постусловие
        delete_courier(payload["login"], payload["password"])


    def test_cannot_create_duplicate_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        # создаём первого курьера
        requests.post(CREATE_URL, json=payload)

        # пробуем создать дубликат
        response = requests.post(CREATE_URL, json=payload)

        assert response.status_code == 409
        assert response.json()["message"] == LOGIN_ALREADY_EXISTS

        # постусловие — удалить, даже если вдруг создался второй
        delete_courier(payload["login"], payload["password"])


    def test_create_courier_without_login(self):
        payload = {
            "password": "1234"
        }

        response = requests.post(CREATE_URL, json=payload)

        assert response.status_code == 400
        assert response.json()["message"] == NOT_ENOUGH_DATA_CREATE

        # защитное постусловие (если вдруг баг)
        delete_courier(payload.get("login"), payload.get("password"))


    def test_create_courier_without_password(self):
        payload = {
            "login": generate_random_string(10)
        }

        response = requests.post(CREATE_URL, json=payload)

        assert response.status_code == 400
        assert response.json()["message"] == NOT_ENOUGH_DATA_CREATE

        # защитное постусловие
        delete_courier(payload.get("login"), payload.get("password"))