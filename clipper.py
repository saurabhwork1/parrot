import os
import subprocess
from config import CLIP_DURATION, CLIPS_FOLDER


def split_video(video_file):
    os.makedirs(CLIPS_FOLDER, exist_ok=True)

    output_pattern = f"{CLIPS_FOLDER}/clip_%03d.mp4"

    subprocess.run([
        "ffmpeg",
        "-i",
        video_file,
        "-c",
        "copy",
        "-map",
        "0",
        "-f",
        "segment",
        "-segment_time",
        str(CLIP_DURATION),
        output_pattern
    ])

    clips = []

    for file in os.listdir(CLIPS_FOLDER):
        if file.endswith(".mp4"):
            clips.append(os.path.join(CLIPS_FOLDER, file))

    clips.sort()

    return clips
