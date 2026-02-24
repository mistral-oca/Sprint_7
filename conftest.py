import pytest
from helpers import register_new_courier_and_return_login_password, delete_courier


@pytest.fixture
def registered_courier():
    login_pass = register_new_courier_and_return_login_password()
    assert login_pass != []

    login, password, first_name = login_pass

    yield login, password, first_name

    delete_courier(login, password)