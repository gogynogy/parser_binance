from datetime import datetime
from statistics import mean

import pytz
from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as buttons
from loader import bot
from loader import dp
from p2p_parser import CrossratesGetter, get_percent

timenow = datetime.now(pytz.timezone('Asia/Colombo')).strftime("%d.%m.%Y %H:%M")
id_egor = 215007307

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


def get_text():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = mean(LKR_USDT.give_list())
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    text = f'Актуальный курс на {timenow}\n' \
           f'Сумма LKR      Курс     Сумма RUB\n' \
           f'50 000              {get_percent(curency, 8)}      {int(round(50000 / get_percent(curency, 8), -2))}\n' \
           f'100 000            {get_percent(curency, 7)}      {int(round(100000 / get_percent(curency, 7), -2))}\n' \
           f'200 000            {get_percent(curency, 6)}      {int(round(200000 / get_percent(curency, 6), -2))}\n' \
           f'400 000            {get_percent(curency, 5)}      {int(round(400000 / get_percent(curency, 5), -2))}\n' \
           f'USDT к LKR                   {round(course_LKR)}\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}'
    return text


def get_text_egor():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = mean(LKR_USDT.give_list())
    course_RUB = give_rus_course(mean(RUB_USDT.give_list()))
    curency = course_LKR / course_RUB
    text2 = f'Расчет курсов обмена рублей на юге Шри Ланки. \nДата актуализации {timenow}\n' \
            f'Контакт для заказа рупий @Real_Egor\n\n' \
            f'Мирисса/Велигама/Ахангама/Матара/Когала\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'---------------------------------------------------\n' \
            f'50 000        |       {get_percent(curency, 8)}   |   {int(round(50000 / get_percent(curency, 8), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'100 000      |       {get_percent(curency, 7)}   |   {int(round(100000 / get_percent(curency, 7), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'200 000      |       {get_percent(curency, 6)}   |   {int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'400 000      |       {get_percent(curency, 5)}   |   {int(round(400000 / get_percent(curency, 5), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'В Мириссе, если сами доедите до точки\nвыдачи, курс будет минимальный {get_percent(curency, 6)}\n' \
            f'на любую сумму, дальше по сеткe\nВ Велигаме, если доберетесь до точки\nвыдачи и сделаете предоплату, ' \
            f'курс будет минимальный {get_percent(curency, 6)} на любую сумму.\n\n' \
            f'Коломбо (минимальная сумма 60 000 руб, по предварительной договоренности)\n' \
            f'Сумма LKR      Курс     Сумма RUB\n' \
            f'---------------------------------------------------\n' \
            f'300 000       |       {get_percent(curency, 8)}   |   {int(round(300000 / get_percent(curency, 8), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'600 000      |       {get_percent(curency, 7)}   |   {int(round(600000 / get_percent(curency, 7), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'800 000      |       {get_percent(curency, 6)}   |   {int(round(800000 / get_percent(curency, 6), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'1 000 000   |       {get_percent(curency, 5)}   |   {int(round(1000000 / get_percent(curency, 5), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'В Канди и Элле доступен обмен по фиксированному курсу {get_percent(curency, 6)}, сумма от 15 000 рублей\n' \
            f'---------------------------------------------------\n' \
            f'80 000        |       {get_percent(curency, 6)}   |   {int(round(80000 / get_percent(curency, 6), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'100 000      |       {get_percent(curency, 6)}   |   {int(round(100000 / get_percent(curency, 6), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'150 000      |       {get_percent(curency, 6)}   |   {int(round(150000 / get_percent(curency, 6), -2))}\n' \
            f'---------------------------------------------------\n' \
            f'200 000      |       {get_percent(curency, 6)}   |   {int(round(200000 / get_percent(curency, 6), -2))}\n' \
            f'---------------------------------------------------\n'
    return text2
@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
    if message.chat.id == id_egor:
        try:
            await bot.edit_message_text(text=get_text(),
                                        chat_id=message.chat.id,
                                        message_id=message.message_id,
                                        reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
        except:
            await bot.send_message(chat_id=message.chat.id,
                                   text=get_text(),
                                   reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
    else:
        try:
            await bot.edit_message_text(text=get_text(),
                                        chat_id=message.chat.id,
                                        message_id=message.message_id,
                                        reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
        except:
            await bot.send_message(chat_id=message.chat.id,
                                   text=get_text(),
                                   reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))


@dp.callback_query_handler(lambda c: c.data == "Refresh")
async def StartSclad(call: types.callback_query):
    if call.message.chat.id == id_egor:
        await bot.edit_message_text(text=get_text(),
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
    else:
        await bot.edit_message_text(text=get_text(),
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
