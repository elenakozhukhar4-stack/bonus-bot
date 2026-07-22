import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Зареєструватися")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Вітаємо!\n\n"
        "Ласкаво просимо до нашої бонусної програми.\n\n"
        "Натисніть кнопку нижче, щоб зареєструватися.",
        reply_markup=register_keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())