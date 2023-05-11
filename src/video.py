from googleapiclient.discovery import build


class Video:
    video_id = '9lO06Zxhu88'

    def __init__(self, video_id):
        self.video_id = video_id
        youtube = build('youtube', 'v3', developerKey="AIzaSyAVUjvEjAiQAlylR6Zlnm7KRBJI1qta70o")
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        # printj(video_response)
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
        self.url = f"https://www.youtube.com/watch?v={video_id}"

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id, video_playlist):

        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return f"{self.video_title}"







