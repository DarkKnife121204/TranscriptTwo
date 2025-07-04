import logging
import g4f
import asyncio


async def run_gpt(prompt, text):
    logging.info("Отправляем запрос GPT")
    try:
        response = await g4f.ChatCompletion.create_async(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text},
            ],
        )
        return response
    except Exception as e:
        logging.exception("Ошибка при использовании GPT")
        return "Ошибка при обращении к GPT"
