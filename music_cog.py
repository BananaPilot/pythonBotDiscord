from discord.ext import commands
import discord


class music_Cog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

		self.isPlaying = False
		self.isPaused = False

		self.queue = []

	@commands.command()
	async def hello(self, ctx: commands.Context, *, member: discord.Member = None) -> None:
		member = member or ctx.author
		await ctx.send(f"Hello {member.name}")

	