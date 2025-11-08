import os
import discord
from discord.ext import commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    custom_status = "I think, I can help you for something?"
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name=custom_status))

    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1298256171890901134)
    text = f"{member.mention} Are you new here!"
    await channel.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1298256171890901134)
    text = f"{member.name} I hope you come back hehe"
    await channel.send(text)

server_on()

bot.run(os.getenv('TOKEN'))
