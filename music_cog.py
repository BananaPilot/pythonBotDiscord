from typing import Any
from attr import dataclass
from discord.ext import commands
from discord import app_commands
import discord
from discord_audio_player import DiscordAudioPlayer


@dataclass
@app_commands.guild_only()
class music_Cog(commands.Cog):
    bot: commands.Bot
    audio_player: DiscordAudioPlayer

    isPlaying: bool = False
    isPaused: bool = False

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

    def addToQueue(self, element: str):
        queue = self.queue
        queue.append()

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
            await ctx.send("I am not connected to a voice channel. Joining...")
            await self.join()

        if not ctx.author.voice.channel == ctx.voice_client.channel:
            await ctx.send("You are not in my voice channel!")
            return
        if not ctx.voice_client.is_playing():
            info = self.audio_player.get_info(url)

            self.audio_player.play(info, voice)

            import json

            with open("info.json", "w") as f:
                json.dump(info, f)

            await ctx.send(f"Now playing {info['url']}")

    @commands.command()
    async def pause(self, ctx: commands.Context):
        self.connected_voice_client.stop()
        ctx.send("The song has been paused")

    @commands.command
    async def resume(self, ctx: commands.Context):
        self.connected_voice_client.resume()
        ctx.send("The song has resumed")

    @commands.command
    async def skip(self, ctx: commands.Context):
        pass

    pass
