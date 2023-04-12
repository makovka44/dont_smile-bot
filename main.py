import discord


import os
from dotenv import load_dotenv()


load_dotenv()
TOKEN = os.getenv("moj_token")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

import discord
import random


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    sporocilo=message.content
    
  

client.run(TOKEN)

