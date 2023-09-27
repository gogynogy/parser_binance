from statistics import mean

from countstr import countSTR
from p2p_parser import CrossratesGetter, give_rus_course, get_percent
from datetime import datetime
import pytz

from bybit_parser import get_rub_rate_bybit


def give_time():
    timenow = datetime.now(pytz.timezone('Asia/Colombo')).strftime("%d.%m.%Y %H:%M")
    return timenow


def course_LKR_USDT(minu):
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    course_LKR = int(mean(LKR_USDT.give_list()))

def course_VND_USDT(minu):
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('VND', 'USDT', "sell", bank_SRI)
    course_LKR = int(mean(LKR_USDT.give_list()))
    return course_LKR - minu

def get_text_admin():
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    course_RUB = get_rub_rate_bybit()
    course_LKR = int(mean(LKR_USDT.give_list()))
    curency = course_LKR / course_RUB
    probel = '         |       '
    text = f'Актуальный курс RUB/LKR на <b>{give_time()}</b>\n\n' \
           f'Сумма LKR         Курс            Сумма RUB\n\n' \
           f'50 000 {probel} {get_percent(curency, 6)}{probel}{int(round(50000 / get_percent(curency, 6), -2))}\n\n' \
           f'200 000{probel}{get_percent(curency, 5)}{probel}{int(round(200000 / get_percent(curency, 5), -2))}\n\n' \
           f'USDT к LKR                    {round(course_LKR)}\n' \
           f'USDT к LKR - 1%           {round(get_percent(course_LKR, 1), 1)}\n' \
           f'USDT к LKR - 2%           {round(get_percent(course_LKR, 2), 1)}\n' \
           f'USDT к LKR - 3%           {round(get_percent(course_LKR, 3), 1)}\n' \
           f'USDT к LKR - 4%           {round(get_percent(course_LKR, 4), 1)}\n' \
           f'USDT к LKR - 5%           {round(get_percent(course_LKR, 5), 1)}\n' \
           f'USDT к LKR - 6%           {round(get_percent(course_LKR, 6), 1)}\n' \
            f'USDT к LKR - 7%           {round(get_percent(course_LKR, 7), 1)}\n' \
           f'USDT к LKR - 8%           {round(get_percent(course_LKR, 8), 1)}\n\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}\n\n' \
           f'RUB к LKR                      {round(curency, 2)}\n' \
           f'RUB к LKR - 1%              {round(get_percent(course_LKR, 1)/course_RUB, 2)}\n' \
           f'RUB к LKR - 2%              {round(get_percent(course_LKR, 2)/course_RUB, 2)}\n' \
           f'RUB к LKR - 3%              {round(get_percent(course_LKR, 3)/course_RUB, 2)}\n' \
           f'RUB к LKR - 4%              {round(get_percent(course_LKR, 4)/course_RUB, 2)}\n' \
           f'RUB к LKR - 5%              {round(get_percent(course_LKR, 5)/course_RUB, 2)}\n' \
           f'RUB к LKR - 6%              {round(get_percent(course_LKR, 6)/course_RUB, 2)}\n' \
            f'RUB к LKR - 7%              {round(get_percent(course_LKR, 7)/course_RUB, 2)}\n' \
             f'RUB к LKR - 8%              {round(get_percent(course_LKR, 8)/course_RUB, 2)}'

    return text



def get_text_admin_viet():
    bank_SRI = ['BANK']
    VND_USDT = CrossratesGetter('VND', 'USDT', "sell", bank_SRI)
    RUB_USDT = get_rub_rate_bybit()
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
           f'USDT к VND                    {round(course_VND)}\n' \
           f'USDT к VND - 1%           {round(get_percent(course_VND, 1))}\n' \
           f'USDT к VND - 3%           {round(get_percent(course_VND, 3), 1)}\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}\n' \
           f'RUB к VND                      {round(curency, 2)}\n' \
           f'RUB к VND - 1%              {round(get_percent(course_VND, 1)/course_RUB, 2)}\n' \
           f'RUB к VND - 3%              {round(get_percent(course_VND, 3)/course_RUB, 3)}'
    return text


def get_start_text():
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    course_RUB = get_rub_rate_bybit()
    course_LKR = int(mean(LKR_USDT.give_list()))
    curency = course_LKR / course_RUB
    probel = '         |       '
    text = f'Расчет курсов обмена рублей на Шри Ланке. \nДата актуализации: <b>{give_time()}</b>\n\n' \
        f'<b>В Канди и Аругамбей</b> доступен самовывоз в центре по фикс курсу {get_percent(curency, 6)}\n\n' \
        f'Сумма LKR         Курс            Сумма RUB\n\n' \
        f'80 000 {probel}{get_percent(curency, 6)}{probel}{int(round(80000 / get_percent(curency, 6), -2))}\n\n' \
        f'<b>Мирисса / Велигама / Ахангама / Матара / Когала / Унаватуна / Галле</b>\n\n' \
        f'100 000 {probel}{get_percent(curency, 6)}{probel}{int(round(100000 / get_percent(curency, 6), -2))}\n\n' \
        f'400 000{probel}{get_percent(curency, 5)}{probel}{int(round(400000 / get_percent(curency, 5), -2))}\n\n' \
        f'<b>В Коломбо</b> (Доставка в центр города от 200 000 рупий)\n\n' \
        f'100 000{probel}{get_percent(curency, 7)}{probel}{int(round(100000 / get_percent(curency, 7), -2))}\n\n' \
        f'200 000{probel}{get_percent(curency, 6)}{probel}{int(round(200000 / get_percent(curency, 6), -2))}\n\n' \
        f'<b>Аэропорт Негомбо</b> (Доставка от 300 000 рупий)\n\n' \
        f'300 000{probel}{get_percent(curency, 7)}{probel}{int(round(300000 / get_percent(curency, 7), -2))}\n\n' \
        f'500 000{probel}{get_percent(curency, 6)}{probel}{int(round(500000 / get_percent(curency, 6), -2))}'
    return text


get_info_text = f"Привет, данный бот написан на чистом энтузиазме и уже насчитиывает в себе {countSTR()} " \
                f"строчки кода.\nЕсли хочешь сказать спасибо, вот мой Binance id - 464113912\n" \
                f"Хочешь бота в телеграмме, пиши мне в личку - @bombambaley"
