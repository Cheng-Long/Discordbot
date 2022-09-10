from unicodedata import category
import nextcord
from nextcord.ext import commands



class VoiceChannel(commands.Cog) :
    TESTING_GUILD_ID = 691167211548704808
     
    def __init__(self , bot) :
        self.bot = bot

    voice_channel_ID = 0
    category_ID = 0


    @nextcord.slash_command(description="創建語音頻道於[類別ID],[頻道名稱]")
    async def create_voice_channel(self, ctx, categoryid, channelname):
        category = int(categoryid)
        category_channel = nextcord.utils.get(ctx.guild.categories, id=category)
        await ctx.guild.create_voice_channel(f"{channelname}", category=category_channel)
        await ctx.send("Create Successfully")

    @nextcord.slash_command(description="創建文字頻道於[類別ID],[頻道名稱]")
    async def create_text_channel(self, ctx, categoryid, channelname):
        category = int(categoryid)
        category_channel = nextcord.utils.get(ctx.guild.categories, id=category)
        await ctx.guild.create_text_channel(f"{channelname}", category=category_channel)
        await ctx.send("Create Successfully")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if member.guild.id == 691167211548704808:
            channel = after.channel
            try:
                if before.channel.members == [] and not before.channel.id == 1017116266944811158:
                    if before.channel.category_id == 911215817948008479:
                        await before.channel.delete()
            except:
                pass
            try:
                if before.channel.members == [] and not before.channel.id == 826115072455737354:
                    if before.channel.category_id == 826114944901709874:
                        await before.channel.delete()
            except:
                pass
            try:
                if channel.id == 1017116266944811158:
                    guild = after.channel.guild
                    category = 911215817948008479
                    category_channel = nextcord.utils.get(guild.categories, id=category)
                    voice_channel = await guild.create_voice_channel(f"{member}'s channel", category=category_channel)
                    await member.move_to(voice_channel)
            except:
                return

    @nextcord.slash_command(description="設置自動語音房類別及頻道")
    async def setting_voice_channel (ctx, categoryidd, channelid):
        global voice_channel_ID
        global category_ID
        voice_channel_ID = int(channelid)
        category_ID = int(categoryidd)
        await  ctx.send(f"**Voice Channel Setting Already, Category ID: **{category_ID}**, Channel ID: **{voice_channel_ID}")

    @nextcord.slash_command(description="檢視自動語音房類別及頻道")
    async def check_voice_channel (ctx):
        global voice_channel_ID
        await  ctx.send(f"**The Voice Start Channel Is : Category ID: **{category_ID}**, Channel ID: **{voice_channel_ID}")

def setup(bot):
    bot.add_cog(VoiceChannel(bot))