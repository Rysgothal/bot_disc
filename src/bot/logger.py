import os
from datetime import datetime
from discord.ext import commands

def get_author_name(ctx: commands.Context):
  if ctx and hasattr(ctx, "author") and ctx.author:
    return ctx.author.name
  
  return "System"

def get_guild_name(ctx: commands.Context):
  if ctx and hasattr(ctx, "guild") and ctx.guild:
    return ctx.guild.name
  
  return "System"

def log(message, ctx: commands.Context=None, padding=0):
  dir_default = "Logs"
  if not os.path.exists(dir_default):
    os.makedirs(dir_default)
  
  filename = f"{get_guild_name(ctx)}.log"
  
  dir_file = os.path.join(dir_default, filename)
  timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

  log_message = f"[{timestamp}] ({get_author_name(ctx)}) "
  log_message += " " * (padding * 2) + message
  
  with open(dir_file, "a", encoding="utf-8") as arquivo:
    arquivo.write(log_message + "\n")