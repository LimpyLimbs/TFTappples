import requests

api_key = {"X-Riot-Token": "RGAPI-a9e57d33-69c8-4510-89c5-71f41da082a3"}
summoner_name = 'mikhailgorbachev'
puuid = 'YiJ23jmOudAh4eBCAvYoGfVbfCcQgYfsJTbMGjAJ15xDGKmVlbR2j56xoHa4_WNyAnSEjUPRbOrjaw'
match_id = 'NA1_4726917536'

response = requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner_name}', headers=api_key).json()
print(response)
response = requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids', headers=api_key).json()
print(response)
response = requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/{match_id}', headers=api_key).json()
print(response)