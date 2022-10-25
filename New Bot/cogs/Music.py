from unicodedata import category
import nextcord
from nextcord.ext import commands



class Music(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command(description="Muic bot(UNFINISHED)")
    async def play(self, ctx):
        await ctx.send ("Still Making")
        
    # @commands.command()
    # async def play(self, ctx, url : str):
    #     await ctx.send("Waiting for Misic Download")
    #     channel = ctx.message.author.voice.channel
    #     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
    #     voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    #     if voice is None or not voice.is_connected():
    #         await voiceChannel.connect()

    # @commands.command()
    # async def leave (self , ctx) :
    #     channel = ctx.message.author.voice.channel
    #     voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    #     voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
    #     if voice_client:
    #         await voice_client.disconnect()
    #     else :
    #         await ctx.send("The bot is not content in a voice channel")


def setup(bot):
    bot.add_cog(Music(bot))