import discord
from discord.ext import commands


class _init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Exec...")

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send("Is fine...")

async def setup(bot):
    await bot.add_cog(_init(bot))
