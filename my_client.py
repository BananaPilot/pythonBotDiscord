# import discord
# from events import handle_event

# class MyClient(discord.Client):
# 	async def on_ready(self):
# 		print(f"Logged as {self.user}.")

# 	async def on_command()




# @client.event
# async def on_message(message):
#     if message.content.startswith('$greet'):
#         channel = message.channel
#         await channel.send('Say hello!')

#         def check(m):
#             return m.content == 'hello' and m.channel == channel

#         msg = await client.wait_for('message', check=check)
#         await channel.send(f'Hello {msg.author}!')




# import discord
# from discord.ext import commands

# bot = commands.Bot(command_prefix="!", case_insensitive=True)

# @bot.command(name='hello', description="Greet the user!")
# async def hello(ctx):
#     await ctx.send(f"Hello {ctx.author.name}!") # f-string

# bot.run('token')



# badwords = ['bad', 'words', 'here']

# @bot.event
# async def on_message(message):
#    for i in badwords: # Go through the list of bad words;
#       if i in message:
#          await message.delete()
#          await message.channel.send(f"{message.author.mention} Don't use that word here!")
#          return # So that it doesn't try to delete the message again.
#    await bot.process_commands(message)