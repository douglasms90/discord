import discord, os
from discord.ext.commands import Bot, Context
from dotenv import load_dotenv

from ext.webscraping import bs
from ext.commands import populateDb
from ext.database import session
from models import website


load_dotenv()
token = os.getenv('BotToken')

client = Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")

populateDb()

@client.command()
async def series(contex):
    await contex.send("**Aguarde um momento**...")
    for serie in session.query(website):
        soup = bs(serie.author)
        try:
            embed = discord.Embed(
                title = soup.find_all('span', class_='info_dados')[0].text,
                description = soup.find_all('span', class_='botao_dublado')[-1].text
            )
            embed.set_author(name=serie.author)
            await contex.send(embed = embed)
        except:
            await contex.send(f"**{soup.find_all('span', class_='info_dados')[0].text}** - Aguardando dublagem")

client.run(token)
