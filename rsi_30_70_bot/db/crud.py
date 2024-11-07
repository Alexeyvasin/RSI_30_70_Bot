import os
import asyncpg

async def connect():
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
    return conn

async def get_exclude_instruments():
    exclude_instruments = []
    conn = await  connect()
    print(conn)
    try:
        values = await conn.fetch(
            '''SELECT * FROM filters WHERE "Key" = $1''', 'exclude_instrument'
        )
    finally:
        await conn.close()
    print(values)

    tuple(exclude_instruments.append(value['value']) for value in values)
    print('*exclude_inst', exclude_instruments)
    return exclude_instruments

async def del_all_exclude_instruments():
    conn = await connect()
    await conn.execute('''
                DELETE FROM filters   WHERE "Key" = $1''', 'exclude_instrument'
                       )
    conn.close()

async def del_instrument(instrument):
    conn = await connect()
    await conn.execute('''
                DELETE FROM filters   WHERE "Key" = $1 and "value" =  $2''',
                       'exclude_instrument', instrument
                       )
    conn.close()

async def add_instrument(instrument):
    conn = await connect()
    await conn.execute('''
                INSERT INTO  filters ("Key", "value") VALUES ($1, $2)''',
                       'exclude_instrument', instrument
                       )
    conn.close()