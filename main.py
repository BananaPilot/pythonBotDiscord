import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
from music_cog import music_Cog
from discord_audio_player import DiscordAudioPlayer
from queue_bot import Queue_bot

has_variables = load_dotenv()

if not has_variables:
    print("You must define a .env file")
    exit(-1)

intents: Intents = Intents.all()
discord_bot = commands.Bot(command_prefix="!", intents=intents)


@discord_bot.check
def my_check(ctx: commands.Context):
    print(ctx.command.name)
    print(ctx.command.cog_name)

    return True


@discord_bot.event
async def on_ready() -> None:
    ffmpeg_path = os.getenv("FFMPEG_PATH")
    queue = Queue_bot()
    audio_player = DiscordAudioPlayer(ffmpeg_path)
    bot_cog = music_Cog(discord_bot, audio_player, queue)

    await discord_bot.add_cog(bot_cog)

    print(f"Logged in as {discord_bot.user}")


def main() -> None:
    discord_bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()

pass
