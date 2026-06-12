import subprocess

def split_video(video_file):
    subprocess.run([
        "ffmpeg",
        "-i", video_file,
        "-f", "segment",
        "-segment_time", "60",
        "-c", "copy",
        "clips/clip_%03d.mp4"
    ])
