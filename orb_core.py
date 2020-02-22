"""
Main controller for Orb, also handles some basic commands & functions

Use the following link to add the bot:
https://discordapp.com/oauth2/authorize?client_id=569758271930368010&scope=bot&permissions=64
"""

# Imports libraries needed
import discord
import random
import os
import csv
import re
import sys
from google.cloud import firestore

from discord.ext import commands as bot_commands
print("Base libraries successfully loaded")


# Gets constants from files. Yay interlinking
from cogs.orb_commands import COMMANDS_VERSION, COMMAND_DATA
from cogs.orb_control import allowed_channel, db #TODO: Move Firestore into a util module (db.py?)
from utils import repo 

# Assigns bot & client
bot = bot_commands.Bot(command_prefix=repo.get_prefix, help_command=None, case_insensitive=True)
client = discord.Client()

# Builds or opens log file
log = open("log.txt", mode="a")

# Loads all the extensions 
files = os.listdir('cogs')
files.remove('__init__.py')
files.remove('orb_fight_new.py')    # under development 
files.remove('orb_economy.py')      # blank placeholder module
files.remove('orb_gacha.py')        # blank placeholder module
for file in files:
    if file.endswith('.py'):
        file_name = file[:-3]
        bot.load_extension(f'cogs.{file_name}')
        print(str(file_name) + '.py loaded!')
print('Just a little bit more...')

# Orb bot help text (TODO: fix this so that it displays the built-in help command in Discord.py instead) 
@bot.command()
async def help(ctx):
    if allowed_channel(ctx):
        print("Help request received from", ctx.author.display_name)
        await ctx.send(u"Orb bot is a bot that does things. Features include:\n   - Reactions\n   - Posting Illya\n   - Ranking\nFor a list of commands see orb.commands, or check them out online at https://aribowe.github.io/orb/commands. To check the bot status, see orb.status.\nDeveloped by xiii™#0013 and 🌸Julianne🌸#6939.")



# Lists commands
@bot.command()
async def commands(ctx, target=None):
    if allowed_channel(ctx):
        # output = ""
        # if target is None:
        #     print("Command overview requested from", ctx.author.display_name)
        #     output += "**Accepted commands:**\n```"
        #     for command in COMMAND_DATA:
        #         output += "orb." + command + "\n"
        #     output += "```\n```Call a specific command for more info, or all for a full command dump```"
        # elif target.upper() == "ALL":
        #     print("Full commands list requested from", ctx.author.display_name)
        #     for command in COMMAND_DATA:
        #         output += "```Command: " + "orb." + command + "\n"
        #         output += "Function: " + COMMAND_DATA[command][0] + "\n"
        #         output += "Arguments: " + COMMAND_DATA[command][1] + "```"
        # else:
        #     print("Info on " + target + " requested by " + ctx.author.display_name)

        #     info, args = COMMAND_DATA[target]
        #     output += "```Command: orb." + target + "\n"
        #     output += "Function: " + str(info) + "\n"
        #     output += "Arguments: " + str(args) + "```"
        #     # except:
        #     #     print("Command not found")
        #     #     output = "Error: Command not found"
        await ctx.send("I have a lot of commands, visit https://aribowe.github.io/orb/commands to see them all")

bot.run(os.environ['DISCORD_TOKEN'], bot=True, reconnect=True)
