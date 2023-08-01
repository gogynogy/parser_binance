from aiogram import types

import buttons
from loader import bot
from loader import dp
from SQLBD import SQL
from messages.order_messages import exchange_point, second_order_message
from users import admins

SQL = SQL()


async def exchange(message: types.Message, agentID):
    text = exchange_point(agentID)
    button = buttons.choice_currency_local(agentID).add(buttons.rus_help)
    try:
        await bot.edit_message_text(text=text,
                                    chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    parse_mode='HTML',
                                    reply_markup=button)
    except:
        await bot.send_message(text=text,
                               chat_id=message.chat.id,
                               parse_mode='HTML',
                               reply_markup=button)

@dp.callback_query_handler(lambda c: c.data == "agents")
async def give_agents_link(call: types.callback_query):
    data = SQL.GiveAgents()
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    for agent in data:
        deep_link = f"https://t.me/{bot_username}?start={agent[2]}"
        await bot.send_message(call.message.chat.id, f"Ссылка на агента {deep_link}")


@dp.callback_query_handler(buttons.back_to_main_menu.filter())
async def restart_start(call: types.callback_query, callback_data: dict):
    agentID = callback_data.get('agentID')
    await exchange(call.message, agentID)
@dp.callback_query_handler(buttons.local_order.filter())
async def give_agents_link(call: types.callback_query, callback_data: dict):
    agentID, currency = callback_data.get('agentID'), callback_data.get('currency')
    text = second_order_message(currency, agentID)
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=buttons.choice_count_money_local(agentID, currency).add(
                                    buttons.enother_money_button(agentID, currency)).add(
                                    buttons.mainmenuButton(agentID)).add(buttons.rus_help))

@dp.callback_query_handler(buttons.enother_money.filter())
async def enother_money_holder(call: types.callback_query, callback_data: dict):
    agentID, currency = callback_data.get('agentID'), callback_data.get('currency')
    agent = SQL.CheckAgent(agentID)
    if not call.message.chat.username:
        text = f'Y тебя закрытый профиль или отсутвует Username.\nПиши на прямую нашему агенту @{agent[2]}'
        bot.send_message(text=text,
                         chat_id=call.message.chat.id,
                         reply_markup=buttons.choice_currency_local(agentID).add(
                                    buttons.mainmenuButton(agentID)).add(buttons.rus_help))
    else:
        for admin in admins:
            await bot.send_message(text=f'@{call.message.chat.username} нажал на другую сумму',
                                   chat_id=admin)
        await bot.send_message(text=f'Пиши на прямую нашему агенту @{agent[2]}',
                               chat_id=call.message.chat.id)

@dp.callback_query_handler(buttons.choise_count_money.filter())
async def enother_money_holder(call: types.callback_query, callback_data: dict):
    agentID, currency, count = callback_data.get('agentID'), callback_data.get('currency'), callback_data.get('count')
    agent = SQL.CheckAgent(agentID)
    if not call.message.chat.username:
        text = f'Y тебя закрытый профиль или отсутвует Username.\nПиши на прямую нашему агенту @{agent[2]}'
        bot.send_message(text=text,
                         chat_id=call.message.chat.id,
                         reply_markup=buttons.choice_currency_local(agentID).add(
                                    buttons.mainmenuButton(agentID)).add(buttons.rus_help))
    else:
        for admin in admins:
            await bot.send_message(text=f'@{call.message.chat.username}\n{currency}, {count}',
                                   chat_id=admin)
        await bot.send_message(text=f'Пиши на прямую нашему агенту @{agent[2]}',
                               chat_id=call.message.chat.id)