import logging

user_transcripts = {}


def save_transcript(user_id: int, text: str):
    logging.info(f"[User {user_id}] Сохраняем транскрипцию")
    user_transcripts[user_id] = text


def get_transcript(user_id: int):
    return user_transcripts.get(user_id)
