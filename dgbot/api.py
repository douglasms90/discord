import discord, os
from discord.ext.commands import Bot, Context
from ext.commands import populateDB
from dotenv import load_dotenv
from ext.database import db, dbo, session
from ext.webscraping import soup
from models import website


populateDB()

load_dotenv()
token = os.getenv('BotToken')

client = Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")

@client.command()
async def series(contex):
    await contex.send("**Aguarde um momento**...")
    for serie in session.query(website):
        try:
            await contex.send(f"**{serie.name}** - {soup(serie.link).find_all('span', class_='botao_dublado')[-1].text}")
        except:
            await contex.send(f"**{serie.name}** - Aguardando dublagem")

client.run(token)
