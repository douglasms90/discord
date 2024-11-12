import discord
from discord.ext import commands

from decouple import config

class psl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mkt")
    async def view(self, ctx):
        with databaseConnection(config("hostMydb")) as db:
            allmkt = db.read("SELECT * FROM mkt ORDER BY id", (None))
        dump = ""
        dump += f"{'-id-':<5}{'-mc-':<5}{'-nm-':<23}{'-pd-':<8}{'-md-':<8}{'-pu-'}\n"
        for i in allmkt:
            dump += f"{i[0]:<5}{i[1]:<5}{i[2]:<23}{i[3]:<8}{('%.2f' %((i[3]+i[4])/2)):<8}{i[4]}\n"
        await ctx.send(f"```{dump}```")

    @commands.command(name="aiaiai")
    async def aiaiai(self, ctx):
        await ctx.send(f"Meu piru...Vem novinha vem sentando o bumbum")
        #await ctx.send(f"Chega {ctx.author}")

    async def replace(self, ctx, *args):
        with databaseConnection(config("hostMydb")) as db:
            before = db.read(f"SELECT * FROM mkt WHERE id={args[0]}", (None))
            db.update(f"UPDATE mkt SET {args[1]} = %s WHERE id = %s", (args[2], args[0]))
            after = db.read(f"SELECT * FROM mkt WHERE id={args[0]}", (None))
            embed = discord.Embed(title='Replace', description=f'Anteriormente: {before[0]}\nPosteriormente: {after[0]}!')
            await ctx.author.send(embed=embed)

async def setup(bot):
    await bot.add_cog(psl(bot))
