import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
from music_cog import music_Cog

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
	await bot.add_cog(music_Cog(bot))

	# test_cog = bot.get_cog("music_Cog")
	# commands = test_cog.get_commands()
	# print([c.name for c in commands])

	print(f"Logged in as {bot.user}")

def main() -> None:
	bot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
	main()


