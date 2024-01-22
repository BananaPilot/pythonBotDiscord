from bot_init import bot

@bot.command(name='hello', description="Greet the user!")
async def hello(context, args):
	await context.send(f"Hello {context.author.name}!")