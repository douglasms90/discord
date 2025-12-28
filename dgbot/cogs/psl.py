import discord
from discord.ext import commands

from ext.database import databaseConnection
from decouple import config

class psl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def readIn(self, query):
        with databaseConnection(config("hostMydb")) as db:
            return db.read(query)

    def crudIn(self, query):
        with databaseConnection(config("hostMydb")) as db:
            return db.crud(query)

    @commands.command(name="mkt")
    async def view(self, ctx):
        dump = ""
        allmkt = self.readIn(f"SELECT * FROM mkt ORDER BY id asc")
        dump += f"{'-id-':<5}{'-mc-':<5}{'-nm-':<23}{'-pd-':<8}{'-md-':<8}{'-pu-':<8}\n"
        for i in allmkt:
            dump += f"{i[0]:<5}{i[1]:<5}{i[2]:<23}{i[3]:<8}{('%.2f' %((i[3]+i[4])/2)):<8}{i[4]:<8}\n"
        await ctx.send(f"```{dump}```", delete_after=1200)

    @commands.command(name="mktreplace")
    async def mktreplace(self, ctx, *args):
        before = self.readIn(f"SELECT * FROM mkt WHERE id = {args[0]}")
        self.crudIn(f"UPDATE mkt SET {args[1]} = '{args[2]}' WHERE id = {args[0]}")
        after = self.readIn(f"SELECT * FROM mkt WHERE id={args[0]}")
        embed = discord.Embed(title='Replace', description=f'Anteriormente: {before[0]}\nPosteriormente: {after[0]}!')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(psl(bot))
