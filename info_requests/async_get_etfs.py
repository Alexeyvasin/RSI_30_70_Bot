import asyncio
import os
import aiofiles

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import InstrumentExchangeType

TOKEN = os.environ["INVEST_TOKEN"]

async def get_etfs(ticker=None):

    if not ticker:
        async with AsyncClient(TOKEN) as client:
            etfs = await client.instruments.etfs()
            # async with aiofiles.open('etfs.txt', 'w') as f_etfs:
            #     for etf  in etfs.instruments:
            #         await f_etfs.write(f'{etf}\n******************\n')
            return  etfs

async def main():
    etfs = await get_etfs()
    for  etf in etfs.instruments:
        print(etf.ticker)



if __name__ == "__main__":
    asyncio.run(main())
