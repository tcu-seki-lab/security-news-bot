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

bot.run(load['token'])