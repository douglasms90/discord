import discord
from discord.ext import commands

from ext.database import Session, databaseConnection
from ext.webscraping import bs
from models import Atv

from bs4 import BeautifulSoup
import requests

class atv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="atv")
    async def atv(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("hostMydb")) as db:
                allatv = db.read(f"SELECT * FROM atv")
                for i in allatv:
                    if i[1] == 'rf':
                        pass
                    else:
                        st = bs(f"https://statusinvest.com.br/{i[1]}/{i[2]}")
                        db.update(f"UPDATE atv SET pr = {float((st.find_all('strong',class_='value')[0].text).replace('.','').replace(',','.'))} WHERE id = {i[0]}")
                        if i[1] == 'fundos-imobiliarios':
                            db.update(f"UPDATE atv SET dv = {float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}, vp = {float(st.find_all('strong',class_='value')[6].text.replace(',','.'))} WHERE id = {i[0]}")
                        if i[1] == 'acoes' or i[1] == 'bdrs':
                            session.query(Atv).filter(Atv.id == i[0]).update({
                                "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                                "pl":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',','.'))}",
                                "vp":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',','.'))}"
                            })
#       else:
#           await ctx.send(f"{ctx.author} você não tem autorização")

#   @commands.command(name="atv")
#   async def atvdump(self, ctx, *args):
#       if ctx.author.id in [269592803602989058]:  D
            with Session() as session:
                active = session.query(Atv).all()
            dump = ""
            tta = ttc = tc = ta = 0
            for i in active:
                if i[1] == "rf":
                    dump += f"{i[0]:<5}{i[2].upper():<9}{('%.2f' %(((i[3]-i[4])/i[4])*100)):<9}{i[3]:<9}{i[4]:<9}{i[5]:<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i[3]*i[5]):<10}{'%.2f' %(i[4]*i[5])}\n"
                    tc += i[3]*i[5]
                    ta += i[4]*i[5]
            ttc += tc
            tta += ta
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'-dv%-':<9}{'-yc%-':<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            typ = tdp = tct = ct = dv = dp = yp = tc = ta = 0
            dump = ""
            for i in active:
                if i[1] == "fundos-imobiliarios":
                    dump += f"{i[0]:<5}{i[2].upper():<9}{('%.2f' %(((i[3]-i[4])/i[4])*100)):<9}{i[3]:<9}{i[4]:<9}{'%.0f' %(i[5]):<9}{'%.2f' %(i.dv):<9}{'%.2f' %((i.dv/i[3])*100):<9}{'%.2f' %((i.dv/i[4])*100):<9}{'':<9}{i.vp:<9}{'%.2f' %(i[3]*i[5]):<10}{'%.2f' %(i[4]*i[5])}\n"
                    tc += i[3]*i[5]
                    ta += i[4]*i[5]
                    dv += i.dv
                    dp += (i.dv/i[3])*100
                    yp += (i.dv/i[4])*100
                    ct += 1
            tct += ct
            tdp += dp
            typ += yp
            ttc += tc
            tta += ta
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'%.2f' %(dv):<9}{'%.2f' %(dp/ct):<9}{'%.2f' %(yp/ct):<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            ct = dv = dp = yp = tc = ta = 0
            for i in active:
                if i[1] == "acoes":
                    dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(((i[3]-i[4])/i[4])*100):<9}{i[3]:<9}{i[4]:<9}{'%.0f' %(i[5]):<9}{'%.2f' %(i.dv):<9}{'%.2f' %((i.dv/i[3])*100):<9}{'%.2f' %((i.dv/i[4])*100):<9}{i.pl:<9}{i.vp:<9}{'%.2f' %(i[3]*i[5]):<10}{'%.2f' %(i[4]*i[5])}\n"
                    tc += i[3]*i[5]
                    ta += i[4]*i[5]
                    dv += i.dv
                    dp += (i.dv/i[3])*100
                    yp += (i.dv/i[4])*100
                    ct += 1
            tdp += dp
            typ += yp
            ttc += tc
            tta += ta
            tct += ct
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'%.2f' %(dv):<9}{'%.2f' %(dp/ct):<9}{'%.2f' %(yp/ct):<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            tc = ta = 0
            for i in active:
                if i[1] == "etfs" or i[1] == "bdrs":
                    dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(((i[3]-i[4])/i[4])*100):<9}{i[3]:<9}{i[4]:<9}{'%.0f' %(i[5]):<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i[3]*i[5]):<10}{'%.2f' %(i[4]*i[5])}\n"
                    tc += i[3]*i[5]
                    ta += i[4]*i[5]
            ttc += tc
            tta += ta
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'-dv%-':<9}{'-yc%-':<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            tc = ta = 0
            for i in active:
                if i[1] == "criptomoedas":
                    dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(((i[3]-i[3])/i[4])*100):<9}{i[3]:<9}{'':<9}{'%.0f' %(i[5]):<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i[3]*i[5]):<10}{''}\n"
                    tc += i[3]*i[5]
                    ta += i[4]*i[5]
            ttc += tc
            tta += ta
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'-dv%-':<9}{'-yc%-':<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{''}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'%.2f' %(tdp/tct):<9}{'%.2f' %(typ/tct):<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(ttc):<10}{'%.2f' %(tta)}\n"
            await ctx.send(f"```{dump}```")
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvinsert")
    async def insert(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                session.add(Atv(id=args[0],tp=args[1],nm=args[2],pm=args[3],qt=args[4],rc=args[5],pa=args[6]))
                session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvreplace")
    async def replace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                session.query(Atv).filter(Atv.id == args[0]).update({args[1]:args[2].replace(',','.')})
                session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    #@commands.command(name="atvreplace")
    #async def replace(self, ctx, *args):
    #    if ctx.author.id in [269592803602989058]: # D
    #        with databaseConnection(config("hostMydb")) as db:
    #            before = db.read(f"SELECT * FROM atv WHERE id = %s", (args[0],))
    #            db.update(f"UPDATE atv SET {args[1]} = %s WHERE id = %s", (args[2].replace(',', '.'), args[0]))
    #            after = db.read(f"SELECT * FROM atv WHERE id = %s", (args[0],))
    #        await ctx.send(f"Update bem sucedido;\nAnteriormente: {before}\nPosteriormente: {after}")
    #    else:
    #        await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvdelete")
    async def delete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                session.query(Atv).filter(Atv.id == args[0]).delete()
                session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

async def setup(bot):
    await bot.add_cog(atv(bot))
