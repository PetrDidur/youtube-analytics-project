import json
import os
import requests
from googleapiclient.discovery import build

api_key = os.getenv('YT_API_KEY')
print(api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        youtube = build('youtube', 'v3', developerKey="AIzaSyAVUjvEjAiQAlylR6Zlnm7KRBJI1qta70o")
        self.channel_id = channel_id
        self.channel_info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info["items"][0]["snippet"]["title"]
        self.description = self.channel_info["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
        self.subscriber_count = self.channel_info["items"][0]["statistics"].get("subscriberCount")
        self.video_count = self.channel_info["items"][0]["statistics"].get("videoCount")
        self.view_count = self.channel_info["items"][0]["statistics"].get("viewCount")



    def print_info(self) -> None:
        youtube = build('youtube', 'v3', developerKey="AIzaSyAVUjvEjAiQAlylR6Zlnm7KRBJI1qta70o")
        channels = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channels)

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey="AIzaSyAVUjvEjAiQAlylR6Zlnm7KRBJI1qta70o")
        return youtube

    def to_json(self, filename):
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count

        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return data







