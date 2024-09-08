from bot.config import token, msg
from aiogram import Bot, Dispatcher, executor

API_TOKEN = token

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def message(text=msg):
    await bot.send_message(-1001941678039, text)


def error_message_tg():
    executor.start(dp, message())
