import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Status: OFF")
