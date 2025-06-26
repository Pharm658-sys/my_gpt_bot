import asyncio
from aiogram import Bot, Dispatcher
from my_gpt_bot.config import BOT_TOKEN
from my_gpt_bot.handlers import gpt_chat

async def main():
	bot = Bot(token=BOT_TOKEN)
	dp = Dispatcher()

	dp.include_router(gpt_chat.router)

	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())

