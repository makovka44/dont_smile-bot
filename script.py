import discord
import asyncio
import aiohttp
import random

from datetime import datetime
from discord.ext import commands

datetime.today()
import os

intents = discord.Intents().all()
intents.members= True

client = discord.Client(intents=intents)


from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("moj_token")

USER_ID = os.getenv("USER_ID")
JURIJ = os.getenv("JURIJ")
MAJ = os.getenv("MAJ")
JERNEJ = os.getenv("JERNEJ")
MATIJA = os.getenv("MATIJA")
LIN = os.getenv("LIN")
VAL = os.getenv("VAL")
JAKA = os.getenv("JAKA")
URBAN = os.getenv("URBAN")

async def send_channel(channel, message):
    channel = client.get_channel(channel)
    await channel.send(message)

async def my_background_task():
    global stop
    await client.wait_until_ready()
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
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Slova je zakon!"))
    await asyncio.sleep(1)
    print("status urejen")

@client.event
async def send_channel(channel, message):
    channel = client.get_channel(channel)
    print(channel, message)
    await channel.send(message)

async def send_meme(channel, message):
    description = (f"<@{message.author.id}>")
    embed = discord.Embed(title="Meme", description=description)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/terriblefacebookmemes/hot.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            print(channel)
            await channel.send(embed=embed)

async def bot_sleep(time,message):
    await asyncio.sleep(1)
    async with message.channel.typing():
            await asyncio.sleep(time)

async def send_8ball(channel):
    seznam_odzivov = ["Eroor 404", "It is certain.", "It is decidely so.", "Without a doubt.", "Yes, definetly.", "You may rely on it", "A I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Sign point yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtfull."]
    message = random.choice(seznam_odzivov)
    print("message izbran")
    await send_channel(channel, message)

@client.event
async def on_message(message):
    print(message)
    lin=message.channel
    global stop, USER_ID
    channel = message.channel.id
    print(channel)
    print(message.content)
    if message.author == client.user:
        return
    # Respond with a custom message if a specific phrase is mentioned in the message
    if 'maj.' in message.content.lower():
        await message.channel.send(f'Govorim o {message.author.mention}!')
        bot_sleep(3, message)
        print("omenil sem maja")
    elif "/meme-me" in message.content.lower():
        await bot_sleep(3,message)
        await send_meme(message.channel, message)

    elif "/ask-me" in message.content.lower():
        await bot_sleep(3, message)
        seznam_odzivov = ["Eroor 404", "It is certain.", "It is decidely so.", "Without a doubt.", "Yes, definetly.", "You may rely on it", "A I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Sign point yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtfull."]
        message = random.choice(seznam_odzivov)
        print("message izbran")
        await send_channel(channel, message)    
    elif "/spam" in message.content.lower():
            bot_sleep(3, message)
            message=" "
            uporabnik=str(message.content.split(" ")[2])
            stevilo=str(message.content.split(" ")[3])
            for i in range(0, stevilo): 
                sporočilce=message + (f"<@{uporabnik}>") + "\n"

    elif "/pojdi k jakatu" in message.content.lower():
        bot_sleep(3, message)
        await send_dm("**Adijos amigos!**")
        USER_ID = JAKA
        await send_dm("Hello my friend. I'm here to meme you. Use /meme-me to get memes.")
    elif "/pojdi k maju" in message.content.lower():
        await send_dm("**Adijos amigos!**")
        USER_ID = MAJ
        await send_dm("Hello my friend. I'm here to meme you. Use /meme-me to get memes.")
    elif "/pojdi k urbanu" in message.content.lower():
        await send_dm("**Adijos amigos!**")
        USER_ID = URBAN
    elif "/čas" in message.content.lower():  
        bot_sleep(3, message)
        await send_dm(f"Čas je {datetime.today()}")
        print(datetime.today())
    elif "/spam me" in message.content.lower():
        bot_sleep(3, message)
        USER_ID = message.author.id
        await send_spam(USER_ID)
        print("sent spam")
    elif "/spamaj" in message.content.lower():
        bot_sleep(3, message)
        print("spamanje")

client.run(TOKEN)
