from datetime import MAXYEAR
from tkinter.messagebox import NO
from unicodedata import category
import nextcord
from nextcord.ui import Button, View
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
    async def role_given(self, ctx, rolename:nextcord.Role):
        user = ctx.user
        role = nextcord.utils.get(ctx.guild.roles , name=rolename)
        await user.add_roles(role)
        await ctx.send(f" **{rolename}** Role Had Successfully Given")

    @nextcord.slash_command(description="(UNFINISHED)")
    async def button1(self, ctx):
        button = Button(label="Click Me!", style=nextcord.ButtonStyle.blurple)

        async def button_callback(interaction):
            await interaction.response.send_message("Hello")

        button.callback = button_callback

        view = View()
        view.add_item(button)
        await ctx.send("Hi", view=view)

    @nextcord.slash_command(description="(UNFINISHED)")
    async def button2(self, ctx):
        button = Button(label="Click Me!", style=nextcord.ButtonStyle.danger)

        async def button_callback(interaction):
            await interaction.response.edit_message(content="Hello", view=None)

        button.callback = button_callback

        view = View()
        view.add_item(button)
        await ctx.send("Hi", view=view)

    @nextcord.slash_command(description="(UNFINISHED)")
    async def button3(self, ctx):
        button = Button(label="Click Me!", style=nextcord.ButtonStyle.gray)

        async def button_callback(interaction):
            await interaction.response.send_message("Hello", ephemeral = True)
            button.disabled = True

        button.callback = button_callback
        
        view = View()
        view.add_item(button)
        await ctx.send("Hi", view=view)



def setup(bot):
    bot.add_cog(Roles(bot))


