from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from loader import bot
from loader import dp
from SQLBD import SQL

SQL = SQL()
class AddAgent(StatesGroup):
    telegramID = State()
    username = State()
    persent = State()
@dp.callback_query_handler(lambda c: c.data == "new_agent")
async def give_agents_link(call: types.callback_query):
    await bot.edit_message_text(text='Введи telegramID',
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await AddAgent.telegramID.set()

@dp.message_handler(state=AddAgent.telegramID)
async def process_comment_order(message: types.Message, state: FSMContext):
    await state.update_data(telegramID=message.text)
    await bot.send_message(text='Введи telegram username',
                           chat_id=message.chat.id)
    await AddAgent.username.set()

@dp.message_handler(state=AddAgent.username)
async def process_comment_order(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await bot.send_message(text='под какой сумарный процент работает агент?',
                           chat_id=message.chat.id)
    await AddAgent.persent.set()

@dp.message_handler(state=AddAgent.persent)
async def process_comment_order(message: types.Message, state: FSMContext):
    await state.update_data(persent=message.text)
    await bot.send_message(text='Агент добавлен',
                           chat_id=message.chat.id)
    data = await state.get_data()
    print(data)
    SQL.AddAgent(data['telegramID'], data['username'], data['persent'])
    await state.finish()