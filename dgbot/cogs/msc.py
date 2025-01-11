import discord
from discord.ext import commands

import yt_dlp

class msc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yt")
    async def yt(self, ctx, *args):
        view = discord.ui.View(timeout=1800)
        
        outbutton = discord.ui.Button(style=discord.ButtonStyle.danger, label="Sair")
        
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
            
            ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-bufsize 128k'}
            
            voice_client.play(discord.FFmpegPCMAudio(audio_url, **ffmpeg_options))
            
            embed = discord.Embed(title='Tocando:', description=f"> {info['title']}")
        
        async def out(interaction: discord.Interaction):
            await interaction.response.defer()
            if ctx.voice_client:
                await ctx.voice_client.disconnect()
            else:
                embed = discord.Embed(title='Não estou mais ai.')
            await interaction.response.send_message(embed = embed, ephemeral=False, delete_after=5)
        
        outbutton.callback = out
        
        view.add_item(outbutton)
        
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(msc(bot))
