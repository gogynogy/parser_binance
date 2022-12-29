from aiogram.utils import executor

from start import dp
from notify_admins import on_start_up_notify
from setBotCommands import set_default_commands
from telega.SQLBD import SQL

SQL = SQL()

async def on_startup(dp):
    await on_start_up_notify()
    await set_default_commands(dp)
    SQL.checkDB()
    print("бот запущен")

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)
