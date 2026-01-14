from Model_API.Call_API import summarize_youtube_video
url = "https://www.youtube.com/watch?v=wiNXzydta4c&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=2"
summary = summarize_youtube_video(url)
print(summary)
