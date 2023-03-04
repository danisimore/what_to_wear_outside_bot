from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileCreateStatesGroup(StatesGroup):
    name = State()
    location = State()
