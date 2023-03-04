import os
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from get_started_keyboard import get_started_keyboard
from get_location_keyboard import get_location_keyboard
from states import ProfileCreateStatesGroup

from database.insert_data import test_name_for_func


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                            FOR CONNECTION TO DATABASE                                            '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
load_dotenv('../database/.env.db.config')

host = os.environ.get('HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('PASSWORD')
db_name = os.environ.get('DB_NAME')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

load_dotenv('.env')

storage = MemoryStorage()

token = os.environ.get('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text='Привет, прежде чем мы продолжим, давай познакомимся!'
    )
    await message.answer(
        text='Я создан, чтобы помочь тебе надеть одежду, '
             'в которой тебе будет комфортно. Я принимаю свои решения на'
             ' основе текущей погоды на улице.',
        reply_markup=get_started_keyboard()
    )


@dp.message_handler()
async def get_started(message: types.Message) -> None:
    if message.text == 'Давай начнем!':
        await ProfileCreateStatesGroup.name.set()
        await message.answer(
            text='Как тебя зовут?'
        )


@dp.message_handler(state=ProfileCreateStatesGroup.name)
async def save_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['name'] = message.text

        await message.answer(
            text='Теперь отправь мне свои координаты. '
                 'Это нужно мне для того, чтобы знать какая у тебя сейчас погода!'
                 'Отправлять координаты нужно с телефона!',
            reply_markup=get_location_keyboard()
        )

        await ProfileCreateStatesGroup.next()


@dp.message_handler(content_types=['location'], state=ProfileCreateStatesGroup.location)
async def save_location(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['latitude'] = message.location.latitude
        data['longitude'] = message.location.longitude

        test_name_for_func(
            host=host,
            user=user,
            password=password,
            db_name=db_name,
            identifier=data['id'],
            name=f"'{data['name']}'",
            latitude=data['latitude'],
            longitude=data['longitude']
        )

        print(data)

    await message.answer('Пока это все, что я умею')

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
