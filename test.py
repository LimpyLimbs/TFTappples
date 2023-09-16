from summoner import Summoner
import os
import requests

api_key_value=os.environ.get('RIOT_API_KEY')
api_key_header={"X-Riot-Token": api_key_value}

# API call
summoner_name='dpei'
summoner_data=requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner_name}', headers=api_key_header).json()
print(summoner_data)
id=summoner_data['id']
ranked_data_list=requests.get(f'https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/{id}', headers=api_key_header)

print(ranked_data_list)
print(ranked_data_list.json())
print(type(ranked_data_list))
