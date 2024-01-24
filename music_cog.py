from attr import dataclass
from discord.ext import commands
from discord import app_commands
import discord
from discord_audio_player import DiscordAudioPlayer
from queue_bot import Queue_bot
from queue_element import QueueElementType, QueueElement
from enum import Enum
import asyncio


# class JoinState(Enum):
#     PENDING = 0  # Has never entered
#     FIRST = 1  # First entrance
#     SUBSEQUENT = 2 # Second or later entrance


class BotState(Enum):
    FREE = 0  # Can process commands
    WORKING = 1  # Elaborating...


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

    async def play_audio(
        self, ctx: commands.Context, element: QueueElementType
    ) -> None:
        async def callback(e: Exception = None):
            if e is not None:
                print(e)
            await self.skip(ctx)

        self.audio_player.play(
            element,
            self.connected_voice_client,
            # Don't ask about this one, for the love of god
            lambda e: asyncio.run_coroutine_threadsafe(
                callback(e), self.discord_bot.loop
            ),
        )

    async def post_update(
        self, ctx: commands.Context, forced_join: bool = False, show_queue: bool = False
    ) -> None:
        playing_element = None

        if forced_join:
            playing_element = self.queue.shiftQueue()

        if playing_element is None:
            await ctx.send("Queue is empty")
        elif not self.connected_voice_client.is_playing():
            await self.play_audio(ctx, playing_element)
            await ctx.send(f"Now playing {playing_element['webpage_url']}")

        self.bot_state = BotState.FREE

    # @commands.Cog.listener()
    # async def on_leave???
    # @commands.Cog.listener()
    # async def on_voice_state_update(self, ctx: commands.Context):
    #     print("on_voice_state_update")
    #     pass
    # @commands.Cog.listener()
    # async def on_done(self):
    #     print("on_done called")
    #     pass

    @commands.command(name="join")
    async def join(self, ctx: commands.Context) -> None:
        """Joins your voice channel"""
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
            return
        self.voice_channel = ctx.author.voice.channel
        self.connected_voice_client = await self.voice_channel.connect()

    @commands.command(name="leave")
    async def leave(self, ctx: commands.Context) -> None:
        """Leaves the voice channel"""
        await ctx.voice_client.disconnect()
        self.connected_voice_client = None

    @commands.command(name="add")
    async def add_to_queue(self, ctx: commands.Context, url: str) -> None:
        """Adds a song to the queue"""
        info = self.audio_player.extract_info(url)
        self.queue.appendToQueue(info)
        await ctx.send(f"Added {url} to the queue")

    @commands.command(name="queue")
    async def list_queue(self, ctx: commands.Context) -> None:
        if len(self.queue.the_queue):
            str_list = str(self.queue)
            await ctx.send(str_list)
        else:
            ctx.send("Queue is empty")
        pass

    @commands.command(name="play")
    async def play(self, ctx: commands.Context, url: str = None) -> None:
        """Plays a song from the queue"""
        track_info = self.audio_player.extract_info(url)
        element = QueueElement.create(track_info)

        forced_join = False

        if (
            self.connected_voice_client is None
            or ctx.voice_client is None
            or not ctx.voice_client.is_connected()
        ):
            await ctx.send("I am not connected to a voice channel. Joining...")
            await self.join(ctx)
            forced_join = True

        self.queue.appendToQueue(element)

        await self.post_update(ctx, forced_join)

    @commands.command(name="clear")
    async def clear(self, ctx: commands.Context) -> None:
        """Clears the queue"""
        self.queue.the_queue.clear()
        await ctx.send("Cleard queue")
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

    @commands.command(name="pause")
    async def pause(self, ctx: commands.Context) -> None:
        self.connected_voice_client.pause()
        ctx.send("The song has been paused")

    @commands.command(name="resume")
    async def resume(self, ctx: commands.Context) -> None:
        self.connected_voice_client.resume()
        ctx.send("The song has resumed")

    @commands.command(name="skip")
    async def skip(self, ctx: commands.Context) -> None:
        await ctx.send("Skipping...")

        if len(self.queue.the_queue) == 0:
            self.leave(ctx)

        if self.connected_voice_client.is_playing():
            self.connected_voice_client.stop()

        await self.post_update(ctx, forced_join=True)

    pass
