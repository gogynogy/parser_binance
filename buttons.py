from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton



menu = InlineKeyboardButton("Обновить", callback_data="Refresh")
activiti_check = InlineKeyboardButton("Посмотреть активность", callback_data="check_activiti")


def cancelOperation():
    """Кнопка закрывания текущего действия"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(f'Галя, у нас отмена!!!', callback_data="cancel")]])
