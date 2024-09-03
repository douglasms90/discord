import discord
from discord.ext import commands

from ext.database import session
from ext.webscraping import bs
from models import Atv

from bs4 import BeautifulSoup
import requests


class atv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="atvsync")
    async def atvsync(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
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
                    if i.cl == 'acoes':
                        session.query(Atv).filter(Atv.id == i.id).update({
                            "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                            "pl":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',','.'))}",
                            "vp":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',','.'))}"
                        })
                    if i.cl == 'bdrs':
                        session.query(Atv).filter(Atv.id == i.id).update({
                            "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                            "pl":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',','.'))}",
                            "vp":f"{float(st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',','.'))}"
                        })
                    session.commit()
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvdump")
    async def atvdump(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            dump = ""
            tc = ta = 0
            for i in session.query(Atv).filter(Atv.id.like(f"{1}%")).order_by(Atv.id):
                dump += f"{i.id:<5}{i.nm.upper():<9}{('%.2f' %(((i.pr-i.pm)/i.pm)*100)):<9}{i.pr:<9}{i.pm:<9}{i.qt:<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i.pr*i.qt):<9}{'%.2f' %(i.pm*i.qt)}\n"
                tc += i.pr*i.qt
                ta += i.pm*i.qt
            dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'-dv%-':<9}{'-yc%-':<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<9}{'%.2f' %(ta)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            for i in session.query(Atv).filter(Atv.id.like(f"{2}%")).order_by(Atv.id):
                dump += f"{i.id:<5}{i.nm.upper():<9}{('%.2f' %(((i.pr-i.pm)/i.pm)*100)):<9}{i.pr:<9}{i.pm:<9}{'%.0f' %(i.qt):<9}{'%.2f' %(i.dv):<9}{'%.2f' %((i.dv/i.pr)*100):<9}{'%.2f' %((i.dv/i.pm)*100):<9}{'':<9}{i.vp:<9}{'%.2f' %(i.pr*i.qt):<9}{'%.2f' %(i.pm*i.qt)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            for i in session.query(Atv).filter(Atv.id.like(f"{3}%")).order_by(Atv.id):
                dump += f"{i.id:<5}{i.nm.upper():<9}{'%.2f' %(((i.pr-i.pm)/i.pm)*100):<9}{i.pr:<9}{i.pm:<9}{'%.0f' %(i.qt):<9}{'%.2f' %(i.dv):<9}{'%.2f' %((i.dv/i.pr)*100):<9}{'%.2f' %((i.dv/i.pm)*100):<9}{i.pl:<9}{i.vp:<9}{'%.2f' %(i.pr*i.qt):<9}{'%.2f' %(i.pm*i.qt)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            for i in session.query(Atv).filter(Atv.id.like(f"{4}%")).order_by(Atv.id):
                dump += f"{i.id:<5}{i.nm.upper():<9}{'%.2f' %(((i.pr-i.pm)/i.pm)*100):<9}{i.pr:<9}{i.pm:<9}{'%.0f' %(i.qt):<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i.pr*i.qt):<9}{'%.2f' %(i.pm*i.qt)}\n"
            await ctx.send(f"```{dump}```")
            dump = ""
            for i in session.query(Atv).filter(Atv.id.like(f"{5}%")).order_by(Atv.id):
                dump += f"{i.id:<5}{i.nm.upper():<9}{'%.2f' %(((i.pr-i.pr)/i.pm)*100):<9}{i.pr:<9}{'':<9}{'%.0f' %(i.qt):<9}{'':<9}{'':<9}{'':<9}{'':<9}{'':<9}{'%.2f' %(i.pr*i.qt):<9}{''}\n"
            await ctx.send(f"```{dump}```")
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvinsert")
    async def insert(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            session.add(Atv(id=args[0],tp=args[1],nm=args[2],pm=args[3],qt=args[4],rc=args[5],pa=args[6]))
            session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvreplace")
    async def replace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            session.query(Atv).filter(Atv.id == args[0]).update({args[1]:args[2].replace(',','.')})
            session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atvdelete")
    async def delete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            session.query(Atv).filter(Atv.id == args[0]).delete()
            session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

async def setup(bot):
    await bot.add_cog(atv(bot))
