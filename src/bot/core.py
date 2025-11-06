import discord
from discord.ext import commands
import bot.commands as custom_commands
import bot.logger as logger

def create_bot():
    logger.log("Criando o bot...", 1)
    bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
    logger.log("Bot criado com sucesso.", 1)

    logger.log("Adicionando comandos personalizados...", 1)
    bot.add_command(custom_commands.ola)
    logger.log("Comandos personalizados adicionados.", 1)

    return bot