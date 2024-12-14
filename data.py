class CourierData:
    data_correct = {
        "login": "ninjahhh12",
        "password": "12344321"
    }
    data_incorrect = {
        "login": "test181920",
        "password": "20241010"
    }
    data_with_empty_login = {
        "login": "",
        "password": "19874634"
    }
    data_with_empty_password = {
        "login": "test181920",
        "password": ""
    }

    data_without_login ={
        "password": "12344321"
    }
    data_without_password={
        "login": "ninjahhh12"
    }

class Orders:
    data_order = {
        "firstName": "Валентина",
        "lastName": "Пахатинская",
        "address": "улица Радио 2",
        "metroStation": "Черкизовская",
        "phone": "89779876532",
        "rentTime": 6,
        "deliveryDate": "2024-12-17",
        "comment": "Test",
        "color": [
            "BLACK"
        ]
    }