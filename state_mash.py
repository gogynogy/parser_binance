from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup


class kalculator(StatesGroup):
    first = State()
    second = State()
    count = State()

values = [
    'USDT',
    'LKR',
    'Rub'
]

def buttons_curensy():
    buttons = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    button_list = [name for name in values]
    return buttons.add(*button_list)

def second_currency(first_currency):
    buttons = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    button_list = []
    for name in values:
        if name != first_currency:
            button_list.append(name)
    return buttons.add(*button_list)
