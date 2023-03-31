import discord
import asyncio
import datetime
import os
import dotenv

from dotenv import load_dotenv
load_dotenv()

stop = 1

# Replace YOUR_TOKEN with your own Discord bot token
TOKEN = os.getenv("moj_token")

# Replace YOUR_USER_ID with your own Discord user ID
USER_ID = os.getenv("USER_ID")
JURIJ = os.getenv("JURIJ")
MAJ = os.getenv("MAJ")
JERNEJ = os.getenv("JERNEJ")
MATIJA = os.getenv("MATIJA")
LIN = os.getenv("LIN")

client = discord.Client(intents=discord.Intents.default())


async def my_background_task():
    global stop
    await client.wait_until_ready()

    while not client.is_closed():
        if stop == 0:
            await send_dm("Hello!!!!")
            await asyncio.sleep(1)


async def send_dm(message):
    user = await client.fetch_user(USER_ID)
    await user.send(message)


async def send_spam(user):
    message=""
    #Naredi neko spotročilo, ki ga potem pošlje

    for i in range(1, 10):
        stvar_za_prilepit=f"<@{user}\n>"
        message+=stvar_za_prilepit
    print(message)
    user = await client.fetch_user(user)
    await user.send(message)
   


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(my_background_task())
    # Send a DM right away when the bot is ready
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Slova je zakon!"))
    await asyncio.sleep(5)


@client.event
async def on_message(message):
    global stop, USER_ID
    print(message.content)
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Respond with a custom message if a specific phrase is mentioned in the message
    if 'maj' in message.content.lower():
        await message.channel.send(f'Govorim o {message.author.mention}!')

    elif 'stop' in message.content.lower():
        stop = 1
        await message.channel.send(f'končal sem!')

    elif 'nadaljuj' in message.content.lower():
        await message.channel.send(f'začenjam')
        stop = 0

    elif "pojdi k juriju" in message.content.lower():
        await send_dm("**Adijos!**")
        USER_ID = JURIJ
    elif "pojdi k jerneju" in message.content.lower():
        await send_dm("**Adijos!**")
        USER_ID = JERNEJ
    elif "pojdi k matiju" in message.content.lower():
        await send_dm("**Adijos!**")
        USER_ID = MATIJA
    elif "pridi nazaj" in message.content.lower():
        await send_dm("**Hello!**")
        USER_ID = MAJ
    elif "pojdi k linu" in message.content.lower():
        await send_dm("**Adijos!**")
        USER_ID = LIN
    elif "cas" in message.content.lower():
        await send_dm(datetime.datetime.now())
        print(datetime.datetime.now())
client.run(TOKEN)
