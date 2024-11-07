import asyncio
import os
from datetime import timedelta

from grpc import StatusCode
from pprint import pprint


from tinkoff.invest import AsyncClient, AioRequestError
from tinkoff.invest.schemas import (
    GetTechAnalysisRequest,
    IndicatorInterval,
    IndicatorType,
    TypeOfPrice, Deviation, Smoothing,
)
from tinkoff.invest.utils import decimal_to_quotation, now

try:
    from async_get_instruments import get_instruments
except ModuleNotFoundError:
    from .async_get_instruments import get_instruments


TOKEN = os.environ["INVEST_TOKEN"]
MAX_RETRIES = 100
RETRY_DELAY = 2


async def get_rsi(
        instrument,
        semaphore=None,
        days_ago=3,
        interval=IndicatorInterval.INDICATOR_INTERVAL_ONE_HOUR,
        type_of_price=TypeOfPrice.TYPE_OF_PRICE_CLOSE,
        length=14
):
    if semaphore is None:
        semaphore = asyncio.Semaphore(1)
    async with semaphore:
        # print('*sem',  semaphore)
        async with AsyncClient(TOKEN) as client:
            rsi_request = GetTechAnalysisRequest(
                indicator_type=IndicatorType.INDICATOR_TYPE_RSI,
                instrument_uid=instrument.uid,
                from_=now() - timedelta(days=days_ago),
                to=now(),
                interval=interval,
                type_of_price=type_of_price,
                length=length,
                # deviation=Deviation(
                #     deviation_multiplier=decimal_to_quotation(Decimal(1.0)),
                # ),
                # smoothing=Smoothing(fast_length=14, slow_length=7, signal_smoothing=3),
            )
            retries = 0
            while retries < MAX_RETRIES:
                try:
                    response = await client.market_data.get_tech_analysis(request=rsi_request)
                    if response.technical_indicators:
                        # pprint(response.technical_indicators)
                        return response.technical_indicators
                        # with open('rsi.txt', 'a') as f_rsi:
                        #     f_rsi.write(instrument.ticker+'\n' + str(response.technical_indicators) + '\n')
                        #     f_rsi.write('************************'+'\n')
                    return
                except AioRequestError as e:
                    if e.args[0] == StatusCode.RESOURCE_EXHAUSTED:
                        # print("Rate limit exceeded, retrying in", RETRY_DELAY, "seconds...")
                        await asyncio.sleep(RETRY_DELAY)
                    else:
                        raise
                retries  += 1

async def main():
    instruments = await get_instruments()
    semaphore = asyncio.Semaphore(15)
    ticker = 'GOLD'
    coro = (
        get_rsi(instrument=instrument, semaphore=semaphore, days_ago=3)
        for instrument in instruments
        if instrument.ticker  == ticker
    )
    for   instrument  in  instruments:
        if  instrument.ticker  ==   ticker:
            print(instrument.ticker, instrument.uid, instrument.name)
    coro_tup = tuple(coro)
    print(len(coro_tup))
    res = await asyncio.gather(*coro_tup)
    pprint(res)
    for  r in res:
        if r is not  None:
            for indicator in r:
                print(indicator.timestamp,  round((indicator.signal.nano/10**9 + int(indicator.signal.units)), 2))

    # for instrument in instruments:
    #
    #     print(instrument.ticker)
    #     await get_rsi(instrument)


if __name__ == "__main__":
    asyncio.run(main())
