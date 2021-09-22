import discord
from discord.ext import commands
from decouple import config 
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"estou pronto Estou conectado como {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance (error,MissingRequiredArgument):
       await ctx.send("Por favor, envie todos os argumentos. Digite help para ver todos os comandos")  
    elif isinstance(error,CommandNotFound):
       await ctx.send("O comando não existe!Digite help para ver todos os comandos")  
    else:
        raise error


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command( name= "play" and "p",help="Toca uma musica com um link")
async def play_music(ctx):
    name = ctx.author.name
    resposta = "olá" + name
    await ctx.send(resposta)    





    

TOKEN = config("TOKEN")
bot.run(TOK)
