# TranscriptTwo — Telegram бот для расшифровки аудио и видео

---

##  Возможности

- Расшифровка **аудио** и **видео** в текст
- Поддержка форматов: `.mp3`, `.wav`, `.ogg`, `.m4a`, `.mp4`, `.mov`, `.avi`
- Поддержка **голосовых сообщений**
- Выбор языка распознавания через команду `/language`
- Офлайн работа через `openai-whisper`
- Docker
- Подсчёт примерного времени обработки
- предлагает пользователю выбрать формат постобработки:
- Техническое задание
- Задача
- Протокол совещания
- и отправляет преобразованный результат с помощью GPT.

---

## Установка и запуск

В файле `config.py` вы можете изменить:

- Token — токен Telegram-бота
- Model_Transcriber — модель Whisper (tiny, base, small, medium, large)
- Max_File_Size_MB — максимальный размер файла
- Max_Duration_Minutes — максимальная длительность записи
- TEMP_DIR — директория для временных файлов

Перед установкой и запуском требуется запущенный Docker

```bash
git clone https://github.com/DarkKnife121204/TranscriptTwo
cd TranscriptTwo
docker build -t transcript-two .
docker run --name transcript-bot transcript-two
```