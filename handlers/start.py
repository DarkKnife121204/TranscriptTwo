from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_route = Router()


@start_route.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "*Я бот для расшифровки аудио и видео файлов в текст*\\.\\.*\\n\\n"
        "Отправь мне один из поддерживаемых файлов, и я верну текстовую транскрипцию\\.\\n\\n"
        "*Поддерживается:*\\n"
        "• Голосовые сообщения\\n"
        "• Аудиофайлы: `.mp3`, `.wav`, `.ogg`, `.m4a`\\n"
        "• Видеофайлы: `.mp4`, `.mov`, `.avi`\\n\\n"
        "*Ограничения:*\\n"
        "• Размер файла — до *500 МБ*\\n"
        "• Длительность — до *5 минут*\\n\\n"
        "*Для улучшения качества распознавания выбери язык с помощью команды* `/language`\\n"
        "*После получения текста ты сможешь выбрать формат его преобразования через GPT*\\n\\n"
        "Жду твой файл!"
    )
