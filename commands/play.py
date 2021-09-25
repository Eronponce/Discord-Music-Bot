import discord
from discord.ext import commands



class Play(commands.Cog):
    """ Play music to the user with a link as usual"""
    
    def __init__(self, bot):
        self.bot = bot
 
    @commands.command( name= "play" and "p",help="Toca uma musica com um link")
    async def play_music(self,ctx):
        await ctx.send("em desenvolvimento")  

def setup(bot):
    bot.add_cog(Play(bot))


