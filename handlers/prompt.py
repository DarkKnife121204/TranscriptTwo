import logging
import json
from pathlib import Path
from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.storage import get_transcript
from services.gpt_service import run_gpt

PROMPTS_PATH = Path(__file__).parent / "prompts.json"


def load_prompts():
    with open(PROMPTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


prompts = load_prompts()


prompt_route = Router()


def get_format_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for key in prompts:
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(text=key, callback_data=key)
        ])
    return keyboard


@prompt_route.callback_query(F.data)
async def handle_format_callback(callback):
    user_id = callback.from_user.id
    prompt_key = callback.data
    logging.info(f"[User {user_id}] Нажал кнопку: {prompt_key}")

    text = get_transcript(user_id)
    prompt = prompts[prompt_key]
    await callback.message.answer("Обработка через GPT...")

    try:
        result = await run_gpt(prompt, text)
        logging.info(f"[User {user_id}] GPT успешно обработал запрос.")
        await callback.message.answer(result)
    except Exception as e:
        logging.exception(f"[User {user_id}] Ошибка при обработке GPT")
        await callback.message.answer("Ошибка обработки текста.")
