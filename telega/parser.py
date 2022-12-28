from aiogram.utils import executor

from start import dp
from notify_admins import on_start_up_notify
from setBotCommands import set_default_commands

async def on_startup(dp):
    await on_start_up_notify()
    await set_default_commands(dp)
    print("бот запущен")

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)
