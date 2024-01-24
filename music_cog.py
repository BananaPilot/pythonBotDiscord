from attr import dataclass
from discord.ext import commands
from discord import app_commands
import discord
from discord_audio_player import DiscordAudioPlayer
from queue_bot import Queue_bot
from queue_element import QueueElementType, QueueElement
from enum import Enum
import asyncio


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

    vc: discord.VoiceChannel = None
    """The voice channel."""

    vc_client_connection: discord.VoiceClient = None
    """The voice channel's client connection."""

    def should_execute(self) -> bool:
        if self.bot_state == BotState.FREE:
            self.bot_state = BotState.WORKING
            return True
        else:
            # await ctx.send("I'm busy, wait a sec")
            return False

    async def cog_check(self, ctx: commands.Context):
        print("CHECKINGGGG cog")
        return self.should_execute()

    async def play_audio(
        self, ctx: commands.Context, element: QueueElementType
    ) -> None:
        async def callback(e: Exception = None):
            if e is not None:
                print(e)
            if self.queue.isQueueEmpty():
                # Start a 5 seconds countdown
                asyncio.create_task(self.afk_countdown(ctx, seconds=5))
                return
            await self.post_update(ctx, shift_queue=True)

        self.audio_player.play(
            element,
            self.vc_client_connection,
            # Don't ask about this one, for the love of god
            lambda e: asyncio.run_coroutine_threadsafe(
                callback(e), self.discord_bot.loop
            ),
        )

    @commands.command(name="join")
    async def join(self, ctx: commands.Context, was_forced: bool = False) -> None:
        """Joins your voice channel"""

        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
            return

        await ctx.send(
            f"{'' if not was_forced else f'{ctx.author.mention} summoned me! '}Joining..."
        )

        self.vc = ctx.author.voice.channel
        self.vc_client_connection = await self.vc.connect()

    # region Leave

    async def leave_client(self, ctx: commands.Context, was_timeout: bool = False):
        await ctx.send("zzz..." if was_timeout else "Leaving...")

        await ctx.voice_client.disconnect()
        self.vc_client_connection = None

    async def on_afk_countdown_end(self, ctx: commands.Context):
        await self.leave_client(ctx, was_timeout=True)
        print("AFK countdown ended!")

    async def afk_countdown(self, ctx: commands.Context, seconds: float):
        await asyncio.sleep(seconds)
        await self.on_afk_countdown_end(ctx)
        await self.post_update(ctx, has_left=True)

    @commands.command(name="leave")
    async def leave(self, ctx: commands.Context, was_timeout: bool = False) -> None:
        """Leaves the voice channel"""

        await self.leave_client(ctx, was_timeout)

        await self.post_update(ctx, has_left=True)

    # endregion

    @commands.command(name="add")
    async def add_to_queue(self, ctx: commands.Context, url: str) -> None:
        """Adds a song to the queue"""

        info = self.audio_player.extract_info(url)
        self.queue.appendToQueue(info)
        await ctx.send(f"Added {url} to the queue")

        await self.post_update(ctx)

    @commands.command(name="queue", aliases=["list", "q", "l"])
    async def list_queue(self, ctx: commands.Context) -> None:
        """Lists the queue"""

        await self.post_update(ctx, print_queue=True)

    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx: commands.Context, url: str = None) -> None:
        """Plays a song from the queue"""

        forced_join = False

        if (
            self.vc_client_connection is None
            or ctx.voice_client is None
            or not ctx.voice_client.is_connected()
        ):
            forced_join = True
            await self.join(ctx, forced_join)

        if url is None:
            await ctx.send("No link provided")
        else:
            track_info = self.audio_player.extract_info(url)
            element = QueueElement.create(track_info)
            self.queue.appendToQueue(element)

        await self.post_update(ctx, shift_queue=forced_join)

    @commands.command(name="clear")
    async def clear(self, ctx: commands.Context) -> None:
        """Clears the queue"""

        self.queue.the_queue.clear()
        await ctx.send("Cleard queue")
        await self.post_update(ctx)

    @commands.command(name="pause")
    async def pause(self, ctx: commands.Context) -> None:
        self.vc_client_connection.pause()
        ctx.send("The song has been paused")
        await self.post_update(ctx)

    @commands.command(name="resume")
    async def resume(self, ctx: commands.Context) -> None:
        self.vc_client_connection.resume()
        ctx.send("The song has resumed")
        await self.post_update(ctx)

    @commands.command(name="skip")
    async def skip(self, ctx: commands.Context) -> None:
        if not self.queue.isQueueEmpty():
            await ctx.send("Skipping...")

            if self.vc_client_connection.is_playing():
                self.vc_client_connection.stop()

            await self.post_update(ctx)

    async def post_update(
        self,
        ctx: commands.Context,
        shift_queue: bool = False,
        print_queue: bool = False,
        has_left: bool = False,
    ) -> None:
        if has_left:
            self.bot_state = BotState.FREE
            return

        playing_element = self.queue.get_current()

        if print_queue:
            if self.queue.length() > 0:
                str_list = str(self.queue)
                embed_msg = discord.Embed(
                    title=":scroll: Queue", description=str_list, color=ctx.author.color
                )
                await ctx.send(embed=embed_msg)

        if shift_queue:
            playing_element = self.queue.shiftQueue()

        if self.queue.isEmpty():
            await ctx.send("Queue is empty")

        if playing_element is not None and not self.vc_client_connection.is_playing():
            await self.play_audio(ctx, playing_element)
            await ctx.send(f"Now playing {playing_element['webpage_url']}")

        self.bot_state = BotState.FREE

    pass
