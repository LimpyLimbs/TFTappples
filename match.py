import os
import requests
# from summoner import Summoner

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
        self.participants_list=self.match_info['metadata']['participants']
        # self.parse_match_info()
        
    # def parse_match_info(self):
    #     self.participants_list=self.match_info['metadata']['participants']
    #     self.get_participant_names()
        
    # def get_participant_names(self):
    #     for participant in self.participants_list:
    #         summoner_object=requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{participant}', headers=self.api_key_header).json()
    #         summoner=Summoner(summoner_object['id'], summoner_object['accountId'], summoner_object['puuid'], summoner_object['name'], summoner_object['summonerLevel'])
    #         self.participant_names.append(summoner.name)