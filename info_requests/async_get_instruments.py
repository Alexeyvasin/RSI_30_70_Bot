import asyncio
import os
from pprint import pprint

from  settings import allowed_trading_status

from info_requests.async_get_etfs import get_etfs
from info_requests.async_get_shares import get_shares

TOKEN = os.environ["INVEST_TOKEN"]

async def get_instruments(ticker=None):

    if not ticker:
        shares, etfs = await asyncio.gather(get_shares(), get_etfs())
        instruments = shares.instruments + etfs.instruments

        # if instruments:
        #     async with aiofiles.open('instruments.txt', 'w') as f_instruments:
        #         for instrument in instruments:
        #             await f_instruments.write(f'{instrument}\n******************\n')

        return  instruments

async def main():
    instruments = await get_instruments()
    # if instruments:
    #     pprint(tuple(instruments))
    print('*len',  len(instruments))
    f_inst  = []
    for instrument  in instruments:
        if instrument.trading_status in allowed_trading_status:
            f_inst.append(instrument)


if __name__ == "__main__":
    asyncio.run(main())
