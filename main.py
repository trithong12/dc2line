from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello!"


import os
import discord
from discord.ext import commands
from functions.sendLineNotifyMessage import sendLineNotifyMessage

bot = commands.Bot(command_prefix='>t')

lineNotifyToken = os.environ["LINE_NOTIFY_TOKEN"]
discordBotToken = os.environ["DISCORD_BOT_TOKEN"]

@bot.listen()
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    if not member or not after.channel:
        return

    message = os.environ["MESSAGE_TEMPLATE"].format(userName=member.name, guildName=member.guild, channelName=after.channel.name)
    sendLineNotifyMessage(lineNotifyToken, message)

print("Running")
bot.run(discordBotToken)
