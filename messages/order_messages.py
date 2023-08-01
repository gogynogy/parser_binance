from statistics import mean

from messages.start_message import give_time
from p2p_parser import CrossratesGetter, give_rus_course, get_percent

from SQLBD import SQL
SQL = SQL()
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

def exchange_point(agentID):
    agent_percent = SQL.CheckAgent(agentID)[4]
    usdt = give_currency_to_LKR('usdt', agent_percent)
    usdt100k = 100000 / usdt
    rub = give_currency_to_LKR('rub', agent_percent)
    rub100k = format_number_with_spaces(100000 / rub)
    text = f'Привет. Вы попали в одну из точек,\nгде вам могут помочь с обменом валюты.\n' \
           f'Тут меняют криптовалюту по курсу:\n1 USDT = <b>{usdt}</b> LKR.\nПример: {round(usdt100k, 2)} USDT ' \
           f'@ {usdt} = 100 000 LKR\n' \
           f'Так же тут можно поменять рубли на рупии по курсу:\n1 Rub = <b>{rub}</b> LKR\n' \
           f'Пример: {rub100k} RUB @ {rub} = 100 000 LKR.\n' \
           f'Так же у нас работает русскоязычная поддержка, обращайтесь.'
    return text

def second_order_message(currency, agentID):
    agent_percent = SQL.CheckAgent(agentID)[4]
    usdt = give_currency_to_LKR('usdt', agent_percent)
    rub = give_currency_to_LKR('rub', agent_percent)
    if currency == 'usdt':
        text = f'Чтобы поменять usdt, Вам нужно определиться с суммой обмена.\nПосле этого, возможно, ' \
               f'потребуется подождать, пока для вас подготовят наличные рупии\n' \
               f'(мы не держим тут сейфов с кучей кеша).\n' \
               f'Реквизиты для перевода вам предоставит русскоязычный помощник.\n' \
               f'Выберите сумму, которую хотите получить.\n<b>Актуальный курс {usdt}</b>'
    elif currency == 'rub':
        text = f'Чтобы поменять рубли, Вам нужно определиться с суммой обмена.\nПосле этого, возможно, ' \
               f'потребуется подождать, пока для вас подготовят наличные рупии\n' \
               f'(мы не держим тут сейфов с кучей кеша).\n' \
               f'Оплату вы будете осуществлять банковским переводом на счет в российском банке.\n' \
               f'Реквизиты для перевода вам предоставит русскоязычный помощник.\n' \
               f'Выберите сумму, которую хотите получить.\n<b>Актуальный курс {rub}</b>'
    return text


def format_number_with_spaces(number):
    number_str = str(int(round(number / 100) * 100))
    groups = []
    while number_str:
        groups.insert(0, number_str[-3:])
        number_str = number_str[:-3]
    formatted_number = ' '.join(groups)
    return formatted_number

def give_currency_to_LKR(monet, percent):
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    course_LKR = mean(LKR_USDT.give_list())
    if monet == 'rub':
        bank_RUS = ['TinkoffNew']
        RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
        course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
        curency = course_LKR / course_RUB
        rub = get_percent(curency, percent)
        return rub
    else:
        usdt = round(get_percent(course_LKR, percent), 2)
        return usdt