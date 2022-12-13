import discord
from discord.ext import commands


client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")

@client.command()
async def series(contex):
    await contex.send(f"Teles of the Walking Dead s01 > {torrent(requests.get('https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'))}")

client.run('')
