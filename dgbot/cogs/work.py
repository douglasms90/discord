import discord
from discord.ext import commands

from ext.database import databaseConnection
from decouple import config
from datetime import datetime

# Futuramente terei que tirar o f-string por causa do sql-injection

class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def readIn(self, query):
        with databaseConnection(config("hostMydb")) as db:
            return db.read(query)

    def crudIn(self, query):
        with databaseConnection(config("hostMydb")) as db:
            return db.crud(query)

    @commands.command(name="act")
    async def act(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            self.crudIn(f"INSERT INTO act (dt, sn, os, cr, ct) VALUES ('{datetime.now()}', '{args[-4]}', '{args[-3]}', '{args[-2]}', '{args[-1]}')")
            dump = f"!ativa_onu {args[-4]} {args[-2]} {args[-1]}"
            await ctx.send(f"`{dump}`", delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="actreplace")
    async def actreplace(self, ctx, *args):
        if ctx.author.id in [269592803602989058]:  # D
            view = discord.ui.View()

            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Sim")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Não")

            before = self.readIn(f"SELECT * FROM act WHERE id={args[0]}")

            async def y(interaction: discord.Interaction):
                self.crudIn(f"UPDATE act SET {args[1]} = '{args[2]}' WHERE id = {args[0]}")
                after = self.readIn(f"SELECT * FROM act WHERE id = {args[0]}")
                await interaction.response.send_message(f"`{args[1]}` será alterado. Vai ser alterado de:\n`{before[0]}`\npara:\n`{after[0]}`", ephemeral=True)

            async def n(interaction: discord.Interaction):
                await interaction.response.send_message(f"Ativação\n`{before[0]}`\nnão foi alterado", ephemeral=True)

            button1.callback = y
            button2.callback = n

            view.add_item(button1)
            view.add_item(button2)

            await ctx.send(f"Deseja alterar o `{args[1]}` da ativação:\n`{before[0]}`\nPara:\n`{args[2]}`", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

    @commands.command(name="acttoday")
    async def acttoday(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            dump = ""
            today = self.readIn(f"SELECT * FROM act WHERE DATE(dt) = CURRENT_DATE order by id asc")
            print(today)
            for i in today:
                dump += f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}\n"
            await ctx.send(f"```{dump}```", delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="actlast")
    async def actlast(self, ctx):
        if ctx.author.id in [269592803602989058]: # D
            dump = ""
            today = self.readIn(f"SELECT * FROM act ORDER BY id desc LIMIT 23;")
            for i in today:
                dump += f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}\n"
            await ctx.send(f"```{dump}```", delete_after=1200)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização", delete_after=1200)

    @commands.command(name="actdelete")
    async def delete(self, ctx, *args):
        if ctx.author.id in [269592803602989058]: # D
            view = discord.ui.View()

            button1 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Sim")
            button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Não")

            before = self.readIn(f"SELECT * FROM act WHERE id = {args[0]}")

            async def y(interaction: discord.Interaction):
                self.crudIn(f"DELETE FROM act WHERE id = {args[0]}")
                await interaction.response.send_message(f"```Ativação\n`{before[0]}`\ndeletado com sucesso```", ephemeral=True)

            async def n(interaction: discord.Interaction):
                await interaction.response.send_message(f"```Ativação\n`{before[0]}`\nnão será deletado```", ephemeral=True)

            button1.callback = y
            button2.callback = n

            view.add_item(button1)
            view.add_item(button2)

            await ctx.send(f"Deseja deletar a ativação id: `{args[0]}`\n`{before[0]}`", view=view, delete_after=120)
        else:
            await ctx.send(f"{ctx.author} você não tem autorização.", delete_after=120)

async def setup(bot):
    await bot.add_cog(work(bot))
