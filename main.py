import os  # for importing env vars for the bot to use
from twitchio.ext import commands

from keep_alive import keep_alive

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']])


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], "/me I'm Online!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('/me test passed!')


keep_alive()
if __name__ == "__main__":
    bot.run()
