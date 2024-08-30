import discord
from discord.ext import commands

from ext.database import session
from ext.webscraping import bs
from models import Atv, Test

from bs4 import BeautifulSoup
import requests


class atv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="atvsync")
    async def atvsync(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            for i in session.query(Test).order_by(Test.id):
                if i.cl == 'rf':
                    pass
                else:
                    st = bs(f"https://statusinvest.com.br/{i.cl}/{i.nm}")
                    session.query(Test).filter(Test.id == i.id).update({"pr":f"{float((st.find_all('strong',class_='value')[0].text).replace('.','').replace(',','.'))}"})
                    if i.cl == 'fundos-imobiliarios':
                        session.query(Test).filter(Test.id == i.id).update({
                            "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                            "vp":f"{st.find_all('strong',class_='value')[6].text.replace(',','.')}"
                        })
                    if i.cl == 'acoes':
                        session.query(Test).filter(Test.id == i.id).update({
                            "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                            "pl":f"{st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',','.')}",
                            "vp":f"{st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',','.')}"
                        })
                    if i.cl == 'bdrs':
                        session.query(Test).filter(Test.id == i.id).update({
                            "dv":f"{float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))}",
                            "pl":f"{st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',','.')}",
                            "vp":f"{st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',','.')}"
                        })
                    session.commit()
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="atv")
    async def atv(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            lv = rv = lf = rf = li = fi = la = ab = lu = ai = lc = cr = ct = dv = dy = yc = tl = ac = 0
            for i in session.query(Atv).order_by(Atv.id):
                if i.tp == 'rf':
                    pr = i.pa/i.qt
                    rf += i.pa
                    pa = i.pa
                    lf += i.pm*i.qt # all rf
                    pa = dp = yp = pl = vr = ''
                else:
                    st = bs(f"https://statusinvest.com.br/{i.tp}/{i.nm}")
                    pr = float((st.find_all('strong',class_='value')[0].text).replace('.','').replace(',','.'))
                    if i.tp == 'tesouro':
                        rf += i.pa
                        pa = i.pa
                        lf += i.pm*i.qt # all rf
                        pa = dp = yp = pl = vr = ''
                    else:
                        ct += 1
                        if i.tp == 'fundos-imobiliarios':
                            dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                            dp = f"{'%.2f' %((dv/pr)*100)}%"
                            yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                            vr = st.find_all('strong',class_='value')[6].text
                            fi += pr*i.qt
                            li += i.pm*i.qt # all fi
                            pl = ''
                        if i.tp == 'acoes':
                            dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                            dp = f"{'%.2f' %((dv/pr)*100)}%"
                            yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                            pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                            vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                            ab += pr*i.qt
                            la += i.pm*i.qt # all aç
                        if i.tp == 'etfs':
                            ai += pr*i.qt
                            lu += i.pm*i.qt
                            dp = yp = pl = vr = ''
                        if i.tp == 'bdrs':
                            pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                            vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                            dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                            dp = f"{'%.2f' %((dv/pr)*100)}%"
                            yp = f"{'%.2f' %((dv/i.pm)*100)}%"
                            ai += pr*i.qt
                            lu += i.pm*i.qt # all ai
                        if i.tp == 'criptomoedas':
                            i.pm = pr
                            cr += pr*i.qt
                            lc += pr*i.qt # all cr
                            pa = dp = yp = pl = vr = ''
                        rv += pr*i.qt
                        lv += i.pm*i.qt
                dy += (dv/pr)*100
                yc += (dv/i.pm)*100
                tl += pr*i.qt
                ac += i.pm*i.qt
                session.commit()
                await ctx.send(f"`{i.id}\t{i.nm.upper().replace('TESOURO-SELIC-20','SLC-').replace('TESOURO-PREFIXADO-20','PRE-').replace('TESOURO-IPCA-20','IPCA')}\t{'%.2f' %(((pr-i.pm)/i.pm)*100)}%\t{'%.0f' %(pr)}\t{'%.0f' %(i.pm)}\t{i.rc}\t{pa}\t{'%.0f' %(i.qt)}\t{dp}\t{yp}\t{pl}\t{vr}\t{'%.0f' %(pr*i.qt)}\t{'%.0f' %(i.pm*i.qt)}`")
                dv = pl = vr = dp = yp = 0
            await ctx.author.send(f"`rf: {'%.2f' %(lf)}\tfi: {'%.2f' %(li)}\taç: {'%.2f' %(la)}\tai: {'%.2f' %(lu)}\tcr: {'%.2f' %(lc)}\tdy: {'%.2f' %(dy/ct)}\trv: {'%.2f' %(lv)}\tac: {'%.2f' %(ac)}\nrf: {'%.2f' %(rf)}\tfi: {'%.2f' %(fi)}\taç: {'%.2f' %(ab)}\tai: {'%.2f' %(ai)}\tcr: {'%.2f' %(cr)}\tyc: {'%.2f' %(yc/ct)}\trv: {'%.2f' %(rv)}\ttl: {'%.2f' %(tl)}`")
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
