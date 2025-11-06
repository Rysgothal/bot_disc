from load_env_variables import get_env_variable
import model.bot as bot_module

def main():
  bot = bot_module.Bot(token=get_env_variable("DISCORD_TOKEN"))
  bot.run()

if __name__ == '__main__':
  main()