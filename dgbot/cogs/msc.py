import discord
from discord.ext import commands

import os
import json
import yt_dlp

class msc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
            'ffmpeg_location': '/usr/bin/ffmpeg',  # Adicione o caminho completo para o ffmpeg
        }
        
        video_url = args[0]  # URL do vídeo que você quer baixar
        
        # Baixa o áudio do vídeo do YouTube
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            #print(json.dumps(ydl.sanitize_info(info)))
            #audio_url = info['url']
            filename = ydl.prepare_filename(info).replace(".webm", ".mp3")
        
        # Conecta ao canal de voz do usuário
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
            
            def after_playing(error):
                
                os.remove(filename)
           
            # Toca a música no canal de voz
            #voice_client.play(discord.FFmpegPCMAudio(audio_url))
            voice_client.play(discord.FFmpegPCMAudio(filename), after=after_playing)
            
            embed = discord.Embed(title='Tocando:', description=f"> {info['title']}")
            
        else:
            embed = discord.Embed(title='Não é possível tocar:', description=f"> Você precisa estar em um canal de voz para usar este comando.")
        
        await ctx.send(embed=embed)

    @commands.command(name="leave")
    async def out(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("O bot não está em um canal de voz.")

async def setup(bot):
    await bot.add_cog(msc(bot))

