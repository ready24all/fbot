from aiogram import Dispatcher, Router, Bot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')



dp = Dispatcher()
my_router = Router(name=__name__)
bot = Bot(TOKEN)
dp.include_router(my_router)

