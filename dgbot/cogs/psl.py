import discord
from discord.ext import commands

from ext.database import databaseConnection
from decouple import config

import yt_dlp

class tst(commands.Cog):
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

    @commands.command(name="aiaiai...")
    async def ai(self, ctx):
        await ctx.send(f"MEU PIRUUUUUUU!")

    async def replace(self, ctx, *args):
        with databaseConnection(config("hostMydb")) as db:
            before = db.read(f"SELECT * FROM mkt WHERE id={args[0]}", (None))
            db.update(f"UPDATE mkt SET {args[1]} = %s WHERE id = %s", (args[2], args[0]))
            after = db.read(f"SELECT * FROM mkt WHERE id={args[0]}", (None))
            embed = discord.Embed(title='Replace', description=f'Anteriormente: {before[0]}\nPosteriormente: {after[0]}!')
            await ctx.author.send(embed=embed)

    @commands.command(name="yt")
    async def ai(self, ctx, *args):
        video_url = args[0] # URL do vídeo que você quer baixar
          
        ydl_opts = { # Opções de download
          'format': 'best',  # Escolhe a melhor qualidade de vídeo
          'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
        }
          
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # Baixa o vídeo
            ydl.download([video_url])
            
        await ctx.send(f"Download concluído:")

async def setup(bot):
    await bot.add_cog(tst(bot))



