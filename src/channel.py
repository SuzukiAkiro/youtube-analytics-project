from googleapiclient.discovery import build
import os
import json

# Получаем API ключ из переменных окружения
api_key = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def json_printer(self, print_task: dict) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(print_task, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return self.json_printer(channel)
