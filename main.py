import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
from config import TOKEN


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Задание 1: Простое меню с кнопками
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Привет"), KeyboardButton("Пока"))
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@dp.message()
async def handle_text_buttons(message: types.Message):
    if message.text == "Привет":
        await message.answer(f"Привет, {message.from_user.first_name}!")
    elif message.text == "Пока":
        await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Кнопки с URL-ссылками
@dp.message(Command("links"))
async def links_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Новости", url="https://news.yandex.ru"),
        InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru"),
        InlineKeyboardButton(text="Видео", url="https://youtube.com")
    )
    await message.answer("Вот ссылки на интересные ресурсы:", reply_markup=keyboard)

# Задание 3: Динамическое изменение клавиатуры
@dp.message(Command("dynamic"))
async def dynamic_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    await message.answer("Нажмите на кнопку, чтобы увидеть больше опций:", reply_markup=keyboard)

@dp.callback_query(lambda callback_query: callback_query.data == "show_more")
async def show_more_options(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Опция 1", callback_data="option_1"),
        InlineKeyboardButton(text="Опция 2", callback_data="option_2")
    )
    await bot.edit_message_text(
        text="Выберите одну из опций:",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=keyboard
    )

@dp.callback_query(lambda callback_query: callback_query.data in ["option_1", "option_2"])
async def handle_options(callback_query: types.CallbackQuery):
    option_text = "Опция 1" if callback_query.data == "option_1" else "Опция 2"
    await callback_query.message.answer(f"Вы выбрали: {option_text}")

# Запуск бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
