from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    data = request.args.get('keyword')
    return render_template('pong.html', data = data)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

if __name__ == ("__main__"):
    app.run(debug=True)