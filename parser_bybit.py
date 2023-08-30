import requests
import hashlib
import hmac
import time
import config.config as con
# Замените на ваши настоящие API ключи
API_KEY = con.api_key_bybit
API_SECRET = con.secret_key_bybit
# Основные параметры запроса
endpoint = 'https://api.bybit.com/v2/private/p2p/order/list'

# Параметры запроса для получения списка объявлений P2P
params = {
    'status': 'open',  # Фильтр по статусу: open, completed, cancelled
    'page': 1,         # Номер страницы
    'limit': 10        # Лимит результатов на странице
}

# Создание подписи (Signature)
timestamp = int(time.time() * 1000)
sign_str = f'GET{endpoint}{timestamp}'.encode('utf-8')
signature = hmac.new(API_SECRET.encode('utf-8'), sign_str, hashlib.sha256).hexdigest()

# Создание заголовков запроса
headers = {
    'API-Key': API_KEY,
    'Timestamp': str(timestamp),
    'Sign': signature
}

# Отправка GET запроса к API с параметрами
response = requests.get(endpoint, params=params, headers=headers)
data = response.json()

# Обработка полученных данных
if response.status_code == 200:
    print(data)
else:
    print("Ошибка при получении данных.")