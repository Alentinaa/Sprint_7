import requests
import helpers
from urls import URLs

class CourierMethods:

    @staticmethod
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(URLs.COURIERS_URL, json=payload)
        return response

    @staticmethod
    def generate_unique_login():
        while True:
            login = helpers.generate_random_string(10)
            response = requests.get(URLs.COURIERS_URL, params={"login": login})
            if response.status_code == 404:
                return login

    @staticmethod
    def register_new_courier_and_return_login_password():
        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(5)
        return login, password, first_name

    @staticmethod
    def register_new_courier():
        login, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
        return {"login": login, "password": password, "firstName": first_name}

    @staticmethod
    def register_new_courier_without_login():
        _, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
        return {"password": password, "firstName": first_name}

    @staticmethod
    def register_new_courier_without_password():
        login, _, first_name = CourierMethods.register_new_courier_and_return_login_password()
        return {"login": login, "firstName": first_name}
