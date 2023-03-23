from statistics import mean

from countstr import countSTR
from p2p_parser import CrossratesGetter, give_rus_course, get_percent
from datetime import datetime
import pytz


def give_time():
    timenow = datetime.now(pytz.timezone('Asia/Colombo')).strftime("%d.%m.%Y %H:%M")
    return timenow


def courseUSDT(minu):
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    course_LKR = int(mean(LKR_USDT.give_list()))
    return course_LKR - minu


def get_text_admin():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = int(mean(LKR_USDT.give_list()))
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    probel = '         |       '
    text = f'Актуальный курс RUB/LKR на <b>{give_time()}</b>\n\n' \
           f'Сумма LKR         Курс            Сумма RUB\n' \
           f'------------------------------------------------\n' \
           f'50 000 {probel} {get_percent(curency, 8)}{probel}{int(round(50000 / get_percent(curency, 8), -2))}\n' \
           f'------------------------------------------------\n' \
           f'100 000{probel}{get_percent(curency, 7)}{probel}{int(round(100000 / get_percent(curency, 7), -2))}\n' \
           f'------------------------------------------------\n' \
           f'200 000{probel}{get_percent(curency, 6)}{probel}{int(round(200000 / get_percent(curency, 6), -2))}\n' \
           f'------------------------------------------------\n' \
           f'400 000{probel}{get_percent(curency, 5)}{probel}{int(round(400000 / get_percent(curency, 5), -2))}\n' \
           f'------------------------------------------------\n\n' \
           f'Актуальный курс USDT/LKR на <b>{give_time()}</b>\n\n' \
           f'Сумма LKR         Курс            Сумма USDT\n' \
           f'------------------------------------------------\n' \
           f'50 000 {probel} {courseUSDT(14)}{probel}{int(50000 / courseUSDT(14))}\n' \
           f'------------------------------------------------\n' \
           f'100 000{probel}{courseUSDT(13)}{probel}{int(100000 / courseUSDT(13))}\n' \
           f'------------------------------------------------\n' \
           f'200 000{probel}{courseUSDT(12)}{probel}{int(200000 / courseUSDT(12))}\n' \
           f'------------------------------------------------\n' \
           f'400 000{probel}{courseUSDT(10)}{probel}{int(400000 / courseUSDT(10))}\n' \
           f'------------------------------------------------\n\n' \
           f'USDT к LKR                    {round(course_LKR)}\n' \
           f'USDT к LKR - 1%           {round(get_percent(course_LKR, 1))}\n' \
           f'USDT к LKR - 3%           {round(get_percent(course_LKR, 3), 1)}\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}\n' \
           f'RUB к LKR                      {round(curency, 2)}\n' \
           f'RUB к LKR - 1%              {round(get_percent(course_LKR, 1)/course_RUB, 2)}\n' \
           f'RUB к LKR - 3%              {round(get_percent(course_LKR, 3)/course_RUB, 3)}'
    return text

