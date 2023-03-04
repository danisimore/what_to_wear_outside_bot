from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_started_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    get_started_button = KeyboardButton(text='Давай начнем!')
    keyboard.add(get_started_button)

    return keyboard
