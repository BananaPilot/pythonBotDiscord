from queue_bot import Queue_bot
from discord_audio_player import DiscordAudioPlayer
from queue_element import QueueElementType, QueueElement


if __name__ == "__main__":
    # queue_manager = Queue_bot()

    info = DiscordAudioPlayer().extract_info(
        "https://www.youtube.com/watch?v=lTRiuFIWV54"
    )
    # queue_manager.appendToQueue(info)

    import json

    with open("info.json", "w") as f:
        json.dump(info, f, indent=4)

    # print(queue_manager)
    # yt-dlp --list-formats <url>

pass
