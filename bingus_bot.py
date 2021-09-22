import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"estou pronto Estou conectado como {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance (error,MissingRequiredArgument):
       await ctx.send("Por favor, envie todos os argumentos.")  
    elif isinstance(error,CommandNotFound):
       await ctx.send("O comando não existe!")  
    else:
        raise error


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command( name= "play" and "p")
async def play_music(ctx):
    name = ctx.author.name
    resposta = "olá" + name
    await ctx.send(resposta)    





    


bot.run("ODg5NTE5MDkwODMyNjU4NTE0.YUibNQ.JXwy3a7Fpb4f9e1KJC5abJSKPIw")
