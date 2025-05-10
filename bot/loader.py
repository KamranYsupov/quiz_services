from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from core import config

bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)
dp = Dispatcher()