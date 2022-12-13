import discord
from discord.ext.commands import Bot, Context
from ext.webscraping import init_api


client = Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")


@client.command()
async def series(contex):
    for serie in init_api(links):
        await contex.send(serie)

client.run('')
