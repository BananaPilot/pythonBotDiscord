from attr import dataclass
from discord.ext import commands
from discord import app_commands
import discord
from discord_audio_player import DiscordAudioPlayer
from queue_bot import Queue_bot
from queue_element import QueueElementType, QueueElement
from enum import Enum


# class JoinState(Enum):
#     PENDING = 0  # Has never entered
#     FIRST = 1  # First entrance
#     SUBSEQUENT = 2 # Second or later entrance

class BotState(Enum):
    FREE = 0 # Can process commands
    WORKING = 1 # Elaborating...


@dataclass
@app_commands.guild_only()
class music_Cog(commands.Cog):
    discord_bot: commands.Bot
    audio_player: DiscordAudioPlayer
    queue: Queue_bot

    bot_state: BotState = BotState.FREE

    # isPlaying: bool = False
    # isPaused: bool = False

    voice_channel: discord.VoiceChannel = None

    connected_voice_client: discord.VoiceClient = None

    async def play_audio(self, element: QueueElementType) -> None:
        self.audio_player.play(element, self.connected_voice_client)
        pass

    def post_update(self, forced_join: bool = False):
        if forced_join:
            forced_join = False
            self.play_audio(self.queue.first())
        
        self.bot_state = BotState.FREE

    # @commands.Cog.listener()
    # async def on_leave???

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

    @commands.command(name="queue")
    async def add_to_queue(self, ctx: commands.Context, url: str) -> None:
        """Adds a song to the queue"""
        info = self.audio_player.extract_info(url)
        self.queue.appendToQueue(info)
        await ctx.send(f"Added {url} to the queue")

    @commands.command(name="list")
    async def list_queue(self, ctx: commands.Context) -> None:
        str_list = str(self.queue)
        await ctx.send(str_list)
        pass

    @commands.command()
    async def play(self, ctx: commands.Context, url: str) -> None:
        """Plays a song from the queue"""

        track_info = self.audio_player.extract_info(url)
        element = QueueElement.create(track_info)
        self.queue.appendToQueue(element)
        # TODO
        pass

    @commands.command(name="clear")
    async def clear(self, ctx: commands.Context) -> None:
        """Clears the queue"""
        self.queue.the_queue.clear()
        ctx.send("Cleard queue")
        pass

    # @commands.command()
    # async def play(self, ctx: commands.Context, url: str) -> None:
    #     """Plays a song from youtube"""

    #     if (
    #         self.connected_voice_client is None
    #         or ctx.voice_client is None
    #         or not ctx.voice_client.is_connected()
    #     ):
    #         await ctx.send("I am not connected to a voice channel. Joining...")
    #         await self.join()

    #     if not ctx.author.voice.channel == ctx.voice_client.channel:
    #         await ctx.send("You are not in my voice channel!")
    #         return

    #     if not ctx.voice_client.is_playing():
    #         self.play_audio()
    #         await ctx.send(f"Now playing {url}")

    @commands.command()
    async def pause(self, ctx: commands.Context) -> None:
        self.connected_voice_client.stop()
        ctx.send("The song has been paused")

    @commands.command
    async def resume(self, ctx: commands.Context) -> None:
        self.connected_voice_client.resume()
        ctx.send("The song has resumed")

    @commands.command
    async def skip(self, ctx: commands.Context) -> None:
        pass

    pass
