from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

refresh = InlineKeyboardButton("Обновить", callback_data="Refresh")
menu = InlineKeyboardButton("Назад", callback_data="Refresh")
activiti_check = InlineKeyboardButton("Посмотреть активность", callback_data="check_activiti")
order = InlineKeyboardButton("Сделать заказ", callback_data="new_order")
info_luser = InlineKeyboardButton("loser", callback_data="info_luser")

order_admin = InlineKeyboardButton("Сделки", callback_data="orders_admin")
new_agent = InlineKeyboardButton("Добавить нового агента", callback_data="new_agent")
open_orders = InlineKeyboardButton("Посмотреть открытые сделки", callback_data="open_orders")
all_orders = InlineKeyboardButton("Посмотреть закрытые сделки", callback_data="all_orders")

agents = InlineKeyboardButton("Агенты", callback_data="agents")

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
    print(numm)
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text=f'Взять сделку {numm} в работу',
                                                                      callback_data=take_order.new(number=numm)))

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