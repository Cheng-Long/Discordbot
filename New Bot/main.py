from audioop import add
import os
import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import json

# with open("gift.json", "r") as hentai :
#     hentaidata = json.load(hentai)

TESTING_GUILD_ID = 691167211548704808  #Test server ID

intents = nextcord.Intents.default()  #commands starts witf
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

initial_extensions = []

for fn in os.listdir("./cogs"):  #Load cogs
    if fn.endswith(".py"):
        initial_extensions.append("cogs." + fn[:-3])

if __name__ == "__main__" :  
    for extension in initial_extensions :
        bot.load_extension(extension)
        print (extension)

@bot.event 
async def on_ready () :
    print (">> Bot is online <<")

@bot.slash_command()
async def giftbox(ctx):  #Hnetai random
    button = Button(label="Open This", style=nextcord.ButtonStyle.blurple)

    async def button_callback(interaction):
        interaction.response.defer()
        await interaction.response.edit_message(content = "**EMPTY INSIDE :P**", view = None)

    button.callback = button_callback

    view = View()
    view.add_item(button)
    await ctx.send("🎁", view = view)

TOKEN = os.getenv("Token")
bot.run (TOKEN)