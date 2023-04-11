import discord

from discord.ext import commands
import os
from dotenv import load_dotenv()
import random
import aiohttp

load_dotenv()
TOKEN = os.getenv("moj_token")

intents = discord.Intents.default()
intents.members = True

import discord
import random
from discord_slash import SlashCommand

client = commands.Bot(command_prefix='!')
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        channel = message.channel
    elif isinstance(message.channel, discord.TextChannel):
        if not message.guild:
            return
        channel = message.channel
    else:
        return

    if message.content.lower() == '/meme':
        embed = discord.Embed()
        async with channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                    await channel.send(embed=embed)

@slash.slash(name='meme', description='Get a random meme')
async def slash_meme(ctx):
    embed = discord.Embed()
    async with ctx.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

client.run(TOKEN)

