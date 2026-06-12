from yt_dlp import YoutubeDL


def download_video(url):
    ydl_opts = {
        "format": "mp4",
        "outtmpl": "video.%(ext)s",
        "noplaylist": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "video.mp4"
