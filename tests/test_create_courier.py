import allure
import pytest
import requests
from methods.create_courier_methods import CourierMethods
from urls import URLs


class TestCreateCourier:

    @allure.title('Создание курьера')
    @allure.description('Курьер успешно создается')
    def test_create_courier(self, register_and_delete_courier):
        login, password, first_name, courier_id = register_and_delete_courier
        assert courier_id is not None

    @allure.title('Создание курьера')
    @allure.description('Нельзя создать двух одинаковых курьеров')
    def test_duplicate_courier(self, register_and_delete_courier):
        login, password, first_name, courier_id = register_and_delete_courier
        payload = {"login": login, "password": password, "firstName": first_name}
        response_duplicate = requests.post(URLs.COURIERS_URL, json=payload)
        assert response_duplicate.status_code == 409
        assert 'Этот логин уже используется' in response_duplicate.text

    @allure.title('Создание курьера')
    @allure.description('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        login_pass = CourierMethods.register_new_courier_without_login()
        password, first_name = login_pass["password"], login_pass["firstName"]
        payload = {"password": password, "firstName": first_name}
        response = requests.post(URLs.COURIERS_URL, json=payload)
        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Создание курьера')
    @allure.description('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        login_pass = CourierMethods.register_new_courier_without_password()
        login, first_name = login_pass["login"], login_pass["firstName"]
        payload = {"login": login, "firstName": first_name}
        response = requests.post(URLs.COURIERS_URL, json=payload)
        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text

