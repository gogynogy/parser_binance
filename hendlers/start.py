from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as but
from users import admins
from loader import bot
from loader import dp
from messages.start_message import get_start_text, get_info_text, get_text_admin
from SQLBD import SQL
SQL = SQL()




@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
    SQL.CheckAccount(message.chat.id, message.chat.username)
    if message.chat.id in admins:
        text = get_text_admin()
        keyboard = InlineKeyboardMarkup(row_width=1).add(but.refresh, but.activiti_check, but.order_admin, but.agents)
    else:
        text = get_start_text()
        keyboard = InlineKeyboardMarkup(row_width=1).add(but.refresh).add(but.order)
    await bot.send_message(chat_id=message.chat.id,
                           text=text,
                           parse_mode='HTML',
                           reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == "Refresh")
async def StartSclad(call: types.callback_query):
    SQL.CheckAccount(call.message.chat.id, call.message.chat.username)
    if call.message.chat.id in admins:
        keyboard = InlineKeyboardMarkup(row_width=1).add(but.refresh, but.activiti_check, but.order_admin, but.agents, but.info_luser)
    else:
        keyboard = InlineKeyboardMarkup(row_width=1).add(but.refresh).add(but.order)
    await bot.edit_message_text(text=get_start_text(),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                parse_mode='HTML',
                                reply_markup=keyboard)


@dp.message_handler(commands="info")  # /start command processing
async def info(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1).add(but.menu)
    await bot.send_message(chat_id=message.chat.id,
                           text=get_info_text,
                           parse_mode='HTML',
                           reply_markup=keyboard)


@dp.message_handler(commands="info_luser")  # /start command processing
async def info(message: types.Message):
    await bot.send_message(chat_id=354921168,
                           text='Привет, напиши пожалуйста по своей заявке: \n@Real_Egor\n@Bombambaley')