from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.order_messages import start_order_message, order_message
from users import admins

SQL = SQL()


@dp.callback_query_handler(lambda c: c.data == "new_order")
async def start_order(call: types.callback_query):
    keyboard = buttons.make_button_locations().add(buttons.menu)
    await bot.edit_message_text(text=start_order_message,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=keyboard)


@dp.callback_query_handler(buttons.start_order.filter())
async def continue_order(call: types.callback_query, callback_data: dict):
    location = callback_data.get('what')
    keyboard = buttons.order_count_money(location)
    await bot.edit_message_text(text=order_message(location),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=keyboard)


@dp.callback_query_handler(buttons.continue_order.filter())
async def finish_order(call: types.callback_query, callback_data: dict):
    location = callback_data.get('where')
    how_much = callback_data.get('how_much')
    SQL.make_order(call.message.chat.id, call.message.chat.username, location, how_much)
    await bot.edit_message_text(text=f'Заказ на сумму {how_much} в городе {location} отправлен модератору, ожидайте.\n'
                                     f'Если тебе кажется, что про тебя забыли, пиши @Real_Egor',
                                chat_id = call.message.chat.id,
                                message_id = call.message.message_id,
                                reply_markup = InlineKeyboardMarkup(row_width=1).add(buttons.menu))
    for admin in admins:
        await bot.send_message(chat_id=admin,
                               text=f'@{call.message.chat.username} заказал {how_much} в городе {location}')


