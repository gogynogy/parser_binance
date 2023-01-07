from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

refresh = InlineKeyboardButton("Обновить", callback_data="Refresh")
menu = InlineKeyboardButton("Назад", callback_data="Refresh")
activiti_check = InlineKeyboardButton("Посмотреть активность", callback_data="check_activiti")
order = InlineKeyboardButton("Сделать заказ", callback_data="new_order")


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