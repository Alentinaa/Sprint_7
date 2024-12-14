import random
import string
import requests
from urls import URLs


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


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

        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")

        if response.status_code == 201 and response.json().get("ok", False):
            return {"login": login, "password": password, "first_name": first_name}
        else:
            raise ValueError

    except requests.exceptions.RequestException as e:
        raise ConnectionError(e)
