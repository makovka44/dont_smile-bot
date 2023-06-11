import os
import inspect
import discord
import random
from discord import app_commands, Intents, Client, Interaction

token = os.getenv("tretji_token")
channel_id = 1117147385882230875

class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync()

client = FunnyBadge(intents=Intents.none())

@client.tree.command()
async def role_request(interaction: Interaction, role: str, reason: str):
    """ Send a message to request a role """
    request_message = f"Role Request:\nRole: {role}\nReason: {reason}"
    username2 = str(interaction.user)
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    color = discord.Color.from_rgb(a, b, c)
    embed = discord.Embed(title="Role Request", description=request_message, color=color)
    username = username2.split("#")[0]
    embed.add_field(name="Username", value=username)
    channel = await client.fetch_channel(channel_id)
    request = await channel.send(embed=embed)
    response = inspect.cleandoc(f"""
        Hi **{interaction.user}**, your role request has been sent to the moderators. Thank you for using the role request command.
    """)
    await interaction.response.send_message(response, ephemeral=True)

"""@client.event
async def on_ready():
    channel_id = 1117064293599432824
    channel = await client.fetch_channel(channel_id)
    
    embed = discord.Embed(
        title="Bot Online!",
        description="Hello @everyone! I'm here and ready to assist you.",
        color=discord.Color.green()
    )
    embed.add_field(name="Usage", value="I'm a bot created by <@1014769833688182825>. Use /role_request to request a role.")
    embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/4532-roleiconmod.png")
    embed.add_field(name="Bot Name", value=client.user.name, inline=True)
    embed.add_field(name="Bot ID", value=client.user.id, inline=True)
    embed.set_footer(text="Thanks for using the bot!")

    await channel.send(embed=embed)
"""

client.run("MTExNzE0NjQ5MDM0Mzc5Mjc0MA.GdZnE8.inLsRzW_xdz6eHbtQ0BM8ltKauapzXl6KwKqLY")
