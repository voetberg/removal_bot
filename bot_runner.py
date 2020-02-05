import json
from twitchio.ext import commands

def open_json(json_path):
    with open(json_path) as json_file:
        return json.load(json_file)


config = open_json("./config")

bot = commands.Bot(
    irc_token=config['token'],
    client_id=config['client_id'],
    nick=config['bot_nickname'],
    prefix=config['bot_command_prefix'],
    initial_channels=[config['channel']]
)

@bot.event("on_start")
async def on_start():
    web_service = bot._ws
    await web_service.send_privmsg(config['channel'], f"{config['bot_nickname']} is placed on the battlefield")

