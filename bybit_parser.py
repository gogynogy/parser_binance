from statistics import mean
import requests

def get_rub_rate_bybit():
    url = 'https://api2.bybit.com/fiat/otc/item/online'
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    params = {
        "userId": [],
        "tokenId": "USDT",
        "currencyId": "RUB",
        "payment": ['14'],
        "side": "1",
        "size": "10",
        "page": "1",
        "amount": ['10000'],
        "authMaker": False,
        "canTrade": False
    }
    response = requests.post(url=url,
                             headers=headers,
                             json=params).json()
    list = []
    for i in range(0, 8):
        list.append(float(response['result']['items'][i]['price']))
    rate = mean(list)
    part = rate - int(rate)
    if part >= 0 and part < 0.25:
        return int(rate) + 0.25
    elif part >= 0.25 and part < 0.50:
        return int(rate) + 0.5
    elif part >= 0.50 and part < 0.75:
        return int(rate) + 0.75
    else:
        return int(rate) + 1
