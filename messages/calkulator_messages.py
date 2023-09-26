from statistics import mean

from bybit_parser import get_rub_rate_bybit
from p2p_parser import give_rus_course, CrossratesGetter, get_percent

start_calkulator = 'Выбери первую валюту'
second_kalculators = 'Выбери вторую валюту'
def third_kalculators(first, second):
    return f'Какую сумму надо перевести из {first} в {second}'

def get_curensy_info(count):
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    course_LKR = int(mean(LKR_USDT.give_list()))
    course_RUB = get_rub_rate_bybit()
    cost_usdt = round(count/get_percent(course_LKR, 1), 2)
    course_minus_persent = round(get_percent(course_LKR, 1) / course_RUB, 2)
    curency = course_LKR / course_RUB
    return f'Сумма LKR {count}\nСтоимость USDT: {cost_usdt}\nКурс -1%: {course_minus_persent}\n\n' \
           f'8%      {get_percent(curency, 8)}      {round(count / get_percent(curency, 8), -2)} rub\n' \
           f'profit USDT: {round((int(round(count / get_percent(curency, 8), -2))/course_RUB) - cost_usdt, 2)}\n\n' \
           f'7%      {get_percent(curency, 7)}      {round(count / get_percent(curency, 7), -2)} rub\n' \
           f'profit USDT: {round((int(round(count / get_percent(curency, 7), -2))/course_RUB) - cost_usdt, 2)}\n\n' \
           f'6%      {get_percent(curency, 6)}      {round(count / get_percent(curency, 6), -2)} rub\n' \
           f'profit USDT: {round((int(round(count / get_percent(curency, 6), -2))/course_RUB) - cost_usdt, 2)}\n\n' \
           f'5%      {get_percent(curency, 5)}      {round(count / get_percent(curency, 5), -2)} rub\n' \
           f'profit USDT: {round((int(round(count / get_percent(curency, 5), -2))/course_RUB) - cost_usdt, 2)}\n'
