import asyncio

from aiogram.exceptions import TelegramRetryAfter

from settings import allowed_trading_status

from info_requests import async_get_rsi as rsi
from info_requests import async_get_instruments  as in_ts


from  bot import bot


async def rsi_30_70(instrument, semaphore=None):
    if  semaphore is None:
        semaphore   = asyncio.Semaphore(1)
    async  with   semaphore:
        res = await rsi.get_rsi(instrument, days_ago=3)
        if res:
            if (unit := int(res[-1].signal.units)) >= 70 or (unit := int(res[-1].signal.units)) < 30:
                try:
                    await bot.send_message(-4566773371, f'@AlexInvestorBot {instrument.ticker}={unit}. {res[-1]}')
                except TelegramRetryAfter as e:
                    print(f"Rate limit exceeded. Retrying after {e.retry_after} seconds...")
                    await asyncio.sleep(e.retry_after)
                    await bot.send_message(-4566773371, f'@AlexInvestorBot {instrument.ticker}={unit}. {res[-1]}')



async  def main():
    semaphore = asyncio.Semaphore(15)
    instruments = await in_ts.get_instruments()
    coro   = (rsi_30_70(instrument, semaphore)
              for instrument in instruments
              if instrument.trading_status in allowed_trading_status)
    await asyncio.gather(*coro)




if __name__ == '__main__':
    asyncio.run(main())
