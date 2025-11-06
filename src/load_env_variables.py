import os
from dotenv import load_dotenv
from pathlib import Path

loaded_env = False

def load_env():
  global loaded_env
  dotenv_path = Path(__file__).resolve().parents[3] / 'env_list' / 'bot_disc' / '.env'

  loaded_env = load_dotenv(dotenv_path=dotenv_path)

def get_env_variable(variable_name):
  global loaded_env

  if not loaded_env:
    load_env()

  return os.getenv(variable_name)