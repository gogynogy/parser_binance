from statistics import mean

from countstr import countSTR
from p2p_parser import CrossratesGetter, give_rus_course, get_percent, calculate_profit
from datetime import datetime
import pytz


def give_time():
    timenow = datetime.now(pytz.timezone('Asia/Colombo')).strftime("%d.%m.%Y %H:%M")
    return timenow

def get_text_admin():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = int(mean(LKR_USDT.give_list()))
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    curency_1 = (course_LKR - course_LKR * 0.01) / course_RUB
    text = f'Актуальный курс на {give_time()}\n' \
           f'Сумма LKR      Курс     Сумма RUB\n\n' \
           f'50 000              {get_percent(curency, 8)}      {int(round(50000 / get_percent(curency, 8), -2))}\n' \
           f'Профит с 50 000 LKR {round(calculate_profit(50000, 8))} LKR\n\n' \
           f'100 000            {get_percent(curency, 7)}      {int(round(100000 / get_percent(curency, 7), -2))}\n' \
           f'Профит с 100 000 LKR {round(calculate_profit(100000, 7))} LKR\n\n' \
           f'200 000            {get_percent(curency, 6)}      {int(round(200000 / get_percent(curency, 6), -2))}\n' \
           f'Профит с 200 000 LKR {round(calculate_profit(200000, 6))} LKR\n\n' \
           f'400 000            {get_percent(curency, 5)}      {int(round(400000 / get_percent(curency, 5), -2))}\n' \
           f'Профит с 400 000 LKR {round(calculate_profit(400000, 5))} LKR\n\n' \
           f'USDT к LKR                   {round(course_LKR)}\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}'
    return text


def get_start_text():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = int(mean(LKR_USDT.give_list()))
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    text2 = f'Расчет курсов обмена рублей на юге Шри Ланки. \nДата актуализации: <b>{give_time()}</b>\n\n' \
            f'<b>Мирисса/Велигама/Ахангама/Матара/Когала</b>\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'50 000        |       {get_percent(curency, 8)}   |   {int(round(50000 / get_percent(curency, 8), -2))}\n' \
            f'------------------------------------------------\n' \
            f'100 000      |       {get_percent(curency, 7)}   |   {int(round(100000 / get_percent(curency, 7), -2))}\n' \
            f'------------------------------------------------\n' \
            f'200 000      |       {get_percent(curency, 6)}   |   {int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'400 000      |       {get_percent(curency, 5)}   |   {int(round(400000 / get_percent(curency, 5), -2))}\n' \
            f'------------------------------------------------\n' \
            f'<b>В Мириссе</b>, если сами доедите до точки\nвыдачи, курс будет минимальный {get_percent(curency, 6)}\n' \
            f'на любую сумму, дальше по сеткe\n<b>В Велигаме</b>, если доберетесь до точки\nвыдачи и сделаете предоплату, ' \
            f'курс будет минимальный {get_percent(curency, 6)} на любую сумму.\n\n' \
            f'<b>В Коломбо</b> (минимальная сумма 60 000 руб, по предварительной договоренности)\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'300 000       |       {get_percent(curency, 8)}   |   {int(round(300000 / get_percent(curency, 8), -2))}\n' \
            f'------------------------------------------------\n' \
            f'600 000      |       {get_percent(curency, 7)}   |   {int(round(600000 / get_percent(curency, 7), -2))}\n' \
            f'------------------------------------------------\n' \
            f'800 000      |       {get_percent(curency, 6)}   |   {int(round(800000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'1 000 000   |       {get_percent(curency, 5)}   |   {int(round(1000000 / get_percent(curency, 5), -2))}\n' \
            f'------------------------------------------------\n\n' \
            f'<b>В Канди и Элле</b> доступен обмен по фиксированному курсу {get_percent(curency, 6)}, сумма от 15 000 рублей\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'80 000        |       {get_percent(curency, 6)}   |   {int(round(80000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'100 000      |       {get_percent(curency, 6)}   |   {int(round(100000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'150 000      |       {get_percent(curency, 6)}   |   {int(round(150000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'200 000      |       {get_percent(curency, 6)}   |   {int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n\n'
    return text2


get_info_text = f"Привет, данный бот написан на чистом энтузиазме и уже насчитиывает в себе {countSTR()} " \
                f"строчки кода.\nЕсли хочешь сказать спасибо, вот мой Binance id - 464113912\n" \
                f"Хочешь бота в телеграмме, пиши мне в личку - @bombambaley"