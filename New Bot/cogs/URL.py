import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import random as rd



class URL(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command(description="Pixiv 8or9位數轉網址&圖片")
    async def pixiv (self, ctx, numbers) :
        await ctx.send (f"https://www.pixiv.net/artworks/{numbers}")
        await ctx.send (f"https://pixiv.cat/{numbers}.jpg")
    
    @nextcord.slash_command(description="N站6位數轉網址")
    async def nhentai (self, ctx,* ,numbers) :
        await ctx.send (f"https://nhentai.net/g/{numbers}/")

    @nextcord.slash_command(name="18comic",description="禁漫天堂6位數轉網址")
    async def comic18 (self, ctx, numbers) :
        await ctx.send (f"https://18comic.vip/album/{numbers}/")

    @nextcord.slash_command()
    async def book (self, ctx) :
        my_book = rd.randint(200000, 430000)
        await ctx.send (my_book)


    @nextcord.slash_command()
    async def hentai_lobby(self, ctx):
        button1 = Button(label="nHentai", url="https://nhentai.to/")
        button2 = Button(label="Pixiv", url="https://www.pixiv.net/")
        button3 = Button(label="禁漫天堂", url="https://18comic.vip/albums?o=mr")
        button4 = Button(label="e-Hentai", url="https://e-hentai.org/")
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        await ctx.send("<:nhentai_icon:1018583382055202856>                  <:pixiv_icon:1018583380339720323>            <:18comic_icon:1018584112606499067>                 <:ehentai_icon:1018583378599100508> ", view=view)


def setup(bot):
    bot.add_cog(URL(bot))