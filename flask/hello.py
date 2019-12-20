from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello!'

@app.route('/fstring')
def fstring():
    fstring = "김진우"
    # print("제 이름은" + {fstring} )
    return f"제 이름은 {fstring} 입니다."

@app.route('/hi')
def hi():
    name = "김진우"
    return render_template('hi.html', html_name = name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>/')
def cube(num):
    cube_num = num**3
    return render_template('cube.html', cube = cube_num, num = num)

@app.route('/dinner')
def dinner():
    menu = ['삼각김밥', '컵라면', '스테이크', '마라탕', '훠궈']
    dinner = random.choice(menu)
    menu_img = {'삼각김밥' : 'https://ppss.kr/wp-content/uploads/2017/12/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-7-1.jpg', 
                '컵라면' : 'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile25.uf.tistory.com%2Fimage%2F99A7CB355A4B982A0381DD',
                '스테이크' : 'https://storage.googleapis.com/cbmpress/tlife/2516102861_p7dfIhVr_8e508001931cf358ba2484f9b22057d49acbf5f3.png',
                '마라탕' : 'http://img1.tmon.kr/cdn3/deals/2019/05/24/2099407062/original_2099407062_front_935dc_1558688230production.jpg',
                '훠궈' : 'https://funshop.akamaized.net//products/0000062075/vs_image800.jpg?1576736400'}
    img_url = menu_img[dinner]
    return render_template('dinner.html', dinner = dinner, img_url = img_url)

@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', movies = movies)


if __name__ == "__main__":
    app.run(debug=True)