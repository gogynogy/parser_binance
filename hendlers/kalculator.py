from aiogram import types
from aiogram.dispatcher import FSMContext

import buttons as but
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.calkulator_messages import start_calkulator, second_kalculators, third_kalculators
from state_mash import buttons_curensy, kalculator, second_currency

SQL = SQL()

# @dp.callback_query_handler(lambda c: c.data == "calkulator", state=None)
# async def start_kalc(call: types.callback_query):
#     await kalculator.first.set()
#     await bot.send_message(text=start_calkulator,
#                            chat_id=call.message.chat.id,
#                            reply_markup=buttons_curensy())
#
# @dp.message_handler(state=kalculator.first)
# async def second_kalculator(message: types.Message, state: FSMContext):
#     await state.update_data(first=message.text)
#     await kalculator.second.set()
#     await bot.send_message(text=second_kalculators,
#                                 chat_id=message.chat.id,
#                                 reply_markup=second_currency(message.text))
#
# @dp.message_handler(state=kalculator.second)
# async def third_kalculator(message: types.Message, state: FSMContext):
#     await state.update_data(second=message.text)
#     await kalculator.count.set()
#     data = await state.get_data()
#     await bot.send_message(text=third_kalculators(data['first'], data['second']),
#                                 chat_id=message.chat.id,
#                                 reply_markup=second_currency(message.text))
#
# @dp.message_handler(state=kalculator.count)
# async def third_kalculator(message: types.Message, state: FSMContext):
#     await state.update_data(second=message.text)
#     await state.finish()
#     data = await state.get_data()
#     await bot.send_message(text=third_kalculators(data['first'], data['second']),
#                                 chat_id=message.chat.id,
#                                 reply_markup=second_currency(message.text))
# async def second_kalculator(call: types.callback_query, callback_data: dict):
#     first_val = callback_data.get('what')
#     await bot.edit_message_text(text=start_calkulator,
#                                 chat_id=call.message.chat.id,
#                                 message_id=call.message.message_id,
#                                 parse_mode='HTML',
#                                 reply_markup=but.make_button_kalc())
