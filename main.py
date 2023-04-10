import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

IMAGE_BETA = os.getenv("beta_server")
IMAGE_BETA_CHANNEL = os.getenv("beta_channel")

load_dotenv()
TOKEN = os.getenv("moj_token")

intents = discord.Intents.default()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(1042465386945314868)
    await channel.send('hello') 

@bot.command()
async def _send(ctx):
    guild = bot.get_guild(IMAGE_BETA) # Replace IMAGE_BETA with your server ID
    channel = guild.get_channel(IMAGE_BETA_CHANNEL) # Replace IMAGE_BETA_CHANNEL with your channel ID
    await channel.send('Hello, world!')
    await print("send")

bot.run(TOKEN)
