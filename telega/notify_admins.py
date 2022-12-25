from telega.config.config import admins
from telega.loader import bot

async def write_admin(message):
    for admin in admins:
        await bot.send_message(admin, message)

async def on_start_up_notify():
    for admin in admins:
        await bot.send_message(admin, "бот запущен")
