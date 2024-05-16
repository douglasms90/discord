import discord
from discord.ext import commands
from ext.database import session
from ext.webscraping import bs
from models import Atv
from bs4 import BeautifulSoup
import requests


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="testatv")
    async def testatv(self, ctx, *args):
        if ctx.author.id == 269592803602989058:
            arv = rv = arf = rf = afi = fi = aab = ab = aai = ai = acr = cr = ct = dv = dy = yc = tl = ac = 0
            for i in session.query(Atv).order_by(Atv.id):
                if i.tp == 'rf':
                    pr = i.pa/i.qt
                    rf += i.pa
                    pa = i.pa
                    arf += i.pm*i.qt
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
                        fi += pr*i.qt
                        afi += i.pm*i.qt
                        pl = ''
                    if i.tp == 'acoes':
                        dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                        dp = f"{'%.2f' %((dv/pr)*100)}%"
                        yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                        pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                        vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                        ab += pr*i.qt
                        aab += i.pm*i.qt
                    if i.tp == 'etfs':
                        dp = yp = pl = vr = ''
                        ai += pr*i.qt
                        aai += i.pm*i.qt
                    if i.tp == 'bdrs':
                        pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                        vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                        dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                        dp = f"{'%.2f' %((dv/pr)*100)}%"
                        yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                        ai += pr*i.qt
                        aai += i.pm*i.qt
                    if i.tp == 'criptomoedas':
                        i.pm = pr
                        cr += pr*i.qt
                        acr += pr*i.qt 
                        pa = dp = yp = pl = vr = ''
                    rv += pr*i.qt
                    arv += i.pm*i.qt
                dy += (dv/pr)*100
                yc += (dv/i.pm)*100
                tl += pr*i.qt
                ac += i.pm*i.qt
                await ctx.send(f"`{i.id}\t{i.nm.upper()}\t{'%.2f' %(((pr-i.pm)/i.pm)*100)}%\t{'%.0f' %(pr)}\t{'%.0f' %(i.pm)}\t{i.rc}\t{pa}\t{'%.0f' %(i.qt)}\t{dp}\t{yp}\t{pl}\t{vr}\t{'%.0f' %(pr*i.qt)}\t{'%.0f' %(i.pm*i.qt)}`")
                dv = pl = vr = dp = yp = 0
            await ctx.send(f"`rf: {'%.2f' %(arf)}\tfi: {'%.2f' %(afi)}\taç: {'%.2f' %(aab)}\tai: {'%.2f' %(aai)}\tcr: {'%.2f' %(acr)}\tdy: {'%.2f' %(dy/ct)}\trv: {'%.2f' %(arv)}\tac: {'%.2f' %(ac)}\nrf: {'%.2f' %(rf)}\tfi: {'%.2f' %(fi)}\taç: {'%.2f' %(ab)}\tai: {'%.2f' %(ai)}\tcr: {'%.2f' %(cr)}\tyc: {'%.2f' %(yc/ct)}\trv: {'%.2f' %(rv)}\ttl: {'%.2f' %(tl)}`")
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

async def setup(bot):
    await bot.add_cog(test(bot))
