from config.config import admins, geo
from loader import bot

def write_admin(message):
    for admin in admins:
        bot.send_message(admin, message)

async def on_start_up_notify():
    await bot.send_message(geo, "бот запущен")

async def on_finish_notify():
    await bot.send_message(geo, "бот наебнулся")