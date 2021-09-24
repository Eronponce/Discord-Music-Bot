from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


class Manager(commands.Cog):
    """ Gerencia o bot """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"EU SOU UM TESTE. ME CHAMO {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(
                "Favor enviar todos os Argumentos. Digite !help para ver os parâmetros de cada comando"
            )
        elif isinstance(error, CommandNotFound):
            await ctx.send(
                "O comando não existe. Digite !help para ver todos os comandos"
            )
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))