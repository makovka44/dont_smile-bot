import discord
import asyncio, os
from dotenv import load_dotenv
from datetime import datetime, time
load_dotenv()
TOKEN=os.getenv("drugi_token")

intents = discord.Intents().all()
intents.members= True

client = discord.Client(intents=intents)
@client.event
async def on_ready():

    # Set the user you want to check
    target_user = "LinCadez"
    target_user2 = "MajMohar"

    while True:
        # Get the current time
        now = datetime.now().time()

        # Check if it is past 10 pm
        if now > time(hour=22):
            # Get the user object from their name
            user = discord.utils.get(client.get_all_members(), name=target_user)
            if user is not None and user.status != discord.Status.offline:
                # Send message to the user
                user_id = user.id
                await user.send(f"<@{user_id}>, pejt spat!")
                print("user 1")
        if now > time(hour=22):
            user2 = discord.utils.get(client.get_all_members(), name=target_user2)
            if user2 is not None and user2.status != discord.Status.offline:
                # Send message to the user
                user2_id = user2.id
                await user2.send(f"<@{user2_id}>, pejt spat!")
                print("user 2")

        # Wait for 1 minute
        await asyncio.sleep(60)
# Replace the token with your own bot's token
client.run(TOKEN)