import discord
from discord.ext import commands

from ext.database import Session
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
            with Session() as session:
                for i in session.query(Atv).order_by(Atv.id):
                    if i.cl == 'rf':
                        pass
                    else:
                        st = bs(f"https://statusinvest.com.br/{i.cl}/{i.nm}")
                        session.query(Atv).filter(Atv.id == i.id).update({"pr":f"{float((st.find_all('strong',class_='value')[0].text).replace('.','').replace(',','.'))}"})
                        if i.cl == 'fundos-imobiliarios':
                            session.query(Atv).filter(Atv.id == i.id).update({
                                "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                                "vp":f"{float(st.find_all('strong',class_='value')[6].text.replace(',','.'))}"
                            })
                        if i.cl == 'acoes' or i.cl == 'bdrs':
                            session.query(Atv).filter(Atv.id == i.id).update({
                                "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                                "pl":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',','.'))}",
                                "vp":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',','.'))}"
                            })
                        session.commit()
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
                if i.cl == "rf":
                    dump += f"{i.id:<5}{i.nm.upper():<9}{('%.2f' %(((i.pr-i.pm)/i.pm)*100)):<9}{i.pr:<9}{i.pm:<9}{i.qt:<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i.pr*i.qt):<10}{'%.2f' %(i.pm*i.qt)}\n"
                    tc += i.pr*i.qt
                    ta += i.pm*i.qt
            ttc += tc
            tta += ta
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'-dv%-':<9}{'-yc%-':<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            typ = tdp = tct = ct = dv = dp = yp = tc = ta = 0
            dump = ""
            for i in active:
                if i.cl == "fundos-imobiliarios":
                    dump += f"{i.id:<5}{i.nm.upper():<9}{('%.2f' %(((i.pr-i.pm)/i.pm)*100)):<9}{i.pr:<9}{i.pm:<9}{'%.0f' %(i.qt):<9}{'%.2f' %(i.dv):<9}{'%.2f' %((i.dv/i.pr)*100):<9}{'%.2f' %((i.dv/i.pm)*100):<9}{'':<9}{i.vp:<9}{'%.2f' %(i.pr*i.qt):<10}{'%.2f' %(i.pm*i.qt)}\n"
                    tc += i.pr*i.qt
                    ta += i.pm*i.qt
                    dv += i.dv
                    dp += (i.dv/i.pr)*100
                    yp += (i.dv/i.pm)*100
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
                if i.cl == "acoes":
                    dump += f"{i.id:<5}{i.nm.upper():<9}{'%.2f' %(((i.pr-i.pm)/i.pm)*100):<9}{i.pr:<9}{i.pm:<9}{'%.0f' %(i.qt):<9}{'%.2f' %(i.dv):<9}{'%.2f' %((i.dv/i.pr)*100):<9}{'%.2f' %((i.dv/i.pm)*100):<9}{i.pl:<9}{i.vp:<9}{'%.2f' %(i.pr*i.qt):<10}{'%.2f' %(i.pm*i.qt)}\n"
                    tc += i.pr*i.qt
                    ta += i.pm*i.qt
                    dv += i.dv
                    dp += (i.dv/i.pr)*100
                    yp += (i.dv/i.pm)*100
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
                if i.cl == "etfs" or i.cl == "bdrs":
                    dump += f"{i.id:<5}{i.nm.upper():<9}{'%.2f' %(((i.pr-i.pm)/i.pm)*100):<9}{i.pr:<9}{i.pm:<9}{'%.0f' %(i.qt):<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i.pr*i.qt):<10}{'%.2f' %(i.pm*i.qt)}\n"
                    tc += i.pr*i.qt
                    ta += i.pm*i.qt
            ttc += tc
            tta += ta
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'-dv%-':<9}{'-yc%-':<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            tc = ta = 0
            for i in active:
                if i.cl == "criptomoedas":
                    dump += f"{i.id:<5}{i.nm.upper():<9}{'%.2f' %(((i.pr-i.pr)/i.pm)*100):<9}{i.pr:<9}{'':<9}{'%.0f' %(i.qt):<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i.pr*i.qt):<10}{''}\n"
                    tc += i.pr*i.qt
                    ta += i.pm*i.qt
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
