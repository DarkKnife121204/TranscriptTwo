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
- и отправляет результат, преобразованный с помощью GPT.

---

## Установка и запуск

Токен Telegram-бота указывается в файле `config.py` в переменной `Token`.
Токен OpenAI указывается в файле `config.py` в переменной `OPENAI_API_KEY`

Перед установкой и запуском требуется запущенный Docker

```bash
git clone https://github.com/DarkKnife121204/TranscriptTwo
cd TranscriptTwo
docker build -t transcript-two .
docker run --name transcript-bot transcript-two
```