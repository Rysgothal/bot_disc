from bot.core import create_bot
from bot.utils import get_env_variable
from bot.logger import log

def main():
    log("Iniciando o bot...", 0)
    token = get_env_variable("DISCORD_TOKEN")

    try:
      bot = create_bot()
      bot.run(token)
    except Exception as e:
       print("Abra o log para mais detalhes.")
       log(f"Erro ao iniciar o bot: {e}")

if __name__ == "__main__":
    main()