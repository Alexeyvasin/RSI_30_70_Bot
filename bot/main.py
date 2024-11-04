import asyncio
try:
    from .bot import  bot, dp
    from .schedule import start
except (ModuleNotFoundError, ImportError):
    from bot  import bot, dp
    from schedule import start

async def  main():
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(dp.start_polling(bot), start())

if __name__   == '__main__':
    asyncio.run(main())