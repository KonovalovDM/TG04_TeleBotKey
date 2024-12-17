import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards import get_main_menu, get_links_menu, get_dynamic_menu, get_dynamic_options
from config import TOKEN

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Задание 1: Простое меню
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Выберите действие:", reply_markup=get_main_menu())

@dp.message(lambda msg: msg.text == "Привет")
async def hello_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(lambda msg: msg.text == "Пока")
async def goodbye_command(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Кнопки с URL-ссылками
@dp.message(Command("links"))
async def links_command(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=get_links_menu())

# Задание 3: Динамическое изменение клавиатуры
@dp.message(Command("dynamic"))
async def dynamic_command(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=get_dynamic_menu())

@dp.callback_query(lambda call: call.data == "show_more")
async def show_more_callback(callback: CallbackQuery):
    await callback.message.edit_text("Выберите одну из опций:", reply_markup=get_dynamic_options())
    await callback.answer()

@dp.callback_query(lambda call: call.data in ["option_1", "option_2"])
async def option_selected_callback(callback: CallbackQuery):
    option_text = "Опция 1" if callback.data == "option_1" else "Опция 2"
    await callback.message.answer(f"Вы выбрали: {option_text}")
    await callback.answer()

# Запуск бота
async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
