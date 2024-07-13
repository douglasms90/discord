import discord
from discord.ext import commands
from decouple import config

from ext.database import dbc


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='naquery')
    async def test(self, ctx):
        conn = dbc(config("host"))
        dump = conn.consult(config("naquery"))
        for i in dump:
            await ctx.send(i)

    @commands.command(name='requery')
    async def test(self, ctx):
        conn = dbc(config("host"))
        dump = conn.consult(config("requery"))
        for i in dump:
            await ctx.send(i)

async def setup(bot):
    await bot.add_cog(test(bot))
