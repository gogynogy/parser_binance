from statistics import mean

from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as buttons
from loader import bot
from loader import dp
from p2p_parser import CrossratesGetter, get_percent

def get_text():
    bank_RUS = ['TinkoffNew']
    bank_SRI = ['BANK']
    LKR_USDT = CrossratesGetter('LKR', 'USDT', "sell", bank_SRI)
    RUB_USDT = CrossratesGetter('RUB', 'USDT', 'buy', bank_RUS)
    course_LKR = mean(LKR_USDT.give_list()) - mean(LKR_USDT.give_list()) * 0.01
    course_RUB = mean(RUB_USDT.give_list())
    curency = course_LKR / course_RUB
    text = f'Сумма LKR      Курс     Сумма RUB\n' \
           f'50 000              {get_percent(curency, 8)}      {round(50000 / get_percent(curency, 8))}\n' \
           f'100 000            {get_percent(curency, 7)}      {round(100000 / get_percent(curency, 7))}\n' \
           f'200 000           {get_percent(curency, 6)}      {round(200000 / get_percent(curency, 6))}\n' \
           f'400 000           {get_percent(curency, 5)}      {round(400000 / get_percent(curency, 5))}\n' \
           f'USDT к LKR                      {round(course_LKR, 2)}\n' \
           f'RUB к USDT                      {round(course_RUB, 2)}'
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