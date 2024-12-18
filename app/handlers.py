from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    phone = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello", reply_markup=kb.main)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Can I help you?")


@router.message(F.text == "Catalog")
async def catalog(message: Message):
    await message.answer("Select product category", reply_markup=kb.catalog)


@router.callback_query(F.data == "oil")
async def oil(callback: CallbackQuery):
    await callback.answer("You have selected category")
    await callback.message.answer("You have selected oil category")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Enter your username")


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Enter your age")


@router.message(Register.age)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.phone)
    await message.answer("Enter your phone", reply_markup=kb.get_phone)


@router.message(Register.phone, F.contact)
async def register_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Your name: {data['name']}\n Your age: {data['age']}\n Your phone: {data['phone']}"
    )
    await state.clear()
