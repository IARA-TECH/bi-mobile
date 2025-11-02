import requests
from os import getenv
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis do .env
load_dotenv()

# Faz login e obtém o token
def gerar_token():
    try:
        payload = {
            "username": getenv("USERNAME_IARA"),
            "password": getenv("PASSWORD_IARA")
        }

        response = requests.post(
            getenv("URL_ENDPOINT"),
            data=payload  # envia como x-www-form-urlencoded
        )

        if response.status_code != 200:
            print(f"❌ Falha ao obter token: {response.status_code}")
            print(response.text)
            return

        data = response.json()
        token = data.get("access_token")

        if not token:
            print("❌ Token não encontrado na resposta da API.")
            print(data)
            return

        # Salva o token no arquivo TXT
        with open("C:\\Users\\guilhermepinheiro-ie\\OneDrive - Instituto Germinare\\Área de Trabalho\\2º Ano\\Tech\\BI\\Inter\\bi-mobile\\token.txt", "w", encoding="utf-8") as f:
            f.write(token)

        print("✅ Token gerado e salvo com sucesso!")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    gerar_token()