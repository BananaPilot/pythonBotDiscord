from bot_init import bot

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx, args):
	await ctx.send(f"Hello {ctx.author.name}!")