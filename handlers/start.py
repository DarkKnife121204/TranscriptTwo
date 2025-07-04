from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_route = Router()
@start_route.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "<b>Я бот для расшифровки аудио и видео файлов в текст.</b>\n\n"
        "Отправь мне один из поддерживаемых файлов, и я верну текстовую транскрипцию.\n\n"
        "<b>Поддерживается:</b>\n"
        "• Голосовые сообщения\n"
        "• Аудиофайлы: .mp3, .wav, .ogg, .m4a\n"
        "• Видеофайлы: .mp4, .mov, .avi\n\n"
        "<b>Ограничения:</b>\n"
        "• Размер файла — до 500 МБ\n"
        "• Длительность — до 5 минут\n\n"
        "<b>Для лучшего качества распознавания выбери язык с помощью команды /language</b>\n"
        "Жду твой файл! 🎧"
    )