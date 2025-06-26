from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_kb():
	return ReplyKeyboardMarkup(
		keyboard=[[KeyboardButton(text="🧠 Задать вопрос GPT")]],
		resize_keyboard=True
	)