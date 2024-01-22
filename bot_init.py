import discord
from discord.ext import commands

# Event list (API reference): https://discordpy.readthedocs.io/en/stable/api.html
# discord.ext.commands: https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
# https://discordpy.readthedocs.io/en/latest/intents.html

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents.all())