import asyncio
try:
    from .bot import  bot, dp
    from .schedule import repeat
except (ModuleNotFoundError, ImportError):
    from rsi_30_70_bot.bot  import bot, dp
    from rsi_30_70_bot.schedule import start

async def  main():
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(dp.start_polling(bot), repeat())

if __name__   == '__main__':
    asyncio.run(main())