import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View



class OthersCommands(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command()
    async def help (self, ctx) :
        embed=nextcord.Embed(title="Slash command use only", description="> / [command name] [value] \n \n > It will show all of command and how to use that", color=0xb3fffe)
        embed.set_author(name="Help")
        embed.set_footer(text="by. ChengLong")
        await ctx.send(embed=embed)

    @nextcord.slash_command()
    async def purge (self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send("message deleted", ephemeral=True)

   


def setup(bot):
    bot.add_cog(OthersCommands(bot))