import os
import discord
from discord.ext import commands, tasks
import random
import json
from dotenv import load_dotenv
from datetime import datetime

from json_manager import load_nuggets_from_json, save_nugget_to_json

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
DAILY_CHANNEL_ID = int(os.getenv("DAILY_CHANNEL_ID", "0"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

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


# pick_random=random.sample(culture_nuggets, 1)[0]
# print(pick_random["Q"])
# print(pick_random["A"])
# print(pick_random["Link"])

@bot.command()
async def nugget(ctx):
    culture_nuggets=load_nuggets_from_json()
    pick_random=pick_random_based_on_old_dates(culture_nuggets)

    question = pick_random.question
    answer = pick_random.answer
    link = pick_random.link

    await ctx.send(
    f"**Did you know? 💡**\n\n"
    f"❓ {question}\n"
    f"**Answer:** ✔️ {answer}\n\n"
    f"🔗 {link}"
)
    save_nugget_to_json(culture_nuggets)

@tasks.loop(minutes=10)
async def daily_nugget():
    channel=bot.get_channel(DAILY_CHANNEL_ID)
    culture_nuggets=load_nuggets_from_json()
    pick_random=pick_random_based_on_old_dates(culture_nuggets)


    # costruire un algoritmo che eviti di ripetere i nugget piu recenti
    # def pick_rendom_nugget_old_dates
    # ciclo for da usare come filtro che usi maggiore o minore con delle date di esecuzione
    # sottolista older_nuggets


    question = pick_random.question #["Q"]
    answer = pick_random.answer
    link = pick_random.link



#     ## ultimo - sovrascrivere file json con dump
#    #    with open("data.json", "w") as file:
    #         json.dump(file, "data.json")

    await channel.send(
    f"**Did you know? 💡**\n\n"
    f"❓ {question}\n"
    f"**Answer:** ✔️ {answer}\n\n"
    f"🔗 {link}"
    )

    save_nugget_to_json(culture_nuggets)

def pick_random_based_on_old_dates(culture_nuggets):
    #calcolo data media per ricercare lista dei nugget eseguiti precedetemente
    average_date=0
    for nugget in culture_nuggets:
        average_date+=nugget.last_execution.timestamp()
    average_date/=len(culture_nuggets)

    #lista nugget piu vecchi
    older_nuggets=[]
    for nugget in culture_nuggets:
        if nugget.last_execution.timestamp()<=average_date:#datamedia es 30 minuti
            older_nuggets.append(nugget)

    # adesso prendiamo il nugget dalla sottolista older nugget (cioe un nugget piu vecchio)
    pick_random = random.choice(older_nuggets)
    #aggiornare data di esecuzione
    pick_random.last_execution=datetime.now()
    return pick_random



@daily_nugget.before_loop
async def before_daily_nugget():
    await bot.wait_until_ready()

bot.run(TOKEN)
