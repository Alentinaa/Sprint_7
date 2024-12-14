import allure
import pytest
import requests
from methods.login_courier_methods import LoginCourierMethods
from data import CourierData
from urls import URLs


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться, успешный запрос возвращает id')
    def test_login_courier(self):
        response = requests.post(URLs.LOGIN_COURIER, data=CourierData.data_correct)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Возврат ошибки, если неправильно указан логин или пароль')
    def test_login__courier_incorrect(self):
        response = LoginCourierMethods.login_courier(CourierData.data_incorrect)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @pytest.mark.parametrize("data_without_login_or_password",
                             [CourierData.data_with_empty_login, CourierData.data_with_empty_password])
    @allure.title('Возврат ошибки, если авторизация происходит с пустым полем логина или пароля')
    def test_courier_login_with_empty_fields(self, data_without_login_or_password):
        response = LoginCourierMethods.login_courier(data_without_login_or_password)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text

