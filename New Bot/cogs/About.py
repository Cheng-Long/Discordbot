import nextcord
from nextcord.ext import commands, tasks
from nextcord.ui import Button, View
import asyncio
import time

class About(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command(description="(UNFINISHED)")
    async def editmessage(self, ctx, times):
        message = await ctx.send("test")
        times = int(times)
        for time in range(times):
            for x in range(4):
                await asyncio.sleep(0.1)
                if x == 0 :
                    icon ="\\"
                if x == 1 :
                    icon ='|'
                if x == 2 :
                    icon ='/'
                if x == 3 :
                    icon ='-'
                await message.edit(content = icon)
            
        
        
    


def setup(bot):
    bot.add_cog(About(bot))