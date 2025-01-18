import discord, asyncio
from discord.ext import commands
from decouple import config

#from ext.commands import createdb

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

async def create_api():
    await bot.load_extension('cogs._init')
    await bot.load_extension('cogs.msc')
    await bot.load_extension('cogs.psl')
    await bot.load_extension('cogs.nails')
    await bot.load_extension('cogs.fin')
    await bot.load_extension('cogs.work')
    await bot.start(config('TOKEN'))

asyncio.run(create_api())
