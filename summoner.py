import os
import requests

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
        from match import Match
        # API call for a list of match IDs
        match_list=requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{self.puuid}/ids?start=0&count=2', headers=self.api_key_header).json()
        
        match_history=[]
        for match_id in match_list:
            match=Match(match_id)
            match_history.append(match)
        return match_history
    
    def get_summoner_rank(self):
        # for some reason riot returns a list with only one dictionary in it (maybe cause doubleup?)
        ranked_data_list=requests.get(f'https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/{self.id}', headers=self.api_key_header).json()
        
        # checks if list is empty (list returns empty if summoner is unranked)
        if len(ranked_data_list):
            ranked_data=ranked_data_list[0]
            tier=ranked_data['tier']
            rank=ranked_data['rank']
            league_points=ranked_data['leaguePoints']
            summoner_rank=f'{tier} {rank} {league_points}LP'
            if tier == 'CHALLENGER' or tier == 'GRANDMASTER' or tier == 'MASTER':
                summoner_rank=f'{tier} {league_points}LP'
            
            top_4s=ranked_data['wins']
            bot_4s=ranked_data['losses']
            total_games=top_4s + bot_4s
            top_4_percentage=round((top_4s/total_games) * 100)
            bot_4_percentage=round((bot_4s/total_games) * 100)
            summoner_stats={'summoner_rank':summoner_rank, 'wins':top_4s, 'losses':bot_4s, 'total_games':total_games, 'top_4_percentage':top_4_percentage, 'bot_4_percentage':bot_4_percentage}
            return summoner_stats
        else :
            return 'Unranked'