import os
import requests

class Match:
    def __init__(self, match_id):
        self.match_id=match_id
        self.match_info={}
        self.participants_list=[]
        self.participant_names=[]
        self.api_key_value=os.environ.get('RIOT_API_KEY')
        self.api_key_header={"X-Riot-Token": self.api_key_value}
        self.get_match_info()
        
    def get_match_info(self):
        self.match_info=requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/{self.match_id}', headers=self.api_key_header).json()
        # self.participants_list=self.match_info['metadata']['participants']
        self.parse_match_info()
        
    def parse_match_info(self):
        self.participants_list=self.match_info['metadata']['participants']
        self.get_participant_names()
        
    def get_participant_names(self):
        from summoner import Summoner
        for participant in self.participants_list:
            summoner_data=requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{participant}', headers=self.api_key_header)
            status_code=str(summoner_data)
            
            if status_code == '<Response [200]>':
                summoner_data=summoner_data.json()
                summoner=Summoner(summoner_data['id'], summoner_data['accountId'], summoner_data['puuid'], summoner_data['name'], summoner_data['summonerLevel'])
                self.participant_names.append(summoner.name)