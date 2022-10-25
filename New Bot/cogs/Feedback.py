import nextcord
from nextcord.ext import commands

class Feedback(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot
    
    @nextcord.slash_command()
    async def feedback(self,user:nextcord.Member):
        await user.message_send("HI")
        



def setup(bot):
    bot.add_cog(Feedback(bot))