from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    what_to_wear_button = KeyboardButton(text='Что надеть?')
    change_location_button = KeyboardButton(text='Сменить местоположение')

    keyboard.add(what_to_wear_button)
    keyboard.add(change_location_button)

    return keyboard
