import os

# from flask import Flask

import discord
from discord.ext import commands

from functions.sendLineNotifyMessage import sendLineNotifyMessage

# app = Flask(__name__)

bot = commands.Bot(command_prefix='>t')

lineNotifyToken = os.environ["LINE_NOTIFY_TOKEN"]
discordBotToken = os.environ["DISCORD_BOT_TOKEN"]

@bot.listen()
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    if not member or not after.channel:
        return

    message = "%s 剛進入群組《%s》語音頻道《%s》" % (member.name, member.guild, after.channel.name)
    sendLineNotifyMessage(lineNotifyToken, message)

print("Running")
bot.run(discordBotToken)
