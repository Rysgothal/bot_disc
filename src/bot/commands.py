from discord.ext import commands
import bot.logger as logger

@commands.command()
async def ola(ctx):
    await ctx.reply("Olá, Tudo bem?")
    logger.log(f"Comando .ola usado", ctx, padding=2)

@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")
    logger.log(f"Comando .ping usado", ctx, padding=2)
