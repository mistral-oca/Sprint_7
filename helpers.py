import requests
import random
import string
from data import BASE_URL, CREATE_COURIER_PATH, LOGIN_COURIER_PATH


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(
        BASE_URL + CREATE_COURIER_PATH,
        json=payload
    )

    if response.status_code == 201:
        login_pass = [login, password, first_name]

    return login_pass


def delete_courier(login, password):
    login_response = requests.post(
        BASE_URL + LOGIN_COURIER_PATH,
        json={"login": login, "password": password}
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")