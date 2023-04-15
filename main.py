import discord
import asyncio
import aiohttp
import random
import io

from datetime import datetime, timedelta
from discord.utils import get
from time import sleep


datetime.today()
import os
stop = 0

intents = discord.Intents().all()
intents.members= True

client = discord.Client(intents=intents)


from dotenv import load_dotenv
load_dotenv()

TOKEN = "MTA5MDg5NjUwNzIxOTIzNDg3OA.GLTfV8.VvtRVgnJ0x_WYEXXAq2EmaFuxF7CuTtkTm-eGk"

USER_ID = "1014769833688182825"
MAJ = "1014769833688182825"
LIN = "989076547732402186"
VAL = "754303415831756822"

async def send_channel(channel, message):
    channel = client.get_channel(channel)
    await channel.send(message)

async def my_background_task():
    global stop
    await client.wait_until_ready()
    await send_dm("Online sem")
    await asyncio.sleep(1)


async def send_dm(message):
    user = await client.fetch_user(USER_ID)
    await user.send(message)

async def send_dm2(user, message):
    user = await client.fetch_user(user)
    await user.send(message)

async def send_spam(user, channel):
    print("trying to spam")
    message=""
    #Naredi neko spotročilo, ki ga potem pošlje

    for i in range(1, 10):
        stvar_za_prilepit=f"<@{USER_ID}>"
        message+=stvar_za_prilepit + "\n"
    print(message)
    user = await client.fetch_user(user)
    await channel.send(message)
   
async def get_channel_id(message):
    channel_id = message.channel.id
    return channel_id


@client.event
async def on_ready():
    await send_dm2(MAJ, 'Logged in as {0.user}'.format(client))
    client.loop.create_task(my_background_task())
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="/help-me and Slova je zakon!"))
    await asyncio.sleep(1)
    await send_dm2(MAJ, "status urejen, sem pri juriju")

async def send_meme(channel, message):
    reddit_api = ["https://www.reddit.com/r/memes/hot.json?sort=hot", "https://www.reddit.com/r/terriblefacebookmemes/new.json?sort=hot", "https://www.reddit.com/r/ProgrammerHumor/hot.json?sort=hot", "https://www.reddit.com/r/HistoryMemes/hot.json?sort=hot", "https://www.reddit.com/r/traaaaaaannnnnnnnnns/hot.json?sort=hot", "https://www.reddit.com/r/Funnymemes/hot.json?sort=hot", "https://www.reddit.com/r/MinecraftMemes/hot.json?sort=hot", "https://www.reddit.com/r/AnarchyChess/hot.json?sort=hot", "https://www.reddit.com/r/PrequelMemes/new.json?sort=hot", "https://www.reddit.com/r/dadjokes/new.json?sort=hot", "https://www.reddit.com/r/Jokes/new.json?sort=hot"]
    izbira = random.choice(reddit_api)
    if izbira =="https://www.reddit.com/r/memes/hot.json?sort=hot":
        ime_meme = "classic meme"
    elif izbira == "https://www.reddit.com/r/terriblefacebookmemes/new.json?sort=hot":
        ime_meme = "terrible facebook meme"
    elif izbira == "https://www.reddit.com/r/ProgrammerHumor/hot.json?sort=hot":
        ime_meme = "programmer meme"
    elif izbira == "https://www.reddit.com/r/HistoryMemes/hot.json?sort=hot":
        ime_meme = "history meme"
    elif izbira == "https://www.reddit.com/r/traaaaaaannnnnnnnnns/hot.json?sort=hot":
        ime_meme = "trans meme"
    elif izbira == "https://www.reddit.com/r/Funnymemes/hot.json?sort=hot":
        ime_meme = "funny meme"
    elif izbira == "https://www.reddit.com/r/MinecraftMemes/hot.json?sort=hot":
        ime_meme = "minecraft meme"
    elif izbira == "https://www.reddit.com/r/AnarchyChess/hot.json?sort=hot":
        ime_meme = "chess meme"
    elif izbira == "https://www.reddit.com/r/PrequelMemes/new.json?sort=hot":
        ime_meme = "random meme"
    elif izbira == "https://www.reddit.com/r/dadjokes/new.json?sort=hot":
        ime_meme = "dad joke"
    elif izbira == "https://www.reddit.com/r/Jokes/new.json?sort=hot":
        ime_meme = "joke"
    description = (f"<@{message.author.id}> tukaj je tvoj "+ ime_meme+ ".")
    if ("dadjokes" or "jokes") in izbira:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(izbira) as r:
                res = await r.json()
                post = random.choice(res['data']['children'])['data']
                joke = post['title'] + '\n\n' + post['selftext']
                embed = discord.Embed(title="Dad Joke", description=description, color=0xffa500)
                embed= embed.add_field(name="Meme", value=joke, inline=False)
                embed = embed.add_field(name="", value=joke, inline=False)
                await channel.send(embed=embed)
    else: 
        async with aiohttp.ClientSession() as cs:
            async with cs.get(izbira) as r:
                res = await r.json()
                children = res['data']['children']
                post = random.choice(children)['data']
                joke = "_" + post['title'] + '\n\n' + post['selftext'] + "_"
                embed = discord.Embed(title="Meme", description=description, color=0xffa500)
                embed= embed.add_field(name="", value=joke, inline=False)
                if post['is_video']:
                    video_url = post['media']['reddit_video']['fallback_url']
                    async with cs.get(video_url) as r:
                        video_bytes = await r.read()
                    video_file = discord.File(io.BytesIO(video_bytes), filename='meme.mp4')
                    while not message.attachments: # Check if attachments have been added yet
                        await asyncio.sleep(1) # Wait for 1 second
                        message = await channel.fetch_message(message.id) # Refresh message object
                    embed.add_field(name="Meme", value=joke, inline=False)
                    await channel.send(file=video_file, embed=embed)
                else:
                    embed.set_image(url=post['url'])
                    await channel.send(embed=embed)

