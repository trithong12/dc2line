# Description
This tiny app will send a message to LINE group when a member has joined the Discord guild voice channel.

# Deployment
This app is deployed on Heroku.

# Usage
- Clone this repository and <code>cd</code> into the folder.
- Prepare your environment variables:
    ```
    LINE_NOTIFY_TOKEN
    DISCORD_BOT_TOKEN
    MESSAGE_TEMPLATE
    WHITELIST_CHANNELS
    ```
    - To get the <code>LINE_NOTIFY_TOKEN</code>, please refer to this page: https://notify-bot.line.me/my/
    - To get the <code>DISCORD_BOT_TOKEN</code>, please refer to this page: https://discord.com/developers/docs/intro
    - <code>MESSAGE_TEMPLATE</code>: a message string with 3 arguments: <code>userName</code>, <code>guildName</code>, <code>channelName</code>.
    - <code>WHITELIST_CHANNELS</code>: includes all the whitelist channel ids (delimited by colon <code>;</code>)
        > Whitelist channels: when a member connect to a whitelist channel, there will be a notification sent to LINE group.

- Install requirements:
    <code>pip install -r requirements.txt</code>
- Execution:
    <code>python main.py</code>