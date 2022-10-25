from unicodedata import category
import nextcord
from nextcord.ext import commands
import json

with open("setting.json", "r") as setting :
    data = json.load(setting)

class Broadcast(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        parent_channel = data["parent_channel"]
        url = message.content
        child_channel = data["child_channel"]
        if message.author !=self.bot.user :
            if message.channel.id == parent_channel :
                if message.content.startswith("https://nhentai"):
                    for several in child_channel :
                        child_channel = await self.bot.fetch_channel(several)
                        await child_channel.send(url)

def setup(bot):
    bot.add_cog(Broadcast(bot))