import os
import discord
from discord.ext import commands, tasks
import random
import datetime
import json
from typing import Any
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
DAILY_CHANNEL_ID = int(os.getenv("DAILY_CHANNEL_ID", "0"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")

    if not daily_nugget.is_running():
        daily_nugget.start()
        print("Task daily_nugget started")

####

# culture_nugget1=\
#      {"ID": 1,
#  "Q": "Who is considered the father of computer science?",
#  "A": "Alan Turing",
#   "Link": "https://en.wikipedia.org/wiki/Alan_Turing"
#  }
#
# culture_nugget2=\
#      {"ID": 2,
#   "Q": "What does HTML stand for?",
#   "A": "HyperText Markup Language",
#   "Link": "https://en.wikipedia.org/wiki/HTML"}
#
#
# culture_nugget3=\
#    {"ID": 3,
#     "Q": "What does the file extension “.jpg” indicate?",
#  "A": "It is a compressed image file format",
#  "Link": "https://kinsta.com/blog/jpg-vs-jpeg/"}
#
# culture_nugget4=\
#     {"ID": 4,
#  "Q": "What is the name of the inventor of the World Wide Web?",
#  "A": "Tim Berners-Lee",
#  "Link": "https://en.wikipedia.org/wiki/Tim_Berners-Lee"}
#
# culture_nugget5=\
#    {"ID": 5,
#  "Q": "What does RAM mean?",
#  "A": "Random Access Memory",
#  "Link": "https://en.wikipedia.org/wiki/Random-access_memory"}
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
#
# ######
#
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
    link = pick_random["Link"]

    await ctx.send(
    f"**Did you know? 💡**\n\n"
    f"❓ {question}\n"
    f"**Answer:** ✔️ {answer}\n\n"
    f"🔗 {link}"
)
@tasks.loop(minutes=10)
async def daily_nugget():
    channel=bot.get_channel(DAILY_CHANNEL_ID)
    pick_random = random.choice(culture_nuggets)
    question = pick_random["Q"]
    answer = pick_random["A"]
    link = pick_random["Link"]

    await channel.send(
    f"**Did you know? 💡**\n\n"
    f"❓ {question}\n"
    f"**Answer:** ✔️ {answer}\n\n"
    f"🔗 {link}"
)

@daily_nugget.before_loop
async def before_daily_nugget():
    await bot.wait_until_ready()

bot.run(TOKEN)
