import discord
from discord.ext import commands

from ext.database import databaseConnection
from decouple import config
from datetime import datetime

class nails(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nails")
    async def nails(self, ctx):
        if ctx.author.id in [269592803602989058, 825867087390048326]:  # D, D
            view = discord.ui.View()
            
            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="25")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="50")
            button3 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="120")
            button4 = discord.ui.Button(style=discord.ButtonStyle.primary, label="Dia")
            
            async def um(interaction: discord.Interaction):
                now = datetime.now()
                with databaseConnection(config("hostMydb")) as db:
                    db.insert("INSERT INTO nails(dt, pr) VALUES(%s, %s)", (now, 25,))
                    view = db.read("SELECT * FROM nails WHERE dt=%s", (now,))
                for i in view:
                    embed = discord.Embed(title=f'{now}',description='Unha')
                    embed.set_author(name=ctx.author)
                    embed.add_field(name='', value='', inline=True)
                    embed.set_footer(text=i[0])
                await interaction.response.send_message(embed = embed, ephemeral=True)
            
            async def dois(interaction: discord.Interaction):
                now = datetime.now()
                with databaseConnection(config("hostMydb")) as db:
                    db.insert("INSERT INTO nails(dt, pr) VALUES(%s, %s)", (now, 50,))
                    view = db.read("SELECT * FROM nails WHERE dt=%s", (now,))
                for i in view:
                    embed = discord.Embed(title=f'{now}',description='Unha')
                    embed.set_author(name=ctx.author)
                    embed.add_field(name='', value='', inline=True)
                    embed.set_footer(text=i[0])
                await interaction.response.send_message(embed = embed, ephemeral=True)
            
            async def tres(interaction: discord.Interaction):
                now = datetime.now()
                with databaseConnection(config("hostMydb")) as db:
                    db.insert("INSERT INTO nails(dt, pr) VALUES(%s, %s)", (now, 120,))
                    view = db.read("SELECT * FROM nails WHERE dt=%s", (now,))
                for i in view:
                    embed = discord.Embed(title=f'{now}',description='Unha')
                    embed.set_author(name=ctx.author)
                    embed.add_field(name='', value='', inline=True)
                    embed.set_footer(text=i[0])
                await interaction.response.send_message(embed = embed, ephemeral=True)
            
            async def quatro(interaction: discord.Interaction):
                dump = ""
                with databaseConnection(config("hostMydb")) as db:
                    today = db.read("SELECT * FROM nails WHERE DATE(dt) = CURRENT_DATE", (None))
                for i in today:
                    dump += f"{i[0]}, {i[1]}, {i[2]}\n"
                await interaction.response.send_message(f"```{dump}```", ephemeral=True)
            
            button1.callback = um
            button2.callback = dois
            button3.callback = tres
            button4.callback = quatro
            
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            
            await ctx.send("Qual o valor?", view=view, delete_after=60)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=60)

    @commands.command(name="nailsdelete")
    async def nailsdelete(self, ctx, *args):
        if ctx.author.id in [269592803602989058, 825867087390048326]:  # D, D
            with databaseConnection(config("hostMydb")) as db:
                before = db.read("SELECT * FROM nails WHERE id = %s", (args[0],))
                db.delete("DELETE FROM nails WHERE id = %s", (args[0],))
            await ctx.send(f'{before}\nDeletado com sucesso.', delete_after=60)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=60)

async def setup(bot):
    await bot.add_cog(nails(bot))
