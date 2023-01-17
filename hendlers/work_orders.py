from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as but
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.order_messages import start_order_message, order_message
from users import admins

SQL = SQL()


@dp.callback_query_handler(but.take_order.filter())
async def continue_order(call: types.callback_query, callback_data: dict):
    location = callback_data.get('number')
    keyboard = but.order_count_money(location)
    await bot.edit_message_text(text=order_message(location),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=keyboard)