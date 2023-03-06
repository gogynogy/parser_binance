from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup

import buttons as but
from config.huins import huins
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.calkulator_messages import start_calkulator, second_kalculators, third_kalculators, get_curensy_info
from state_mash import buttons_curensy, kalculator, second_currency
from users import agents

SQL = SQL()

@dp.message_handler(lambda message: message.text.isdigit())
async def only_numbers(message: types.Message):
    if message.chat.id in agents:
        num = int(message.text)
        if message.text in huins:
            await message.answer(text=huins[message.text],
                                 reply_markup=InlineKeyboardMarkup(row_width=1).add(but.menu))
            return
        text = get_curensy_info(num)
        await message.answer(text=text,
                             reply_markup=InlineKeyboardMarkup(row_width=1).add(but.menu))
