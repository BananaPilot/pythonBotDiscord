from typing import Any
import discord

class MyClient(discord.Client):
	async def on_ready(self):
		print(f"Logged as {self.user}.")

	async def on_message(self, message):
		print(f"Message from {message.author}: {message.content}")