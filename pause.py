from discord.ext import commands
from discord.ext.commands import bot


class Play(commands.Cog):
    """ Play music to the user with a link""""
    
    def __init__(self, bot):
        self.bot = bot
 
def setup(bot):
    bot.add_cog(Play(bot))


