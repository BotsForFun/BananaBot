import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('Banana Bot Success!')

client.run(os.environ.get("TOKEN"))
