import os
import requests
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
print(api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

    def print_info(self) -> None:
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return print(channel)


