from discord.ext import commands
from discord.ext.commands import bot


class Bass(commands.Cog):
    """ Troca a o bass da musica """
    
    def __init__(self, bot):
        self.bot = bot
 
def setup(bot):
    bot.add_cog(Bass(bot))


