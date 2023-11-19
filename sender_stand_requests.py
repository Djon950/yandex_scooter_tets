import configuration
import requests
import data


#Запрос на создание заказа и сохранение номера
def post_new_orders(orders_body):
    order_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_OREDERS_PATH,
                         json=data.orders_body,
                         headers=data.headers).json()["track"]
    return order_response

#Получение информации о заказе по треку заказа
def get_track_orders():
    track_number = post_new_orders(data.orders_body)
    return requests.get(configuration.URL_SERVICE + configuration.OREDERS_NUMBER_PATH + str(track_number))
