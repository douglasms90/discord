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

    @commands.command(name="aiaiai")
    async def aiaiai(self, ctx):
        await ctx.send(f"Meu piru...Vem novinha vem sentando o bumbum")

    async def replace(self, ctx, *args):
        with databaseConnection(config("hostMydb")) as db:
            before = db.read(f"SELECT * FROM mkt WHERE id={args[0]}", (None))
            db.update(f"UPDATE mkt SET {args[1]} = %s WHERE id = %s", (args[2], args[0]))
            after = db.read(f"SELECT * FROM mkt WHERE id={args[0]}", (None))
            embed = discord.Embed(title='Replace', description=f'Anteriormente: {before[0]}\nPosteriormente: {after[0]}!')
            await ctx.author.send(embed=embed)

    @commands.command(name="join")
    async def join(self, ctx):
        # Verifica se o autor da mensagem está em um canal de voz
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            try:
                print(f"Tentando conectar ao canal: {channel.name}")
                # Conecta ao canal de voz do autor da mensagem
                voice_client = await channel.connect()
                await ctx.send(f"Conectado ao canal: {channel.name}")
                print(f"Conectado ao canal: {channel.name}")
            except discord.errors.ClientException as e:
                await ctx.send("Já estou conectado a um canal de voz.")
                print(f"Já estou conectado a um canal de voz: {str(e)}")
            except discord.errors.DiscordException as e:
                await ctx.send(f"Ocorreu um erro ao tentar conectar: {str(e)}")
                print(f"Ocorreu um erro ao tentar conectar: {str(e)}")
        else:
            await ctx.send("Você precisa estar em um canal de voz para usar este comando.")
            print("Usuário não está em um canal de voz.")

    @commands.command(name="yt")
    async def yt(self, ctx, *args):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'ffmpeg_location': '/caminho/para/ffmpeg.exe',  # Adicione o caminho completo para o ffmpeg
        }
        
        video_url = args[0]  # URL do vídeo que você quer baixar
        
        # Baixa o áudio do vídeo do YouTube
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info).replace(".webm", ".mp3")
        
        # Conecta ao canal de voz do usuário
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
            
            # Toca a música no canal de voz
            voice_client.play(discord.FFmpegPCMAudio(filename))
            
            await ctx.send(f"Agora tocando: {info['title']}")
        else:
            await ctx.send("Você precisa estar em um canal de voz para usar este comando.")

async def setup(bot):
    await bot.add_cog(tst(bot))

# Download de vídeo básico
'''
video_url = args[0] # URL do vídeo que você quer baixar
  
ydl_opts = { # Opções de download
  'format': 'best',  # Escolhe a melhor qualidade de vídeo
  'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl: # Baixa o vídeo
    ydl.download([video_url])
'''
