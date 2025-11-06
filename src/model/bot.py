import discord
from discord.ext import commands
from utils.logger import log

class Bot(commands.Bot):
    def __init__(self, token: str):
        self.token = token
        super().__init__(command_prefix='.', intents=discord.Intents.all())
        
    def run(self):
        try:
            self.add_commands()
            super().run(self.token)
        except Exception as e:
            log(f"Erro ao iniciar o bot: {e}")

    def add_commands(self):
        self.add_command(self.hello)

    async def on_ready(self):
        log('Bot iniciado com sucesso')
        
    @commands.command(name='ola')
    async def hello(self, ctx):
        log(f'Comando .ola executado por: {ctx.author}')
        await ctx.reply('Olá! Eu sou um bot Discord.')

    