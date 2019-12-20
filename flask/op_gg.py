from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/opgg')
def opgg():

    userName = request.args.get('userName')
    url = f"https://www.op.gg/summoner/userName={userName}"

    req = requests.get(url).text
    data = BeautifulSoup(req, 'html.parser')

    tier = data.select_one('#SummonerLayoutContent div.TierRank').text
    win = data.select_one('#SummonerLayoutContent span.wins').text
    lose = data.select_one('#SummonerLayoutContent .losses').text
    return render_template('opgg.html', userName = userName, url = url, tier = tier, win = win[0:3], lose = lose[0:3] )

if __name__ == "__main__":
    app.run(debug=True)