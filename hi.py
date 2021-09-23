from discord.ext import commands
from discord

class Hi(commands.Cog):
    """ diz oi para o usuário """
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        await self.bot.process_commands(message)
def setup(bot):
    bot.add_cog(Hi(bot))


