import discord
from discord.ext import commands

from ext.database import Session
from models import Mkt

class tst(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tst")
    async def meu_comando(self, ctx):
        view = discord.ui.View()
        
        # Primeiro botão
        button1 = discord.ui.Button(style=discord.ButtonStyle.primary, label="Botão 1")
        
        # Segundo botão
        button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Botão 2")
        
        async def button_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"Botão {interaction.component.label} pressionado!", ephemeral=True)
        
        button1.callback = button_callback
        button2.callback = button_callback
        
        view.add_item(button1)
        view.add_item(button2)
        
        await ctx.send("Escolha um botão:", view=view)

    @commands.command(name="mkt")
    async def view(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                allmkt = session.query(Mkt).all()
            dump = ""
            dump += f"{'-id-':<5}{'-mc-':<5}{'-nm-':<23}{'-kc-':<5}{'-ma-':<8}{'-md-':<8}{'-mr-'}\n"
            for i in allmkt:
                dump += f"{i.id:<5}{i.mc:<5}{i.nm:<23}{i.kc:<5}{i.pu:<8}{('%.2f' %((i.pu+i.pd)/2)):<8}{i.pd}\n"
            await ctx.send(f"```{dump}```")
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

    @commands.command(name="mktreplace")
    async def replace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            with Session() as session:
                session.query(Mkt).filter(Mkt.id == args[0]).update({args[1]:args[2].replace(',','.')})
                session.commit()
            await ctx.author.send('Feito!')
        else:
            await ctx.send(f"{ctx.author} você não tem autorização")

async def setup(bot):
    await bot.add_cog(tst(bot))
