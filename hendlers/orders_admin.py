from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as but
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.orders_admin import start_order_admin
from users import admins
SQL = SQL()



@dp.callback_query_handler(lambda c: c.data == "orders_admin")
async def start_order(call: types.callback_query):
    await bot.edit_message_text(text=start_order_admin,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup = InlineKeyboardMarkup(row_width=1).
                                add(but.new_agent, but.open_orders, but.all_orders))


@dp.callback_query_handler(lambda c: c.data == "open_orders")
async def start_order(call: types.callback_query):
    await bot.edit_message_text(text=SQL.watch_open_orders(),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup = InlineKeyboardMarkup(row_width=1).
                                add(but.new_agent, but.open_orders, but.all_orders))
