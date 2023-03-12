from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_location_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    get_location_button = KeyboardButton(text='Отправить координаты', request_location=True)
    keyboard.add(get_location_button)

    return keyboard
