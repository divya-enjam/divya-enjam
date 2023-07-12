from googleapiclient.discovery import build
from bert_extractive_summarizer import Summarizer

# YouTube API credentials (Replace with your own credentials)
API_KEY = 'YOUR_YOUTUBE_API_KEY'

# YouTube video ID
VIDEO_ID = 'YOUR_YOUTUBE_VIDEO_ID'

# Build the YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Get the transcript for the specified video
def get_transcript(video_id):
    response = youtube.captions().list(
        part='id',
        videoId=video_id
    ).execute()

    if 'items' in response:
        caption_id = response['items'][0]['id']
        transcript = youtube.captions().download(
            id=caption_id,
            tfmt='srt'
        ).execute()

        return transcript['body']

    return None

# Summarize the transcript
def summarize_transcript(transcript):
    summarizer = Summarizer()
    summary = summarizer(transcript, ratio=0.3)  # Adjust the ratio to control the summary length

    return summary

# Fetch the transcript for the YouTube video
transcript = get_transcript(VIDEO_ID)
if transcript:
    # Summarize the transcript
    summary = summarize_transcript(transcript)
    print(summary)
else:
    print('Transcript not found for the video.')