def get_text_admin_viet():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    VND_USDT = CrossratesGetter('VND', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_VND = int(mean(VND_USDT.give_list()))
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_VND / course_RUB
    probel = '         |       '
    text = f'Актуальный курс RUB/VND на <b>{give_time()}</b>\n\n' \
           f'Сумма VND         Курс            Сумма RUB\n' \
           f'------------------------------------------------\n' \
           f'1 000 000 {probel} {get_percent(curency, 8)}{probel}{int(round(1000000 / get_percent(curency, 8), -2))}\n' \
           f'------------------------------------------------\n' \
           f'4 000 000{probel}{get_percent(curency, 7)}{probel}{int(round(4000000 / get_percent(curency, 7), -2))}\n' \
           f'------------------------------------------------\n' \
           f'8 000 000{probel}{get_percent(curency, 6)}{probel}{int(round(8000000 / get_percent(curency, 6), -2))}\n' \
           f'------------------------------------------------\n' \
           f'10 000 000{probel}{get_percent(curency, 5)}{probel}{int(round(10000000 / get_percent(curency, 5), -2))}\n' \
           f'------------------------------------------------\n\n' \
           f'Актуальный курс USDT/VND на <b>{give_time()}</b>\n\n' \
           f'Сумма VND         Курс            Сумма USDT\n' \
           f'------------------------------------------------\n' \
           f'1 000 000 {probel} {courseUSDT(14)}{probel}{int(1000000 / courseUSDT(14))}\n' \
           f'------------------------------------------------\n' \
           f'4 000 000{probel}{courseUSDT(13)}{probel}{int(4000000 / courseUSDT(13))}\n' \
           f'------------------------------------------------\n' \
           f'8 000 000{probel}{courseUSDT(12)}{probel}{int(8000000 / courseUSDT(12))}\n' \
           f'------------------------------------------------\n' \
           f'10 000 000{probel}{courseUSDT(10)}{probel}{int(10000000 / courseUSDT(10))}\n' \
           f'------------------------------------------------\n\n' \
           f'USDT к VND                    {round(course_VND)}\n' \
           f'USDT к VND - 1%           {round(get_percent(course_VND, 1))}\n' \
           f'USDT к VND - 3%           {round(get_percent(course_VND, 3), 1)}\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}\n' \
           f'RUB к VND                      {round(curency, 2)}\n' \
           f'RUB к VND - 1%              {round(get_percent(course_VND, 1)/course_RUB, 2)}\n' \
           f'RUB к VND - 3%              {round(get_percent(course_VND, 3)/course_RUB, 3)}'
    return text


def get_start_text():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = int(mean(LKR_USDT.give_list()))
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    probel = '         |       '
    text2 = f'Расчет курсов обмена рублей на юге Шри Ланки. \nДата актуализации: <b>{give_time()}</b>\n\n' \
            f'<b>Мирисса / Велигама / Ахангама / Матара / Когала</b>\n' \
            f'Сумма LKR         Курс            Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'50 000  {probel}{get_percent(curency, 8)}{probel}{int(round(50000 / get_percent(curency, 8), -2))}\n' \
            f'------------------------------------------------\n' \
            f'100 000{probel}{get_percent(curency, 7)}{probel}{int(round(100000 / get_percent(curency, 7), -2))}\n' \
            f'------------------------------------------------\n' \
            f'200 000{probel}{get_percent(curency, 6)}{probel}{int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'400 000{probel}{get_percent(curency, 5)}{probel}{int(round(400000 / get_percent(curency, 5), -2))}\n' \
            f'------------------------------------------------\n' \
            f'<b>В Мириссе</b>, если сами доедите до точки выдачи, курс будет минимальный {get_percent(curency, 6)} ' \
            f'на любую сумму, дальше по сеткe.\n<b>В Велигаме</b>, ' \
            f'если доберетесь до точки выдачи и сделаете предоплату, ' \
            f'курс будет минимальный {get_percent(curency, 6)} на любую сумму.\n\n' \
            f'<b>В Коломбо</b> (минимальная сумма 60 000 руб, по предварительной договоренности)\n' \
            f'Сумма LKR         Курс            Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'300 000  {probel}{get_percent(curency, 8)}{probel}{int(round(300000 / get_percent(curency, 8), -2))}\n' \
            f'------------------------------------------------\n' \
            f'600 000  {probel}{get_percent(curency, 7)}{probel}{int(round(600000 / get_percent(curency, 7), -2))}\n' \
            f'------------------------------------------------\n' \
            f'800 000  {probel}{get_percent(curency, 6)}{probel}{int(round(800000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'1 000 000{probel}{get_percent(curency, 5)}{probel}{int(round(1000000 / get_percent(curency, 5), -2))}\n' \
            f'------------------------------------------------\n\n' \
            f'<b>В Канди и Элле</b> доступен обмен по фиксированному курсу {get_percent(curency, 6)}, ' \
            f'сумма от 15 000 рублей\n' \
            f'Сумма LKR         Курс            Сумма RUB\n' \
            f'------------------------------------------------\n' \
            f'80 000  {probel}{get_percent(curency, 6)}{probel}{int(round(80000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'100 000{probel}{get_percent(curency, 6)}{probel}{int(round(100000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'150 000{probel}{get_percent(curency, 6)}{probel}{int(round(150000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n' \
            f'200 000{probel}{get_percent(curency, 6)}{probel}{int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'------------------------------------------------\n\n'
    return text2


get_info_text = f"Привет, данный бот написан на чистом энтузиазме и уже насчитиывает в себе {countSTR()} " \
                f"строчки кода.\nЕсли хочешь сказать спасибо, вот мой Binance id - 464113912\n" \
                f"Хочешь бота в телеграмме, пиши мне в личку - @bombambaley"
