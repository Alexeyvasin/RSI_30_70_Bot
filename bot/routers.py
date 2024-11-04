import asyncio
import logging
import os

import asyncpg

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from settings import exclude_instruments


logging.basicConfig(
    level='DEBUG'
)
logger = logging.getLogger(__name__)


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    logger.info('Start')
    await message.answer('Hello! I am started')


@router.message(Command('exclude_instruments'))
async def exclude_instruments(message: Message, state: FSMContext):

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
        values = await conn.fetch(
            '''SELECT * FROM filters WHERE "Key" = $1''', 'exclude_instrument'
        )

        for value  in values:
            print (value['value'])
    finally:
        await   conn.close()
async def  main():
    await   asyncio.gather(exclude_instruments(None))

if __name__ == '__main__':
    asyncio.run(main())



