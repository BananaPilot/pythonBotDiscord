import asyncio
from typing import Any
from attr import dataclass
from discord.ext import commands
from discord import app_commands
import discord
from yt_dlp import YoutubeDL


@dataclass
@app_commands.guild_only()
class music_Cog(commands.Cog):
    bot: commands.Bot
    ffmpeg_path: str

    isPlaying: bool = False
    isPaused: bool = False

    queue: list[str] = []

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

    voice_channel: discord.VoiceChannel = None

    connected_voice_client: discord.VoiceClient = None

    @commands.command()
    async def join(self, ctx: commands.Context) -> None:
        """Joins your voice channel"""
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
            return
        self.voice_channel = ctx.author.voice.channel
        self.connected_voice_client = await self.voice_channel.connect()

    @commands.command()
    async def leave(self, ctx: commands.Context) -> None:
        """Leaves the voice channel"""
        await ctx.voice_client.disconnect()
        self.connected_voice_client = None

    @commands.command()
    async def play(self, ctx: commands.Context, url: str) -> None:
        """Plays a song from youtube"""

        voice = self.connected_voice_client

        if (
            voice is None
            or ctx.voice_client is None
            or not ctx.voice_client.is_connected()
        ):
            print_task = asyncio.create_task(
                ctx.send("I am not connected to a voice channel. Joining...")
            )
            await self.join()
            await print_task

        if not ctx.author.voice.channel == ctx.voice_client.channel:
            await ctx.send("You are not in my voice channel!")
            return
        if not ctx.voice_client.is_playing():
            with YoutubeDL(self.YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url=url, download=False)

            URL = info["url"]
            voice.play(
                discord.FFmpegPCMAudio(
                    URL, executable=self.ffmpeg_path, **self.FFMPEG_OPTIONS
                )
            )
            await ctx.send(f"Now playing {url}")
