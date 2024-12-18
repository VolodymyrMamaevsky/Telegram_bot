from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello", reply_markup=kb.main)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Can I help you?")


@router.message(F.text == "Catalog")
async def catalog(message: Message):
    await message.answer("Select product category", reply_markup=kb.catalog)
