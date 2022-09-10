from unicodedata import category
import nextcord
from nextcord.ext import commands



class URL(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command(name="pixiv",description="Pixiv 8or9位數轉網址&圖片")
    async def p (self, ctx, numbers) :
        await ctx.send (f"https://www.pixiv.net/artworks/{numbers}")
        await ctx.send (f"https://pixiv.cat/{numbers}.jpg")
    
    @nextcord.slash_command(name="nhentai",description="N站6位數轉網址")
    async def n (self, ctx,* ,numbers) :
        await ctx.send (f"https://nhentai.net/g/{numbers}/")

def setup(bot):
    bot.add_cog(URL(bot))