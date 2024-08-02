import data
import sender_stand_request

# Автотест
def test_order_creation_and_retrieval():
    response = sender_stand_request.create_order(data.order_body)

    assert response.status_code == 201, f"Ошибка при создании заказа: {response.status_code}"

    track_number = response.json().get("track")
    assert track_number, "Номер трека не найден в ответе"

    print("Заказ создан. Номер трека:", track_number)

    order_response = sender_stand_request.get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка при получении данных заказа: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)