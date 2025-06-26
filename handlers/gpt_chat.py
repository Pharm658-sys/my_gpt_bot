from aiogram import Router, F
from aiogram.types import Message
from openai import AsyncOpenAI
from my_gpt_bot.config import OPENAI_API_KEY
from my_gpt_bot.keyboards.replay_kb import get_start_kb
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam, ChatCompletionMessageParam

router = Router()
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

@router.message(F.text == "/start")
async def start_handler(msg: Message):
	await msg.answer("Привет! Я бот с ChatGPT. Напиши свой вопрос:", reply_markup=get_start_kb())


@router.message()
async def gpt_handler(msg: Message):
	try:
		messages: list[ChatCompletionMessageParam] = [
			ChatCompletionSystemMessageParam(role="system", content="Ты умный ассистент."),
			ChatCompletionUserMessageParam(role="user", content=msg.text),
		]

		response = await client.chat.completions.create(
			model="chatgpt-4o-latest",
			messages=messages,
		)
		answer = response.choices[0].message.content
		await msg.answer(answer)
	except Exception as e:
		await msg.answer(f"Ошибка: {e}")



