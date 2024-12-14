import allure
import requests
from urls import URLs


class TestOrderListIsReturned:
    @allure.title('Список заказов')
    @allure.description('В тело ответа возвращается список заказов')
    def test_order_list(self):
        response = requests.get(URLs.ORDER_LIST)
        assert response.status_code == 200 and "orders" in response.json()

