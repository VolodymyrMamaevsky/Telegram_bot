from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Catalog")],
        [KeyboardButton(text="Cart")],
        [
            KeyboardButton(text="Contacts"),
            KeyboardButton(text="About us"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Select menu item...",
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Oil", callback_data="oil")],
        [InlineKeyboardButton(text="Tools", callback_data="tools")],
        [InlineKeyboardButton(text="Filters", callback_data="filters")],
    ]
)
