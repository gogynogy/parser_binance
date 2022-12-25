from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import buttons as buttons
from loader import bot
from loader import dp
from p2p_parser import text as p2p_parser



@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
    try:
        await bot.edit_message_text(text=p2p_parser,
                                    chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))
    except:
        await bot.send_message(chat_id=message.chat.id,
                               text=p2p_parser,
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))


@dp.callback_query_handler(lambda c: c.data == "Refresh")
async def StartSclad(call: types.callback_query):
    await bot.edit_message_text(text=p2p_parser,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=InlineKeyboardMarkup(row_width=1).add(buttons.menu))