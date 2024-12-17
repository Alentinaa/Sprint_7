import json
import allure
import pytest
import requests
from data import Orders
from urls import URLs


class TestCreateOrder:
    @pytest.mark.parametrize('order_data', [{"color": ["BLACK"]}, {"color": ["GREY"]},
                                            {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.title('Создание заказа')
    @allure.description('Проверка, что можно указать разные вариации цветов, что тело ответа содержит track')
    def test_create_order(self, order_data):
        Orders.data_order.update(order_data)
        order_data = json.dumps(Orders.data_order)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URLs.CREATE_ORDER, data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text
        response_json = response.json()
        track = response_json.get('track')
        cancel_data = {"track": track}
        requests.put(URLs.CANCEL_ORDER, data=json.dumps(cancel_data), headers=headers)
