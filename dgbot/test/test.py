import discord
from discord.ext import commands
import youtube_dl


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='testando')
    async def test(self, ctx):
        await ctx.send('test')

async def setup(bot):
    await bot.add_cog(test(bot))
