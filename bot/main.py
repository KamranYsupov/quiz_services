import asyncio

import loguru

from loader import bot, dp
from handlers.routing import get_main_router
from core.container import Container
from core import config

async def main():
    """Запуск бота"""
    dp.include_router(get_main_router())

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    loguru.logger.info('Bot is starting')

    container = Container()
    container.init_resources()
    container.wire(modules=config.CONTAINER_WIRING_MODULES)

    asyncio.run(main())