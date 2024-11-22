import disnake
from disnake.ext import commands
import os

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents, test_guilds=[1092877622318477384])

@bot.event
async def on_ready():
    print("Ready!")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run('')
