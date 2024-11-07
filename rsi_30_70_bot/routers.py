import asyncio
import logging
import os

import asyncpg

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
try:
    from .states import BotStates
    from .schedule import searcher
except ImportError:
    from parent_package.rsi_30_70_bot.states import BotStates
    from parent_package.rsi_30_70_bot.schedule import searcher
from .db import crud



logging.basicConfig(
    level='DEBUG'
)
logger = logging.getLogger(__name__)


router = Router()

@router.message(Command('search'))
async def search(message:  Message):
    logger.info('Search')
    await searcher()



@router.message(Command('start'))
async def start(message: Message):
    logger.info('Start')
    await message.answer('Hello! I am started')


@router.message(Command('exclude_instruments'))
async def exclude_instruments(message: Message, state: FSMContext):
    print(await state.get_state())
    exclude_instr = []

    name = os.getenv('DB_NAME')
    username = os.getenv('DB_USERNAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    password = os.getenv('DB_PASSWORD')
    conn = await asyncpg.connect(
        host=host,
        password=password,
        database=name,
        port=port,
        user=username,
        )
    try:
        print(type(conn))
        values = await conn.fetch(
            '''SELECT * FROM filters WHERE "Key" = $1''', 'exclude_instrument'
        )

        for value  in values:
            exclude_instr.append(value['value'])

    finally:
        await   conn.close()

    await message.answer(
        f'На данный момент из выдачи исключены следующие инструменты: \n{exclude_instr}')
    await message.answer(
        f'Укажите тикер инструмента для исключения из поиска '
        f'\n(если указать "-" в начале - инструмент удалиться из списка исключений)'
        f'(если указать "0" - список исключений очистится')
    await state.set_state(BotStates.choosing_instruments)
    print(await state.get_state())

@router.message(StateFilter(BotStates.choosing_instruments))
async def set_exclude_instruments(message: types.Message, state: FSMContext):
    print('*set_', message)
    if message.text == '0':
        await crud.del_all_exclude_instruments()

    elif message.text.startswith('-'):
            await crud.del_instrument(message.text[1:].strip())

    else:
        await crud.add_instrument(message.text.strip())
    values = await crud.get_exclude_instruments()
    exclude_inst = []
    for value in values:
        exclude_inst.append(value)

    await message.answer(
        f'Исключены следующие инструменты: \n{exclude_inst}')
    await state.set_state(None)


# async def  main():
#     await   asyncio.gather(exclude_instruments(None))
#
# if __name__ == '__main__':
#     asyncio.run(main())



