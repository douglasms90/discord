import discord
from discord.ext import commands

from ext.database import session
from models import Act, Vln
from datetime import datetime

from bs4 import BeautifulSoup
import requests

class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="today")
    async def today(self, ctx):
        for obj in session.query(Act).filter(Act.dt.like(f'{datetime.now().date()}%')):
            embed = discord.Embed(title=obj.olt,description=obj.tfc)
            embed.set_author(name=obj.usr)
            embed.add_field(name='', value=f'!ativa_onu_vlan {obj.sn} {obj.vln} {obj.ctr} {obj.cto}', inline=True)
            embed.set_footer(text=obj.id)
            await ctx.send(embed = embed)

    @commands.command(name="replace")
    async def replace(self, ctx, *args):
        session.query(Act).filter(Act.id == args[0]).update({args[1]:args[2]})
        session.commit()
        
        for obj in session.query(Act).filter(Act.id == args[0]):
            embed = discord.Embed(title=obj.olt,description=obj.tfc)
            embed.set_author(name=obj.usr)
            embed.add_field(name='Comando:', value=f'!ativa_onu_vlan {obj.sn} {obj.vln} {obj.ctr} {obj.cto}', inline=True)
            embed.set_footer(text=obj.id)
            await ctx.send(embed = embed)

    @commands.command(name="act")
    async def act(self, ctx, *args):
        now=datetime.now()
        session.add(Act(dt=now,usr=ctx.author.name,olt=args[1],tfc=args[4],sn=args[-3],vln=session.query(Vln.vln).filter(Vln.olt == args[1], Vln.tfc == args[4]),ctr=args[-2],cto=args[-1]))
        session.commit()
        
        for obj in session.query(Act).filter(Act.dt == now):
            embed = discord.Embed(title=obj.olt,description=obj.tfc)
            embed.set_author(name=obj.usr)
            embed.add_field(name='Comando:', value=f'!ativa_onu_vlan {obj.sn} {obj.vln} {obj.ctr} {obj.cto}', inline=True)
            embed.set_footer(text=obj.id)
            await ctx.send(embed = embed)

    @commands.command(name="fin")
    async def fin(self, ctx, *args):
        tt = 134280.65
        data=[
            {'tp':'rf',                 	'nm':'inv',     'pm':79.18,     'qt':1,         'rc':'',    'pa':79.68      }, #1
            {'tp':'rf',                 	'nm':'tdi',     'pm':100,       'qt':220,       'rc':'',    'pa':22441.26   }, #2
            {'tp':'rf',	                	'nm':'slc 29',  'pm':12874.14,  'qt':1.31,      'rc':'',    'pa':18520.63   }, #3 01/03/2029
            {'tp':'rf',	                	'nm':'lci',     'pm':1000,      'qt':20,        'rc':'',    'pa':20980.40   }, #4 08/05/2023 > 08/05/2024
            {'tp':'rf',	                	'nm':'cdb',     'pm':1000,      'qt':10,        'rc':'',    'pa':12104.96   }, #5 05/08/2022 > 05/08/2024
            {'tp':'rf',	                	'nm':'pre 25',  'pm':738.14,    'qt':3.38,      'rc':'',    'pa':3068.36    }, #6 14/04/2022 > 01/01/2025
            {'tp':'rf',	                	'nm':'inf 26',  'pm':3146.81,   'qt':0.79,      'rc':'',    'pa':2880.60    }, #7 26/04/2022 > 15/08/2026
            {'tp':'fundos-imobiliarios',	'nm':'irdm11',  'pm':109.30,	'qt':35,        'rc':'N',   'pa':87         }, #8   1
            {'tp':'fundos-imobiliarios',	'nm':'mcci11',  'pm':98.47, 	'qt':15,        'rc':'',    'pa':94         }, #9   2
            {'tp':'fundos-imobiliarios',	'nm':'recr11',  'pm':95.64, 	'qt':18,        'rc':'N',   'pa':94         }, #10  3
            {'tp':'fundos-imobiliarios',	'nm':'vgip11',  'pm':89.33, 	'qt':15,        'rc':'',    'pa':0          }, #11  4
            {'tp':'fundos-imobiliarios',	'nm':'btlg11',  'pm':102.39,	'qt':17,        'rc':'',    'pa':113        }, #12  5
            {'tp':'fundos-imobiliarios',	'nm':'bcff11',  'pm':7.99,  	'qt':112,       'rc':'N',   'pa':78         }, #13  6
            {'tp':'fundos-imobiliarios',	'nm':'hgru11',  'pm':127.04,	'qt':27,        'rc':'',    'pa':136        }, #14  7
            {'tp':'fundos-imobiliarios',	'nm':'mall11',  'pm':91.66, 	'qt':14,        'rc':'N',   'pa':116        }, #15  8
            {'tp':'fundos-imobiliarios',	'nm':'pvbi11',  'pm':91.79, 	'qt':4,         'rc':'N',   'pa':106        }, #16  9
            {'tp':'fundos-imobiliarios',	'nm':'rbrp11',  'pm':87.01, 	'qt':43,        'rc':'N',   'pa':74         }, #17  10
            {'tp':'fundos-imobiliarios',	'nm':'vilg11',  'pm':119.28,	'qt':30,        'rc':'N',   'pa':127        }, #18  11
            {'tp':'fundos-imobiliarios',	'nm':'vino11',  'pm':11.91, 	'qt':205,       'rc':'',    'pa':0          }, #19  12
            {'tp':'acoes',              	'nm':'bbse3',   'pm':21.22, 	'qt':65,        'rc':'N',   'pa':34         }, #20  13
            {'tp':'acoes',	        	'nm':'b3sA3',   'pm':13.84, 	'qt':135,       'rc':'N',   'pa':15         }, #21  14
            {'tp':'acoes',	        	'nm':'eztc3',   'pm':16.95, 	'qt':75,        'rc':'N',   'pa':22         }, #22  15
            {'tp':'acoes',	        	'nm':'flry3',   'pm':27.08, 	'qt':84,        'rc':'N',   'pa':19         }, #23  16
            {'tp':'acoes',	        	'nm':'itsa4',   'pm':8.78,  	'qt':231,       'rc':'',    'pa':0          }, #24  17
            {'tp':'acoes',	        	'nm':'mypk3',   'pm':13.08, 	'qt':133,       'rc':'N',   'pa':15         }, #25  18
            {'tp':'acoes',	        	'nm':'sapr4',   'pm':4.09,  	'qt':423,       'rc':'N',   'pa':26         }, #26  19
            {'tp':'acoes',	        	'nm':'vale3',   'pm':69.33, 	'qt':18,        'rc':'N',   'pa':73         }, #27  20
            {'tp':'acoes',	        	'nm':'vbbr3',   'pm':24.74, 	'qt':83,        'rc':'',    'pa':0          }, #28  21
            {'tp':'acoes',	        	'nm':'vivt3',   'pm':44.79, 	'qt':33,        'rc':'N',   'pa':54         }, #29  22
            {'tp':'acoes',	        	'nm':'wege3',   'pm':19.52, 	'qt':66,        'rc':'N',   'pa':40         }, #30  23
            {'tp':'etfs',	        	'nm':'ivvb11',  'pm':231.95,	'qt':14,        'rc':'',    'pa':0          }, #31  24
            {'tp':'bdrs',	        	'nm':'baba34',  'pm':17.37,     'qt':80,        'rc':'',    'pa':23         }, #32  25
            {'tp':'bdrs',	        	'nm':'disb34',  'pm':37.27, 	'qt':33,        'rc':'',    'pa':34         }, #33  26
            {'tp':'criptomoedas',		'nm':'btc',	'pm':1,         'qt':0.01257466,'rc':'',    'pa':0          }, #34  27
            {'tp':'criptomoedas',		'nm':'beth',    'pm':1,         'qt':0.18710108,'rc':'',    'pa':0          }, #35  28
        ]

        def bs(url):
            return BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}).content, 'html.parser')

        arv = rv = arf = rf = afi = fi = aab = ab = aai = ai = acr = cr = ct = dv = dy = yc = tl = ac = 0

        for i in data:
            pm = i['pm']
            pa = i['pa']
            if i['tp'] == 'rf':
                pr = pa/i['qt']
                arf += pm*i['qt']
                rf += pa
                pa = dp = yp = pl = vr = ''
            else:
                ct += 1
                st = bs(f"https://statusinvest.com.br/{i['tp']}/{i['nm']}")
                pr = float((st.find_all('strong',class_='value')[0].text).replace('.','').replace(',','.'))
                if i['tp'] == 'fundos-imobiliarios':
                    dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                    dp = f"{'%.2f' %((dv/pr)*100)}%"
                    yp = f"{'%.2f' %((dv/pm)*100)}%"
                    vr = st.find_all('strong',class_='value')[6].text
                    afi += pm*i['qt']
                    fi += pr*i['qt']
                    pl = ''
                if i['tp'] == 'acoes':
                    dv = float((st.find_all('span',class_='sub-value')[3].text)[3:].replace(',','.'))
                    dp = f"{'%.2f' %((dv/pr)*100)}%"
                    yp = f"{'%.2f' %((dv/pm)*100)}%"
                    pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                    vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                    aab += pm*i['qt']
                    ab += pr*i['qt']
                if i['tp'] == 'etfs':
                    dp = yp = pl = vr = ''
                    aai += pm*i['qt']
                    ai += pr*i['qt']
                if i['tp'] == 'bdrs':
                    pl = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[1].text
                    vr = st.find_all('strong',class_='value d-block lh-4 fs-4 fw-700')[3].text
                    aai += pm*i['qt']
                    ai += pr*i['qt']
                    dp = yp = ''
                if i['tp'] == 'criptomoedas':
                    pm = pr
                    acr += pr*i['qt'] 
                    cr += pr*i['qt']
                    pa = dp = yp = pl = vr = ''
                arv += pm*i['qt']
                rv += pr*i['qt']

            dy += (dv/pr)*100
            yc += (dv/pm)*100
            tl += pr*i['qt']
            ac += pm*i['qt']

            print(f"{i['nm'].upper()}\t{'%.2f' %(((pr-pm)/pm)*100)}%\t{'%.0f' %(pr)}\t{i['rc']} {pa}\t{dp}\t{yp}\t{pl}\t{vr}\t{'%.2f' %(((pr*i['qt'])/tt)*100)}%\t{'%.2f' %(((pm*i['qt'])/tt)*100)}%")
            dv = pl = vr = dp = yp = 0
        print(f"fi: {'%.2f' %(afi)}\taç: {'%.2f' %(aab)}\tai: {'%.2f' %(aai)}\tcr: {'%.2f' %(acr)}\tac: {'%.2f' %(ac)}")
        print(f"fi: {'%.2f' %(fi)}\taç: {'%.2f' %(ab)}\tai: {'%.2f' %(ai)}\tcr: {'%.2f' %(cr)}\ttl: {'%.2f' %(tl)}")
        print(f"dy: {'%.2f' %(dy/ct)}\trf: {'%.2f' %(arf)}\trv: {'%.2f' %(arv)}")
        print(f"yc: {'%.2f' %(yc/ct)}\trf: {'%.2f' %(rf)}\trv: {'%.2f' %(rv)}")
        await ctx.send('Feito')

async def setup(bot):
    await bot.add_cog(work(bot))
