from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
import asyncio

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def run():
    print('🤖 Karnataka Superbot running...')
    await dp.start_polling(bot)

def start_bot():
    asyncio.run(run())
