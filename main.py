# This part is for gunicorn running environment
from flask import Flask, session
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello!"
########################

import os
import datetime
import discord
from discord.ext import commands
from functions.sendLineNotifyMessage import sendLineNotifyMessage

bot = commands.Bot(command_prefix='>t')

lineNotifyToken = os.environ["LINE_NOTIFY_TOKEN"]
discordBotToken = os.environ["DISCORD_BOT_TOKEN"]
whitelistChannels = [eval(x) for x in os.environ["WHITELIST_CHANNELS"].split(';') if x != ""]
messageTemplate = os.environ["MESSAGE_TEMPLATE"]
log = dict()
cooldown = 1.5 # 1.5 minutes

@bot.listen()
async def on_voice_state_update(member, before, after):
    if member.bot: return
    if not member or not after.channel: return
    if after.channel.id not in whitelistChannels: return

    # check cooldown
    now = datetime.datetime.now()
    if member.id in log:
        lastTimestamp = log[member.id]        
        if now - lastTimestamp < datetime.timedelta(minutes=cooldown):
            print("白目 {userName} 的冷卻時間還有 {cooldown}".format(userName=member.name, cooldown=datetime.timedelta(minutes=cooldown) - (now - lastTimestamp)))
            return

    # send messages to Line group
    log[member.id] = now
    message = messageTemplate.format(userName=member.name, guildName=member.guild, channelName=after.channel.name)
    sendLineNotifyMessage(lineNotifyToken, message)
    print("已發出訊息：", message)

print("Running")
bot.run(discordBotToken)
