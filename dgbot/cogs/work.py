import discord
from discord.ext import commands

from ext.database import dbc, databaseConnection
from decouple import config

class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="acttst")
    async def act(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("host")) as db:
                cr = db.read(f"SELECT co.contrato FROM mk_os os JOIN mk_conexoes co ON os.conexao_associada = co.codconexao WHERE codos=44612")
                print(cr)

    @commands.command(name="act")
    async def act(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            conn = dbc(config("host"))
            dump = conn.consult(f"SELECT co.contrato FROM mk_os os JOIN mk_conexoes co ON os.conexao_associada = co.codconexao WHERE codos={args[-2]}")
            now=datetime.now()
            with Session() as session:
                session.add(Act(dt=now,usr=ctx.author.id,ido=args[-2],sn=args[-3],ctr=dump[0][0],cto=args[-1]))
                session.commit()
                vln=args[-6].replace('#',''),
                for obj in session.query(Act).filter(Act.dt == now):
                    embed = discord.Embed(title='tittle',description='description')
                    embed.set_author(name=obj.usr)
                    embed.add_field(name='Comando:', value=f'!ativa_onu_vlan {obj.sn} {vln} {obj.ctr} {obj.cto}', inline=True)
                    embed.set_footer(text=obj.id)
                    await ctx.author.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="actid")
    async def actid(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            conn = dbc(config("host"))
            dump = conn.consult(f"SELECT co.contrato FROM mk_os os JOIN mk_conexoes co ON os.conexao_associada = co.codconexao WHERE codos={args[0]}")
            now=datetime.now()
            with Session() as session:
                session.add(Act(dt=now,usr=ctx.author.id,ido=args[0],sn=args[1],ctr=dump[0][0],cto=args[2]))
                session.commit()
                for obj in session.query(Act).filter(Act.dt == now):
                    embed = discord.Embed(title='title',description='description')
                    embed.set_author(name=obj.usr)
                    embed.add_field(name='name:', value=f'value', inline=True)
                    embed.set_footer(text=obj.id)
                await ctx.author.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="actreplace")
    async def replace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                session.query(Act).filter(Act.id == args[0]).update({args[1]:args[2]})
                session.commit()
            await ctx.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="acttoday")
    async def today(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                for obj in session.query(Act).filter(Act.dt.like(f'{datetime.now().date()}%')):
                    embed = discord.Embed(title='tittle',description='description')
                    embed.set_author(name=obj.usr)
                    embed.add_field(name='name', value=f'value', inline=True)
                    embed.set_footer(text=obj.id)
                    await ctx.author.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="actdelete")
    async def delete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                session.query(Act).filter(Act.id == args[0]).delete()
                session.commit()
            await ctx.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name='naquery')
    async def na(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            conn = dbc(config("host"))
            dump = conn.consult("SELECT os.codos, cl.nome_razaosocial, left(os.defeito_reclamado, 100), cd.cidade, ba.bairro, FROM mk_os os JOIN mk_pessoas cl ON os.cliente = cl.codpessoa JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade, ba.bairro asc")
            for i in dump:
                embed = discord.Embed(title=i[0],description=i[2])
                embed.set_author(name=i[1])
                embed.add_field(name='cdd', value=i[3], inline=True)
                embed.add_field(name='brr', value=i[4], inline=True)
                embed.set_footer(text='contrato')
                await ctx.author.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name='insta')
    async def na(self, ctx, *args):
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
                await ctx.author.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name='requery')
    async def re(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            conn = dbc(config("host"))
            dump = conn.consult("SELECT os.codos, cl.nome_razaosocial, left(os.servico_prestado, 100), cd.cidade, ba.bairro FROM mk_os os FULL OUTER JOIN mk_pessoas cl ON os.cliente = cl.codpessoa JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro WHERE data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ugl%' ORDER BY os.data_fechamento desc")
            for i in dump:
                embed = discord.Embed(title=i[0],description=i[2])
                embed.set_author(name=i[1])
                embed.add_field(name='cdd', value=i[3], inline=True)
                embed.add_field(name='brr', value=i[4], inline=True)
                embed.set_footer(text='footer')
                await ctx.author.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    # Nail --------------------------------------------------------

    @commands.command(name="nails")
    async def nail(self, ctx, *args):
        now=datetime.now()
        with databaseConnection(config("hostMydb")) as db:
            db.insert("INSERT INTO nails(dt, pr) VALUES(%s, %s)", (now, args[0],))
            view = db.read("SELECT * FROM nails WHERE dt={now}")
        for i in view:
            embed = discord.Embed(title=f'{now}',description='Unha')
            embed.set_author(name=ctx.author)
            embed.add_field(name='', value=f'', inline=True)
            embed.set_footer(text=view[0])
        await ctx.send(embed = embed)

    @commands.command(name="nailsdelete")
    async def delete(self, ctx, *args):
        with databaseConnection(config("hostMydb")) as db:
            before = db.read(f"SELECT * FROM nails WHERE id = {args[0]}")
            db.delete(f"DELETE FROM nails WHERE id = {args[0]}")
        await ctx.send(f'{before}\nDeletado com sucesso.')

    @commands.command(name="nailstoday")
    async def nailtoday(self, ctx):
        dump = ""
        with databaseConnection(config("hostMydb")) as db:
            allnails = db.read("SELECT * FROM nails WHERE DATE(dt) = CURRENT_DATE")
        print(allnails)
        for i in allnails:
            dump += f"{i[0]}, {i[1]}, {i[2]}\n"
        await ctx.send(f"```{dump}```")

async def setup(bot):
    await bot.add_cog(work(bot))
