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
    rows = conn.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, to_char(os.data_abertura, 'dd/mm/yyyy'), cl.nome_razaosocial, cd.cidade, ba.bairro
        FROM mk_os os
        FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
        JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
        JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
        JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
        JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
        WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='S' ORDER BY cd.cidade asc""")
    for row in rows:
        await contex.send(f'{row}')

@client.command()
async def re(contex):
    await contex.send(f'ID DEFEITO DESCRIÇÃO FECHAMENTO CLIENTE OPERADOR DESCRIÇÃO')
    rows = conn.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, to_char(os.data_fechamento, 'dd/mm/yyyy'), cl.nome_razaosocial, os.operador_fech_tecnico, os.servico_prestado
        FROM mk_os os
        FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
        JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
        JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
        WHERE  tipo_os in ('4','15','18') AND data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ugl%' ORDER BY os.data_fechamento desc""")    
    for row in rows:
        await contex.send(f'{row}')

client.run(token)
