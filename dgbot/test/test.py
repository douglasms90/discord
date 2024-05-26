import discord
from discord.ext import commands
from ext.database import session
from ext.webscraping import bs
from models import Atv
from bs4 import BeautifulSoup
import youtube_dl
import requests


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx, url):
        # Configurações do youtube_dl
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        # Inicializa o youtube_dl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url = info['formats'][0]['url']  # Obtém a URL do áudio
        
        # Conecta ao canal de voz e reproduz o áudio
        voice_channel = ctx.author.voice.channel
        print(voice_channel)
        voice_client = await voice_channel.connect()
        voice_client.play(discord.FFmpegPCMAudio(url))

async def setup(bot):
    await bot.add_cog(test(bot))
