import requests

def get_lkr_rates():
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    headers = {
        'Accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
               }
    params = {
        'asset': "USDT",
        'countries': [],
        'fiat': "LKR",
        'page': 1,
        'payTypes': ['BANK',],
        'proMerchantAds': False,
        'publisherType': None,
        'rows': 10,
        'shieldMerchantAds': False,
        'tradeType': "SELL"
    }

    response = requests.post(url=url, headers=headers, json=params).json()
    return response

def get_rub_rates():
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    headers = {
        'Accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
               }
    params = {
        'asset': "USDT",
        'countries': [],
        'fiat': "RUB",
        'page': 1,
        'payTypes': ['PostBankNew',],
        'proMerchantAds': False,
        'publisherType': None,
        'rows': 10,
        'shieldMerchantAds': False,
        'tradeType': "BUY"
    }

    response = requests.post(url=url, json=params).json()
    return response

print(get_lkr_rates())
print(get_rub_rates())