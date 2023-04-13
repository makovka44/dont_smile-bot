import discord
import asyncio
import aiohttp
import random

from datetime import datetime


datetime.today()
import os
stop = 0

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
    await asyncio.sleep(1)


async def send_dm(message):
    user = await client.fetch_user(USER_ID)
    await user.send(message)

async def send_dm2(user, message):
    user = await client.fetch_user(user)
    await user.send(message)

async def get_sender_id(message):
    sender_id = message.author.id
    print(sender_id)
    return sender_id

async def send_spam(user, channel):
    message=""
    #Naredi neko spotročilo, ki ga potem pošlje

    for i in range(1, 10):
        stvar_za_prilepit=f"<@{USER_ID}>"
        message+=stvar_za_prilepit + "\n"
    print(message)
    user = await client.fetch_user(user)
    await channel.send(message)
    await send_dm2(MAJ, "sent spam")
   
async def get_channel_id(message):
    channel_id = message.channel.id
    return channel_id


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(my_background_task())
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Slova je zakon!"))
    #await asyncio.sleep(1)
    await send_dm2(MAJ, "status urejen")
    await send_dm2(MAJ, "Hello!!!!")
    await send_dm2(MAJ, "hostan pr juriju")

@client.event
async def send_channel(channel, message):
    channel = message.get_channel(channel)
    await channel.send(message)

async def send_meme(channel, message):
    reddit_api = ["https://www.reddit.com/r/memes/hot.json?sort=hot", "https://www.reddit.com/r/terriblefacebookmemes/new.json?sort=hot", "https://www.reddit.com/r/ProgrammerHumor/hot.json?sort=hot", "https://www.reddit.com/r/HistoryMemes/hot.json?sort=hot", "https://www.reddit.com/r/traaaaaaannnnnnnnnns/hot.json?sort=hot", "https://www.reddit.com/r/Funnymemes/hot.json?sort=hot", "https://www.reddit.com/r/MinecraftMemes/hot.json?sort=hot", "https://www.reddit.com/r/AnarchyChess/hot.json?sort=hot", "https://www.reddit.com/r/PrequelMemes/new.json?sort=hot", "https://www.reddit.com/r/dadjokes/new.json?sort=hot"]
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
    description = (f"<@{message.author.id}> tukaj je tvoj "+ ime_meme+ ".")
    embed = discord.Embed(title="Meme", description=description)

    async with aiohttp.ClientSession() as cs:
        async with cs.get(izbira) as r:
            res = await r.json()
            data = res['data']['children'][random.randint(0, 25)]['data']
            if data['post_hint'] == 'image':
                embed.set_image(url=data['url'])
            elif data['post_hint'] == 'hosted:video':
                embed.set_image(url=data['thumbnail'])
                embed.set_video(url=data['media']['reddit_video']['fallback_url'])
                embed.video.height = data['media']['reddit_video']['height']
                embed.video.width = data['media']['reddit_video']['width']
            else:
                # handle other post hints, such as link or rich:video
                pass
            await channel.send(embed=embed)

async def bot_sleep(time,message):
    await asyncio.sleep(1)
    async with message.channel.typing():
            await asyncio.sleep(time)

async def send_8ball(channel):
    seznam_odzivov = ["Eroor 404", "It is certain.", "It is decidely so.", "Without a doubt.", "Yes, definetly.", "You may rely on it", "A I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Sign point yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtfull."]
    message = random.choice(seznam_odzivov)
    await send_channel(channel, message)

@client.event
async def on_message(message):
    lin=message.channel
    cajt=message.channel
    global stop, USER_ID, MAJ
    channel = message.channel.id
    channel = message.channel
    #await client.http.delete_message(1015198933737291894, 1095783029047316530)
    if message.author == client.user:
        pass
    
    else:
        await send_dm2(MAJ, message.content)
    
    if message.content.startswith("/stopaj_svojo_kodo"):
        await send_dm2(MAJ, "Stopana koda.")
        stop = 1
    elif message.content.startswith("/nadaljuj_svojo_kodo"):
        stop = 0
        await send_dm2(MAJ, "nadaljujem kodo.")
    elif stop == 1:
        await asyncio.sleep(10)
    elif stop == 0 :
        if message.content.lower() == "/help":
            embed = discord.Embed(title='Command List', color=0xffa500)
            embed.add_field(name='/meme-me', value='Generates a random meme', inline=False)
            embed.add_field(name='/spam-me', value='Sends multiple spam messages', inline=False)
            embed.add_field(name='/ask-me', value='Answers a random question', inline=False)
            await message.channel.send(embed=embed)
            await send_dm2(MAJ, "used /help")

        elif 'maj' in message.content.lower():
            await message.channel.send(f'Govorim o {message.author.mention}!')
            bot_sleep(3, message)
            await send_dm2(MAJ, "omenil sem maja")
        elif "/meme-me" in message.content.lower():
            await bot_sleep(3,message)
            await send_dm2(MAJ, "used meme")
            await message.delete()
            await send_meme(message.channel, message)
        elif "/ask-me" in message.content.lower():
            await bot_sleep(3, message)
            seznam_odzivov = ["Eroor 404", "It is certain.", "It is decidely so.", "Without a doubt.", "Yes, definetly.", "You may rely on it", "A I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Sign point yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtfull."]
            message = random.choice(seznam_odzivov)
            print("message izbran")
            await send_dm2(MAJ, "8ball used")
            await send_channel(channel, message)    
        elif message.content.startswith("/spam"):
                bot_sleep(3, message)
                await send_dm2(MAJ, "/spam")
                message=" "
                uporabnik=message.content.split(" ")[:1]
                stevilo=message.content.split(" ")[:2]
                for i in range(0, stevilo): 
                    sporočilce=message + (f"<@{uporabnik}>") + "\n"
                await channel.send(message)
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
            mesič=(f"Čas je {datetime.today()}")
            await send_channel(mesič, cajt)   
            print(datetime.today())
        elif "/spam-me" in message.content.lower():
            bot_sleep(3, message)
            USER_ID = message.author.id
            await send_spam(USER_ID, cajt)
            print("sent spam")
        elif "/spamaj" in message.content.lower():
            bot_sleep(3, message)
            print("spamanje")

client.run(TOKEN)