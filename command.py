import os
import discord
from discord.ext import commands
import random
import json
from typing import Any

TOKEN = "MTQzODkyMzc1NzAyMzM5NTk0MA.GXJ_yc.GQUPdK_AOn7-CmBn_SZfEQO-oGgAeEQ0Waj4D8"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")

####

# culture_nugget1=\
#      {"ID": 1,
#  "Q": "Who is considered the father of computer science?",
#  "A": "Alan Turing"
#  }
#
# culture_nugget2=\
#      {"ID": 2,
#   "Q": "What does HTML stand for?",
#   "A": "HyperText Markup Language"}
#
#
# culture_nugget3=\
#    {"ID": 3,
#     "Q": "What does the file extension “.jpg” indicate?",
#  "A": "It is a compressed image file format"}
#
# culture_nugget4=\
#     {"ID": 4,
#  "Q": "What is the name of the inventor of the World Wide Web?",
#  "A": "Tim Berners-Lee"}
#
# culture_nugget5=\
#    {"ID": 5,
#  "Q": "What does RAM mean?",
#  "A": "Random Access Memory"}
#
# culture_nuggets= [
#  culture_nugget1,
#  culture_nugget2,
#  culture_nugget3,
#  culture_nugget4,
#  culture_nugget5
#  ]
#
# with open("data.json", "w") as file:
#      culture_nuggets=json.dump(culture_nuggets, file)
#
# print(culture_nuggets)

######

with open("data.json", "r") as file:
    culture_nuggets=json.load(file)

# pick_random=random.choice(culture_nuggets)
# print(pick_random["Q"])
# print(pick_random["A"])

@bot.command()
async def nugget(ctx):
    pick_random = random.choice(culture_nuggets)
    question = pick_random["Q"]
    answer = pick_random["A"]

    await ctx.send(f"💡 **Did you know?**\n {question}\n **Answer:** {answer}")


bot.run(TOKEN)


