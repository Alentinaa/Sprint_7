import random
import string
import requests
import allure
from urls import URLs


@allure.step('Генерация случайной строки заданной длины из букв английского алфавита')
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@allure.step('Регистрация нового курьера и возврат его логина, пароля и имени')
def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    try:
        response = requests.post(URLs.COURIERS_URL, json=payload)
        response.raise_for_status()
        if response.status_code == 201 and response.json().get("ok", False):
            return {"login": login, "password": password, "first_name": first_name}
        else:
            raise ValueError
    except requests.exceptions.RequestException as e:
        raise ConnectionError(e)

