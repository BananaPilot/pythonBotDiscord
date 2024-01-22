async def handle_event(_self, type, *args):

	if type == "ready":
		await ready(_self, *args)

	if type == "message":
		await message(_self, *args)


	pass
	

async def ready(_self, boh):
	print("fabio di m")

	pass
	

async def message(_self, msg):
	if msg.content.startwith("$hello"):
		await msg.channel.send("Hello")
	pass