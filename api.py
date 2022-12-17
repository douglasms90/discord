import discord, os
from discord.ext.commands import Bot, Context
from ext import webscraping
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('BotToken')

client = Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")

@client.command()
async def series(contex):
    await contex.send("**Aguarde um momento**...")
    for serie in webscraping.init_api():
        await contex.send(serie)

client.run(token)
