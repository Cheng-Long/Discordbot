import nextcord
from nextcord.ui import Button, View
from nextcord.ext import commands
import json
import random

with open("gift.json","r") as hentai :
        hentaidata = json.load(hentai)

nnum = random.choice(hentaidata["HentaiNumbers"])

url = f"https://nhentai.net/g/{nnum}"

class Giftbox(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot
    
    @nextcord.slash_command()
    async def giftbox(self,ctx):  #Hnetai random
        button = Button(label="Open This", style=nextcord.ButtonStyle.blurple)

        async def button_callback(interaction):
            interaction.response.defer()
            await interaction.response.edit_message(content = url , view = None)

        button.callback = button_callback

        view = View()
        view.add_item(button)
        await ctx.send("🎁", view = view)




def setup(bot):
    bot.add_cog(Giftbox(bot))