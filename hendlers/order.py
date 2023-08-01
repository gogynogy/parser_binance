from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as but
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.order_messages import start_order_message, order_message
from users import admins

SQL = SQL()


@dp.callback_query_handler(lambda c: c.data == "new_order")
async def start_order(call: types.callback_query):
    keyboard = but.make_button_locations().add(but.menu)
    await bot.edit_message_text(text=start_order_message,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=keyboard)


@dp.callback_query_handler(but.start_order.filter())
async def continue_order(call: types.callback_query, callback_data: dict):
    location = callback_data.get('what')
    keyboard = but.order_count_money(location)
    await bot.edit_message_text(text=order_message(location),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=keyboard)


@dp.callback_query_handler(but.continue_order.filter())
async def finish_order(call: types.callback_query, callback_data: dict):
    location = callback_data.get('where')
    how_much = callback_data.get('how_much')
    count_num = SQL.make_order(call.message.chat.id, call.message.chat.username, location, how_much)
    if not call.message.chat.username:
        await bot.edit_message_text(text=f'Твой ник в телеграмме скрыт и написать тебе нельзя('
                                         f'По обмену пиши: @Real_Egor, @Bombambaley',
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=InlineKeyboardMarkup(row_width=1).add(but.menu))
    else:
        await bot.edit_message_text(text=f'Заказ на сумму {how_much} в городе {location} отправлен модератору, ожидайте.',
                                chat_id = call.message.chat.id,
                                message_id = call.message.message_id,
                                reply_markup = InlineKeyboardMarkup(row_width=1).add(but.menu))
    for admin in admins:
        await bot.send_message(chat_id=admin,
                               text=f'@{call.message.chat.username} заказал {how_much} в городе {location}',
                               reply_markup = InlineKeyboardMarkup(row_width=1).add(
                                   but.take_order_work(count_num), but.write_customer(call.message)))