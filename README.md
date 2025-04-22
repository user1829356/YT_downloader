# YouTube Video Downloader (yt-dlp)

This Python script allows you to easily download high-quality YouTube videos using the `yt-dlp` library.

## Features

- Downloads the **best available video and audio**, then merges them into an `.mp4` file
- Outputs with the **original YouTube video title**
- **Avoids full playlist downloads** to prevent accidental bulk downloads
- **Easy to customize** with your own list of YouTube URLs

## Requirements

- Python 3.6+
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

## Installation

First, install `yt-dlp`:

```bash
pip install yt-dlp
```

Usage

Clone this repository or copy the script to your local machine.
Open the script and paste your desired YouTube video links into the video_urls list.
Run the script:

```bash
python download_youtube_videos.py
```

Notes

If you uncomment more links in the video_urls list, all will be downloaded one by one.
