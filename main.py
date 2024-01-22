from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

# Event list (API reference): https://discordpy.readthedocs.io/en/stable/api.html
# discord.ext.commands: https://discordpy.readthedocs.io/en/stable/ext/commands/index.html

prefix="!"
# https://discordpy.readthedocs.io/en/latest/intents.html
intents = discord.Intents.all()
case_insentitive = True

bot = commands.Bot(command_prefix=prefix, case_insensitive=case_insentitive, intents=intents)

# https://stackoverflow.com/a/64321470/16804863
@bot.event
async def on_ready():
	print("hello")

@bot.event
async def on_message(message):
	if(message.content.startswith("!")):
		await message.channel.send("Hello")
	

# Decorators
# `commands` or `bot` are indifferent
# @commands.command(name='hello', description="Greet the user!")
@bot.command(name='hello', description="Greet the user!")
# @commands.has_permissions(kick_members=True)
async def hello(ctx, args):
	await ctx.send(f"Hello {ctx.author.name}!")

bot.run(os.environ.get("DISCORD_TOKEN"))
