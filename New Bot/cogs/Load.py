from logging import exception
from unicodedata import category
import nextcord
from nextcord.ext import commands



class Load(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command(description="重新載入插件[插件ID]")
    async def load(self, ctx, filename):
        try :
            self.bot.load_extension(f'cogs.{filename}')
            await ctx.send("Loaded")
        except Exception as error :
            await ctx.send(error)

    @nextcord.slash_command(description="取消載入插件[插件ID]")
    async def unload(self, ctx, filename):
        try :
            self.bot.unload_extension(f'cogs.{filename}')
            await ctx.send("Unloaded")
        except Exception as error :
            await ctx.send(error)

    @nextcord.slash_command(description="插件重新整理[插件ID]")
    async def reload(self, ctx, filename):
        try :
            self.bot.reload_extension(f'cogs.{filename}')
            await ctx.send("Reloaded")
        except Exception as error :
            await ctx.send(error)


def setup(bot):
    bot.add_cog(Load(bot))