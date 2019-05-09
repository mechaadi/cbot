import discord
import numpy as np
import random
from itertools import cycle
import asyncio
from discord.utils import find
from discord.ext import commands

status_msgs = ["Writing future", "Bugs radar on", "Roaming the internet", "Life is awesome", "Enjoying summers"] #status messages

bot = commands.Bot("command_prefix='>'")

class MyClient(discord.Client):
    async def on_member_join(self, guild):
        channel = self.get_channel(576063824596041760)

        print("joined")
        await channel.send("Welcome to the server"+" "+"<@"+str(guild.id)+">" +" !. Enjoy the party.")

    async def on_ready(self):


        # channel = self.get_channel("general")

        # channel.send("I am live")

        messages = cycle(status_msgs)
        while self.is_closed:
            #print("here")
            current_status = next(messages)
            await self.change_presence(activity=discord.Game(name=current_status))
            await asyncio.sleep(4)
        else:
            print("there")

        # while not client.is_closed:
        #     current_status = next(messages)
        #     await client.change_presense(game=discord.Game(name=current_status))
        #     await asyncio.sleep(4)
        print('Logged on as', self.user)

    
    async def on_message(self, message):
        # don't respond to ourselves
        greetings = ["hi", "hello", "hey", "howdy", "yo"]
        greetingsReply = ["hi", "hello", "hey", "howdy", "yo", "hola", "what's up?"]

        if message.content.startswith(''):
            print(message.author)
            print(message.content)
            if message.author == self.user:
                return
            else:
                
                if message.content in greetings:
                    await message.channel.send(random.choice(greetingsReply)+","+" "+"<@"+str(message.author.id)+">")


            

client = MyClient()
client.run('NTU2NDM2NDUzNjc3MjAzNDU3.D27D2w.qSgW5xS9cHtObSGhzsGbn1txWCE')

# import discord
# from discord.ext import commands

# bot = commands.Bot(command_prefix='>')

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# bot.run('NTU2NDM2NDUzNjc3MjAzNDU3.XNREAA._JfPnTimbKxk_-SnBqBip55BgEE')