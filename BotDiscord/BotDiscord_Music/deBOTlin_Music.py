import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('OTY2MDYyNTg0NjQ4MzEwODM1.Yl8R5A.tYz8HoiMdHnuECFoiXPLJjM_br8')
