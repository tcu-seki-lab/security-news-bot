import discord
from discord.ext import commands
import json

r = open('config.json')
load = json.load(r)

bot = commands.Bot(command_prefix=load['prefix'])

@bot.event
async def on_ready():
    print("起動しました:{}".format(bot.user))

@bot.command()
async def test(ctx):
    await ctx.send("return test")

bot.run(load['token'])