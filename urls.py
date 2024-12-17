class URLs:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIERS_URL = f'{BASE_URL}courier'
    LOGIN_COURIER = f'{BASE_URL}courier/login'
    DELETE_COURIER = f'{BASE_URL}courier/:id'
    ORDER_LIST = f'{BASE_URL}orders'
    CREATE_ORDER = f'{BASE_URL}orders'
    CANCEL_ORDER = f'{BASE_URL}orders/cancel'

