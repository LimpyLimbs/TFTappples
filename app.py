from flask import Flask, redirect, url_for, render_template, request
import requests
import os
from summoner import Summoner

app = Flask(__name__)

def create_summoner(summoner_data):
    summoner=Summoner(summoner_data['id'], summoner_data['accountId'], summoner_data['puuid'], summoner_data['name'], summoner_data['summonerLevel'])
    return summoner

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search') 
def search():  
    # request.args.get('sn') takes the query from index.html search bar and uses that as a variable
    # the query is redirected to the 'summoner' function and passes the 'query' variable to 'summonername' 
    query=request.args.get('sn')
    return redirect(url_for('summoner', summoner_name=query))

@app.route('/<summoner_name>')
def summoner(summoner_name):
    # gets env variable for riot API key
    api_key_value=os.environ.get('RIOT_API_KEY')
    api_key_header={"X-Riot-Token": api_key_value}
    
    # API call
    summoner_data=requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner_name}', headers=api_key_header)
    status_code=str(summoner_data)
    
    if status_code == '<Response [200]>':
        summoner_object=create_summoner(summoner_data.json())
        return render_template('summonername.html', summoner_name=summoner_object.name, summoner_data=summoner_object.summoner_level, summoner_match_history=match_history)
    else :
        return redirect(url_for('searcherror', summoner_name=summoner_name))

@app.route('/searcherror/<summoner_name>')
def searcherror(summoner_name):
    return render_template('searcherror.html', name=summoner_name)

@app.route('/augments')
def augments():
    return render_template('augments.html')

@app.route('/items')
def items():
    return render_template('items.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)