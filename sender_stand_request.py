# Горда Анастасия 19-я когорта. Финальный проект
import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}{configuration.GET_ORDER_TRACK}{track_number}"
    response = requests.get(get_order_url)
    return response