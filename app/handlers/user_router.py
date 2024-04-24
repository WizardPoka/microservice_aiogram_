# ====================================================================================

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.handlers.keyboards as kb

user_router = Router()


# ====================================================================================
 
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет. \nYour ID: {message.from_user.id}\nИмя: {message.from_user.first_name}",
                        reply_markup=kb.main)

# если переменная то без await
# reply_markup=kb.main

# если функция то await
# reply_markup=await kb.inline_cars()
# ====================================================================================

@user_router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Команда /help")

@user_router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMXZiIaO1xC0Xef6sX3lNcIaVKnX3gAAtjWMRuFDQFJQbsuuSjYreQBAAMCAAN5AAM0BA",
                               caption="Лого")

# ====================================================================================

@user_router.message(F.text.lower() == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("Хорошо")

@user_router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")

# ====================================================================================

@user_router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Привет", reply_markup=await kb.inline_cars())

# ====================================================================================

class Reg( StatesGroup):
    name = State()
    number = State()

@user_router.message(Command("reg"))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите ваше имя")

@user_router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Введите номер телефона")

@user_router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    print(f'Получено сообщение: {data["name"]}\nНомер: {data["number"]}')
    await message.answer(f'Регистрация завершена.\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()

# ====================================================================================

@user_router.message()
async def log_all_messages(message: Message):
    print(f"Получено сообщение: {message.text}")

# ====================================================================================
