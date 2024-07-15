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
            embed = discord.Embed(title=i[2],description=i[3])
            embed.set_author(name=i[1].add_field(name='', value=fi[4], inline=True)
            embed.set_footer(text=i[0])
            await ctx.send(embed = embed)

    @commands.command(name='requery')
    async def test(self, ctx):
        conn = dbc(config("host"))
        dump = conn.consult(config("requery"))
        for i in dump:
            await ctx.send(i)

async def setup(bot):
    await bot.add_cog(test(bot))
