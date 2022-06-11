import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    print(1)


@bot.command()
async def test(ctx):
    await ctx.send("hi")
    
    
bot.run("OTMyNjM4MjQ3NTcyNjExMDcy.G6IJM3.gRzTpUe8PQ0D58SXJJNRwzAPAHEnDSuLDkk4ZM")
