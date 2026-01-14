from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url: str) -> str:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    video_ids = qs.get('v')
    if not video_ids:
        raise ValueError("No video id found")
    return video_ids[0]

def get_transcription(video_url):
    video_id = extract_video_id(video_url)

    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=["en"])

    return " ".join([snippet.text for snippet in fetched])
