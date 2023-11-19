import sender_stand_requests

# Проверка, что код ответа равен 200
def test_order_data_acquisition():
    assert sender_stand_requests.get_track_orders().status_code == 200