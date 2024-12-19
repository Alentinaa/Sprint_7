import pytest
import requests
from methods.create_courier_methods import CourierMethods
from urls import URLs

@pytest.fixture(scope="function")
def register_and_delete_courier():
    login_pass = CourierMethods.register_new_courier_and_return_login_password()
    login, password, first_name = login_pass
    courier_id = None
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(URLs.COURIERS_URL, json=payload)
    if response.status_code == 201:
        login_response = requests.post(URLs.LOGIN_COURIER, json={"login": login, "password": password})
        courier_id = login_response.json().get("id")
    yield login, password, first_name, courier_id
    if courier_id:
        delete_url = URLs.DELETE_COURIER.replace(":id", str(courier_id))
        requests.delete(delete_url)