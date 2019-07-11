from flask import Flask, render_template, request # 사용자의 요청 확인 가능
import requests
app = Flask(__name__)


@app.route('/') # / => root
def index():
    return 'Hello world'


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', name=name)  


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'Pong! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/op_gg_ow')
def op_gg_ow():
    return render_template('op_gg_ow.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # input의 name을 text로 보냈으므로
    # Ascii art API 활용하여 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)


if  __name__ == '__main__':
    app.run(debug=True)
