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
    print(f'Logged in as {client.user}')

    # Set the user you want to check
    target_user = "LinCadez"

    while True:
        # Get the current time
        now = datetime.now().time()

        # Check if it is past 10 pm
        if now > time(hour=20):
            # Get the user object from their name
            user = discord.utils.get(client.get_all_members(), name=target_user)
            print("found lin")
            if user is not None and user.status != discord.Status.offline:
                # Send message to the user
                await user.send("Pejt spat!")
                print("sent")

        # Wait for 1 minute
        await asyncio.sleep(60)

# Replace the token with your own bot's token
client.run(TOKEN)