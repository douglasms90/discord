import discord, os, asyncio
from discord.ext import commands
from decouple import config

from ext.commands import create

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

async def create_api():
    await bot.load_extension(f'cogs._init')
    await bot.load_extension(f'cogs.psl')
    await bot.load_extension(f'cogs.fin')
    await bot.load_extension(f'cogs.work')
    await bot.start(config('TOKEN'))

asyncio.run(create_api())
