import discord
import datetime
import os

from COGS.UTILS.Database import checkserverprefix
from discord.ext import commands

start_time = datetime.datetime.now()

guild_id = discord.Guild.id

# prefix = checkserverprefix(guild_id)


# Convert uptime to a string.
def timedelta_str(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days, hours, minutes, sec)
    elif minutes > 1 and sec == 1:
        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days, hours, minutes, sec)
    elif minutes == 1 and sec > 1:
        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days, hours, minutes, sec)
    else:
        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days, hours, minutes, sec)


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('Banana Bot Success!')
    print(f"{guild_id}")


@client.command()
async def uptime(ctx):
    """Displays bot uptime."""
    global start_time
    await ctx.send(timedelta_str(datetime.datetime.now() - start_time))


client.run(os.environ.get("TOKEN"))
