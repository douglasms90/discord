import discord
from discord.ext import commands

from ext.database import dbc, databaseConnection
from decouple import config
from datetime import datetime

class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="act")
    async def act(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("hostMydb")) as db:
                db.insert("INSERT INTO act (dt, os, sn, cr, ct) VALUES(%s, %s, %s, %s, %s)", (datetime.now(), args[-2], args[-3], 0, args[-1],))
            embed = discord.Embed(title = args[-2], description = f"!ativa_onu_vlan {args[-3]} {args[-6].replace('#','')} {0} {args[-1]}")
            await ctx.send(embed = embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="actid")
    async def actid(self, ctx, *args):
        if ctx.author.id in [269592803602989058]:  # D
            now = datetime.now()
            with databaseConnection(config("hostMydb")) as db:
                db.insert("INSERT INTO act (dt, os, sn, cr, ct) VALUES(%s, %s, %s, %s, %s)", (now, args[0], args[1], 0, args[2],))
            embed = discord.Embed(title='Título', description='Descrição')
            embed.set_author(name='Autor')
            embed.add_field(name='Comando:', value=f"{args[0]}", inline=True)
            embed.set_footer(text='Rodapé')
            await ctx.send(embed = embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=1200)


    @commands.command(name="actreplace")
    async def actreplace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("hostMydb")) as db:
                before = db.read(f"SELECT * FROM act WHERE id={args[0]}", (None))
                db.update(f"UPDATE act SET {args[1]} = %s WHERE id = %s", (args[2], args[0]))
                after = db.read(f"SELECT * FROM act WHERE id={args[0]}", (None))
            embed = discord.Embed(title='Replace', description=f'Anteriormente: {before[0]}\nPosteriormente: {after[0]}!')
            await ctx.send(embed=embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="acttoday")
    async def acttoday(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            dump = ""
            with databaseConnection(config("hostMydb")) as db:
                today = db.read("SELECT * FROM act WHERE DATE(dt) = CURRENT_DATE order by id asc", (None))
            for i in today:
                dump += f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}\n"
            await ctx.send(f"```{dump}```", delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="actlast")
    async def actlast(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            dump = ""
            with databaseConnection(config("hostMydb")) as db:
                today = db.read("SELECT * FROM act ORDER BY id desc LIMIT 20;", None)
            for i in today:
                dump += f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}\n"
            await ctx.send(f"```{dump}```", delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="actdelete")
    async def actdelete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("hostMydb")) as db:
                before = db.read("SELECT * FROM act WHERE id = %s", (args[0],))
                db.delete("DELETE FROM act WHERE id = %s", (args[0],))
            await ctx.send(f'{before}\nDeletado com sucesso.', delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=1200)

    @commands.command(name='naquery')
    async def na(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("host")) as db:
                dump = db.read("SELECT os.codos, cl.nome_razaosocial, left(os.defeito_reclamado, 100), cd.cidade, ba.bairro, FROM mk_os os JOIN mk_pessoas cl ON os.cliente = cl.codpessoa JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade, ba.bairro asc")
            for i in dump:
                embed = discord.Embed(title=i[0],description=i[2])
                embed.set_author(name=i[1])
                embed.add_field(name='cdd', value=i[3], inline=True)
                embed.add_field(name='brr', value=i[4], inline=True)
                embed.set_footer(text='contrato')
                await ctx.send(embed = embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name='insta')
    async def inst(self, ctx, *args):
        if ctx.author.id in [269592803602989058, 867493176666619924, 277135914394845184, 461571385261686786, 1217443149455163442]: # D, C, A, F, R
            conn = dbc(config("host"))
            dump = conn.consult(f"SELECT os.codos, cl.nome_razaosocial, left(os.defeito_reclamado, 100), cl.fone01, cl.fone02, cl.acesso_sac, cl.user_sac, cl.pass_sac, cd.cidade, ba.bairro, co.contrato FROM mk_os os JOIN mk_pessoas cl ON os.cliente = cl.codpessoa JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro JOIN mk_conexoes co ON os.conexao_associada = co.codconexao WHERE codos IN {args}")
            for i in dump:
                embed = discord.Embed(title=i[0],description=i[2])
                embed.set_author(name=i[1])
                embed.add_field(name='f01', value=i[3], inline=True)
                embed.add_field(name='f02', value=i[4], inline=True)
                embed.add_field(name='sac', value=i[5], inline=False)
                embed.add_field(name='usr', value=i[6], inline=True)
                embed.add_field(name='pwd', value=i[7], inline=True)
                embed.add_field(name='cdd', value=i[8], inline=True)
                embed.add_field(name='brr', value=i[9], inline=True)
                embed.set_footer(text=i[10])
                await ctx.send(embed = embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name='requery')
    async def re(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("hostMydb")) as db:
                dump = db.read("SELECT os.codos, cl.nome_razaosocial, left(os.servico_prestado, 100), cd.cidade, ba.bairro FROM mk_os os FULL OUTER JOIN mk_pessoas cl ON os.cliente = cl.codpessoa JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro WHERE data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ugl%' ORDER BY os.data_fechamento desc", (None))
            for i in dump:
                embed = discord.Embed(title=i[0],description=i[2])
                embed.set_author(name=i[1])
                embed.add_field(name='cdd', value=i[3], inline=True)
                embed.add_field(name='brr', value=i[4], inline=True)
                embed.set_footer(text='footer')
                await ctx.send(embed = embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

async def setup(bot):
    await bot.add_cog(work(bot))
