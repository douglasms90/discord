import discord
from discord.ext import commands

from ext.database import databaseConnection
from ext.webscraping import bs
from decouple import config

import requests
import json

class fin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fire")
    async def fire(self, ctx):
        if ctx.author.id in [269592803602989058]:  # D

            # Post(Create)
            link = "https://database-11bec-default-rtdb.firebaseio.com/"
            dados = {
                "Act":[
                    {
                        "rf":[
                            {
                                "id":101,
                                "nm":"vsback",
                                "pr":0,
                                "pm":0,
                                "qt":0
                            },
                            {
                                "id":102,
                                "nm":"selic",
                                "pr":0,
                                "pm":0,
                                "qt":0
                            },
                            {
                                "id":103,
                                "nm":"lci-26",
                                "pr":0,
                                "pm":0,
                                "qt":0
                            },
                            {
                                "id":104,
                                "nm":"ipca26",
                                "pr":0,
                                "pm":0,
                                "qt":0
                            },
                            {
                                "id":105,
                                "nm":"lci-26",
                                "pr":0,
                                "pm":0,
                                "qt":0
                            },
                        ]
                    }
                ]
            }
            req = requests.post(f"{link}/discord/.json", data=json.dumps(dados))

            # Patch(Update)
            #dados = {'nome':'Douglas'}
            #id = '-OPHWlWesheJbcvFUuoN'
            #req = requests.patch(f"{link}/discord/tests/{id}/.json", data=json.dumps(dados))

            # Get(Read)
            req = requests.get(f'{link}/.json')
            print(req.text)

            await ctx.send("Pressione um dos botões:", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

    @commands.command(name="atv")
    async def atv(self, ctx):
        if ctx.author.id in [269592803602989058]:  # D
            view = discord.ui.View()
            
            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Sync")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Atv")
            button3 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Cot")
            button4 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Div")
            
            async def sync(interaction: discord.Interaction):
                await interaction.response.defer()
                
                with databaseConnection(config("hostMydb")) as db:
                    allatv = db.read("SELECT * FROM atv order by id asc", None)
                     
                    for i in allatv:
                        if i[1] == 'rf':
                            pass
                        else:
                            st = bs(f"https://statusinvest.com.br/{i[1]}/{i[2]}")
                            pr = float((st.find_all('strong', class_='value')[0].text).replace('.', '').replace(',', '.'))
                            db.update("UPDATE atv SET pr = %s WHERE id = %s", (pr, i[0]))
                            
                            if i[1] == 'fundos-imobiliarios':
                                dv = float((st.find_all('span', class_='sub-value')[3].text)[3:].replace(',', '.'))
                                vp = float(st.find_all('strong', class_='value')[6].text.replace(',', '.'))
                                db.update("UPDATE atv SET dv = %s, vp = %s WHERE id = %s", (dv, vp, i[0]))
                            
                            if i[1] == 'acoes': #or i[1] == 'bdrs':
                                dv = float((st.find_all('span', class_='sub-value')[3].text)[3:].replace(',', '.'))
                                pl = float(st.find_all('strong', class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',', '.'))
                                vp = float(st.find_all('strong', class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',', '.'))
                                db.update("UPDATE atv SET dv = %s, pl = %s, vp = %s WHERE id = %s", (dv, pl, vp, i[0]))
                
                await interaction.followup.send("Sync ok", ephemeral=True)
            
            async def atv(interaction: discord.Interaction):
                await interaction.response.defer()
                with databaseConnection(config("hostMydb")) as db:
                    active = db.read("SELECT * FROM atv ORDER BY id asc", None)
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
                await ctx.send(f"```{dump}```", delete_after=1800)
                typ = tdp = tct = ct = dv = dp = yp = tc = ta = 0
                dump = ""
                for i in active:
                    if i[1] == "fundos-imobiliarios":
                        dump += f"{i[0]:<5}{i[2].upper():<9}{('%.2f' %(((i[3]-i[4])/i[4])*100)):<9}{i[3]:<9}{i[4]:<9}{'%.0f' %(i[5]):<9}{'%.2f' %(i[6]):<9}{'%.2f' %((i[6]/i[3])*100):<9}{'%.2f' %((i[6]/i[4])*100):<9}{'':<9}{i[8]:<9}{'%.2f' %(i[3]*i[5]):<10}{'%.2f' %(i[4]*i[5])}\n"
                        tc += i[3]*i[5]
                        ta += i[4]*i[5]
                        dv += i[6]
                        dp += (i[6]/i[3])*100
                        yp += (i[6]/i[4])*100
                        ct += 1
                tct += ct
                tdp += dp
                typ += yp
                ttc += tc
                tta += ta
                dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'%.2f' %(dv):<9}{'%.2f' %(dp/ct):<9}{'%.2f' %(yp/ct):<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
                await ctx.send(f"```{dump}```", delete_after=1800)
                dump = ""
                ct = dv = dp = yp = tc = ta = 0
                for i in active:
                    if i[1] == "acoes":
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(((i[3]-i[4])/i[4])*100):<9}{i[3]:<9}{i[4]:<9}{'%.0f' %(i[5]):<9}{'%.2f' %(i[6]):<9}{'%.2f' %((i[6]/i[3])*100):<9}{'%.2f' %((i[6]/i[4])*100):<9}{i[7]:<9}{i[8]:<9}{'%.2f' %(i[3]*i[5]):<10}{'%.2f' %(i[4]*i[5])}\n"
                        tc += i[3]*i[5]
                        ta += i[4]*i[5]
                        dv += i[6]
                        dp += (i[6]/i[3])*100
                        yp += (i[6]/i[4])*100
                        ct += 1
                tdp += dp
                typ += yp
                ttc += tc
                tta += ta
                tct += ct
                dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'%.2f' %(dv):<9}{'%.2f' %(dp/ct):<9}{'%.2f' %(yp/ct):<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(tc):<10}{'%.2f' %(ta)}\n"
                await ctx.send(f"```{dump}```", delete_after=1800)
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
                await ctx.send(f"```{dump}```", delete_after=1800)
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
                await ctx.send(f"```{dump}```", delete_after=1800)
                dump = ""
                dump += f"{'-id-':<5}{'-nm-':<9}{'-vl%-':<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}{'-dv-':<9}{'%.2f' %(tdp/tct):<9}{'%.2f' %(typ/tct):<9}{'-pl-':<9}{'-vp-':<9}{'%.2f' %(ttc):<10}{'%.2f' %(tta)}\n"
                await ctx.send(f"```{dump}```", delete_after=1800)
            
            async def cot(interaction: discord.Interaction):
                with databaseConnection(config("hostMydb")) as db:
                    active = db.read("SELECT * FROM atv ORDER BY id asc", None)
                dump = ""
                allct = allvl = tvl = vl = ct = 0
                for i in active:
                    if i[1] == "rf":
                        ct += 1
                        vl = ((i[3]-i[4])/i[4])*100
                        ct += 1
                        tvl += vl
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{i[3]:<9}{i[4]:<9}{i[5]:<9}\n"
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}\n\n"
                allct += ct
                allvl += tvl
                tvl = ct = 0
                for i in active:
                    if i[1] == "fundos-imobiliarios":
                        vl = ((i[3]-i[4])/i[4])*100
                        ct += 1
                        tvl += vl
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{i[3]:<9}{i[4]:<9}{i[5]:<9}\n"
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}\n\n"
                allct += ct
                allvl += tvl
                tvl = ct = 0
                for i in active:
                    if i[1] == "acoes":
                        vl = ((i[3]-i[4])/i[4])*100
                        ct += 1
                        tvl += vl
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{i[3]:<9}{i[4]:<9}{i[5]:<9}\n"
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}\n\n"
                allct += ct
                allvl += tvl
                tvl = ct = 0
                for i in active:
                    if i[1] == "etfs" or i[1] == "bdrs":
                        vl = ((i[3]-i[4])/i[4])*100
                        ct += 1
                        tvl += vl
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{i[3]:<9}{i[4]:<9}{i[5]:<9}\n"
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}\n\n"
                allct += ct
                allvl += tvl
                tvl = ct = 0
                #for i in active:
                #    if i[1] == "criptomoedas":
                #        ct += 1
                #        vl = ((i[3]-i[4])/i[4])*100
                #        tvl += vl
                #        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{i[3]:<9}{i[4]:<9}{i[5]:<9}\n"
                #dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}\n\n"
                #allct += ct
                #allvl += tvl
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(allvl/allct):<9}{'-pr-':<9}{'-pm-':<9}{'-qt-':<9}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)

            async def div(interaction: discord.Interaction):
                with databaseConnection(config("hostMydb")) as db:
                    active = db.read("SELECT * FROM atv WHERE cl IN ('fundos-imobiliarios','acoes') ORDER BY id asc", None)
                dump = ""
                allct = allvl = alldp = allyp = tdp = typ = tvl = yp = dp = ct = 0
                for i in active:
                    if i[1] == "fundos-imobiliarios":
                        vl = ((i[3]-i[4])/i[4])*100
                        dp = (i[6]/i[3])*100
                        yp = (i[6]/i[4])*100
                        ct += 1
                        tvl += vl
                        tdp += dp
                        typ += yp
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{'%.2f' %(dp):<9}{'%.2f' %(yp):<9}\n"
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'%.2f' %(tdp/ct):<9}{'%.2f' %(typ/ct):<9}\n\n"
                allct += ct
                allvl += tvl
                alldp += tdp
                allyp += typ
                tdp = typ = tvl = yp = dp = ct = 0
                for i in active:
                    if i[1] == "acoes":
                        vl = ((i[3]-i[4])/i[4])*100
                        dp = (i[6]/i[3])*100
                        yp = (i[6]/i[4])*100
                        ct += 1
                        tvl += vl
                        tdp += dp
                        typ += yp
                        dump += f"{i[0]:<5}{i[2].upper():<9}{'%.2f' %(vl):<9}{'%.2f' %(dp):<9}{'%.2f' %(yp):<9}\n"
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(tvl/ct):<9}{'%.2f' %(tdp/ct):<9}{'%.2f' %(typ/ct):<9}\n\n"
                allct += ct
                allvl += tvl
                alldp += tdp
                allyp += typ
                dump += f"{'-i-':<5}{'-nm-':<9}{'%.2f' %(allvl/allct):<9}{'%.2f' %(alldp/allct):<9}{'%.2f' %(allyp/allct):<9}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)
            
            button1.callback = sync
            button2.callback = atv
            button3.callback = cot
            button4.callback = div
            
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            
            await ctx.send("Pressione um dos botões:", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

    @commands.command(name="atvreplace")
    async def replace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]:  # D
            with databaseConnection(config("hostMydb")) as db:
                before = db.read("SELECT * FROM atv WHERE id = %s", (args[0],))
                db.update("UPDATE atv SET {} = %s WHERE id = %s".format(args[1]), (args[2].replace(',', '.'), args[0]))
                after = db.read("SELECT * FROM atv WHERE id = %s", (args[0],))
            embed = discord.Embed(title='Replace', description=f'Anteriormente: {before[0]}\nPosteriormente: {after[0]}!')
            await ctx.send(embed=embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1800)

    @commands.command(name="atvdelete")
    async def delete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with databaseConnection(config("hostMydb")) as db:
                before = db.read("SELECT * FROM atv WHERE id = %s", (args[0],))
                db.delete("DELETE FROM atv WHERE id = %s", (args[0],))
            embed = discord.Embed(title='Replace', description=f'Anteriormente: {before}\nDeletado com sucesso.')
            await ctx.send(embed=embed, delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1800)

async def setup(bot):
    await bot.add_cog(fin(bot))
