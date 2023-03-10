from statistics import mean

import requests
import csv
import os
from pathlib import Path



class CrossratesGetter:
    HOST = 'https://p2p.binance.com/'

    def __init__(self, fiat, asset, operacion, pay_types):
        self.pay_types = pay_types or []
        self.asset = asset
        self.fiat = fiat
        self._current_page = 1
        self.operacion = operacion

    def _post(self, url, json):
        response = requests.post(url, json=json)
        return response.json()

    @property
    def request_data(self) -> dict:
        return {
            "page": self.current_page,
            "rows": 20,
            "countries": [],
            "publisherType": None,
            "fiat": self.fiat,
            "payTypes": self.pay_types,
            "tradeType": self.operacion,
            "asset": self.asset,
            "merchantCheck": False
        }

    @property
    def crossrates_url(self) -> str:
        return self.HOST + 'bapi/c2c/v2/friendly/c2c/adv/search'

    def get_crossrates(self) -> dict:
        result = self._post(self.crossrates_url, self.request_data)
        return result.get('data')

    @property
    def current_page(self) -> int:
        return self._current_page

    def next_page(self):
        self._current_page += 1

    @property
    def print_crossrate_prices(self):
        for crossrate in self.get_crossrates():
            print(crossrate['adv']['price'])

    def filepath(self, filename):
        path_to_script = os.path.dirname(os.path.abspath(__file__))
        return Path(os.path.join(path_to_script, filename))

    def write_to_csv(self, filename):
        with open(self.filepath(filename), 'w') as file:
            writer = csv.writer(file)
            data = list()
            for crossrate in self.get_crossrates():
                data.append([crossrate['adv']['price']])
            writer.writerow([self.asset])
            writer.writerows(data)
    def give_list(self):
        list = []
        for crossrate in self.get_crossrates():
            list.append(float(crossrate['adv']['price']))
        return list


def get_percent(what, percent):
    count = what - what * percent / 100
    return round(count, 2)


def calculate_profit(what, percent):
    count = what * percent / 100
    return round(count, 2)


def calculate_profit_minus_percent(what, percent):
    what = what - what * -0.01


def give_rus_course(usdt_rub):
    part = usdt_rub - int(usdt_rub)
    if part >= 0 and part < 0.25:
        return int(usdt_rub) + 0.25
    elif part >= 0.25 and part < 0.50:
        return int(usdt_rub) + 0.5
    elif part >= 0.50 and part < 0.75:
        return int(usdt_rub) + 0.75
    else:
        return int(usdt_rub) + 1
