from typing import Any
from attr import dataclass
from yt_dlp import YoutubeDL
import discord


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

    def extract_info(self, url: str) -> dict[str, Any]:
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        return info

    def play(
        self, info: (Any | dict[str, Any] | None), voice_client: discord.VoiceClient
    ):
        url = info["url"]

        voice_client.play(
            discord.FFmpegPCMAudio(
                source=url, executable=self.FFMPEG_PATH, **self.FFMPEG_OPTIONS
            )
        )

    pass
