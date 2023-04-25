import discord
from discord.ext import commands
import json

# config.jsonからトークンなどの情報を読み込む
r = open('config.json')
load = json.load(r)

# Botの設定を行う
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=load['PREFIX'], intents=intents)
"""
# ボタンが押された時にメッセージを返す関数
async def button_callback(interaction):
    await interaction.response.send_message("Hi!")
"""
# 起動シーケンス
@bot.event
async def on_ready():
    print("{}を起動しました".format(bot.user))

# discord botとの対話ができるかを確認するコマンド
@bot.command()
async def ping(ctx):
    await ctx.send("pong")
"""
# Helloのリアクションコマンド
@bot.command()
async def hello(ctx):
    button = Button(label="Click", style=discord.ButtonStyle.green, emoji="🥹")
    button.callback = button_callback

    view = View()
    view.add_item(button)
    await ctx.send("Hi!", view=view)
"""
# リアクションを増やした時に実行される
@bot.event
async def on_raw_reaction_add(payload):
    print("reaction add func start")

    message_id = payload.message_id
    # load['MESSAGE_ID]はdiscordの特定のメッセージを指定してるIDです。（config.jsonに記載します）
    if message_id == int(load['MESSAGE_ID']):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        # "environment"という名の絵文字が追加されたら
        if payload.emoji.name == "environment":
            print("-" * 50 + "environment" + "-" * 50)
            role = discord.utils.get(guild.roles, name="environment")
        # "pr"という名の絵文字が追加されたら
        elif payload.emoji.name == "pr":
            print("-" * 50 + "pr" + "-" * 50)
            role = discord.utils.get(guild.roles, name="pr")
        # "seminar"という名の絵文字が追加されたら
        elif payload.emoji.name == "seminar":
            print("-" * 50 + "seminar" + "-" * 50)
            role = discord.utils.get(guild.roles, name="seminar")
        # "event"という名の絵文字が追加されたら
        elif payload.emoji.name == "event":
            print("-" * 50 + "event" + "-" * 50)
            role = discord.utils.get(guild.roles, name="event")
        # "plan"という名の絵文字が追加されたら
        elif payload.emoji.name == "plan":
            print("-" * 50 + "plan" + "-" * 50)
            role = discord.utils.get(guild.roles, name="plan")
        else:
            print("emoji not found.")
            role = None

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.add_roles(role)
            print("done")
        else:
            print("Member not found.")
    else:
        print("Role not found.")
    
    print("reaction add func end")

# リアクションを減らした時に実行される
@bot.event
async def on_raw_reaction_remove(payload):
    print("reaction remove func start")

    message_id = payload.message_id
    # load['MESSAGE_ID]はdiscordの特定のメッセージを指定してるIDです。（config.jsonに記載します）
    if message_id == int(load['MESSAGE_ID']):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        # "environment"という名の絵文字が追加されたら
        if payload.emoji.name == "environment":
            print("-" * 50 + "environment" + "-" * 50)
            role = discord.utils.get(guild.roles, name="environment")
        # "pr"という名の絵文字が追加されたら
        elif payload.emoji.name == "pr":
            print("-" * 50 + "pr" + "-" * 50)
            role = discord.utils.get(guild.roles, name="pr")
        # "seminar"という名の絵文字が追加されたら
        elif payload.emoji.name == "seminar":
            print("-" * 50 + "seminar" + "-" * 50)
            role = discord.utils.get(guild.roles, name="seminar")
        # "event"という名の絵文字が追加されたら
        elif payload.emoji.name == "event":
            print("-" * 50 + "event" + "-" * 50)
            role = discord.utils.get(guild.roles, name="event")
        # "plan"という名の絵文字が追加されたら
        elif payload.emoji.name == "plan":
            print("-" * 50 + "plan" + "-" * 50)
            role = discord.utils.get(guild.roles, name="plan")
        else:
            print("emoji not found.")
            role = None

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            print("done")
        else:
            print("Member not found.")
    else:
        print("Role not found.")

    print("reaction remove func end")

bot.run(load['TOKEN'])