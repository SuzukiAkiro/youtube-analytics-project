from googleapiclient.discovery import build
import os
import json

# Получаем API ключ из переменных окружения
api_key = os.getenv("YT_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = (
            youtube.channels()
            .list(id=self.__channel_id, part="snippet,statistics")
            .execute()
        )
        return json.dumps(channel, indent=4, ensure_ascii=False)

    @property
    def title(self) -> str:
        """Возвращает название канала."""
        channel = (
            youtube.channels().list(id=self.__channel_id, part="snippet").execute()
        )
        return channel["items"][0]["snippet"]["title"]

    @property
    def url(self) -> str:
        """Возвращает url канала."""
        return f"https://www.youtube.com/channel/{self.__channel_id}"

    @property
    def video_count(self) -> int:
        """Возвращает количество видео в канале."""
        channel = (
            youtube.channels().list(id=self.__channel_id, part="statistics").execute()
        )
        return int(channel["items"][0]["statistics"]["videoCount"])

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        api_key = os.getenv("YT_API_KEY")
        youtube = build("youtube", "v3", developerKey=api_key)
        return youtube

    def to_json(self, file_name: str) -> None:
        channel = {
            "channel_id": self.channel_id,
            "title": self.title,
            "url": self.url,
            "video_count": self.video_count,
        }
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(channel, file, ensure_ascii=False, indent=4)
