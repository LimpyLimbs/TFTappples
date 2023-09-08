from flask import Flask, redirect, url_for, render_template, request
import requests
# url_for and redirect redirect users to other webpages

app = Flask(__name__)

# @app.route('/') is what the user will navigate to using a URL
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search') 
def search():  
    # request.args.get('sn') takes the query from index.html search bar and uses that as a variable
    # the query is redirected to the 'summoner' function and passes the 'query' variable to 'summonername' 
    query = request.args.get('sn')
    # this function will need to handle errors
    return redirect(url_for('summoner', summonername=query))

@app.route('/<summonername>')
def summoner(summonername):
    api_key = {"X-Riot-Token": "RGAPI-a9c4d526-c250-4004-8d76-fd1228a9ffb9"}
    puuid = 'YiJ23jmOudAh4eBCAvYoGfVbfCcQgYfsJTbMGjAJ15xDGKmVlbR2j56xoHa4_WNyAnSEjUPRbOrjaw'
    response = requests.get(f'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}', headers=api_key).json()
    print(type(response))
    return render_template('summonername.html', content=response, name=summonername)

@app.route('/augments')
def augments():
    return render_template('augments.html')

@app.route('/comps')
def comps():
    return render_template('comps.html')

@app.route('/items')
def items():
    return render_template('items.html')

# this is what actually starts the server
if __name__ == '__main__':
    app.run(debug=True)