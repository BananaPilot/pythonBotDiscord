from queue_bot import Queue_bot
from discord_audio_player import DiscordAudioPlayer
from queue_element import QueueElementType, QueueElement

# import json


if __name__ == "__main__":
    queue_manager = Queue_bot()

    info = DiscordAudioPlayer().extract_info(
        "https://www.youtube.com/watch?v=eUCm4wKarpQ"
    )
    queue_manager.appendToQueue(info)

    # with open("info.json", "w") as f:
    # 	json.dump(info, f, indent=4)

    print(queue_manager)

pass
