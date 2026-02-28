BASE_URL = "https://qa-scooter.praktikum-services.ru"

# courier
CREATE_COURIER_PATH = "/api/v1/courier"
LOGIN_COURIER_PATH = "/api/v1/courier/login"
DELETE_COURIER_PATH = "/api/v1/courier/"

CREATE_COURIER_SUCCESS = {"ok": True}
NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
LOGIN_ALREADY_EXISTS = "Этот логин уже используется. Попробуйте другой."

# login
NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

# orders
CREATE_ORDER_PATH = "/api/v1/orders"
GET_ORDERS_PATH = "/api/v1/orders"

ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}