import discord
from discord.ui import Button, View
from discord.ext import commands
import json

# config.jsonからトークンなどの情報を読み込む
r = open('config.json')
load = json.load(r)

# Botの設定を行う
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=load['prefix'], intents=intents)

# ボタンが押された時にメッセージを返す関数
async def button_callback(interaction):
    await interaction.response.send_message("Hi!")

# 起動シーケンス
@bot.event
async def on_ready():
    print("{}を起動しました".format(bot.user))

# discord botとの対話ができるかを確認するコマンド
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

# Helloのリアクションコマンド
@bot.command()
async def hello(ctx):
    button = Button(label="Click", style=discord.ButtonStyle.green, emoji="🥹")
    button.callback = button_callback

    view = View()
    view.add_item(button)
    await ctx.send("Hi!", view=view)

# リアクションを増やした時に実行される
@bot.event
async def on_raw_reaction_add(payload):
    print("reaction add func start")
    print("reaction add func end")

# リアクションを減らした時に実行される
@bot.event
async def on_raw_reaction_remove(payload):
    print("reaction remove func start")
    print("reaction remove func end")

bot.run(load['token'])