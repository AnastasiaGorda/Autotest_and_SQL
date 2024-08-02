# Горда Анастасия 19-я когорта. Финальный проект
import configuration
import requests
import data

# Создание заказа
# Эта функция отправляет POST-запрос на создание нового заказа.
# Аргумент body - это JSON-объект с данными заказа, который мы берем из файла data.
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS, json=body)

# Получение заказа по номеру трекера
# Эта функция отправляет GET-запрос для получения информации о заказе по трек-номеру.
# Аргумент track_number - это номер трека, который мы получаем при создании заказа.
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

# Автотест
# Эта функция выполняет последовательность шагов для проверки сценария создания и получения заказа.
def test_order_creation_and_retrieval():
    # Создание заказа и проверка успешности запроса
    response = create_order(data.order_body)
    assert response.status_code == 201, f"Ошибка при создании заказа: {response.status_code}"

    # Получение номера трека из ответа на запрос создания заказа
    track_number = response.json().get("track")
    assert track_number, "Номер трека не найден в ответе"
    print("Заказ создан. Номер трека:", track_number)

    # Получение данных заказа по номеру трека и проверка успешности запроса
    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка при получении данных заказа: {order_response.status_code}"

    # Печать данных заказа для проверки
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)