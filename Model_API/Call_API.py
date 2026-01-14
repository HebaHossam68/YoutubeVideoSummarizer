from Utils.Get_Transcription import get_transcription, extract_video_id
import requests

API_Key="YOUR_API_KEY_HERE"
NGROK_URL = "YOUR_NGROK_URL_HERE"

def summarize_youtube_video(video_url):
    # 1. get transcript
    text = get_transcription(video_url)

    # 2. prepare request
    headers = {
        "Authorization": f"Bearer {API_Key}"
    }

    payload = {
        "text": text,
        "max_length": 150,
        "min_length": 50
    }

    # 3. call API
    response = requests.post(
        f"{NGROK_URL}/summarize",
        headers=headers,
        json=payload,
        timeout=120
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["summary"]
