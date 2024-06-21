import discord
from discord.ext import commands
import youtube_dl


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    '''
    @commands.command()
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    # Comando para o bot sair do canal de voz
    @commands.command()
    async def leave(ctx):
        await ctx.voice_client.disconnect()

    # Comando para tocar música do YouTube
    @commands.command()
    async def play(ctx, url):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    # Comando para pausar a música
    @commands.command()
    async def pause(ctx):
        await ctx.voice_client.pause()

    # Comando para continuar a música
    @commands.command()
    async def resume(ctx):
        await ctx.voice_client.resume()
    '''
async def setup(bot):
    await bot.add_cog(test(bot))
