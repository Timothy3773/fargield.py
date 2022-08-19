import imp
import json
import math
import random
import os
import discord
from discord.ext import commands

client_settings_file = open("clientSettings.json", "r", encoding="utf-8")
client_settings = json.load(client_settings_file)
bot_token = open("token.txt", 'r', encoding="utf-8").read()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=client_settings['prefix'], intents=intents)

def random_activity():
    statie = client_settings['statuses']
    result = statie[random.randint(0, len(statie) - 1)]
    return discord.Activity(name=result['name'],type=discord.ActivityType[result['type']])

def read_dir(path:str, format: bool):
    data = []
    files = os.listdir(path)
    for file in files:
        if len(files) > 0 and file.endswith(".py"):
            data.append(f"{path}.{file.removesuffix('.py')}" if format == True else file)
    return data

@bot.listen("on_ready")
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=random_activity())
    for cmd in read_dir("cmds", True):
        await bot.load_extension(cmd)


bot.run(bot_token)
