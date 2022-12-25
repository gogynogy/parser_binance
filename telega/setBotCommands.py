from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Дать курсы валют'),
        types.BotCommand('help', 'Помощь'),
        # types.BotCommand('beer', 'хочу пива')
    ])