from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Дать курсы валют'),
        types.BotCommand('info', 'Информация о боте'),
        # types.BotCommand('beer', 'хочу пива')
    ])