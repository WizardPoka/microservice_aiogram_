# ====================================================================================

# Reply клавиатура снизу ввода
# Inline клавиатура привязана к сообщению

# ====================================================================================

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

# С помощью Builder можно создавать кнопки и значения к ним с помощью бд к примеру

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# ====================================================================================

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
    ],
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню.")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url = "https://youtube.com")]
    ])

# ====================================================================================

cars = ["Tesla", "BMW", "Lada", "Dodge", "Toyota"]

async def reply_cars():
    keyboard = ReplyKeyboardBuilder()

    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    
    # .adjust(2) - сколько кнопок в одной строке
    return keyboard.adjust(2).as_markup()


async def inline_cars():
    keyboard = InlineKeyboardBuilder()

    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url = "https://youtube.com"))

    # .adjust(2) - сколько кнопок в одной строке
    return keyboard.adjust(2).as_markup()
# ====================================================================================
