import os
import sys
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
from music_cog import music_Cog
from yt_dlp import YoutubeDL
import discord
import json

# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

load_dotenv()

intents: Intents = Intents.all()
bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.check
def my_check(ctx: commands.Context):
	print(ctx.command.name)
	print(ctx.command.cog_name)

	return True

@bot.event
async def on_ready() -> None:
	# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
	await bot.add_cog(music_Cog(bot, ffmpeg_path=os.getenv("FFMPEG_PATH")))
	# test_cog = bot.get_cog("music_Cog")
	# commands = test_cog.get_commands()
	# print([c.name for c in commands])

	print(f"Logged in as {bot.user}")

def main() -> None:
	bot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
	main()

	##### youtube-dl.exe -x --audio-format "mp3" %*
	
	# if len(sys.argv) < 0:
	# 	exit(2)

	# url = sys.argv[1]
	# print(f"URL argument: {url}")

	# YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True', "verbose": True, 'ignoreerrors': 'only_download', 'youtube_include_dash_manifest': False}
	
	# with YoutubeDL(YDL_OPTIONS) as ydl:
	# 	info = ydl.extract_info(url=url, download=False)

	# URL = info['url']
	# discord.FFmpegPCMAudio(URL, executable=os.getenv("FFMPEG_PATH"), **{'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'})

	# print("Roba" + URL)

	# # vado al bagno, intanto avvialo
	# with open("info.json", "x") as file:
	# 	json.dump(info, file, indent=4)
	
	# print(URL)
	# voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
	
	# URL = info['formats'][0]['url']
	# voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
	# voice.is_playing()
	# await ctx.send("Added to queue")