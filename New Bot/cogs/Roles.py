from unicodedata import category
import nextcord
from nextcord.ext import commands



class Roles(commands.Cog) :

    def __init__(self , bot) :
        self.bot = bot

    @nextcord.slash_command(description="新增身分組[名稱],[顏色(hex色碼)]")
    async def create_role (self, ctx, name, color:str):
        guild = ctx.guild
        user = ctx.user
        colour=int(color , 16)
        permissions=nextcord.Permissions(permissions=2386026304)
            
        await guild.create_role(name=name,colour=colour,permissions=permissions)

        role = nextcord.utils.get(ctx.guild.roles , name=name)

        await ctx.send(f" **{name}** Role Had Successfully Created")

        await user.add_roles (role)

    @nextcord.slash_command(description="給予身分組(指定)")
    async def role_given(self, ctx, rolename):
        user = ctx.user
        role = nextcord.utils.get(ctx.guild.roles , name=rolename)
        await user.add_roles(role)
        await ctx.send(f" **{rolename}** Role Had Successfully Given")


def setup(bot):
    bot.add_cog(Roles(bot))