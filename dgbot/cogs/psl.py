import discord
from discord.ext import commands

from ext.database import databaseConnection
from decouple import config

class tst(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tst")
    async def meu_comando(self, ctx):
        view = discord.ui.View()
        
        # Primeiro botão
        button1 = discord.ui.Button(style=discord.ButtonStyle.primary, label="Botão 1")
        
        # Segundo botão
        button2 = discord.ui.Button(style=discord.ButtonStyle.primary, label="Botão 2")
        
        async def button_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"Botão {interaction.component.label} pressionado!", ephemeral=True)
        
        button1.callback = button_callback
        button2.callback = button_callback
        
        view.add_item(button1)
        view.add_item(button2)
        
        await ctx.send("Escolha um botão:", view=view)

    @commands.command(name="mkt")
    async def view(self, ctx):
        with databaseConnection(config("hostMydb")) as db:
            allmkt = db.read("SELECT * FROM mkt ORDER BY id")
        dump = ""
        dump += f"{'-id-':<5}{'-mc-':<5}{'-nm-':<23}{'-pd-':<8}{'-md-':<8}{'-pu-'}\n"
        for i in allmkt:
            dump += f"{i[0]:<5}{i[1]:<5}{i[2]:<23}{i[3]:<8}{('%.2f' %((i[3]+i[4])/2)):<8}{i[4]}\n"
        await ctx.send(f"```{dump}```")

    @commands.command(name="mktreplace")
    async def replace(self, ctx, *args):
        with databaseConnection(config("hostMydb")) as db:
            before = db.read(f"SELECT * FROM mkt WHERE id={args[0]}")
            db.update(f"UPDATE mkt SET {args[1]} = %s WHERE id = %s", (args[2], args[0]))
            after = db.read(f"SELECT * FROM mkt WHERE id={args[0]}")
        await ctx.send(f'Anteriormente: {before}\nPosteriormente: {after}!')

async def setup(bot):
    await bot.add_cog(tst(bot))
