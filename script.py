import discord
import asyncio
import aiohttp
import random

from datetime import datetime
from discord.ext import commands

datetime.today()
import os

intents = discord.Intents(members=True)
client = commands.Bot(command_prefix="!", intents=intents)

from dotenv import load_dotenv
load_dotenv()

stop = 0

# Replace YOUR_TOKEN with your own Discord bot token
TOKEN = os.getenv("moj_token")

channel_id = 0
sender_id = 0

IMAGE_BETA = os.getenv("beta_server")
IMAGE_BETA_CHANNEL = os.getenv("beta_channel")

# Replace YOUR_USER_ID with your own Discord user ID
USER_ID = os.getenv("USER_ID")
JURIJ = os.getenv("JURIJ")
MAJ = os.getenv("MAJ")
JERNEJ = os.getenv("JERNEJ")
MATIJA = os.getenv("MATIJA")
LIN = os.getenv("LIN")
VAL = os.getenv("VAL")

SERVER = os.getenv("g1a")
CHANNEL = os.getenv("spam")

client = discord.Client(intents=discord.Intents.default())

async def send_message(server, channel):
    server = client.get_guild(server)
    channel = server.get_channel(channel)
    message = 'This is a message from your Python bot! '
    # Get the user object for the specified user ID
    user = await client.fetch_user(USER_ID)
    # Mention the user in the message
    message += user.mention
    await channel.send(message)
async def send_channel(channel, message):
    channel = client.get_channel(channel)
    await channel.send(message)


async def my_background_task():
    global stop
    await client.wait_until_ready()

    if stop == 0:
        await send_dm("Hello!!!!")
        await asyncio.sleep(1)


async def send_dm(message):
    user = await client.fetch_user(USER_ID)
    await user.send(message)

async def get_sender_id(message):
    sender_id = message.author.id
    print(sender_id)
    return sender_id

async def send_spam(user):
    print("trying to spam")
    message=""
    #Naredi neko spotročilo, ki ga potem pošlje

    for i in range(1, 10):
        stvar_za_prilepit=f"<@{USER_ID}>"
        message+=stvar_za_prilepit + "\n"
    print(message)
    user = await client.fetch_user(user)
    await user.send(message)
    print("sent spam")
   
async def get_channel_id(message):
    channel_id = message.channel.id
    print(channel_id)
    return channel_id


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(my_background_task())
    # Send a DM right away when the bot is ready
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Slova je zakon!"))
    await asyncio.sleep(1)
    print("status urejen")

@client.event
async def send_channel(channel, message):
    channel = client.get_channel(channel)
    channel.send(message)

async def send_meme(channel):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await channel.send(embed=embed)

@client.event
async def on_message(message):
    global stop, USER_ID
    channel = client.get_channel(message.channel.id)
    print(message.content)
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    # Respond with a custom message if a specific phrase is mentioned in the message
    if 'maj' in message.content.lower():
        await message.channel.send(f'Govorim o {message.author.mention}!')
        print("omenil sem maja")
    elif "/meme-me" in message.content.lower():
        await send_meme(channel)

    elif '/nadaljuj' in message.content.lower():
        await message.channel.send(f'začenjam')
        print("začenjam")
        stop = 0

    elif "/čas" in message.content.lower():  
        await send_dm(f"Čas je {datetime.today()}")
        print(datetime.today())
    elif "/spam me" in message.content.lower():
        await send_spam(USER_ID)
        print("sent spam")
    elif "/spamaj" in message.content.lower():
        print("spamanje")



client.run(TOKEN)
