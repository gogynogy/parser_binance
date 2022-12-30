from aiogram.utils import executor

from hendlers import dp
from notify_admins import on_start_up_notify, on_finish_notify
from setBotCommands import set_default_commands
from SQLBD import SQL

SQL = SQL()

async def on_startup(dp):
    await on_start_up_notify()
    await set_default_commands(dp)
    SQL.checkDB()
    print("бот запущен")

async def on_shutdown(dp):
    await on_finish_notify()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
