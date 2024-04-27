# Жабасова Антонина, 15-я когорта — Дипломный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_track_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track_number})



