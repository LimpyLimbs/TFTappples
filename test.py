from summoner import Summoner
import os
import requests

def create_summoner(summoner_data):
    print(summoner_data)
    print(summoner_data['id'])
    summoner=Summoner(id=summoner_data['id'], account_id=summoner_data['accountId'], puuid=summoner_data['puuid'], name=summoner_data['name'], summoner_level=summoner_data['summonerLevel'])
    return summoner

# gets env variable for riot API key
api_key_value=os.environ.get('RIOT_API_KEY')
api_key_header={"X-Riot-Token": api_key_value}

# API call
summoner_name='south1737'
summoner_data=requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner_name}', headers=api_key_header)
status_code=str(summoner_data)
    
# instantiates summoner object
summoner_object=create_summoner(summoner_data.json())
print(summoner_object.id)


