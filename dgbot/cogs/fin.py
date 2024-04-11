import discord
from discord.ext import commands

from ext.database import session
from models import Atv

from bs4 import BeautifulSoup
import requests


class atv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="atv")
    async def atv(self, ctx, *args):
        def bs(url):
            return BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}).content, 'html.parser')

        arv = rv = arf = rf = afi = fi = aab = ab = aai = ai = acr = cr = ct = dv = dy = yc = tl = ac = 0
        for i in session.query(Atv).order_by(Atv.id):
            if i.tp == 'rf':
                pr = i.pa/i.qt
                arf += i.pm*i.qt
                rf += i.pa
                pa = i.pa
                pa = dp = yp = pl = vr = ''
            else:
                ct += 1
                st = bs(f"https://statusinvest.com.br/{i.tp}/{i.nm}")
                pr = float((st.find_all('strong',class_='value')[0].text).replace('.','').replace(',','.'))
                if i.tp == 'fundos-imobiliarios':
                    dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                    dp = f"{'%.2f' %((dv/pr)*100)}%"
                    yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                    vr = st.find_all('strong',class_='value')[6].text
                    afi += i.pm*i.qt
                    fi += pr*i.qt
                    pl = ''
                if i.tp == 'acoes':
                    dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                    dp = f"{'%.2f' %((dv/pr)*100)}%"
                    yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                    pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                    vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                    aab += i.pm*i.qt
                    ab += pr*i.qt
                if i.tp == 'etfs':
                    dp = yp = pl = vr = ''
                    aai += i.pm*i.qt
                    ai += pr*i.qt
                if i.tp == 'bdrs':
                    pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                    vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                    dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                    dp = f"{'%.2f' %((dv/pr)*100)}%"
                    yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                    aai += i.pm*i.qt
                    ai += pr*i.qt
                if i.tp == 'criptomoedas':
                    i.pm = pr
                    acr += pr*i.qt 
                    cr += pr*i.qt
                    pa = dp = yp = pl = vr = ''
                arv += i.pm*i.qt
                rv += pr*i.qt
            dy += (dv/pr)*100
            yc += (dv/i.pm)*100
            tl += pr*i.qt
            ac += i.pm*i.qt
            await ctx.send(f"`{i.id}\t{i.nm.upper()}\t{'%.2f' %(((pr-i.pm)/i.pm)*100)}%\t{'%.0f' %(pr)}\t{'%.0f' %(i.pm)}\t{i.rc}\t{pa}\t{'%.0f' %(i.qt)}\t{dp}\t{yp}\t{pl}\t{vr}\t{'%.0f' %(pr*i.qt)}\t{'%.0f' %(i.pm*i.qt)}`")
            dv = pl = vr = dp = yp = 0
        await ctx.send(f"`rf: {'%.2f' %(tl*0.50)}\tfi: {'%.2f' %(tl*0.20)}\taç: {'%.2f' %(tl*0.15)}\tai: {'%.2f' %(tl*0.10)}\tcr: {'%.2f' %(tl*0.05)}\nrf: {'%.2f' %(arf)}\tfi: {'%.2f' %(afi)}\taç: {'%.2f' %(aab)}\tai: {'%.2f' %(aai)}\tcr: {'%.2f' %(acr)}\tdy: {'%.2f' %(dy/ct)}\trv: {'%.2f' %(arv)}\tac: {'%.2f' %(ac)}\nrf: {'%.2f' %(rf)}\tfi: {'%.2f' %(fi)}\taç: {'%.2f' %(ab)}\tai: {'%.2f' %(ai)}\tcr: {'%.2f' %(cr)}\tyc: {'%.2f' %(yc/ct)}\trv: {'%.2f' %(rv)}\ttl: {'%.2f' %(tl)}`")

    @commands.command(name="atvinsert")
    async def insert(self, ctx, *args):
        session.add(Atv(id=args[0],tp=args[1],nm=args[2],pm=args[3],qt=args[4],rc=args[5],pa=args[6]))
        session.commit()
        await ctx.send('Feito!')

    @commands.command(name="atvreplace")
    async def replace(self, ctx, *args):
        session.query(Atv).filter(Atv.id == args[0]).update({args[1]:args[2].replace(',','.')})
        session.commit()
        await ctx.send('Feito!')

    @commands.command(name="atvdelete")
    async def delete(self, ctx, *args):
        session.query(Atv).filter(Atv.id == args[0]).delete()
        session.commit()
        await ctx.send('Feito!')

async def setup(bot):
    await bot.add_cog(atv(bot))
