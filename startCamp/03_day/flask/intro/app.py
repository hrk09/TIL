from flask import Flask, render_template 
import datetime
import random
app = Flask(__name__)

@app.route('/') # / 를 endpoint라고 함
def hello():
    # return 'Hello Hailey!'
    return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return 'Hello ssafy'


@app.route('/dday')
def dday():
    today = datetime.datetime.now
    b_day = datetime.datetime(2019, 1, 23)
    td = b_day - today
    return f'{td.days} 일 남았습니다!'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''
@app.route('/greeting/ziont')
def greeting_ziont():
    return '반갑습니다! ziont 님'

# Variable Routing
@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다 {name} 님!'
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:num>')
def cube(num):
    num ** 3
    # return f'{num}의 3 제곱은 {num ** 3} 입니다.'
    return render_template('cube.html', html_num=num)
    # result = num ** 3
    # return render_template('cube.html', num=num, result=result)

# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['김밥', '떡볶이', '라면']
    order = random.sample(menu, people)
    return str(order)


@app.route('/movie')
def movie():
    movies = ['스파이더맨', '엔드게임', '기생충', '알라딘']
    return render_template('movie.html', movies=movies)


if  __name__ == '__main__':
    app.run(debug=True)
