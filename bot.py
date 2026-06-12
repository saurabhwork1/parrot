import os
import shutil

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN
from downloader import download_video
from clipper import split_video


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "YouTube link bhejo. Main video ko clips me split kar dunga."
    )


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = update.message.text

    await update.message.reply_text(
        "Video download ho rahi hai..."
    )

    try:

        video_file = download_video(url)

        await update.message.reply_text(
            "Video split ho rahi hai..."
        )

        clips = split_video(video_file)

        await update.message.reply_text(
            f"{len(clips)} clips bani hain."
        )

        for clip in clips:

            with open(clip, "rb") as video:
                await update.message.reply_video(video)

        if os.path.exists(video_file):
            os.remove(video_file)

        if os.path.exists("clips"):
            shutil.rmtree("clips")

    except Exception as e:
        await update.message.reply_text(
            f"Error: {e}"
        )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_link
        )
    )

    print("Bot Running...")

    app.run_polling()


if __name__ == "__main__":
    main()
