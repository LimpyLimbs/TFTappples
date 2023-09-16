import os
import requests
from match import Match

class Summoner:
    def __init__(self, id, account_id, puuid, name, summoner_level):
        self.id=id
        self.account_id=account_id
        self.puuid=puuid
        self.name=name
        self.summoner_level=summoner_level
        self.api_key_value=os.environ.get('RIOT_API_KEY')
        self.api_key_header={"X-Riot-Token": self.api_key_value}

    def get_match_history(self):
        # API call for a list of match IDs
        match_list=requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{self.puuid}/ids', headers=self.api_key_header).json()
        
        match_history=[]
        for match_id in match_list:
            match=Match(match_id)
            match_history.append(match)
        return match_history
    
    def get_summoner_rank(self):
        ranked_data=requests.get(f'https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/{self.id}', headers=self.api_key_header).json()
        print(ranked_data)