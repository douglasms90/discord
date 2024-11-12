import discord
from discord.ext import commands

from ext.database import databaseConnection
from decouple import config
from datetime import datetime

class nails(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nails")
    async def nails(self, ctx, *args):
        now = datetime.now()
        with databaseConnection(config("hostMydb")) as db:
            db.insert("INSERT INTO nails(dt, pr) VALUES(%s, %s)", (now, args[0],))
            view = db.read("SELECT * FROM nails WHERE dt=%s", (now,))
        for i in view:
            embed = discord.Embed(title=f'{now}',description='Unha')
            embed.set_author(name=ctx.author)
            embed.add_field(name='', value=f'', inline=True)
            embed.set_footer(text=i[0])
        await ctx.send(embed = embed)

    @commands.command(name="nailsdelete")
    async def nailsdelete(self, ctx, *args):
        with databaseConnection(config("hostMydb")) as db:
            before = db.read("SELECT * FROM nails WHERE id = %s", (args[0],))
            db.delete("DELETE FROM nails WHERE id = %s", (args[0],))
        await ctx.send(f'{before}\nDeletado com sucesso.')

    @commands.command(name="nailstoday")
    async def nailstoday(self, ctx):
        dump = ""
        with databaseConnection(config("hostMydb")) as db:
            today = db.read("SELECT * FROM nails WHERE DATE(dt) = CURRENT_DATE", (None))
        for i in today:
            dump += f"{i[0]}, {i[1]}, {i[2]}\n"
        await ctx.send(f"```{dump}```")

async def setup(bot):
    await bot.add_cog(nails(bot))
