# ====================================================================================


from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

# ====================================================================================
 
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет. \nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}")

# ====================================================================================

@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Команда /help")

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("Хорошо")

# ====================================================================================

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")

@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMXZiIaO1xC0Xef6sX3lNcIaVKnX3gAAtjWMRuFDQFJQbsuuSjYreQBAAMCAAN5AAM0BA",
                               caption="Лого")

# ====================================================================================
