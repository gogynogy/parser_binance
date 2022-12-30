from config.config import admins
from loader import bot

def write_admin(message):
    for admin in admins:
        bot.send_message(admin, message)

async def on_start_up_notify():
    for admin in admins:
        await bot.send_message(admin, "бот запущен")

async def on_finish_notify():
    for admin in admins:
        await bot.send_message(admin, "бот наебнулся")