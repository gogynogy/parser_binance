from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons
from loader import bot
from loader import dp
from SQLBD import SQL
SQL = SQL()


@dp.callback_query_handler(lambda c: c.data == "check_activiti")
async def StartSclad(call: types.callback_query):
    keyboard = InlineKeyboardMarkup(row_width=1).add(buttons.refresh).add(buttons.activiti_check)
    await bot.edit_message_text(text=SQL.watch_activity(),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                parse_mode='HTML',
                                reply_markup=keyboard)