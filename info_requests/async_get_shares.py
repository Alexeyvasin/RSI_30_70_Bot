import asyncio
import os

from tinkoff.invest import AsyncClient

TOKEN = os.environ["INVEST_TOKEN"]

async def get_shares(ticker=None):
    if not ticker:
        async with AsyncClient(TOKEN) as client:
            shares = await client.instruments.shares()
            return  shares

async def main():
    shares = await get_shares()
    for share  in shares.instruments:
        print(share.ticker)




if __name__ == "__main__":
    asyncio.run(main())
