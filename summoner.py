import os
import requests

class Summoner:
    def __init__(self, id, account_id, puuid, name, summoner_level):
        self.id=id
        self.account_id=account_id
        self.puuid=puuid
        self.name=name
        self.summoner_level=summoner_level
        
    def get_match_history(self):
        # gets env variable for riot API key
        api_key_value=os.environ.get('RIOT_API_KEY')
        api_key_header={"X-Riot-Token": api_key_value}
        
        # API call which is cast into a list
        match_list=list(requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{self.puuid}/ids', headers=api_key_header).json)
        return match_list
        
        