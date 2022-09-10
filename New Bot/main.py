import os
import nextcord
from nextcord.ext import commands


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

TOKEN = os.getenv("Token")
bot.run (TOKEN)