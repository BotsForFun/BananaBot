import discord
from discord.ext import commands


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready(ctx):
    print('Banana Bot Success!')

client.run(os.environ.get("TOKEN"))
