import discord, os
from discord.ext.commands import Bot, Context
from dotenv import load_dotenv

from ext.webscraping import soup
from ext.commands import populateDB
from ext.database import session, dbConn
from models import website


load_dotenv()
token = os.getenv('BotToken')

client = Bot(command_prefix='.', intents=discord.Intents.all())

@client.command()
async def test(contex):
    await contex.send("Hi!")

populateDB()

@client.command()
async def series(contex):
    await contex.send("**Aguarde um momento**...")
    for serie in session.query(website):
        try:
            await contex.send(f"**{serie.name}** - {soup(serie.link).find_all('span', class_='botao_dublado')[-1].text}")
        except:
            await contex.send(f"**{serie.name}** - Aguardando dublagem")

@client.command()
async def os(contex):
    conn = dbConn()
    await contex.send(f'ID DEFEITO TIPO GERADA CLIENTE CIDADE BAIRRO')
    rows = conn.consult("""""")
    for row in rows:
        await contex.send(f'{row}')

@client.command()
async def re(contex):
    await contex.send(f'ID DEFEITO DESCRIÇÃO FECHAMENTO CLIENTE OPERADOR DESCRIÇÃO')
    rows = conn.consult("""""")    
    for row in rows:
        await contex.send(f'{row}')

client.run(token)
