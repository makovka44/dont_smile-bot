import asyncio
import discord
import aiohttp
import random
import io, os


token= "MTA5NjgwNjUzMTA5MTE1Mjk3OQ.G9BOhN.flyDI2AE-fu_-v-X5-fFZTz-VtlkchOlEStVHc"
intents = discord.Intents().all()
intents.members= True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="/help-me and Slova je zakon!"))
    await asyncio.sleep(1)
async def bot_sleep(time,message):
    async with message.channel.typing():
            await asyncio.sleep(time)

@client.event
async def on_message(message):
    channel=message.channel
    if message.content == "memer":
        #Naredi neko spotročilo, ki ga potem pošlje

        for i in range(1, 100):
            stvar_za_prilepit="/meme-me"
            await channel.send(stvar_za_prilepit)
            await bot_sleep(2, message)

client.run(token)