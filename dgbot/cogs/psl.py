import discord
from discord.ext import commands


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

async def setup(bot):
    await bot.add_cog(tst(bot))
