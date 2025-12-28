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
        self.dols = 5.52

    def readIn(self, query):
        with databaseConnection(config("hostMydb")) as db:
            return db.read(query)

    def crudIn(self, query):
        with databaseConnection(config("hostMydb")) as db:
            return db.crud(query)

    @commands.command(name="atv")
    async def atv(self, ctx):
        if ctx.author.id in [269592803602989058]:  # D
            view = discord.ui.View()
            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="sync")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="rf")
            button3 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="fii")
            button4 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="ações")
            button5 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="eua")
            button6 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="ttl")
            
            async def sync(interaction: discord.Interaction):
                await interaction.response.defer()
                allatv = self.readIn("SELECT * FROM atv order by id asc")
                for i in allatv:
                    if i[1] == 'rf':
                        pass
                    elif i[1] == 'dollar':
                        pass
                    elif i[1] == 'rf/eua':
                        pass
                    else:
                        st = bs(f"https://statusinvest.com.br/{i[1]}/{i[2]}")
                        pr = float((st.find_all('strong', class_='value')[0].text).replace('.', '').replace(',', '.'))
                        self.crudIn(f"UPDATE atv SET pr = {pr} WHERE id = {i[0]}")
                        if i[1] == 'fundos-imobiliarios':
                            dv = float((st.find_all('span', class_='sub-value')[3].text)[3:].replace(',', '.'))
                            try:
                                vp = float(st.find_all('strong', class_='value')[6].text.replace(',', '.'))
                            except:
                                vp = 0
                            self.crudIn(f"UPDATE atv SET dv = {dv}, vp = {vp} WHERE id = {i[0]}")
                        if i[1] == 'acoes':
                            dv = float((st.find_all('span', class_='sub-value')[3].text)[3:].replace(',', '.'))
                            pl = float(st.find_all('strong', class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',', '.'))
                            vp = float(st.find_all('strong', class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',', '.'))
                            self.crudIn(f"UPDATE atv SET dv = {dv}, pl = {pl}, vp = {vp} WHERE id = {i[0]}")
                await interaction.followup.send("Sync ok", ephemeral=True)
            
            async def rf(interaction: discord.Interaction):
                active = self.readIn("SELECT * FROM atv order by id asc")
                tta = ttc = tc = ta = 0
                dump = ""
                for i in active:
                    if i[1] == "rf" or i[1] == "tesouro":
                        dump += f"{i[0]:<4}{i[2].upper():<19}{('%.2f' %(((i[3]-i[4])/i[4])*100)):>6}{'%.2f' %(i[3]):>9}{'%.2f' %(i[4]):>9}{'%.2f' %(i[5]):>7}{'':>4}{'':>4}{'':>3}{'':>3}{'%.2f' %(i[3]*i[5]):>9}{'%.2f' %(i[4]*i[5]):>9}{'%.2f' %((i[3]*i[5])-(i[4]*i[5])):>9}\n"
                        tc += i[3]*i[5]
                        ta += i[4]*i[5]
                dump += f"id{'nm':>13}{'vl%':>13}{'pr':>8}{'pm':>9}{'qt':>7}{'dv%':>6}{'yc%':>4}{'pl':>3}{'vp':>3}{'%.2f' %(tc):>9}{'%.2f' %(ta):>9}{'%.2f' %(tc-ta):>9}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)

            async def fiis(interaction: discord.Interaction):
                active = self.readIn("SELECT * FROM atv ORDER BY id asc")
                tta = ttc = typ = tdp = tct = ct = dv = dp = yp = tc = ta = 0
                dump = ""
                for i in active:
                    if i[1] == "fundos-imobiliarios":
                        dump += f"{i[0]}{i[2].upper():>7}{('%.2f' %(((i[3]-i[4])/i[4])*100)):>7}{'%.2f' %(i[3]):>7}{'%.2f' %(i[4]):>7}{'%.0f' %(i[5]):>4}{'%.2f' %((i[6]/i[3])*100):>6}{'%.2f' %((i[6]/i[4])*100):>6}{'':>3}{i[8]:>5}{'%.2f' %(i[3]*i[5]):>9}{'%.2f' %(i[4]*i[5]):>9}{'%.2f' %((i[3]*i[5])-(i[4]*i[5])):>9}\n"
                        tc += i[3]*i[5]
                        ta += i[4]*i[5]
                        dv += i[6]
                        dp += (i[6]/i[3])*100
                        yp += (i[6]/i[4])*100
                        ct += 1
                dump += f"id{'nm':>6}{'vl%':>8}{'pr':>6}{'pm':>7}{'qt':>6}{'%.2f' %(dp/ct):>6}{'%.2f' %(yp/ct):>6}{'pl':>3}{'vp':>4}{'%.2f' %(tc):>10}{'%.2f' %(ta):>9}{'%.2f' %(tc-ta):>9}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)
            
            async def acoes(interaction: discord.Interaction):
                active = self.readIn("SELECT * FROM atv ORDER BY id asc")
                tta = ttc = typ = tdp = tct = ct = dv = dp = yp = tc = ta = 0
                dump = ""
                for i in active:
                    if i[1] == "acoes":
                        dump += f"{i[0]}{i[2].upper():>7}{'%.2f' %(((i[3]-i[4])/i[4])*100):>6}{'%.2f' %(i[3]):>6}{'%.2f' %(i[4]):>6}{'%.0f' %(i[5]):>4}{'%.2f' %((i[6]/i[3])*100):>6}{'%.2f' %((i[6]/i[4])*100):>6}{i[7]:>6}{i[8]:>5}{'%.2f' %(i[3]*i[5]):>9}{'%.2f' %(i[4]*i[5]):>9}{'%.2f' %((i[3]*i[5])-(i[4]*i[5])):>8}\n"
                        tc += i[3]*i[5]
                        ta += i[4]*i[5]
                        dv += i[6]
                        dp += (i[6]/i[3])*100
                        yp += (i[6]/i[4])*100
                        ct += 1
                dump += f"id{'nm':>6}{'vl%':>7}{'pr':>5}{'pm':>6}{'qt':>6}{'%.2f' %(dp/ct):>6}{'%.2f' %(yp/ct):>6}{'pl':>5}{'vp':>5}{'%.2f' %(tc):>10}{'%.2f' %(ta):>9}{'%.2f' %(tc-ta):>8}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)

            async def eua(interaction: discord.Interaction):
                active = self.readIn("SELECT * FROM atv ORDER BY id asc")
                tta = ttc = typ = tdp = tct = ct = dv = dp = yp = tc = ta = 0
                dump = ""
                for i in active:
                    if i[1] == "dollar" or i[1] == "etf/eua" or i[1] == "rf/eua":
                        dump += f"{i[0]:<4}{i[2].upper():<6}{'%.2f' %(((i[3]-i[4])/i[4])*100):>7}{'%.2f' %(i[3]):>8}{'%.2f' %(i[4]):>8}{'%.2f' %(i[5]):>6}{'':>3}{'':>3}{'':>3}{'':>3}{'%.2f' %((i[3]*i[5])*self.dols):>11}{'%.2f' %((i[4]*i[5])*self.dols):>9}{'%.2f' %(((i[3]*i[5])*self.dols)-((i[4]*i[5])*self.dols)):>9}\n"
                        tc += (i[3]*i[5])*self.dols
                        ta += (i[4]*i[5])*self.dols
                dump += f"id{'nm':>6}{'vl%':>8}{'pr':>7}{'pm':>8}{'qt':>6}{'dv%':>6}{'yc%':>4}{'pl':>3}{'vp':>3}{'%.2f' %(tc):>9}{'%.2f' %(ta):>9}{'%.2f' %(tc-ta):>9}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)

            async def ttl(interaction: discord.Interaction):
                active = self.readIn("SELECT * FROM atv ORDER BY id asc")
                ttc = tta = rtc = rta = fdp = fct = fyp = ftc = fta = fdv = adp = ayp = act = atc = ata = adv = itc = ita = sta = stc = 0
                dump = ""
                for i in active:
                    if i[1] == "rf" or i[1] == "tesouro":
                        rtc += i[3]*i[5]
                        rta += i[4]*i[5]
                ttc += rtc
                tta += rta
                for i in active:
                    if i[1] == "fundos-imobiliarios":
                        ftc += i[3]*i[5]
                        fta += i[4]*i[5]
                        fdv += i[6]
                        fdp += (i[6]/i[3])*100
                        fyp += (i[6]/i[4])*100
                        fct += 1
                ttc += ftc
                tta += fta
                for i in active:
                    if i[1] == "acoes":
                        atc += i[3]*i[5]
                        ata += i[4]*i[5]
                        adv += i[6]
                        adp += (i[6]/i[3])*100
                        ayp += (i[6]/i[4])*100
                        act += 1
                ttc += atc
                tta += ata
                for i in active:
                    if i[1] == "dollar" or i[1] == "rf/eua":
                        itc += (i[3]*i[5])*self.dols
                        ita += (i[4]*i[5])*self.dols
                ttc += itc
                tta += ita
                for i in active:
                    if i[1] == "etf/eua":
                        stc += (i[3]*i[5])*self.dols
                        sta += (i[4]*i[5])*self.dols
                ttc += stc
                tta += sta
                dump += f"rf {'%.2f' %(ttc*0.5):>21}{'%.2f' %(rtc):>10}{'%.2f' %(rta):>10}{'%.2f' %(rtc-rta):>9}\n"
                dump += f"fi {'%.2f' %(fdp/fct)}{'%.2f' %(fyp/fct):>6}{'%.2f' %(ttc*0.2):>10}{'%.2f' %(ftc):>10}{'%.2f' %(fta):>10}{'%.2f' %(ftc-fta):>9}\n"
                dump += f"aç {'%.2f' %(adp/act):>1}{'%.2f' %(ayp/act):>7}{'%.2f' %(ttc*0.15):>10}{'%.2f' %(atc):>10}{'%.2f' %(ata):>10}{'%.2f' %(atc-ata):>9}\n"
                dump += f"ea {'%.2f' %(ttc*0.10):>21}{'%.2f' %(itc):>10}{'%.2f' %(ita):>10}{'%.2f' %(itc-ita):>9}\n"
                dump += f"bt {'%.2f' %(ttc*0.05):>21}{'%.2f' %(stc):>10}{'%.2f' %(sta):>10}{'%.2f' %(stc-sta):>9}\n"
                dump += f"tl {'%.2f' %((fdp+adp)/(fct+act))}{'%.2f' %((fyp+ayp)/(fct+act)):>6}{'%.2f' %(ttc):>20}{'%.2f' %(tta):>10}{'%.2f' %(ttc-tta):>9}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)

            button1.callback = sync
            button2.callback = rf
            button3.callback = fiis
            button4.callback = acoes
            button5.callback = eua
            button6.callback = ttl
            
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            view.add_item(button5)
            view.add_item(button6)
            
            await ctx.send("Pressione um dos botões:", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

    @commands.command(name="atvreplace")
    async def replace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]:  # D
            view = discord.ui.View()

            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Sim")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Não")

            before = self.readIn(f"SELECT * FROM atv WHERE id = {args[0]}")

            async def y(interaction: discord.Interaction):
                with self.readIn() as db:
                    self.crudIn("UPDATE atv SET {} = %s WHERE id = %s".format(args[1]), (args[2].replace(',', '.'), args[0]))
                    after = self.readIn(f"SELECT * FROM atv WHERE id = {args[0]}")
                await interaction.response.send_message(f"`{args[1]}` da linha:\n`{before[0]}`\nAlterado para:\n`{after[0]}`", ephemeral=True)

            async def n(interaction: discord.Interaction):
                await interaction.response.send_message(f"```Ativo {before[0]} não alterado```", ephemeral=True)

            button1.callback = y
            button2.callback = n

            view.add_item(button1)
            view.add_item(button2)

            await ctx.send(f"Deseja alterar o `{args[1]}` da linha:\n`{before[0]}`\nPara:\n`{args[2]}`", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

    @commands.command(name="atvdelete")
    async def delete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            view = discord.ui.View()

            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Sim")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Não")

            with self.readIn() as db:
                before = self.readIn(f"SELECT * FROM atv WHERE id = {args[0]}")

            async def y(interaction: discord.Interaction):
                with self.readIn() as db:
                    self.crudIn(f"DELETE FROM atv WHERE id = {args[0]}")
                await interaction.response.send_message(f"```Ativo {before[0]} deletado com sucesso```", ephemeral=True)

            async def n(interaction: discord.Interaction):
                await interaction.response.send_message(f"```Ativo {before[0]} não será deletado```", ephemeral=True)

            button1.callback = y
            button2.callback = n

            view.add_item(button1)
            view.add_item(button2)

            await ctx.send(f"Deseja deletar o ativo id: {args[0]}\n{before[0]}", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

async def setup(bot):
    await bot.add_cog(fin(bot))
