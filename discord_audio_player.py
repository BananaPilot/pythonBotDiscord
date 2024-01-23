from typing import Any
from attr import dataclass
from yt_dlp import YoutubeDL
import discord
from queue_element import QueueElementType
from queue_bot import TrackInfo


@dataclass
class DiscordAudioPlayer:
    FFMPEG_PATH: str = "ffmpeg"

    YDL_OPTIONS: dict[str, Any] = {
        "format": "bestaudio/best",
        "noplaylist": "True",
        "verbose": True,
        "ignoreerrors": "only_download",
        "youtube_include_dash_manifest": False,
        "noplaylist": True,
    }

    FFMPEG_OPTIONS: dict[str, Any] = {
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        "options": "-vn",
    }

    def extract_info(self, url: str) -> TrackInfo:
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        return info

    def play(self, element: QueueElementType, voice_client: discord.VoiceClient):
        url = element["url"]

        voice_client.play(
            discord.FFmpegPCMAudio(
                source=url, executable=self.FFMPEG_PATH, **self.FFMPEG_OPTIONS
            )
        )

    pass
