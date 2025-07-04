import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.start import start_route
from handlers.media import media_route
from handlers.language import language_router
from handlers.prompt import prompt_route

from config import Token

bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()


async def main():
    dp.include_router(start_route)
    dp.include_router(language_router)
    dp.include_router(prompt_route)
    dp.include_router(media_route)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')