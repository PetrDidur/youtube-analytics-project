import json
import os
import datetime

import isodate

from googleapiclient.discovery import build

api_key = os.getenv('YT_API_KEY')


class PlayList:

    def __init__(self, playlist_id):
        self.youtube = build('youtube', 'v3', developerKey="AIzaSyAVUjvEjAiQAlylR6Zlnm7KRBJI1qta70o")
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(part='snippet', id=playlist_id).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()


    @property
    def total_duration(self):

        # printj(playlist_videos)

        # получить все id видеороликов из плейлиста

        # printj(video_response)
        total_duration = datetime.timedelta()

        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):

        max_like_counter = 0
        max_video_id = ""
        for video in self.video_response['items']:
            like_count = video["statistics"]["likeCount"]
            video_id = video['id']
            if int(like_count) > int(max_like_counter):
                max_like_counter = like_count
                max_video_id = video_id
        return f'https://youtu.be/{max_video_id}'









