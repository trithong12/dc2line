# Description
This tiny app will send a message to Line group when a member has joined the Discord guild voice channel.

# Deployment
This app is deployed on Heroku

# Usage
- Clone this repository and <code>cd</code> into the folder.
- Prepare your environment variables:
    ```
    LINE_NOTIFY_TOKEN
    DISCORD_BOT_TOKEN
    ```
    - To get the <code>LINE_NOTIFY_TOKEN</code>, please refer to this page: https://notify-bot.line.me/my/
    - To get the <code>DISCORD_BOT_TOKEN</code>, please refer to this page: https://discord.com/developers/docs/intro 
- Install requirements:
    <code>pip install -r requirements.txt</code>
- Execution:
    <code>python main.py</code>