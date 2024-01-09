import discord
from discord.ext import commands

from ext.database import session
from models import Atv

from bs4 import BeautifulSoup
import requests

class fin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fin")
    async def fin(self, ctx, *args):
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

            print(f"{i.id}\t{i.nm.upper()}\t{'%.2f' %(((pr-i.pm)/i.pm)*100)}%\t{'%.0f' %(pr)}\t{i.rc} {pa}\t{dp}\t{yp}\t{pl}\t{vr}\t{'%.0f' %(pr*i.qt)}\t{'%.0f' %(i.pm*i.qt)}")
            dv = pl = vr = dp = yp = 0
        print(f"fi: {'%.2f' %(afi)}\taç: {'%.2f' %(aab)}\tai: {'%.2f' %(aai)}\tcr: {'%.2f' %(acr)}\tac: {'%.2f' %(ac)}")
        print(f"fi: {'%.2f' %(fi)}\taç: {'%.2f' %(ab)}\tai: {'%.2f' %(ai)}\tcr: {'%.2f' %(cr)}\ttl: {'%.2f' %(tl)}")
        print(f"dy: {'%.2f' %(dy/ct)}\trf: {'%.2f' %(arf)}\trv: {'%.2f' %(arv)}")
        print(f"yc: {'%.2f' %(yc/ct)}\trf: {'%.2f' %(rf)}\trv: {'%.2f' %(rv)}")
        await ctx.send('Pronto!')

    @commands.command(name="replaceatv")
    async def replace(self, ctx, *args):
        session.query(Atv).filter(Atv.id == args[0]).update({args[1]:args[2]})
        session.commit()
        await ctx.send('Pronto!')

async def setup(bot):
    await bot.add_cog(fin(bot))
