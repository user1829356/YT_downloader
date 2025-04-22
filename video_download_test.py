import yt_dlp

# Paste your 6 YouTube links here
video_urls = [
    "https://www.youtube.com/watch?v=GhskWGhO83Y",
   # "https://www.youtube.com/watch?v=oe3Jn6FRoII",
   # "https://www.youtube.com/watch?v=VloXc0Tyi4R4",
   # "https://www.youtube.com/watch?v=5u9u8yzPEpA",
   # "https://www.youtube.com/watch?v=IuoscQiQQLg",
   # "https://www.youtube.com/watch?v=-B96nN9N6rs"
]

# yt-dlp options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Downloads best video & audio separately, then merges
    'merge_output_format': 'mp4',          # Final output format
    'outtmpl': '%(title)s.%(ext)s',        # Output file name pattern
    'noplaylist': True,                    # Don't download full playlists accidentally
    'quiet': False                         # Show progress (set to True to suppress)
}

def download_videos(urls):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                print(f"Downloading: {url}")
                ydl.download([url])
            except Exception as e:
                print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    download_videos(video_urls)
