import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

# Event list (API reference): https://discordpy.readthedocs.io/en/stable/api.html
# discord.ext.commands: https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
# https://discordpy.readthedocs.io/en/latest/intents.html

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
	print(bot.user)

@bot.event
async def on_message(message):
	if(message.content.startswith("!")):
		await message.channel.send("Hello")

@bot.command(name='hello', description="Greet the user!")
async def hello(context, args):
	await context.send(f"Hello {context.author.name}!")

bot.run(os.environ.get("DISCORD_TOKEN"))