from statistics import mean

from messages.start_message import give_time
from p2p_parser import CrossratesGetter, give_rus_course, get_percent

start_order_message = 'Выбери локацию из списка:'

def order_message(location):
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = mean(LKR_USDT.give_list())
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    tourist_place = ['Галле', 'Унаватуна', 'Велигама', 'Мирисса', 'Матара']
    if location in tourist_place:
        text = f'<b>Мирисса/Велигама/Ахангама/Матара/Когала</b>\n' \
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
            f'курс будет минимальный {get_percent(curency, 6)} на любую сумму.\n\n'
    elif location == 'Коломбо':
        text = f'<b>В Коломбо</b> (минимальная сумма 60 000 руб, по предварительной договоренности)\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'300 000       |       {get_percent(curency, 8)}   |   {int(round(300000 / get_percent(curency, 8), -2))}\n' \
            f'------------------------------------------------\n' \
            f'600 000      |       {get_percent(curency, 7)}   |   {int(round(600000 / get_percent(curency, 7), -2))}\n' \
            f'------------------------------------------------\n' \
            f'800 000      |       {get_percent(curency, 6)}   |   {int(round(800000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'1 000 000   |       {get_percent(curency, 5)}   |   {int(round(1000000 / get_percent(curency, 5), -2))}\n' \
            f'------------------------------------------------\n\n'
    elif location == 'Канди' or location == 'Элла':
        text = f'<b>В Канди и Элле</b> доступен обмен по фиксированному курсу {get_percent(curency, 6)}, сумма от 15 000 рублей\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'80 000        |       {get_percent(curency, 6)}   |   {int(round(80000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'100 000      |       {get_percent(curency, 6)}   |   {int(round(100000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'150 000      |       {get_percent(curency, 6)}   |   {int(round(150000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'200 000      |       {get_percent(curency, 6)}   |   {int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n'
    return text