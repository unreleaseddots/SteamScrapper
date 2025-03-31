import requests, json, os, cryptography.fernet

#pegando a chave da steam //remove dps nao deixa isso publico
API_KEY = input ("Insert your api key\n")
USERNAME = input ("insert your url username, NOT YOUR STEAM NAME!\n")

#verifica se o input do username ja e um "STEAMID64"
try:
    float(USERNAME)
    STEAMID64 = USERNAME

except ValueError:
    #como a steam nao permite a busca direta por nomes tem que converter para steambase64 entao o codigo abaixo pega o "USERNAME" e converte para "STEAMID64" usando a propria api
    vanity_url = f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={API_KEY}&vanityurl={USERNAME}"
    response = requests.get(vanity_url)
    data = response.json()

    #verifica se a resposta "data" e diferente de um (no caso 0) caso seja 0 ele vai retornar erro, caso seja 1 e ele ache ele vai continuar o codigo
    if data["response"]["success"] !=1:
        print("Profile not found.")
        exit()

    STEAMID64 = data["response"]["steamid"]
try:
    #pega url da api da steam e insere seus dados
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={STEAMID64}&format=json&include_appinfo=1"

#pega a resposta 'response' da url da api da steam e escreve em um json chamado response
    response = requests.get(url)
    data = response.json()

#dentro do arquivo response ele pega e da um 'get' procurando a parte 'games'
    games = data ['response'].get('games', [])

#caso encontre ele ira printar usando o print abaixo
    print(f"Games Found: {len(games)}")
    print ("-" * 40)

#a cada 'game' dentro de games ele ira dar um print no nome do jogo
    for game in games:
        print(game['name'])
except Exception as e:
    print(f"Api error: {e}")
