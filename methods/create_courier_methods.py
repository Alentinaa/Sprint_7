import requests
import helpers
import allure
from urls import URLs

class CourierMethods:

    @staticmethod
    @allure.step('Регистрация курьера и возврат его логина и пароля')
    def register_new_courier_and_return_login_password():
        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(5)
        return login, password, first_name

    @staticmethod
    @allure.step('Регистрация нового курьера')
    def register_new_courier():
        login, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
        return {"login": login, "password": password, "firstName": first_name}

    @staticmethod
    @allure.step('Регистрация нового курьера без логина')
    def register_new_courier_without_login():
        _, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
        return {"password": password, "firstName": first_name}

    @staticmethod
    @allure.step('Регистрация нового курьера без пароля')
    def register_new_courier_without_password():
        login, _, first_name = CourierMethods.register_new_courier_and_return_login_password()
        return {"login": login, "firstName": first_name}
