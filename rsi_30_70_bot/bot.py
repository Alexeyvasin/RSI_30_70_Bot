import os
from dotenv   import load_dotenv

from aiogram  import Bot, Dispatcher, types
try:
    from rsi_30_70_bot.routers import router
except ModuleNotFoundError:
    from .routers import router


load_dotenv()

dp   = Dispatcher()
try:
    dp.include_router(router)
except RuntimeError:
    print('Router already  attached')

TOKEN  = os.getenv('BOT_TOKEN')

bot = Bot(TOKEN)