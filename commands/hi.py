from discord.ext import commands
import discord

class Hi(commands.Cog):
    """ diz oi para o usuário """
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command( name= "oi",help="te da oi de volta")
    async def play_music(self,ctx):
        name = ctx.author.name
        resposta = "olá" + name
        await ctx.send(resposta)  

def setup(bot):
    bot.add_cog(Hi(bot))


