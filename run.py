import discord, requests
from discord.ext.commands import Bot, Context
from bs4 import BeautifulSoup


client = Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")

def torrent(source):
    try:
        return BeautifulSoup(source.content, "html.parser").find_all("span", class_="botao_dublado")[-1].text
    except:
        return "Aguardando dublagem"


@client.command()
async def series(contex):
    await contex.send(f"Teles of the Walking Dead s01 > {torrent(requests.get('https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'))}")
    await contex.send(f"Titans s04 > {torrent(requests.get('https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/'))}")
    await contex.send(f"Fear in the Walking Dead s08 > {torrent(requests.get('https://lacraiatorrent.com/fear-the-walking-dead-8-temporada-torrent-dublada/'))}")
    await contex.send(f"The Rings of Power s02 > {torrent(requests.get('https://lacraiatorrent.com/o-senhor-dos-aneis-os-aneis-de-poder-2-temporada-torrent-dublada/'))}")
    await contex.send(f"House of the Dragon s02 > {torrent(requests.get('https://lacraiatorrent.com/a-casa-do-dragao-2-temporada-torrent-dublada/'))}")
    await contex.send(f"Succession s04 > {torrent(requests.get('https://lacraiatorrent.com/succession-4-temporada-torrent-dublada/'))}")
    await contex.send(f"Barbarians s03 > {torrent(requests.get('https://lacraiatorrent.com/barbaros-3-temporada-completa-torrent-dublada/'))}")
    await contex.send(f"Arcanjo Renegado s03 > {torrent(requests.get('https://lacraiatorrent.com/arcanjo-renegado-3-temporada-torrent/'))}")
    await contex.send(f"She Hulk s02 > {torrent(requests.get('https://lacraiatorrent.com/mulher-hulk-defensora-de-herois-2-temporada-torrent-dublada/'))}")
    await contex.send(f"Sandman s02 > {torrent(requests.get('https://lacraiatorrent.com/sandman-2-temporada-completa-torrent-dublada/'))}")

client.run('')
