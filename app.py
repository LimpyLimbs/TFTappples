from flask import Flask, redirect, url_for, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search') 
def search():  
    # request.args.get('sn') takes the query from index.html search bar and uses that as a variable
    # the query is redirected to the 'summoner' function and passes the 'query' variable to 'summonername' 
    query=request.args.get('sn')
    return redirect(url_for('summoner', summonername=query))

@app.route('/<summonername>')
def summoner(summonername):
    api_key={"X-Riot-Token": "RGAPI-a9c4d526-c250-4004-8d76-fd1228a9ffb9"}
    summonerdata=requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}', headers=api_key)
    statuscode=str(summonerdata)
    puuid=summonerdata.json().get('puuid')
    
    matchlist_json=requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids', headers=api_key)
    matchlist=list(matchlist_json.json())
    print(type(matchlist))
    singlematch=requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/{matchlist[0]}', headers=api_key)
    
    if statuscode == '<Response [200]>':
        return render_template('summonername.html', summonername=summonerdata.json().get('name'), summonerdata=summonerdata.json(), matchlist=matchlist, singlematch=singlematch.json())
    else :
        return redirect(url_for('searcherror', summonername=summonername))

@app.route('/searcherror/<summonername>')
def searcherror(summonername):
    return render_template('searcherror.html', name=summonername)

@app.route('/augments')
def augments():
    return render_template('augments.html')

@app.route('/comps')
def comps():
    return render_template('comps.html')

@app.route('/items')
def items():
    return render_template('items.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)