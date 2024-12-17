from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Задание 1: Главное меню
def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
        ],
        resize_keyboard=True
    )

# Задание 2: Кнопки с URL-ссылками
def get_links_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Новости", url="https://ria.ru/")],
            [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/home")],
            [InlineKeyboardButton(text="Видео", url="https://ria.ru/video/")]
        ]
    )

# Задание 3: Динамическое изменение клавиатуры
def get_dynamic_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
        ]
    )

def get_dynamic_options():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
            [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
        ]
    )
