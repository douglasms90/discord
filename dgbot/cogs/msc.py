import discord
from discord.ext import commands

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
        video_url = args[0]
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
        
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
            
            def after_playing(error):
                print('Fim')
            
            ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-bufsize 128k'}
            
            voice_client.play(discord.FFmpegPCMAudio(audio_url, **ffmpeg_options), after = after_playing)
            
            embed = discord.Embed(title='Tocando:', description=f"> {info['title']}")
        else:
            embed = discord.Embed(title='Não é possível tocar:', description=f"> Você precisa estar em um canal de voz para usar este comando.")
        await ctx.send(embed=embed)

    @commands.command(name="leave")
    async def out(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("O bot não está em um canal de voz.", delete_after=60)

async def setup(bot):
    await bot.add_cog(msc(bot))

