from flask import Flask, render_template, request
from decouple import config
import requests
app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"


@app.route('/')
def hello():
    return "Hello world"

@app.route('/write')
def write():
    return render_template('write.html') 

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')


if __name__==("__main__"):
    app.run(debug=True)