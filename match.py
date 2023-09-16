import os
import requests

class Match:
    def __init__(self, match_id):
        self.match_id=match_id
        self.api_key_value=os.environ.get('RIOT_API_KEY')
        self.api_key_header={"X-Riot-Token": self.api_key_value}