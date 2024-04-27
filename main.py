# Жабасова Антонина, 15-я когорта — Дипломный проект. Инженер по тестированию плюс
import data
import send_requests
def get_track_order():
    response = send_requests.post_new_order(data.order_body)
    return response.json()["track"]


def test_track_order():
    track_number = get_track_order()
    response = send_requests.get_track_order(track_number)
    assert response.status_code == 200