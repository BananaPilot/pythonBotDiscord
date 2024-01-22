from bot_init import bot

# https://stackoverflow.com/a/64321470/16804863
@bot.event
async def on_ready():
	print("hello")

@bot.event
async def on_message(message):
	if(message.content.startswith("!")):
		await message.channel.send("Hello")