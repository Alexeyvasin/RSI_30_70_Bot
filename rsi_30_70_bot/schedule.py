from datetime import timedelta
try:
    from settings import allowed_trading_status, time_of_repeat
except ModuleNotFoundError:
    try:
        from .settings import allowed_trading_status, time_of_repeat
    except (ModuleNotFoundError, ImportError):
        from ..settings import allowed_trading_status, time_of_repeat
from  tinkoff.invest.utils import now
import asyncio

from  rsi_30_70_bot.db.crud import get_exclude_instruments

async def searcher():
    try:
        from .bot import bot
    except ImportError:
        from rsi_30_70_bot.bot import bot
    from   strategies.on_rsi import rsi_30_70
    from info_requests import async_get_instruments as in_ts
    await bot.send_message(-4566773371, 'Start')
    exclude_instruments = await get_exclude_instruments()
    print('*excl_instr', exclude_instruments)
    semaphore = asyncio.Semaphore(15)
    instruments = await in_ts.get_instruments()

    coro = (
        rsi_30_70(instrument, semaphore)
        for instrument in instruments
        if (
            instrument.trading_status in allowed_trading_status and
            instrument.ticker not in exclude_instruments
            )
        )
    await asyncio.gather(*coro)
    await bot.send_message(-4566773371, 'Finish')


async def repeat(every_min=time_of_repeat):
    before_start_time = None
    while  True:
        if before_start_time  is  None or now()-before_start_time >= timedelta(minutes=every_min):
            before_start_time = now()
            await searcher()
        await asyncio.sleep(30)

async def main():

    await asyncio.gather(repeat())

if __name__=='__main__':
    asyncio.run(main())