import discord
import asyncio
import os
import requests
import aiohttp
from dotenv import load_dotenv
from datetime import datetime, time

load_dotenv()
TOKEN = os.getenv("drugi_token")

intents = discord.Intents().all()
intents.members = True

client = discord.Client(intents=intents)

async def get_current_hour():
    url = "http://worldtimeapi.org/api/ip"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                current_time = datetime.strptime(data["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z").time()
                return current_time.hour
            else:
                raise Exception("Failed to fetch current time from the API.")
            await session.close()

@client.event
async def on_ready():
    # Set the user you want to check
    target_user = "LinCadez"
    target_user2 = "MajMohar"

    while True:
        try:
            # Get the current hour
            hour = await get_current_hour()

            # Check if it is between 10 PM and 5 AM
            if hour > 22 or hour < 5:
                # Get the user object from their name
                user = discord.utils.get(client.get_all_members(), name=target_user)
                if user is not None and user.status == discord.Status.online:
                    # Send message to the user
                    user_id = user.id
                    await user.send(f"<@{user_id}>, pejt spat!")
                    print("user 1")
                user2 = discord.utils.get(client.get_all_members(), name=target_user2)
                if user2 is not None and user2.status == discord.Status.online:
                    # Send message to the user
                    user2_id = user2.id
                    await user2.send(f"<@{user2_id}>, pejt spat!")
                    print("user 2")
        except Exception as e:
            print(f"Error: {str(e)}")

        # Wait for 1 minute
        await asyncio.sleep(60)

# Replace the token with your own bot's token
client.run(TOKEN)
