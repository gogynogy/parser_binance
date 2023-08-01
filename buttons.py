from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from SQLBD import SQL

SQL = SQL()

from messages.order_messages import give_currency_to_LKR, format_number_with_spaces

refresh = InlineKeyboardButton("Обновить", callback_data="Refresh")
menu = InlineKeyboardButton("Назад", callback_data="Refresh")
activiti_check = InlineKeyboardButton("Посмотреть активность", callback_data="check_activiti")
send_message = InlineKeyboardButton("Текст для отправки", callback_data="send_message")
vietnam_currency = InlineKeyboardButton("Курсы по вьетнаму", callback_data="vietnam_currency")


order_admin = InlineKeyboardButton("Сделки", callback_data="orders_admin")
new_agent = InlineKeyboardButton("Добавить нового агента", callback_data="new_agent")
open_orders = InlineKeyboardButton("Посмотреть открытые сделки", callback_data="open_orders")
all_orders = InlineKeyboardButton("Посмотреть закрытые сделки", callback_data="all_orders")
calkulator = InlineKeyboardButton("Калькулятор", callback_data="calkulator")

rus_help = InlineKeyboardButton("Нужна русскоязычная помощь", callback_data="rus_help")

agents = InlineKeyboardButton("Агенты", callback_data="agents")


order = InlineKeyboardButton("Сделать заказ", callback_data="new_order")
give_contact = KeyboardButton('Отправить свой контакт', request_contact=True, )


def cancelOperation():
    """Кнопка закрывания текущего действия"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(f'Галя, у нас отмена!!!', callback_data="cancel")]])


locations = [
    "Коломбо",
    "Галле",
    "Унаватуна",
    "Велигама",
    "Мирисса",
    "Матара",
    "Канди",
    "Элла"
]

start_order = CallbackData('w', 'what')
def make_button_locations():
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=city, callback_data=start_order.new(what=city)) for city in locations]
    return buttons.add(*button_list)

take_order = CallbackData('a', 'number')
def take_order_work(numm):
    return InlineKeyboardButton(text=f'Взять сделку {numm} в работу', callback_data=take_order.new(number=numm))

continue_order = CallbackData('s', 'where', 'how_much')
def order_count_money(location):
    buttons = InlineKeyboardMarkup(row_width=1)
    prices = []
    tourist_place = ['Галле', 'Унаватуна', 'Велигама', 'Мирисса', 'Матара']
    if location in tourist_place:
        prices = ['50 000', '100 000', '200 000', '400 000']
    elif location == 'Коломбо':
        prices = ['300 000', '600 000', '800 000', '1 000 000']
    elif location == 'Канди' or location == 'Элла':
        prices = ['80 000', '100 000', '150 000', '200 000']
    button_list = [InlineKeyboardButton(text=f"Заказать {price} LKR",
                                        callback_data=continue_order.new(where=location, how_much=price))
                                        for price in prices]
    return buttons.add(*button_list).add(menu)

def write_customer(message: types.Message):
    button_url = f'tg://openmessage?user_id={message.chat.id}'
    return InlineKeyboardButton(text=f'написать {message.chat.first_name}',
                                url=button_url)

local_order = CallbackData('b', 'agentID', 'currency')
def choice_currency_local(agentID):
    buttons = InlineKeyboardMarkup(row_width=2)
    rub = InlineKeyboardButton(text=f'Поменять рубли', callback_data=local_order.new(agentID=agentID, currency='rub'))
    usdt = InlineKeyboardButton(text=f'Поменять USDT', callback_data=local_order.new(agentID=agentID, currency='usdt'))
    buttonList = buttons.add(rub, usdt)
    return buttonList

choise_count_money = CallbackData('c', 'agentID', 'currency', 'count')
def choice_count_money_local(agentID, currency):
    agent_percent = SQL.CheckAgent(agentID)[4]
    rate = give_currency_to_LKR(currency, agent_percent)
    buttons = InlineKeyboardMarkup(row_width=1)
    prices = [100000, 200000]
    if currency == 'rub':
        button_list = [InlineKeyboardButton(text=f'{format_number_with_spaces(price / rate)} @ {currency} = {price} LKR',
                                        callback_data=choise_count_money.new(agentID=agentID, currency=currency, count=price))
                                        for price in prices]
    else:
        button_list = [InlineKeyboardButton(text=f'{round(price / rate, 2)} @ {currency} = {price} LKR',
                                        callback_data=choise_count_money.new(agentID=agentID, currency=currency, count=price))
                                        for price in prices]
    return buttons.add(*button_list)

back_to_main_menu = CallbackData('d', 'agentID')
def mainmenuButton(agentID):
    button = InlineKeyboardButton(text='Назад', callback_data=back_to_main_menu.new(agentID=agentID))
    return button

enother_money = CallbackData('d', 'agentID', 'currency')
def enother_money_button(agentID, currency):
    button = InlineKeyboardButton(text='Другая сумма', callback_data=enother_money.new(agentID=agentID, currency=currency))
    return button