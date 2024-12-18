from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Can I help you?")


@router.message(F.text == "I'm ok!")
async def cmd_ok(message: Message):
    await message.answer("I'm happy")
