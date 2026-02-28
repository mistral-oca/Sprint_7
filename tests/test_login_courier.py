import requests
from data import *

LOGIN_URL = BASE_URL + LOGIN_COURIER_PATH


class TestLoginCourier:

    def test_courier_can_login(self, registered_courier):
        login, password, _ = registered_courier

        response = requests.post(LOGIN_URL, json={
            "login": login,
            "password": password
        })

        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_without_login(self):
        response = requests.post(LOGIN_URL, json={"password": "1234"})

        assert response.status_code == 400
        assert response.json()["message"] == NOT_ENOUGH_DATA_LOGIN

    def test_login_without_password(self):
        response = requests.post(LOGIN_URL, json={"login": "test"})

        assert response.status_code == 400
        assert response.json()["message"] == NOT_ENOUGH_DATA_LOGIN

    def test_login_with_wrong_password(self, registered_courier):
        login, password, _ = registered_courier

        response = requests.post(LOGIN_URL, json={
            "login": login,
            "password": "wrongpassword"
        })

        assert response.status_code == 404
        assert response.json()["message"] == ACCOUNT_NOT_FOUND

    def test_login_non_existing_user(self):
        response = requests.post(LOGIN_URL, json={
            "login": "nonexisting",
            "password": "1234"
        })

        assert response.status_code == 404
        assert response.json()["message"] == ACCOUNT_NOT_FOUND