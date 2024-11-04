import os
from dotenv   import load_dotenv

from aiogram  import Bot, Dispatcher, types
try:
    from routers import router
except ModuleNotFoundError:
    from bot.routers import router


load_dotenv()

dp   = Dispatcher()

dp.include_router(router)

TOKEN  = os.getenv('BOT_TOKEN')

bot = Bot(TOKEN)