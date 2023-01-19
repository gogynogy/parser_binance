from statistics import mean

from countstr import countSTR
from p2p_parser import CrossratesGetter, give_rus_course, get_percent, calculate_profit
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
    probel ='         |       '
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
           f'Актуальный курс RUB/LKR на <b>{give_time()}</b>\n\n' \
            f'Сумма LKR         Курс            Сумма USDT\n' \
            f'------------------------------------------------\n' \
            f'50 000 {probel} {courseUSDT(22)}{probel}{int(50000 / courseUSDT(22))}\n' \
            f'------------------------------------------------\n' \
            f'100 000{probel}{courseUSDT(20)}{probel}{int(100000 / courseUSDT(20))}\n' \
            f'------------------------------------------------\n' \
            f'200 000{probel}{courseUSDT(17)}{probel}{int(200000 / courseUSDT(17))}\n' \
            f'------------------------------------------------\n' \
            f'400 000{probel}{courseUSDT(15)}{probel}{int(400000 / courseUSDT(15))}\n' \
            f'------------------------------------------------\n\n' \
           f'USDT к LKR                    {round(course_LKR)}\n' \
           f'USDT к LKR - 1%           {round(get_percent(course_LKR, 1))}\n' \
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
    probel ='         |       '
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
            f'на любую сумму, дальше по сеткe.\n<b>В Велигаме</b>, если доберетесь до точки выдачи и сделаете предоплату, ' \
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