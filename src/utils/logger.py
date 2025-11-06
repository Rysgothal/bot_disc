import os
from datetime import datetime

def log(mensagem):
  pasta_logs = "Logs"

  if not os.path.exists(pasta_logs):
    os.makedirs(pasta_logs)
  
  
  data_atual = datetime.now().strftime("%d-%m-%Y")
  nome_arquivo = f"{data_atual}.log"
  caminho_arquivo = os.path.join(pasta_logs, nome_arquivo)
  
  # Adicionar timestamp à mensagem
  timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  mensagem_completa = f"[{timestamp}]: {mensagem}\n"
  
  # Escrever mensagem no arquivo
  with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write(mensagem_completa)