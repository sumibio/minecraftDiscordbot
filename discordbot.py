from discord.ext import commands
import json
import requests
import traceback
import os


bot = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']
URL = os.environ['APIURL']
APIKEY = os.environ['APIKEY']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def start(ctx):
    headers = {
        'x-api-key': APIKEY,
        'action': 'start'
    }
    url = URL
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        message = json.loads(res.content)['message']
        await ctx.send(message)


@bot.command()
async def stop(ctx):
    headers = {
        'x-api-key': APIKEY,
        'action': 'stop'
    }
    url = URL
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        message = json.loads(res.content)['message']
        await ctx.send(message)


bot.run(TOKEN)
