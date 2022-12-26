from statistics import mean

from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as buttons
from loader import bot
from loader import dp
from p2p_parser import CrossratesGetter, get_percent


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
    text = f'Сумма LKR      Курс     Сумма RUB\n' \
           f'50 000              {get_percent(curency, 8)}      {int(round(50000 / get_percent(curency, 8), -2))}\n' \
           f'100 000            {get_percent(curency, 7)}      {int(round(100000 / get_percent(curency, 7), -2))}\n' \
           f'200 000            {get_percent(curency, 6)}      {int(round(200000 / get_percent(curency, 6), -2))}\n' \
           f'400 000            {get_percent(curency, 5)}      {int(round(400000 / get_percent(curency, 5), -2))}\n' \
           f'USDT к LKR                   {round(course_LKR, 2)}\n' \
           f'RUB к USDT                   {round(course_RUB, 2)}'
    return text
@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
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
    # try:
    await bot.edit_message_text(text=get_text(),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
    # except:
    #     await bot.send_message(chat_id=call.message.chat.id,
    #                            text=get_text(),
    #                            reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))