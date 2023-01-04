from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons
from users import admins
from loader import bot
from loader import dp
from messages.start_message import get_start_text, get_info_text
from SQLBD import SQL
SQL = SQL()




@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
    SQL.CheckAccount(message.chat.id, message.chat.username)
    if message.chat.id in admins:
        keyboard = InlineKeyboardMarkup(row_width=1).add(buttons.refresh).add(buttons.activiti_check)
    else:
        keyboard = InlineKeyboardMarkup(row_width=1).add(buttons.refresh).add(buttons.order)
    await bot.send_message(chat_id=message.chat.id,
                           text=get_start_text(),
                           parse_mode='HTML',
                           reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == "Refresh")
async def StartSclad(call: types.callback_query):
    SQL.CheckAccount(call.message.chat.id, call.message.chat.username)
    if call.message.chat.id in admins:
        keyboard = InlineKeyboardMarkup(row_width=1).add(buttons.refresh).add(buttons.activiti_check)
    else:
        keyboard = InlineKeyboardMarkup(row_width=1).add(buttons.refresh).add(buttons.order)
    await bot.edit_message_text(text=get_start_text(),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                parse_mode='HTML',
                                reply_markup=keyboard)


@dp.message_handler(commands="info")  # /start command processing
async def begin(message: types.Message):
    SQL.CheckAccount(message.chat.id, message.chat.username)
    keyboard = InlineKeyboardMarkup(row_width=1).add(buttons.menu)
    await bot.send_message(chat_id=message.chat.id,
                           text=get_info_text,
                           parse_mode='HTML',
                           reply_markup=keyboard)