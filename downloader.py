from yt_dlp import YoutubeDL

def download_video(url):
    ydl_opts = {
        "outtmpl": "video.%(ext)s"
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "video.mp4"
