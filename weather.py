import os
import requests

# Pega a chave da API do GitHub Secrets
API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY", "São Paulo")

if not API_KEY:
    print("Erro: API_KEY não encontrada! Defina um secret no GitHub.")
    exit(1)

# Chama a API OpenWeather para obter a previsão do tempo
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=pt"
response = requests.get(url)

if response.status_code != 200:
    print("Erro ao obter dados da API.")
    exit(1)

data = response.json()
weather = data["weather"][0]["description"]
temp = data["main"]["temp"]

print(f"Previsão do tempo para {CITY}: {weather}, {temp}°C")

# Se estiver chovendo, avisa
if "chuva" in weather.lower():
    print("☔ Leve um guarda-chuva!")
else:
    print("🌞 O tempo está bom!")
