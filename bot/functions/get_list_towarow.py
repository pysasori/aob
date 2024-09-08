import requests
from .error_message_tg import error_message_tg


def get_list_towarow(url, id):
    # URL вашего Django API
    url = f'http://192.168.0.{url}:6543/api/'

    # Параметры запроса (в данном случае передаем id=1)
    params = {'id': id}

    # Отправляем GET запрос
    response = requests.get(url, params=params)

    # Проверяем статус код ответа
    if response.status_code == 200:
        print(response.json()['id'])
        # Выводим ответ в формате JSON
        data = response.json()['data']
        return data
    else:
        error_message_tg()
        print('Ошибка при запросе:', response.status_code)

