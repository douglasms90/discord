import discord
from discord.ext import commands

from ext.database import session
from models import Act, Vln
from datetime import datetime

from bs4 import BeautifulSoup
import requests

class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="act")
    async def act(self, ctx, *args):
        now=datetime.now()
        session.add(Act(dt=now,usr=ctx.author.name,olt=args[1],tfc=args[4],sn=args[-3],vln=session.query(Vln.vln).filter(Vln.olt == args[1], Vln.tfc == args[4]),ctr=args[-2],cto=args[-1]))
        session.commit()
        for obj in session.query(Act).filter(Act.dt == now):
            embed = discord.Embed(title=obj.olt,description=obj.tfc)
            embed.set_author(name=obj.usr)
            embed.add_field(name='Comando:', value=f'!ativa_onu_vlan {obj.sn} {obj.vln} {obj.ctr} {obj.cto}', inline=True)
            embed.set_footer(text=obj.id)
            await ctx.send(embed = embed)

    @commands.command(name="actreplace")
    async def replace(self, ctx, *args):
        session.query(Act).filter(Act.id == args[0]).update({args[1]:args[2]})
        session.commit()
        await ctx.send('Feito!')

    @commands.command(name="acttoday")
    async def today(self, ctx):
        for obj in session.query(Act).filter(Act.dt.like(f'{datetime.now().date()}%')):
            embed = discord.Embed(title=obj.olt,description=obj.tfc)
            embed.set_author(name=obj.usr)
            embed.add_field(name='', value=f'!ativa_onu_vlan {obj.sn} {obj.vln} {obj.ctr} {obj.cto}', inline=True)
            embed.set_footer(text=obj.id)
            await ctx.send(embed = embed)

    @commands.command(name="actdelete")
    async def delete(self, ctx, *args):
        session.query(Act).filter(Act.id == args[0]).delete()
        session.commit()
        await ctx.send('Feito!')

async def setup(bot):
    await bot.add_cog(work(bot))
