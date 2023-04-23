import discord
from discord.ext import commands
import json

r = open('config.json')
load = json.load(r)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=load['prefix'], intents=intents)

@bot.event
async def on_ready():
    print("起動しました:{}".format(bot.user))

@bot.command()
async def test(ctx):
    await ctx.send("return test")

bot.run(load['token'])