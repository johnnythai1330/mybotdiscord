
import os
import discord
from discord.ext import commands
from myserver import server_on

@bot.event
async def on_ready():
    print("Bot Online!")

server_on()

bot.run(os.getenv('TOKEN'))