async def bot_sleep(time,message):
    await asyncio.sleep(1)
    async with message.channel.typing():
            await asyncio.sleep(time)


@client.event
async def on_message(message):
    #print(message)
    lin=message.content
    cajt=message.channel
    global stop, USER_ID
    channel = message.channel.id
    channel = message.channel

    #num_mentions = 0  # initialize the variable to 0

    """if message.guild is not None:
        # Split the last word of the message
        žrtev = message.content.rsplit(None, 1)[-1]
        # Get member object based on username
        member = get(message.guild.members, name=žrtev)
        if member is not None:
            # Print member ID
            print(member.id)
        print(žrtev)
        num_mentions = message.content.count("@")
        print(num_mentions)

    if num_mentions == 2:
        # Timeout member for 10 seconds
        await message.channel.set_permissions(member, send_messages=False)
        await message.channel.send(f"<@{member}> has been timed out for 10 seconds, because of spamming.")
        await asyncio.sleep(10)
        print("timeout")
        await message.channel.set_permissions(member, send_messages=True)
        await message.channel.send(f"<@{žrtev}> is no longer timed out.")
    else:
        pass"""


    print(message.author.id)
    print(message.content)
    if stop == 0 :
        if message.content.lower() == "/help-me":
            embed = discord.Embed(title='Die Liste', color=0xffa500)
            embed.add_field(name='/meme-me', value='Generates a random meme', inline=False)
            embed.add_field(name='/spam-me', value='Sends multiple spam messages', inline=False)
            embed.add_field(name='/ask-me', value='Answers a random question.', inline=False)
            embed.add_field(name='/help-me', value='Shows this menu.', inline=False)
            embed.add_field(name="/spam-c", value='Spams c=> custom.', inline=False)
            await message.channel.send(embed=embed)
            await send_dm2(MAJ, "used help-me")
        if ('maj'or"maju"or"majči") in message.content.lower():
            await bot_sleep(1, message)
            avtor = str(f"{message.author}")
            avtor_send = str(avtor.split("#")[0])
            await message.channel.send(f"{avtor_send} govori o <@{MAJ}>!")
            send_dm2(MAJ, "omenil sem maja")
        elif "/meme-me" in message.content.lower():
            await bot_sleep(3,message)
            await message.delete()
            await send_dm2(MAJ, "used meme.me")
            await send_meme(message.channel, message)
        elif message.content.startswith("/ask-me: "):
            lin = str(message.content.split(":")[1])
            avtor = str(f"{message.author}")
            avtor_send = "*_By "+ str(avtor.split("#")[0])+"_*"
            await bot_sleep(3, message)
            seznam_odzivov = ["Eroor 404", "It is certain.", "It is decidely so.", "Without a doubt.", "Yes, definetly.", "You may rely on it", "A I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Sign point yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtfull."]
            message_to_send = random.choice(seznam_odzivov)
            embed = discord.Embed(title=lin, color=0xffa500)
            embed.add_field(name='Answer:', value= message_to_send, inline=False)
            embed.add_field(name="", value= avtor_send, inline=False)
            await message.channel.send(embed=embed) 
            await send_dm2(MAJ, "used as-me")  
            await message.delete()
        elif "/čas" in message.content.lower():
            await bot_sleep(3, message)
            now = datetime.now()
            mesic = now.strftime("%d.%m.%Y, %H:%M")
            embed = discord.Embed(title="Čas", description=mesic, color=0xffa500)
            await channel.send(embed=embed)
            await send_dm2(MAJ, "uporabljen čas")
            await message.delete()
        elif "/spam-me" in message.content.lower():
            await bot_sleep(3, message)
            USER_ID = message.author.id
            await send_spam(USER_ID, cajt)
            await message.delete()
            send_dm2(MAJ, "sent spam")
        elif message.content.startswith("/spam-c "):
            await message.delete()
            user = message.content.split(" ")[1]
            await bot_sleep(3, message)
            stevilka = int(message.content.split(" ")[2])
            if stevilka * len(user)>3900:
                stevilka=3900//len(user)
            message_to_send = " "
            for i in range(1, stevilka):
                stvar_za_prilepit=f"<@{user}>"
                message_to_send+=stvar_za_prilepit + "\n"
            avtor = str(f"{message.author}")
            message_to_send+= "By "+ str(avtor.split("#")[0])
            await channel.send(message_to_send)
            await send_dm2(MAJ, message_to_send)
        elif message.content.startswith("/custom"):
            if message.author.id == 1014769833688182825:  
                await bot_sleep(2, message)  
                channel_id = message.channel.id
                if "," in message.content.lower():
                    mesič1=message.content.split(", ")[1]
                    trash = message.content.split(", ")[0]
                    mesič2=trash.split(" ")[1]
                    await client.http.delete_message(channel_id, mesič1)
                    await client.http.delete_message(channel_id, mesič2)
                else :
                    message_id = message.content.split(" ")[1]
                    await client.http.delete_message(channel_id, message_id)
                await message.delete()
                await send_dm2(1014769833688182825, "deleted")
        elif "/pošlji-manual" in message.content.lower():
            await bot_sleep(3, message)
            await message.delete()
            send_dm2(MAJ, "manual")
            embed = discord.Embed(title='Die Liste', color=0xffa500)
            embed.add_field(name='/meme-me', value='Generates a random meme.', inline=False)
            embed.add_field(name='/spam-me', value='Sends multiple spam messages.', inline=False)
            embed.add_field(name='/ask-me: ', value='Answers a random question.', inline=False)
            embed.add_field(name='/help-me', value='Shows this menu.', inline=False)
            embed.add_field(name="/spam-c", value='Spams c=> custom.', inline=False)
            await message.channel.send(embed=embed)
        elif message.content.startswith("/joke "):
            print("found joke")
            await message.delete()
            stevilka = int(message.content.split(" ")[1])
            for i in range(stevilka):
                await channel.send("prazen_message")
            for i in range(stevilka):
                last_hour = datetime.utcnow() - timedelta(hours=1)
                async for msg in message.channel.history(after=last_hour, limit=None):
                    if msg.author == client.user and msg.content == "prazen_message":
                        await msg.delete()
                        print("loop deleting")
                        await asyncio.sleep(1)
                    await send_dm2(MAJ, "joke used")
client.run(TOKEN)