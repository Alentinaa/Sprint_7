import requests
from urls import URLs
from data import CourierData


class LoginCourierMethods:

    @staticmethod
    def register_courier():
        response = requests.post(URLs.COURIERS_URL, data=CourierData.data_correct)
        assert response.status_code == 201
        return response.json()['id']

    @staticmethod
    def login_courier(login_data):
        response = requests.post(URLs.LOGIN_COURIER, data=login_data)
        return response