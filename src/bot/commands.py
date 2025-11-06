from discord.ext import commands
import bot.logger as logger

@commands.command()
async def ola(ctx):
    await ctx.reply("Olá, Tudo bem?")
    logger.log(f"Comando .ola usado por {ctx.author}", padding=2)
